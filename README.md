# docker-sample
experiment on docker with multiple microservice (coffee, bean and report)

use current dir docker-compose up command

<hr>

```
version: "2"
services:
  # 1 DB service and 3 microservices
  db:
    image: postgres
    restart: always
    ports:
      - "5431:5432"
    environment:
      POSTGRES_PASSWORD: admin@123*
      POSTGRES_USER: postgres
      POSTGRES_DB: postgres
    volumes:
      - ./init.sql:/docker-entrypoint-initdb.d/1-init.sql #to import init.sql file into postgres
      - dbvolume:/var/lib/postgresql/data #external volume data so that we don't loose any data after docker restart
  web:
    build: ./coffee
    ports:
      - "8081:5000"
    volumes:
      - ./coffee:/code
    depends_on:
      - bean
      - report
  bean:
    image: bean_web
    # Setting db in ENV instead of hardcoding it on .py file
    environment:
      DB_PASS: admin@123*
      DB_USER: postgres
      DB: postgres
      DB_HOST: db # network host, bean service will look for links as a reference
    links:
      - db #pointing db link with service name 'db'
    build: ./bean
    ports:
      - "8082:4000"
    volumes:
      - ./bean:/code
  report:
    image: report_web
    build: ./report
    ports:
      - "8083:5000"
    volumes:
      - ./report:/code
volumes:
  dbvolume:
```
