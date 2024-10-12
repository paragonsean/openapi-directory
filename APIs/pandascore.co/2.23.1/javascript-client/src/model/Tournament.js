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
import BaseLeague from './BaseLeague';
import BaseMatch from './BaseMatch';
import BaseSerie from './BaseSerie';
import BaseTeam from './BaseTeam';
import CurrentVideogame from './CurrentVideogame';
import OpponentID1 from './OpponentID1';
import TournamentRosterItem from './TournamentRosterItem';

/**
 * The Tournament model module.
 * @module model/Tournament
 * @version 2.23.1
 */
class Tournament {
    /**
     * Constructs a new <code>Tournament</code>.
     * @alias module:model/Tournament
     * @param beginAt {Object} 
     * @param endAt {Object} 
     * @param expectedRoster {Array.<module:model/TournamentRosterItem>} 
     * @param id {Number} 
     * @param league {module:model/BaseLeague} 
     * @param leagueId {Number} 
     * @param liveSupported {Boolean} Whether live is supported
     * @param matches {Array.<module:model/BaseMatch>} 
     * @param modifiedAt {Date} 
     * @param name {String} 
     * @param prizepool {Object} 
     * @param serie {module:model/BaseSerie} 
     * @param serieId {Number} 
     * @param slug {String} 
     * @param teams {Array.<module:model/BaseTeam>} 
     * @param videogame {module:model/CurrentVideogame} 
     * @param winnerId {module:model/OpponentID1} 
     * @param winnerType {Object} 
     */
    constructor(beginAt, endAt, expectedRoster, id, league, leagueId, liveSupported, matches, modifiedAt, name, prizepool, serie, serieId, slug, teams, videogame, winnerId, winnerType) { 
        
        Tournament.initialize(this, beginAt, endAt, expectedRoster, id, league, leagueId, liveSupported, matches, modifiedAt, name, prizepool, serie, serieId, slug, teams, videogame, winnerId, winnerType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, beginAt, endAt, expectedRoster, id, league, leagueId, liveSupported, matches, modifiedAt, name, prizepool, serie, serieId, slug, teams, videogame, winnerId, winnerType) { 
        obj['begin_at'] = beginAt;
        obj['end_at'] = endAt;
        obj['expected_roster'] = expectedRoster;
        obj['id'] = id;
        obj['league'] = league;
        obj['league_id'] = leagueId;
        obj['live_supported'] = liveSupported;
        obj['matches'] = matches;
        obj['modified_at'] = modifiedAt;
        obj['name'] = name;
        obj['prizepool'] = prizepool;
        obj['serie'] = serie;
        obj['serie_id'] = serieId;
        obj['slug'] = slug;
        obj['teams'] = teams;
        obj['videogame'] = videogame;
        obj['winner_id'] = winnerId;
        obj['winner_type'] = winnerType;
    }

    /**
     * Constructs a <code>Tournament</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Tournament} obj Optional instance to populate.
     * @return {module:model/Tournament} The populated <code>Tournament</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Tournament();

            if (data.hasOwnProperty('begin_at')) {
                obj['begin_at'] = ApiClient.convertToType(data['begin_at'], Object);
            }
            if (data.hasOwnProperty('end_at')) {
                obj['end_at'] = ApiClient.convertToType(data['end_at'], Object);
            }
            if (data.hasOwnProperty('expected_roster')) {
                obj['expected_roster'] = ApiClient.convertToType(data['expected_roster'], [TournamentRosterItem]);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('league')) {
                obj['league'] = BaseLeague.constructFromObject(data['league']);
            }
            if (data.hasOwnProperty('league_id')) {
                obj['league_id'] = ApiClient.convertToType(data['league_id'], 'Number');
            }
            if (data.hasOwnProperty('live_supported')) {
                obj['live_supported'] = ApiClient.convertToType(data['live_supported'], 'Boolean');
            }
            if (data.hasOwnProperty('matches')) {
                obj['matches'] = ApiClient.convertToType(data['matches'], [BaseMatch]);
            }
            if (data.hasOwnProperty('modified_at')) {
                obj['modified_at'] = ApiClient.convertToType(data['modified_at'], 'Date');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('prizepool')) {
                obj['prizepool'] = ApiClient.convertToType(data['prizepool'], Object);
            }
            if (data.hasOwnProperty('serie')) {
                obj['serie'] = BaseSerie.constructFromObject(data['serie']);
            }
            if (data.hasOwnProperty('serie_id')) {
                obj['serie_id'] = ApiClient.convertToType(data['serie_id'], 'Number');
            }
            if (data.hasOwnProperty('slug')) {
                obj['slug'] = ApiClient.convertToType(data['slug'], 'String');
            }
            if (data.hasOwnProperty('teams')) {
                obj['teams'] = ApiClient.convertToType(data['teams'], [BaseTeam]);
            }
            if (data.hasOwnProperty('videogame')) {
                obj['videogame'] = CurrentVideogame.constructFromObject(data['videogame']);
            }
            if (data.hasOwnProperty('winner_id')) {
                obj['winner_id'] = OpponentID1.constructFromObject(data['winner_id']);
            }
            if (data.hasOwnProperty('winner_type')) {
                obj['winner_type'] = ApiClient.convertToType(data['winner_type'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Tournament</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Tournament</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Tournament.RequiredProperties) {
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
        if (data['expected_roster']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['expected_roster'])) {
                throw new Error("Expected the field `expected_roster` to be an array in the JSON data but got " + data['expected_roster']);
            }
            // validate the optional field `expected_roster` (array)
            for (const item of data['expected_roster']) {
                TournamentRosterItem.validateJSON(item);
            };
        }
        // validate the optional field `league`
        if (data['league']) { // data not null
          BaseLeague.validateJSON(data['league']);
        }
        if (data['matches']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['matches'])) {
                throw new Error("Expected the field `matches` to be an array in the JSON data but got " + data['matches']);
            }
            // validate the optional field `matches` (array)
            for (const item of data['matches']) {
                BaseMatch.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `prizepool`
        if (data['prizepool']) { // data not null
          Object.validateJSON(data['prizepool']);
        }
        // validate the optional field `serie`
        if (data['serie']) { // data not null
          BaseSerie.validateJSON(data['serie']);
        }
        // ensure the json data is a string
        if (data['slug'] && !(typeof data['slug'] === 'string' || data['slug'] instanceof String)) {
            throw new Error("Expected the field `slug` to be a primitive type in the JSON string but got " + data['slug']);
        }
        if (data['teams']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['teams'])) {
                throw new Error("Expected the field `teams` to be an array in the JSON data but got " + data['teams']);
            }
            // validate the optional field `teams` (array)
            for (const item of data['teams']) {
                BaseTeam.validateJSON(item);
            };
        }
        // validate the optional field `videogame`
        if (data['videogame']) { // data not null
          CurrentVideogame.validateJSON(data['videogame']);
        }
        // validate the optional field `winner_id`
        if (data['winner_id']) { // data not null
          OpponentID1.validateJSON(data['winner_id']);
        }
        // validate the optional field `winner_type`
        if (data['winner_type']) { // data not null
          Object.validateJSON(data['winner_type']);
        }

        return true;
    }


}

Tournament.RequiredProperties = ["begin_at", "end_at", "expected_roster", "id", "league", "league_id", "live_supported", "matches", "modified_at", "name", "prizepool", "serie", "serie_id", "slug", "teams", "videogame", "winner_id", "winner_type"];

/**
 * @member {Object} begin_at
 */
Tournament.prototype['begin_at'] = undefined;

/**
 * @member {Object} end_at
 */
Tournament.prototype['end_at'] = undefined;

/**
 * @member {Array.<module:model/TournamentRosterItem>} expected_roster
 */
Tournament.prototype['expected_roster'] = undefined;

/**
 * @member {Number} id
 */
Tournament.prototype['id'] = undefined;

/**
 * @member {module:model/BaseLeague} league
 */
Tournament.prototype['league'] = undefined;

/**
 * @member {Number} league_id
 */
Tournament.prototype['league_id'] = undefined;

/**
 * Whether live is supported
 * @member {Boolean} live_supported
 */
Tournament.prototype['live_supported'] = undefined;

/**
 * @member {Array.<module:model/BaseMatch>} matches
 */
Tournament.prototype['matches'] = undefined;

/**
 * @member {Date} modified_at
 */
Tournament.prototype['modified_at'] = undefined;

/**
 * @member {String} name
 */
Tournament.prototype['name'] = undefined;

/**
 * @member {Object} prizepool
 */
Tournament.prototype['prizepool'] = undefined;

/**
 * @member {module:model/BaseSerie} serie
 */
Tournament.prototype['serie'] = undefined;

/**
 * @member {Number} serie_id
 */
Tournament.prototype['serie_id'] = undefined;

/**
 * @member {String} slug
 */
Tournament.prototype['slug'] = undefined;

/**
 * @member {Array.<module:model/BaseTeam>} teams
 */
Tournament.prototype['teams'] = undefined;

/**
 * @member {module:model/CurrentVideogame} videogame
 */
Tournament.prototype['videogame'] = undefined;

/**
 * @member {module:model/OpponentID1} winner_id
 */
Tournament.prototype['winner_id'] = undefined;

/**
 * @member {Object} winner_type
 */
Tournament.prototype['winner_type'] = undefined;






export default Tournament;

