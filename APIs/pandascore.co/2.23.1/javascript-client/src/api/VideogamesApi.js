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
import FilterOverSeries from '../model/FilterOverSeries';
import FilterOverShortTournaments from '../model/FilterOverShortTournaments';
import FilterOverShortVideogameVersions from '../model/FilterOverShortVideogameVersions';
import GetAdditions400Response from '../model/GetAdditions400Response';
import GetAdditionsPageParameter from '../model/GetAdditionsPageParameter';
import League from '../model/League';
import RangeOverLeagues from '../model/RangeOverLeagues';
import RangeOverSeries from '../model/RangeOverSeries';
import RangeOverShortTournaments from '../model/RangeOverShortTournaments';
import RangeOverShortVideogameVersions from '../model/RangeOverShortVideogameVersions';
import SearchOverLeagues from '../model/SearchOverLeagues';
import SearchOverSeries from '../model/SearchOverSeries';
import SearchOverShortTournaments from '../model/SearchOverShortTournaments';
import SearchOverShortVideogameVersions from '../model/SearchOverShortVideogameVersions';
import Serie from '../model/Serie';
import ShortTournament from '../model/ShortTournament';
import ShortVideogameVersion from '../model/ShortVideogameVersion';
import Videogame from '../model/Videogame';
import VideogameIDOrSlug from '../model/VideogameIDOrSlug';

/**
* Videogames service.
* @module api/VideogamesApi
* @version 2.23.1
*/
export default class VideogamesApi {

    /**
    * Constructs a new VideogamesApi. 
    * @alias module:api/VideogamesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getVideogames operation.
     * @callback module:api/VideogamesApi~getVideogamesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Videogame>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List videogames
     * List videogames
     * @param {Object} opts Optional parameters
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/VideogamesApi~getVideogamesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Videogame>}
     */
    getVideogames(opts, callback) {
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
      let returnType = [Videogame];
      return this.apiClient.callApi(
        '/videogames', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideogamesVideogameIdOrSlug operation.
     * @callback module:api/VideogamesApi~getVideogamesVideogameIdOrSlugCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Videogame} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a videogame
     * Get a single videogame by ID or by slug
     * @param {module:model/VideogameIDOrSlug} videogameIdOrSlug A videogame ID or slug
     * @param {module:api/VideogamesApi~getVideogamesVideogameIdOrSlugCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Videogame}
     */
    getVideogamesVideogameIdOrSlug(videogameIdOrSlug, callback) {
      let postBody = null;
      // verify the required parameter 'videogameIdOrSlug' is set
      if (videogameIdOrSlug === undefined || videogameIdOrSlug === null) {
        throw new Error("Missing the required parameter 'videogameIdOrSlug' when calling getVideogamesVideogameIdOrSlug");
      }

      let pathParams = {
        'videogame_id_or_slug': videogameIdOrSlug
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
      let returnType = Videogame;
      return this.apiClient.callApi(
        '/videogames/{videogame_id_or_slug}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideogamesVideogameIdOrSlugLeagues operation.
     * @callback module:api/VideogamesApi~getVideogamesVideogameIdOrSlugLeaguesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/League>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:model/VideogameIDOrSlug} videogameIdOrSlug A videogame ID or slug
     * @param {Object} opts Optional parameters
     * @param {module:model/SearchOverLeagues} [search] Options to search results
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/RangeOverLeagues} [range] Options to select results within ranges
     * @param {module:model/FilterOverLeagues} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/VideogamesApi~getVideogamesVideogameIdOrSlugLeaguesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/League>}
     */
    getVideogamesVideogameIdOrSlugLeagues(videogameIdOrSlug, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'videogameIdOrSlug' is set
      if (videogameIdOrSlug === undefined || videogameIdOrSlug === null) {
        throw new Error("Missing the required parameter 'videogameIdOrSlug' when calling getVideogamesVideogameIdOrSlugLeagues");
      }

      let pathParams = {
        'videogame_id_or_slug': videogameIdOrSlug
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
        '/videogames/{videogame_id_or_slug}/leagues', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideogamesVideogameIdOrSlugSeries operation.
     * @callback module:api/VideogamesApi~getVideogamesVideogameIdOrSlugSeriesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Serie>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List series for a videogame
     * List series for the given videogame
     * @param {module:model/VideogameIDOrSlug} videogameIdOrSlug A videogame ID or slug
     * @param {Object} opts Optional parameters
     * @param {module:model/FilterOverSeries} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/SearchOverSeries} [search] Options to search results
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/RangeOverSeries} [range] Options to select results within ranges
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/VideogamesApi~getVideogamesVideogameIdOrSlugSeriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Serie>}
     */
    getVideogamesVideogameIdOrSlugSeries(videogameIdOrSlug, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'videogameIdOrSlug' is set
      if (videogameIdOrSlug === undefined || videogameIdOrSlug === null) {
        throw new Error("Missing the required parameter 'videogameIdOrSlug' when calling getVideogamesVideogameIdOrSlugSeries");
      }

      let pathParams = {
        'videogame_id_or_slug': videogameIdOrSlug
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
        '/videogames/{videogame_id_or_slug}/series', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideogamesVideogameIdOrSlugTournaments operation.
     * @callback module:api/VideogamesApi~getVideogamesVideogameIdOrSlugTournamentsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ShortTournament>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get tournaments for a videogame
     * List tournaments of the given videogame
     * @param {module:model/VideogameIDOrSlug} videogameIdOrSlug A videogame ID or slug
     * @param {Object} opts Optional parameters
     * @param {module:model/FilterOverShortTournaments} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/RangeOverShortTournaments} [range] Options to select results within ranges
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/SearchOverShortTournaments} [search] Options to search results
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/VideogamesApi~getVideogamesVideogameIdOrSlugTournamentsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ShortTournament>}
     */
    getVideogamesVideogameIdOrSlugTournaments(videogameIdOrSlug, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'videogameIdOrSlug' is set
      if (videogameIdOrSlug === undefined || videogameIdOrSlug === null) {
        throw new Error("Missing the required parameter 'videogameIdOrSlug' when calling getVideogamesVideogameIdOrSlugTournaments");
      }

      let pathParams = {
        'videogame_id_or_slug': videogameIdOrSlug
      };
      let queryParams = {
        'filter': opts['filter'],
        'range': opts['range'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'multi'),
        'search': opts['search'],
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
        '/videogames/{videogame_id_or_slug}/tournaments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getVideogamesVideogameIdOrSlugVersions operation.
     * @callback module:api/VideogamesApi~getVideogamesVideogameIdOrSlugVersionsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/ShortVideogameVersion>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List videogame versions
     * List available versions for a given videogame
     * @param {module:model/VideogameIDOrSlug} videogameIdOrSlug A videogame ID or slug
     * @param {Object} opts Optional parameters
     * @param {module:model/FilterOverShortVideogameVersions} [filter] Options to filter results. String fields are case sensitive
     * @param {module:model/RangeOverShortVideogameVersions} [range] Options to select results within ranges
     * @param {Array.<module:model/String>} [sort] Options to sort results
     * @param {module:model/SearchOverShortVideogameVersions} [search] Options to search results
     * @param {module:model/GetAdditionsPageParameter} [page] Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
     * @param {Number} [perPage = 50)] Equivalent to `page[size]`
     * @param {module:api/VideogamesApi~getVideogamesVideogameIdOrSlugVersionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/ShortVideogameVersion>}
     */
    getVideogamesVideogameIdOrSlugVersions(videogameIdOrSlug, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'videogameIdOrSlug' is set
      if (videogameIdOrSlug === undefined || videogameIdOrSlug === null) {
        throw new Error("Missing the required parameter 'videogameIdOrSlug' when calling getVideogamesVideogameIdOrSlugVersions");
      }

      let pathParams = {
        'videogame_id_or_slug': videogameIdOrSlug
      };
      let queryParams = {
        'filter': opts['filter'],
        'range': opts['range'],
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'multi'),
        'search': opts['search'],
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
      let returnType = [ShortVideogameVersion];
      return this.apiClient.callApi(
        '/videogames/{videogame_id_or_slug}/versions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
