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
import MarketSelection from './MarketSelection';
import MarketStatus from './MarketStatus';
import OpponentID1 from './OpponentID1';

/**
 * The Market model module.
 * @module model/Market
 * @version 2.23.1
 */
class Market {
    /**
     * Constructs a new <code>Market</code>.
     * @alias module:model/Market
     * @param id {String} 
     * @param line {Object} 
     * @param margin {Number} 
     * @param name {String} 
     * @param participantId {module:model/OpponentID1} 
     * @param participantType {Object} 
     * @param selections {Array.<module:model/MarketSelection>} 
     * @param status {module:model/MarketStatus} 
     * @param template {String} 
     */
    constructor(id, line, margin, name, participantId, participantType, selections, status, template) { 
        
        Market.initialize(this, id, line, margin, name, participantId, participantType, selections, status, template);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, line, margin, name, participantId, participantType, selections, status, template) { 
        obj['id'] = id;
        obj['line'] = line;
        obj['margin'] = margin;
        obj['name'] = name;
        obj['participant_id'] = participantId;
        obj['participant_type'] = participantType;
        obj['selections'] = selections;
        obj['status'] = status;
        obj['template'] = template;
    }

    /**
     * Constructs a <code>Market</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Market} obj Optional instance to populate.
     * @return {module:model/Market} The populated <code>Market</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Market();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('line')) {
                obj['line'] = ApiClient.convertToType(data['line'], Object);
            }
            if (data.hasOwnProperty('margin')) {
                obj['margin'] = ApiClient.convertToType(data['margin'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('participant_id')) {
                obj['participant_id'] = OpponentID1.constructFromObject(data['participant_id']);
            }
            if (data.hasOwnProperty('participant_type')) {
                obj['participant_type'] = ApiClient.convertToType(data['participant_type'], Object);
            }
            if (data.hasOwnProperty('selections')) {
                obj['selections'] = ApiClient.convertToType(data['selections'], [MarketSelection]);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = MarketStatus.constructFromObject(data['status']);
            }
            if (data.hasOwnProperty('template')) {
                obj['template'] = ApiClient.convertToType(data['template'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Market</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Market</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Market.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `line`
        if (data['line']) { // data not null
          Object.validateJSON(data['line']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `participant_id`
        if (data['participant_id']) { // data not null
          OpponentID1.validateJSON(data['participant_id']);
        }
        // validate the optional field `participant_type`
        if (data['participant_type']) { // data not null
          Object.validateJSON(data['participant_type']);
        }
        if (data['selections']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['selections'])) {
                throw new Error("Expected the field `selections` to be an array in the JSON data but got " + data['selections']);
            }
            // validate the optional field `selections` (array)
            for (const item of data['selections']) {
                MarketSelection.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['template'] && !(typeof data['template'] === 'string' || data['template'] instanceof String)) {
            throw new Error("Expected the field `template` to be a primitive type in the JSON string but got " + data['template']);
        }

        return true;
    }


}

Market.RequiredProperties = ["id", "line", "margin", "name", "participant_id", "participant_type", "selections", "status", "template"];

/**
 * @member {String} id
 */
Market.prototype['id'] = undefined;

/**
 * @member {Object} line
 */
Market.prototype['line'] = undefined;

/**
 * @member {Number} margin
 */
Market.prototype['margin'] = undefined;

/**
 * @member {String} name
 */
Market.prototype['name'] = undefined;

/**
 * @member {module:model/OpponentID1} participant_id
 */
Market.prototype['participant_id'] = undefined;

/**
 * @member {Object} participant_type
 */
Market.prototype['participant_type'] = undefined;

/**
 * @member {Array.<module:model/MarketSelection>} selections
 */
Market.prototype['selections'] = undefined;

/**
 * @member {module:model/MarketStatus} status
 */
Market.prototype['status'] = undefined;

/**
 * @member {String} template
 */
Market.prototype['template'] = undefined;






export default Market;

