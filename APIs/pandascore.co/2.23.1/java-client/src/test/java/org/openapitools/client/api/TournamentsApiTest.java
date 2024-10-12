/*
 * PandaScore REST API for All Videogames
 *  # Introduction  Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \"stages\" and \"groups\".   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.  The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format  ``` Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\" ```  There is also:  * A `X-Page` header field, which contains the current page. * A `X-Per-Page` header field, which contains the current pagination length. * A `X-Total` header field, which contains the total count of items across all pages.  ## Filtering  The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  ``` GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN ```  ## Range  The `range` parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with `hp` within 500 and 1000:  ``` GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN ```  ## Search  The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.  For example, to get all the champions with a name containing `\"twi\"`:  ``` $ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name' \"Twitch\" \"Twisted Fate\" ```  ## Sorting  All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt; 
 *
 * The version of the OpenAPI document: 2.23.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Bracket;
import org.openapitools.client.model.FilterOverBrackets;
import org.openapitools.client.model.FilterOverMatches;
import org.openapitools.client.model.FilterOverPlayers;
import org.openapitools.client.model.FilterOverShortTournaments;
import org.openapitools.client.model.FilterOverTeams;
import org.openapitools.client.model.GetAdditions400Response;
import org.openapitools.client.model.GetAdditionsPageParameter;
import org.openapitools.client.model.Match;
import org.openapitools.client.model.Player;
import org.openapitools.client.model.RangeOverBrackets;
import org.openapitools.client.model.RangeOverMatches;
import org.openapitools.client.model.RangeOverPlayers;
import org.openapitools.client.model.RangeOverShortTournaments;
import org.openapitools.client.model.RangeOverTeams;
import org.openapitools.client.model.SearchOverBrackets;
import org.openapitools.client.model.SearchOverMatches;
import org.openapitools.client.model.SearchOverPlayers;
import org.openapitools.client.model.SearchOverShortTournaments;
import org.openapitools.client.model.SearchOverTeams;
import org.openapitools.client.model.ShortTournament;
import org.openapitools.client.model.Standing;
import org.openapitools.client.model.Team;
import org.openapitools.client.model.Tournament;
import org.openapitools.client.model.TournamentIDOrSlug;
import org.openapitools.client.model.TournamentRosters;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TournamentsApi
 */
@Disabled
public class TournamentsApiTest {

    private final TournamentsApi api = new TournamentsApi();

    /**
     * List tournaments
     *
     * List tournaments
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTournamentsTest() throws ApiException {
        FilterOverShortTournaments filter = null;
        SearchOverShortTournaments search = null;
        List<String> sort = null;
        RangeOverShortTournaments range = null;
        GetAdditionsPageParameter page = null;
        Integer perPage = null;
        List<ShortTournament> response = api.getTournaments(filter, search, sort, range, page, perPage);
        // TODO: test validations
    }

    /**
     * Get past tournaments
     *
     * List past tournaments
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTournamentsPastTest() throws ApiException {
        FilterOverShortTournaments filter = null;
        SearchOverShortTournaments search = null;
        List<String> sort = null;
        RangeOverShortTournaments range = null;
        GetAdditionsPageParameter page = null;
        Integer perPage = null;
        List<ShortTournament> response = api.getTournamentsPast(filter, search, sort, range, page, perPage);
        // TODO: test validations
    }

    /**
     * Get running tournaments
     *
     * List currently running tournaments
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTournamentsRunningTest() throws ApiException {
        FilterOverShortTournaments filter = null;
        SearchOverShortTournaments search = null;
        List<String> sort = null;
        RangeOverShortTournaments range = null;
        GetAdditionsPageParameter page = null;
        Integer perPage = null;
        List<ShortTournament> response = api.getTournamentsRunning(filter, search, sort, range, page, perPage);
        // TODO: test validations
    }

    /**
     * Get a tournament
     *
     * Get a single tournament by ID or by slug
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTournamentsTournamentIdOrSlugTest() throws ApiException {
        TournamentIDOrSlug tournamentIdOrSlug = null;
        Tournament response = api.getTournamentsTournamentIdOrSlug(tournamentIdOrSlug);
        // TODO: test validations
    }

    /**
     * Get a tournament&#39;s brackets
     *
     * Get the brackets of the given tournament
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTournamentsTournamentIdOrSlugBracketsTest() throws ApiException {
        TournamentIDOrSlug tournamentIdOrSlug = null;
        FilterOverBrackets filter = null;
        RangeOverBrackets range = null;
        List<String> sort = null;
        SearchOverBrackets search = null;
        GetAdditionsPageParameter page = null;
        Integer perPage = null;
        List<Bracket> response = api.getTournamentsTournamentIdOrSlugBrackets(tournamentIdOrSlug, filter, range, sort, search, page, perPage);
        // TODO: test validations
    }

    /**
     * Get matches for tournament
     *
     * List matches for the given tournament
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTournamentsTournamentIdOrSlugMatchesTest() throws ApiException {
        TournamentIDOrSlug tournamentIdOrSlug = null;
        FilterOverMatches filter = null;
        SearchOverMatches search = null;
        List<String> sort = null;
        RangeOverMatches range = null;
        GetAdditionsPageParameter page = null;
        Integer perPage = null;
        List<Match> response = api.getTournamentsTournamentIdOrSlugMatches(tournamentIdOrSlug, filter, search, sort, range, page, perPage);
        // TODO: test validations
    }

    /**
     * Get players for a tournament
     *
     * List players for the given tournament
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTournamentsTournamentIdOrSlugPlayersTest() throws ApiException {
        String tournamentIdOrSlug = null;
        FilterOverPlayers filter = null;
        SearchOverPlayers search = null;
        List<String> sort = null;
        RangeOverPlayers range = null;
        GetAdditionsPageParameter page = null;
        Integer perPage = null;
        List<Player> response = api.getTournamentsTournamentIdOrSlugPlayers(tournamentIdOrSlug, filter, search, sort, range, page, perPage);
        // TODO: test validations
    }

    /**
     * Get rosters for a tournament
     *
     * List participants (player or team) for a given tournament.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTournamentsTournamentIdOrSlugRostersTest() throws ApiException {
        TournamentIDOrSlug tournamentIdOrSlug = null;
        TournamentRosters response = api.getTournamentsTournamentIdOrSlugRosters(tournamentIdOrSlug);
        // TODO: test validations
    }

    /**
     * Get tournament standings
     *
     * Get the current standings for a given tournament
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTournamentsTournamentIdOrSlugStandingsTest() throws ApiException {
        TournamentIDOrSlug tournamentIdOrSlug = null;
        GetAdditionsPageParameter page = null;
        Integer perPage = null;
        List<Standing> response = api.getTournamentsTournamentIdOrSlugStandings(tournamentIdOrSlug, page, perPage);
        // TODO: test validations
    }

    /**
     * Get teams for a tournament
     *
     * List teams for the given tournament
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTournamentsTournamentIdOrSlugTeamsTest() throws ApiException {
        TournamentIDOrSlug tournamentIdOrSlug = null;
        FilterOverTeams filter = null;
        SearchOverTeams search = null;
        List<String> sort = null;
        RangeOverTeams range = null;
        GetAdditionsPageParameter page = null;
        Integer perPage = null;
        List<Team> response = api.getTournamentsTournamentIdOrSlugTeams(tournamentIdOrSlug, filter, search, sort, range, page, perPage);
        // TODO: test validations
    }

    /**
     * Get upcoming tournaments
     *
     * List upcoming tournaments
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTournamentsUpcomingTest() throws ApiException {
        FilterOverShortTournaments filter = null;
        SearchOverShortTournaments search = null;
        List<String> sort = null;
        RangeOverShortTournaments range = null;
        GetAdditionsPageParameter page = null;
        Integer perPage = null;
        List<ShortTournament> response = api.getTournamentsUpcoming(filter, search, sort, range, page, perPage);
        // TODO: test validations
    }

}
