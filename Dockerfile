FROM python:3.6

WORKDIR /usr/src/app

COPY . .
RUN pip install .
RUN chmod u+rx entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["api"]