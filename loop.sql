DECLARE
    author_name      author.name%TYPE;
    country    author.country%TYPE;
    ssulka    author.url%TYPE;


BEGIN

 DELETE FROM author;

    author_name := 'Author';
    country := 'country';
    ssulka := 'url';
    FOR i IN 1..10 LOOP
        INSERT INTO author (
            name,
            country,
            url
        ) VALUES (
            TRIM(author_name) || i,
            TRIM(country) || i,
            TRIM(ssulka)|| i
        );
    END LOOP;
END;