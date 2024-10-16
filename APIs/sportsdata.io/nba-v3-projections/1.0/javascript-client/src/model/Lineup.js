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

/**
 * The Lineup model module.
 * @module model/Lineup
 * @version 1.0
 */
class Lineup {
    /**
     * Constructs a new <code>Lineup</code>.
     * @alias module:model/Lineup
     */
    constructor() { 
        
        Lineup.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Lineup</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Lineup} obj Optional instance to populate.
     * @return {module:model/Lineup} The populated <code>Lineup</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Lineup();

            if (data.hasOwnProperty('Confirmed')) {
                obj['Confirmed'] = ApiClient.convertToType(data['Confirmed'], 'Boolean');
            }
            if (data.hasOwnProperty('FirstName')) {
                obj['FirstName'] = ApiClient.convertToType(data['FirstName'], 'String');
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
            if (data.hasOwnProperty('Starting')) {
                obj['Starting'] = ApiClient.convertToType(data['Starting'], 'Boolean');
            }
            if (data.hasOwnProperty('Team')) {
                obj['Team'] = ApiClient.convertToType(data['Team'], 'String');
            }
            if (data.hasOwnProperty('TeamID')) {
                obj['TeamID'] = ApiClient.convertToType(data['TeamID'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Lineup</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Lineup</code>.
     */
    static validateJSON(data) {
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
 * @member {Boolean} Confirmed
 */
Lineup.prototype['Confirmed'] = undefined;

/**
 * @member {String} FirstName
 */
Lineup.prototype['FirstName'] = undefined;

/**
 * @member {String} LastName
 */
Lineup.prototype['LastName'] = undefined;

/**
 * @member {Number} PlayerID
 */
Lineup.prototype['PlayerID'] = undefined;

/**
 * @member {String} Position
 */
Lineup.prototype['Position'] = undefined;

/**
 * @member {Boolean} Starting
 */
Lineup.prototype['Starting'] = undefined;

/**
 * @member {String} Team
 */
Lineup.prototype['Team'] = undefined;

/**
 * @member {Number} TeamID
 */
Lineup.prototype['TeamID'] = undefined;






export default Lineup;

