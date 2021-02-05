# Interface monitor task

1. Write a small program using a language of your choice that prints every (configurable through env var) 30 seconds the following data in json format: RX/TX packets, bytes and errors of the default network interface.
 
2. Create Dockerfile for the program.

3. Set up a Gitlab CI configuration with the following tasks:

  - build  docker image with your program;
  - push docker image to gitlab docker registry;
  - provide a manifest that deploys the docker image to k8s cluster;

The deployment stage should be fired on a new git tag creation only. The git tag must be semver compliant.

Bonus points:
Expose the collected data from task /1/ through a web API.
Provide a k8s manifest that exposes the API only in the k8s cluster


**Important points:**<br>
1. Code simplicity and readability
1. Clean and well-organized code
1. Architecture
1. Linters, docs, etc. are a bonus