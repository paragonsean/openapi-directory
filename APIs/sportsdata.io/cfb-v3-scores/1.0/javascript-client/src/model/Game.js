/**
 * CFB v3 Scores
 * CFB schedules, scores, team stats, odds, weather, and news API.
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
import Period from './Period';
import Stadium from './Stadium';

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

            if (data.hasOwnProperty('Attendance')) {
                obj['Attendance'] = ApiClient.convertToType(data['Attendance'], 'Number');
            }
            if (data.hasOwnProperty('AwayPointSpreadPayout')) {
                obj['AwayPointSpreadPayout'] = ApiClient.convertToType(data['AwayPointSpreadPayout'], 'Number');
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
            if (data.hasOwnProperty('AwayTeamName')) {
                obj['AwayTeamName'] = ApiClient.convertToType(data['AwayTeamName'], 'String');
            }
            if (data.hasOwnProperty('AwayTeamScore')) {
                obj['AwayTeamScore'] = ApiClient.convertToType(data['AwayTeamScore'], 'Number');
            }
            if (data.hasOwnProperty('Channel')) {
                obj['Channel'] = ApiClient.convertToType(data['Channel'], 'String');
            }
            if (data.hasOwnProperty('Created')) {
                obj['Created'] = ApiClient.convertToType(data['Created'], 'String');
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
            if (data.hasOwnProperty('Distance')) {
                obj['Distance'] = ApiClient.convertToType(data['Distance'], 'Number');
            }
            if (data.hasOwnProperty('Down')) {
                obj['Down'] = ApiClient.convertToType(data['Down'], 'Number');
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
            if (data.hasOwnProperty('HomePointSpreadPayout')) {
                obj['HomePointSpreadPayout'] = ApiClient.convertToType(data['HomePointSpreadPayout'], 'Number');
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
            if (data.hasOwnProperty('HomeTeamName')) {
                obj['HomeTeamName'] = ApiClient.convertToType(data['HomeTeamName'], 'String');
            }
            if (data.hasOwnProperty('HomeTeamScore')) {
                obj['HomeTeamScore'] = ApiClient.convertToType(data['HomeTeamScore'], 'Number');
            }
            if (data.hasOwnProperty('IsClosed')) {
                obj['IsClosed'] = ApiClient.convertToType(data['IsClosed'], 'Boolean');
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
            if (data.hasOwnProperty('Period')) {
                obj['Period'] = ApiClient.convertToType(data['Period'], 'String');
            }
            if (data.hasOwnProperty('Periods')) {
                obj['Periods'] = ApiClient.convertToType(data['Periods'], [Period]);
            }
            if (data.hasOwnProperty('PointSpread')) {
                obj['PointSpread'] = ApiClient.convertToType(data['PointSpread'], 'Number');
            }
            if (data.hasOwnProperty('Possession')) {
                obj['Possession'] = ApiClient.convertToType(data['Possession'], 'String');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('SeasonType')) {
                obj['SeasonType'] = ApiClient.convertToType(data['SeasonType'], 'Number');
            }
            if (data.hasOwnProperty('Stadium')) {
                obj['Stadium'] = Stadium.constructFromObject(data['Stadium']);
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
            if (data.hasOwnProperty('Title')) {
                obj['Title'] = ApiClient.convertToType(data['Title'], 'String');
            }
            if (data.hasOwnProperty('UnderPayout')) {
                obj['UnderPayout'] = ApiClient.convertToType(data['UnderPayout'], 'Number');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
            if (data.hasOwnProperty('Week')) {
                obj['Week'] = ApiClient.convertToType(data['Week'], 'Number');
            }
            if (data.hasOwnProperty('YardLine')) {
                obj['YardLine'] = ApiClient.convertToType(data['YardLine'], 'Number');
            }
            if (data.hasOwnProperty('YardLineTerritory')) {
                obj['YardLineTerritory'] = ApiClient.convertToType(data['YardLineTerritory'], 'String');
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
        if (data['AwayTeamName'] && !(typeof data['AwayTeamName'] === 'string' || data['AwayTeamName'] instanceof String)) {
            throw new Error("Expected the field `AwayTeamName` to be a primitive type in the JSON string but got " + data['AwayTeamName']);
        }
        // ensure the json data is a string
        if (data['Channel'] && !(typeof data['Channel'] === 'string' || data['Channel'] instanceof String)) {
            throw new Error("Expected the field `Channel` to be a primitive type in the JSON string but got " + data['Channel']);
        }
        // ensure the json data is a string
        if (data['Created'] && !(typeof data['Created'] === 'string' || data['Created'] instanceof String)) {
            throw new Error("Expected the field `Created` to be a primitive type in the JSON string but got " + data['Created']);
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
        if (data['HomeTeamName'] && !(typeof data['HomeTeamName'] === 'string' || data['HomeTeamName'] instanceof String)) {
            throw new Error("Expected the field `HomeTeamName` to be a primitive type in the JSON string but got " + data['HomeTeamName']);
        }
        // ensure the json data is a string
        if (data['Period'] && !(typeof data['Period'] === 'string' || data['Period'] instanceof String)) {
            throw new Error("Expected the field `Period` to be a primitive type in the JSON string but got " + data['Period']);
        }
        if (data['Periods']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Periods'])) {
                throw new Error("Expected the field `Periods` to be an array in the JSON data but got " + data['Periods']);
            }
            // validate the optional field `Periods` (array)
            for (const item of data['Periods']) {
                Period.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['Possession'] && !(typeof data['Possession'] === 'string' || data['Possession'] instanceof String)) {
            throw new Error("Expected the field `Possession` to be a primitive type in the JSON string but got " + data['Possession']);
        }
        // validate the optional field `Stadium`
        if (data['Stadium']) { // data not null
          Stadium.validateJSON(data['Stadium']);
        }
        // ensure the json data is a string
        if (data['Status'] && !(typeof data['Status'] === 'string' || data['Status'] instanceof String)) {
            throw new Error("Expected the field `Status` to be a primitive type in the JSON string but got " + data['Status']);
        }
        // ensure the json data is a string
        if (data['Title'] && !(typeof data['Title'] === 'string' || data['Title'] instanceof String)) {
            throw new Error("Expected the field `Title` to be a primitive type in the JSON string but got " + data['Title']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }
        // ensure the json data is a string
        if (data['YardLineTerritory'] && !(typeof data['YardLineTerritory'] === 'string' || data['YardLineTerritory'] instanceof String)) {
            throw new Error("Expected the field `YardLineTerritory` to be a primitive type in the JSON string but got " + data['YardLineTerritory']);
        }

        return true;
    }


}



/**
 * @member {Number} Attendance
 */
Game.prototype['Attendance'] = undefined;

/**
 * @member {Number} AwayPointSpreadPayout
 */
Game.prototype['AwayPointSpreadPayout'] = undefined;

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
 * @member {String} AwayTeamName
 */
Game.prototype['AwayTeamName'] = undefined;

/**
 * @member {Number} AwayTeamScore
 */
Game.prototype['AwayTeamScore'] = undefined;

/**
 * @member {String} Channel
 */
Game.prototype['Channel'] = undefined;

/**
 * @member {String} Created
 */
Game.prototype['Created'] = undefined;

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
 * @member {Number} Distance
 */
Game.prototype['Distance'] = undefined;

/**
 * @member {Number} Down
 */
Game.prototype['Down'] = undefined;

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
 * @member {Number} HomePointSpreadPayout
 */
Game.prototype['HomePointSpreadPayout'] = undefined;

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
 * @member {String} HomeTeamName
 */
Game.prototype['HomeTeamName'] = undefined;

/**
 * @member {Number} HomeTeamScore
 */
Game.prototype['HomeTeamScore'] = undefined;

/**
 * @member {Boolean} IsClosed
 */
Game.prototype['IsClosed'] = undefined;

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
 * @member {String} Period
 */
Game.prototype['Period'] = undefined;

/**
 * @member {Array.<module:model/Period>} Periods
 */
Game.prototype['Periods'] = undefined;

/**
 * @member {Number} PointSpread
 */
Game.prototype['PointSpread'] = undefined;

/**
 * @member {String} Possession
 */
Game.prototype['Possession'] = undefined;

/**
 * @member {Number} Season
 */
Game.prototype['Season'] = undefined;

/**
 * @member {Number} SeasonType
 */
Game.prototype['SeasonType'] = undefined;

/**
 * @member {module:model/Stadium} Stadium
 */
Game.prototype['Stadium'] = undefined;

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
 * @member {String} Title
 */
Game.prototype['Title'] = undefined;

/**
 * @member {Number} UnderPayout
 */
Game.prototype['UnderPayout'] = undefined;

/**
 * @member {String} Updated
 */
Game.prototype['Updated'] = undefined;

/**
 * @member {Number} Week
 */
Game.prototype['Week'] = undefined;

/**
 * @member {Number} YardLine
 */
Game.prototype['YardLine'] = undefined;

/**
 * @member {String} YardLineTerritory
 */
Game.prototype['YardLineTerritory'] = undefined;






export default Game;

