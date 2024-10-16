/*
 * Soccer v3 Projections
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.DfsSlate;
import org.openapitools.client.model.Player;
import org.openapitools.client.model.PlayerGameProjection;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * Dfs Slates By Date
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void dfsSlatesByDateTest() throws ApiException {
        String format = null;
        String date = null;
        List<DfsSlate> response = api.dfsSlatesByDate(format, date);
        // TODO: test validations
    }

    /**
     * Injured Players By Competition
     *
     * This endpoint provides all currently injured soccer players by competition, along with injury details.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void injuredPlayersByCompetitionTest() throws ApiException {
        String format = null;
        String competition = null;
        List<Player> response = api.injuredPlayersByCompetition(format, competition);
        // TODO: test validations
    }

    /**
     * Projected Player Game Stats by Competition (w/ DFS Salaries)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void projectedPlayerGameStatsByCompetitionWDfsSalariesTest() throws ApiException {
        String format = null;
        String competition = null;
        String date = null;
        List<PlayerGameProjection> response = api.projectedPlayerGameStatsByCompetitionWDfsSalaries(format, competition, date);
        // TODO: test validations
    }

    /**
     * Projected Player Game Stats by Date (w/ DFS Salaries)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void projectedPlayerGameStatsByDateWDfsSalariesTest() throws ApiException {
        String format = null;
        String date = null;
        List<PlayerGameProjection> response = api.projectedPlayerGameStatsByDateWDfsSalaries(format, date);
        // TODO: test validations
    }

    /**
     * Projected Player Game Stats by Player (w/ DFS Salaries)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void projectedPlayerGameStatsByPlayerWDfsSalariesTest() throws ApiException {
        String format = null;
        String date = null;
        String playerid = null;
        List<PlayerGameProjection> response = api.projectedPlayerGameStatsByPlayerWDfsSalaries(format, date, playerid);
        // TODO: test validations
    }

    /**
     * Upcoming Dfs Slates By Competition
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void upcomingDfsSlatesByCompetitionTest() throws ApiException {
        String format = null;
        String competitionId = null;
        List<DfsSlate> response = api.upcomingDfsSlatesByCompetition(format, competitionId);
        // TODO: test validations
    }

}
