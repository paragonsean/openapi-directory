/**
 * NFL v3 Stats
 * NFL rosters, player stats, team stats, and fantasy stats API.
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

/**
 * The ScoringPlay model module.
 * @module model/ScoringPlay
 * @version 1.0
 */
class ScoringPlay {
    /**
     * Constructs a new <code>ScoringPlay</code>.
     * @alias module:model/ScoringPlay
     */
    constructor() { 
        
        ScoringPlay.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ScoringPlay</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ScoringPlay} obj Optional instance to populate.
     * @return {module:model/ScoringPlay} The populated <code>ScoringPlay</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ScoringPlay();

            if (data.hasOwnProperty('AwayScore')) {
                obj['AwayScore'] = ApiClient.convertToType(data['AwayScore'], 'Number');
            }
            if (data.hasOwnProperty('AwayTeam')) {
                obj['AwayTeam'] = ApiClient.convertToType(data['AwayTeam'], 'String');
            }
            if (data.hasOwnProperty('Date')) {
                obj['Date'] = ApiClient.convertToType(data['Date'], 'String');
            }
            if (data.hasOwnProperty('GameKey')) {
                obj['GameKey'] = ApiClient.convertToType(data['GameKey'], 'String');
            }
            if (data.hasOwnProperty('HomeScore')) {
                obj['HomeScore'] = ApiClient.convertToType(data['HomeScore'], 'Number');
            }
            if (data.hasOwnProperty('HomeTeam')) {
                obj['HomeTeam'] = ApiClient.convertToType(data['HomeTeam'], 'String');
            }
            if (data.hasOwnProperty('PlayDescription')) {
                obj['PlayDescription'] = ApiClient.convertToType(data['PlayDescription'], 'String');
            }
            if (data.hasOwnProperty('Quarter')) {
                obj['Quarter'] = ApiClient.convertToType(data['Quarter'], 'String');
            }
            if (data.hasOwnProperty('ScoreID')) {
                obj['ScoreID'] = ApiClient.convertToType(data['ScoreID'], 'Number');
            }
            if (data.hasOwnProperty('ScoringPlayID')) {
                obj['ScoringPlayID'] = ApiClient.convertToType(data['ScoringPlayID'], 'Number');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('SeasonType')) {
                obj['SeasonType'] = ApiClient.convertToType(data['SeasonType'], 'Number');
            }
            if (data.hasOwnProperty('Sequence')) {
                obj['Sequence'] = ApiClient.convertToType(data['Sequence'], 'Number');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('TimeRemaining')) {
                obj['TimeRemaining'] = ApiClient.convertToType(data['TimeRemaining'], 'String');
            }
            if (data.hasOwnProperty('Week')) {
                obj['Week'] = ApiClient.convertToType(data['Week'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ScoringPlay</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ScoringPlay</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AwayTeam'] && !(typeof data['AwayTeam'] === 'string' || data['AwayTeam'] instanceof String)) {
            throw new Error("Expected the field `AwayTeam` to be a primitive type in the JSON string but got " + data['AwayTeam']);
        }
        // ensure the json data is a string
        if (data['Date'] && !(typeof data['Date'] === 'string' || data['Date'] instanceof String)) {
            throw new Error("Expected the field `Date` to be a primitive type in the JSON string but got " + data['Date']);
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
        if (data['PlayDescription'] && !(typeof data['PlayDescription'] === 'string' || data['PlayDescription'] instanceof String)) {
            throw new Error("Expected the field `PlayDescription` to be a primitive type in the JSON string but got " + data['PlayDescription']);
        }
        // ensure the json data is a string
        if (data['Quarter'] && !(typeof data['Quarter'] === 'string' || data['Quarter'] instanceof String)) {
            throw new Error("Expected the field `Quarter` to be a primitive type in the JSON string but got " + data['Quarter']);
        }
        // ensure the json data is a string
        if (data['Team'] && !(typeof data['Team'] === 'string' || data['Team'] instanceof String)) {
            throw new Error("Expected the field `Team` to be a primitive type in the JSON string but got " + data['Team']);
        }
        // ensure the json data is a string
        if (data['TimeRemaining'] && !(typeof data['TimeRemaining'] === 'string' || data['TimeRemaining'] instanceof String)) {
            throw new Error("Expected the field `TimeRemaining` to be a primitive type in the JSON string but got " + data['TimeRemaining']);
        }

        return true;
    }


}



/**
 * @member {Number} AwayScore
 */
ScoringPlay.prototype['AwayScore'] = undefined;

/**
 * @member {String} AwayTeam
 */
ScoringPlay.prototype['AwayTeam'] = undefined;

/**
 * @member {String} Date
 */
ScoringPlay.prototype['Date'] = undefined;

/**
 * @member {String} GameKey
 */
ScoringPlay.prototype['GameKey'] = undefined;

/**
 * @member {Number} HomeScore
 */
ScoringPlay.prototype['HomeScore'] = undefined;

/**
 * @member {String} HomeTeam
 */
ScoringPlay.prototype['HomeTeam'] = undefined;

/**
 * @member {String} PlayDescription
 */
ScoringPlay.prototype['PlayDescription'] = undefined;

/**
 * @member {String} Quarter
 */
ScoringPlay.prototype['Quarter'] = undefined;

/**
 * @member {Number} ScoreID
 */
ScoringPlay.prototype['ScoreID'] = undefined;

/**
 * @member {Number} ScoringPlayID
 */
ScoringPlay.prototype['ScoringPlayID'] = undefined;

/**
 * @member {Number} Season
 */
ScoringPlay.prototype['Season'] = undefined;

/**
 * @member {Number} SeasonType
 */
ScoringPlay.prototype['SeasonType'] = undefined;

/**
 * @member {Number} Sequence
 */
ScoringPlay.prototype['Sequence'] = undefined;

/**
 * @member {String} Team
 */
ScoringPlay.prototype['Team'] = undefined;

/**
 * @member {String} TimeRemaining
 */
ScoringPlay.prototype['TimeRemaining'] = undefined;

/**
 * @member {Number} Week
 */
ScoringPlay.prototype['Week'] = undefined;






export default ScoringPlay;

