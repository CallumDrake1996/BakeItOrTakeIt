-- MySQL dump 10.13  Distrib 8.1.0, for macos13.3 (x86_64)
--
-- Host: localhost    Database: MakeItOrTakeIt
-- ------------------------------------------------------
-- Server version	8.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Login`
--

DROP TABLE IF EXISTS `Login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Login` (
  `User_id` int NOT NULL AUTO_INCREMENT,
  `Email` varchar(30) DEFAULT NULL,
  `Username` varchar(30) DEFAULT NULL,
  `Password` varchar(15) DEFAULT NULL,
  `First_Name` varchar(45) DEFAULT NULL,
  `Last_Name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Login`
--

LOCK TABLES `Login` WRITE;
/*!40000 ALTER TABLE `Login` DISABLE KEYS */;
INSERT INTO `Login` VALUES (25,'3d@hotmail.com','3d@hotmail.com','123456','olivia','Rodrigo'),(26,'aaberg@hotmail.com','aaberg@hotmail.com','123456789','Ruby','Bell'),(27,'aardwolf@hotmail.com','aardwolf@hotmail.com','abecedary','Emily','Clarke'),(28,'aarhus@hotmail.com','aarhus@hotmail.com','abell','Grace','Holland'),(29,'abbey@hotmail.com','abbey@hotmail.com','abednego','Jessica','Smith'),(30,'abbieabbot@hotmail.com','abbieabbot@hotmail.com','abebi','Chloe','Bell'),(31,'abbottson@hotmail.com','abbottson@hotmail.com','abdullah','Sophie','Baxter'),(32,'notreal@sky.ip','admin','password','Admin','Admin'),(33,'mrjoker122@hotmail.co.uk','bob','pass','Bob','Marley'),(34,'george@hotmail.com','george@hotmail.com','abeyta','George','Sinclare'),(35,'klaster@hotmail.com','klaster@hotmail.com','abfarad','Kyle','House'),(36,'robert@hotmail.com','robert@hotmail.com','abie','Robert','Fuler'),(37,'sad@hotmail.com','sad@hotmail.com','@@','Sadie','Smith'),(38,'test1@hotmail.com','test1@hotmail.com','test1','Test','1'),(39,'test2@hotmail.com','test2@hotmail.com','test2','Test','2'),(40,'test3@hotmail.com','test3@hotmail.com','test3','Test','3'),(41,'test5@hotmail.com','test5@hotmail.com','test5','Test','5'),(42,'test6@hotmail.com','test6@hotmail.com','test6','Test','6'),(43,'test7@hotmail.com','test7@hotmail.com','test7','Test','7'),(44,'testtest@hotmail.com','testtest@hotmail.com','testtest','Test','Test'),(45,'yankees@hotmail.com','yankees@hotmail.com','xxxxxx','Yankee','Doodle'),(46,'zxcvbn@hotmail.com','zxcvbn@hotmail.com','dakota','John','Smith'),(47,'mrjoker122@hotmail.co.uk','mrjoker122@hotmail.co.uk','password','Mr','Joker'),(48,'t43797192@gmail.com','t43797192@gmail.com','admin','Bakeit','Takeit'),(49,'callum.drake@sky.uk','callum.drake@sky.uk','Password','callum','drake');
/*!40000 ALTER TABLE `Login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-30 19:37:59
