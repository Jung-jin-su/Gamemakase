package com.gamemakase.domain.model.repository;

import com.gamemakase.domain.model.dto.GameResponseDto;
import com.gamemakase.domain.model.entity.Game;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface GameRepository extends JpaRepository<Game, Long> {

    Optional<Game> findByGameId(Long gameId);

    @Query(value = "select * from game where upper(game_name) like upper(concat('%', :gameName, '%')) " +
            "order by case when game_name = :gameName then 0 " +
            "when upper(game_name) = upper(:gameName) then 1 " +
            "when game_name like concat(:gameName, '%') then 2 " +
            "when upper(game_name) like upper(concat(:gameName, '%')) then 3 " +
            "when game_name like concat('%', :gameName, '%') then 4 " +
            "when upper(game_name) like upper(concat('%', :gameName, '%')) then 5 " +
            "when upper(game_name) like upper(concat(:gameName, '%')) then 6 " +
            "else 7 end"
    		, nativeQuery = true)
    Page<Game> findAllByGameNameLikeOrderByGameName(@Param("gameName") String gameName, Pageable pageable);

    List<Game> findTop100ByOrderByPeakCcuDesc();

    @Query("SELECT new com.gamemakase.domain.model.dto.GameResponseDto(g.gameId, g.gameName, i.imagePath) " +
            "FROM Game g " +
            "LEFT JOIN Image i ON g.gameId = i.typeId " +
            "WHERE i.type = 'GAME_HEADER' AND g.peakCcu IS NOT NULL " +
            "ORDER BY g.peakCcu DESC")
    Page<GameResponseDto> findTop100GamesWithImagesOrderByPeakCcuDesc(Pageable pageable);

    @Query("SELECT new com.gamemakase.domain.model.dto.GameResponseDto(g.gameId, g.gameName, i.imagePath) " +
            "FROM Game g " +
            "LEFT JOIN Image i ON g.gameId = i.typeId " +
            "WHERE i.type = 'GAME_HEADER' AND g.peakCcu IS NOT NULL " +
            "AND (g.score >= 95 or g.recommendations >= 50000)" +
            "ORDER BY RAND()")
    Page<GameResponseDto> getAllByScoreGreaterThanEqual95OrRecommendationsGreaterThanEqual50000(Pageable pageable);









}
