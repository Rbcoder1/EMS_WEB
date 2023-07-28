-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 28, 2023 at 08:27 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eventmanage`
--

-- --------------------------------------------------------

--
-- Table structure for table `internal_events`
--

CREATE TABLE `internal_events` (
  `event_id` int(11) NOT NULL,
  `event_name` varchar(20) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `tags` varchar(10) NOT NULL,
  `images` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `objective` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `tech_used` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `phases` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `rules` text NOT NULL,
  `dates` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `is_open` tinyint(1) NOT NULL DEFAULT 1,
  `upcoming` tinyint(1) NOT NULL DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `internal_events`
--

INSERT INTO `internal_events` (`event_id`, `event_name`, `description`, `tags`, `images`, `objective`, `tech_used`, `phases`, `rules`, `dates`, `is_open`, `upcoming`, `created_at`) VALUES
(1, 'Field Work', 'In the 5th semester examination student are required to carry out a Field Work individually or by\r\ngroup of two students. It should be compulsorily based on assessment of any IT project\r\nimplemented in real time as mentioned in the point 3. The topic should be decided with\r\nconsultation and guidance of internal teacher of the Institute. The field work should be necessarily\r\nResearch oriented, Innovative and Problem solving', 'field_work', 'img/fieldworkbanner.png,\r\nimg/fieldworklogo.png', 'To Understand The Issue Implementated IT Project by assigning it using research methodology.\r\n', 'none', 'Submit Your Topic Of Field Work,\r\nWork On It And Research,\r\nSubmit Work Report,\r\nViva on topic and report', 'Field work shall be strictly based on primary data. The Sample Size shall be minimum 100.The students are encouraged to use advance excel or SPSS software\",\r\nField work viva shall be conducted at the end of Semester V\",\r\nViva Voce for one student shall be of minimum 15 minutes. The Student has to prepare Power Point presentation based on field work to be presented at the time of Viva voce.', 'none', 1, 0, '2023-07-27'),
(2, 'hackathon 3.0', 'This Is AI Based Hackathon In Which Student Make Their Project In Hackathon Using Artificial Intelligence And Other AI Technologies.', 'hackathon', '{\r\n\"msg\":\"none\"\r\n}', '{\r\n\"first\":\"To Aware About Artificial Intelligence Technology\",\r\n\"second\":\"To Get Hands On Practise On AI Related Field\"\r\n}', '{\r\n\"tech1\":\"Machine Learning\",\r\n\"tech2\":\"Deep Learning\",\r\n\"tech3\":\"Computer Vision\",\r\n\"tech4\":\"NLP\",\r\n\"tech5\":\"Android\"\r\n}', '{\r\n\"phase1\":\"Registration Of Team\",\r\n\"phase2\":\"Submit Your Idea\",\r\n\"phase3\":\"Development Phase\",\r\n\"phase4\":\"Project Exhibition\"\r\n}', '{\r\n\"msg\":\"none\"\r\n}', '{\r\n\"date1\":\"13 Feb 2023\",\r\n\"date2\":\"13 Feb 2023\",\r\n\"date3\":\"20 Feb 2023\",\r\n\"date4\":\"21 Feb 2023\",\r\n\"date5\":\"31 Feb 2023\",\r\n\"date6\":\"15 Mar 2023 \"\r\n}', 0, 0, '2023-07-27');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `internal_events`
--
ALTER TABLE `internal_events`
  ADD PRIMARY KEY (`event_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `internal_events`
--
ALTER TABLE `internal_events`
  MODIFY `event_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
