/**
 * import.io
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
 * The ScheduleIntervalData model module.
 * @module model/ScheduleIntervalData
 * @version 1.0
 */
class ScheduleIntervalData {
    /**
     * Constructs a new <code>ScheduleIntervalData</code>.
     * @alias module:model/ScheduleIntervalData
     */
    constructor() { 
        
        ScheduleIntervalData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ScheduleIntervalData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ScheduleIntervalData} obj Optional instance to populate.
     * @return {module:model/ScheduleIntervalData} The populated <code>ScheduleIntervalData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ScheduleIntervalData();

            if (data.hasOwnProperty('minutes')) {
                obj['minutes'] = ApiClient.convertToType(data['minutes'], 'String');
            }
            if (data.hasOwnProperty('time')) {
                obj['time'] = ApiClient.convertToType(data['time'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ScheduleIntervalData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ScheduleIntervalData</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['minutes'] && !(typeof data['minutes'] === 'string' || data['minutes'] instanceof String)) {
            throw new Error("Expected the field `minutes` to be a primitive type in the JSON string but got " + data['minutes']);
        }
        // ensure the json data is a string
        if (data['time'] && !(typeof data['time'] === 'string' || data['time'] instanceof String)) {
            throw new Error("Expected the field `time` to be a primitive type in the JSON string but got " + data['time']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {String} minutes
 */
ScheduleIntervalData.prototype['minutes'] = undefined;

/**
 * @member {String} time
 */
ScheduleIntervalData.prototype['time'] = undefined;

/**
 * @member {String} type
 */
ScheduleIntervalData.prototype['type'] = undefined;






export default ScheduleIntervalData;

