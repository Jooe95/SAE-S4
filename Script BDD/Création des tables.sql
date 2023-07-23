DROP TABLE IF EXISTS title_basics CASCADE;
DROP TABLE IF EXISTS title_akas CASCADE;
DROP TABLE IF EXISTS title_crew CASCADE;
DROP TABLE IF EXISTS title_episode CASCADE;
DROP TABLE IF EXISTS title_ratings CASCADE;
DROP TABLE IF EXISTS name_basics CASCADE;
DROP TABLE IF EXISTS title_principals CASCADE;



CREATE TABLE title_basics(
        tconst text primary key,
        titleType text,
        primaryTitle text,
        originalTitle text,
        isAdult boolean,
        startYear smallint check(startYear>0),
        endYear smallint check(endYear>=startYear),
        runtimeMinutes int check(runtimeMinutes>=0),
        genres text[]
);

CREATE TABLE title_akas(
    titleId text references title_basics,
    ordering int,
    PRIMARY KEY(titleId, ordering),
    title text not null, 
    region text,
    language text, 
    types text[], 
    attributes text[],
    isOriginalTitle boolean
);

CREATE TABLE title_crew(
    tconst text primary key references title_basics,
    directors text[],
    writers text[]
);

CREATE TABLE title_episode(
    tconst text primary key references title_basics,
    parentTconst text not null references title_basics,
    seasonNumber smallint check(seasonNumber>=0), 
    episodeNumber int check(episodeNumber>=0)
);

CREATE TABLE title_ratings(
    tconst text primary key references title_basics,
    averageRating float check(averageRating>=0 AND averageRating<=10),
    numVotes int check(numVotes>=0)
);

CREATE TABLE name_basics(
    nconst text primary key,
    primaryName text not null,
    birthYear smallint check(birthYear>0),
    deathYear smallint, --check(deathYear is null OR deathYear>=birthYear),
    primaryProfession text[],
    knownForTitles text[]
);

CREATE TABLE title_principals(
    tconst text references title_basics,
    ordering int,
    nconst text references name_basics,
    primary key(tconst, ordering, nconst),
    category text,
    job text,
    character text
);