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
import BaseOpponent1 from './BaseOpponent1';
import BettingBaseTournament from './BettingBaseTournament';
import BettingGame from './BettingGame';
import BettingLeague1 from './BettingLeague1';
import BettingMatchStatus from './BettingMatchStatus';
import BettingMetadata from './BettingMetadata';
import BettingSerie1 from './BettingSerie1';
import CurrentVideogame from './CurrentVideogame';
import MatchLive from './MatchLive';
import MatchLocalizedStreams from './MatchLocalizedStreams';
import MatchResult from './MatchResult';
import MatchType from './MatchType';
import Opponent from './Opponent';
import OpponentID1 from './OpponentID1';
import ShortVideogameVersion1 from './ShortVideogameVersion1';
import Stream from './Stream';

/**
 * The BettingMatch model module.
 * @module model/BettingMatch
 * @version 2.23.1
 */
class BettingMatch {
    /**
     * Constructs a new <code>BettingMatch</code>.
     * @alias module:model/BettingMatch
     * @param beginAt {Object} 
     * @param bettingMetadata {module:model/BettingMetadata} 
     * @param detailedStats {Boolean} Whether the match offers full stats
     * @param draw {Boolean} Whether result of the match is a draw
     * @param endAt {Object} 
     * @param forfeit {Boolean} Whether match was forfeited
     * @param gameAdvantage {module:model/OpponentID1} 
     * @param games {Array.<module:model/BettingGame>} 
     * @param id {Number} 
     * @param league {module:model/BettingLeague1} 
     * @param leagueId {Number} 
     * @param live {module:model/MatchLive} 
     * @param liveEmbedUrl {Object} 
     * @param matchType {module:model/MatchType} 
     * @param modifiedAt {Date} 
     * @param name {String} 
     * @param numberOfGames {Number} Number of games
     * @param officialStreamUrl {Object} 
     * @param opponents {Array.<module:model/Opponent>} 
     * @param originalScheduledAt {Object} 
     * @param rescheduled {Object} 
     * @param results {Array.<module:model/MatchResult>} 
     * @param scheduledAt {Object} 
     * @param serie {module:model/BettingSerie1} 
     * @param serieId {Number} 
     * @param slug {Object} 
     * @param status {module:model/BettingMatchStatus} 
     * @param streams {module:model/MatchLocalizedStreams} 
     * @param streamsList {Array.<module:model/Stream>} 
     * @param tournament {module:model/BettingBaseTournament} 
     * @param tournamentId {Number} 
     * @param videogame {module:model/CurrentVideogame} 
     * @param videogameVersion {module:model/ShortVideogameVersion1} 
     * @param winner {module:model/BaseOpponent1} 
     * @param winnerId {module:model/OpponentID1} 
     */
    constructor(beginAt, bettingMetadata, detailedStats, draw, endAt, forfeit, gameAdvantage, games, id, league, leagueId, live, liveEmbedUrl, matchType, modifiedAt, name, numberOfGames, officialStreamUrl, opponents, originalScheduledAt, rescheduled, results, scheduledAt, serie, serieId, slug, status, streams, streamsList, tournament, tournamentId, videogame, videogameVersion, winner, winnerId) { 
        
        BettingMatch.initialize(this, beginAt, bettingMetadata, detailedStats, draw, endAt, forfeit, gameAdvantage, games, id, league, leagueId, live, liveEmbedUrl, matchType, modifiedAt, name, numberOfGames, officialStreamUrl, opponents, originalScheduledAt, rescheduled, results, scheduledAt, serie, serieId, slug, status, streams, streamsList, tournament, tournamentId, videogame, videogameVersion, winner, winnerId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, beginAt, bettingMetadata, detailedStats, draw, endAt, forfeit, gameAdvantage, games, id, league, leagueId, live, liveEmbedUrl, matchType, modifiedAt, name, numberOfGames, officialStreamUrl, opponents, originalScheduledAt, rescheduled, results, scheduledAt, serie, serieId, slug, status, streams, streamsList, tournament, tournamentId, videogame, videogameVersion, winner, winnerId) { 
        obj['begin_at'] = beginAt;
        obj['betting_metadata'] = bettingMetadata;
        obj['detailed_stats'] = detailedStats;
        obj['draw'] = draw;
        obj['end_at'] = endAt;
        obj['forfeit'] = forfeit;
        obj['game_advantage'] = gameAdvantage;
        obj['games'] = games;
        obj['id'] = id;
        obj['league'] = league;
        obj['league_id'] = leagueId;
        obj['live'] = live;
        obj['live_embed_url'] = liveEmbedUrl;
        obj['match_type'] = matchType;
        obj['modified_at'] = modifiedAt;
        obj['name'] = name;
        obj['number_of_games'] = numberOfGames;
        obj['official_stream_url'] = officialStreamUrl;
        obj['opponents'] = opponents;
        obj['original_scheduled_at'] = originalScheduledAt;
        obj['rescheduled'] = rescheduled;
        obj['results'] = results;
        obj['scheduled_at'] = scheduledAt;
        obj['serie'] = serie;
        obj['serie_id'] = serieId;
        obj['slug'] = slug;
        obj['status'] = status;
        obj['streams'] = streams;
        obj['streams_list'] = streamsList;
        obj['tournament'] = tournament;
        obj['tournament_id'] = tournamentId;
        obj['videogame'] = videogame;
        obj['videogame_version'] = videogameVersion;
        obj['winner'] = winner;
        obj['winner_id'] = winnerId;
    }

    /**
     * Constructs a <code>BettingMatch</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BettingMatch} obj Optional instance to populate.
     * @return {module:model/BettingMatch} The populated <code>BettingMatch</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BettingMatch();

            if (data.hasOwnProperty('begin_at')) {
                obj['begin_at'] = ApiClient.convertToType(data['begin_at'], Object);
            }
            if (data.hasOwnProperty('betting_metadata')) {
                obj['betting_metadata'] = BettingMetadata.constructFromObject(data['betting_metadata']);
            }
            if (data.hasOwnProperty('detailed_stats')) {
                obj['detailed_stats'] = ApiClient.convertToType(data['detailed_stats'], 'Boolean');
            }
            if (data.hasOwnProperty('draw')) {
                obj['draw'] = ApiClient.convertToType(data['draw'], 'Boolean');
            }
            if (data.hasOwnProperty('end_at')) {
                obj['end_at'] = ApiClient.convertToType(data['end_at'], Object);
            }
            if (data.hasOwnProperty('forfeit')) {
                obj['forfeit'] = ApiClient.convertToType(data['forfeit'], 'Boolean');
            }
            if (data.hasOwnProperty('game_advantage')) {
                obj['game_advantage'] = OpponentID1.constructFromObject(data['game_advantage']);
            }
            if (data.hasOwnProperty('games')) {
                obj['games'] = ApiClient.convertToType(data['games'], [BettingGame]);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('league')) {
                obj['league'] = BettingLeague1.constructFromObject(data['league']);
            }
            if (data.hasOwnProperty('league_id')) {
                obj['league_id'] = ApiClient.convertToType(data['league_id'], 'Number');
            }
            if (data.hasOwnProperty('live')) {
                obj['live'] = MatchLive.constructFromObject(data['live']);
            }
            if (data.hasOwnProperty('live_embed_url')) {
                obj['live_embed_url'] = ApiClient.convertToType(data['live_embed_url'], Object);
            }
            if (data.hasOwnProperty('match_type')) {
                obj['match_type'] = MatchType.constructFromObject(data['match_type']);
            }
            if (data.hasOwnProperty('modified_at')) {
                obj['modified_at'] = ApiClient.convertToType(data['modified_at'], 'Date');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('number_of_games')) {
                obj['number_of_games'] = ApiClient.convertToType(data['number_of_games'], 'Number');
            }
            if (data.hasOwnProperty('official_stream_url')) {
                obj['official_stream_url'] = ApiClient.convertToType(data['official_stream_url'], Object);
            }
            if (data.hasOwnProperty('opponents')) {
                obj['opponents'] = ApiClient.convertToType(data['opponents'], [Opponent]);
            }
            if (data.hasOwnProperty('original_scheduled_at')) {
                obj['original_scheduled_at'] = ApiClient.convertToType(data['original_scheduled_at'], Object);
            }
            if (data.hasOwnProperty('rescheduled')) {
                obj['rescheduled'] = ApiClient.convertToType(data['rescheduled'], Object);
            }
            if (data.hasOwnProperty('results')) {
                obj['results'] = ApiClient.convertToType(data['results'], [MatchResult]);
            }
            if (data.hasOwnProperty('scheduled_at')) {
                obj['scheduled_at'] = ApiClient.convertToType(data['scheduled_at'], Object);
            }
            if (data.hasOwnProperty('serie')) {
                obj['serie'] = BettingSerie1.constructFromObject(data['serie']);
            }
            if (data.hasOwnProperty('serie_id')) {
                obj['serie_id'] = ApiClient.convertToType(data['serie_id'], 'Number');
            }
            if (data.hasOwnProperty('slug')) {
                obj['slug'] = ApiClient.convertToType(data['slug'], Object);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = BettingMatchStatus.constructFromObject(data['status']);
            }
            if (data.hasOwnProperty('streams')) {
                obj['streams'] = MatchLocalizedStreams.constructFromObject(data['streams']);
            }
            if (data.hasOwnProperty('streams_list')) {
                obj['streams_list'] = ApiClient.convertToType(data['streams_list'], [Stream]);
            }
            if (data.hasOwnProperty('tournament')) {
                obj['tournament'] = BettingBaseTournament.constructFromObject(data['tournament']);
            }
            if (data.hasOwnProperty('tournament_id')) {
                obj['tournament_id'] = ApiClient.convertToType(data['tournament_id'], 'Number');
            }
            if (data.hasOwnProperty('videogame')) {
                obj['videogame'] = CurrentVideogame.constructFromObject(data['videogame']);
            }
            if (data.hasOwnProperty('videogame_version')) {
                obj['videogame_version'] = ShortVideogameVersion1.constructFromObject(data['videogame_version']);
            }
            if (data.hasOwnProperty('winner')) {
                obj['winner'] = BaseOpponent1.constructFromObject(data['winner']);
            }
            if (data.hasOwnProperty('winner_id')) {
                obj['winner_id'] = OpponentID1.constructFromObject(data['winner_id']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BettingMatch</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BettingMatch</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BettingMatch.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `begin_at`
        if (data['begin_at']) { // data not null
          Object.validateJSON(data['begin_at']);
        }
        // validate the optional field `betting_metadata`
        if (data['betting_metadata']) { // data not null
          BettingMetadata.validateJSON(data['betting_metadata']);
        }
        // validate the optional field `end_at`
        if (data['end_at']) { // data not null
          Object.validateJSON(data['end_at']);
        }
        // validate the optional field `game_advantage`
        if (data['game_advantage']) { // data not null
          OpponentID1.validateJSON(data['game_advantage']);
        }
        if (data['games']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['games'])) {
                throw new Error("Expected the field `games` to be an array in the JSON data but got " + data['games']);
            }
            // validate the optional field `games` (array)
            for (const item of data['games']) {
                BettingGame.validateJSON(item);
            };
        }
        // validate the optional field `league`
        if (data['league']) { // data not null
          BettingLeague1.validateJSON(data['league']);
        }
        // validate the optional field `live`
        if (data['live']) { // data not null
          MatchLive.validateJSON(data['live']);
        }
        // validate the optional field `live_embed_url`
        if (data['live_embed_url']) { // data not null
          Object.validateJSON(data['live_embed_url']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `official_stream_url`
        if (data['official_stream_url']) { // data not null
          Object.validateJSON(data['official_stream_url']);
        }
        if (data['opponents']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['opponents'])) {
                throw new Error("Expected the field `opponents` to be an array in the JSON data but got " + data['opponents']);
            }
            // validate the optional field `opponents` (array)
            for (const item of data['opponents']) {
                Opponent.validateJSON(item);
            };
        }
        // validate the optional field `original_scheduled_at`
        if (data['original_scheduled_at']) { // data not null
          Object.validateJSON(data['original_scheduled_at']);
        }
        // validate the optional field `rescheduled`
        if (data['rescheduled']) { // data not null
          Object.validateJSON(data['rescheduled']);
        }
        if (data['results']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['results'])) {
                throw new Error("Expected the field `results` to be an array in the JSON data but got " + data['results']);
            }
            // validate the optional field `results` (array)
            for (const item of data['results']) {
                MatchResult.validateJSON(item);
            };
        }
        // validate the optional field `scheduled_at`
        if (data['scheduled_at']) { // data not null
          Object.validateJSON(data['scheduled_at']);
        }
        // validate the optional field `serie`
        if (data['serie']) { // data not null
          BettingSerie1.validateJSON(data['serie']);
        }
        // validate the optional field `slug`
        if (data['slug']) { // data not null
          Object.validateJSON(data['slug']);
        }
        // validate the optional field `streams`
        if (data['streams']) { // data not null
          MatchLocalizedStreams.validateJSON(data['streams']);
        }
        if (data['streams_list']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['streams_list'])) {
                throw new Error("Expected the field `streams_list` to be an array in the JSON data but got " + data['streams_list']);
            }
            // validate the optional field `streams_list` (array)
            for (const item of data['streams_list']) {
                Stream.validateJSON(item);
            };
        }
        // validate the optional field `tournament`
        if (data['tournament']) { // data not null
          BettingBaseTournament.validateJSON(data['tournament']);
        }
        // validate the optional field `videogame`
        if (data['videogame']) { // data not null
          CurrentVideogame.validateJSON(data['videogame']);
        }
        // validate the optional field `videogame_version`
        if (data['videogame_version']) { // data not null
          ShortVideogameVersion1.validateJSON(data['videogame_version']);
        }
        // validate the optional field `winner`
        if (data['winner']) { // data not null
          BaseOpponent1.validateJSON(data['winner']);
        }
        // validate the optional field `winner_id`
        if (data['winner_id']) { // data not null
          OpponentID1.validateJSON(data['winner_id']);
        }

        return true;
    }


}

BettingMatch.RequiredProperties = ["begin_at", "betting_metadata", "detailed_stats", "draw", "end_at", "forfeit", "game_advantage", "games", "id", "league", "league_id", "live", "live_embed_url", "match_type", "modified_at", "name", "number_of_games", "official_stream_url", "opponents", "original_scheduled_at", "rescheduled", "results", "scheduled_at", "serie", "serie_id", "slug", "status", "streams", "streams_list", "tournament", "tournament_id", "videogame", "videogame_version", "winner", "winner_id"];

/**
 * @member {Object} begin_at
 */
BettingMatch.prototype['begin_at'] = undefined;

/**
 * @member {module:model/BettingMetadata} betting_metadata
 */
BettingMatch.prototype['betting_metadata'] = undefined;

/**
 * Whether the match offers full stats
 * @member {Boolean} detailed_stats
 */
BettingMatch.prototype['detailed_stats'] = undefined;

/**
 * Whether result of the match is a draw
 * @member {Boolean} draw
 */
BettingMatch.prototype['draw'] = undefined;

/**
 * @member {Object} end_at
 */
BettingMatch.prototype['end_at'] = undefined;

/**
 * Whether match was forfeited
 * @member {Boolean} forfeit
 */
BettingMatch.prototype['forfeit'] = undefined;

/**
 * @member {module:model/OpponentID1} game_advantage
 */
BettingMatch.prototype['game_advantage'] = undefined;

/**
 * @member {Array.<module:model/BettingGame>} games
 */
BettingMatch.prototype['games'] = undefined;

/**
 * @member {Number} id
 */
BettingMatch.prototype['id'] = undefined;

/**
 * @member {module:model/BettingLeague1} league
 */
BettingMatch.prototype['league'] = undefined;

/**
 * @member {Number} league_id
 */
BettingMatch.prototype['league_id'] = undefined;

/**
 * @member {module:model/MatchLive} live
 */
BettingMatch.prototype['live'] = undefined;

/**
 * @member {Object} live_embed_url
 */
BettingMatch.prototype['live_embed_url'] = undefined;

/**
 * @member {module:model/MatchType} match_type
 */
BettingMatch.prototype['match_type'] = undefined;

/**
 * @member {Date} modified_at
 */
BettingMatch.prototype['modified_at'] = undefined;

/**
 * @member {String} name
 */
BettingMatch.prototype['name'] = undefined;

/**
 * Number of games
 * @member {Number} number_of_games
 */
BettingMatch.prototype['number_of_games'] = undefined;

/**
 * @member {Object} official_stream_url
 */
BettingMatch.prototype['official_stream_url'] = undefined;

/**
 * @member {Array.<module:model/Opponent>} opponents
 */
BettingMatch.prototype['opponents'] = undefined;

/**
 * @member {Object} original_scheduled_at
 */
BettingMatch.prototype['original_scheduled_at'] = undefined;

/**
 * @member {Object} rescheduled
 */
BettingMatch.prototype['rescheduled'] = undefined;

/**
 * @member {Array.<module:model/MatchResult>} results
 */
BettingMatch.prototype['results'] = undefined;

/**
 * @member {Object} scheduled_at
 */
BettingMatch.prototype['scheduled_at'] = undefined;

/**
 * @member {module:model/BettingSerie1} serie
 */
BettingMatch.prototype['serie'] = undefined;

/**
 * @member {Number} serie_id
 */
BettingMatch.prototype['serie_id'] = undefined;

/**
 * @member {Object} slug
 */
BettingMatch.prototype['slug'] = undefined;

/**
 * @member {module:model/BettingMatchStatus} status
 */
BettingMatch.prototype['status'] = undefined;

/**
 * @member {module:model/MatchLocalizedStreams} streams
 */
BettingMatch.prototype['streams'] = undefined;

/**
 * @member {Array.<module:model/Stream>} streams_list
 */
BettingMatch.prototype['streams_list'] = undefined;

/**
 * @member {module:model/BettingBaseTournament} tournament
 */
BettingMatch.prototype['tournament'] = undefined;

/**
 * @member {Number} tournament_id
 */
BettingMatch.prototype['tournament_id'] = undefined;

/**
 * @member {module:model/CurrentVideogame} videogame
 */
BettingMatch.prototype['videogame'] = undefined;

/**
 * @member {module:model/ShortVideogameVersion1} videogame_version
 */
BettingMatch.prototype['videogame_version'] = undefined;

/**
 * @member {module:model/BaseOpponent1} winner
 */
BettingMatch.prototype['winner'] = undefined;

/**
 * @member {module:model/OpponentID1} winner_id
 */
BettingMatch.prototype['winner_id'] = undefined;






export default BettingMatch;

