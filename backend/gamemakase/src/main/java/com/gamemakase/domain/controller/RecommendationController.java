package com.gamemakase.domain.controller;

import com.gamemakase.domain.model.dto.RecommendationResponseDto;
import com.gamemakase.domain.model.service.RecommendationService;
import com.gamemakase.global.Exception.NotFoundException;
import com.gamemakase.global.Exception.TokenValidFailedException;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Api(value = "추천 결과 관련 api")
@RequiredArgsConstructor
@RestController
@Slf4j
public class RecommendationController {

    private final RecommendationService recommendationService;

    @ApiOperation(value = "개인 맞춤 추천", notes = "페이징해서 보내드립니다.")
    @GetMapping("/api/recommend/games")
    public ResponseEntity<List<RecommendationResponseDto>> getByUserId(
            @RequestHeader("accessToken") @ApiParam(required = true) String token,
            @RequestParam(name = "page", required = false) Integer pageNo,
            @RequestParam(name = "size", required = false) Integer pageSize
    )
            throws NotFoundException, TokenValidFailedException
    {
        return ResponseEntity.status(HttpStatus.OK).body(recommendationService.getByUserId(pageNo, pageSize, token));
    }
}
