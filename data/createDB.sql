create table Regions (
    code_region INTEGER,
    nom_region TEXT,
    constraint pk_regions primary key (code_region)
);

create table Departements (
    code_departement TEXT,
    nom_departement TEXT,
    code_region INTEGER,
    zone_climatique TEXT  CHECK (zone_climatique IN ('H1','H2','H3','')),
    constraint pk_departements primary key (code_departement),
    constraint fk_region foreign key (code_region) references Regions(code_region)
);

create table Mesures (
    code_departement TEXT,
    date_mesure DATE,
    temperature_min_mesure FLOAT,
    temperature_max_mesure FLOAT,
    temperature_moy_mesure FLOAT,
    constraint pk_mesures primary key (code_departement, date_mesure),
    constraint fk_mesures foreign key (code_departement) references Departements(code_departement)
);

--TODO Q4 Ajouter les créations des nouvelles tables
create table Communes (
    code INTEGER,
    nom TEXT,
    statut TEXT,
    altitude_moyenne INTEGER,
    population INTEGER,
    superficie INTEGER,
    code_canton INTEGER,
    code_arrondissement INTEGER,
    constraint pk_commune primary key (code)
);

create table Isolation (
  poste TEXT CHECK (poste IN ('COMBLES PERDUES','ITI','ITE','RAMPANTS','SARKING','TOITURE TERRASSE','PLANCHER BAS')),
  isolant TEXT CHECK (isolant in ('AUTRES','LAINE VEGETALE','LAINE MINERALE','PLASTIQUES')),
  epaisseur INT,
  surface FLOAT
);

create table Chauffage (
  energie_avant_travaux TEXT CHECK (energie_avant_travaux IN ('AUTRES','BOIS','ELECTRICITE','FIOUL','GAZ')),
  energie_installee TEXT CHECK (energie_installee IN  ('AUTRES','BOIS','ELECTRICITE','FIOUL','GAZ')),
  generateur TEXT CHECK (generateur IN ('AUTRES','CHAUDIERE','INSERT','PAC','POELE','RADIATEUR')),
  type_chaudiere TEXT CHECK (type_chaudiere IN ('STANDART','AIR-EAU','A CONDENSATION','AUTRES','AIR-AIR','GEOTHERMIE','HPE'))
);

create table Photovoltaique (
  puissance_installee INT,
  types_panneaux TEXT CHECK (types_panneaux IN ('MONOCRISTALLIN','POLYCRISTALLIN'))
);

create table Travaux (
   id INTEGER,
   cout_tot_ht FLOAT,
   cout_induit_ht FLOAT,
   annee INTEGER,
   anne_cons_logement TEXT,
   type_logement TEXT,
   constraint pk_travaux primary key (id)
);
--constraint fk_travaux foreign key (id) references Regions(code_region)
