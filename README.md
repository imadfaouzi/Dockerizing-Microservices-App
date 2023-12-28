# Microservices Deployment with Docker Compose

This project demonstrates the deployment of microservices using Docker Compose. The microservices include a discovery service, a configuration service, a customer service, and a gateway service.

## Prerequisites
- Docker
- Docker Compose

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/imadfaouzi/Dockerizing-Microservices-App
cd Dockerizing-Microservices-App
```

### 2. Build and Run with Docker Compose

```bash
docker-compose up --build
```
This command will build and start the containers for the discovery service, configuration service, customer service, and gateway service.

### 3. Access the Services
   * Discovery Service: http://localhost:8761
* Config Service: http://localhost:9990
* Customer Service: http://localhost:8081
* Gateway Service: http://localhost:8888
###  4. Health Checks
   The health checks for each service are configured to ensure their proper functioning.

*  Discovery Service Health: http://localhost:8761/actuator/health
* Config Service Health: http://localhost:9990/actuator/health

### Cleanup
To stop and remove the containers, run the following command:
``` bash
 docker-compose down
```