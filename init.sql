
SET TIMEZONE TO 'America/Sao_Paulo';

CREATE TABLE IF NOT EXISTS cep_location (
    cep varchar(10) NOT NULL,
    uf varchar(2) NOT NULL,
    localidade varchar(255) NOT NULL,
    logradouro varchar(255) NOT NULL,
    data_consulta TIMESTAMP,
    constraint "PKCepLocation" primary key ("cep")
);
