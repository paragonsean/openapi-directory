/**
 * Soccer v3 Stats
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
import Season from './Season';

/**
 * The Competition model module.
 * @module model/Competition
 * @version 1.0
 */
class Competition {
    /**
     * Constructs a new <code>Competition</code>.
     * @alias module:model/Competition
     */
    constructor() { 
        
        Competition.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Competition</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Competition} obj Optional instance to populate.
     * @return {module:model/Competition} The populated <code>Competition</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Competition();

            if (data.hasOwnProperty('AreaId')) {
                obj['AreaId'] = ApiClient.convertToType(data['AreaId'], 'Number');
            }
            if (data.hasOwnProperty('AreaName')) {
                obj['AreaName'] = ApiClient.convertToType(data['AreaName'], 'String');
            }
            if (data.hasOwnProperty('CompetitionId')) {
                obj['CompetitionId'] = ApiClient.convertToType(data['CompetitionId'], 'Number');
            }
            if (data.hasOwnProperty('Format')) {
                obj['Format'] = ApiClient.convertToType(data['Format'], 'String');
            }
            if (data.hasOwnProperty('Gender')) {
                obj['Gender'] = ApiClient.convertToType(data['Gender'], 'String');
            }
            if (data.hasOwnProperty('Key')) {
                obj['Key'] = ApiClient.convertToType(data['Key'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Seasons')) {
                obj['Seasons'] = ApiClient.convertToType(data['Seasons'], [Season]);
            }
            if (data.hasOwnProperty('Type')) {
                obj['Type'] = ApiClient.convertToType(data['Type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Competition</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Competition</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AreaName'] && !(typeof data['AreaName'] === 'string' || data['AreaName'] instanceof String)) {
            throw new Error("Expected the field `AreaName` to be a primitive type in the JSON string but got " + data['AreaName']);
        }
        // ensure the json data is a string
        if (data['Format'] && !(typeof data['Format'] === 'string' || data['Format'] instanceof String)) {
            throw new Error("Expected the field `Format` to be a primitive type in the JSON string but got " + data['Format']);
        }
        // ensure the json data is a string
        if (data['Gender'] && !(typeof data['Gender'] === 'string' || data['Gender'] instanceof String)) {
            throw new Error("Expected the field `Gender` to be a primitive type in the JSON string but got " + data['Gender']);
        }
        // ensure the json data is a string
        if (data['Key'] && !(typeof data['Key'] === 'string' || data['Key'] instanceof String)) {
            throw new Error("Expected the field `Key` to be a primitive type in the JSON string but got " + data['Key']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        if (data['Seasons']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Seasons'])) {
                throw new Error("Expected the field `Seasons` to be an array in the JSON data but got " + data['Seasons']);
            }
            // validate the optional field `Seasons` (array)
            for (const item of data['Seasons']) {
                Season.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['Type'] && !(typeof data['Type'] === 'string' || data['Type'] instanceof String)) {
            throw new Error("Expected the field `Type` to be a primitive type in the JSON string but got " + data['Type']);
        }

        return true;
    }


}



/**
 * @member {Number} AreaId
 */
Competition.prototype['AreaId'] = undefined;

/**
 * @member {String} AreaName
 */
Competition.prototype['AreaName'] = undefined;

/**
 * @member {Number} CompetitionId
 */
Competition.prototype['CompetitionId'] = undefined;

/**
 * @member {String} Format
 */
Competition.prototype['Format'] = undefined;

/**
 * @member {String} Gender
 */
Competition.prototype['Gender'] = undefined;

/**
 * @member {String} Key
 */
Competition.prototype['Key'] = undefined;

/**
 * @member {String} Name
 */
Competition.prototype['Name'] = undefined;

/**
 * @member {Array.<module:model/Season>} Seasons
 */
Competition.prototype['Seasons'] = undefined;

/**
 * @member {String} Type
 */
Competition.prototype['Type'] = undefined;






export default Competition;

