cmake_minimum_required(VERSION 3.13)

# Set the project name and C++ standard
project(grpc_server_project)
set(CMAKE_CXX_STANDARD 17)

# Specify the gRPC and Protobuf installation paths
list(APPEND CMAKE_PREFIX_PATH "/usr/local/grpc" "/usr/local/protobuf")

# Find gRPC and Protobuf packages
find_package(Protobuf REQUIRED)
find_package(gRPC CONFIG REQUIRED)

# Include directories
include_directories(${Protobuf_INCLUDE_DIRS})
include_directories(${gRPC_INCLUDE_DIRS})

# Generate Protobuf and gRPC sources from the .proto file
set(PROTO_FILE service.proto)
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS ${PROTO_FILE})
grpc_generate_cpp(GRPC_SRCS GRPC_HDRS ${PROTO_FILE})

# Add the executable target
add_executable(server server.cpp ${PROTO_SRCS} ${GRPC_SRCS})

# Link libraries
target_link_libraries(server gRPC::grpc++ ${Protobuf_LIBRARIES})
