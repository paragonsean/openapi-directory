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

/**
 * The Quarter model module.
 * @module model/Quarter
 * @version 1.0
 */
class Quarter {
    /**
     * Constructs a new <code>Quarter</code>.
     * @alias module:model/Quarter
     */
    constructor() { 
        
        Quarter.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Quarter</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Quarter} obj Optional instance to populate.
     * @return {module:model/Quarter} The populated <code>Quarter</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Quarter();

            if (data.hasOwnProperty('AwayTeamScore')) {
                obj['AwayTeamScore'] = ApiClient.convertToType(data['AwayTeamScore'], 'Number');
            }
            if (data.hasOwnProperty('Created')) {
                obj['Created'] = ApiClient.convertToType(data['Created'], 'String');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('HomeTeamScore')) {
                obj['HomeTeamScore'] = ApiClient.convertToType(data['HomeTeamScore'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Number')) {
                obj['Number'] = ApiClient.convertToType(data['Number'], 'Number');
            }
            if (data.hasOwnProperty('QuarterID')) {
                obj['QuarterID'] = ApiClient.convertToType(data['QuarterID'], 'Number');
            }
            if (data.hasOwnProperty('ScoreID')) {
                obj['ScoreID'] = ApiClient.convertToType(data['ScoreID'], 'Number');
            }
            if (data.hasOwnProperty('Updated')) {
                obj['Updated'] = ApiClient.convertToType(data['Updated'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Quarter</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Quarter</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Created'] && !(typeof data['Created'] === 'string' || data['Created'] instanceof String)) {
            throw new Error("Expected the field `Created` to be a primitive type in the JSON string but got " + data['Created']);
        }
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Updated'] && !(typeof data['Updated'] === 'string' || data['Updated'] instanceof String)) {
            throw new Error("Expected the field `Updated` to be a primitive type in the JSON string but got " + data['Updated']);
        }

        return true;
    }


}



/**
 * @member {Number} AwayTeamScore
 */
Quarter.prototype['AwayTeamScore'] = undefined;

/**
 * @member {String} Created
 */
Quarter.prototype['Created'] = undefined;

/**
 * @member {String} Description
 */
Quarter.prototype['Description'] = undefined;

/**
 * @member {Number} HomeTeamScore
 */
Quarter.prototype['HomeTeamScore'] = undefined;

/**
 * @member {String} Name
 */
Quarter.prototype['Name'] = undefined;

/**
 * @member {Number} Number
 */
Quarter.prototype['Number'] = undefined;

/**
 * @member {Number} QuarterID
 */
Quarter.prototype['QuarterID'] = undefined;

/**
 * @member {Number} ScoreID
 */
Quarter.prototype['ScoreID'] = undefined;

/**
 * @member {String} Updated
 */
Quarter.prototype['Updated'] = undefined;






export default Quarter;

