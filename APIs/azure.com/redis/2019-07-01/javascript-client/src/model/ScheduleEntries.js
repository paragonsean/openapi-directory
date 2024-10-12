/**
 * RedisManagementClient
 * REST API for Azure Redis Cache Service.
 *
 * The version of the OpenAPI document: 2019-07-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ScheduleEntry from './ScheduleEntry';

/**
 * The ScheduleEntries model module.
 * @module model/ScheduleEntries
 * @version 2019-07-01
 */
class ScheduleEntries {
    /**
     * Constructs a new <code>ScheduleEntries</code>.
     * List of patch schedules for a Redis cache.
     * @alias module:model/ScheduleEntries
     * @param scheduleEntries {Array.<module:model/ScheduleEntry>} List of patch schedules for a Redis cache.
     */
    constructor(scheduleEntries) { 
        
        ScheduleEntries.initialize(this, scheduleEntries);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, scheduleEntries) { 
        obj['scheduleEntries'] = scheduleEntries;
    }

    /**
     * Constructs a <code>ScheduleEntries</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ScheduleEntries} obj Optional instance to populate.
     * @return {module:model/ScheduleEntries} The populated <code>ScheduleEntries</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ScheduleEntries();

            if (data.hasOwnProperty('scheduleEntries')) {
                obj['scheduleEntries'] = ApiClient.convertToType(data['scheduleEntries'], [ScheduleEntry]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ScheduleEntries</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ScheduleEntries</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ScheduleEntries.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['scheduleEntries']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['scheduleEntries'])) {
                throw new Error("Expected the field `scheduleEntries` to be an array in the JSON data but got " + data['scheduleEntries']);
            }
            // validate the optional field `scheduleEntries` (array)
            for (const item of data['scheduleEntries']) {
                ScheduleEntry.validateJSON(item);
            };
        }

        return true;
    }


}

ScheduleEntries.RequiredProperties = ["scheduleEntries"];

/**
 * List of patch schedules for a Redis cache.
 * @member {Array.<module:model/ScheduleEntry>} scheduleEntries
 */
ScheduleEntries.prototype['scheduleEntries'] = undefined;






export default ScheduleEntries;

