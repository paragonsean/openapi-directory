/**
 * MLB v3 Play-by-Play
 * MLB play-by-play API.
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
import Inning from './Inning';
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

            if (data.hasOwnProperty('Attendance')) {
                obj['Attendance'] = ApiClient.convertToType(data['Attendance'], 'Number');
            }
            if (data.hasOwnProperty('AwayRotationNumber')) {
                obj['AwayRotationNumber'] = ApiClient.convertToType(data['AwayRotationNumber'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeam')) {
                obj['AwayTeam'] = ApiClient.convertToType(data['AwayTeam'], 'String');
            }
            if (data.hasOwnProperty('AwayTeamErrors')) {
                obj['AwayTeamErrors'] = ApiClient.convertToType(data['AwayTeamErrors'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeamHits')) {
                obj['AwayTeamHits'] = ApiClient.convertToType(data['AwayTeamHits'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeamID')) {
                obj['AwayTeamID'] = ApiClient.convertToType(data['AwayTeamID'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeamMoneyLine')) {
                obj['AwayTeamMoneyLine'] = ApiClient.convertToType(data['AwayTeamMoneyLine'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeamProbablePitcherID')) {
                obj['AwayTeamProbablePitcherID'] = ApiClient.convertToType(data['AwayTeamProbablePitcherID'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeamRuns')) {
                obj['AwayTeamRuns'] = ApiClient.convertToType(data['AwayTeamRuns'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeamStartingPitcher')) {
                obj['AwayTeamStartingPitcher'] = ApiClient.convertToType(data['AwayTeamStartingPitcher'], 'String');
            }
            if (data.hasOwnProperty('AwayTeamStartingPitcherID')) {
                obj['AwayTeamStartingPitcherID'] = ApiClient.convertToType(data['AwayTeamStartingPitcherID'], 'Number');
            }
            if (data.hasOwnProperty('Balls')) {
                obj['Balls'] = ApiClient.convertToType(data['Balls'], 'Number');
            }
            if (data.hasOwnProperty('Channel')) {
                obj['Channel'] = ApiClient.convertToType(data['Channel'], 'String');
            }
            if (data.hasOwnProperty('CurrentHitter')) {
                obj['CurrentHitter'] = ApiClient.convertToType(data['CurrentHitter'], 'String');
            }
            if (data.hasOwnProperty('CurrentHitterID')) {
                obj['CurrentHitterID'] = ApiClient.convertToType(data['CurrentHitterID'], 'Number');
            }
            if (data.hasOwnProperty('CurrentHittingTeamID')) {
                obj['CurrentHittingTeamID'] = ApiClient.convertToType(data['CurrentHittingTeamID'], 'Number');
            }
            if (data.hasOwnProperty('CurrentPitcher')) {
                obj['CurrentPitcher'] = ApiClient.convertToType(data['CurrentPitcher'], 'String');
            }
            if (data.hasOwnProperty('CurrentPitcherID')) {
                obj['CurrentPitcherID'] = ApiClient.convertToType(data['CurrentPitcherID'], 'Number');
            }
            if (data.hasOwnProperty('CurrentPitchingTeamID')) {
                obj['CurrentPitchingTeamID'] = ApiClient.convertToType(data['CurrentPitchingTeamID'], 'Number');
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
            if (data.hasOwnProperty('DueUpHitterID1')) {
                obj['DueUpHitterID1'] = ApiClient.convertToType(data['DueUpHitterID1'], 'Number');
            }
            if (data.hasOwnProperty('DueUpHitterID2')) {
                obj['DueUpHitterID2'] = ApiClient.convertToType(data['DueUpHitterID2'], 'Number');
            }
            if (data.hasOwnProperty('DueUpHitterID3')) {
                obj['DueUpHitterID3'] = ApiClient.convertToType(data['DueUpHitterID3'], 'Number');
            }
            if (data.hasOwnProperty('ForecastDescription')) {
                obj['ForecastDescription'] = ApiClient.convertToType(data['ForecastDescription'], 'String');
            }
            if (data.hasOwnProperty('ForecastTempHigh')) {
                obj['ForecastTempHigh'] = ApiClient.convertToType(data['ForecastTempHigh'], 'Number');
            }
            if (data.hasOwnProperty('ForecastTempLow')) {
                obj['ForecastTempLow'] = ApiClient.convertToType(data['ForecastTempLow'], 'Number');
            }
            if (data.hasOwnProperty('ForecastWindChill')) {
                obj['ForecastWindChill'] = ApiClient.convertToType(data['ForecastWindChill'], 'Number');
            }
            if (data.hasOwnProperty('ForecastWindDirection')) {
                obj['ForecastWindDirection'] = ApiClient.convertToType(data['ForecastWindDirection'], 'Number');
            }
            if (data.hasOwnProperty('ForecastWindSpeed')) {
                obj['ForecastWindSpeed'] = ApiClient.convertToType(data['ForecastWindSpeed'], 'Number');
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
            if (data.hasOwnProperty('HomeTeamErrors')) {
                obj['HomeTeamErrors'] = ApiClient.convertToType(data['HomeTeamErrors'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamHits')) {
                obj['HomeTeamHits'] = ApiClient.convertToType(data['HomeTeamHits'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamID')) {
                obj['HomeTeamID'] = ApiClient.convertToType(data['HomeTeamID'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamMoneyLine')) {
                obj['HomeTeamMoneyLine'] = ApiClient.convertToType(data['HomeTeamMoneyLine'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamProbablePitcherID')) {
                obj['HomeTeamProbablePitcherID'] = ApiClient.convertToType(data['HomeTeamProbablePitcherID'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamRuns')) {
                obj['HomeTeamRuns'] = ApiClient.convertToType(data['HomeTeamRuns'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamStartingPitcher')) {
                obj['HomeTeamStartingPitcher'] = ApiClient.convertToType(data['HomeTeamStartingPitcher'], 'String');
            }
            if (data.hasOwnProperty('HomeTeamStartingPitcherID')) {
                obj['HomeTeamStartingPitcherID'] = ApiClient.convertToType(data['HomeTeamStartingPitcherID'], 'Number');
            }
            if (data.hasOwnProperty('Inning')) {
                obj['Inning'] = ApiClient.convertToType(data['Inning'], 'Number');
            }
            if (data.hasOwnProperty('InningDescription')) {
                obj['InningDescription'] = ApiClient.convertToType(data['InningDescription'], 'String');
            }
            if (data.hasOwnProperty('InningHalf')) {
                obj['InningHalf'] = ApiClient.convertToType(data['InningHalf'], 'String');
            }
            if (data.hasOwnProperty('Innings')) {
                obj['Innings'] = ApiClient.convertToType(data['Innings'], [Inning]);
            }
            if (data.hasOwnProperty('IsClosed')) {
                obj['IsClosed'] = ApiClient.convertToType(data['IsClosed'], 'Boolean');
            }
            if (data.hasOwnProperty('LastPlay')) {
                obj['LastPlay'] = ApiClient.convertToType(data['LastPlay'], 'String');
            }
            if (data.hasOwnProperty('LosingPitcher')) {
                obj['LosingPitcher'] = ApiClient.convertToType(data['LosingPitcher'], 'String');
            }
            if (data.hasOwnProperty('LosingPitcherID')) {
                obj['LosingPitcherID'] = ApiClient.convertToType(data['LosingPitcherID'], 'Number');
            }
            if (data.hasOwnProperty('NeutralVenue')) {
                obj['NeutralVenue'] = ApiClient.convertToType(data['NeutralVenue'], 'Boolean');
            }
            if (data.hasOwnProperty('Outs')) {
                obj['Outs'] = ApiClient.convertToType(data['Outs'], 'Number');
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
            if (data.hasOwnProperty('RescheduledFromGameID')) {
                obj['RescheduledFromGameID'] = ApiClient.convertToType(data['RescheduledFromGameID'], 'Number');
            }
            if (data.hasOwnProperty('RescheduledGameID')) {
                obj['RescheduledGameID'] = ApiClient.convertToType(data['RescheduledGameID'], 'Number');
            }
            if (data.hasOwnProperty('RunnerOnFirst')) {
                obj['RunnerOnFirst'] = ApiClient.convertToType(data['RunnerOnFirst'], 'Boolean');
            }
            if (data.hasOwnProperty('RunnerOnSecond')) {
                obj['RunnerOnSecond'] = ApiClient.convertToType(data['RunnerOnSecond'], 'Boolean');
            }
            if (data.hasOwnProperty('RunnerOnThird')) {
                obj['RunnerOnThird'] = ApiClient.convertToType(data['RunnerOnThird'], 'Boolean');
            }
            if (data.hasOwnProperty('SavingPitcher')) {
                obj['SavingPitcher'] = ApiClient.convertToType(data['SavingPitcher'], 'String');
            }
            if (data.hasOwnProperty('SavingPitcherID')) {
                obj['SavingPitcherID'] = ApiClient.convertToType(data['SavingPitcherID'], 'Number');
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
            if (data.hasOwnProperty('Strikes')) {
                obj['Strikes'] = ApiClient.convertToType(data['Strikes'], 'Number');
            }
            if (data.hasOwnProperty('UnderPayout')) {
                obj['UnderPayout'] = ApiClient.convertToType(data['UnderPayout'], 'Number');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
            if (data.hasOwnProperty('WinningPitcher')) {
                obj['WinningPitcher'] = ApiClient.convertToType(data['WinningPitcher'], 'String');
            }
            if (data.hasOwnProperty('WinningPitcherID')) {
                obj['WinningPitcherID'] = ApiClient.convertToType(data['WinningPitcherID'], 'Number');
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
        if (data['AwayTeamStartingPitcher'] && !(typeof data['AwayTeamStartingPitcher'] === 'string' || data['AwayTeamStartingPitcher'] instanceof String)) {
            throw new Error("Expected the field `AwayTeamStartingPitcher` to be a primitive type in the JSON string but got " + data['AwayTeamStartingPitcher']);
        }
        // ensure the json data is a string
        if (data['Channel'] && !(typeof data['Channel'] === 'string' || data['Channel'] instanceof String)) {
            throw new Error("Expected the field `Channel` to be a primitive type in the JSON string but got " + data['Channel']);
        }
        // ensure the json data is a string
        if (data['CurrentHitter'] && !(typeof data['CurrentHitter'] === 'string' || data['CurrentHitter'] instanceof String)) {
            throw new Error("Expected the field `CurrentHitter` to be a primitive type in the JSON string but got " + data['CurrentHitter']);
        }
        // ensure the json data is a string
        if (data['CurrentPitcher'] && !(typeof data['CurrentPitcher'] === 'string' || data['CurrentPitcher'] instanceof String)) {
            throw new Error("Expected the field `CurrentPitcher` to be a primitive type in the JSON string but got " + data['CurrentPitcher']);
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
        if (data['ForecastDescription'] && !(typeof data['ForecastDescription'] === 'string' || data['ForecastDescription'] instanceof String)) {
            throw new Error("Expected the field `ForecastDescription` to be a primitive type in the JSON string but got " + data['ForecastDescription']);
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
        if (data['HomeTeamStartingPitcher'] && !(typeof data['HomeTeamStartingPitcher'] === 'string' || data['HomeTeamStartingPitcher'] instanceof String)) {
            throw new Error("Expected the field `HomeTeamStartingPitcher` to be a primitive type in the JSON string but got " + data['HomeTeamStartingPitcher']);
        }
        // ensure the json data is a string
        if (data['InningDescription'] && !(typeof data['InningDescription'] === 'string' || data['InningDescription'] instanceof String)) {
            throw new Error("Expected the field `InningDescription` to be a primitive type in the JSON string but got " + data['InningDescription']);
        }
        // ensure the json data is a string
        if (data['InningHalf'] && !(typeof data['InningHalf'] === 'string' || data['InningHalf'] instanceof String)) {
            throw new Error("Expected the field `InningHalf` to be a primitive type in the JSON string but got " + data['InningHalf']);
        }
        if (data['Innings']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Innings'])) {
                throw new Error("Expected the field `Innings` to be an array in the JSON data but got " + data['Innings']);
            }
            // validate the optional field `Innings` (array)
            for (const item of data['Innings']) {
                Inning.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['LastPlay'] && !(typeof data['LastPlay'] === 'string' || data['LastPlay'] instanceof String)) {
            throw new Error("Expected the field `LastPlay` to be a primitive type in the JSON string but got " + data['LastPlay']);
        }
        // ensure the json data is a string
        if (data['LosingPitcher'] && !(typeof data['LosingPitcher'] === 'string' || data['LosingPitcher'] instanceof String)) {
            throw new Error("Expected the field `LosingPitcher` to be a primitive type in the JSON string but got " + data['LosingPitcher']);
        }
        // ensure the json data is a string
        if (data['SavingPitcher'] && !(typeof data['SavingPitcher'] === 'string' || data['SavingPitcher'] instanceof String)) {
            throw new Error("Expected the field `SavingPitcher` to be a primitive type in the JSON string but got " + data['SavingPitcher']);
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
        // ensure the json data is a string
        if (data['WinningPitcher'] && !(typeof data['WinningPitcher'] === 'string' || data['WinningPitcher'] instanceof String)) {
            throw new Error("Expected the field `WinningPitcher` to be a primitive type in the JSON string but got " + data['WinningPitcher']);
        }

        return true;
    }


}



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
 * @member {Number} AwayTeamErrors
 */
Game.prototype['AwayTeamErrors'] = undefined;

/**
 * @member {Number} AwayTeamHits
 */
Game.prototype['AwayTeamHits'] = undefined;

/**
 * @member {Number} AwayTeamID
 */
Game.prototype['AwayTeamID'] = undefined;

/**
 * @member {Number} AwayTeamMoneyLine
 */
Game.prototype['AwayTeamMoneyLine'] = undefined;

/**
 * @member {Number} AwayTeamProbablePitcherID
 */
Game.prototype['AwayTeamProbablePitcherID'] = undefined;

/**
 * @member {Number} AwayTeamRuns
 */
Game.prototype['AwayTeamRuns'] = undefined;

/**
 * @member {String} AwayTeamStartingPitcher
 */
Game.prototype['AwayTeamStartingPitcher'] = undefined;

/**
 * @member {Number} AwayTeamStartingPitcherID
 */
Game.prototype['AwayTeamStartingPitcherID'] = undefined;

/**
 * @member {Number} Balls
 */
Game.prototype['Balls'] = undefined;

/**
 * @member {String} Channel
 */
Game.prototype['Channel'] = undefined;

/**
 * @member {String} CurrentHitter
 */
Game.prototype['CurrentHitter'] = undefined;

/**
 * @member {Number} CurrentHitterID
 */
Game.prototype['CurrentHitterID'] = undefined;

/**
 * @member {Number} CurrentHittingTeamID
 */
Game.prototype['CurrentHittingTeamID'] = undefined;

/**
 * @member {String} CurrentPitcher
 */
Game.prototype['CurrentPitcher'] = undefined;

/**
 * @member {Number} CurrentPitcherID
 */
Game.prototype['CurrentPitcherID'] = undefined;

/**
 * @member {Number} CurrentPitchingTeamID
 */
Game.prototype['CurrentPitchingTeamID'] = undefined;

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
 * @member {Number} DueUpHitterID1
 */
Game.prototype['DueUpHitterID1'] = undefined;

/**
 * @member {Number} DueUpHitterID2
 */
Game.prototype['DueUpHitterID2'] = undefined;

/**
 * @member {Number} DueUpHitterID3
 */
Game.prototype['DueUpHitterID3'] = undefined;

/**
 * @member {String} ForecastDescription
 */
Game.prototype['ForecastDescription'] = undefined;

/**
 * @member {Number} ForecastTempHigh
 */
Game.prototype['ForecastTempHigh'] = undefined;

/**
 * @member {Number} ForecastTempLow
 */
Game.prototype['ForecastTempLow'] = undefined;

/**
 * @member {Number} ForecastWindChill
 */
Game.prototype['ForecastWindChill'] = undefined;

/**
 * @member {Number} ForecastWindDirection
 */
Game.prototype['ForecastWindDirection'] = undefined;

/**
 * @member {Number} ForecastWindSpeed
 */
Game.prototype['ForecastWindSpeed'] = undefined;

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
 * @member {Number} HomeTeamErrors
 */
Game.prototype['HomeTeamErrors'] = undefined;

/**
 * @member {Number} HomeTeamHits
 */
Game.prototype['HomeTeamHits'] = undefined;

/**
 * @member {Number} HomeTeamID
 */
Game.prototype['HomeTeamID'] = undefined;

/**
 * @member {Number} HomeTeamMoneyLine
 */
Game.prototype['HomeTeamMoneyLine'] = undefined;

/**
 * @member {Number} HomeTeamProbablePitcherID
 */
Game.prototype['HomeTeamProbablePitcherID'] = undefined;

/**
 * @member {Number} HomeTeamRuns
 */
Game.prototype['HomeTeamRuns'] = undefined;

/**
 * @member {String} HomeTeamStartingPitcher
 */
Game.prototype['HomeTeamStartingPitcher'] = undefined;

/**
 * @member {Number} HomeTeamStartingPitcherID
 */
Game.prototype['HomeTeamStartingPitcherID'] = undefined;

/**
 * @member {Number} Inning
 */
Game.prototype['Inning'] = undefined;

/**
 * @member {String} InningDescription
 */
Game.prototype['InningDescription'] = undefined;

/**
 * @member {String} InningHalf
 */
Game.prototype['InningHalf'] = undefined;

/**
 * @member {Array.<module:model/Inning>} Innings
 */
Game.prototype['Innings'] = undefined;

/**
 * @member {Boolean} IsClosed
 */
Game.prototype['IsClosed'] = undefined;

/**
 * @member {String} LastPlay
 */
Game.prototype['LastPlay'] = undefined;

/**
 * @member {String} LosingPitcher
 */
Game.prototype['LosingPitcher'] = undefined;

/**
 * @member {Number} LosingPitcherID
 */
Game.prototype['LosingPitcherID'] = undefined;

/**
 * @member {Boolean} NeutralVenue
 */
Game.prototype['NeutralVenue'] = undefined;

/**
 * @member {Number} Outs
 */
Game.prototype['Outs'] = undefined;

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
 * @member {Number} RescheduledFromGameID
 */
Game.prototype['RescheduledFromGameID'] = undefined;

/**
 * @member {Number} RescheduledGameID
 */
Game.prototype['RescheduledGameID'] = undefined;

/**
 * @member {Boolean} RunnerOnFirst
 */
Game.prototype['RunnerOnFirst'] = undefined;

/**
 * @member {Boolean} RunnerOnSecond
 */
Game.prototype['RunnerOnSecond'] = undefined;

/**
 * @member {Boolean} RunnerOnThird
 */
Game.prototype['RunnerOnThird'] = undefined;

/**
 * @member {String} SavingPitcher
 */
Game.prototype['SavingPitcher'] = undefined;

/**
 * @member {Number} SavingPitcherID
 */
Game.prototype['SavingPitcherID'] = undefined;

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
 * @member {Number} Strikes
 */
Game.prototype['Strikes'] = undefined;

/**
 * @member {Number} UnderPayout
 */
Game.prototype['UnderPayout'] = undefined;

/**
 * @member {String} Updated
 */
Game.prototype['Updated'] = undefined;

/**
 * @member {String} WinningPitcher
 */
Game.prototype['WinningPitcher'] = undefined;

/**
 * @member {Number} WinningPitcherID
 */
Game.prototype['WinningPitcherID'] = undefined;






export default Game;

