from flask import Flask, request, jsonify
import grpc
import dictionary_pb2
import dictionary_pb2_grpc

app = Flask(__name__)

# Configuração do cliente gRPC
def get_grpc_client():
    channel = grpc.insecure_channel('localhost:50051')
    return dictionary_pb2_grpc.DictionaryServiceStub(channel)

@app.route('/add_word', methods=['POST'])
def add_word():
    data = request.json
    word = data.get('word')
    meaning = data.get('meaning')

    if not word or not meaning:
        return jsonify({"error": "Both 'word' and 'meaning' are required"}), 400

    grpc_client = get_grpc_client()
    response = grpc_client.AddWord(dictionary_pb2.WordEntry(word=word, meaning=meaning))
    return jsonify({"success": response.success, "message": response.message})

@app.route('/get_word/<word>', methods=['GET'])
def get_word(word):
    grpc_client = get_grpc_client()
    response = grpc_client.GetWord(dictionary_pb2.WordRequest(word=word))

    if response.found:
        return jsonify({"word": response.word, "meaning": response.meaning})
    else:
        return jsonify({"error": f"Word '{word}' not found"}), 404

if __name__ == "__main__":
    app.run(port=5000)
