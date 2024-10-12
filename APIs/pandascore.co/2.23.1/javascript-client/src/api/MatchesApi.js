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
import FilterOverMatches from '../model/FilterOverMatches';
import GetAdditions400Response from '../model/GetAdditions400Response';
import GetAdditionsPageParameter from '../model/GetAdditionsPageParameter';
import Live from '../model/Live';
import Match from '../model/Match';
import MatchIDOrSlug from '../model/MatchIDOrSlug';
import MatchOpponentsObject from '../model/MatchOpponentsObject';
import RangeOverMatches from '../model/RangeOverMatches';
import SearchOverMatches from '../model/SearchOverMatches';

/**
* Matches service.
* @module api/MatchesApi
* @version 2.23.1
*/
export default class MatchesApi {

    /**
    * Constructs a new MatchesApi. 
    * @alias module:api/MatchesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getLives operation.
     * @callback module:api/MatchesApi~getLivesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Live>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List lives matches
     * List currently running live matches, available from pandascore with live websocket data.
     * @param {Object} opts Optional parameters
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/MatchesApi~getLivesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Live>}
     */
    getLives(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
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
      let returnType = [Live];
      return this.apiClient.callApi(
        '/lives', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMatches operation.
     * @callback module:api/MatchesApi~getMatchesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Match>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List matches
     * List matches
     * @param {Object} opts Optional parameters
     * @param {module:model/FilterOverMatches} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/SearchOverMatches} [search] Options to search results
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/RangeOverMatches} [range] Options to select results within ranges
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/MatchesApi~getMatchesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Match>}
     */
    getMatches(opts, callback) {
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
      let returnType = [Match];
      return this.apiClient.callApi(
        '/matches', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMatchesMatchIdOrSlug operation.
     * @callback module:api/MatchesApi~getMatchesMatchIdOrSlugCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Match} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a match
     * Get a single match by ID or by slug
     * @param {module:model/MatchIDOrSlug} matchIdOrSlug A match ID or slug
     * @param {module:api/MatchesApi~getMatchesMatchIdOrSlugCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Match}
     */
    getMatchesMatchIdOrSlug(matchIdOrSlug, callback) {
      let postBody = null;
      // verify the required parameter 'matchIdOrSlug' is set
      if (matchIdOrSlug === undefined || matchIdOrSlug === null) {
        throw new Error("Missing the required parameter 'matchIdOrSlug' when calling getMatchesMatchIdOrSlug");
      }

      let pathParams = {
        'match_id_or_slug': matchIdOrSlug
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
      let returnType = Match;
      return this.apiClient.callApi(
        '/matches/{match_id_or_slug}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMatchesMatchIdOrSlugOpponents operation.
     * @callback module:api/MatchesApi~getMatchesMatchIdOrSlugOpponentsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/MatchOpponentsObject} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get match's opponents
     * List opponents (player or teams) for the given match
     * @param {module:model/MatchIDOrSlug} matchIdOrSlug A match ID or slug
     * @param {module:api/MatchesApi~getMatchesMatchIdOrSlugOpponentsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MatchOpponentsObject}
     */
    getMatchesMatchIdOrSlugOpponents(matchIdOrSlug, callback) {
      let postBody = null;
      // verify the required parameter 'matchIdOrSlug' is set
      if (matchIdOrSlug === undefined || matchIdOrSlug === null) {
        throw new Error("Missing the required parameter 'matchIdOrSlug' when calling getMatchesMatchIdOrSlugOpponents");
      }

      let pathParams = {
        'match_id_or_slug': matchIdOrSlug
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
      let returnType = MatchOpponentsObject;
      return this.apiClient.callApi(
        '/matches/{match_id_or_slug}/opponents', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMatchesPast operation.
     * @callback module:api/MatchesApi~getMatchesPastCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Match>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get past matches
     * List past matches
     * @param {Object} opts Optional parameters
     * @param {module:model/FilterOverMatches} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/SearchOverMatches} [search] Options to search results
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/RangeOverMatches} [range] Options to select results within ranges
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/MatchesApi~getMatchesPastCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Match>}
     */
    getMatchesPast(opts, callback) {
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
      let returnType = [Match];
      return this.apiClient.callApi(
        '/matches/past', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMatchesRunning operation.
     * @callback module:api/MatchesApi~getMatchesRunningCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Match>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get running matches
     * List currently running matches
     * @param {Object} opts Optional parameters
     * @param {module:model/FilterOverMatches} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/SearchOverMatches} [search] Options to search results
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/RangeOverMatches} [range] Options to select results within ranges
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/MatchesApi~getMatchesRunningCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Match>}
     */
    getMatchesRunning(opts, callback) {
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
      let returnType = [Match];
      return this.apiClient.callApi(
        '/matches/running', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getMatchesUpcoming operation.
     * @callback module:api/MatchesApi~getMatchesUpcomingCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Match>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get upcoming matches
     * List upcoming matches
     * @param {Object} opts Optional parameters
     * @param {module:model/FilterOverMatches} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/SearchOverMatches} [search] Options to search results
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/RangeOverMatches} [range] Options to select results within ranges
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/MatchesApi~getMatchesUpcomingCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Match>}
     */
    getMatchesUpcoming(opts, callback) {
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
      let returnType = [Match];
      return this.apiClient.callApi(
        '/matches/upcoming', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
