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
import org.openapitools.client.model.DistrictRanking;
import org.openapitools.client.model.Event;
import org.openapitools.client.model.EventSimple;
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
 * API tests for ListApi
 */
@Disabled
public class ListApiTest {

    private final ListApi api = new ListApi();

    /**
     * Gets a list of event keys for events in the given district.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDistrictEventsKeys_1Test() throws ApiException {
        String districtKey = null;
        String ifNoneMatch = null;
        List<String> response = api.getDistrictEventsKeys_1(districtKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form list of events in the given district.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDistrictEventsSimple_1Test() throws ApiException {
        String districtKey = null;
        String ifNoneMatch = null;
        List<EventSimple> response = api.getDistrictEventsSimple_1(districtKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of events in the given district.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDistrictEvents_1Test() throws ApiException {
        String districtKey = null;
        String ifNoneMatch = null;
        List<Event> response = api.getDistrictEvents_1(districtKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of team district rankings for the given district.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDistrictRankings_1Test() throws ApiException {
        String districtKey = null;
        String ifNoneMatch = null;
        List<DistrictRanking> response = api.getDistrictRankings_1(districtKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of &#x60;Team&#x60; objects that competed in events in the given district.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDistrictTeamsKeys_1Test() throws ApiException {
        String districtKey = null;
        String ifNoneMatch = null;
        List<String> response = api.getDistrictTeamsKeys_1(districtKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form list of &#x60;Team&#x60; objects that competed in events in the given district.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDistrictTeamsSimple_1Test() throws ApiException {
        String districtKey = null;
        String ifNoneMatch = null;
        List<TeamSimple> response = api.getDistrictTeamsSimple_1(districtKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of &#x60;Team&#x60; objects that competed in events in the given district.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDistrictTeams_1Test() throws ApiException {
        String districtKey = null;
        String ifNoneMatch = null;
        List<Team> response = api.getDistrictTeams_1(districtKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of &#x60;Team&#x60; keys that competed in the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventTeamsKeys_1Test() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<String> response = api.getEventTeamsKeys_1(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form list of &#x60;Team&#x60; objects that competed in the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventTeamsSimple_1Test() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<TeamSimple> response = api.getEventTeamsSimple_1(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a key-value list of the event statuses for teams competing at the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventTeamsStatuses_1Test() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        Map<String, TeamEventStatus> response = api.getEventTeamsStatuses_1(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of &#x60;Team&#x60; objects that competed in the given event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventTeams_1Test() throws ApiException {
        String eventKey = null;
        String ifNoneMatch = null;
        List<Team> response = api.getEventTeams_1(eventKey, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of event keys in the given year.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventsByYearKeys_0Test() throws ApiException {
        Integer year = null;
        String ifNoneMatch = null;
        List<String> response = api.getEventsByYearKeys_0(year, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a short-form list of events in the given year.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventsByYearSimple_0Test() throws ApiException {
        Integer year = null;
        String ifNoneMatch = null;
        List<EventSimple> response = api.getEventsByYearSimple_0(year, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of events in the given year.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getEventsByYear_0Test() throws ApiException {
        Integer year = null;
        String ifNoneMatch = null;
        List<Event> response = api.getEventsByYear_0(year, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a key-value list of the event statuses for events this team has competed at in the given year.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamEventsStatusesByYearTest() throws ApiException {
        String teamKey = null;
        Integer year = null;
        String ifNoneMatch = null;
        Map<String, TeamEventStatus> response = api.getTeamEventsStatusesByYear(teamKey, year, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list Team Keys that competed in the given year, paginated in groups of 500.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamsByYearKeys_0Test() throws ApiException {
        Integer year = null;
        Integer pageNum = null;
        String ifNoneMatch = null;
        List<String> response = api.getTeamsByYearKeys_0(year, pageNum, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of short form &#x60;Team_Simple&#x60; objects that competed in the given year, paginated in groups of 500.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamsByYearSimple_0Test() throws ApiException {
        Integer year = null;
        Integer pageNum = null;
        String ifNoneMatch = null;
        List<TeamSimple> response = api.getTeamsByYearSimple_0(year, pageNum, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of &#x60;Team&#x60; objects that competed in the given year, paginated in groups of 500.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamsByYear_0Test() throws ApiException {
        Integer year = null;
        Integer pageNum = null;
        String ifNoneMatch = null;
        List<Team> response = api.getTeamsByYear_0(year, pageNum, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of Team keys, paginated in groups of 500. (Note, each page will not have 500 teams, but will include the teams within that range of 500.)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamsKeys_0Test() throws ApiException {
        Integer pageNum = null;
        String ifNoneMatch = null;
        List<String> response = api.getTeamsKeys_0(pageNum, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of short form &#x60;Team_Simple&#x60; objects, paginated in groups of 500.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeamsSimple_0Test() throws ApiException {
        Integer pageNum = null;
        String ifNoneMatch = null;
        List<TeamSimple> response = api.getTeamsSimple_0(pageNum, ifNoneMatch);
        // TODO: test validations
    }

    /**
     * Gets a list of &#x60;Team&#x60; objects, paginated in groups of 500.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTeams_0Test() throws ApiException {
        Integer pageNum = null;
        String ifNoneMatch = null;
        List<Team> response = api.getTeams_0(pageNum, ifNoneMatch);
        // TODO: test validations
    }

}
