Delta Proxy
===========
An HTTP proxy cache server that uses delta encoding to reduce data usage.

It is designed for Venezuelan internet connections which are extremely slow (think dial-up, but worse), the ideal setup would consist of a 2 level hierarchy. One "root" server running on a cloud instance with a good connection and a local instance of the proxy, which in turn connects to the root server (effectively using it as a second-layer proxy) to fetch resources and deltas.

This is an experiment, results will be documented thoroughly as I will 

## Limitations
+ In order to prevent polluting our cache with dynamic resources, our proxy server will only store in cache the following file types: Javascript, CSS

## Features
+ No dependencies
+ Gracefully recover incomplete requests in the background