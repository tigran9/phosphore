##Database creation ###For psql

sudo su - postgres
psql > DROP DATABASE IF EXISTS gihub;
psql > CREATE DATABASE github;
psql > CREATE USER github_user WITH password 'password';
psql > GRANT ALL privileges ON DATABASE github TO github_user;