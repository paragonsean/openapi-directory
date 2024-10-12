/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GetNetworkSmDeviceDeviceCommandLogs200ResponseInner model module.
 * @module model/GetNetworkSmDeviceDeviceCommandLogs200ResponseInner
 * @version 1.32.0
 */
class GetNetworkSmDeviceDeviceCommandLogs200ResponseInner {
    /**
     * Constructs a new <code>GetNetworkSmDeviceDeviceCommandLogs200ResponseInner</code>.
     * @alias module:model/GetNetworkSmDeviceDeviceCommandLogs200ResponseInner
     */
    constructor() { 
        
        GetNetworkSmDeviceDeviceCommandLogs200ResponseInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkSmDeviceDeviceCommandLogs200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkSmDeviceDeviceCommandLogs200ResponseInner} obj Optional instance to populate.
     * @return {module:model/GetNetworkSmDeviceDeviceCommandLogs200ResponseInner} The populated <code>GetNetworkSmDeviceDeviceCommandLogs200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkSmDeviceDeviceCommandLogs200ResponseInner();

            if (data.hasOwnProperty('action')) {
                obj['action'] = ApiClient.convertToType(data['action'], 'String');
            }
            if (data.hasOwnProperty('dashboardUser')) {
                obj['dashboardUser'] = ApiClient.convertToType(data['dashboardUser'], 'String');
            }
            if (data.hasOwnProperty('details')) {
                obj['details'] = ApiClient.convertToType(data['details'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('ts')) {
                obj['ts'] = ApiClient.convertToType(data['ts'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkSmDeviceDeviceCommandLogs200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkSmDeviceDeviceCommandLogs200ResponseInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['action'] && !(typeof data['action'] === 'string' || data['action'] instanceof String)) {
            throw new Error("Expected the field `action` to be a primitive type in the JSON string but got " + data['action']);
        }
        // ensure the json data is a string
        if (data['dashboardUser'] && !(typeof data['dashboardUser'] === 'string' || data['dashboardUser'] instanceof String)) {
            throw new Error("Expected the field `dashboardUser` to be a primitive type in the JSON string but got " + data['dashboardUser']);
        }
        // ensure the json data is a string
        if (data['details'] && !(typeof data['details'] === 'string' || data['details'] instanceof String)) {
            throw new Error("Expected the field `details` to be a primitive type in the JSON string but got " + data['details']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['ts'] && !(typeof data['ts'] === 'string' || data['ts'] instanceof String)) {
            throw new Error("Expected the field `ts` to be a primitive type in the JSON string but got " + data['ts']);
        }

        return true;
    }


}



/**
 * The type of command sent to the device.
 * @member {String} action
 */
GetNetworkSmDeviceDeviceCommandLogs200ResponseInner.prototype['action'] = undefined;

/**
 * The Meraki dashboard user who initiated the command.
 * @member {String} dashboardUser
 */
GetNetworkSmDeviceDeviceCommandLogs200ResponseInner.prototype['dashboardUser'] = undefined;

/**
 * A JSON string object containing command details.
 * @member {String} details
 */
GetNetworkSmDeviceDeviceCommandLogs200ResponseInner.prototype['details'] = undefined;

/**
 * The name of the device to which the command is sent.
 * @member {String} name
 */
GetNetworkSmDeviceDeviceCommandLogs200ResponseInner.prototype['name'] = undefined;

/**
 * The time the command was sent to the device.
 * @member {String} ts
 */
GetNetworkSmDeviceDeviceCommandLogs200ResponseInner.prototype['ts'] = undefined;






export default GetNetworkSmDeviceDeviceCommandLogs200ResponseInner;

