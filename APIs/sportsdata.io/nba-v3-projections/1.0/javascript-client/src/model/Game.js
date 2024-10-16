/**
 * NBA v3 Projections
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Quarter from './Quarter';
import Series from './Series';

/**
 * The Game model module.
 * @module model/Game
 * @version 1.0
 */
class Game {
    /**
     * Constructs a new <code>Game</code>.
     * @alias module:model/Game
     */
    constructor() { 
        
        Game.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
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

            if (data.hasOwnProperty('AlternateID')) {
                obj['AlternateID'] = ApiClient.convertToType(data['AlternateID'], 'Number');
            }
            if (data.hasOwnProperty('Attendance')) {
                obj['Attendance'] = ApiClient.convertToType(data['Attendance'], 'Number');
            }
            if (data.hasOwnProperty('AwayRotationNumber')) {
                obj['AwayRotationNumber'] = ApiClient.convertToType(data['AwayRotationNumber'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeam')) {
                obj['AwayTeam'] = ApiClient.convertToType(data['AwayTeam'], 'String');
            }
            if (data.hasOwnProperty('AwayTeamID')) {
                obj['AwayTeamID'] = ApiClient.convertToType(data['AwayTeamID'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeamMoneyLine')) {
                obj['AwayTeamMoneyLine'] = ApiClient.convertToType(data['AwayTeamMoneyLine'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeamScore')) {
                obj['AwayTeamScore'] = ApiClient.convertToType(data['AwayTeamScore'], 'Number');
            }
            if (data.hasOwnProperty('Channel')) {
                obj['Channel'] = ApiClient.convertToType(data['Channel'], 'String');
            }
            if (data.hasOwnProperty('CrewChiefID')) {
                obj['CrewChiefID'] = ApiClient.convertToType(data['CrewChiefID'], 'Number');
            }
            if (data.hasOwnProperty('DateTime')) {
                obj['DateTime'] = ApiClient.convertToType(data['DateTime'], 'String');
            }
            if (data.hasOwnProperty('DateTimeUTC')) {
                obj['DateTimeUTC'] = ApiClient.convertToType(data['DateTimeUTC'], 'String');
            }
            if (data.hasOwnProperty('Day')) {
                obj['Day'] = ApiClient.convertToType(data['Day'], 'String');
            }
            if (data.hasOwnProperty('GameEndDateTime')) {
                obj['GameEndDateTime'] = ApiClient.convertToType(data['GameEndDateTime'], 'String');
            }
            if (data.hasOwnProperty('GameID')) {
                obj['GameID'] = ApiClient.convertToType(data['GameID'], 'Number');
            }
            if (data.hasOwnProperty('GlobalAwayTeamID')) {
                obj['GlobalAwayTeamID'] = ApiClient.convertToType(data['GlobalAwayTeamID'], 'Number');
            }
            if (data.hasOwnProperty('GlobalGameID')) {
                obj['GlobalGameID'] = ApiClient.convertToType(data['GlobalGameID'], 'Number');
            }
            if (data.hasOwnProperty('GlobalHomeTeamID')) {
                obj['GlobalHomeTeamID'] = ApiClient.convertToType(data['GlobalHomeTeamID'], 'Number');
            }
            if (data.hasOwnProperty('HomeRotationNumber')) {
                obj['HomeRotationNumber'] = ApiClient.convertToType(data['HomeRotationNumber'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeam')) {
                obj['HomeTeam'] = ApiClient.convertToType(data['HomeTeam'], 'String');
            }
            if (data.hasOwnProperty('HomeTeamID')) {
                obj['HomeTeamID'] = ApiClient.convertToType(data['HomeTeamID'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamMoneyLine')) {
                obj['HomeTeamMoneyLine'] = ApiClient.convertToType(data['HomeTeamMoneyLine'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamScore')) {
                obj['HomeTeamScore'] = ApiClient.convertToType(data['HomeTeamScore'], 'Number');
            }
            if (data.hasOwnProperty('IsClosed')) {
                obj['IsClosed'] = ApiClient.convertToType(data['IsClosed'], 'Boolean');
            }
            if (data.hasOwnProperty('LastPlay')) {
                obj['LastPlay'] = ApiClient.convertToType(data['LastPlay'], 'String');
            }
            if (data.hasOwnProperty('NeutralVenue')) {
                obj['NeutralVenue'] = ApiClient.convertToType(data['NeutralVenue'], 'Boolean');
            }
            if (data.hasOwnProperty('OverPayout')) {
                obj['OverPayout'] = ApiClient.convertToType(data['OverPayout'], 'Number');
            }
            if (data.hasOwnProperty('OverUnder')) {
                obj['OverUnder'] = ApiClient.convertToType(data['OverUnder'], 'Number');
            }
            if (data.hasOwnProperty('PointSpread')) {
                obj['PointSpread'] = ApiClient.convertToType(data['PointSpread'], 'Number');
            }
            if (data.hasOwnProperty('PointSpreadAwayTeamMoneyLine')) {
                obj['PointSpreadAwayTeamMoneyLine'] = ApiClient.convertToType(data['PointSpreadAwayTeamMoneyLine'], 'Number');
            }
            if (data.hasOwnProperty('PointSpreadHomeTeamMoneyLine')) {
                obj['PointSpreadHomeTeamMoneyLine'] = ApiClient.convertToType(data['PointSpreadHomeTeamMoneyLine'], 'Number');
            }
            if (data.hasOwnProperty('Quarter')) {
                obj['Quarter'] = ApiClient.convertToType(data['Quarter'], 'String');
            }
            if (data.hasOwnProperty('Quarters')) {
                obj['Quarters'] = ApiClient.convertToType(data['Quarters'], [Quarter]);
            }
            if (data.hasOwnProperty('RefereeID')) {
                obj['RefereeID'] = ApiClient.convertToType(data['RefereeID'], 'Number');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('SeasonType')) {
                obj['SeasonType'] = ApiClient.convertToType(data['SeasonType'], 'Number');
            }
            if (data.hasOwnProperty('SeriesInfo')) {
                obj['SeriesInfo'] = Series.constructFromObject(data['SeriesInfo']);
            }
            if (data.hasOwnProperty('StadiumID')) {
                obj['StadiumID'] = ApiClient.convertToType(data['StadiumID'], 'Number');
            }
            if (data.hasOwnProperty('Status')) {
                obj['Status'] = ApiClient.convertToType(data['Status'], 'String');
            }
            if (data.hasOwnProperty('TimeRemainingMinutes')) {
                obj['TimeRemainingMinutes'] = ApiClient.convertToType(data['TimeRemainingMinutes'], 'Number');
            }
            if (data.hasOwnProperty('TimeRemainingSeconds')) {
                obj['TimeRemainingSeconds'] = ApiClient.convertToType(data['TimeRemainingSeconds'], 'Number');
            }
            if (data.hasOwnProperty('UmpireID')) {
                obj['UmpireID'] = ApiClient.convertToType(data['UmpireID'], 'Number');
            }
            if (data.hasOwnProperty('UnderPayout')) {
                obj['UnderPayout'] = ApiClient.convertToType(data['UnderPayout'], 'Number');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
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
        // ensure the json data is a string
        if (data['AwayTeam'] && !(typeof data['AwayTeam'] === 'string' || data['AwayTeam'] instanceof String)) {
            throw new Error("Expected the field `AwayTeam` to be a primitive type in the JSON string but got " + data['AwayTeam']);
        }
        // ensure the json data is a string
        if (data['Channel'] && !(typeof data['Channel'] === 'string' || data['Channel'] instanceof String)) {
            throw new Error("Expected the field `Channel` to be a primitive type in the JSON string but got " + data['Channel']);
        }
        // ensure the json data is a string
        if (data['DateTime'] && !(typeof data['DateTime'] === 'string' || data['DateTime'] instanceof String)) {
            throw new Error("Expected the field `DateTime` to be a primitive type in the JSON string but got " + data['DateTime']);
        }
        // ensure the json data is a string
        if (data['DateTimeUTC'] && !(typeof data['DateTimeUTC'] === 'string' || data['DateTimeUTC'] instanceof String)) {
            throw new Error("Expected the field `DateTimeUTC` to be a primitive type in the JSON string but got " + data['DateTimeUTC']);
        }
        // ensure the json data is a string
        if (data['Day'] && !(typeof data['Day'] === 'string' || data['Day'] instanceof String)) {
            throw new Error("Expected the field `Day` to be a primitive type in the JSON string but got " + data['Day']);
        }
        // ensure the json data is a string
        if (data['GameEndDateTime'] && !(typeof data['GameEndDateTime'] === 'string' || data['GameEndDateTime'] instanceof String)) {
            throw new Error("Expected the field `GameEndDateTime` to be a primitive type in the JSON string but got " + data['GameEndDateTime']);
        }
        // ensure the json data is a string
        if (data['HomeTeam'] && !(typeof data['HomeTeam'] === 'string' || data['HomeTeam'] instanceof String)) {
            throw new Error("Expected the field `HomeTeam` to be a primitive type in the JSON string but got " + data['HomeTeam']);
        }
        // ensure the json data is a string
        if (data['LastPlay'] && !(typeof data['LastPlay'] === 'string' || data['LastPlay'] instanceof String)) {
            throw new Error("Expected the field `LastPlay` to be a primitive type in the JSON string but got " + data['LastPlay']);
        }
        // ensure the json data is a string
        if (data['Quarter'] && !(typeof data['Quarter'] === 'string' || data['Quarter'] instanceof String)) {
            throw new Error("Expected the field `Quarter` to be a primitive type in the JSON string but got " + data['Quarter']);
        }
        if (data['Quarters']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Quarters'])) {
                throw new Error("Expected the field `Quarters` to be an array in the JSON data but got " + data['Quarters']);
            }
            // validate the optional field `Quarters` (array)
            for (const item of data['Quarters']) {
                Quarter.validateJSON(item);
            };
        }
        // validate the optional field `SeriesInfo`
        if (data['SeriesInfo']) { // data not null
          Series.validateJSON(data['SeriesInfo']);
        }
        // ensure the json data is a string
        if (data['Status'] && !(typeof data['Status'] === 'string' || data['Status'] instanceof String)) {
            throw new Error("Expected the field `Status` to be a primitive type in the JSON string but got " + data['Status']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }

        return true;
    }


}



/**
 * @member {Number} AlternateID
 */
Game.prototype['AlternateID'] = undefined;

/**
 * @member {Number} Attendance
 */
Game.prototype['Attendance'] = undefined;

/**
 * @member {Number} AwayRotationNumber
 */
Game.prototype['AwayRotationNumber'] = undefined;

/**
 * @member {String} AwayTeam
 */
Game.prototype['AwayTeam'] = undefined;

/**
 * @member {Number} AwayTeamID
 */
Game.prototype['AwayTeamID'] = undefined;

/**
 * @member {Number} AwayTeamMoneyLine
 */
Game.prototype['AwayTeamMoneyLine'] = undefined;

/**
 * @member {Number} AwayTeamScore
 */
Game.prototype['AwayTeamScore'] = undefined;

/**
 * @member {String} Channel
 */
Game.prototype['Channel'] = undefined;

/**
 * @member {Number} CrewChiefID
 */
Game.prototype['CrewChiefID'] = undefined;

/**
 * @member {String} DateTime
 */
Game.prototype['DateTime'] = undefined;

/**
 * @member {String} DateTimeUTC
 */
Game.prototype['DateTimeUTC'] = undefined;

/**
 * @member {String} Day
 */
Game.prototype['Day'] = undefined;

/**
 * @member {String} GameEndDateTime
 */
Game.prototype['GameEndDateTime'] = undefined;

/**
 * @member {Number} GameID
 */
Game.prototype['GameID'] = undefined;

/**
 * @member {Number} GlobalAwayTeamID
 */
Game.prototype['GlobalAwayTeamID'] = undefined;

/**
 * @member {Number} GlobalGameID
 */
Game.prototype['GlobalGameID'] = undefined;

/**
 * @member {Number} GlobalHomeTeamID
 */
Game.prototype['GlobalHomeTeamID'] = undefined;

/**
 * @member {Number} HomeRotationNumber
 */
Game.prototype['HomeRotationNumber'] = undefined;

/**
 * @member {String} HomeTeam
 */
Game.prototype['HomeTeam'] = undefined;

/**
 * @member {Number} HomeTeamID
 */
Game.prototype['HomeTeamID'] = undefined;

/**
 * @member {Number} HomeTeamMoneyLine
 */
Game.prototype['HomeTeamMoneyLine'] = undefined;

/**
 * @member {Number} HomeTeamScore
 */
Game.prototype['HomeTeamScore'] = undefined;

/**
 * @member {Boolean} IsClosed
 */
Game.prototype['IsClosed'] = undefined;

/**
 * @member {String} LastPlay
 */
Game.prototype['LastPlay'] = undefined;

/**
 * @member {Boolean} NeutralVenue
 */
Game.prototype['NeutralVenue'] = undefined;

/**
 * @member {Number} OverPayout
 */
Game.prototype['OverPayout'] = undefined;

/**
 * @member {Number} OverUnder
 */
Game.prototype['OverUnder'] = undefined;

/**
 * @member {Number} PointSpread
 */
Game.prototype['PointSpread'] = undefined;

/**
 * @member {Number} PointSpreadAwayTeamMoneyLine
 */
Game.prototype['PointSpreadAwayTeamMoneyLine'] = undefined;

/**
 * @member {Number} PointSpreadHomeTeamMoneyLine
 */
Game.prototype['PointSpreadHomeTeamMoneyLine'] = undefined;

/**
 * @member {String} Quarter
 */
Game.prototype['Quarter'] = undefined;

/**
 * @member {Array.<module:model/Quarter>} Quarters
 */
Game.prototype['Quarters'] = undefined;

/**
 * @member {Number} RefereeID
 */
Game.prototype['RefereeID'] = undefined;

/**
 * @member {Number} Season
 */
Game.prototype['Season'] = undefined;

/**
 * @member {Number} SeasonType
 */
Game.prototype['SeasonType'] = undefined;

/**
 * @member {module:model/Series} SeriesInfo
 */
Game.prototype['SeriesInfo'] = undefined;

/**
 * @member {Number} StadiumID
 */
Game.prototype['StadiumID'] = undefined;

/**
 * @member {String} Status
 */
Game.prototype['Status'] = undefined;

/**
 * @member {Number} TimeRemainingMinutes
 */
Game.prototype['TimeRemainingMinutes'] = undefined;

/**
 * @member {Number} TimeRemainingSeconds
 */
Game.prototype['TimeRemainingSeconds'] = undefined;

/**
 * @member {Number} UmpireID
 */
Game.prototype['UmpireID'] = undefined;

/**
 * @member {Number} UnderPayout
 */
Game.prototype['UnderPayout'] = undefined;

/**
 * @member {String} Updated
 */
Game.prototype['Updated'] = undefined;






export default Game;

