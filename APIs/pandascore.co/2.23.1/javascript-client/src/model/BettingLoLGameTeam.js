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
import LoLTeamColor from './LoLTeamColor';

/**
 * The BettingLoLGameTeam model module.
 * @module model/BettingLoLGameTeam
 * @version 2.23.1
 */
class BettingLoLGameTeam {
    /**
     * Constructs a new <code>BettingLoLGameTeam</code>.
     * Team&#39;s data for a Game
     * @alias module:model/BettingLoLGameTeam
     * @param baronKills {Object} 
     * @param color {module:model/LoLTeamColor} 
     * @param dragonKills {Object} 
     * @param firstBaron {Object} 
     * @param firstBlood {Object} 
     * @param firstDragon {Object} 
     * @param firstHerald {Object} 
     * @param firstInhibitor {Object} 
     * @param firstTower {Object} 
     * @param goldEarned {Object} 
     * @param heraldKill {Object} 
     * @param inhibitorKills {Object} 
     * @param teamId {Number} 
     * @param teamKills {Object} 
     * @param towerKills {Object} 
     */
    constructor(baronKills, color, dragonKills, firstBaron, firstBlood, firstDragon, firstHerald, firstInhibitor, firstTower, goldEarned, heraldKill, inhibitorKills, teamId, teamKills, towerKills) { 
        
        BettingLoLGameTeam.initialize(this, baronKills, color, dragonKills, firstBaron, firstBlood, firstDragon, firstHerald, firstInhibitor, firstTower, goldEarned, heraldKill, inhibitorKills, teamId, teamKills, towerKills);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, baronKills, color, dragonKills, firstBaron, firstBlood, firstDragon, firstHerald, firstInhibitor, firstTower, goldEarned, heraldKill, inhibitorKills, teamId, teamKills, towerKills) { 
        obj['baron_kills'] = baronKills;
        obj['color'] = color;
        obj['dragon_kills'] = dragonKills;
        obj['first_baron'] = firstBaron;
        obj['first_blood'] = firstBlood;
        obj['first_dragon'] = firstDragon;
        obj['first_herald'] = firstHerald;
        obj['first_inhibitor'] = firstInhibitor;
        obj['first_tower'] = firstTower;
        obj['gold_earned'] = goldEarned;
        obj['herald_kill'] = heraldKill;
        obj['inhibitor_kills'] = inhibitorKills;
        obj['team_id'] = teamId;
        obj['team_kills'] = teamKills;
        obj['tower_kills'] = towerKills;
    }

    /**
     * Constructs a <code>BettingLoLGameTeam</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BettingLoLGameTeam} obj Optional instance to populate.
     * @return {module:model/BettingLoLGameTeam} The populated <code>BettingLoLGameTeam</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BettingLoLGameTeam();

            if (data.hasOwnProperty('baron_kills')) {
                obj['baron_kills'] = ApiClient.convertToType(data['baron_kills'], Object);
            }
            if (data.hasOwnProperty('color')) {
                obj['color'] = LoLTeamColor.constructFromObject(data['color']);
            }
            if (data.hasOwnProperty('dragon_kills')) {
                obj['dragon_kills'] = ApiClient.convertToType(data['dragon_kills'], Object);
            }
            if (data.hasOwnProperty('first_baron')) {
                obj['first_baron'] = ApiClient.convertToType(data['first_baron'], Object);
            }
            if (data.hasOwnProperty('first_blood')) {
                obj['first_blood'] = ApiClient.convertToType(data['first_blood'], Object);
            }
            if (data.hasOwnProperty('first_dragon')) {
                obj['first_dragon'] = ApiClient.convertToType(data['first_dragon'], Object);
            }
            if (data.hasOwnProperty('first_herald')) {
                obj['first_herald'] = ApiClient.convertToType(data['first_herald'], Object);
            }
            if (data.hasOwnProperty('first_inhibitor')) {
                obj['first_inhibitor'] = ApiClient.convertToType(data['first_inhibitor'], Object);
            }
            if (data.hasOwnProperty('first_tower')) {
                obj['first_tower'] = ApiClient.convertToType(data['first_tower'], Object);
            }
            if (data.hasOwnProperty('gold_earned')) {
                obj['gold_earned'] = ApiClient.convertToType(data['gold_earned'], Object);
            }
            if (data.hasOwnProperty('herald_kill')) {
                obj['herald_kill'] = ApiClient.convertToType(data['herald_kill'], Object);
            }
            if (data.hasOwnProperty('inhibitor_kills')) {
                obj['inhibitor_kills'] = ApiClient.convertToType(data['inhibitor_kills'], Object);
            }
            if (data.hasOwnProperty('team_id')) {
                obj['team_id'] = ApiClient.convertToType(data['team_id'], 'Number');
            }
            if (data.hasOwnProperty('team_kills')) {
                obj['team_kills'] = ApiClient.convertToType(data['team_kills'], Object);
            }
            if (data.hasOwnProperty('tower_kills')) {
                obj['tower_kills'] = ApiClient.convertToType(data['tower_kills'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BettingLoLGameTeam</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BettingLoLGameTeam</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BettingLoLGameTeam.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `baron_kills`
        if (data['baron_kills']) { // data not null
          Object.validateJSON(data['baron_kills']);
        }
        // validate the optional field `dragon_kills`
        if (data['dragon_kills']) { // data not null
          Object.validateJSON(data['dragon_kills']);
        }
        // validate the optional field `first_baron`
        if (data['first_baron']) { // data not null
          Object.validateJSON(data['first_baron']);
        }
        // validate the optional field `first_blood`
        if (data['first_blood']) { // data not null
          Object.validateJSON(data['first_blood']);
        }
        // validate the optional field `first_dragon`
        if (data['first_dragon']) { // data not null
          Object.validateJSON(data['first_dragon']);
        }
        // validate the optional field `first_herald`
        if (data['first_herald']) { // data not null
          Object.validateJSON(data['first_herald']);
        }
        // validate the optional field `first_inhibitor`
        if (data['first_inhibitor']) { // data not null
          Object.validateJSON(data['first_inhibitor']);
        }
        // validate the optional field `first_tower`
        if (data['first_tower']) { // data not null
          Object.validateJSON(data['first_tower']);
        }
        // validate the optional field `gold_earned`
        if (data['gold_earned']) { // data not null
          Object.validateJSON(data['gold_earned']);
        }
        // validate the optional field `herald_kill`
        if (data['herald_kill']) { // data not null
          Object.validateJSON(data['herald_kill']);
        }
        // validate the optional field `inhibitor_kills`
        if (data['inhibitor_kills']) { // data not null
          Object.validateJSON(data['inhibitor_kills']);
        }
        // validate the optional field `team_kills`
        if (data['team_kills']) { // data not null
          Object.validateJSON(data['team_kills']);
        }
        // validate the optional field `tower_kills`
        if (data['tower_kills']) { // data not null
          Object.validateJSON(data['tower_kills']);
        }

        return true;
    }


}

BettingLoLGameTeam.RequiredProperties = ["baron_kills", "color", "dragon_kills", "first_baron", "first_blood", "first_dragon", "first_herald", "first_inhibitor", "first_tower", "gold_earned", "herald_kill", "inhibitor_kills", "team_id", "team_kills", "tower_kills"];

/**
 * @member {Object} baron_kills
 */
BettingLoLGameTeam.prototype['baron_kills'] = undefined;

/**
 * @member {module:model/LoLTeamColor} color
 */
BettingLoLGameTeam.prototype['color'] = undefined;

/**
 * @member {Object} dragon_kills
 */
BettingLoLGameTeam.prototype['dragon_kills'] = undefined;

/**
 * @member {Object} first_baron
 */
BettingLoLGameTeam.prototype['first_baron'] = undefined;

/**
 * @member {Object} first_blood
 */
BettingLoLGameTeam.prototype['first_blood'] = undefined;

/**
 * @member {Object} first_dragon
 */
BettingLoLGameTeam.prototype['first_dragon'] = undefined;

/**
 * @member {Object} first_herald
 */
BettingLoLGameTeam.prototype['first_herald'] = undefined;

/**
 * @member {Object} first_inhibitor
 */
BettingLoLGameTeam.prototype['first_inhibitor'] = undefined;

/**
 * @member {Object} first_tower
 */
BettingLoLGameTeam.prototype['first_tower'] = undefined;

/**
 * @member {Object} gold_earned
 */
BettingLoLGameTeam.prototype['gold_earned'] = undefined;

/**
 * @member {Object} herald_kill
 */
BettingLoLGameTeam.prototype['herald_kill'] = undefined;

/**
 * @member {Object} inhibitor_kills
 */
BettingLoLGameTeam.prototype['inhibitor_kills'] = undefined;

/**
 * @member {Number} team_id
 */
BettingLoLGameTeam.prototype['team_id'] = undefined;

/**
 * @member {Object} team_kills
 */
BettingLoLGameTeam.prototype['team_kills'] = undefined;

/**
 * @member {Object} tower_kills
 */
BettingLoLGameTeam.prototype['tower_kills'] = undefined;






export default BettingLoLGameTeam;

