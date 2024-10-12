/**
 * PandaScore REST API for All Videogames
 *  # Introduction  Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \"stages\" and \"groups\".   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.  The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format  ``` Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\" ```  There is also:  * A `X-Page` header field, which contains the current page. * A `X-Per-Page` header field, which contains the current pagination length. * A `X-Total` header field, which contains the total count of items across all pages.  ## Filtering  The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  ``` GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN ```  ## Range  The `range` parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with `hp` within 500 and 1000:  ``` GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN ```  ## Search  The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.  For example, to get all the champions with a name containing `\"twi\"`:  ``` $ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name' \"Twitch\" \"Twisted Fate\" ```  ## Sorting  All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt; 
 *
 * The version of the OpenAPI document: 2.23.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import FilterOverLeagues from '../model/FilterOverLeagues';
import FilterOverMatches from '../model/FilterOverMatches';
import FilterOverSeries from '../model/FilterOverSeries';
import FilterOverShortTournaments from '../model/FilterOverShortTournaments';
import FilterOverTeams from '../model/FilterOverTeams';
import GetAdditions400Response from '../model/GetAdditions400Response';
import GetAdditionsPageParameter from '../model/GetAdditionsPageParameter';
import League from '../model/League';
import Match from '../model/Match';
import RangeOverLeagues from '../model/RangeOverLeagues';
import RangeOverMatches from '../model/RangeOverMatches';
import RangeOverSeries from '../model/RangeOverSeries';
import RangeOverShortTournaments from '../model/RangeOverShortTournaments';
import RangeOverTeams from '../model/RangeOverTeams';
import SearchOverLeagues from '../model/SearchOverLeagues';
import SearchOverMatches from '../model/SearchOverMatches';
import SearchOverSeries from '../model/SearchOverSeries';
import SearchOverShortTournaments from '../model/SearchOverShortTournaments';
import SearchOverTeams from '../model/SearchOverTeams';
import Serie from '../model/Serie';
import ShortTournament from '../model/ShortTournament';
import Team from '../model/Team';
import TeamIDOrSlug from '../model/TeamIDOrSlug';

/**
* Teams service.
* @module api/TeamsApi
* @version 2.23.1
*/
export default class TeamsApi {

    /**
    * Constructs a new TeamsApi. 
    * @alias module:api/TeamsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getTeams operation.
     * @callback module:api/TeamsApi~getTeamsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Team>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List teams
     * List teams
     * @param {Object} opts Optional parameters
     * @param {module:model/FilterOverTeams} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/SearchOverTeams} [search] Options to search results
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/RangeOverTeams} [range] Options to select results within ranges
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/TeamsApi~getTeamsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Team>}
     */
    getTeams(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'filter': opts['filter'],
        'search': opts['search'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'multi'),
        'range': opts['range'],
        'page': opts['page'],
        'per_page': opts['perPage']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerToken', 'QueryToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Team];
      return this.apiClient.callApi(
        '/teams', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTeamsTeamIdOrSlug operation.
     * @callback module:api/TeamsApi~getTeamsTeamIdOrSlugCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Team} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a team
     * Get a single team by ID or by slug
     * @param {module:model/TeamIDOrSlug} teamIdOrSlug A team ID or slug
     * @param {module:api/TeamsApi~getTeamsTeamIdOrSlugCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Team}
     */
    getTeamsTeamIdOrSlug(teamIdOrSlug, callback) {
      let postBody = null;
      // verify the required parameter 'teamIdOrSlug' is set
      if (teamIdOrSlug === undefined || teamIdOrSlug === null) {
        throw new Error("Missing the required parameter 'teamIdOrSlug' when calling getTeamsTeamIdOrSlug");
      }

      let pathParams = {
        'team_id_or_slug': teamIdOrSlug
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerToken', 'QueryToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Team;
      return this.apiClient.callApi(
        '/teams/{team_id_or_slug}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTeamsTeamIdOrSlugLeagues operation.
     * @callback module:api/TeamsApi~getTeamsTeamIdOrSlugLeaguesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/League>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get leagues for a team
     * List leagues in which the given team was part of
     * @param {module:model/TeamIDOrSlug} teamIdOrSlug A team ID or slug
     * @param {Object} opts Optional parameters
     * @param {module:model/SearchOverLeagues} [search] Options to search results
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/RangeOverLeagues} [range] Options to select results within ranges
     * @param {module:model/FilterOverLeagues} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/TeamsApi~getTeamsTeamIdOrSlugLeaguesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/League>}
     */
    getTeamsTeamIdOrSlugLeagues(teamIdOrSlug, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'teamIdOrSlug' is set
      if (teamIdOrSlug === undefined || teamIdOrSlug === null) {
        throw new Error("Missing the required parameter 'teamIdOrSlug' when calling getTeamsTeamIdOrSlugLeagues");
      }

      let pathParams = {
        'team_id_or_slug': teamIdOrSlug
      };
      let queryParams = {
        'search': opts['search'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'multi'),
        'range': opts['range'],
        'filter': opts['filter'],
        'page': opts['page'],
        'per_page': opts['perPage']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerToken', 'QueryToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [League];
      return this.apiClient.callApi(
        '/teams/{team_id_or_slug}/leagues', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTeamsTeamIdOrSlugMatches operation.
     * @callback module:api/TeamsApi~getTeamsTeamIdOrSlugMatchesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Match>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get matches for team
     * List matches for the given team
     * @param {module:model/TeamIDOrSlug} teamIdOrSlug A team ID or slug
     * @param {Object} opts Optional parameters
     * @param {module:model/FilterOverMatches} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/SearchOverMatches} [search] Options to search results
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/RangeOverMatches} [range] Options to select results within ranges
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/TeamsApi~getTeamsTeamIdOrSlugMatchesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Match>}
     */
    getTeamsTeamIdOrSlugMatches(teamIdOrSlug, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'teamIdOrSlug' is set
      if (teamIdOrSlug === undefined || teamIdOrSlug === null) {
        throw new Error("Missing the required parameter 'teamIdOrSlug' when calling getTeamsTeamIdOrSlugMatches");
      }

      let pathParams = {
        'team_id_or_slug': teamIdOrSlug
      };
      let queryParams = {
        'filter': opts['filter'],
        'search': opts['search'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'multi'),
        'range': opts['range'],
        'page': opts['page'],
        'per_page': opts['perPage']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerToken', 'QueryToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Match];
      return this.apiClient.callApi(
        '/teams/{team_id_or_slug}/matches', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTeamsTeamIdOrSlugSeries operation.
     * @callback module:api/TeamsApi~getTeamsTeamIdOrSlugSeriesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Serie>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get series for a team
     * List series in which the given team was part of
     * @param {module:model/TeamIDOrSlug} teamIdOrSlug A team ID or slug
     * @param {Object} opts Optional parameters
     * @param {module:model/FilterOverSeries} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/SearchOverSeries} [search] Options to search results
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/RangeOverSeries} [range] Options to select results within ranges
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/TeamsApi~getTeamsTeamIdOrSlugSeriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Serie>}
     */
    getTeamsTeamIdOrSlugSeries(teamIdOrSlug, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'teamIdOrSlug' is set
      if (teamIdOrSlug === undefined || teamIdOrSlug === null) {
        throw new Error("Missing the required parameter 'teamIdOrSlug' when calling getTeamsTeamIdOrSlugSeries");
      }

      let pathParams = {
        'team_id_or_slug': teamIdOrSlug
      };
      let queryParams = {
        'filter': opts['filter'],
        'search': opts['search'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'multi'),
        'range': opts['range'],
        'page': opts['page'],
        'per_page': opts['perPage']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerToken', 'QueryToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Serie];
      return this.apiClient.callApi(
        '/teams/{team_id_or_slug}/series', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTeamsTeamIdOrSlugTournaments operation.
     * @callback module:api/TeamsApi~getTeamsTeamIdOrSlugTournamentsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ShortTournament>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get tournaments for a team
     * List tournaments in which the given team was part of
     * @param {module:model/TeamIDOrSlug} teamIdOrSlug A team ID or slug
     * @param {Object} opts Optional parameters
     * @param {module:model/FilterOverShortTournaments} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/SearchOverShortTournaments} [search] Options to search results
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/RangeOverShortTournaments} [range] Options to select results within ranges
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/TeamsApi~getTeamsTeamIdOrSlugTournamentsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ShortTournament>}
     */
    getTeamsTeamIdOrSlugTournaments(teamIdOrSlug, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'teamIdOrSlug' is set
      if (teamIdOrSlug === undefined || teamIdOrSlug === null) {
        throw new Error("Missing the required parameter 'teamIdOrSlug' when calling getTeamsTeamIdOrSlugTournaments");
      }

      let pathParams = {
        'team_id_or_slug': teamIdOrSlug
      };
      let queryParams = {
        'filter': opts['filter'],
        'search': opts['search'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'multi'),
        'range': opts['range'],
        'page': opts['page'],
        'per_page': opts['perPage']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['BearerToken', 'QueryToken'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [ShortTournament];
      return this.apiClient.callApi(
        '/teams/{team_id_or_slug}/tournaments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
