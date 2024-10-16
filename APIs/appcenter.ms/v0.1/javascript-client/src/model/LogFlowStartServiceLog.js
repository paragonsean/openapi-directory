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
import AnalyticsGenericLogFlow200ResponseLogsInnerDevice from './AnalyticsGenericLogFlow200ResponseLogsInnerDevice';

/**
 * The LogFlowStartServiceLog model module.
 * @module model/LogFlowStartServiceLog
 * @version v0.1
 */
class LogFlowStartServiceLog {
    /**
     * Constructs a new <code>LogFlowStartServiceLog</code>.
     * Describe a AppCenter.Start API call from the SDK.
     * @alias module:model/LogFlowStartServiceLog
     * @param device {module:model/AnalyticsGenericLogFlow200ResponseLogsInnerDevice} 
     * @param installId {String} Install ID. 
     * @param timestamp {Date} Log creation timestamp. 
     * @param type {module:model/LogFlowStartServiceLog.TypeEnum} Log type. 
     */
    constructor(device, installId, timestamp, type) { 
        
        LogFlowStartServiceLog.initialize(this, device, installId, timestamp, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, device, installId, timestamp, type) { 
        obj['device'] = device;
        obj['install_id'] = installId;
        obj['timestamp'] = timestamp;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>LogFlowStartServiceLog</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LogFlowStartServiceLog} obj Optional instance to populate.
     * @return {module:model/LogFlowStartServiceLog} The populated <code>LogFlowStartServiceLog</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LogFlowStartServiceLog();

            if (data.hasOwnProperty('services')) {
                obj['services'] = ApiClient.convertToType(data['services'], ['String']);
            }
            if (data.hasOwnProperty('device')) {
                obj['device'] = AnalyticsGenericLogFlow200ResponseLogsInnerDevice.constructFromObject(data['device']);
            }
            if (data.hasOwnProperty('install_id')) {
                obj['install_id'] = ApiClient.convertToType(data['install_id'], 'String');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Date');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LogFlowStartServiceLog</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LogFlowStartServiceLog</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of LogFlowStartServiceLog.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['services'])) {
            throw new Error("Expected the field `services` to be an array in the JSON data but got " + data['services']);
        }
        // validate the optional field `device`
        if (data['device']) { // data not null
          AnalyticsGenericLogFlow200ResponseLogsInnerDevice.validateJSON(data['device']);
        }
        // ensure the json data is a string
        if (data['install_id'] && !(typeof data['install_id'] === 'string' || data['install_id'] instanceof String)) {
            throw new Error("Expected the field `install_id` to be a primitive type in the JSON string but got " + data['install_id']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

LogFlowStartServiceLog.RequiredProperties = ["device", "install_id", "timestamp", "type"];

/**
 * The list of services of the AppCenter Start API call.
 * @member {Array.<String>} services
 */
LogFlowStartServiceLog.prototype['services'] = undefined;

/**
 * @member {module:model/AnalyticsGenericLogFlow200ResponseLogsInnerDevice} device
 */
LogFlowStartServiceLog.prototype['device'] = undefined;

/**
 * Install ID. 
 * @member {String} install_id
 */
LogFlowStartServiceLog.prototype['install_id'] = undefined;

/**
 * Log creation timestamp. 
 * @member {Date} timestamp
 */
LogFlowStartServiceLog.prototype['timestamp'] = undefined;

/**
 * Log type. 
 * @member {module:model/LogFlowStartServiceLog.TypeEnum} type
 */
LogFlowStartServiceLog.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
LogFlowStartServiceLog['TypeEnum'] = {

    /**
     * value: "event"
     * @const
     */
    "event": "event",

    /**
     * value: "page"
     * @const
     */
    "page": "page",

    /**
     * value: "start_session"
     * @const
     */
    "start_session": "start_session",

    /**
     * value: "error"
     * @const
     */
    "error": "error",

    /**
     * value: "start_service"
     * @const
     */
    "start_service": "start_service",

    /**
     * value: "custom_properties"
     * @const
     */
    "custom_properties": "custom_properties"
};



export default LogFlowStartServiceLog;

