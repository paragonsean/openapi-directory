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
 * The PlayerKicking model module.
 * @module model/PlayerKicking
 * @version 1.0
 */
class PlayerKicking {
    /**
     * Constructs a new <code>PlayerKicking</code>.
     * @alias module:model/PlayerKicking
     */
    constructor() { 
        
        PlayerKicking.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PlayerKicking</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlayerKicking} obj Optional instance to populate.
     * @return {module:model/PlayerKicking} The populated <code>PlayerKicking</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlayerKicking();

            if (data.hasOwnProperty('ExtraPointsAttempted')) {
                obj['ExtraPointsAttempted'] = ApiClient.convertToType(data['ExtraPointsAttempted'], 'Number');
            }
            if (data.hasOwnProperty('ExtraPointsMade')) {
                obj['ExtraPointsMade'] = ApiClient.convertToType(data['ExtraPointsMade'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPoints')) {
                obj['FantasyPoints'] = ApiClient.convertToType(data['FantasyPoints'], 'Number');
            }
            if (data.hasOwnProperty('FantasyPosition')) {
                obj['FantasyPosition'] = ApiClient.convertToType(data['FantasyPosition'], 'String');
            }
            if (data.hasOwnProperty('FieldGoalPercentage')) {
                obj['FieldGoalPercentage'] = ApiClient.convertToType(data['FieldGoalPercentage'], 'Number');
            }
            if (data.hasOwnProperty('FieldGoalsAttempted')) {
                obj['FieldGoalsAttempted'] = ApiClient.convertToType(data['FieldGoalsAttempted'], 'Number');
            }
            if (data.hasOwnProperty('FieldGoalsLongestMade')) {
                obj['FieldGoalsLongestMade'] = ApiClient.convertToType(data['FieldGoalsLongestMade'], 'Number');
            }
            if (data.hasOwnProperty('FieldGoalsMade')) {
                obj['FieldGoalsMade'] = ApiClient.convertToType(data['FieldGoalsMade'], 'Number');
            }
            if (data.hasOwnProperty('FieldGoalsMade0to19')) {
                obj['FieldGoalsMade0to19'] = ApiClient.convertToType(data['FieldGoalsMade0to19'], 'Number');
            }
            if (data.hasOwnProperty('FieldGoalsMade20to29')) {
                obj['FieldGoalsMade20to29'] = ApiClient.convertToType(data['FieldGoalsMade20to29'], 'Number');
            }
            if (data.hasOwnProperty('FieldGoalsMade30to39')) {
                obj['FieldGoalsMade30to39'] = ApiClient.convertToType(data['FieldGoalsMade30to39'], 'Number');
            }
            if (data.hasOwnProperty('FieldGoalsMade40to49')) {
                obj['FieldGoalsMade40to49'] = ApiClient.convertToType(data['FieldGoalsMade40to49'], 'Number');
            }
            if (data.hasOwnProperty('FieldGoalsMade50Plus')) {
                obj['FieldGoalsMade50Plus'] = ApiClient.convertToType(data['FieldGoalsMade50Plus'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Number')) {
                obj['Number'] = ApiClient.convertToType(data['Number'], 'Number');
            }
            if (data.hasOwnProperty('PlayerGameID')) {
                obj['PlayerGameID'] = ApiClient.convertToType(data['PlayerGameID'], 'Number');
            }
            if (data.hasOwnProperty('PlayerID')) {
                obj['PlayerID'] = ApiClient.convertToType(data['PlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Position')) {
                obj['Position'] = ApiClient.convertToType(data['Position'], 'String');
            }
            if (data.hasOwnProperty('PositionCategory')) {
                obj['PositionCategory'] = ApiClient.convertToType(data['PositionCategory'], 'String');
            }
            if (data.hasOwnProperty('ShortName')) {
                obj['ShortName'] = ApiClient.convertToType(data['ShortName'], 'String');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlayerKicking</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlayerKicking</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['FantasyPosition'] && !(typeof data['FantasyPosition'] === 'string' || data['FantasyPosition'] instanceof String)) {
            throw new Error("Expected the field `FantasyPosition` to be a primitive type in the JSON string but got " + data['FantasyPosition']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Position'] && !(typeof data['Position'] === 'string' || data['Position'] instanceof String)) {
            throw new Error("Expected the field `Position` to be a primitive type in the JSON string but got " + data['Position']);
        }
        // ensure the json data is a string
        if (data['PositionCategory'] && !(typeof data['PositionCategory'] === 'string' || data['PositionCategory'] instanceof String)) {
            throw new Error("Expected the field `PositionCategory` to be a primitive type in the JSON string but got " + data['PositionCategory']);
        }
        // ensure the json data is a string
        if (data['ShortName'] && !(typeof data['ShortName'] === 'string' || data['ShortName'] instanceof String)) {
            throw new Error("Expected the field `ShortName` to be a primitive type in the JSON string but got " + data['ShortName']);
        }
        // ensure the json data is a string
        if (data['Team'] && !(typeof data['Team'] === 'string' || data['Team'] instanceof String)) {
            throw new Error("Expected the field `Team` to be a primitive type in the JSON string but got " + data['Team']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }

        return true;
    }


}



/**
 * @member {Number} ExtraPointsAttempted
 */
PlayerKicking.prototype['ExtraPointsAttempted'] = undefined;

/**
 * @member {Number} ExtraPointsMade
 */
PlayerKicking.prototype['ExtraPointsMade'] = undefined;

/**
 * @member {Number} FantasyPoints
 */
PlayerKicking.prototype['FantasyPoints'] = undefined;

/**
 * @member {String} FantasyPosition
 */
PlayerKicking.prototype['FantasyPosition'] = undefined;

/**
 * @member {Number} FieldGoalPercentage
 */
PlayerKicking.prototype['FieldGoalPercentage'] = undefined;

/**
 * @member {Number} FieldGoalsAttempted
 */
PlayerKicking.prototype['FieldGoalsAttempted'] = undefined;

/**
 * @member {Number} FieldGoalsLongestMade
 */
PlayerKicking.prototype['FieldGoalsLongestMade'] = undefined;

/**
 * @member {Number} FieldGoalsMade
 */
PlayerKicking.prototype['FieldGoalsMade'] = undefined;

/**
 * @member {Number} FieldGoalsMade0to19
 */
PlayerKicking.prototype['FieldGoalsMade0to19'] = undefined;

/**
 * @member {Number} FieldGoalsMade20to29
 */
PlayerKicking.prototype['FieldGoalsMade20to29'] = undefined;

/**
 * @member {Number} FieldGoalsMade30to39
 */
PlayerKicking.prototype['FieldGoalsMade30to39'] = undefined;

/**
 * @member {Number} FieldGoalsMade40to49
 */
PlayerKicking.prototype['FieldGoalsMade40to49'] = undefined;

/**
 * @member {Number} FieldGoalsMade50Plus
 */
PlayerKicking.prototype['FieldGoalsMade50Plus'] = undefined;

/**
 * @member {String} Name
 */
PlayerKicking.prototype['Name'] = undefined;

/**
 * @member {Number} Number
 */
PlayerKicking.prototype['Number'] = undefined;

/**
 * @member {Number} PlayerGameID
 */
PlayerKicking.prototype['PlayerGameID'] = undefined;

/**
 * @member {Number} PlayerID
 */
PlayerKicking.prototype['PlayerID'] = undefined;

/**
 * @member {String} Position
 */
PlayerKicking.prototype['Position'] = undefined;

/**
 * @member {String} PositionCategory
 */
PlayerKicking.prototype['PositionCategory'] = undefined;

/**
 * @member {String} ShortName
 */
PlayerKicking.prototype['ShortName'] = undefined;

/**
 * @member {String} Team
 */
PlayerKicking.prototype['Team'] = undefined;

/**
 * @member {String} Updated
 */
PlayerKicking.prototype['Updated'] = undefined;






export default PlayerKicking;

