CREATE TABLE "__EFMigrationsHistory" (
"MigrationId" TEXT NOT NULL CONSTRAINT "PK___EFMigrationsHistory" PRIMARY KEY,
"ProductVersion" TEXT NOT NULL
);

CREATE TABLE "Articles" (
"id" SERIAL PRIMARY KEY NOT NULL,
"photoLink" TEXT,
"discription" TEXT,
"BTN" TEXT
);

CREATE TABLE "Consumption" (
"userId" INTEGER NOT NULL,
"time" TEXT,
"date" DATE,
"consume" REAL,
PRIMARY KEY ("userId")
);

CREATE TABLE "Products" (
"id" SERIAL PRIMARY KEY NOT NULL,
"photo" TEXT,
"discription" TEXT NOT NULL,
"link" TEXT
);

CREATE TABLE "StationInfo" (
"SolarPanelType" TEXT,
"InverterType" TEXT,
"BatteryType" TEXT,
"SolarPanelCount" INTEGER,
"Space" REAL,
"Location" TEXT,
"InstallationDate" DATE,
"InstallationType" TEXT,
"TotalAmpereNeed" REAL,
"BatteryCapacty" REAL,
"BattteryCount" INTEGER,
"BatteryDate" DATE,
"SystemId" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"UserId" INTEGER,
"EnergyNeed" REAL,
FOREIGN KEY ("UserId") REFERENCES "Users" ("id")
);

CREATE TABLE "StationStatus" (
"Time" TIME,
"Date" DATE,
"SystemId" INTEGER,
"TempDegree" INTEGER,
"CloudStatus" TEXT,
"WindSpeed" INTEGER,
"WindDirection" TEXT,
"SunPostion" TEXT,
"SolarAngel" TEXT,
"EnergyProduction" REAL,
"EnergyConsumption" REAL,
"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
FOREIGN KEY ("SystemId") REFERENCES "StationInfo" ("SystemId")
);

CREATE TABLE "Users" (
"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"Name" TEXT,
"Email" TEXT,
"Password" TEXT,
"Phone" TEXT,
"Address" TEXT
);