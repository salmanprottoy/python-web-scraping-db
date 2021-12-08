-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 08, 2021 at 08:31 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `family_friendly_rentals`
--

CREATE TABLE `family_friendly_rentals` (
  `id` int(11) NOT NULL,
  `Title` varchar(255) NOT NULL,
  `Location` varchar(255) NOT NULL,
  `Sleeps` varchar(255) NOT NULL,
  `Bedroom` varchar(255) NOT NULL,
  `Bathroom` varchar(255) NOT NULL,
  `Image1` varchar(255) NOT NULL,
  `Image2` varchar(255) NOT NULL,
  `Image3` varchar(255) NOT NULL,
  `Price` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `family_friendly_rentals`
--

INSERT INTO `family_friendly_rentals` (`id`, `Title`, `Location`, `Sleeps`, `Bedroom`, `Bathroom`, `Image1`, `Image2`, `Image3`, `Price`) VALUES
(1, 'Spectacular mountain beauty at Hawkes Hill Vacation Home in Golden BC', 'british columbia, canada', 'Sleeps 4', '2 Bedrooms', '1 Bathroom', '\"https://media.vrbo.com/lodging/35000000/34590000/34581500/34581421/8c4aa6b0.c6.jpg\"', '\"https://media.vrbo.com/lodging/35000000/34590000/34581500/34581421/14380b59.c6.jpg\"', '\"https://media.vrbo.com/lodging/35000000/34590000/34581500/34581421/2b1b9f77.c6.jpg\"', '$114'),
(2, 'Sunshine Coast Chill', 'british columbia, canada', 'Sleeps 6', '2 Bedrooms', '2 Bathrooms', '\"https://media.vrbo.com/lodging/26000000/25140000/25135000/25134980/afb3ca97.c6.jpg\"', '\"https://media.vrbo.com/lodging/26000000/25140000/25135000/25134980/b0ba3553.c6.jpg\"', '\"https://media.vrbo.com/lodging/26000000/25140000/25135000/25134980/30476eda.c6.jpg\"', '$198'),
(3, 'Ocean Front, Spectacular Views, Minutes From Sechelt, a Sunshine Coast Hub!', 'british columbia, canada', 'Sleeps 3', '1 Bedroom', '1 Bathroom', '\"https://media.vrbo.com/lodging/32000000/31060000/31052400/31052305/347cd500.c6.jpg\"', '\"https://media.vrbo.com/lodging/32000000/31060000/31052400/31052305/320081ab.c6.jpg\"', '\"https://media.vrbo.com/lodging/32000000/31060000/31052400/31052305/df183c28.c6.jpg\"', '$141'),
(4, 'Cozy, romantic waterfront cabin. Sleeps 2, pet-friendly, walk to all amenities.', 'british columbia, canada', 'Sleeps 2', 'Studio', '1 Bathroom', '\"https://media.vrbo.com/lodging/34000000/33990000/33984000/33983903/fc376eb4.c6.jpg\"', '\"https://media.vrbo.com/lodging/34000000/33990000/33984000/33983903/f4695ae9.c6.jpg\"', '\"https://media.vrbo.com/lodging/34000000/33990000/33984000/33983903/76ee9ef3.c6.jpg\"', '$116'),
(5, 'Luxury Villa With Hot Tub & Private Sandy Beach. ', 'british columbia, canada', 'Sleeps 4', '1 Bedroom', '1 Bathroom', '\"https://media.vrbo.com/lodging/35000000/34590000/34580400/34580380/5e09b260.c6.jpg\"', '\"https://media.vrbo.com/lodging/35000000/34590000/34580400/34580380/485fcf69.c6.jpg\"', '\"https://media.vrbo.com/lodging/35000000/34590000/34580400/34580380/3a2a1a9b.c6.jpg\"', '$136'),
(6, 'Rocky Mountain Getaway, Beautiful Cabin, Hidden Gem in Kimberley, BC', 'british columbia, canada', 'Sleeps 10', '3 Bedrooms', '2 Bathrooms', '\"https://media.vrbo.com/lodging/35000000/34080000/34075900/34075847/42481141.c6.jpg\"', '\"https://media.vrbo.com/lodging/35000000/34080000/34075900/34075847/b84fb3f5.c6.jpg\"', '\"https://media.vrbo.com/lodging/35000000/34080000/34075900/34075847/3c82f534.c6.jpg\"', '$185');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `family_friendly_rentals`
--
ALTER TABLE `family_friendly_rentals`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `family_friendly_rentals`
--
ALTER TABLE `family_friendly_rentals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
