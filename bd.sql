CREATE DATABASE IF NOT EXISTS notes_python;
use notes_python;

CREATE TABLE IF NOT EXISTS `users` (
  `id`          INT(25)        NOT NULL AUTO_INCREMENT,
  `name`        VARCHAR(255),
  `lastname`    VARCHAR(255),
  `email`       VARCHAR(255)   NOT NULL,
  `password`    VARCHAR(255)   NOT NULL,
  `fecha`       DATE           NOT NULL,
  PRIMARY KEY `pk_users`(`id`),
  CONSTRAINT  `uq_email` UNIQUE(email)
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;


CREATE TABLE IF NOT EXISTS `notas` (
  `id`          INT(25)        NOT NULL AUTO_INCREMENT,
  `user_id`     INT(25)        NOT NULL,
  `title`       VARCHAR(255),
  `description` VARCHAR(255),
  `fecha`       DATE           NOT NULL,
  PRIMARY KEY `pk_notas`(`id`),
  INDEX `fk_nota_users`(`user_id`),
  CONSTRAINT `fk_nota_users` FOREIGN KEY(`user_id`) REFERENCES `users`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;
