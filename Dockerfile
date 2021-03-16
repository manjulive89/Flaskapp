FROM centos

RUN  yum install -y python-pip \
      && pip install flask

COPY . /

EXPOSE 8081

CMD cd / && python blog.py
