/**
 * NBA v3 Scores
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
import Series from './Series';

/**
 * The ScoreBasic model module.
 * @module model/ScoreBasic
 * @version 1.0
 */
class ScoreBasic {
    /**
     * Constructs a new <code>ScoreBasic</code>.
     * @alias module:model/ScoreBasic
     */
    constructor() { 
        
        ScoreBasic.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ScoreBasic</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ScoreBasic} obj Optional instance to populate.
     * @return {module:model/ScoreBasic} The populated <code>ScoreBasic</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ScoreBasic();

            if (data.hasOwnProperty('AwayTeam')) {
                obj['AwayTeam'] = ApiClient.convertToType(data['AwayTeam'], 'String');
            }
            if (data.hasOwnProperty('AwayTeamID')) {
                obj['AwayTeamID'] = ApiClient.convertToType(data['AwayTeamID'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeamScore')) {
                obj['AwayTeamScore'] = ApiClient.convertToType(data['AwayTeamScore'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeamScore2')) {
                obj['AwayTeamScore2'] = ApiClient.convertToType(data['AwayTeamScore2'], 'Number');
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
            if (data.hasOwnProperty('HomeTeam')) {
                obj['HomeTeam'] = ApiClient.convertToType(data['HomeTeam'], 'String');
            }
            if (data.hasOwnProperty('HomeTeamID')) {
                obj['HomeTeamID'] = ApiClient.convertToType(data['HomeTeamID'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamScore')) {
                obj['HomeTeamScore'] = ApiClient.convertToType(data['HomeTeamScore'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeamScore2')) {
                obj['HomeTeamScore2'] = ApiClient.convertToType(data['HomeTeamScore2'], 'Number');
            }
            if (data.hasOwnProperty('IsClosed')) {
                obj['IsClosed'] = ApiClient.convertToType(data['IsClosed'], 'Boolean');
            }
            if (data.hasOwnProperty('NeutralVenue')) {
                obj['NeutralVenue'] = ApiClient.convertToType(data['NeutralVenue'], 'Boolean');
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
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ScoreBasic</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ScoreBasic</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AwayTeam'] && !(typeof data['AwayTeam'] === 'string' || data['AwayTeam'] instanceof String)) {
            throw new Error("Expected the field `AwayTeam` to be a primitive type in the JSON string but got " + data['AwayTeam']);
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
 * @member {String} AwayTeam
 */
ScoreBasic.prototype['AwayTeam'] = undefined;

/**
 * @member {Number} AwayTeamID
 */
ScoreBasic.prototype['AwayTeamID'] = undefined;

/**
 * @member {Number} AwayTeamScore
 */
ScoreBasic.prototype['AwayTeamScore'] = undefined;

/**
 * @member {Number} AwayTeamScore2
 */
ScoreBasic.prototype['AwayTeamScore2'] = undefined;

/**
 * @member {String} DateTime
 */
ScoreBasic.prototype['DateTime'] = undefined;

/**
 * @member {String} DateTimeUTC
 */
ScoreBasic.prototype['DateTimeUTC'] = undefined;

/**
 * @member {String} Day
 */
ScoreBasic.prototype['Day'] = undefined;

/**
 * @member {String} GameEndDateTime
 */
ScoreBasic.prototype['GameEndDateTime'] = undefined;

/**
 * @member {Number} GameID
 */
ScoreBasic.prototype['GameID'] = undefined;

/**
 * @member {Number} GlobalAwayTeamID
 */
ScoreBasic.prototype['GlobalAwayTeamID'] = undefined;

/**
 * @member {Number} GlobalGameID
 */
ScoreBasic.prototype['GlobalGameID'] = undefined;

/**
 * @member {Number} GlobalHomeTeamID
 */
ScoreBasic.prototype['GlobalHomeTeamID'] = undefined;

/**
 * @member {String} HomeTeam
 */
ScoreBasic.prototype['HomeTeam'] = undefined;

/**
 * @member {Number} HomeTeamID
 */
ScoreBasic.prototype['HomeTeamID'] = undefined;

/**
 * @member {Number} HomeTeamScore
 */
ScoreBasic.prototype['HomeTeamScore'] = undefined;

/**
 * @member {Number} HomeTeamScore2
 */
ScoreBasic.prototype['HomeTeamScore2'] = undefined;

/**
 * @member {Boolean} IsClosed
 */
ScoreBasic.prototype['IsClosed'] = undefined;

/**
 * @member {Boolean} NeutralVenue
 */
ScoreBasic.prototype['NeutralVenue'] = undefined;

/**
 * @member {Number} Season
 */
ScoreBasic.prototype['Season'] = undefined;

/**
 * @member {Number} SeasonType
 */
ScoreBasic.prototype['SeasonType'] = undefined;

/**
 * @member {module:model/Series} SeriesInfo
 */
ScoreBasic.prototype['SeriesInfo'] = undefined;

/**
 * @member {Number} StadiumID
 */
ScoreBasic.prototype['StadiumID'] = undefined;

/**
 * @member {String} Status
 */
ScoreBasic.prototype['Status'] = undefined;

/**
 * @member {String} Updated
 */
ScoreBasic.prototype['Updated'] = undefined;






export default ScoreBasic;

