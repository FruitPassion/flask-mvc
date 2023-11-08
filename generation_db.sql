CREATE TABLE Compte(
   Id_Compte INT AUTO_INCREMENT,
   nom VARCHAR(50),
   date_creation DATE,
   hash TEXT,
   essaie_connexion VARCHAR(50),
   actif BOOLEAN,
   PRIMARY KEY(Id_Compte)
);

CREATE TABLE Photo(
   Id_Photo INT AUTO_INCREMENT,
   libellle VARCHAR(50),
   chemin VARCHAR(100),
   Id_Compte INT NOT NULL,
   PRIMARY KEY(Id_Photo),
   FOREIGN KEY(Id_Compte) REFERENCES Compte(Id_Compte)
);

CREATE TABLE Cour(
   Id_Cour INT AUTO_INCREMENT,
   libelle VARCHAR(50),
   code VARCHAR(5),
   PRIMARY KEY(Id_Cour)
);

CREATE TABLE ParticiperA(
   Id_Compte INT,
   Id_Cour INT,
   PRIMARY KEY(Id_Compte, Id_Cour),
   FOREIGN KEY(Id_Compte) REFERENCES Compte(Id_Compte),
   FOREIGN KEY(Id_Cour) REFERENCES Cour(Id_Cour)
);
