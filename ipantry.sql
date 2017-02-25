BEGIN;
/* This table list all the possible ingredients available
	 amongst all recipes
*/
CREATE TABLE store
(
	id								bigserial		NOT NULL,
	name							char(100)		NOT NULL UNIQUE,
	PRIMARY KEY (id)
);

/* This table hold all the ingredients that the user has in
	 their kitchen
*/
CREATE TABLE shopping_cart
(
	id								bigserial		NOT NULL,
	name							char(100)		NOT NULL UNIQUE,
	expiration_date		timestamp,
	PRIMARY KEY (id),
	FOREIGN KEY (name) REFERENCES store(name)
);

/* This table contains all the recipes available. This is
	 generated using a web crawler
CREATE TABLE recipe_book
(

);
*/
COMMIT;
