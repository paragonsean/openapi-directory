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
 * The MemberDevicesInfoResponse model module.
 * @module model/MemberDevicesInfoResponse
 * @version v0.1
 */
class MemberDevicesInfoResponse {
    /**
     * Constructs a new <code>MemberDevicesInfoResponse</code>.
     * The information for a single distribution group member and their ios device
     * @alias module:model/MemberDevicesInfoResponse
     * @param deviceName {String} The device description, in the format \"iPhone 7 Plus (A1784)\"
     * @param email {String} The email address of the user
     * @param id {String} The unique id (UUID) of the user
     * @param model {String} The model identifier of the device, in the format iDeviceM,N
     * @param osBuild {String} The last known OS version running on the device
     * @param osVersion {String} The last known OS version running on the device
     * @param status {String} The provisioning status of the device.
     * @param udid {String} The Unique Device IDentifier of the device
     */
    constructor(deviceName, email, id, model, osBuild, osVersion, status, udid) { 
        
        MemberDevicesInfoResponse.initialize(this, deviceName, email, id, model, osBuild, osVersion, status, udid);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, deviceName, email, id, model, osBuild, osVersion, status, udid) { 
        obj['device_name'] = deviceName;
        obj['email'] = email;
        obj['id'] = id;
        obj['model'] = model;
        obj['os_build'] = osBuild;
        obj['os_version'] = osVersion;
        obj['status'] = status;
        obj['udid'] = udid;
    }

    /**
     * Constructs a <code>MemberDevicesInfoResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MemberDevicesInfoResponse} obj Optional instance to populate.
     * @return {module:model/MemberDevicesInfoResponse} The populated <code>MemberDevicesInfoResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MemberDevicesInfoResponse();

            if (data.hasOwnProperty('avatar_url')) {
                obj['avatar_url'] = ApiClient.convertToType(data['avatar_url'], 'String');
            }
            if (data.hasOwnProperty('can_change_password')) {
                obj['can_change_password'] = ApiClient.convertToType(data['can_change_password'], 'Boolean');
            }
            if (data.hasOwnProperty('device_name')) {
                obj['device_name'] = ApiClient.convertToType(data['device_name'], 'String');
            }
            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('full_device_name')) {
                obj['full_device_name'] = ApiClient.convertToType(data['full_device_name'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('imei')) {
                obj['imei'] = ApiClient.convertToType(data['imei'], 'String');
            }
            if (data.hasOwnProperty('invite_pending')) {
                obj['invite_pending'] = ApiClient.convertToType(data['invite_pending'], 'Boolean');
            }
            if (data.hasOwnProperty('model')) {
                obj['model'] = ApiClient.convertToType(data['model'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
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
     * Validates the JSON data with respect to <code>MemberDevicesInfoResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MemberDevicesInfoResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of MemberDevicesInfoResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['avatar_url'] && !(typeof data['avatar_url'] === 'string' || data['avatar_url'] instanceof String)) {
            throw new Error("Expected the field `avatar_url` to be a primitive type in the JSON string but got " + data['avatar_url']);
        }
        // ensure the json data is a string
        if (data['device_name'] && !(typeof data['device_name'] === 'string' || data['device_name'] instanceof String)) {
            throw new Error("Expected the field `device_name` to be a primitive type in the JSON string but got " + data['device_name']);
        }
        // ensure the json data is a string
        if (data['display_name'] && !(typeof data['display_name'] === 'string' || data['display_name'] instanceof String)) {
            throw new Error("Expected the field `display_name` to be a primitive type in the JSON string but got " + data['display_name']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['full_device_name'] && !(typeof data['full_device_name'] === 'string' || data['full_device_name'] instanceof String)) {
            throw new Error("Expected the field `full_device_name` to be a primitive type in the JSON string but got " + data['full_device_name']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
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
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
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

MemberDevicesInfoResponse.RequiredProperties = ["device_name", "email", "id", "model", "os_build", "os_version", "status", "udid"];

/**
 * The avatar URL of the user
 * @member {String} avatar_url
 */
MemberDevicesInfoResponse.prototype['avatar_url'] = undefined;

/**
 * User is required to send an old password in order to change the password.
 * @member {Boolean} can_change_password
 */
MemberDevicesInfoResponse.prototype['can_change_password'] = undefined;

/**
 * The device description, in the format \"iPhone 7 Plus (A1784)\"
 * @member {String} device_name
 */
MemberDevicesInfoResponse.prototype['device_name'] = undefined;

/**
 * The full name of the user. Might for example be first and last name
 * @member {String} display_name
 */
MemberDevicesInfoResponse.prototype['display_name'] = undefined;

/**
 * The email address of the user
 * @member {String} email
 */
MemberDevicesInfoResponse.prototype['email'] = undefined;

/**
 * A combination of the device model name and the owner name.
 * @member {String} full_device_name
 */
MemberDevicesInfoResponse.prototype['full_device_name'] = undefined;

/**
 * The unique id (UUID) of the user
 * @member {String} id
 */
MemberDevicesInfoResponse.prototype['id'] = undefined;

/**
 * The device's International Mobile Equipment Identity number. Always empty or undefined at present.
 * @member {String} imei
 */
MemberDevicesInfoResponse.prototype['imei'] = undefined;

/**
 * Whether the has accepted the invite. Available when an invite is pending, and the value will be \"true\".
 * @member {Boolean} invite_pending
 */
MemberDevicesInfoResponse.prototype['invite_pending'] = undefined;

/**
 * The model identifier of the device, in the format iDeviceM,N
 * @member {String} model
 */
MemberDevicesInfoResponse.prototype['model'] = undefined;

/**
 * The unique name that is used to identify the user.
 * @member {String} name
 */
MemberDevicesInfoResponse.prototype['name'] = undefined;

/**
 * The last known OS version running on the device
 * @member {String} os_build
 */
MemberDevicesInfoResponse.prototype['os_build'] = undefined;

/**
 * The last known OS version running on the device
 * @member {String} os_version
 */
MemberDevicesInfoResponse.prototype['os_version'] = undefined;

/**
 * The user ID of the device owner.
 * @member {String} owner_id
 */
MemberDevicesInfoResponse.prototype['owner_id'] = undefined;

/**
 * Timestamp of when the device was registered in ISO format.
 * @member {String} registered_at
 */
MemberDevicesInfoResponse.prototype['registered_at'] = undefined;

/**
 * The device's serial number. Always empty or undefined at present.
 * @member {String} serial
 */
MemberDevicesInfoResponse.prototype['serial'] = undefined;

/**
 * The provisioning status of the device.
 * @member {String} status
 */
MemberDevicesInfoResponse.prototype['status'] = undefined;

/**
 * The Unique Device IDentifier of the device
 * @member {String} udid
 */
MemberDevicesInfoResponse.prototype['udid'] = undefined;






export default MemberDevicesInfoResponse;

