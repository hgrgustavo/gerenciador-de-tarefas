-- MySQL Script generated by MySQL Workbench
-- Fri Mar 28 20:10:00 2025
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_crud_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_crud_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_crud_schema` DEFAULT CHARACTER SET utf8 ;
USE `db_crud_schema` ;


-- -----------------------------------------------------
-- Table `db_crud_schema`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_crud_schema`.`usuario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_crud_schema`.`tasks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_crud_schema`.`tarefa` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario_id` INT NOT NULL,
  `descricao` TEXT NOT NULL,
  `setor` VARCHAR(255) NOT NULL,
  `prioridade` ENUM("baixa", "media", "alta") NOT NULL,
  `data_cadastro` DATE NOT NULL,
  `status` ENUM("a fazer", "fazendo", "´pronto") NOT NULL DEFAULT "a fazer",
  PRIMARY KEY (`id`, `usuario_id`),
  INDEX `fk_tarefa_usuario_idx` (`usuario_id` ASC) VISIBLE,
  UNIQUE INDEX `setor_UNIQUE` (`setor` ASC) VISIBLE,
  CONSTRAINT `fk_tarefa_usuario`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `db_crud_schema`.`usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
