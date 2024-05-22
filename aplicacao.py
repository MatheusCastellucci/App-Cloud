import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Inicializa o DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='sa-east-1')
table = dynamodb.Table('MatheusTable')

# Configura o logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

@app.route('/health', methods=['GET'])
def health():
    health_status = {'DynamoDB': 'Healthy'}
    try:
        table.table_status
    except NoCredentialsError:
        logger.error("Credenciais não disponíveis")
        health_status['DynamoDB'] = 'Degraded - No credentials'
    except PartialCredentialsError:
        logger.error("Credenciais incompletas")
        health_status['DynamoDB'] = 'Degraded - Incomplete credentials'
    except Exception as e:
        logger.error(f"Ocorreu um erro com o DynamoDB: {e}")
        health_status['DynamoDB'] = f'Unhealthy - {e}' 
    overall_status = 'Healthy' if all(status == 'Healthy' for status in health_status.values()) else 'Unhealthy'
    return jsonify({'message': overall_status, 'details': health_status}), 200 if overall_status == 'Healthy' else 500

@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        user_data = request.json
        if not user_data.get('user_id') or not user_data.get('name'):
            return jsonify({'error': '"user_id" e "name" são campos obrigatórios'}), 400
        item = {
            'user_id': user_data['user_id'],
            'name': user_data['name'],
        }
        if 'user_id' in table.get_item(Key={'user_id': user_data['user_id']}).get('Item', {}):
            return jsonify({'error': 'Usuário já existe, poste em /update_user para atualizar um usuário.'}), 400
        response = table.put_item(Item=item)
        return jsonify({'message': 'Usuário adicionado com sucesso', 'response': response}), 200
    except NoCredentialsError:
        logger.error("Credenciais não disponíveis")
        return jsonify({'error': 'Credenciais não disponíveis'}), 500
    except PartialCredentialsError:
        logger.error("Credenciais incompletas")
        return jsonify({'error': 'Credenciais incompletas'}), 500
    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/get_user', methods=['GET'])
def get_user():
    try:
        user_id = request.args.get('user_id')
        if not user_id:
            return jsonify({'error': 'user_id é um campo obrigatório'}), 400
        response = table.get_item(Key={'user_id': user_id})
        return jsonify({'message': 'Usuário recuperado com sucesso', 'user_data': response.get('Item', {})})
    except NoCredentialsError:
        logger.error("Credenciais não disponíveis")
        return jsonify({'error': 'Credenciais não disponíveis'}), 500
    except PartialCredentialsError:
        logger.error("Credenciais incompletas")
        return jsonify({'error': 'Credenciais incompletas'}), 500
    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    try:
        user_id = request.args.get('user_id')
        if not user_id:
            return jsonify({'error': 'user_id é um campo obrigatório'}), 400
        response = table.delete_item(Key={'user_id': user_id})
        return jsonify({'message': 'Usuário excluído com sucesso', 'response': response}), 200
    except NoCredentialsError:
        logger.error("Credenciais não disponíveis")
        return jsonify({'error': 'Credenciais não disponíveis'}), 500
    except PartialCredentialsError:
        logger.error("Credenciais incompletas")
        return jsonify({'error': 'Credenciais incompletas'}), 500
    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/update_user', methods=['PUT'])
def update_user():
    try:
        user_data = request.json
        if not user_data.get('user_id'):
            return jsonify({'error': 'user_id é um campo obrigatório'}), 400
        item = {
            'user_id': user_data['user_id'],
            'name': user_data.get('name'),
        }
        response = table.put_item(Item=item)
        return jsonify({'message': 'Usuário atualizado com sucesso', 'response': response}), 200
    except NoCredentialsError:
        logger.error("Credenciais não disponíveis")
        return jsonify({'error': 'Credenciais não disponíveis'}), 500
    except PartialCredentialsError:
        logger.error("Credenciais incompletas")
        return jsonify({'error': 'Credenciais incompletas'}), 500
    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
