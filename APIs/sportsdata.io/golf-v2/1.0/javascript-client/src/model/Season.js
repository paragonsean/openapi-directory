/**
 * Golf v2
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
 * The Season model module.
 * @module model/Season
 * @version 1.0
 */
class Season {
    /**
     * Constructs a new <code>Season</code>.
     * @alias module:model/Season
     */
    constructor() { 
        
        Season.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Season</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Season} obj Optional instance to populate.
     * @return {module:model/Season} The populated <code>Season</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Season();

            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('EndDate')) {
                obj['EndDate'] = ApiClient.convertToType(data['EndDate'], 'String');
            }
            if (data.hasOwnProperty('SeasonID')) {
                obj['SeasonID'] = ApiClient.convertToType(data['SeasonID'], 'Number');
            }
            if (data.hasOwnProperty('StartDate')) {
                obj['StartDate'] = ApiClient.convertToType(data['StartDate'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Season</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Season</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }
        // ensure the json data is a string
        if (data['EndDate'] && !(typeof data['EndDate'] === 'string' || data['EndDate'] instanceof String)) {
            throw new Error("Expected the field `EndDate` to be a primitive type in the JSON string but got " + data['EndDate']);
        }
        // ensure the json data is a string
        if (data['StartDate'] && !(typeof data['StartDate'] === 'string' || data['StartDate'] instanceof String)) {
            throw new Error("Expected the field `StartDate` to be a primitive type in the JSON string but got " + data['StartDate']);
        }

        return true;
    }


}



/**
 * @member {String} Description
 */
Season.prototype['Description'] = undefined;

/**
 * @member {String} EndDate
 */
Season.prototype['EndDate'] = undefined;

/**
 * @member {Number} SeasonID
 */
Season.prototype['SeasonID'] = undefined;

/**
 * @member {String} StartDate
 */
Season.prototype['StartDate'] = undefined;






export default Season;

