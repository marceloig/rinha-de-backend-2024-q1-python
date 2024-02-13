CREATE TABLE IF NOT EXISTS "clientes" (
                                          "id" serial PRIMARY KEY NOT NULL,
                                          "nome" text NOT NULL,
                                          "saldo" integer DEFAULT 0 NOT NULL,
                                          "limite" integer DEFAULT 0 NOT NULL
);

CREATE INDEX clientes_id_idx ON "clientes" USING HASH(id);

CREATE TABLE IF NOT EXISTS "transacoes" (
                                            "id" serial PRIMARY KEY NOT NULL,
                                            "cliente_id" integer NOT NULL ,
                                            "valor" integer NOT NULL,
                                            "tipo" char(1) NOT NULL,
                                            "descricao" varchar(10) NOT NULL,
                                            "realizada_em" timestamp NOT NULL DEFAULT now()
);

CREATE INDEX transacoes_id_idx ON "transacoes" USING HASH(id);
CREATE INDEX transacoes_cliente_id_idx ON "transacoes" USING HASH(cliente_id);

DO $$
    BEGIN
        INSERT INTO clientes (nome, limite)
        VALUES
            ('o barato sai caro', 1000 * 100),
            ('zan corp ltda', 800 * 100),
            ('les cruders', 10000 * 100),
            ('padaria joia de cocaia', 100000 * 100),
            ('kid mais', 5000 * 100);
    END; $$