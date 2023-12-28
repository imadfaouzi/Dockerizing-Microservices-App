const express = require('express');
const Eureka = require('eureka-js-client').Eureka;

const app = express();
const port = 3000;

// Your Eureka server's host and port
const eurekaHost = 'localhost';
const eurekaPort = 8761;

// Create a Eureka client
const client = new Eureka({
    instance: {
        app: 'customer-service-nodejs',
        hostName: 'localhost',
        ipAddr: '127.0.0.1',
        port: {
            '$': port,
            '@enabled': 'true',
        },
        vipAddress: 'customer-service-nodejs', // Update this line
        dataCenterInfo: {
            '@class': 'com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo',
            name: 'MyOwn',
        },
    },
    eureka: {
        host: eurekaHost,
        port: eurekaPort,
        servicePath: '/eureka/apps/',
    },
});

// Start the Eureka client
client.start(error => {
    console.error(error || 'Eureka client started');
});

// Define a simple API endpoint
app.get('/test', (req, res) => {
    console.log("here I'am")
    res.send('Hello from your Node.js service!');
});

// Start the Node.js server
app.listen(port, () => {
    console.log(`Node.js service listening at http://localhost:${port}`);
});
