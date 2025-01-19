#include <grpcpp/grpcpp.h>
#include "service.grpc.pb.h"
#include <unordered_map>
#include <string>
#include <mutex>

class DictionaryServiceImpl final : public dictionary::Dictionary::Service {
    std::unordered_map<std::string, std::string> dictionary_;
    std::mutex dictionary_mutex_;

public:
    grpc::Status AddWord(grpc::ServerContext* context, 
                         const dictionary::AddWordRequest* request,
                         dictionary::AddWordResponse* response) override {
        std::lock_guard<std::mutex> lock(dictionary_mutex_);
        const auto& word = request->word();
        const auto& definition = request->definition();

        if (dictionary_.find(word) != dictionary_.end()) {
            response->set_message("Word already exists!");
        } else {
            dictionary_[word] = definition;
            response->set_message("Word added successfully!");
        }
        return grpc::Status::OK;
    }

    grpc::Status ListWords(grpc::ServerContext* context, const service_pb2::ListWordsRequest* request, service_pb2::ListWordsResponse* response) override {
        // Aqui você deve acessar o banco de dados ou a estrutura onde as palavras estão armazenadas
        // Exemplo de palavras armazenadas
        std::vector<std::string> words = {"example", "test", "sample"};
        
        // Adicionando as palavras à resposta
        for (const auto& word : words) {
            service_pb2::Word* word_msg = response->add_words();
            word_msg->set_word(word);
        }
        
        return grpc::Status::OK;
    }
};

void RunServer() {
    std::string server_address("0.0.0.0:8080");
    DictionaryServiceImpl service;

    grpc::ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::unique_ptr<grpc::Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;
    server->Wait();
}

int main(int argc, char** argv) {
    RunServer();
    return 0;
}
