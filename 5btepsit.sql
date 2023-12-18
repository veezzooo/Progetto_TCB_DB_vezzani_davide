-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Dic 18, 2023 alle 22:42
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5btepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `dipendenti_davide_vezzani`
--

CREATE TABLE `dipendenti_davide_vezzani` (
  `id` int(11) NOT NULL,
  `nome` varchar(15) NOT NULL,
  `cognome` varchar(15) NOT NULL,
  `residenza` varchar(30) NOT NULL,
  `indirizzo` varchar(40) NOT NULL,
  `data_nascita` date NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `agente` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `dipendenti_davide_vezzani`
--

INSERT INTO `dipendenti_davide_vezzani` (`id`, `nome`, `cognome`, `residenza`, `indirizzo`, `data_nascita`, `telefono`, `agente`) VALUES
(5, 'Davide', 'Vezzani', 'Rio Saliceto', 'Via Griminella 70', '2005-11-30', '3317290702', 'immobiliare');

-- --------------------------------------------------------

--
-- Struttura della tabella `zone_di_lavoro_davide_vezzani`
--

CREATE TABLE `zone_di_lavoro_davide_vezzani` (
  `id_zona` int(11) NOT NULL,
  `nome_zona` char(50) NOT NULL,
  `numero_clienti` int(11) NOT NULL,
  `citta` char(50) NOT NULL,
  `codd` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `zone_di_lavoro_davide_vezzani`
--

INSERT INTO `zone_di_lavoro_davide_vezzani` (`id_zona`, `nome_zona`, `numero_clienti`, `citta`, `codd`) VALUES
(1, 'Sud', 4, 'Milano', 1),
(2, 'Est', 5, 'Milano', 2);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_davide_vezzani`
--
ALTER TABLE `dipendenti_davide_vezzani`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `zone_di_lavoro_davide_vezzani`
--
ALTER TABLE `zone_di_lavoro_davide_vezzani`
  ADD PRIMARY KEY (`id_zona`),
  ADD KEY `codd` (`codd`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_davide_vezzani`
--
ALTER TABLE `dipendenti_davide_vezzani`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT per la tabella `zone_di_lavoro_davide_vezzani`
--
ALTER TABLE `zone_di_lavoro_davide_vezzani`
  MODIFY `id_zona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
