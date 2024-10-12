/*
 * LoL v3 Scores
 * LoL v3 Scores
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
import org.openapitools.client.model.Area;
import org.openapitools.client.model.Competition;
import org.openapitools.client.model.CompetitionDetail;
import org.openapitools.client.model.Game;
import org.openapitools.client.model.Membership;
import org.openapitools.client.model.Player;
import org.openapitools.client.model.SeasonTeam;
import org.openapitools.client.model.Standing;
import org.openapitools.client.model.Team;
import org.openapitools.client.model.Venue;
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
     * Areas (Countries)
     *
     * Areas (Countries)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void areasCountriesTest() throws ApiException {
        String format = null;
        List<Area> response = api.areasCountries(format);
        // TODO: test validations
    }

    /**
     * Competition Fixtures (League Details)
     *
     * Competition Fixtures (League Details)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void competitionFixturesLeagueDetailsTest() throws ApiException {
        String format = null;
        String competitionid = null;
        CompetitionDetail response = api.competitionFixturesLeagueDetails(format, competitionid);
        // TODO: test validations
    }

    /**
     * Competitions (Leagues)
     *
     * Competitions (Leagues)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void competitionsLeaguesTest() throws ApiException {
        String format = null;
        List<Competition> response = api.competitionsLeagues(format);
        // TODO: test validations
    }

    /**
     * Games by Date
     *
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
     * Memberships (Active)
     *
     * Memberships (Active)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void membershipsActiveTest() throws ApiException {
        String format = null;
        List<Membership> response = api.membershipsActive(format);
        // TODO: test validations
    }

    /**
     * Memberships by Team (Active)
     *
     * Memberships by Team (Active)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void membershipsByTeamActiveTest() throws ApiException {
        String format = null;
        String teamid = null;
        List<Membership> response = api.membershipsByTeamActive(format, teamid);
        // TODO: test validations
    }

    /**
     * Memberships by Team (Historical)
     *
     * Memberships by Team (Historical)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void membershipsByTeamHistoricalTest() throws ApiException {
        String format = null;
        String teamid = null;
        List<Membership> response = api.membershipsByTeamHistorical(format, teamid);
        // TODO: test validations
    }

    /**
     * Memberships (Historical)
     *
     * Memberships (Historical)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void membershipsHistoricalTest() throws ApiException {
        String format = null;
        List<Membership> response = api.membershipsHistorical(format);
        // TODO: test validations
    }

    /**
     * Player
     *
     * Player
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void playerTest() throws ApiException {
        String format = null;
        String playerid = null;
        Player response = api.player(format, playerid);
        // TODO: test validations
    }

    /**
     * Players
     *
     * Players
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void playersTest() throws ApiException {
        String format = null;
        List<Player> response = api.players(format);
        // TODO: test validations
    }

    /**
     * Players by Team
     *
     * Players by Team
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void playersByTeamTest() throws ApiException {
        String format = null;
        String teamid = null;
        List<Player> response = api.playersByTeam(format, teamid);
        // TODO: test validations
    }

    /**
     * Schedule
     *
     * Schedule
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void scheduleTest() throws ApiException {
        String format = null;
        String roundid = null;
        List<Game> response = api.schedule(format, roundid);
        // TODO: test validations
    }

    /**
     * Season Teams
     *
     * Season Teams
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seasonTeamsTest() throws ApiException {
        String format = null;
        String seasonid = null;
        List<SeasonTeam> response = api.seasonTeams(format, seasonid);
        // TODO: test validations
    }

    /**
     * Standings
     *
     * Standings
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void standingsTest() throws ApiException {
        String format = null;
        String roundid = null;
        List<Standing> response = api.standings(format, roundid);
        // TODO: test validations
    }

    /**
     * Teams
     *
     * Teams
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void teamsTest() throws ApiException {
        String format = null;
        List<Team> response = api.teams(format);
        // TODO: test validations
    }

    /**
     * Venues
     *
     * Venues
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void venuesTest() throws ApiException {
        String format = null;
        List<Venue> response = api.venues(format);
        // TODO: test validations
    }

}
