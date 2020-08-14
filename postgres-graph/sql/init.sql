CREATE TABLE graphs (
    id SERIAL PRIMARY KEY
);

CREATE TABLE edges (
    id SERIAL PRIMARY KEY,
    graph_id SERIAL,
    source BYTEA NOT NULL,
    target BYTEA NOT NULL,
    weight DOUBLE PRECISION DEFAULT 0.0,
    CONSTRAINT fk_graphs FOREIGN KEY(graph_id) REFERENCES graphs(id)
);