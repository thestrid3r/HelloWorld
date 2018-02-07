# README #

* A Flask web app running in docker using redis to count the view and print hostname of container

* To build and run the server after cloning the repo use:
```
docker-compose up --build -d
        or
docker-compose up --build
```

* dockerhub image
```
https://hub.docker.com/r/thestrider/helloworld/
```
* To get the aws-region use this

```
curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone | sed 's/\(.*\)[a-z]/\1/'
```
