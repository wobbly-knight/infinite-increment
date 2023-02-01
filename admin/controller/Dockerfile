FROM ubuntu:18.04

ENV GITHUB_PAT=<classic github pat or fine grained pat>
ENV ORG=<NAME OF ORG IN GITHUB>

# Setting nameserver for DNS resolution
RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf \
        && cat /etc/resolv.conf

# Installing required packages
RUN apt-get update \
        && apt-get upgrade -y \
        && apt install -y \
            python3 \
            python3-pip

# Installing python package 'requests'
RUN pip3 install requests

# Setting working directory
WORKDIR /var/task

# Copying scripts to the working directory
COPY scripts/ .

# Making entrypoint script executable
RUN chmod +x entrypoint.sh

# Setting entrypoint to the build script
ENTRYPOINT ["/var/task/entrypoint.sh"]
