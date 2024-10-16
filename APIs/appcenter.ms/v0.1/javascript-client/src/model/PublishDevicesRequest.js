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
 * The PublishDevicesRequest model module.
 * @module model/PublishDevicesRequest
 * @version v0.1
 */
class PublishDevicesRequest {
    /**
     * Constructs a new <code>PublishDevicesRequest</code>.
     * The publising information.
     * @alias module:model/PublishDevicesRequest
     */
    constructor() { 
        
        PublishDevicesRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PublishDevicesRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PublishDevicesRequest} obj Optional instance to populate.
     * @return {module:model/PublishDevicesRequest} The populated <code>PublishDevicesRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PublishDevicesRequest();

            if (data.hasOwnProperty('account_service_connection_id')) {
                obj['account_service_connection_id'] = ApiClient.convertToType(data['account_service_connection_id'], 'String');
            }
            if (data.hasOwnProperty('devices')) {
                obj['devices'] = ApiClient.convertToType(data['devices'], ['String']);
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
            if (data.hasOwnProperty('publish_all_devices')) {
                obj['publish_all_devices'] = ApiClient.convertToType(data['publish_all_devices'], 'Boolean');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PublishDevicesRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PublishDevicesRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['account_service_connection_id'] && !(typeof data['account_service_connection_id'] === 'string' || data['account_service_connection_id'] instanceof String)) {
            throw new Error("Expected the field `account_service_connection_id` to be a primitive type in the JSON string but got " + data['account_service_connection_id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['devices'])) {
            throw new Error("Expected the field `devices` to be an array in the JSON data but got " + data['devices']);
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
PublishDevicesRequest.prototype['account_service_connection_id'] = undefined;

/**
 * Array of device UDID's to be published to the Apple Developer account.
 * @member {Array.<String>} devices
 */
PublishDevicesRequest.prototype['devices'] = undefined;

/**
 * The password for the Apple Developer account to publish the devices to.
 * @member {String} password
 */
PublishDevicesRequest.prototype['password'] = undefined;

/**
 * When set to true, all unprovisioned devices will be published to the Apple Developer account.  When false, only the provided devices will be published to the Apple Developer account.
 * @member {Boolean} publish_all_devices
 */
PublishDevicesRequest.prototype['publish_all_devices'] = undefined;

/**
 * The username for the Apple Developer account to publish the devices to.
 * @member {String} username
 */
PublishDevicesRequest.prototype['username'] = undefined;






export default PublishDevicesRequest;

