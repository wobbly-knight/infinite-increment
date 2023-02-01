FROM ubuntu:18.04

ENV GITHUB_PAT=<classic github pat or fine grained pat>
ENV ORG=<NAME OF ORG IN GITHUB>

RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf \
        && cat /etc/resolv.conf

RUN apt-get update \
        && apt-get upgrade -y \
        && apt install -y \
            curl \
            jq \
            sudo \
            python3-pip

RUN pip3 install \
        pynacl \
        PyGithub \
        pyyaml \
        invoke


RUN useradd -ms /bin/bash runner \
        && usermod -aG sudo runner \
        && echo "runner ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

WORKDIR /home/runner

RUN mkdir /home/runner/actions-runner \
        && cd /home/runner/actions-runner

RUN curl -o actions-runner-linux-x64-2.301.1.tar.gz \
        -L https://github.com/actions/runner/releases/download/v2.301.1/actions-runner-linux-x64-2.301.1.tar.gz \
        && tar xzf ./actions-runner-linux-x64-2.301.1.tar.gz

RUN /home/runner/bin/installdependencies.sh \
        && chown -R runner:runner /home/runner

COPY scripts/ .
RUN chmod +x /home/runner/entrypoint.sh

RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf \
        && cat /etc/resolv.conf

USER runner

ENTRYPOINT ["/home/runner/entrypoint.sh"]
