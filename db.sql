-- Run these 2 commands before using APIs to make sure tables exist

CREATE TABLE tasks
(
    id               SERIAL PRIMARY KEY,
    task_name        VARCHAR(255) NOT NULL,
    task_description TEXT,
    task_status      VARCHAR(50),
    task_tag         VARCHAR(50),
    created_by       VARCHAR(255) NOT NULL,
    created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE users
(
    id       SERIAL PRIMARY KEY,
    email    VARCHAR(50) NOT NULL,
    password VARCHAR(100)
);
