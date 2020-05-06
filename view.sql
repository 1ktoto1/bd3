CREATE OR REPLACE VIEW countrylike AS
   SELECT 
   Country.country , 
   SUM(Map.rating) as sum_like 
    FROM country 
    JOIN author ON country.country = author.country 
    JOIN map ON map.author_name = author.name
    GROUP BY Country.country;
    

CREATE OR REPLACE VIEW gamemapparcent AS
    SELECT
    game.game,
    ROUND(COUNT(map.id)*100/t.total, 2) AS percent
        FROM map JOIN game ON map.game = game.game,
        (SELECT COUNT(map.id) AS total FROM map) t
        GROUP BY game.game, t.total;