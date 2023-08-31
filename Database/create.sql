CREATE DATABASE debate_tournaments;

CREATE TABLE tournament 
(tournament_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
 tournament_name VARCHAR(255), 
 circuit VARCHAR(255), 
 startdate DATE,
 enddate DATE,
 states_or_provinces VARCHAR(255),
 country VARCHAR(255),
 bid_level ENUM('None', 'Finals', 'Semifinals', 'Quarters', 'Octofinals'),
 has_JV boolean,
 has_Varsity boolean,
 allows_independents boolean
);