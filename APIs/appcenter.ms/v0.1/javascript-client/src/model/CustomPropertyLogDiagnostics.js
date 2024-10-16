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
 * The CustomPropertyLogDiagnostics model module.
 * @module model/CustomPropertyLogDiagnostics
 * @version v0.1
 */
class CustomPropertyLogDiagnostics {
    /**
     * Constructs a new <code>CustomPropertyLogDiagnostics</code>.
     * Set or remove custom properties.
     * @alias module:model/CustomPropertyLogDiagnostics
     * @param device {module:model/AnalyticsGenericLogFlow200ResponseLogsInnerDevice} 
     * @param installId {String} Install ID. 
     * @param timestamp {Date} Log creation timestamp. 
     * @param type {module:model/CustomPropertyLogDiagnostics.TypeEnum} Log type. 
     */
    constructor(device, installId, timestamp, type) { 
        
        CustomPropertyLogDiagnostics.initialize(this, device, installId, timestamp, type);
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
     * Constructs a <code>CustomPropertyLogDiagnostics</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CustomPropertyLogDiagnostics} obj Optional instance to populate.
     * @return {module:model/CustomPropertyLogDiagnostics} The populated <code>CustomPropertyLogDiagnostics</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CustomPropertyLogDiagnostics();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ApiClient.convertToType(data['properties'], [Object]);
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
     * Validates the JSON data with respect to <code>CustomPropertyLogDiagnostics</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CustomPropertyLogDiagnostics</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CustomPropertyLogDiagnostics.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['properties']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['properties'])) {
                throw new Error("Expected the field `properties` to be an array in the JSON data but got " + data['properties']);
            }
            // validate the optional field `properties` (array)
            for (const item of data['properties']) {
                Object.validateJSON(item);
            };
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

CustomPropertyLogDiagnostics.RequiredProperties = ["device", "install_id", "timestamp", "type"];

/**
 * Custom property changes.
 * @member {Array.<Object>} properties
 */
CustomPropertyLogDiagnostics.prototype['properties'] = undefined;

/**
 * @member {module:model/AnalyticsGenericLogFlow200ResponseLogsInnerDevice} device
 */
CustomPropertyLogDiagnostics.prototype['device'] = undefined;

/**
 * Install ID. 
 * @member {String} install_id
 */
CustomPropertyLogDiagnostics.prototype['install_id'] = undefined;

/**
 * Log creation timestamp. 
 * @member {Date} timestamp
 */
CustomPropertyLogDiagnostics.prototype['timestamp'] = undefined;

/**
 * Log type. 
 * @member {module:model/CustomPropertyLogDiagnostics.TypeEnum} type
 */
CustomPropertyLogDiagnostics.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
CustomPropertyLogDiagnostics['TypeEnum'] = {

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
     * value: "push_installation"
     * @const
     */
    "push_installation": "push_installation",

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



export default CustomPropertyLogDiagnostics;

