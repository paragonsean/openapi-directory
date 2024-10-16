/**
 * LoL v3 Scores
 * LoL v3 Scores
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

            if (data.hasOwnProperty('BestOf')) {
                obj['BestOf'] = ApiClient.convertToType(data['BestOf'], 'String');
            }
            if (data.hasOwnProperty('DateTime')) {
                obj['DateTime'] = ApiClient.convertToType(data['DateTime'], 'String');
            }
            if (data.hasOwnProperty('Day')) {
                obj['Day'] = ApiClient.convertToType(data['Day'], 'String');
            }
            if (data.hasOwnProperty('DrawMoneyLine')) {
                obj['DrawMoneyLine'] = ApiClient.convertToType(data['DrawMoneyLine'], 'Number');
            }
            if (data.hasOwnProperty('GameId')) {
                obj['GameId'] = ApiClient.convertToType(data['GameId'], 'Number');
            }
            if (data.hasOwnProperty('Group')) {
                obj['Group'] = ApiClient.convertToType(data['Group'], 'String');
            }
            if (data.hasOwnProperty('IsClosed')) {
                obj['IsClosed'] = ApiClient.convertToType(data['IsClosed'], 'Boolean');
            }
            if (data.hasOwnProperty('PointSpread')) {
                obj['PointSpread'] = ApiClient.convertToType(data['PointSpread'], 'Number');
            }
            if (data.hasOwnProperty('RoundId')) {
                obj['RoundId'] = ApiClient.convertToType(data['RoundId'], 'Number');
            }
            if (data.hasOwnProperty('Season')) {
                obj['Season'] = ApiClient.convertToType(data['Season'], 'Number');
            }
            if (data.hasOwnProperty('SeasonType')) {
                obj['SeasonType'] = ApiClient.convertToType(data['SeasonType'], 'Number');
            }
            if (data.hasOwnProperty('Status')) {
                obj['Status'] = ApiClient.convertToType(data['Status'], 'String');
            }
            if (data.hasOwnProperty('TeamAId')) {
                obj['TeamAId'] = ApiClient.convertToType(data['TeamAId'], 'Number');
            }
            if (data.hasOwnProperty('TeamAKey')) {
                obj['TeamAKey'] = ApiClient.convertToType(data['TeamAKey'], 'String');
            }
            if (data.hasOwnProperty('TeamAMoneyLine')) {
                obj['TeamAMoneyLine'] = ApiClient.convertToType(data['TeamAMoneyLine'], 'Number');
            }
            if (data.hasOwnProperty('TeamAName')) {
                obj['TeamAName'] = ApiClient.convertToType(data['TeamAName'], 'String');
            }
            if (data.hasOwnProperty('TeamAPointSpreadPayout')) {
                obj['TeamAPointSpreadPayout'] = ApiClient.convertToType(data['TeamAPointSpreadPayout'], 'Number');
            }
            if (data.hasOwnProperty('TeamAScore')) {
                obj['TeamAScore'] = ApiClient.convertToType(data['TeamAScore'], 'Number');
            }
            if (data.hasOwnProperty('TeamBId')) {
                obj['TeamBId'] = ApiClient.convertToType(data['TeamBId'], 'Number');
            }
            if (data.hasOwnProperty('TeamBKey')) {
                obj['TeamBKey'] = ApiClient.convertToType(data['TeamBKey'], 'String');
            }
            if (data.hasOwnProperty('TeamBMoneyLine')) {
                obj['TeamBMoneyLine'] = ApiClient.convertToType(data['TeamBMoneyLine'], 'Number');
            }
            if (data.hasOwnProperty('TeamBName')) {
                obj['TeamBName'] = ApiClient.convertToType(data['TeamBName'], 'String');
            }
            if (data.hasOwnProperty('TeamBPointSpreadPayout')) {
                obj['TeamBPointSpreadPayout'] = ApiClient.convertToType(data['TeamBPointSpreadPayout'], 'Number');
            }
            if (data.hasOwnProperty('TeamBScore')) {
                obj['TeamBScore'] = ApiClient.convertToType(data['TeamBScore'], 'Number');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
            if (data.hasOwnProperty('UpdatedUtc')) {
                obj['UpdatedUtc'] = ApiClient.convertToType(data['UpdatedUtc'], 'String');
            }
            if (data.hasOwnProperty('VenueId')) {
                obj['VenueId'] = ApiClient.convertToType(data['VenueId'], 'Number');
            }
            if (data.hasOwnProperty('VenueType')) {
                obj['VenueType'] = ApiClient.convertToType(data['VenueType'], 'String');
            }
            if (data.hasOwnProperty('Week')) {
                obj['Week'] = ApiClient.convertToType(data['Week'], 'Number');
            }
            if (data.hasOwnProperty('Winner')) {
                obj['Winner'] = ApiClient.convertToType(data['Winner'], 'String');
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
        if (data['BestOf'] && !(typeof data['BestOf'] === 'string' || data['BestOf'] instanceof String)) {
            throw new Error("Expected the field `BestOf` to be a primitive type in the JSON string but got " + data['BestOf']);
        }
        // ensure the json data is a string
        if (data['DateTime'] && !(typeof data['DateTime'] === 'string' || data['DateTime'] instanceof String)) {
            throw new Error("Expected the field `DateTime` to be a primitive type in the JSON string but got " + data['DateTime']);
        }
        // ensure the json data is a string
        if (data['Day'] && !(typeof data['Day'] === 'string' || data['Day'] instanceof String)) {
            throw new Error("Expected the field `Day` to be a primitive type in the JSON string but got " + data['Day']);
        }
        // ensure the json data is a string
        if (data['Group'] && !(typeof data['Group'] === 'string' || data['Group'] instanceof String)) {
            throw new Error("Expected the field `Group` to be a primitive type in the JSON string but got " + data['Group']);
        }
        // ensure the json data is a string
        if (data['Status'] && !(typeof data['Status'] === 'string' || data['Status'] instanceof String)) {
            throw new Error("Expected the field `Status` to be a primitive type in the JSON string but got " + data['Status']);
        }
        // ensure the json data is a string
        if (data['TeamAKey'] && !(typeof data['TeamAKey'] === 'string' || data['TeamAKey'] instanceof String)) {
            throw new Error("Expected the field `TeamAKey` to be a primitive type in the JSON string but got " + data['TeamAKey']);
        }
        // ensure the json data is a string
        if (data['TeamAName'] && !(typeof data['TeamAName'] === 'string' || data['TeamAName'] instanceof String)) {
            throw new Error("Expected the field `TeamAName` to be a primitive type in the JSON string but got " + data['TeamAName']);
        }
        // ensure the json data is a string
        if (data['TeamBKey'] && !(typeof data['TeamBKey'] === 'string' || data['TeamBKey'] instanceof String)) {
            throw new Error("Expected the field `TeamBKey` to be a primitive type in the JSON string but got " + data['TeamBKey']);
        }
        // ensure the json data is a string
        if (data['TeamBName'] && !(typeof data['TeamBName'] === 'string' || data['TeamBName'] instanceof String)) {
            throw new Error("Expected the field `TeamBName` to be a primitive type in the JSON string but got " + data['TeamBName']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }
        // ensure the json data is a string
        if (data['UpdatedUtc'] && !(typeof data['UpdatedUtc'] === 'string' || data['UpdatedUtc'] instanceof String)) {
            throw new Error("Expected the field `UpdatedUtc` to be a primitive type in the JSON string but got " + data['UpdatedUtc']);
        }
        // ensure the json data is a string
        if (data['VenueType'] && !(typeof data['VenueType'] === 'string' || data['VenueType'] instanceof String)) {
            throw new Error("Expected the field `VenueType` to be a primitive type in the JSON string but got " + data['VenueType']);
        }
        // ensure the json data is a string
        if (data['Winner'] && !(typeof data['Winner'] === 'string' || data['Winner'] instanceof String)) {
            throw new Error("Expected the field `Winner` to be a primitive type in the JSON string but got " + data['Winner']);
        }

        return true;
    }


}



/**
 * @member {String} BestOf
 */
Game.prototype['BestOf'] = undefined;

/**
 * @member {String} DateTime
 */
Game.prototype['DateTime'] = undefined;

/**
 * @member {String} Day
 */
Game.prototype['Day'] = undefined;

/**
 * @member {Number} DrawMoneyLine
 */
Game.prototype['DrawMoneyLine'] = undefined;

/**
 * @member {Number} GameId
 */
Game.prototype['GameId'] = undefined;

/**
 * @member {String} Group
 */
Game.prototype['Group'] = undefined;

/**
 * @member {Boolean} IsClosed
 */
Game.prototype['IsClosed'] = undefined;

/**
 * @member {Number} PointSpread
 */
Game.prototype['PointSpread'] = undefined;

/**
 * @member {Number} RoundId
 */
Game.prototype['RoundId'] = undefined;

/**
 * @member {Number} Season
 */
Game.prototype['Season'] = undefined;

/**
 * @member {Number} SeasonType
 */
Game.prototype['SeasonType'] = undefined;

/**
 * @member {String} Status
 */
Game.prototype['Status'] = undefined;

/**
 * @member {Number} TeamAId
 */
Game.prototype['TeamAId'] = undefined;

/**
 * @member {String} TeamAKey
 */
Game.prototype['TeamAKey'] = undefined;

/**
 * @member {Number} TeamAMoneyLine
 */
Game.prototype['TeamAMoneyLine'] = undefined;

/**
 * @member {String} TeamAName
 */
Game.prototype['TeamAName'] = undefined;

/**
 * @member {Number} TeamAPointSpreadPayout
 */
Game.prototype['TeamAPointSpreadPayout'] = undefined;

/**
 * @member {Number} TeamAScore
 */
Game.prototype['TeamAScore'] = undefined;

/**
 * @member {Number} TeamBId
 */
Game.prototype['TeamBId'] = undefined;

/**
 * @member {String} TeamBKey
 */
Game.prototype['TeamBKey'] = undefined;

/**
 * @member {Number} TeamBMoneyLine
 */
Game.prototype['TeamBMoneyLine'] = undefined;

/**
 * @member {String} TeamBName
 */
Game.prototype['TeamBName'] = undefined;

/**
 * @member {Number} TeamBPointSpreadPayout
 */
Game.prototype['TeamBPointSpreadPayout'] = undefined;

/**
 * @member {Number} TeamBScore
 */
Game.prototype['TeamBScore'] = undefined;

/**
 * @member {String} Updated
 */
Game.prototype['Updated'] = undefined;

/**
 * @member {String} UpdatedUtc
 */
Game.prototype['UpdatedUtc'] = undefined;

/**
 * @member {Number} VenueId
 */
Game.prototype['VenueId'] = undefined;

/**
 * @member {String} VenueType
 */
Game.prototype['VenueType'] = undefined;

/**
 * @member {Number} Week
 */
Game.prototype['Week'] = undefined;

/**
 * @member {String} Winner
 */
Game.prototype['Winner'] = undefined;






export default Game;

