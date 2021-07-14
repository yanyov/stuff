-----
Python script - net_interface_monitor.py which will display RX/TX packets, 
bytes and errors of the default network interface.

This script is looking for two env variables:

- API_ENDPOINT - if this env var is set to 'y' the script will API endpoint on
port 5000 on all network interfaces. When you pass GET http request to 
<your_ip>:5000 you will get the network statistics for you default network 
adapter. If this var is not set the script will display this statistics to 
STDOUT.

- DURATION - the time interval in seconds between which the script will 
display the network statistics that he collects. By defult it's 30s.

The script will use python Flask to expose an API endpoint.

The script has three methods:

- get_default_iface_name_linux - this will return the default network adapter
on the system.

- net_interface_monitor - this will collect the network statistics for the
default network adapter.

- main - the main method that's the entry point for the script.

-----
.gitlab-ci.yml - the file that is used by GitLab Runner to manage your 
project's builds.
This will build a Docker image, will tag this image with the current build id
and put latest tag. It will push this newly created docker image to docker 
registry and will deploy this image to kubernetes.

-----
Dockerfile - instruction on how to build our docker image.

-----
deployment.yml - this is used to deploy the docker image to kubernetes cluster.
It will create deployment object and service.

-----
requirements.txt - here are required python modules for our python script.