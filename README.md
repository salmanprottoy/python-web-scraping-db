# _Web Scraping_ #

A python script that scrapes data from the vrbo vacation rental service and stores it in a MySQL database.

## Prerequisite ##

- Python
- MySql

## Usage ##

- Create Table

``
CREATE TABLE `family_friendly_rentals` ( `id` INT NOT NULL AUTO_INCREMENT , `Title` VARCHAR(255) NOT NULL , `Location` VARCHAR(255) NOT NULL , `Sleeps` VARCHAR(255) NOT NULL , `Bedroom` VARCHAR(255) NOT NULL , `Bathroom` VARCHAR(255) NOT NULL , `Image1` VARCHAR(255) , `Image2` VARCHAR(255) , `Image3` VARCHAR(255) , `Price` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`, `Title`));
``

- Run script

```sh
python3 webScraping.py
```
