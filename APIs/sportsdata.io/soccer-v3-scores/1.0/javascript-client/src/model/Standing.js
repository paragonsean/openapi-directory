/**
 * Soccer v3 Scores
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

/**
 * The Standing model module.
 * @module model/Standing
 * @version 1.0
 */
class Standing {
    /**
     * Constructs a new <code>Standing</code>.
     * @alias module:model/Standing
     */
    constructor() { 
        
        Standing.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Standing</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Standing} obj Optional instance to populate.
     * @return {module:model/Standing} The populated <code>Standing</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Standing();

            if (data.hasOwnProperty('Draws')) {
                obj['Draws'] = ApiClient.convertToType(data['Draws'], 'Number');
            }
            if (data.hasOwnProperty('Games')) {
                obj['Games'] = ApiClient.convertToType(data['Games'], 'Number');
            }
            if (data.hasOwnProperty('GlobalTeamID')) {
                obj['GlobalTeamID'] = ApiClient.convertToType(data['GlobalTeamID'], 'Number');
            }
            if (data.hasOwnProperty('GoalsAgainst')) {
                obj['GoalsAgainst'] = ApiClient.convertToType(data['GoalsAgainst'], 'Number');
            }
            if (data.hasOwnProperty('GoalsDifferential')) {
                obj['GoalsDifferential'] = ApiClient.convertToType(data['GoalsDifferential'], 'Number');
            }
            if (data.hasOwnProperty('GoalsScored')) {
                obj['GoalsScored'] = ApiClient.convertToType(data['GoalsScored'], 'Number');
            }
            if (data.hasOwnProperty('Group')) {
                obj['Group'] = ApiClient.convertToType(data['Group'], 'String');
            }
            if (data.hasOwnProperty('Losses')) {
                obj['Losses'] = ApiClient.convertToType(data['Losses'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Order')) {
                obj['Order'] = ApiClient.convertToType(data['Order'], 'Number');
            }
            if (data.hasOwnProperty('Points')) {
                obj['Points'] = ApiClient.convertToType(data['Points'], 'Number');
            }
            if (data.hasOwnProperty('RoundId')) {
                obj['RoundId'] = ApiClient.convertToType(data['RoundId'], 'Number');
            }
            if (data.hasOwnProperty('Scope')) {
                obj['Scope'] = ApiClient.convertToType(data['Scope'], 'String');
            }
            if (data.hasOwnProperty('ShortName')) {
                obj['ShortName'] = ApiClient.convertToType(data['ShortName'], 'String');
            }
            if (data.hasOwnProperty('StandingId')) {
                obj['StandingId'] = ApiClient.convertToType(data['StandingId'], 'Number');
            }
            if (data.hasOwnProperty('TeamId')) {
                obj['TeamId'] = ApiClient.convertToType(data['TeamId'], 'Number');
            }
            if (data.hasOwnProperty('Wins')) {
                obj['Wins'] = ApiClient.convertToType(data['Wins'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Standing</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Standing</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Group'] && !(typeof data['Group'] === 'string' || data['Group'] instanceof String)) {
            throw new Error("Expected the field `Group` to be a primitive type in the JSON string but got " + data['Group']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Scope'] && !(typeof data['Scope'] === 'string' || data['Scope'] instanceof String)) {
            throw new Error("Expected the field `Scope` to be a primitive type in the JSON string but got " + data['Scope']);
        }
        // ensure the json data is a string
        if (data['ShortName'] && !(typeof data['ShortName'] === 'string' || data['ShortName'] instanceof String)) {
            throw new Error("Expected the field `ShortName` to be a primitive type in the JSON string but got " + data['ShortName']);
        }

        return true;
    }


}



/**
 * @member {Number} Draws
 */
Standing.prototype['Draws'] = undefined;

/**
 * @member {Number} Games
 */
Standing.prototype['Games'] = undefined;

/**
 * @member {Number} GlobalTeamID
 */
Standing.prototype['GlobalTeamID'] = undefined;

/**
 * @member {Number} GoalsAgainst
 */
Standing.prototype['GoalsAgainst'] = undefined;

/**
 * @member {Number} GoalsDifferential
 */
Standing.prototype['GoalsDifferential'] = undefined;

/**
 * @member {Number} GoalsScored
 */
Standing.prototype['GoalsScored'] = undefined;

/**
 * @member {String} Group
 */
Standing.prototype['Group'] = undefined;

/**
 * @member {Number} Losses
 */
Standing.prototype['Losses'] = undefined;

/**
 * @member {String} Name
 */
Standing.prototype['Name'] = undefined;

/**
 * @member {Number} Order
 */
Standing.prototype['Order'] = undefined;

/**
 * @member {Number} Points
 */
Standing.prototype['Points'] = undefined;

/**
 * @member {Number} RoundId
 */
Standing.prototype['RoundId'] = undefined;

/**
 * @member {String} Scope
 */
Standing.prototype['Scope'] = undefined;

/**
 * @member {String} ShortName
 */
Standing.prototype['ShortName'] = undefined;

/**
 * @member {Number} StandingId
 */
Standing.prototype['StandingId'] = undefined;

/**
 * @member {Number} TeamId
 */
Standing.prototype['TeamId'] = undefined;

/**
 * @member {Number} Wins
 */
Standing.prototype['Wins'] = undefined;






export default Standing;

