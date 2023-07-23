-- Créez une table temporaire "temp_title_principals" pour charger les données du fichier TSV
CREATE TEMP TABLE temp_title_principals (
    tconst VARCHAR(255),
    ordering INTEGER,
    nconst VARCHAR(255),
    category VARCHAR(500),
    job VARCHAR(1000),
    characters VARCHAR(10000)
);

COPY temp_title_principals (tconst, ordering, nconst, category, job, characters)
FROM 'C:/Users/Admin/Desktop/bdd/TITLEP~1.TSV/data.tsv'
WITH (DELIMITER E'\t', NULL '\\N', HEADER true);

DO $$
DECLARE
    temp_record RECORD;
BEGIN
    FOR temp_record IN (SELECT * FROM temp_title_principals)
    LOOP
        BEGIN
            INSERT INTO title_principals (tconst, ordering, nconst, category, job, characters)
            VALUES (temp_record.tconst, temp_record.ordering, temp_record.nconst, temp_record.category, temp_record.job, temp_record.characters);
        EXCEPTION
            WHEN foreign_key_violation THEN
                CONTINUE; -- Ignore les erreurs de clé étrangère et passe à l'enregistrement suivant
        END;
    END LOOP;
END $$;

SELECT COUNT(*) FROM title_principals;
