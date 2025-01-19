FROM ubuntu:22.04

# Set environment variables for non-interactive installations
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    unzip \
    autoconf \
    libtool \
    pkg-config \
    libprotobuf-dev \
    protobuf-compiler \
    && apt-get clean

# Install Protobuf and gRPC
WORKDIR /tmp
RUN git clone --recurse-submodules -b v1.66.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc \
    && cd grpc \
    && mkdir -p cmake/build \
    && cd cmake/build \
    && cmake ../.. -DCMAKE_INSTALL_PREFIX=/usr/local -DgRPC_INSTALL=ON -DgRPC_BUILD_TESTS=OFF -DCMAKE_CXX_STANDARD=17 -DBUILD_DEPS=ON \
    && make -j$(nproc) \
    && make install \
    && ldconfig

# Set up your project directory
WORKDIR /app

# Copy the project files into the image
COPY CMakeLists.txt .
COPY server.cpp .
COPY service.proto .

# Build the server during the Docker build process
RUN mkdir -p build \
    && cd build \
    && cmake .. -D Protobuf_PROTOC_EXECUTABLE=/usr/bin/protoc \
    && make -j$(nproc)

# Expose the port
EXPOSE 8080

# Command to run the server
CMD ["./build/server"]
