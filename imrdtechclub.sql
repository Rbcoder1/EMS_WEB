-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2024 at 02:01 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

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
-- Table structure for table `bootcamps`
--

CREATE TABLE `bootcamps` (
  `bootcamp_id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `objective` varchar(500) NOT NULL,
  `mode` varchar(10) NOT NULL DEFAULT 'online',
  `instructor` varchar(100) NOT NULL,
  `outcome` varchar(200) NOT NULL,
  `hours_per_day` int(11) NOT NULL,
  `total_duration` int(11) NOT NULL,
  `cover_image` varchar(200) DEFAULT 'bootcamp_default.jpg',
  `register_start_on` timestamp NULL DEFAULT NULL,
  `register_end_on` timestamp NULL DEFAULT NULL,
  `camp_start_on` timestamp NULL DEFAULT NULL,
  `camp_end_on` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `event_registration`
--

CREATE TABLE `event_registration` (
  `register_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `event_id` int(11) NOT NULL,
  `roll_no` int(3) NOT NULL,
  `topic` varchar(30) NOT NULL,
  `tech_used` varchar(50) NOT NULL,
  `team_name` varchar(20) NOT NULL,
  `leader_name` varchar(20) NOT NULL,
  `member1_name` varchar(20) NOT NULL,
  `member2_name` varchar(20) NOT NULL,
  `member3_name` varchar(20) NOT NULL,
  `member4_name` varchar(20) NOT NULL,
  `register_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `feature_banner`
--

CREATE TABLE `feature_banner` (
  `banner_id` int(11) NOT NULL,
  `bannner_name` varchar(100) NOT NULL,
  `banner_img` varchar(200) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `feature_banners`
--

CREATE TABLE `feature_banners` (
  `banner_id` int(11) NOT NULL,
  `bannner_name` varchar(100) NOT NULL,
  `banner_img` varchar(200) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `internal_events`
--

CREATE TABLE `imrdcompetion` (
  `event_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` varchar(400) NOT NULL,
  `category` varchar(400) NOT NULL,
  `logo_image` varchar(300) NOT NULL,
  `objective` varchar(400) NOT NULL,
  `rules` varchar(400) NOT NULL,
  `mentors` varchar(300) NOT NULL,
  `phases` varchar(400) NOT NULL,
  `prices` varchar(300) NOT NULL,
  `dates` varchar(400) NOT NULL,
  `registration_start_on` timestamp NULL DEFAULT NULL,
  `registration_ends_on` timestamp NULL DEFAULT NULL,
  `event_start_on` timestamp NULL DEFAULT NULL,
  `event_ends_on` timestamp NULL DEFAULT NULL,
  `created_on` timestamp NOT NULL DEFAULT current_timestamp(),
  `updates_on` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `internal_events`
--

INSERT INTO `internal_events` (`event_id`, `title`, `description`, `category`, `logo_image`, `objective`, `rules`, `mentors`, `phases`, `prices`, `dates`, `registration_start_on`, `registration_ends_on`, `event_start_on`, `event_ends_on`, `created_on`, `updates_on`) VALUES
(1, 'fdafsdfg', 'ihljh', 'sdfgdfg', '', 'fsgdfg', 'jlkjhjklhj', 'jbkjkj', 'ljlkhjjkjl', 'lkjlkjl', 'kjnj,jn', '2024-02-27 18:30:00', '2024-02-29 18:30:00', '2024-02-05 18:30:00', '2024-03-05 18:30:00', '2024-02-25 12:44:53', NULL),
(2, 'fdafsdfg', 'ihljh', 'sdfgdfg', '', 'fsgdfg', 'jlkjhjklhj', 'jbkjkj', 'ljlkhjjkjl', 'lkjlkjl', 'kjnj,jn', '2024-02-27 18:30:00', '2024-02-29 18:30:00', '2024-02-05 18:30:00', '2024-03-05 18:30:00', '2024-02-25 12:46:26', NULL),
(3, 'fdafsdfg', 'ihljh', 'sdfgdfg', '', 'fsgdfg', 'jlkjhjklhj', 'jbkjkj', 'ljlkhjjkjl', 'lkjlkjl', 'kjnj,jn', '2024-02-27 18:30:00', '2024-02-29 18:30:00', '2024-02-05 18:30:00', '2024-03-05 18:30:00', '2024-02-25 12:46:53', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `learning_history`
--

CREATE TABLE `learning_history` (
  `stud_id` int(11) NOT NULL,
  `video_id` int(11) NOT NULL,
  `stop_on` int(11) NOT NULL,
  `started_on` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_event_history`
--

CREATE TABLE `user_event_history` (
  `event_history_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `event_id` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_profile`
--

CREATE TABLE `user_profile` (
  `profile_id` int(11) NOT NULL,
  `photo` varchar(20) DEFAULT NULL,
  `mobile_no` varchar(12) DEFAULT NULL,
  `about` varchar(255) DEFAULT NULL,
  `b_date` date DEFAULT NULL,
  `interest` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `skill` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `future_goal` varchar(10) DEFAULT NULL,
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_profile`
--

INSERT INTO `user_profile` (`profile_id`, `photo`, `mobile_no`, `about`, `b_date`, `interest`, `skill`, `future_goal`, `updated_at`) VALUES
(23, '', '9527081664', 'I Am A Good Boy With Best Technical Knowledge.', '2023-07-05', 'PHP Developement', 'HTML,CSS,Javascript,Python,Ruby,Github', 'web', '2023-07-30 09:00:11'),
(24, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2024-02-25 11:07:44');

-- --------------------------------------------------------

--
-- Table structure for table `user_register`
--

CREATE TABLE `user_register` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `user_email` varchar(40) NOT NULL,
  `user_password` varchar(10) NOT NULL,
  `ban` varchar(6) NOT NULL DEFAULT 'false',
  `created_at` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_register`
--

INSERT INTO `user_register` (`user_id`, `first_name`, `last_name`, `user_email`, `user_password`, `ban`, `created_at`) VALUES
(23, 'Rohit', 'Borse', 'rohitborse@gmail.com', 'Rohit', '1', '2023-07-30'),
(24, 'isha', 'borse', 'isha@gmail.com', 'Isha@123', '1', '2024-02-25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bootcamps`
--
ALTER TABLE `bootcamps`
  ADD PRIMARY KEY (`bootcamp_id`);

--
-- Indexes for table `event_registration`
--
ALTER TABLE `event_registration`
  ADD PRIMARY KEY (`register_id`),
  ADD KEY `foreignkey` (`user_id`);

--
-- Indexes for table `feature_banners`
--
ALTER TABLE `feature_banners`
  ADD PRIMARY KEY (`banner_id`);

--
-- Indexes for table `internal_events`
--
ALTER TABLE `internal_events`
  ADD PRIMARY KEY (`event_id`);

--
-- Indexes for table `user_event_history`
--
ALTER TABLE `user_event_history`
  ADD PRIMARY KEY (`event_history_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `event_id` (`event_id`);

--
-- Indexes for table `user_profile`
--
ALTER TABLE `user_profile`
  ADD KEY `test` (`profile_id`);

--
-- Indexes for table `user_register`
--
ALTER TABLE `user_register`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `user_email` (`user_email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bootcamps`
--
ALTER TABLE `bootcamps`
  MODIFY `bootcamp_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `event_registration`
--
ALTER TABLE `event_registration`
  MODIFY `register_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `feature_banners`
--
ALTER TABLE `feature_banners`
  MODIFY `banner_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `internal_events`
--
ALTER TABLE `internal_events`
  MODIFY `event_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user_event_history`
--
ALTER TABLE `user_event_history`
  MODIFY `event_history_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_register`
--
ALTER TABLE `user_register`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `event_registration`
--
ALTER TABLE `event_registration`
  ADD CONSTRAINT `foreignkey` FOREIGN KEY (`user_id`) REFERENCES `user_register` (`user_id`);

--
-- Constraints for table `user_event_history`
--
ALTER TABLE `user_event_history`
  ADD CONSTRAINT `user_event_history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_register` (`user_id`),
  ADD CONSTRAINT `user_event_history_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `internal_events` (`event_id`);

--
-- Constraints for table `user_profile`
--
ALTER TABLE `user_profile`
  ADD CONSTRAINT `test` FOREIGN KEY (`profile_id`) REFERENCES `user_register` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
