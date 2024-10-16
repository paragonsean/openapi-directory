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
import UpdateDevicesRequestDestinationsInner from './UpdateDevicesRequestDestinationsInner';

/**
 * The UpdateDevicesRequest model module.
 * @module model/UpdateDevicesRequest
 * @version v0.1
 */
class UpdateDevicesRequest {
    /**
     * Constructs a new <code>UpdateDevicesRequest</code>.
     * Information required to publish devices to the Apple Developer account and resign the application.
     * @alias module:model/UpdateDevicesRequest
     */
    constructor() { 
        
        UpdateDevicesRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateDevicesRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateDevicesRequest} obj Optional instance to populate.
     * @return {module:model/UpdateDevicesRequest} The populated <code>UpdateDevicesRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateDevicesRequest();

            if (data.hasOwnProperty('account_service_connection_id')) {
                obj['account_service_connection_id'] = ApiClient.convertToType(data['account_service_connection_id'], 'String');
            }
            if (data.hasOwnProperty('destinations')) {
                obj['destinations'] = ApiClient.convertToType(data['destinations'], [UpdateDevicesRequestDestinationsInner]);
            }
            if (data.hasOwnProperty('devices')) {
                obj['devices'] = ApiClient.convertToType(data['devices'], ['String']);
            }
            if (data.hasOwnProperty('p12_base64')) {
                obj['p12_base64'] = ApiClient.convertToType(data['p12_base64'], 'String');
            }
            if (data.hasOwnProperty('p12_password')) {
                obj['p12_password'] = ApiClient.convertToType(data['p12_password'], 'String');
            }
            if (data.hasOwnProperty('p12_service_connection_id')) {
                obj['p12_service_connection_id'] = ApiClient.convertToType(data['p12_service_connection_id'], 'String');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
            if (data.hasOwnProperty('publish_all_devices')) {
                obj['publish_all_devices'] = ApiClient.convertToType(data['publish_all_devices'], 'Boolean');
            }
            if (data.hasOwnProperty('release_id')) {
                obj['release_id'] = ApiClient.convertToType(data['release_id'], 'Number');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateDevicesRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateDevicesRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['account_service_connection_id'] && !(typeof data['account_service_connection_id'] === 'string' || data['account_service_connection_id'] instanceof String)) {
            throw new Error("Expected the field `account_service_connection_id` to be a primitive type in the JSON string but got " + data['account_service_connection_id']);
        }
        if (data['destinations']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['destinations'])) {
                throw new Error("Expected the field `destinations` to be an array in the JSON data but got " + data['destinations']);
            }
            // validate the optional field `destinations` (array)
            for (const item of data['destinations']) {
                UpdateDevicesRequestDestinationsInner.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['devices'])) {
            throw new Error("Expected the field `devices` to be an array in the JSON data but got " + data['devices']);
        }
        // ensure the json data is a string
        if (data['p12_base64'] && !(typeof data['p12_base64'] === 'string' || data['p12_base64'] instanceof String)) {
            throw new Error("Expected the field `p12_base64` to be a primitive type in the JSON string but got " + data['p12_base64']);
        }
        // ensure the json data is a string
        if (data['p12_password'] && !(typeof data['p12_password'] === 'string' || data['p12_password'] instanceof String)) {
            throw new Error("Expected the field `p12_password` to be a primitive type in the JSON string but got " + data['p12_password']);
        }
        // ensure the json data is a string
        if (data['p12_service_connection_id'] && !(typeof data['p12_service_connection_id'] === 'string' || data['p12_service_connection_id'] instanceof String)) {
            throw new Error("Expected the field `p12_service_connection_id` to be a primitive type in the JSON string but got " + data['p12_service_connection_id']);
        }
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }

        return true;
    }


}



/**
 * The service_connection_id of the stored Apple credentials instead of username, password.
 * @member {String} account_service_connection_id
 */
UpdateDevicesRequest.prototype['account_service_connection_id'] = undefined;

/**
 * Array of distribution groups that the devices should be provisioned from.
 * @member {Array.<module:model/UpdateDevicesRequestDestinationsInner>} destinations
 */
UpdateDevicesRequest.prototype['destinations'] = undefined;

/**
 * Array of device UDID's to be published to the Apple Developer account.
 * @member {Array.<String>} devices
 */
UpdateDevicesRequest.prototype['devices'] = undefined;

/**
 * The certificate to use for resigning the application with the updated provisioning profiles.
 * @member {String} p12_base64
 */
UpdateDevicesRequest.prototype['p12_base64'] = undefined;

/**
 * The password certificate if one is needed.
 * @member {String} p12_password
 */
UpdateDevicesRequest.prototype['p12_password'] = undefined;

/**
 * The service_connection_id of the stored Apple certificate instead of p12_base64 value.
 * @member {String} p12_service_connection_id
 */
UpdateDevicesRequest.prototype['p12_service_connection_id'] = undefined;

/**
 * The password for the Apple Developer account to publish the devices to.
 * @member {String} password
 */
UpdateDevicesRequest.prototype['password'] = undefined;

/**
 * When set to true, all unprovisioned devices will be published to the Apple Developer account.  When false, only the provided devices will be published to the Apple Developer account.
 * @member {Boolean} publish_all_devices
 */
UpdateDevicesRequest.prototype['publish_all_devices'] = undefined;

/**
 * When provided, will update the provided release with the new set of devices. By default the latest release of the distribution group is used when this property is omitted. If `release_id` is passed in the path, there is no need to pass in the body as well.
 * @member {Number} release_id
 */
UpdateDevicesRequest.prototype['release_id'] = undefined;

/**
 * The username for the Apple Developer account to publish the devices to.
 * @member {String} username
 */
UpdateDevicesRequest.prototype['username'] = undefined;






export default UpdateDevicesRequest;

