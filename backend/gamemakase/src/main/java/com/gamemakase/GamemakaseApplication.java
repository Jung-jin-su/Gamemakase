package com.gamemakase;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;
import org.springframework.data.mongodb.config.EnableMongoAuditing;

@SpringBootApplication
@EnableMongoAuditing
@EnableJpaAuditing
public class GamemakaseApplication {

  public static void main(String[] args) {
    SpringApplication.run(GamemakaseApplication.class, args);
  }

}
