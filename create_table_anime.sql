CREATE TABLE IF NOT EXISTS anime
(
    anime_id integer NOT NULL,
    name character varying(200),
    type character varying(200),
    rating real,
    members integer,
    episodes integer,
    CONSTRAINT anime_pkey PRIMARY KEY (anime_id)
);

CREATE TABLE IF NOT EXISTS anime_genre
(
    anime_id integer,
    genre_id integer
);

CREATE TABLE IF NOT EXISTS genre
(
    genre_id integer,
    genre_name character varying(200)
);