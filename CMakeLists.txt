cmake_minimum_required(VERSION 3.15)

project(MyGrpcProject)

# Localização de gRPC e Protobuf
find_package(gRPC CONFIG REQUIRED)
find_package(Protobuf CONFIG REQUIRED)

add_executable(server server.cpp service.pb.cc service.grpc.pb.cc)
target_link_libraries(server gRPC::grpc++ protobuf::libprotobuf)
