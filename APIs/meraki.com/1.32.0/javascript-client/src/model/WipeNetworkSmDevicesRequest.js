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
 * The WipeNetworkSmDevicesRequest model module.
 * @module model/WipeNetworkSmDevicesRequest
 * @version 1.32.0
 */
class WipeNetworkSmDevicesRequest {
    /**
     * Constructs a new <code>WipeNetworkSmDevicesRequest</code>.
     * @alias module:model/WipeNetworkSmDevicesRequest
     */
    constructor() { 
        
        WipeNetworkSmDevicesRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>WipeNetworkSmDevicesRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WipeNetworkSmDevicesRequest} obj Optional instance to populate.
     * @return {module:model/WipeNetworkSmDevicesRequest} The populated <code>WipeNetworkSmDevicesRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WipeNetworkSmDevicesRequest();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('pin')) {
                obj['pin'] = ApiClient.convertToType(data['pin'], 'Number');
            }
            if (data.hasOwnProperty('serial')) {
                obj['serial'] = ApiClient.convertToType(data['serial'], 'String');
            }
            if (data.hasOwnProperty('wifiMac')) {
                obj['wifiMac'] = ApiClient.convertToType(data['wifiMac'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WipeNetworkSmDevicesRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WipeNetworkSmDevicesRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['serial'] && !(typeof data['serial'] === 'string' || data['serial'] instanceof String)) {
            throw new Error("Expected the field `serial` to be a primitive type in the JSON string but got " + data['serial']);
        }
        // ensure the json data is a string
        if (data['wifiMac'] && !(typeof data['wifiMac'] === 'string' || data['wifiMac'] instanceof String)) {
            throw new Error("Expected the field `wifiMac` to be a primitive type in the JSON string but got " + data['wifiMac']);
        }

        return true;
    }


}



/**
 * The id of the device to be wiped.
 * @member {String} id
 */
WipeNetworkSmDevicesRequest.prototype['id'] = undefined;

/**
 * The pin number (a six digit value) for wiping a macOS device. Required only for macOS devices.
 * @member {Number} pin
 */
WipeNetworkSmDevicesRequest.prototype['pin'] = undefined;

/**
 * The serial of the device to be wiped.
 * @member {String} serial
 */
WipeNetworkSmDevicesRequest.prototype['serial'] = undefined;

/**
 * The wifiMac of the device to be wiped.
 * @member {String} wifiMac
 */
WipeNetworkSmDevicesRequest.prototype['wifiMac'] = undefined;






export default WipeNetworkSmDevicesRequest;

