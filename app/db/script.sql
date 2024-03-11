-- Coloque scripts iniciais aqui
CREATE TABLE IF NOT EXISTS cliente (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    limite INT,
    saldo INT
);

CREATE TABLE IF NOT EXISTS transacao (
    id INT PRIMARY KEY,
    valor INT,
    tipo VARCHAR(10),
    descricao VARCHAR(255)
    cliente INT,
    realizada_em DATETIME
);

DO $$
BEGIN
  INSERT INTO cliente (nome, limite)
  VALUES
    ('o barato sai caro', 1000 * 100),
    ('zan corp ltda', 800 * 100),
    ('les cruders', 10000 * 100),
    ('padaria joia de cocaia', 100000 * 100),
    ('kid mais', 5000 * 100);
END; $$