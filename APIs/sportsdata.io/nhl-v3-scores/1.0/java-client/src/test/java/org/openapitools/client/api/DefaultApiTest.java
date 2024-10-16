/*
 * NHL v3 Scores
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
import org.openapitools.client.model.Game;
import org.openapitools.client.model.News;
import org.openapitools.client.model.Player;
import org.openapitools.client.model.PlayerBasic;
import org.openapitools.client.model.ScheduleBasic;
import org.openapitools.client.model.ScoreBasic;
import org.openapitools.client.model.Season;
import org.openapitools.client.model.Stadium;
import org.openapitools.client.model.Standing;
import org.openapitools.client.model.Team;
import org.openapitools.client.model.TeamGame;
import org.openapitools.client.model.TeamSeason;
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
     * Are Games In Progress
     *
     * Returns &lt;code&gt;true&lt;/code&gt; if there is at least one game being played at the time of the request or &lt;code&gt;false&lt;/code&gt; if there are none.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void areGamesInProgressTest() throws ApiException {
        String format = null;
        Boolean response = api.areGamesInProgress(format);
        // TODO: test validations
    }

    /**
     * Current Season
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void currentSeasonTest() throws ApiException {
        String format = null;
        Season response = api.currentSeason(format);
        // TODO: test validations
    }

    /**
     * Games by Date
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void gamesByDateTest() throws ApiException {
        String format = null;
        String date = null;
        List<Game> response = api.gamesByDate(format, date);
        // TODO: test validations
    }

    /**
     * Games by Date (Basic)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void gamesByDateBasicTest() throws ApiException {
        String format = null;
        String date = null;
        List<ScoreBasic> response = api.gamesByDateBasic(format, date);
        // TODO: test validations
    }

    /**
     * News
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void newsTest() throws ApiException {
        String format = null;
        List<News> response = api.news(format);
        // TODO: test validations
    }

    /**
     * News by Date
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void newsByDateTest() throws ApiException {
        String format = null;
        String date = null;
        List<News> response = api.newsByDate(format, date);
        // TODO: test validations
    }

    /**
     * News by Player
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void newsByPlayerTest() throws ApiException {
        String format = null;
        String playerid = null;
        List<News> response = api.newsByPlayer(format, playerid);
        // TODO: test validations
    }

    /**
     * Player Details by Active
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void playerDetailsByActiveTest() throws ApiException {
        String format = null;
        List<Player> response = api.playerDetailsByActive(format);
        // TODO: test validations
    }

    /**
     * Player Details by Free Agent
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void playerDetailsByFreeAgentTest() throws ApiException {
        String format = null;
        List<Player> response = api.playerDetailsByFreeAgent(format);
        // TODO: test validations
    }

    /**
     * Player Details by Player
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void playerDetailsByPlayerTest() throws ApiException {
        String format = null;
        String playerid = null;
        Player response = api.playerDetailsByPlayer(format, playerid);
        // TODO: test validations
    }

    /**
     * Players by Team
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void playersByTeamTest() throws ApiException {
        String format = null;
        String team = null;
        List<Player> response = api.playersByTeam(format, team);
        // TODO: test validations
    }

    /**
     * Players by Team (Basic)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void playersByTeamBasicTest() throws ApiException {
        String format = null;
        String team = null;
        List<PlayerBasic> response = api.playersByTeamBasic(format, team);
        // TODO: test validations
    }

    /**
     * Schedules
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void schedulesTest() throws ApiException {
        String format = null;
        String season = null;
        List<Game> response = api.schedules(format, season);
        // TODO: test validations
    }

    /**
     * Schedules (Basic)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void schedulesBasicTest() throws ApiException {
        String format = null;
        String season = null;
        List<ScheduleBasic> response = api.schedulesBasic(format, season);
        // TODO: test validations
    }

    /**
     * Stadiums
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void stadiumsTest() throws ApiException {
        String format = null;
        List<Stadium> response = api.stadiums(format);
        // TODO: test validations
    }

    /**
     * Standings
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void standingsTest() throws ApiException {
        String format = null;
        String season = null;
        List<Standing> response = api.standings(format, season);
        // TODO: test validations
    }

    /**
     * Team Game Logs By Season
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void teamGameLogsBySeasonTest() throws ApiException {
        String format = null;
        String season = null;
        String teamid = null;
        String numberofgames = null;
        List<TeamGame> response = api.teamGameLogsBySeason(format, season, teamid, numberofgames);
        // TODO: test validations
    }

    /**
     * Team Game Stats by Date
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void teamGameStatsByDateTest() throws ApiException {
        String format = null;
        String date = null;
        List<TeamGame> response = api.teamGameStatsByDate(format, date);
        // TODO: test validations
    }

    /**
     * Team Season Stats
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void teamSeasonStatsTest() throws ApiException {
        String format = null;
        String season = null;
        List<TeamSeason> response = api.teamSeasonStats(format, season);
        // TODO: test validations
    }

    /**
     * Teams (Active)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void teamsActiveTest() throws ApiException {
        String format = null;
        List<Team> response = api.teamsActive(format);
        // TODO: test validations
    }

    /**
     * Teams (All)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void teamsAllTest() throws ApiException {
        String format = null;
        List<Team> response = api.teamsAll(format);
        // TODO: test validations
    }

}
