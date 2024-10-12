/**
 * CS:GO v3 Stats
 * CS:GO v3 Stats
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
 * The Player model module.
 * @module model/Player
 * @version 1.0
 */
class Player {
    /**
     * Constructs a new <code>Player</code>.
     * @alias module:model/Player
     */
    constructor() { 
        
        Player.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Player</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Player} obj Optional instance to populate.
     * @return {module:model/Player} The populated <code>Player</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Player();

            if (data.hasOwnProperty('BirthCity')) {
                obj['BirthCity'] = ApiClient.convertToType(data['BirthCity'], 'String');
            }
            if (data.hasOwnProperty('BirthCountry')) {
                obj['BirthCountry'] = ApiClient.convertToType(data['BirthCountry'], 'String');
            }
            if (data.hasOwnProperty('BirthDate')) {
                obj['BirthDate'] = ApiClient.convertToType(data['BirthDate'], 'String');
            }
            if (data.hasOwnProperty('CommonName')) {
                obj['CommonName'] = ApiClient.convertToType(data['CommonName'], 'String');
            }
            if (data.hasOwnProperty('FirstName')) {
                obj['FirstName'] = ApiClient.convertToType(data['FirstName'], 'String');
            }
            if (data.hasOwnProperty('Gender')) {
                obj['Gender'] = ApiClient.convertToType(data['Gender'], 'String');
            }
            if (data.hasOwnProperty('LastName')) {
                obj['LastName'] = ApiClient.convertToType(data['LastName'], 'String');
            }
            if (data.hasOwnProperty('MatchName')) {
                obj['MatchName'] = ApiClient.convertToType(data['MatchName'], 'String');
            }
            if (data.hasOwnProperty('Nationality')) {
                obj['Nationality'] = ApiClient.convertToType(data['Nationality'], 'String');
            }
            if (data.hasOwnProperty('PlayerId')) {
                obj['PlayerId'] = ApiClient.convertToType(data['PlayerId'], 'Number');
            }
            if (data.hasOwnProperty('Position')) {
                obj['Position'] = ApiClient.convertToType(data['Position'], 'String');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Player</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Player</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['BirthCity'] && !(typeof data['BirthCity'] === 'string' || data['BirthCity'] instanceof String)) {
            throw new Error("Expected the field `BirthCity` to be a primitive type in the JSON string but got " + data['BirthCity']);
        }
        // ensure the json data is a string
        if (data['BirthCountry'] && !(typeof data['BirthCountry'] === 'string' || data['BirthCountry'] instanceof String)) {
            throw new Error("Expected the field `BirthCountry` to be a primitive type in the JSON string but got " + data['BirthCountry']);
        }
        // ensure the json data is a string
        if (data['BirthDate'] && !(typeof data['BirthDate'] === 'string' || data['BirthDate'] instanceof String)) {
            throw new Error("Expected the field `BirthDate` to be a primitive type in the JSON string but got " + data['BirthDate']);
        }
        // ensure the json data is a string
        if (data['CommonName'] && !(typeof data['CommonName'] === 'string' || data['CommonName'] instanceof String)) {
            throw new Error("Expected the field `CommonName` to be a primitive type in the JSON string but got " + data['CommonName']);
        }
        // ensure the json data is a string
        if (data['FirstName'] && !(typeof data['FirstName'] === 'string' || data['FirstName'] instanceof String)) {
            throw new Error("Expected the field `FirstName` to be a primitive type in the JSON string but got " + data['FirstName']);
        }
        // ensure the json data is a string
        if (data['Gender'] && !(typeof data['Gender'] === 'string' || data['Gender'] instanceof String)) {
            throw new Error("Expected the field `Gender` to be a primitive type in the JSON string but got " + data['Gender']);
        }
        // ensure the json data is a string
        if (data['LastName'] && !(typeof data['LastName'] === 'string' || data['LastName'] instanceof String)) {
            throw new Error("Expected the field `LastName` to be a primitive type in the JSON string but got " + data['LastName']);
        }
        // ensure the json data is a string
        if (data['MatchName'] && !(typeof data['MatchName'] === 'string' || data['MatchName'] instanceof String)) {
            throw new Error("Expected the field `MatchName` to be a primitive type in the JSON string but got " + data['MatchName']);
        }
        // ensure the json data is a string
        if (data['Nationality'] && !(typeof data['Nationality'] === 'string' || data['Nationality'] instanceof String)) {
            throw new Error("Expected the field `Nationality` to be a primitive type in the JSON string but got " + data['Nationality']);
        }
        // ensure the json data is a string
        if (data['Position'] && !(typeof data['Position'] === 'string' || data['Position'] instanceof String)) {
            throw new Error("Expected the field `Position` to be a primitive type in the JSON string but got " + data['Position']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }

        return true;
    }


}



/**
 * @member {String} BirthCity
 */
Player.prototype['BirthCity'] = undefined;

/**
 * @member {String} BirthCountry
 */
Player.prototype['BirthCountry'] = undefined;

/**
 * @member {String} BirthDate
 */
Player.prototype['BirthDate'] = undefined;

/**
 * @member {String} CommonName
 */
Player.prototype['CommonName'] = undefined;

/**
 * @member {String} FirstName
 */
Player.prototype['FirstName'] = undefined;

/**
 * @member {String} Gender
 */
Player.prototype['Gender'] = undefined;

/**
 * @member {String} LastName
 */
Player.prototype['LastName'] = undefined;

/**
 * @member {String} MatchName
 */
Player.prototype['MatchName'] = undefined;

/**
 * @member {String} Nationality
 */
Player.prototype['Nationality'] = undefined;

/**
 * @member {Number} PlayerId
 */
Player.prototype['PlayerId'] = undefined;

/**
 * @member {String} Position
 */
Player.prototype['Position'] = undefined;

/**
 * @member {String} Updated
 */
Player.prototype['Updated'] = undefined;






export default Player;

