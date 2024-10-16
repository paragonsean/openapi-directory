/*
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Award;
import org.openapitools.client.model.EliminationAlliance;
import org.openapitools.client.model.Event;
import org.openapitools.client.model.EventDistrictPoints;
import org.openapitools.client.model.EventInsights;
import org.openapitools.client.model.EventOPRs;
import org.openapitools.client.model.EventRanking;
import org.openapitools.client.model.EventSimple;
import org.openapitools.client.model.Match;
import org.openapitools.client.model.MatchSimple;
import org.openapitools.client.model.Team;
import org.openapitools.client.model.TeamEventStatus;
import org.openapitools.client.model.TeamSimple;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for EventApi
 */
@Disabled
public class EventApiTest {

    private final EventApi api = new EventApi();

    /**
     * Gets a list of event keys for events in the given district.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDistrictEventsKeys_0Test() throws ApiException {
        String districtKey = null;
        String ifNoneMatch = null;
        List<String> response = api.getDistrictEventsKeys_0(districtKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form list of events in the given district.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDistrictEventsSimple_0Test() throws ApiException {
        String districtKey = null;
        String ifNoneMatch = null;
        List<EventSimple> response = api.getDistrictEventsSimple_0(districtKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of events in the given district.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDistrictEvents_0Test() throws ApiException {
        String districtKey = null;
        String ifNoneMatch = null;
        List<Event> response = api.getDistrictEvents_0(districtKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets an Event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        Event response = api.getEvent(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of Elimination Alliances for the given Event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventAlliancesTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<EliminationAlliance> response = api.getEventAlliances(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of awards from the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventAwardsTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<Award> response = api.getEventAwards(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of team rankings for the Event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventDistrictPointsTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        EventDistrictPoints response = api.getEventDistrictPoints(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a set of Event-specific insights for the given Event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventInsightsTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        EventInsights response = api.getEventInsights(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets an array of Match Keys for the given event key that have timeseries data. Returns an empty array if no matches have timeseries data. *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do not rely on this data for any purpose. In fact, pretend we made it up. *WARNING:* This endpoint and corresponding data models are under *active development* and may change at any time, including in breaking ways.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventMatchTimeseriesTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<String> response = api.getEventMatchTimeseries(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of matches for the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventMatchesTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<Match> response = api.getEventMatches(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of match keys for the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventMatchesKeysTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<String> response = api.getEventMatchesKeys(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form list of matches for the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventMatchesSimpleTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<MatchSimple> response = api.getEventMatchesSimple(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a set of Event OPRs (including OPR, DPR, and CCWM) for the given Event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventOPRsTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        EventOPRs response = api.getEventOPRs(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets information on TBA-generated predictions for the given Event. Contains year-specific information. *WARNING* This endpoint is currently under development and may change at any time.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventPredictionsTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        Object response = api.getEventPredictions(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of team rankings for the Event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventRankingsTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        EventRanking response = api.getEventRankings(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form Event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventSimpleTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        EventSimple response = api.getEventSimple(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of &#x60;Team&#x60; objects that competed in the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventTeamsTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<Team> response = api.getEventTeams(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of &#x60;Team&#x60; keys that competed in the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventTeamsKeysTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<String> response = api.getEventTeamsKeys(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form list of &#x60;Team&#x60; objects that competed in the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventTeamsSimpleTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<TeamSimple> response = api.getEventTeamsSimple(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a key-value list of the event statuses for teams competing at the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventTeamsStatusesTest() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        Map<String, TeamEventStatus> response = api.getEventTeamsStatuses(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of events in the given year.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventsByYearTest() throws ApiException {
        Integer year = null;
        String ifNoneMatch = null;
        List<Event> response = api.getEventsByYear(year, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of event keys in the given year.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventsByYearKeysTest() throws ApiException {
        Integer year = null;
        String ifNoneMatch = null;
        List<String> response = api.getEventsByYearKeys(year, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form list of events in the given year.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventsByYearSimpleTest() throws ApiException {
        Integer year = null;
        String ifNoneMatch = null;
        List<EventSimple> response = api.getEventsByYearSimple(year, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of awards the given team won at the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventAwards_0Test() throws ApiException {
        String teamKey = null;
        String eventKey = null;
        String ifNoneMatch = null;
        List<Award> response = api.getTeamEventAwards_0(teamKey, eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of match keys for matches for the given team and event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventMatchesKeys_0Test() throws ApiException {
        String teamKey = null;
        String eventKey = null;
        String ifNoneMatch = null;
        List<String> response = api.getTeamEventMatchesKeys_0(teamKey, eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form list of matches for the given team and event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventMatchesSimple_0Test() throws ApiException {
        String teamKey = null;
        String eventKey = null;
        String ifNoneMatch = null;
        List<Match> response = api.getTeamEventMatchesSimple_0(teamKey, eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of matches for the given team and event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventMatches_0Test() throws ApiException {
        String teamKey = null;
        String eventKey = null;
        String ifNoneMatch = null;
        List<Match> response = api.getTeamEventMatches_0(teamKey, eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets the competition rank and status of the team at the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventStatus_0Test() throws ApiException {
        String teamKey = null;
        String eventKey = null;
        String ifNoneMatch = null;
        TeamEventStatus response = api.getTeamEventStatus_0(teamKey, eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of the event keys for events this team has competed at in the given year.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventsByYearKeys_0Test() throws ApiException {
        String teamKey = null;
        Integer year = null;
        String ifNoneMatch = null;
        List<String> response = api.getTeamEventsByYearKeys_0(teamKey, year, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form list of events this team has competed at in the given year.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventsByYearSimple_0Test() throws ApiException {
        String teamKey = null;
        Integer year = null;
        String ifNoneMatch = null;
        List<EventSimple> response = api.getTeamEventsByYearSimple_0(teamKey, year, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of events this team has competed at in the given year.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventsByYear_0Test() throws ApiException {
        String teamKey = null;
        Integer year = null;
        String ifNoneMatch = null;
        List<Event> response = api.getTeamEventsByYear_0(teamKey, year, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of the event keys for all events this team has competed at.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventsKeys_0Test() throws ApiException {
        String teamKey = null;
        String ifNoneMatch = null;
        List<String> response = api.getTeamEventsKeys_0(teamKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form list of all events this team has competed at.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventsSimple_0Test() throws ApiException {
        String teamKey = null;
        String ifNoneMatch = null;
        List<EventSimple> response = api.getTeamEventsSimple_0(teamKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a key-value list of the event statuses for events this team has competed at in the given year.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventsStatusesByYear_1Test() throws ApiException {
        String teamKey = null;
        Integer year = null;
        String ifNoneMatch = null;
        Map<String, TeamEventStatus> response = api.getTeamEventsStatusesByYear_1(teamKey, year, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of all events this team has competed at.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEvents_0Test() throws ApiException {
        String teamKey = null;
        String ifNoneMatch = null;
        List<Event> response = api.getTeamEvents_0(teamKey, ifNoneMatch);
        // TODO: test validations
    }

}
