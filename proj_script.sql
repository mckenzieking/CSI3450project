-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`ADMIN`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ADMIN` (
  `ADMIN_ID` INT NOT NULL,
  `ADMIN_FNAME` VARCHAR(45) NOT NULL,
  `ADMIN_LNAME` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ADMIN_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`MENU`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`MENU` (
  `MENU_ITEM_ID` INT NOT NULL,
  `MENU_ITEM_NAME` VARCHAR(45) NOT NULL,
  `MENU_QUANT` INT NOT NULL,
  `MENU_PRICE` DECIMAL(2) NOT NULL,
  `MENU_CATEG` VARCHAR(45) NOT NULL,
  `MENU_CALS` INT NOT NULL,
  `ADMIN_ADMIN_ID` INT NOT NULL,
  PRIMARY KEY (`MENU_ITEM_ID`, `ADMIN_ADMIN_ID`),
  INDEX `fk_MENU_ADMIN1_idx` (`ADMIN_ADMIN_ID` ASC),
  CONSTRAINT `fk_MENU_ADMIN1`
    FOREIGN KEY (`ADMIN_ADMIN_ID`)
    REFERENCES `mydb`.`ADMIN` (`ADMIN_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CUSTOMER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`CUSTOMER` (
  `CUST_ID` INT NOT NULL,
  `CUST_FNAME` VARCHAR(45) NOT NULL,
  `CUST_LNAME` VARCHAR(45) NOT NULL,
  `CUST_PHONE` VARCHAR(45) NOT NULL,
  `MENU_MENU_ITEM_ID` INT NOT NULL,
  `MENU_ADMIN_ADMIN_ID` INT NOT NULL,
  PRIMARY KEY (`CUST_ID`, `MENU_MENU_ITEM_ID`, `MENU_ADMIN_ADMIN_ID`),
  INDEX `fk_CUSTOMER_MENU1_idx` (`MENU_MENU_ITEM_ID` ASC, `MENU_ADMIN_ADMIN_ID` ASC),
  CONSTRAINT `fk_CUSTOMER_MENU1`
    FOREIGN KEY (`MENU_MENU_ITEM_ID` , `MENU_ADMIN_ADMIN_ID`)
    REFERENCES `mydb`.`MENU` (`MENU_ITEM_ID` , `ADMIN_ADMIN_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ORDER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ORDER` (
  `ORD_ITEM_ID` INT NOT NULL,
  `ORD_QUANT` INT NOT NULL,
  `CUSTOMER_CUST_ID` INT NOT NULL,
  `MENU_MENU_ITEM_ID` INT NOT NULL,
  PRIMARY KEY (`ORD_ITEM_ID`, `CUSTOMER_CUST_ID`, `MENU_MENU_ITEM_ID`),
  INDEX `fk_ORDER_CUSTOMER_idx` (`CUSTOMER_CUST_ID` ASC),
  INDEX `fk_ORDER_MENU1_idx` (`MENU_MENU_ITEM_ID` ASC),
  CONSTRAINT `fk_ORDER_CUSTOMER`
    FOREIGN KEY (`CUSTOMER_CUST_ID`)
    REFERENCES `mydb`.`CUSTOMER` (`CUST_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ORDER_MENU1`
    FOREIGN KEY (`MENU_MENU_ITEM_ID`)
    REFERENCES `mydb`.`MENU` (`MENU_ITEM_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ADMIN_has_CUSTOMER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ADMIN_has_CUSTOMER` (
  `ADMIN_ADMIN_ID` INT NOT NULL,
  `CUSTOMER_CUST_ID` INT NOT NULL,
  `CUSTOMER_MENU_MENU_ITEM_ID` INT NOT NULL,
  `CUSTOMER_MENU_ADMIN_ADMIN_ID` INT NOT NULL,
  PRIMARY KEY (`ADMIN_ADMIN_ID`, `CUSTOMER_CUST_ID`, `CUSTOMER_MENU_MENU_ITEM_ID`, `CUSTOMER_MENU_ADMIN_ADMIN_ID`),
  INDEX `fk_ADMIN_has_CUSTOMER_CUSTOMER1_idx` (`CUSTOMER_CUST_ID` ASC, `CUSTOMER_MENU_MENU_ITEM_ID` ASC, `CUSTOMER_MENU_ADMIN_ADMIN_ID` ASC),
  INDEX `fk_ADMIN_has_CUSTOMER_ADMIN1_idx` (`ADMIN_ADMIN_ID` ASC),
  CONSTRAINT `fk_ADMIN_has_CUSTOMER_ADMIN1`
    FOREIGN KEY (`ADMIN_ADMIN_ID`)
    REFERENCES `mydb`.`ADMIN` (`ADMIN_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ADMIN_has_CUSTOMER_CUSTOMER1`
    FOREIGN KEY (`CUSTOMER_CUST_ID` , `CUSTOMER_MENU_MENU_ITEM_ID` , `CUSTOMER_MENU_ADMIN_ADMIN_ID`)
    REFERENCES `mydb`.`CUSTOMER` (`CUST_ID` , `MENU_MENU_ITEM_ID` , `MENU_ADMIN_ADMIN_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
