import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='sa-east-1')
table = dynamodb.Table('MatheusTable')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@app.route('/health', methods=['GET'])
def health():
    health_status = {'DynamoDB': 'Healthy'}
    try:
        # Check if DynamoDB table is available
        table.table_status
    except NoCredentialsError:
        logger.error("Credentials not available")
        health_status['DynamoDB'] = 'Degraded - No credentials'
    except PartialCredentialsError:
        logger.error("Incomplete credentials")
        health_status['DynamoDB'] = 'Degraded - Incomplete credentials'
    except Exception as e:
        logger.error(f"An error occurred with DynamoDB: {e}")
        health_status['DynamoDB'] = f'Unhealthy - {e}'
    
    overall_status = 'Healthy' if all(status == 'Healthy' for status in health_status.values()) else 'Unhealthy'
    
    return jsonify({'message': overall_status, 'details': health_status}), 200 if overall_status == 'Healthy' else 500


@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        # Get data from the request
        user_data = request.json
        
        # Validate input
        if not user_data.get('user_id') or not user_data.get('name'):
            return jsonify({'error': 'user_id and name are required fields'}), 400
        
        # Ensure user_id is included in the item
        item = {
            'user_id': user_data['user_id'],
            'name': user_data['name'],
            # Include other attributes as necessary
        }
        
        if 'user_id' in table.get_item(Key={'user_id': user_data['user_id']}).get('Item', {}):
            return jsonify({'error': 'User already exists, post to /update_user to update an user.'}), 400
        # Save data to DynamoDB
        response = table.put_item(Item=item)
        
        return jsonify({'message': 'User added successfully', 'response': response}), 200
    except NoCredentialsError:
        logger.error("Credentials not available")
        return jsonify({'error': 'Credentials not available'}), 500
    except PartialCredentialsError:
        logger.error("Incomplete credentials")
        return jsonify({'error': 'Incomplete credentials'}), 500
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/get_user', methods=['GET'])
def get_user():
    try:
        # Get user_id from the request
        user_id = request.args.get('user_id')
        
        # Validate input
        if not user_id:
            return jsonify({'error': 'user_id is a required field'}), 400
        
        # Get user data from DynamoDB
        response = table.get_item(Key={'user_id': user_id})
        
        return jsonify({'message': 'User retrieved successfully', 'user_data': response.get('Item', {})})
    except NoCredentialsError:
        logger.error("Credentials not available")
        return jsonify({'error': 'Credentials not available'}), 500
    except PartialCredentialsError:
        logger.error("Incomplete credentials")
        return jsonify({'error': 'Incomplete credentials'}), 500
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    try:
        # Get user_id from the request
        user_id = request.args.get('user_id')
        
        # Validate input
        if not user_id:
            return jsonify({'error': 'user_id is a required field'}), 400
        
        # Delete user data from DynamoDB
        response = table.delete_item(Key={'user_id': user_id})
        
        return jsonify({'message': 'User deleted successfully', 'response': response}), 200
    except NoCredentialsError:
        logger.error("Credentials not available")
        return jsonify({'error': 'Credentials not available'}), 500
    except PartialCredentialsError:
        logger.error("Incomplete credentials")
        return jsonify({'error': 'Incomplete credentials'}), 500
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500
    

@app.route('/update_user', methods=['PUT'])
def update_user():
    try:
        # Get data from the request
        user_data = request.json
        
        # Validate input
        if not user_data.get('user_id'):
            return jsonify({'error': 'user_id is a required field'}), 400
        
        # Ensure user_id is included in the item
        item = {
            'user_id': user_data['user_id'],
            'name': user_data.get('name'),
            # Include other attributes as necessary
        }
        
        # Save data to DynamoDB
        response = table.put_item(Item=item)
        
        return jsonify({'message': 'User updated successfully', 'response': response}), 200
    except NoCredentialsError:
        logger.error("Credentials not available")
        return jsonify({'error': 'Credentials not available'}), 500
    except PartialCredentialsError:
        logger.error("Incomplete credentials")
        return jsonify({'error': 'Incomplete credentials'}), 500
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the app on HTTP
    app.run(host='0.0.0.0', port=80)
    
    # Run the app on HTTPS
    # app.run(host='0.0.0.0', port=443, ssl_context='adhoc')