CREATE TABLE IF NOT EXISTS public.anime
(
    anime_id integer NOT NULL,
    name character varying(200),
    genre character varying(200),
    type character varying(200),
    rating real,
    members integer,
    episodes character varying(200),
    CONSTRAINT anime_pkey PRIMARY KEY (anime_id)
)