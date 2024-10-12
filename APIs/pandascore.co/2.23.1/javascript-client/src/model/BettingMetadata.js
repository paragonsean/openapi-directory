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
import BettingGroup1 from './BettingGroup1';
import Blueprint1 from './Blueprint1';

/**
 * The BettingMetadata model module.
 * @module model/BettingMetadata
 * @version 2.23.1
 */
class BettingMetadata {
    /**
     * Constructs a new <code>BettingMetadata</code>.
     * @alias module:model/BettingMetadata
     * @param bettingGroup {module:model/BettingGroup1} 
     * @param blueprint {module:model/Blueprint1} 
     * @param bookable {Boolean} Whether match can be booked
     * @param booked {Boolean} Whether match has been booked
     * @param liveAvailable {Boolean} Whether live is available
     * @param marketsCreated {Boolean} Whether markets has been created
     * @param marketsUpdatedAt {Date} 
     * @param pandascoreReviewed {Boolean} Whether PandaScore reviewed the match
     * @param settled {Boolean} Whether match has been settled
     */
    constructor(bettingGroup, blueprint, bookable, booked, liveAvailable, marketsCreated, marketsUpdatedAt, pandascoreReviewed, settled) { 
        
        BettingMetadata.initialize(this, bettingGroup, blueprint, bookable, booked, liveAvailable, marketsCreated, marketsUpdatedAt, pandascoreReviewed, settled);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, bettingGroup, blueprint, bookable, booked, liveAvailable, marketsCreated, marketsUpdatedAt, pandascoreReviewed, settled) { 
        obj['betting_group'] = bettingGroup;
        obj['blueprint'] = blueprint;
        obj['bookable'] = bookable;
        obj['booked'] = booked;
        obj['live_available'] = liveAvailable;
        obj['markets_created'] = marketsCreated;
        obj['markets_updated_at'] = marketsUpdatedAt;
        obj['pandascore_reviewed'] = pandascoreReviewed;
        obj['settled'] = settled;
    }

    /**
     * Constructs a <code>BettingMetadata</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BettingMetadata} obj Optional instance to populate.
     * @return {module:model/BettingMetadata} The populated <code>BettingMetadata</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BettingMetadata();

            if (data.hasOwnProperty('betting_group')) {
                obj['betting_group'] = BettingGroup1.constructFromObject(data['betting_group']);
            }
            if (data.hasOwnProperty('blueprint')) {
                obj['blueprint'] = Blueprint1.constructFromObject(data['blueprint']);
            }
            if (data.hasOwnProperty('bookable')) {
                obj['bookable'] = ApiClient.convertToType(data['bookable'], 'Boolean');
            }
            if (data.hasOwnProperty('booked')) {
                obj['booked'] = ApiClient.convertToType(data['booked'], 'Boolean');
            }
            if (data.hasOwnProperty('live_available')) {
                obj['live_available'] = ApiClient.convertToType(data['live_available'], 'Boolean');
            }
            if (data.hasOwnProperty('markets_created')) {
                obj['markets_created'] = ApiClient.convertToType(data['markets_created'], 'Boolean');
            }
            if (data.hasOwnProperty('markets_updated_at')) {
                obj['markets_updated_at'] = ApiClient.convertToType(data['markets_updated_at'], 'Date');
            }
            if (data.hasOwnProperty('pandascore_reviewed')) {
                obj['pandascore_reviewed'] = ApiClient.convertToType(data['pandascore_reviewed'], 'Boolean');
            }
            if (data.hasOwnProperty('settled')) {
                obj['settled'] = ApiClient.convertToType(data['settled'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BettingMetadata</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BettingMetadata</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BettingMetadata.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `betting_group`
        if (data['betting_group']) { // data not null
          BettingGroup1.validateJSON(data['betting_group']);
        }
        // validate the optional field `blueprint`
        if (data['blueprint']) { // data not null
          Blueprint1.validateJSON(data['blueprint']);
        }

        return true;
    }


}

BettingMetadata.RequiredProperties = ["betting_group", "blueprint", "bookable", "booked", "live_available", "markets_created", "markets_updated_at", "pandascore_reviewed", "settled"];

/**
 * @member {module:model/BettingGroup1} betting_group
 */
BettingMetadata.prototype['betting_group'] = undefined;

/**
 * @member {module:model/Blueprint1} blueprint
 */
BettingMetadata.prototype['blueprint'] = undefined;

/**
 * Whether match can be booked
 * @member {Boolean} bookable
 */
BettingMetadata.prototype['bookable'] = undefined;

/**
 * Whether match has been booked
 * @member {Boolean} booked
 */
BettingMetadata.prototype['booked'] = undefined;

/**
 * Whether live is available
 * @member {Boolean} live_available
 */
BettingMetadata.prototype['live_available'] = undefined;

/**
 * Whether markets has been created
 * @member {Boolean} markets_created
 */
BettingMetadata.prototype['markets_created'] = undefined;

/**
 * @member {Date} markets_updated_at
 */
BettingMetadata.prototype['markets_updated_at'] = undefined;

/**
 * Whether PandaScore reviewed the match
 * @member {Boolean} pandascore_reviewed
 */
BettingMetadata.prototype['pandascore_reviewed'] = undefined;

/**
 * Whether match has been settled
 * @member {Boolean} settled
 */
BettingMetadata.prototype['settled'] = undefined;






export default BettingMetadata;

