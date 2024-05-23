import logging
from flask import Flask, request, jsonify
import boto3
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

app = Flask(__name__)

# Inicialização do cliente boto3 para DynamoDB
def initialize_dynamodb():
    dynamodb = boto3.resource('dynamodb', region_name='sa-east-1')
    return dynamodb.Table('MatheusTable')

table = initialize_dynamodb()

# Constantes para respostas
HEALTHY_STATUS = 'Healthy'
UNHEALTHY_STATUS = 'Unhealthy'

@app.route('/health', methods=['GET'])
def health():
    health = {'DynamoDB': HEALTHY_STATUS}
    try:
        table.table_status
    except Exception as e:
        logger.error(f"An error occurred with DynamoDB: {e}")
        health['DynamoDB'] = f'{UNHEALTHY_STATUS} - {e}'
    
    if all(status == HEALTHY_STATUS for status in health.values()):
        status = HEALTHY_STATUS
        return jsonify({'message': status, 'details': health}), 200
    else:
        status = UNHEALTHY_STATUS
        return jsonify({'message': status, 'details': health}), 500

@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        user_data = request.json
        response = table.put_item(Item={'UserID': user_data['user_id'], 'Name':  user_data['name']})
        return jsonify({'message': 'User criado com sucesso', 'response': response}), 200
    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
        return jsonify({'erro': str(e)}), 500

@app.route('/get_user', methods=['GET'])
def get_user():
    try:
        user_id = request.args.get('user_id')
        response = table.get_item(Key={'UserID': user_id})
        return jsonify({'message': 'User encontrado com sucesso', 'user_data': response.get('Item', {})}), 200
    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
        return jsonify({'erro': str(e)}), 500

@app.route('/update_user', methods=['PUT'])
def update_user():
    try:
        user_data = request.json
        response = table.put_item(Item={'UserID': user_data['user_id'], 'Name':  user_data['name']})
        return jsonify({'message': 'User atualizado com sucesso', 'response': response}), 200
    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
        return jsonify({'erro': str(e)}), 500

@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    try:
        response = table.delete_item(Key={'UserID': request.args.get('user_id')})
        return jsonify({'message': 'User deletado com sucesso', 'response': response}), 200
    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
        return jsonify({'erro': str(e)}), 500
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
