# CREATING DATABASES
CREATE DATABASE Petshop;
USE Petshop;

CREATE TABLE Pets(
ID int,
Name varchar(50),
Price decimal(5,2), 
Species varchar(50),
Owner_ID int,
PRIMARY KEY (ID));

CREATE TABLE Owners(
Owner_ID int,
Name varchar(50),
Contact_Number varchar(15),
PRIMARY KEY (Owner_ID));

INSERT INTO Pets(ID, Name, Price, Species, Owner_ID)
VALUES (1,'Natasha', 49.99, 'Cat', 1),
(2,'Peggy', 12.45, 'Parrot', 3),
(3,'Freddie', 25.64, 'Fish', 2),
(4,'Peter', 35.00, 'Rabbit', 2),
(5,'Flopsy', 15.00, 'Rabbit', 4),
(6,'Socks', 36.25, 'Cat', 1),
(7,'Peter', 9.99, 'Parrot', 3);

INSERT INTO Owners(Owner_ID, Name, Contact_Number)
VALUES (1, 'Roisin Wherry', '07854123456'),
(2, 'Danny Smith', '07492690884'),
(3, 'Sam Brown', ''),
(4, 'Laura Low', '07432976401'),
(5, 'Brad Bowden', '');

UPDATE Pets 
SET  Pets.Name = 'Sox'
WHERE Pets.ID = 6;

DELETE FROM Pets
WHERE ID = 2;

ALTER TABLE Pets
ADD FOREIGN KEY (Owner_ID)
REFERENCES Owners(Owner_ID);

SELECT Pets.Price, Pets.Species, Owners.Name, Owners.Contact_Number 
FROM Pets INNER JOIN Owners
ON Pets.Owner_ID = Owners.Owner_ID;

UPDATE Pets
SET Pets.Owner_ID = NULL
WHERE Pets.Name = 'Freddie';

SELECT Pets.Price, Pets.Species, Owners.Name, Owners.Contact_Number 
FROM Pets LEFT JOIN Owners
ON Pets.Owner_ID = Owners.Owner_ID;


