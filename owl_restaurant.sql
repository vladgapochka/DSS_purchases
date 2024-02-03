-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Фев 03 2024 г., 14:00
-- Версия сервера: 8.0.30
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `owl_restaurant`
--

-- --------------------------------------------------------

--
-- Структура таблицы `composition_dish`
--

CREATE TABLE `composition_dish` (
  `id_dishes` int NOT NULL,
  `id_product` int NOT NULL,
  `number_of_product` float NOT NULL,
  `id_unit_of_measurement` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `composition_dish`
--

INSERT INTO `composition_dish` (`id_dishes`, `id_product`, `number_of_product`, `id_unit_of_measurement`) VALUES
(8, 22, 0.2, 1),
(8, 23, 0.1, 1),
(8, 24, 0.1, 1),
(8, 26, 0.2, 1),
(8, 27, 0.1, 1),
(8, 28, 0.15, 1),
(8, 29, 0.05, 1),
(8, 30, 0.005, 1),
(8, 31, 0.005, 1),
(7, 32, 0.2, 1),
(7, 33, 0.15, 1),
(7, 27, 3, 2),
(7, 34, 0.08, 2),
(7, 28, 0.15, 1),
(7, 35, 0.02, 1),
(7, 36, 0.005, 1),
(9, 22, 0.1, 1),
(9, 27, 2, 2),
(9, 28, 0.1, 2),
(9, 36, 0.005, 1),
(15, 44, 0.34, 1),
(11, 47, 1.5, 1),
(11, 35, 0.7, 1),
(11, 39, 0.18, 1),
(11, 48, 0.06, 1),
(11, 30, 0.007, 1),
(11, 41, 0.007, 1),
(12, 49, 1, 1),
(12, 28, 0.05, 1),
(12, 50, 0.005, 1),
(12, 31, 0.01, 1),
(16, 51, 0.12, 1),
(16, 52, 0.1, 1),
(16, 53, 0.08, 1),
(16, 54, 0.08, 1),
(16, 55, 0.005, 1),
(16, 56, 0.01, 3),
(16, 45, 0.1, 1),
(16, 44, 0.16, 1),
(15, 45, 0.24, 3),
(15, 55, 0.005, 1),
(15, 56, 0.015, 3),
(15, 57, 0.014, 1),
(15, 30, 0.007, 1),
(15, 39, 0.3, 1),
(15, 51, 0.2, 1),
(15, 58, 0.025, 1),
(15, 59, 0.02, 1),
(10, 60, 2.4, 1),
(10, 35, 0.3, 1),
(10, 61, 0.3, 1),
(10, 31, 0.125, 1),
(10, 62, 0.25, 3),
(17, 62, 0.7, 3),
(17, 37, 0.08, 1),
(17, 63, 0.08, 1),
(17, 64, 0.08, 1),
(17, 65, 0.08, 1),
(17, 66, 0.2, 1),
(18, 22, 0.3, 1),
(18, 67, 0.05, 3),
(18, 30, 0.01, 3),
(20, 22, 1, 1),
(20, 30, 0.05, 1),
(20, 36, 0.05, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `container`
--

CREATE TABLE `container` (
  `id_container` int NOT NULL,
  `volume` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `container`
--

INSERT INTO `container` (`id_container`, `volume`) VALUES
(863, 'вес'),
(864, 'батон'),
(865, 'бутылка'),
(866, 'б/к'),
(867, 'подложка');

-- --------------------------------------------------------

--
-- Структура таблицы `customer`
--

CREATE TABLE `customer` (
  `id_customer` int NOT NULL,
  `surname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `patronymic` varchar(20) NOT NULL,
  `phone` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `customer`
--

INSERT INTO `customer` (`id_customer`, `surname`, `name`, `patronymic`, `phone`) VALUES
(12, 'Гапочка', 'Владислав', 'Валерьевич', '89883667279'),
(13, 'Ноженко', 'Сергей', 'Викторович', '89184336747'),
(14, 'Хачатурян', 'Артур', 'Каренович', '89182557670'),
(15, 'Иванов', 'Иван', 'Иванович', '89182295770'),
(16, 'Чеховской', 'Никита', 'Владимирович', '89182308571'),
(17, 'Сергеев', 'Михаил', 'Александрович', '89182098976'),
(19, 'Жовкивская', 'Лилия', 'Андреевна', '89615082823');

-- --------------------------------------------------------

--
-- Структура таблицы `dishes`
--

CREATE TABLE `dishes` (
  `id_dishes` int NOT NULL,
  `name_dishes` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `output` varchar(20) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `dishes`
--

INSERT INTO `dishes` (`id_dishes`, `name_dishes`, `output`, `price`) VALUES
(7, 'Салат \"Нежность\"', '310', 120),
(8, ' Салат Оливье', '150', 220),
(9, 'Салат Влада', '200', 150),
(10, 'Шашлык их баранины', '175', 350),
(11, 'Шашлык из свинины', '220', 340),
(12, 'Шашлык из курицы', '150', 290),
(13, 'Стейк из семги', '100', 220),
(14, 'Солянка', '400', 390),
(15, 'Пицца маргарита', '400', 360),
(16, 'Пицца 4 сыра', '600', 450),
(17, 'Лимонад ягодный', '0.9', 400),
(18, 'Картофель фри', '200', 150),
(19, 'Картофельное пюре', '200', 150),
(20, 'Картофель по деревенски', '200', 150);

-- --------------------------------------------------------

--
-- Структура таблицы `events`
--

CREATE TABLE `events` (
  `id_events` int NOT NULL,
  `id_customer` int NOT NULL,
  `number_of_persons` int NOT NULL,
  `date` varchar(50) NOT NULL,
  `address` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `events`
--

INSERT INTO `events` (`id_events`, `id_customer`, `number_of_persons`, `date`, `address`) VALUES
(12, 12, 23, '22.04.2023 20:00', 'Красная 77'),
(13, 12, 2, '25.08.2023 17:00', 'Красная 321'),
(14, 13, 12, '24.04.2023 20:00', 'Красная 77'),
(15, 14, 21, '01.05.2023 18:00', 'Шоссейная 15'),
(16, 15, 21, '05.05.2023 19:00', 'Шоссейная 15'),
(17, 16, 8, '06.05.2023 16:00', 'Шоссейная 15'),
(18, 13, 15, '09.04.2023 17:00', 'Шоссейная 15'),
(19, 17, 13, '11.05.2023 15:00', 'Шоссейная 15'),
(20, 19, 18, '15.05.2023 18:00', 'Красная 77');

-- --------------------------------------------------------

--
-- Структура таблицы `events_in_dishes`
--

CREATE TABLE `events_in_dishes` (
  `id_events` int NOT NULL,
  `id_dishes` int NOT NULL,
  `number_of_servings` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `events_in_dishes`
--

INSERT INTO `events_in_dishes` (`id_events`, `id_dishes`, `number_of_servings`) VALUES
(12, 8, 5),
(12, 7, 5),
(14, 9, 10),
(17, 7, 5),
(17, 10, 7),
(17, 11, 4),
(17, 12, 5),
(17, 16, 8),
(17, 14, 2),
(17, 13, 2),
(17, 17, 5),
(16, 10, 5),
(18, 8, 7),
(18, 10, 5),
(18, 11, 5),
(18, 12, 5),
(18, 16, 3),
(18, 17, 8),
(12, 19, 5),
(18, 19, 5),
(18, 18, 5),
(18, 20, 5),
(12, 9, 3),
(15, 16, 3),
(15, 9, 3),
(15, 15, 5),
(12, 15, 4),
(12, 16, 4),
(19, 16, 4),
(19, 15, 4),
(19, 10, 5),
(19, 11, 5),
(19, 17, 7),
(19, 18, 7),
(19, 20, 2),
(19, 7, 4),
(19, 8, 4),
(15, 10, 1),
(15, 11, 2),
(15, 17, 4),
(15, 18, 4),
(15, 20, 3),
(15, 7, 2);

-- --------------------------------------------------------

--
-- Структура таблицы `manufacturer`
--

CREATE TABLE `manufacturer` (
  `id_manufacturer` int NOT NULL,
  `name_manufacturer` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `manufacturer`
--

INSERT INTO `manufacturer` (`id_manufacturer`, `name_manufacturer`) VALUES
(3, 'Рыбомиров'),
(4, 'СберМаркет'),
(5, 'Метро'),
(6, 'Лента'),
(7, 'Ладожский рынок'),
(8, 'СПК');

-- --------------------------------------------------------

--
-- Структура таблицы `product`
--

CREATE TABLE `product` (
  `id_product` int NOT NULL,
  `name_product` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `product`
--

INSERT INTO `product` (`id_product`, `name_product`) VALUES
(22, 'Картофель'),
(23, 'Морковь'),
(24, 'Огурцы солёные (бочковые)'),
(25, 'Горошек зеленый консервированный'),
(26, 'Колбаса вареная (докторская)'),
(27, 'Яйца'),
(28, 'Майонез'),
(29, 'Сметана'),
(30, 'Соль'),
(31, 'Перец черный молотый'),
(32, 'Филе куриное'),
(33, 'Грибы (шампиньоны) консервированные'),
(34, 'Сыр твердый'),
(35, 'Лук репчатый'),
(36, 'Зелень укропа'),
(37, 'Малина'),
(38, 'Перец болгарский'),
(39, 'Томаты'),
(40, 'Оливки'),
(41, 'Перец красный молотый'),
(42, ''),
(43, ''),
(44, 'Мука'),
(45, 'Вода'),
(46, 'Молоко'),
(47, 'Свинина'),
(48, 'Лимон'),
(49, 'Куриное филе'),
(50, 'Приправа для курицы'),
(51, 'Сыр моцарелла'),
(52, 'Сыр рикотта'),
(53, 'Сыр пармезан'),
(54, 'Сыр горгонзола'),
(55, 'Дрожжи сухие'),
(56, 'Масло оливковое'),
(57, 'Сахар'),
(58, 'Базилик зелёный'),
(59, 'Чеснок'),
(60, 'Баранина'),
(61, 'Петрушка'),
(62, 'Вода минеральная'),
(63, 'Клубника'),
(64, 'Голубика'),
(65, 'Ежевика'),
(66, 'Сироп клубничный'),
(67, 'Растительное масло');

-- --------------------------------------------------------

--
-- Структура таблицы `product_options`
--

CREATE TABLE `product_options` (
  `id_product_options` int NOT NULL,
  `id_product` int NOT NULL,
  `id_container` int NOT NULL,
  `id_unit_of_measurement` int NOT NULL,
  `id_manufacturer` int NOT NULL,
  `quantity` float NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `product_options`
--

INSERT INTO `product_options` (`id_product_options`, `id_product`, `id_container`, `id_unit_of_measurement`, `id_manufacturer`, `quantity`, `price`) VALUES
(12, 22, 863, 1, 4, 1, 20),
(13, 37, 863, 1, 4, 1, 240),
(14, 22, 863, 1, 3, 2.5, 50),
(15, 28, 863, 1, 5, 0.5, 75),
(16, 36, 863, 1, 5, 0.005, 30),
(17, 36, 863, 1, 4, 0.005, 20),
(18, 28, 863, 1, 4, 0.5, 80),
(19, 27, 863, 1, 4, 1, 100),
(20, 27, 863, 1, 5, 1, 88),
(21, 32, 863, 1, 6, 1, 299),
(22, 23, 863, 1, 6, 1, 49),
(23, 46, 865, 1, 6, 0.9, 79),
(24, 44, 863, 1, 5, 2.5, 170),
(25, 44, 863, 1, 6, 2.5, 145),
(26, 44, 863, 1, 7, 5, 300),
(27, 45, 865, 3, 5, 5, 89),
(28, 51, 863, 1, 5, 0.125, 169),
(29, 51, 863, 1, 6, 0.4, 319),
(30, 52, 863, 1, 6, 0.25, 129),
(31, 52, 863, 1, 5, 0.2, 109),
(32, 53, 863, 1, 6, 0.25, 250),
(33, 53, 863, 1, 6, 1, 1199),
(34, 53, 863, 1, 5, 1, 1749),
(35, 54, 863, 1, 5, 0.1, 259),
(36, 54, 863, 1, 5, 0.15, 319),
(37, 54, 863, 1, 6, 0.1, 209),
(38, 55, 863, 1, 5, 0.007, 19),
(39, 55, 863, 1, 5, 0.5, 319),
(40, 55, 863, 1, 6, 0.011, 14),
(41, 55, 863, 1, 6, 0.1, 99),
(42, 56, 865, 3, 5, 1, 799),
(43, 56, 865, 3, 5, 0.5, 439),
(44, 56, 865, 3, 6, 0.5, 568),
(45, 45, 865, 3, 6, 1, 39),
(46, 45, 865, 3, 5, 5, 129),
(47, 57, 863, 1, 5, 1, 62),
(48, 57, 863, 1, 6, 1, 59),
(49, 30, 863, 1, 5, 1, 35),
(50, 30, 863, 1, 6, 1, 27),
(51, 39, 863, 1, 6, 1, 168),
(52, 39, 863, 1, 5, 1, 329),
(53, 58, 863, 1, 5, 0.3, 819),
(54, 59, 863, 1, 5, 0.1, 29),
(55, 60, 863, 1, 5, 1, 1099),
(56, 60, 863, 1, 5, 1, 1099),
(57, 60, 863, 1, 6, 1, 699),
(58, 62, 863, 3, 6, 1.5, 64),
(59, 62, 863, 3, 5, 0.5, 17),
(60, 35, 863, 1, 5, 5, 89),
(61, 35, 863, 1, 6, 0.5, 129),
(62, 61, 863, 1, 6, 0.25, 159),
(63, 61, 863, 1, 6, 0.25, 139),
(64, 31, 863, 1, 6, 0.22, 149),
(65, 31, 863, 1, 5, 0.02, 70),
(66, 47, 863, 1, 5, 1, 499),
(67, 48, 863, 1, 5, 0.3, 159),
(68, 41, 863, 1, 5, 0.5, 319),
(69, 41, 863, 1, 6, 0.03, 63),
(70, 63, 863, 1, 5, 0.25, 229),
(71, 63, 863, 1, 6, 1, 600),
(72, 63, 863, 1, 7, 1, 250),
(73, 37, 863, 1, 7, 1, 200),
(74, 65, 863, 1, 7, 1, 180),
(75, 64, 863, 1, 6, 0.5, 889),
(76, 64, 863, 1, 5, 0.3, 289),
(77, 66, 863, 1, 6, 0.3, 114),
(78, 67, 865, 3, 5, 1, 139),
(79, 32, 863, 1, 5, 2.5, 349),
(81, 34, 863, 1, 5, 0.25, 359),
(82, 33, 863, 1, 5, 0.35, 259),
(83, 24, 863, 1, 5, 1, 139),
(84, 26, 863, 1, 5, 0.35, 189),
(85, 29, 863, 1, 5, 0.3, 86);

-- --------------------------------------------------------

--
-- Структура таблицы `unit_of_measurement`
--

CREATE TABLE `unit_of_measurement` (
  `id_unit_of_measurement` int NOT NULL,
  `unit_of_measurement` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `unit_of_measurement`
--

INSERT INTO `unit_of_measurement` (`id_unit_of_measurement`, `unit_of_measurement`) VALUES
(1, 'Кг'),
(2, 'шт'),
(3, 'литр');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `composition_dish`
--
ALTER TABLE `composition_dish`
  ADD KEY `id_dishes` (`id_dishes`),
  ADD KEY `id_product` (`id_product`),
  ADD KEY `id_unit_of_measurement` (`id_unit_of_measurement`);

--
-- Индексы таблицы `container`
--
ALTER TABLE `container`
  ADD PRIMARY KEY (`id_container`);

--
-- Индексы таблицы `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id_customer`);

--
-- Индексы таблицы `dishes`
--
ALTER TABLE `dishes`
  ADD PRIMARY KEY (`id_dishes`);

--
-- Индексы таблицы `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id_events`),
  ADD KEY `id_customer` (`id_customer`);

--
-- Индексы таблицы `events_in_dishes`
--
ALTER TABLE `events_in_dishes`
  ADD KEY `id_events` (`id_events`),
  ADD KEY `id_dishes` (`id_dishes`);

--
-- Индексы таблицы `manufacturer`
--
ALTER TABLE `manufacturer`
  ADD PRIMARY KEY (`id_manufacturer`);

--
-- Индексы таблицы `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id_product`);

--
-- Индексы таблицы `product_options`
--
ALTER TABLE `product_options`
  ADD PRIMARY KEY (`id_product_options`),
  ADD KEY `id_product` (`id_product`),
  ADD KEY `id_container` (`id_container`),
  ADD KEY `id_unit_of_measurement` (`id_unit_of_measurement`),
  ADD KEY `id_manufacturer` (`id_manufacturer`);

--
-- Индексы таблицы `unit_of_measurement`
--
ALTER TABLE `unit_of_measurement`
  ADD PRIMARY KEY (`id_unit_of_measurement`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `container`
--
ALTER TABLE `container`
  MODIFY `id_container` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=868;

--
-- AUTO_INCREMENT для таблицы `customer`
--
ALTER TABLE `customer`
  MODIFY `id_customer` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT для таблицы `dishes`
--
ALTER TABLE `dishes`
  MODIFY `id_dishes` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT для таблицы `events`
--
ALTER TABLE `events`
  MODIFY `id_events` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT для таблицы `manufacturer`
--
ALTER TABLE `manufacturer`
  MODIFY `id_manufacturer` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `product`
--
ALTER TABLE `product`
  MODIFY `id_product` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=68;

--
-- AUTO_INCREMENT для таблицы `product_options`
--
ALTER TABLE `product_options`
  MODIFY `id_product_options` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;

--
-- AUTO_INCREMENT для таблицы `unit_of_measurement`
--
ALTER TABLE `unit_of_measurement`
  MODIFY `id_unit_of_measurement` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `composition_dish`
--
ALTER TABLE `composition_dish`
  ADD CONSTRAINT `composition_dish_ibfk_1` FOREIGN KEY (`id_dishes`) REFERENCES `dishes` (`id_dishes`),
  ADD CONSTRAINT `composition_dish_ibfk_2` FOREIGN KEY (`id_product`) REFERENCES `product` (`id_product`),
  ADD CONSTRAINT `composition_dish_ibfk_3` FOREIGN KEY (`id_unit_of_measurement`) REFERENCES `unit_of_measurement` (`id_unit_of_measurement`);

--
-- Ограничения внешнего ключа таблицы `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `events_ibfk_1` FOREIGN KEY (`id_customer`) REFERENCES `customer` (`id_customer`);

--
-- Ограничения внешнего ключа таблицы `events_in_dishes`
--
ALTER TABLE `events_in_dishes`
  ADD CONSTRAINT `events_in_dishes_ibfk_1` FOREIGN KEY (`id_dishes`) REFERENCES `dishes` (`id_dishes`),
  ADD CONSTRAINT `events_in_dishes_ibfk_2` FOREIGN KEY (`id_events`) REFERENCES `events` (`id_events`);

--
-- Ограничения внешнего ключа таблицы `product_options`
--
ALTER TABLE `product_options`
  ADD CONSTRAINT `product_options_ibfk_2` FOREIGN KEY (`id_product`) REFERENCES `product` (`id_product`),
  ADD CONSTRAINT `product_options_ibfk_3` FOREIGN KEY (`id_unit_of_measurement`) REFERENCES `unit_of_measurement` (`id_unit_of_measurement`),
  ADD CONSTRAINT `product_options_ibfk_4` FOREIGN KEY (`id_manufacturer`) REFERENCES `manufacturer` (`id_manufacturer`),
  ADD CONSTRAINT `product_options_ibfk_5` FOREIGN KEY (`id_container`) REFERENCES `container` (`id_container`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
