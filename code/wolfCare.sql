-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 06, 2022 at 04:19 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wolfCare`
--

-- ------------------------------------------------------

--
-- Table structure for table `appointment`
--

CREATE TABLE `appointment` (
	`appointmentid` int NOT NULL AUTO_INCREMENT,
	`userid` int NOT NULL,
	`doctorid` int NOT NULL,
	`hospitalid` int NOT NULL,
	`date` varchar(255) NOT NULL,
	`timeslot` varchar(255) NOT NULL,
	`isactive` varchar(255) NOT NULL,
	`lastmoddate` varchar(255) NOT NULL,
	PRIMARY KEY (`appointmentid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `appointment` AUTO_INCREMENT=5000;
--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`appointmentid`, `userid`, `doctorid`, `hospitalid`, `date`, `timeslot`, `isactive`, `lastmoddate`) VALUES
(5001,7001,1001,2001,'20221223','14:00:00','TRUE','20221129');

-- --------------------------------------------------------

--
-- Table structure for table `doctors`
--

CREATE TABLE `doctors` (
	`doctorid` int NOT NULL AUTO_INCREMENT,
	`firstname` varchar(255) NOT NULL,
	`lastname` varchar(255) NOT NULL,
	`primaryspecality` varchar(255) NOT NULL,
	`secondaryspecialty` varchar(255),
	`type` varchar(255) NOT NULL,
	`degree` varchar(255) NOT NULL,
	`phone` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL,
	`gender` varchar(255) NOT NULL,
	`yoe` varchar(255) NOT NULL,
	`approvalstatus` varchar(255) NOT NULL,
	`isactive` varchar(255) NOT NULL,
	`lastmoddate` varchar(255) NOT NULL,
	`userid` int,
	PRIMARY KEY (`doctorid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `doctors` AUTO_INCREMENT=1000;
--
-- Dumping data for table `doctors`
--

INSERT INTO `doctors` (`doctorid`, `firstname`, `lastname`, `primaryspecality`, `secondaryspecialty`, `type`, `degree`, `phone`, `email`, `gender`, `yoe`, `approvalstatus`, `isactive`, `lastmoddate`,`userid`) VALUES
(1001,'John','Doe','Dermatology','Family Medicine','Prescriber','MD','9192383821','johndoe@gmail.com','Male','3','TRUE','TRUE','20221129',7002),
(1002,'Jack','Black','Family Medicine',NULL,'Prescriber','MD','9192383822','jackblack@gmail.com','Male','12','TRUE','TRUE','20221129',NULL),
(1003,'Ron','Mccarthy','Oncology',NULL,'Prescriber','MBBS','9192383823','ronmccarthy@gmail.com','Male','20','TRUE','TRUE','20221129',NULL),
(1004,'Jill','Hoffman','Othopedic','Family Medicine','Prescriber','MD','9192383824','jillhoffman@gmail.com','Female','3','TRUE','TRUE','20221129',NULL),
(1005,'Nigel','Tucker','Dermatology',NULL,'Prescriber','MBBS','9192383825','nigeltucker@gmail.com','Male','5','TRUE','TRUE','20221129',NULL),
(1006,'Ben','Johnson','General Physician','Family Medicine','Prescriber','MBBS','9192383826','benjohnson@gmail.com','Male','3','TRUE','TRUE','20221129',NULL),
(1007,'Sarah','Mikaelson','Neurology',NULL,'Prescriber','MD','9192383827','sarahmikaelson@gmail.com','Female','5','TRUE','TRUE','20221129',NULL),
(1008,'Dan','Peters','Dermatology',NULL,'Prescriber','MBBS','9192383828','danpeters@gmail.com','Male','6','TRUE','TRUE','20221129',NULL),
(1009,'Hannah','Woodson','Neurology','Family Medicine','Prescriber','MBBS','9192383829','hannahwoodson@gmail.com','Female','11','TRUE','TRUE','20221129',NULL),
(1010,'Carla','Martin','Oncology','Orthopedic','Prescriber','MBBS','9192383830','carlamartin@gmail.com','Female','15','TRUE','TRUE','20221129',NULL),
(1011,'Casey','Arnold','Dermatology',NULL,'Prescriber','MBBS','9192383831','caseyarnold@gmail.com','Male','4','TRUE','TRUE','20221129',NULL),
(1012,'Macy','Pipin','Nurse Practioner',NULL,'Non Prescriber','BSN','9192383832','macypipin@gmail.com','Female','18','TRUE','TRUE','20221129',NULL),
(1013,'John','Shelvey','General Physician','Family Medicine','Prescriber','MD','9192383833','johnshelvey@gmail.com','Male','2','TRUE','TRUE','20221129',NULL);

-- --------------------------------------------------------

--
-- Table structure for table `hospitals`
--

CREATE TABLE `hospitals` (
	`hospitalid` int NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`type` varchar(255) NOT NULL,
	`addressline1` varchar(255) NOT NULL,
	`addressline2` varchar(255) NOT NULL,
	`city` varchar(255) NOT NULL,
	`state` varchar(255) NOT NULL,
	`country` varchar(255) NOT NULL,
	`zipcode` varchar(255) NOT NULL,
	`phone` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL,
	`approvalstatus` varchar(255) NOT NULL,
	`isactive` varchar(255) NOT NULL,
	`lastmoddate` varchar(255) NOT NULL,
	PRIMARY KEY (`hospitalid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `hospitals` AUTO_INCREMENT=2000;

--
-- Dumping data for table `hospitals`
--

INSERT INTO `hospitals` (`hospitalid`, `name`, `type`, `addressline1`, `addressline2`, `city`, `state`, `country`, `zipcode`, `phone`, `email`, `approvalstatus`, `isactive`, `lastmoddate`) VALUES
(2001,'Abbott Northwestern Hospital','Hospital',NULL,NULL,'Seattle','WA','USA','12345','8765434567',NULL,'TRUE','TRUE','20221129'),
(2002,'Carolinas Medical Center','Health Center',NULL,NULL,'Charlotte','NC','USA','29392','8765434569',NULL,'TRUE','TRUE','20221129'),
(2003,'Cedars-Sinai Marina Del Rey Hospital','Hospital',NULL,NULL,'Ney York City','NY','USA','32343','8765434571',NULL,'TRUE','TRUE','20221129'),
(2004,'Monterey Park Hospital','Hospital',NULL,NULL,'Los Angeles','CA','USA','13433','8765434573',NULL,'TRUE','TRUE','20221129'),
(2005,'Lake Charles Memorial Hospital','Hospital',NULL,NULL,'Arlington','TX','USA','34455','8765434575',NULL,'TRUE','TRUE','20221129'),
(2006,'Providence Saint John''s Health Center','Health Center',NULL,NULL,'Chicago','IL','USA','24322','8765434577',NULL,'TRUE','TRUE','20221129'),
(2007,'Trinity Health','Clinic',NULL,NULL,'Raleigh','NC','USA','12312','8765434579',NULL,'TRUE','TRUE','20221129');


-- --------------------------------------------------------

--
-- Table structure for table `affiliation`
--

CREATE TABLE `affiliation` (
    `affiliaitionid` int NOT NULL AUTO_INCREMENT,
    `doctorid` int NOT NULL,
    `hospitalid` int NOT NULL,
    `appointmentschedule` varchar(255) NOT NULL,
    `isactive` varchar(255) NOT NULL,
    `lastmoddate` varchar(255) NOT NULL,
	PRIMARY KEY (`affiliaitionid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `affiliation` AUTO_INCREMENT=3000;

--
-- Dumping data for table `affiliation`
--

INSERT INTO `affiliation` (`affiliaitionid`, `doctorid`, `hospitalid`, `appointmentschedule`, `isactive`, `lastmoddate`) VALUES
(3001,1001,2001,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3002,1002,2002,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3003,1003,2003,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3004,1004,2004,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3005,1005,2005,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3006,1006,2006,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3007,1007,2007,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3008,1008,2001,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3009,1009,2002,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3010,1010,2003,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3011,1011,2004,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3012,1012,2005,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3013,1013,2001,'{"Monday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Tuesday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3014,1004,2002,'{"Wednesday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Thursday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3015,1005,2003,'{"Wednesday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Thursday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3016,1008,2004,'{"Wednesday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Thursday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3017,1009,2005,'{"Wednesday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Thursday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3018,1010,2006,'{"Wednesday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Thursday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3019,1013,2007,'{"Wednesday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}, "Thursday":{"StartTime": "11:00:00", "EndTime":"16:00:00"}}','TRUE','20221129'),
(3020,1013,2006,'{"Friday":{"StartTime": "10:00:00", "EndTime":"16:00:00"}','TRUE','20221129');



-- --------------------------------------------------------


--
-- Table structure for table `users`
--

CREATE TABLE `users` (
	`userid`  int NOT NULL AUTO_INCREMENT,
	`username` varchar(255) NOT NULL,
	`firstname` varchar(255) NOT NULL,
	`lastname` varchar(255) NOT NULL,
    `usertype` varchar(255) NOT NULL,
	`gender` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL,
	`password` varchar(255) NOT NULL,
	`phone` varchar(255) NOT NULL,
	`isactive` varchar(255) NOT NULL,
	`lastmoddate` varchar(255) NOT NULL,
	PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `users` AUTO_INCREMENT=7000;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userid`,`username`, `firstname`, `lastname`, `usertype`, `gender`, `email`, `password`, `phone`, `isactive`, `lastmoddate`) VALUES
(7001,'MickSchum', 'Mick', 'Schum', 'Patient', 'Male', 'mickschum@gmail.com', 'mick','9090909099','TRUE','20221129'),
(7002,'JohnDoe', 'John', 'Doe', 'Patient;Doctor', 'Male', 'johndoe@gmail.com', 'john','9090909098','TRUE','20221129');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
