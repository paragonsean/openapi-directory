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
 * The DeviceInfoResponse model module.
 * @module model/DeviceInfoResponse
 * @version v0.1
 */
class DeviceInfoResponse {
    /**
     * Constructs a new <code>DeviceInfoResponse</code>.
     * The information for a single iOS device
     * @alias module:model/DeviceInfoResponse
     * @param deviceName {String} The device description, in the format \"iPhone 7 Plus (A1784)\"
     * @param model {String} The model identifier of the device, in the format iDeviceM,N
     * @param osBuild {String} The last known OS version running on the device
     * @param osVersion {String} The last known OS version running on the device
     * @param status {String} The provisioning status of the device.
     * @param udid {String} The Unique Device IDentifier of the device
     */
    constructor(deviceName, model, osBuild, osVersion, status, udid) { 
        
        DeviceInfoResponse.initialize(this, deviceName, model, osBuild, osVersion, status, udid);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, deviceName, model, osBuild, osVersion, status, udid) { 
        obj['device_name'] = deviceName;
        obj['model'] = model;
        obj['os_build'] = osBuild;
        obj['os_version'] = osVersion;
        obj['status'] = status;
        obj['udid'] = udid;
    }

    /**
     * Constructs a <code>DeviceInfoResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeviceInfoResponse} obj Optional instance to populate.
     * @return {module:model/DeviceInfoResponse} The populated <code>DeviceInfoResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeviceInfoResponse();

            if (data.hasOwnProperty('device_name')) {
                obj['device_name'] = ApiClient.convertToType(data['device_name'], 'String');
            }
            if (data.hasOwnProperty('full_device_name')) {
                obj['full_device_name'] = ApiClient.convertToType(data['full_device_name'], 'String');
            }
            if (data.hasOwnProperty('imei')) {
                obj['imei'] = ApiClient.convertToType(data['imei'], 'String');
            }
            if (data.hasOwnProperty('model')) {
                obj['model'] = ApiClient.convertToType(data['model'], 'String');
            }
            if (data.hasOwnProperty('os_build')) {
                obj['os_build'] = ApiClient.convertToType(data['os_build'], 'String');
            }
            if (data.hasOwnProperty('os_version')) {
                obj['os_version'] = ApiClient.convertToType(data['os_version'], 'String');
            }
            if (data.hasOwnProperty('owner_id')) {
                obj['owner_id'] = ApiClient.convertToType(data['owner_id'], 'String');
            }
            if (data.hasOwnProperty('registered_at')) {
                obj['registered_at'] = ApiClient.convertToType(data['registered_at'], 'String');
            }
            if (data.hasOwnProperty('serial')) {
                obj['serial'] = ApiClient.convertToType(data['serial'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('udid')) {
                obj['udid'] = ApiClient.convertToType(data['udid'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeviceInfoResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeviceInfoResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DeviceInfoResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['device_name'] && !(typeof data['device_name'] === 'string' || data['device_name'] instanceof String)) {
            throw new Error("Expected the field `device_name` to be a primitive type in the JSON string but got " + data['device_name']);
        }
        // ensure the json data is a string
        if (data['full_device_name'] && !(typeof data['full_device_name'] === 'string' || data['full_device_name'] instanceof String)) {
            throw new Error("Expected the field `full_device_name` to be a primitive type in the JSON string but got " + data['full_device_name']);
        }
        // ensure the json data is a string
        if (data['imei'] && !(typeof data['imei'] === 'string' || data['imei'] instanceof String)) {
            throw new Error("Expected the field `imei` to be a primitive type in the JSON string but got " + data['imei']);
        }
        // ensure the json data is a string
        if (data['model'] && !(typeof data['model'] === 'string' || data['model'] instanceof String)) {
            throw new Error("Expected the field `model` to be a primitive type in the JSON string but got " + data['model']);
        }
        // ensure the json data is a string
        if (data['os_build'] && !(typeof data['os_build'] === 'string' || data['os_build'] instanceof String)) {
            throw new Error("Expected the field `os_build` to be a primitive type in the JSON string but got " + data['os_build']);
        }
        // ensure the json data is a string
        if (data['os_version'] && !(typeof data['os_version'] === 'string' || data['os_version'] instanceof String)) {
            throw new Error("Expected the field `os_version` to be a primitive type in the JSON string but got " + data['os_version']);
        }
        // ensure the json data is a string
        if (data['owner_id'] && !(typeof data['owner_id'] === 'string' || data['owner_id'] instanceof String)) {
            throw new Error("Expected the field `owner_id` to be a primitive type in the JSON string but got " + data['owner_id']);
        }
        // ensure the json data is a string
        if (data['registered_at'] && !(typeof data['registered_at'] === 'string' || data['registered_at'] instanceof String)) {
            throw new Error("Expected the field `registered_at` to be a primitive type in the JSON string but got " + data['registered_at']);
        }
        // ensure the json data is a string
        if (data['serial'] && !(typeof data['serial'] === 'string' || data['serial'] instanceof String)) {
            throw new Error("Expected the field `serial` to be a primitive type in the JSON string but got " + data['serial']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['udid'] && !(typeof data['udid'] === 'string' || data['udid'] instanceof String)) {
            throw new Error("Expected the field `udid` to be a primitive type in the JSON string but got " + data['udid']);
        }

        return true;
    }


}

DeviceInfoResponse.RequiredProperties = ["device_name", "model", "os_build", "os_version", "status", "udid"];

/**
 * The device description, in the format \"iPhone 7 Plus (A1784)\"
 * @member {String} device_name
 */
DeviceInfoResponse.prototype['device_name'] = undefined;

/**
 * A combination of the device model name and the owner name.
 * @member {String} full_device_name
 */
DeviceInfoResponse.prototype['full_device_name'] = undefined;

/**
 * The device's International Mobile Equipment Identity number. Always empty or undefined at present.
 * @member {String} imei
 */
DeviceInfoResponse.prototype['imei'] = undefined;

/**
 * The model identifier of the device, in the format iDeviceM,N
 * @member {String} model
 */
DeviceInfoResponse.prototype['model'] = undefined;

/**
 * The last known OS version running on the device
 * @member {String} os_build
 */
DeviceInfoResponse.prototype['os_build'] = undefined;

/**
 * The last known OS version running on the device
 * @member {String} os_version
 */
DeviceInfoResponse.prototype['os_version'] = undefined;

/**
 * The user ID of the device owner.
 * @member {String} owner_id
 */
DeviceInfoResponse.prototype['owner_id'] = undefined;

/**
 * Timestamp of when the device was registered in ISO format.
 * @member {String} registered_at
 */
DeviceInfoResponse.prototype['registered_at'] = undefined;

/**
 * The device's serial number. Always empty or undefined at present.
 * @member {String} serial
 */
DeviceInfoResponse.prototype['serial'] = undefined;

/**
 * The provisioning status of the device.
 * @member {String} status
 */
DeviceInfoResponse.prototype['status'] = undefined;

/**
 * The Unique Device IDentifier of the device
 * @member {String} udid
 */
DeviceInfoResponse.prototype['udid'] = undefined;






export default DeviceInfoResponse;

