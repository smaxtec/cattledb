FROM google/cloud-sdk:450.0.0-alpine

RUN gcloud components install beta bigtable cbt

RUN addgroup -S cbt && adduser -S cbt -G cbt -h /home/cbt
USER cbt
WORKDIR /home/cbt

RUN echo -e 'project = local\ninstance = local\n' > /home/cbt/.cbtrc

EXPOSE 8080
ENTRYPOINT gcloud beta emulators bigtable start --host-port=0.0.0.0:8080
