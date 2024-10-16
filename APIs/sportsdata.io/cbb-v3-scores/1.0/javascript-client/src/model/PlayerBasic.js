/**
 * CBB v3 Scores
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
 * The PlayerBasic model module.
 * @module model/PlayerBasic
 * @version 1.0
 */
class PlayerBasic {
    /**
     * Constructs a new <code>PlayerBasic</code>.
     * @alias module:model/PlayerBasic
     */
    constructor() { 
        
        PlayerBasic.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PlayerBasic</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlayerBasic} obj Optional instance to populate.
     * @return {module:model/PlayerBasic} The populated <code>PlayerBasic</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlayerBasic();

            if (data.hasOwnProperty('BirthCity')) {
                obj['BirthCity'] = ApiClient.convertToType(data['BirthCity'], 'String');
            }
            if (data.hasOwnProperty('BirthState')) {
                obj['BirthState'] = ApiClient.convertToType(data['BirthState'], 'String');
            }
            if (data.hasOwnProperty('Class')) {
                obj['Class'] = ApiClient.convertToType(data['Class'], 'String');
            }
            if (data.hasOwnProperty('FirstName')) {
                obj['FirstName'] = ApiClient.convertToType(data['FirstName'], 'String');
            }
            if (data.hasOwnProperty('GlobalTeamID')) {
                obj['GlobalTeamID'] = ApiClient.convertToType(data['GlobalTeamID'], 'Number');
            }
            if (data.hasOwnProperty('Height')) {
                obj['Height'] = ApiClient.convertToType(data['Height'], 'Number');
            }
            if (data.hasOwnProperty('Jersey')) {
                obj['Jersey'] = ApiClient.convertToType(data['Jersey'], 'Number');
            }
            if (data.hasOwnProperty('LastName')) {
                obj['LastName'] = ApiClient.convertToType(data['LastName'], 'String');
            }
            if (data.hasOwnProperty('PlayerID')) {
                obj['PlayerID'] = ApiClient.convertToType(data['PlayerID'], 'Number');
            }
            if (data.hasOwnProperty('Position')) {
                obj['Position'] = ApiClient.convertToType(data['Position'], 'String');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('TeamID')) {
                obj['TeamID'] = ApiClient.convertToType(data['TeamID'], 'Number');
            }
            if (data.hasOwnProperty('Weight')) {
                obj['Weight'] = ApiClient.convertToType(data['Weight'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlayerBasic</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlayerBasic</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['BirthCity'] && !(typeof data['BirthCity'] === 'string' || data['BirthCity'] instanceof String)) {
            throw new Error("Expected the field `BirthCity` to be a primitive type in the JSON string but got " + data['BirthCity']);
        }
        // ensure the json data is a string
        if (data['BirthState'] && !(typeof data['BirthState'] === 'string' || data['BirthState'] instanceof String)) {
            throw new Error("Expected the field `BirthState` to be a primitive type in the JSON string but got " + data['BirthState']);
        }
        // ensure the json data is a string
        if (data['Class'] && !(typeof data['Class'] === 'string' || data['Class'] instanceof String)) {
            throw new Error("Expected the field `Class` to be a primitive type in the JSON string but got " + data['Class']);
        }
        // ensure the json data is a string
        if (data['FirstName'] && !(typeof data['FirstName'] === 'string' || data['FirstName'] instanceof String)) {
            throw new Error("Expected the field `FirstName` to be a primitive type in the JSON string but got " + data['FirstName']);
        }
        // ensure the json data is a string
        if (data['LastName'] && !(typeof data['LastName'] === 'string' || data['LastName'] instanceof String)) {
            throw new Error("Expected the field `LastName` to be a primitive type in the JSON string but got " + data['LastName']);
        }
        // ensure the json data is a string
        if (data['Position'] && !(typeof data['Position'] === 'string' || data['Position'] instanceof String)) {
            throw new Error("Expected the field `Position` to be a primitive type in the JSON string but got " + data['Position']);
        }
        // ensure the json data is a string
        if (data['Team'] && !(typeof data['Team'] === 'string' || data['Team'] instanceof String)) {
            throw new Error("Expected the field `Team` to be a primitive type in the JSON string but got " + data['Team']);
        }

        return true;
    }


}



/**
 * @member {String} BirthCity
 */
PlayerBasic.prototype['BirthCity'] = undefined;

/**
 * @member {String} BirthState
 */
PlayerBasic.prototype['BirthState'] = undefined;

/**
 * @member {String} Class
 */
PlayerBasic.prototype['Class'] = undefined;

/**
 * @member {String} FirstName
 */
PlayerBasic.prototype['FirstName'] = undefined;

/**
 * @member {Number} GlobalTeamID
 */
PlayerBasic.prototype['GlobalTeamID'] = undefined;

/**
 * @member {Number} Height
 */
PlayerBasic.prototype['Height'] = undefined;

/**
 * @member {Number} Jersey
 */
PlayerBasic.prototype['Jersey'] = undefined;

/**
 * @member {String} LastName
 */
PlayerBasic.prototype['LastName'] = undefined;

/**
 * @member {Number} PlayerID
 */
PlayerBasic.prototype['PlayerID'] = undefined;

/**
 * @member {String} Position
 */
PlayerBasic.prototype['Position'] = undefined;

/**
 * @member {String} Team
 */
PlayerBasic.prototype['Team'] = undefined;

/**
 * @member {Number} TeamID
 */
PlayerBasic.prototype['TeamID'] = undefined;

/**
 * @member {Number} Weight
 */
PlayerBasic.prototype['Weight'] = undefined;






export default PlayerBasic;

