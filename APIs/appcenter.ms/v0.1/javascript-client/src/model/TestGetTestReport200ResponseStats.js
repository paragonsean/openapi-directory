/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The TestGetTestReport200ResponseStats model module.
 * @module model/TestGetTestReport200ResponseStats
 * @version v0.1
 */
class TestGetTestReport200ResponseStats {
    /**
     * Constructs a new <code>TestGetTestReport200ResponseStats</code>.
     * @alias module:model/TestGetTestReport200ResponseStats
     * @param devices {Number} 
     * @param devicesFailed {Number} 
     * @param devicesFinished {Number} 
     * @param devicesNotRunned {Number} 
     * @param devicesSkipped {Number} 
     * @param failed {Number} 
     * @param filesize {Number} 
     * @param os {Number} 
     * @param passed {Number} 
     * @param skipped {Number} 
     * @param stepCount {Number} 
     * @param total {Number} 
     * @param totalDeviceMinutes {Number} 
     */
    constructor(devices, devicesFailed, devicesFinished, devicesNotRunned, devicesSkipped, failed, filesize, os, passed, skipped, stepCount, total, totalDeviceMinutes) { 
        
        TestGetTestReport200ResponseStats.initialize(this, devices, devicesFailed, devicesFinished, devicesNotRunned, devicesSkipped, failed, filesize, os, passed, skipped, stepCount, total, totalDeviceMinutes);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, devices, devicesFailed, devicesFinished, devicesNotRunned, devicesSkipped, failed, filesize, os, passed, skipped, stepCount, total, totalDeviceMinutes) { 
        obj['devices'] = devices;
        obj['devices_failed'] = devicesFailed;
        obj['devices_finished'] = devicesFinished;
        obj['devices_not_runned'] = devicesNotRunned;
        obj['devices_skipped'] = devicesSkipped;
        obj['failed'] = failed;
        obj['filesize'] = filesize;
        obj['os'] = os;
        obj['passed'] = passed;
        obj['skipped'] = skipped;
        obj['step_count'] = stepCount;
        obj['total'] = total;
        obj['totalDeviceMinutes'] = totalDeviceMinutes;
    }

    /**
     * Constructs a <code>TestGetTestReport200ResponseStats</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TestGetTestReport200ResponseStats} obj Optional instance to populate.
     * @return {module:model/TestGetTestReport200ResponseStats} The populated <code>TestGetTestReport200ResponseStats</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TestGetTestReport200ResponseStats();

            if (data.hasOwnProperty('artifacts')) {
                obj['artifacts'] = ApiClient.convertToType(data['artifacts'], {'String': 'String'});
            }
            if (data.hasOwnProperty('devices')) {
                obj['devices'] = ApiClient.convertToType(data['devices'], 'Number');
            }
            if (data.hasOwnProperty('devices_failed')) {
                obj['devices_failed'] = ApiClient.convertToType(data['devices_failed'], 'Number');
            }
            if (data.hasOwnProperty('devices_finished')) {
                obj['devices_finished'] = ApiClient.convertToType(data['devices_finished'], 'Number');
            }
            if (data.hasOwnProperty('devices_not_runned')) {
                obj['devices_not_runned'] = ApiClient.convertToType(data['devices_not_runned'], 'Number');
            }
            if (data.hasOwnProperty('devices_skipped')) {
                obj['devices_skipped'] = ApiClient.convertToType(data['devices_skipped'], 'Number');
            }
            if (data.hasOwnProperty('failed')) {
                obj['failed'] = ApiClient.convertToType(data['failed'], 'Number');
            }
            if (data.hasOwnProperty('filesize')) {
                obj['filesize'] = ApiClient.convertToType(data['filesize'], 'Number');
            }
            if (data.hasOwnProperty('os')) {
                obj['os'] = ApiClient.convertToType(data['os'], 'Number');
            }
            if (data.hasOwnProperty('passed')) {
                obj['passed'] = ApiClient.convertToType(data['passed'], 'Number');
            }
            if (data.hasOwnProperty('skipped')) {
                obj['skipped'] = ApiClient.convertToType(data['skipped'], 'Number');
            }
            if (data.hasOwnProperty('step_count')) {
                obj['step_count'] = ApiClient.convertToType(data['step_count'], 'Number');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
            if (data.hasOwnProperty('totalDeviceMinutes')) {
                obj['totalDeviceMinutes'] = ApiClient.convertToType(data['totalDeviceMinutes'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TestGetTestReport200ResponseStats</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TestGetTestReport200ResponseStats</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TestGetTestReport200ResponseStats.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

TestGetTestReport200ResponseStats.RequiredProperties = ["devices", "devices_failed", "devices_finished", "devices_not_runned", "devices_skipped", "failed", "filesize", "os", "passed", "skipped", "step_count", "total", "totalDeviceMinutes"];

/**
 * @member {Object.<String, String>} artifacts
 */
TestGetTestReport200ResponseStats.prototype['artifacts'] = undefined;

/**
 * @member {Number} devices
 */
TestGetTestReport200ResponseStats.prototype['devices'] = undefined;

/**
 * @member {Number} devices_failed
 */
TestGetTestReport200ResponseStats.prototype['devices_failed'] = undefined;

/**
 * @member {Number} devices_finished
 */
TestGetTestReport200ResponseStats.prototype['devices_finished'] = undefined;

/**
 * @member {Number} devices_not_runned
 */
TestGetTestReport200ResponseStats.prototype['devices_not_runned'] = undefined;

/**
 * @member {Number} devices_skipped
 */
TestGetTestReport200ResponseStats.prototype['devices_skipped'] = undefined;

/**
 * @member {Number} failed
 */
TestGetTestReport200ResponseStats.prototype['failed'] = undefined;

/**
 * @member {Number} filesize
 */
TestGetTestReport200ResponseStats.prototype['filesize'] = undefined;

/**
 * @member {Number} os
 */
TestGetTestReport200ResponseStats.prototype['os'] = undefined;

/**
 * @member {Number} passed
 */
TestGetTestReport200ResponseStats.prototype['passed'] = undefined;

/**
 * @member {Number} skipped
 */
TestGetTestReport200ResponseStats.prototype['skipped'] = undefined;

/**
 * @member {Number} step_count
 */
TestGetTestReport200ResponseStats.prototype['step_count'] = undefined;

/**
 * @member {Number} total
 */
TestGetTestReport200ResponseStats.prototype['total'] = undefined;

/**
 * @member {Number} totalDeviceMinutes
 */
TestGetTestReport200ResponseStats.prototype['totalDeviceMinutes'] = undefined;






export default TestGetTestReport200ResponseStats;

