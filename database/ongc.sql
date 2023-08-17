-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: ongc
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `f_name` varchar(50) DEFAULT NULL,
  `id` varchar(45) NOT NULL,
  `pwd` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('Admin','admin','admin','Admin'),('Delevery','delevery','delevery','Delevery'),('master','master','master','Master_Creation'),('Orders','Orders','Orders','Orders'),('qr_code','qr_code','qr_code','qr_code'),('return','return','return','Return'),('Stock','stock','stock','Stock'),('transport','transport','transport','Transport');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_creation`
--

DROP TABLE IF EXISTS `master_creation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_creation` (
  `Phone` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `date` varchar(15) NOT NULL,
  `quantity` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_creation`
--

LOCK TABLES `master_creation` WRITE;
/*!40000 ALTER TABLE `master_creation` DISABLE KEYS */;
INSERT INTO `master_creation` VALUES (12345678,'Satish Munde','30/03/23',500),(770961707,'sujit maske','03/04/23',50),(1234567890,'sujit maskes','03/04/23',50),(1234567563,'gopal sir','10/04/23',100);
/*!40000 ALTER TABLE `master_creation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `Order_id` int NOT NULL,
  `Tank_id` int NOT NULL,
  `Customer_Name` varchar(45) DEFAULT NULL,
  `Number` int DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Tank_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (10001,20000,'Satish Munde',845989607,'05/05/23','A'),(10002,20001,'Saurabh Maske',845989607,'05/05/23','B'),(10002,20002,'Mangesh Tambade',123456789,'05/05/23','C'),(10003,20003,'Sujit Maske',123456789,'05/05/23','D');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qr_code_details`
--

DROP TABLE IF EXISTS `qr_code_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `qr_code_details` (
  `QR_Code_ID` int NOT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`QR_Code_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qr_code_details`
--

LOCK TABLES `qr_code_details` WRITE;
/*!40000 ALTER TABLE `qr_code_details` DISABLE KEYS */;
INSERT INTO `qr_code_details` VALUES (20000,'30:03:2023','Printed'),(20001,'08:45:10','Printed'),(20002,'08:45:22','Printed'),(20003,'08:45:32','Printed');
/*!40000 ALTER TABLE `qr_code_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tank_details`
--

DROP TABLE IF EXISTS `tank_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tank_details` (
  `QR_Code_ID` int NOT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Time` varchar(45) DEFAULT NULL,
  `Status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`QR_Code_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tank_details`
--

LOCK TABLES `tank_details` WRITE;
/*!40000 ALTER TABLE `tank_details` DISABLE KEYS */;
INSERT INTO `tank_details` VALUES (20000,'05:05:23','20:59:19','In Transist'),(20001,'05:05:23','08:57:14','Stock'),(20002,'05:05:23','08:57:28','Stock'),(20003,'05:05:23','08:57:55','Stock');
/*!40000 ALTER TABLE `tank_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-06 10:15:03
