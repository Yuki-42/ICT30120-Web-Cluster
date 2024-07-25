CREATE TABLE contact_requests
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name       TEXT NOT NULL,
    email      TEXT NOT NULL,
    phone      TEXT,
    subject    TEXT NOT NULL,
    message    TEXT NOT NULL,
    state      TEXT NOT NULL,
    contact_method TEXT NOT NULL
);

CREATE TABLE images
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    name        TEXT NOT NULL,
    path        TEXT NOT NULL,
    description TEXT NOT NULL
);