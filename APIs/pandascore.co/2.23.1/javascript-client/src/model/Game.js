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
import GameID from './GameID';
import GameStatus from './GameStatus';
import GameWinner from './GameWinner';

/**
 * The Game model module.
 * @module model/Game
 * @version 2.23.1
 */
class Game {
    /**
     * Constructs a new <code>Game</code>.
     * @alias module:model/Game
     * @param beginAt {Object} 
     * @param complete {Boolean} Whether game data are complete and won't change
     * @param detailedStats {Boolean} Whether the game offers full stats
     * @param endAt {Object} 
     * @param finished {Boolean} Whether game is finished
     * @param forfeit {Boolean} Whether game is forfeit
     * @param id {module:model/GameID} 
     * @param length {Object} 
     * @param matchId {Number} 
     * @param position {Number} 
     * @param status {module:model/GameStatus} 
     * @param videoUrl {Object} 
     * @param winner {module:model/GameWinner} 
     * @param winnerType {Object} 
     */
    constructor(beginAt, complete, detailedStats, endAt, finished, forfeit, id, length, matchId, position, status, videoUrl, winner, winnerType) { 
        
        Game.initialize(this, beginAt, complete, detailedStats, endAt, finished, forfeit, id, length, matchId, position, status, videoUrl, winner, winnerType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, beginAt, complete, detailedStats, endAt, finished, forfeit, id, length, matchId, position, status, videoUrl, winner, winnerType) { 
        obj['begin_at'] = beginAt;
        obj['complete'] = complete;
        obj['detailed_stats'] = detailedStats;
        obj['end_at'] = endAt;
        obj['finished'] = finished;
        obj['forfeit'] = forfeit;
        obj['id'] = id;
        obj['length'] = length;
        obj['match_id'] = matchId;
        obj['position'] = position;
        obj['status'] = status;
        obj['video_url'] = videoUrl;
        obj['winner'] = winner;
        obj['winner_type'] = winnerType;
    }

    /**
     * Constructs a <code>Game</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Game} obj Optional instance to populate.
     * @return {module:model/Game} The populated <code>Game</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Game();

            if (data.hasOwnProperty('begin_at')) {
                obj['begin_at'] = ApiClient.convertToType(data['begin_at'], Object);
            }
            if (data.hasOwnProperty('complete')) {
                obj['complete'] = ApiClient.convertToType(data['complete'], 'Boolean');
            }
            if (data.hasOwnProperty('detailed_stats')) {
                obj['detailed_stats'] = ApiClient.convertToType(data['detailed_stats'], 'Boolean');
            }
            if (data.hasOwnProperty('end_at')) {
                obj['end_at'] = ApiClient.convertToType(data['end_at'], Object);
            }
            if (data.hasOwnProperty('finished')) {
                obj['finished'] = ApiClient.convertToType(data['finished'], 'Boolean');
            }
            if (data.hasOwnProperty('forfeit')) {
                obj['forfeit'] = ApiClient.convertToType(data['forfeit'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = GameID.constructFromObject(data['id']);
            }
            if (data.hasOwnProperty('length')) {
                obj['length'] = ApiClient.convertToType(data['length'], Object);
            }
            if (data.hasOwnProperty('match_id')) {
                obj['match_id'] = ApiClient.convertToType(data['match_id'], 'Number');
            }
            if (data.hasOwnProperty('position')) {
                obj['position'] = ApiClient.convertToType(data['position'], 'Number');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = GameStatus.constructFromObject(data['status']);
            }
            if (data.hasOwnProperty('video_url')) {
                obj['video_url'] = ApiClient.convertToType(data['video_url'], Object);
            }
            if (data.hasOwnProperty('winner')) {
                obj['winner'] = GameWinner.constructFromObject(data['winner']);
            }
            if (data.hasOwnProperty('winner_type')) {
                obj['winner_type'] = ApiClient.convertToType(data['winner_type'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Game</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Game</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Game.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `begin_at`
        if (data['begin_at']) { // data not null
          Object.validateJSON(data['begin_at']);
        }
        // validate the optional field `end_at`
        if (data['end_at']) { // data not null
          Object.validateJSON(data['end_at']);
        }
        // validate the optional field `id`
        if (data['id']) { // data not null
          GameID.validateJSON(data['id']);
        }
        // validate the optional field `length`
        if (data['length']) { // data not null
          Object.validateJSON(data['length']);
        }
        // validate the optional field `video_url`
        if (data['video_url']) { // data not null
          Object.validateJSON(data['video_url']);
        }
        // validate the optional field `winner`
        if (data['winner']) { // data not null
          GameWinner.validateJSON(data['winner']);
        }
        // validate the optional field `winner_type`
        if (data['winner_type']) { // data not null
          Object.validateJSON(data['winner_type']);
        }

        return true;
    }


}

Game.RequiredProperties = ["begin_at", "complete", "detailed_stats", "end_at", "finished", "forfeit", "id", "length", "match_id", "position", "status", "video_url", "winner", "winner_type"];

/**
 * @member {Object} begin_at
 */
Game.prototype['begin_at'] = undefined;

/**
 * Whether game data are complete and won't change
 * @member {Boolean} complete
 */
Game.prototype['complete'] = undefined;

/**
 * Whether the game offers full stats
 * @member {Boolean} detailed_stats
 */
Game.prototype['detailed_stats'] = undefined;

/**
 * @member {Object} end_at
 */
Game.prototype['end_at'] = undefined;

/**
 * Whether game is finished
 * @member {Boolean} finished
 */
Game.prototype['finished'] = undefined;

/**
 * Whether game is forfeit
 * @member {Boolean} forfeit
 */
Game.prototype['forfeit'] = undefined;

/**
 * @member {module:model/GameID} id
 */
Game.prototype['id'] = undefined;

/**
 * @member {Object} length
 */
Game.prototype['length'] = undefined;

/**
 * @member {Number} match_id
 */
Game.prototype['match_id'] = undefined;

/**
 * @member {Number} position
 */
Game.prototype['position'] = undefined;

/**
 * @member {module:model/GameStatus} status
 */
Game.prototype['status'] = undefined;

/**
 * @member {Object} video_url
 */
Game.prototype['video_url'] = undefined;

/**
 * @member {module:model/GameWinner} winner
 */
Game.prototype['winner'] = undefined;

/**
 * @member {Object} winner_type
 */
Game.prototype['winner_type'] = undefined;






export default Game;

