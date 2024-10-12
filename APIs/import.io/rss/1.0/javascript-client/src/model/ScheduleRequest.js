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
 * The ScheduleRequest model module.
 * @module model/ScheduleRequest
 * @version 1.0
 */
class ScheduleRequest {
    /**
     * Constructs a new <code>ScheduleRequest</code>.
     * @alias module:model/ScheduleRequest
     * @param extractorId {String} 
     * @param interval {String} 
     */
    constructor(extractorId, interval) { 
        
        ScheduleRequest.initialize(this, extractorId, interval);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, extractorId, interval) { 
        obj['extractorId'] = extractorId;
        obj['interval'] = interval;
    }

    /**
     * Constructs a <code>ScheduleRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ScheduleRequest} obj Optional instance to populate.
     * @return {module:model/ScheduleRequest} The populated <code>ScheduleRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ScheduleRequest();

            if (data.hasOwnProperty('extractorId')) {
                obj['extractorId'] = ApiClient.convertToType(data['extractorId'], 'String');
            }
            if (data.hasOwnProperty('interval')) {
                obj['interval'] = ApiClient.convertToType(data['interval'], 'String');
            }
            if (data.hasOwnProperty('startTimestamp')) {
                obj['startTimestamp'] = ApiClient.convertToType(data['startTimestamp'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ScheduleRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ScheduleRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ScheduleRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['extractorId'] && !(typeof data['extractorId'] === 'string' || data['extractorId'] instanceof String)) {
            throw new Error("Expected the field `extractorId` to be a primitive type in the JSON string but got " + data['extractorId']);
        }
        // ensure the json data is a string
        if (data['interval'] && !(typeof data['interval'] === 'string' || data['interval'] instanceof String)) {
            throw new Error("Expected the field `interval` to be a primitive type in the JSON string but got " + data['interval']);
        }

        return true;
    }


}

ScheduleRequest.RequiredProperties = ["extractorId", "interval"];

/**
 * @member {String} extractorId
 */
ScheduleRequest.prototype['extractorId'] = undefined;

/**
 * @member {String} interval
 */
ScheduleRequest.prototype['interval'] = undefined;

/**
 * @member {Number} startTimestamp
 */
ScheduleRequest.prototype['startTimestamp'] = undefined;






export default ScheduleRequest;

