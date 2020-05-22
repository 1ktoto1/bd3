DECLARE
    country    author.country%TYPE;

BEGIN

 DELETE FROM author;

    country := 'country';
    FOR i IN 1..10 LOOP
        INSERT INTO country (
            country
        ) VALUES (
            TRIM(country) || i
        );
    END LOOP;
END;