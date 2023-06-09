package com.gamemakase.domain.model.service;

import com.gamemakase.domain.model.dto.GameResponseDto;
import com.gamemakase.domain.model.dto.RecommendationResponseDto;
import com.gamemakase.global.Exception.NotFoundException;
import com.gamemakase.global.Exception.TokenValidFailedException;

import java.util.List;

public interface RecommendationService {

    List<RecommendationResponseDto> getByUserId(Integer pageNo, Integer pageSize, String token) throws NotFoundException, TokenValidFailedException;

    List<RecommendationResponseDto> getByUserIdTest(Integer pageNo, Integer pageSize, Long userId) throws NotFoundException, TokenValidFailedException;

    List<GameResponseDto> getTopGamesInRandomOrder(Integer pageSize);

    List<GameResponseDto> getGamesInRandomOrder(Integer pageSize);

    List<GameResponseDto> getDailyRecommendations();
}
