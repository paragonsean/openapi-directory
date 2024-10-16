/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DistrictList model module.
 * @module model/DistrictList
 * @version 3.8.2
 */
class DistrictList {
    /**
     * Constructs a new <code>DistrictList</code>.
     * @alias module:model/DistrictList
     * @param abbreviation {String} The short identifier for the district.
     * @param displayName {String} The long name for the district.
     * @param key {String} Key for this district, e.g. `2016ne`.
     * @param year {Number} Year this district participated.
     */
    constructor(abbreviation, displayName, key, year) { 
        
        DistrictList.initialize(this, abbreviation, displayName, key, year);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, abbreviation, displayName, key, year) { 
        obj['abbreviation'] = abbreviation;
        obj['display_name'] = displayName;
        obj['key'] = key;
        obj['year'] = year;
    }

    /**
     * Constructs a <code>DistrictList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DistrictList} obj Optional instance to populate.
     * @return {module:model/DistrictList} The populated <code>DistrictList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DistrictList();

            if (data.hasOwnProperty('abbreviation')) {
                obj['abbreviation'] = ApiClient.convertToType(data['abbreviation'], 'String');
            }
            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
            if (data.hasOwnProperty('key')) {
                obj['key'] = ApiClient.convertToType(data['key'], 'String');
            }
            if (data.hasOwnProperty('year')) {
                obj['year'] = ApiClient.convertToType(data['year'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DistrictList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DistrictList</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DistrictList.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['abbreviation'] && !(typeof data['abbreviation'] === 'string' || data['abbreviation'] instanceof String)) {
            throw new Error("Expected the field `abbreviation` to be a primitive type in the JSON string but got " + data['abbreviation']);
        }
        // ensure the json data is a string
        if (data['display_name'] && !(typeof data['display_name'] === 'string' || data['display_name'] instanceof String)) {
            throw new Error("Expected the field `display_name` to be a primitive type in the JSON string but got " + data['display_name']);
        }
        // ensure the json data is a string
        if (data['key'] && !(typeof data['key'] === 'string' || data['key'] instanceof String)) {
            throw new Error("Expected the field `key` to be a primitive type in the JSON string but got " + data['key']);
        }

        return true;
    }


}

DistrictList.RequiredProperties = ["abbreviation", "display_name", "key", "year"];

/**
 * The short identifier for the district.
 * @member {String} abbreviation
 */
DistrictList.prototype['abbreviation'] = undefined;

/**
 * The long name for the district.
 * @member {String} display_name
 */
DistrictList.prototype['display_name'] = undefined;

/**
 * Key for this district, e.g. `2016ne`.
 * @member {String} key
 */
DistrictList.prototype['key'] = undefined;

/**
 * Year this district participated.
 * @member {Number} year
 */
DistrictList.prototype['year'] = undefined;






export default DistrictList;

