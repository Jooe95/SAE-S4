CREATE TEMP TABLE temp_title_akas (
    titleid VARCHAR(10000),
    ordering INTEGER,
    title VARCHAR(10000),
    region VARCHAR(10000),
    language VARCHAR(10000),
    types VARCHAR(10000),
    attributes VARCHAR(10000),
    isoriginaltitle BOOLEAN
);

COPY temp_title_akas (titleid, ordering, title, region, language, types, attributes, isoriginaltitle)
FROM 'C:/Users/Admin/Desktop/bdd/TITLEA~1.TSV/data.tsv'
DELIMITER E'\t';

INSERT INTO title_akas (titleid, ordering, title, region, language, types, attributes, isoriginaltitle)
SELECT temp.titleid, temp.ordering, temp.title, temp.region, temp.language, temp.types, temp.attributes, temp.isoriginaltitle
FROM temp_title_akas temp
LEFT JOIN title_basics tb ON temp.titleid = tb.tconst
WHERE tb.tconst IS NOT NULL;