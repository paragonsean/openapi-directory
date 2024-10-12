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

import ApiClient from '../ApiClient';
import OpponentID from './OpponentID';
import OpponentType from './OpponentType';

/**
 * The FilterOverSeries model module.
 * @module model/FilterOverSeries
 * @version 2.23.1
 */
class FilterOverSeries {
    /**
     * Constructs a new <code>FilterOverSeries</code>.
     * @alias module:model/FilterOverSeries
     */
    constructor() { 
        
        FilterOverSeries.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FilterOverSeries</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FilterOverSeries} obj Optional instance to populate.
     * @return {module:model/FilterOverSeries} The populated <code>FilterOverSeries</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FilterOverSeries();

            if (data.hasOwnProperty('begin_at')) {
                obj['begin_at'] = ApiClient.convertToType(data['begin_at'], ['Date']);
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], ['String']);
            }
            if (data.hasOwnProperty('end_at')) {
                obj['end_at'] = ApiClient.convertToType(data['end_at'], ['Date']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], ['Number']);
            }
            if (data.hasOwnProperty('league_id')) {
                obj['league_id'] = ApiClient.convertToType(data['league_id'], ['Number']);
            }
            if (data.hasOwnProperty('modified_at')) {
                obj['modified_at'] = ApiClient.convertToType(data['modified_at'], ['Date']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], ['String']);
            }
            if (data.hasOwnProperty('season')) {
                obj['season'] = ApiClient.convertToType(data['season'], ['String']);
            }
            if (data.hasOwnProperty('slug')) {
                obj['slug'] = ApiClient.convertToType(data['slug'], ['String']);
            }
            if (data.hasOwnProperty('tier')) {
                obj['tier'] = ApiClient.convertToType(data['tier'], ['String']);
            }
            if (data.hasOwnProperty('winner_id')) {
                obj['winner_id'] = ApiClient.convertToType(data['winner_id'], [OpponentID]);
            }
            if (data.hasOwnProperty('winner_type')) {
                obj['winner_type'] = ApiClient.convertToType(data['winner_type'], [OpponentType]);
            }
            if (data.hasOwnProperty('year')) {
                obj['year'] = ApiClient.convertToType(data['year'], ['Number']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FilterOverSeries</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FilterOverSeries</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['begin_at'])) {
            throw new Error("Expected the field `begin_at` to be an array in the JSON data but got " + data['begin_at']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['description'])) {
            throw new Error("Expected the field `description` to be an array in the JSON data but got " + data['description']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['end_at'])) {
            throw new Error("Expected the field `end_at` to be an array in the JSON data but got " + data['end_at']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['id'])) {
            throw new Error("Expected the field `id` to be an array in the JSON data but got " + data['id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['league_id'])) {
            throw new Error("Expected the field `league_id` to be an array in the JSON data but got " + data['league_id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['modified_at'])) {
            throw new Error("Expected the field `modified_at` to be an array in the JSON data but got " + data['modified_at']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['name'])) {
            throw new Error("Expected the field `name` to be an array in the JSON data but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['season'])) {
            throw new Error("Expected the field `season` to be an array in the JSON data but got " + data['season']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['slug'])) {
            throw new Error("Expected the field `slug` to be an array in the JSON data but got " + data['slug']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['tier'])) {
            throw new Error("Expected the field `tier` to be an array in the JSON data but got " + data['tier']);
        }
        if (data['winner_id']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['winner_id'])) {
                throw new Error("Expected the field `winner_id` to be an array in the JSON data but got " + data['winner_id']);
            }
            // validate the optional field `winner_id` (array)
            for (const item of data['winner_id']) {
                OpponentID.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['winner_type'])) {
            throw new Error("Expected the field `winner_type` to be an array in the JSON data but got " + data['winner_type']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['year'])) {
            throw new Error("Expected the field `year` to be an array in the JSON data but got " + data['year']);
        }

        return true;
    }


}



/**
 * @member {Array.<Date>} begin_at
 */
FilterOverSeries.prototype['begin_at'] = undefined;

/**
 * @member {Array.<String>} description
 */
FilterOverSeries.prototype['description'] = undefined;

/**
 * @member {Array.<Date>} end_at
 */
FilterOverSeries.prototype['end_at'] = undefined;

/**
 * @member {Array.<Number>} id
 */
FilterOverSeries.prototype['id'] = undefined;

/**
 * @member {Array.<Number>} league_id
 */
FilterOverSeries.prototype['league_id'] = undefined;

/**
 * @member {Array.<Date>} modified_at
 */
FilterOverSeries.prototype['modified_at'] = undefined;

/**
 * @member {Array.<String>} name
 */
FilterOverSeries.prototype['name'] = undefined;

/**
 * @member {Array.<String>} season
 */
FilterOverSeries.prototype['season'] = undefined;

/**
 * @member {Array.<String>} slug
 */
FilterOverSeries.prototype['slug'] = undefined;

/**
 * @member {Array.<String>} tier
 */
FilterOverSeries.prototype['tier'] = undefined;

/**
 * @member {Array.<module:model/OpponentID>} winner_id
 */
FilterOverSeries.prototype['winner_id'] = undefined;

/**
 * @member {Array.<module:model/OpponentType>} winner_type
 */
FilterOverSeries.prototype['winner_type'] = undefined;

/**
 * @member {Array.<Number>} year
 */
FilterOverSeries.prototype['year'] = undefined;






export default FilterOverSeries;

