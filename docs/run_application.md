# Building and Running the FastAPI UV Playground Application
___

This guide will walk you through the steps to build a Docker image for the FastAPI UV Playground application and run the container.

### Prerequisites
- [Docker installed on your machine](https://docs.docker.com/engine/install/ubuntu/)
- [Access to the project repository](https://github.com/Miguel-mmf/fastapi-uv-playground)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Miguel-mmf/fastapi-uv-playground.git
   cd fastapi-uv-playground
   ```

2. **Build the Docker Image**
   Use the following command to build the Docker image. This command will create an image named `fastapi-uv-playground-app`.
   ```bash
   docker build -t 'fastapi-uv-playground-app' .
   ```

3. **List Docker Images**
   After building the image, you can list all Docker images to verify that the image was created successfully.
   ```bash
   docker images
   ```

4. **Run the Docker Container**
   Use the following command to run the Docker container. This command will start the container and map port 8000 on your host to port 8000 on the container.
   ```bash
   docker run -it --name fastapi-uv-playground -p 8000:8000 fastapi-uv-playground-app:latest
   ```

5. **Access the Application**
   Open your web browser and navigate to `http://localhost:8000` to access the FastAPI UV Playground application.

### Additional Information
- To stop the container, use the following command:
  ```bash
  docker stop fastapi-uv-playground
  ```

- To remove the container, use the following command:
  ```bash
  docker rm fastapi-uv-playground
  ```

---
Ref.: [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/#installing-python-in-musl-based-images)
