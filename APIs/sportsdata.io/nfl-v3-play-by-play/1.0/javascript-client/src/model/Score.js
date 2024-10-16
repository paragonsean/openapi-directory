/**
 * NFL v3 Play-by-Play
 * NFL play-by-play API.
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
import Stadium from './Stadium';

/**
 * The Score model module.
 * @module model/Score
 * @version 1.0
 */
class Score {
    /**
     * Constructs a new <code>Score</code>.
     * @alias module:model/Score
     */
    constructor() { 
        
        Score.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Score</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Score} obj Optional instance to populate.
     * @return {module:model/Score} The populated <code>Score</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Score();

            if (data.hasOwnProperty('Attendance')) {
                obj['Attendance'] = ApiClient.convertToType(data['Attendance'], 'Number');
            }
            if (data.hasOwnProperty('AwayRotationNumber')) {
                obj['AwayRotationNumber'] = ApiClient.convertToType(data['AwayRotationNumber'], 'Number');
            }
            if (data.hasOwnProperty('AwayScore')) {
                obj['AwayScore'] = ApiClient.convertToType(data['AwayScore'], 'Number');
            }
            if (data.hasOwnProperty('AwayScoreOvertime')) {
                obj['AwayScoreOvertime'] = ApiClient.convertToType(data['AwayScoreOvertime'], 'Number');
            }
            if (data.hasOwnProperty('AwayScoreQuarter1')) {
                obj['AwayScoreQuarter1'] = ApiClient.convertToType(data['AwayScoreQuarter1'], 'Number');
            }
            if (data.hasOwnProperty('AwayScoreQuarter2')) {
                obj['AwayScoreQuarter2'] = ApiClient.convertToType(data['AwayScoreQuarter2'], 'Number');
            }
            if (data.hasOwnProperty('AwayScoreQuarter3')) {
                obj['AwayScoreQuarter3'] = ApiClient.convertToType(data['AwayScoreQuarter3'], 'Number');
            }
            if (data.hasOwnProperty('AwayScoreQuarter4')) {
                obj['AwayScoreQuarter4'] = ApiClient.convertToType(data['AwayScoreQuarter4'], 'Number');
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
            if (data.hasOwnProperty('AwayTimeouts')) {
                obj['AwayTimeouts'] = ApiClient.convertToType(data['AwayTimeouts'], 'Number');
            }
            if (data.hasOwnProperty('Canceled')) {
                obj['Canceled'] = ApiClient.convertToType(data['Canceled'], 'Boolean');
            }
            if (data.hasOwnProperty('Channel')) {
                obj['Channel'] = ApiClient.convertToType(data['Channel'], 'String');
            }
            if (data.hasOwnProperty('Closed')) {
                obj['Closed'] = ApiClient.convertToType(data['Closed'], 'Boolean');
            }
            if (data.hasOwnProperty('Date')) {
                obj['Date'] = ApiClient.convertToType(data['Date'], 'String');
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
                obj['Distance'] = ApiClient.convertToType(data['Distance'], 'String');
            }
            if (data.hasOwnProperty('Down')) {
                obj['Down'] = ApiClient.convertToType(data['Down'], 'Number');
            }
            if (data.hasOwnProperty('DownAndDistance')) {
                obj['DownAndDistance'] = ApiClient.convertToType(data['DownAndDistance'], 'String');
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
            if (data.hasOwnProperty('ForecastWindSpeed')) {
                obj['ForecastWindSpeed'] = ApiClient.convertToType(data['ForecastWindSpeed'], 'Number');
            }
            if (data.hasOwnProperty('GameEndDateTime')) {
                obj['GameEndDateTime'] = ApiClient.convertToType(data['GameEndDateTime'], 'String');
            }
            if (data.hasOwnProperty('GameKey')) {
                obj['GameKey'] = ApiClient.convertToType(data['GameKey'], 'String');
            }
            if (data.hasOwnProperty('GeoLat')) {
                obj['GeoLat'] = ApiClient.convertToType(data['GeoLat'], 'Number');
            }
            if (data.hasOwnProperty('GeoLong')) {
                obj['GeoLong'] = ApiClient.convertToType(data['GeoLong'], 'Number');
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
            if (data.hasOwnProperty('Has1stQuarterStarted')) {
                obj['Has1stQuarterStarted'] = ApiClient.convertToType(data['Has1stQuarterStarted'], 'Boolean');
            }
            if (data.hasOwnProperty('Has2ndQuarterStarted')) {
                obj['Has2ndQuarterStarted'] = ApiClient.convertToType(data['Has2ndQuarterStarted'], 'Boolean');
            }
            if (data.hasOwnProperty('Has3rdQuarterStarted')) {
                obj['Has3rdQuarterStarted'] = ApiClient.convertToType(data['Has3rdQuarterStarted'], 'Boolean');
            }
            if (data.hasOwnProperty('Has4thQuarterStarted')) {
                obj['Has4thQuarterStarted'] = ApiClient.convertToType(data['Has4thQuarterStarted'], 'Boolean');
            }
            if (data.hasOwnProperty('HasStarted')) {
                obj['HasStarted'] = ApiClient.convertToType(data['HasStarted'], 'Boolean');
            }
            if (data.hasOwnProperty('HomeRotationNumber')) {
                obj['HomeRotationNumber'] = ApiClient.convertToType(data['HomeRotationNumber'], 'Number');
            }
            if (data.hasOwnProperty('HomeScore')) {
                obj['HomeScore'] = ApiClient.convertToType(data['HomeScore'], 'Number');
            }
            if (data.hasOwnProperty('HomeScoreOvertime')) {
                obj['HomeScoreOvertime'] = ApiClient.convertToType(data['HomeScoreOvertime'], 'Number');
            }
            if (data.hasOwnProperty('HomeScoreQuarter1')) {
                obj['HomeScoreQuarter1'] = ApiClient.convertToType(data['HomeScoreQuarter1'], 'Number');
            }
            if (data.hasOwnProperty('HomeScoreQuarter2')) {
                obj['HomeScoreQuarter2'] = ApiClient.convertToType(data['HomeScoreQuarter2'], 'Number');
            }
            if (data.hasOwnProperty('HomeScoreQuarter3')) {
                obj['HomeScoreQuarter3'] = ApiClient.convertToType(data['HomeScoreQuarter3'], 'Number');
            }
            if (data.hasOwnProperty('HomeScoreQuarter4')) {
                obj['HomeScoreQuarter4'] = ApiClient.convertToType(data['HomeScoreQuarter4'], 'Number');
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
            if (data.hasOwnProperty('HomeTimeouts')) {
                obj['HomeTimeouts'] = ApiClient.convertToType(data['HomeTimeouts'], 'Number');
            }
            if (data.hasOwnProperty('IsInProgress')) {
                obj['IsInProgress'] = ApiClient.convertToType(data['IsInProgress'], 'Boolean');
            }
            if (data.hasOwnProperty('IsOver')) {
                obj['IsOver'] = ApiClient.convertToType(data['IsOver'], 'Boolean');
            }
            if (data.hasOwnProperty('IsOvertime')) {
                obj['IsOvertime'] = ApiClient.convertToType(data['IsOvertime'], 'Boolean');
            }
            if (data.hasOwnProperty('LastPlay')) {
                obj['LastPlay'] = ApiClient.convertToType(data['LastPlay'], 'String');
            }
            if (data.hasOwnProperty('LastUpdated')) {
                obj['LastUpdated'] = ApiClient.convertToType(data['LastUpdated'], 'String');
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
            if (data.hasOwnProperty('Possession')) {
                obj['Possession'] = ApiClient.convertToType(data['Possession'], 'String');
            }
            if (data.hasOwnProperty('Quarter')) {
                obj['Quarter'] = ApiClient.convertToType(data['Quarter'], 'String');
            }
            if (data.hasOwnProperty('QuarterDescription')) {
                obj['QuarterDescription'] = ApiClient.convertToType(data['QuarterDescription'], 'String');
            }
            if (data.hasOwnProperty('RedZone')) {
                obj['RedZone'] = ApiClient.convertToType(data['RedZone'], 'String');
            }
            if (data.hasOwnProperty('RefereeID')) {
                obj['RefereeID'] = ApiClient.convertToType(data['RefereeID'], 'Number');
            }
            if (data.hasOwnProperty('ScoreID')) {
                obj['ScoreID'] = ApiClient.convertToType(data['ScoreID'], 'Number');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('SeasonType')) {
                obj['SeasonType'] = ApiClient.convertToType(data['SeasonType'], 'Number');
            }
            if (data.hasOwnProperty('StadiumDetails')) {
                obj['StadiumDetails'] = Stadium.constructFromObject(data['StadiumDetails']);
            }
            if (data.hasOwnProperty('StadiumID')) {
                obj['StadiumID'] = ApiClient.convertToType(data['StadiumID'], 'Number');
            }
            if (data.hasOwnProperty('Status')) {
                obj['Status'] = ApiClient.convertToType(data['Status'], 'String');
            }
            if (data.hasOwnProperty('TimeRemaining')) {
                obj['TimeRemaining'] = ApiClient.convertToType(data['TimeRemaining'], 'String');
            }
            if (data.hasOwnProperty('UnderPayout')) {
                obj['UnderPayout'] = ApiClient.convertToType(data['UnderPayout'], 'Number');
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
     * Validates the JSON data with respect to <code>Score</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Score</code>.
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
        if (data['Date'] && !(typeof data['Date'] === 'string' || data['Date'] instanceof String)) {
            throw new Error("Expected the field `Date` to be a primitive type in the JSON string but got " + data['Date']);
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
        if (data['Distance'] && !(typeof data['Distance'] === 'string' || data['Distance'] instanceof String)) {
            throw new Error("Expected the field `Distance` to be a primitive type in the JSON string but got " + data['Distance']);
        }
        // ensure the json data is a string
        if (data['DownAndDistance'] && !(typeof data['DownAndDistance'] === 'string' || data['DownAndDistance'] instanceof String)) {
            throw new Error("Expected the field `DownAndDistance` to be a primitive type in the JSON string but got " + data['DownAndDistance']);
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
        if (data['GameKey'] && !(typeof data['GameKey'] === 'string' || data['GameKey'] instanceof String)) {
            throw new Error("Expected the field `GameKey` to be a primitive type in the JSON string but got " + data['GameKey']);
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
        if (data['LastUpdated'] && !(typeof data['LastUpdated'] === 'string' || data['LastUpdated'] instanceof String)) {
            throw new Error("Expected the field `LastUpdated` to be a primitive type in the JSON string but got " + data['LastUpdated']);
        }
        // ensure the json data is a string
        if (data['Possession'] && !(typeof data['Possession'] === 'string' || data['Possession'] instanceof String)) {
            throw new Error("Expected the field `Possession` to be a primitive type in the JSON string but got " + data['Possession']);
        }
        // ensure the json data is a string
        if (data['Quarter'] && !(typeof data['Quarter'] === 'string' || data['Quarter'] instanceof String)) {
            throw new Error("Expected the field `Quarter` to be a primitive type in the JSON string but got " + data['Quarter']);
        }
        // ensure the json data is a string
        if (data['QuarterDescription'] && !(typeof data['QuarterDescription'] === 'string' || data['QuarterDescription'] instanceof String)) {
            throw new Error("Expected the field `QuarterDescription` to be a primitive type in the JSON string but got " + data['QuarterDescription']);
        }
        // ensure the json data is a string
        if (data['RedZone'] && !(typeof data['RedZone'] === 'string' || data['RedZone'] instanceof String)) {
            throw new Error("Expected the field `RedZone` to be a primitive type in the JSON string but got " + data['RedZone']);
        }
        // validate the optional field `StadiumDetails`
        if (data['StadiumDetails']) { // data not null
          Stadium.validateJSON(data['StadiumDetails']);
        }
        // ensure the json data is a string
        if (data['Status'] && !(typeof data['Status'] === 'string' || data['Status'] instanceof String)) {
            throw new Error("Expected the field `Status` to be a primitive type in the JSON string but got " + data['Status']);
        }
        // ensure the json data is a string
        if (data['TimeRemaining'] && !(typeof data['TimeRemaining'] === 'string' || data['TimeRemaining'] instanceof String)) {
            throw new Error("Expected the field `TimeRemaining` to be a primitive type in the JSON string but got " + data['TimeRemaining']);
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
Score.prototype['Attendance'] = undefined;

/**
 * @member {Number} AwayRotationNumber
 */
Score.prototype['AwayRotationNumber'] = undefined;

/**
 * @member {Number} AwayScore
 */
Score.prototype['AwayScore'] = undefined;

/**
 * @member {Number} AwayScoreOvertime
 */
Score.prototype['AwayScoreOvertime'] = undefined;

/**
 * @member {Number} AwayScoreQuarter1
 */
Score.prototype['AwayScoreQuarter1'] = undefined;

/**
 * @member {Number} AwayScoreQuarter2
 */
Score.prototype['AwayScoreQuarter2'] = undefined;

/**
 * @member {Number} AwayScoreQuarter3
 */
Score.prototype['AwayScoreQuarter3'] = undefined;

/**
 * @member {Number} AwayScoreQuarter4
 */
Score.prototype['AwayScoreQuarter4'] = undefined;

/**
 * @member {String} AwayTeam
 */
Score.prototype['AwayTeam'] = undefined;

/**
 * @member {Number} AwayTeamID
 */
Score.prototype['AwayTeamID'] = undefined;

/**
 * @member {Number} AwayTeamMoneyLine
 */
Score.prototype['AwayTeamMoneyLine'] = undefined;

/**
 * @member {Number} AwayTimeouts
 */
Score.prototype['AwayTimeouts'] = undefined;

/**
 * @member {Boolean} Canceled
 */
Score.prototype['Canceled'] = undefined;

/**
 * @member {String} Channel
 */
Score.prototype['Channel'] = undefined;

/**
 * @member {Boolean} Closed
 */
Score.prototype['Closed'] = undefined;

/**
 * @member {String} Date
 */
Score.prototype['Date'] = undefined;

/**
 * @member {String} DateTime
 */
Score.prototype['DateTime'] = undefined;

/**
 * @member {String} DateTimeUTC
 */
Score.prototype['DateTimeUTC'] = undefined;

/**
 * @member {String} Day
 */
Score.prototype['Day'] = undefined;

/**
 * @member {String} Distance
 */
Score.prototype['Distance'] = undefined;

/**
 * @member {Number} Down
 */
Score.prototype['Down'] = undefined;

/**
 * @member {String} DownAndDistance
 */
Score.prototype['DownAndDistance'] = undefined;

/**
 * @member {String} ForecastDescription
 */
Score.prototype['ForecastDescription'] = undefined;

/**
 * @member {Number} ForecastTempHigh
 */
Score.prototype['ForecastTempHigh'] = undefined;

/**
 * @member {Number} ForecastTempLow
 */
Score.prototype['ForecastTempLow'] = undefined;

/**
 * @member {Number} ForecastWindChill
 */
Score.prototype['ForecastWindChill'] = undefined;

/**
 * @member {Number} ForecastWindSpeed
 */
Score.prototype['ForecastWindSpeed'] = undefined;

/**
 * @member {String} GameEndDateTime
 */
Score.prototype['GameEndDateTime'] = undefined;

/**
 * @member {String} GameKey
 */
Score.prototype['GameKey'] = undefined;

/**
 * @member {Number} GeoLat
 */
Score.prototype['GeoLat'] = undefined;

/**
 * @member {Number} GeoLong
 */
Score.prototype['GeoLong'] = undefined;

/**
 * @member {Number} GlobalAwayTeamID
 */
Score.prototype['GlobalAwayTeamID'] = undefined;

/**
 * @member {Number} GlobalGameID
 */
Score.prototype['GlobalGameID'] = undefined;

/**
 * @member {Number} GlobalHomeTeamID
 */
Score.prototype['GlobalHomeTeamID'] = undefined;

/**
 * @member {Boolean} Has1stQuarterStarted
 */
Score.prototype['Has1stQuarterStarted'] = undefined;

/**
 * @member {Boolean} Has2ndQuarterStarted
 */
Score.prototype['Has2ndQuarterStarted'] = undefined;

/**
 * @member {Boolean} Has3rdQuarterStarted
 */
Score.prototype['Has3rdQuarterStarted'] = undefined;

/**
 * @member {Boolean} Has4thQuarterStarted
 */
Score.prototype['Has4thQuarterStarted'] = undefined;

/**
 * @member {Boolean} HasStarted
 */
Score.prototype['HasStarted'] = undefined;

/**
 * @member {Number} HomeRotationNumber
 */
Score.prototype['HomeRotationNumber'] = undefined;

/**
 * @member {Number} HomeScore
 */
Score.prototype['HomeScore'] = undefined;

/**
 * @member {Number} HomeScoreOvertime
 */
Score.prototype['HomeScoreOvertime'] = undefined;

/**
 * @member {Number} HomeScoreQuarter1
 */
Score.prototype['HomeScoreQuarter1'] = undefined;

/**
 * @member {Number} HomeScoreQuarter2
 */
Score.prototype['HomeScoreQuarter2'] = undefined;

/**
 * @member {Number} HomeScoreQuarter3
 */
Score.prototype['HomeScoreQuarter3'] = undefined;

/**
 * @member {Number} HomeScoreQuarter4
 */
Score.prototype['HomeScoreQuarter4'] = undefined;

/**
 * @member {String} HomeTeam
 */
Score.prototype['HomeTeam'] = undefined;

/**
 * @member {Number} HomeTeamID
 */
Score.prototype['HomeTeamID'] = undefined;

/**
 * @member {Number} HomeTeamMoneyLine
 */
Score.prototype['HomeTeamMoneyLine'] = undefined;

/**
 * @member {Number} HomeTimeouts
 */
Score.prototype['HomeTimeouts'] = undefined;

/**
 * @member {Boolean} IsInProgress
 */
Score.prototype['IsInProgress'] = undefined;

/**
 * @member {Boolean} IsOver
 */
Score.prototype['IsOver'] = undefined;

/**
 * @member {Boolean} IsOvertime
 */
Score.prototype['IsOvertime'] = undefined;

/**
 * @member {String} LastPlay
 */
Score.prototype['LastPlay'] = undefined;

/**
 * @member {String} LastUpdated
 */
Score.prototype['LastUpdated'] = undefined;

/**
 * @member {Boolean} NeutralVenue
 */
Score.prototype['NeutralVenue'] = undefined;

/**
 * @member {Number} OverPayout
 */
Score.prototype['OverPayout'] = undefined;

/**
 * @member {Number} OverUnder
 */
Score.prototype['OverUnder'] = undefined;

/**
 * @member {Number} PointSpread
 */
Score.prototype['PointSpread'] = undefined;

/**
 * @member {Number} PointSpreadAwayTeamMoneyLine
 */
Score.prototype['PointSpreadAwayTeamMoneyLine'] = undefined;

/**
 * @member {Number} PointSpreadHomeTeamMoneyLine
 */
Score.prototype['PointSpreadHomeTeamMoneyLine'] = undefined;

/**
 * @member {String} Possession
 */
Score.prototype['Possession'] = undefined;

/**
 * @member {String} Quarter
 */
Score.prototype['Quarter'] = undefined;

/**
 * @member {String} QuarterDescription
 */
Score.prototype['QuarterDescription'] = undefined;

/**
 * @member {String} RedZone
 */
Score.prototype['RedZone'] = undefined;

/**
 * @member {Number} RefereeID
 */
Score.prototype['RefereeID'] = undefined;

/**
 * @member {Number} ScoreID
 */
Score.prototype['ScoreID'] = undefined;

/**
 * @member {Number} Season
 */
Score.prototype['Season'] = undefined;

/**
 * @member {Number} SeasonType
 */
Score.prototype['SeasonType'] = undefined;

/**
 * @member {module:model/Stadium} StadiumDetails
 */
Score.prototype['StadiumDetails'] = undefined;

/**
 * @member {Number} StadiumID
 */
Score.prototype['StadiumID'] = undefined;

/**
 * @member {String} Status
 */
Score.prototype['Status'] = undefined;

/**
 * @member {String} TimeRemaining
 */
Score.prototype['TimeRemaining'] = undefined;

/**
 * @member {Number} UnderPayout
 */
Score.prototype['UnderPayout'] = undefined;

/**
 * @member {Number} Week
 */
Score.prototype['Week'] = undefined;

/**
 * @member {Number} YardLine
 */
Score.prototype['YardLine'] = undefined;

/**
 * @member {String} YardLineTerritory
 */
Score.prototype['YardLineTerritory'] = undefined;






export default Score;

