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
 * The GetNetworkSmDeviceWlanLists200ResponseInner model module.
 * @module model/GetNetworkSmDeviceWlanLists200ResponseInner
 * @version 1.32.0
 */
class GetNetworkSmDeviceWlanLists200ResponseInner {
    /**
     * Constructs a new <code>GetNetworkSmDeviceWlanLists200ResponseInner</code>.
     * @alias module:model/GetNetworkSmDeviceWlanLists200ResponseInner
     */
    constructor() { 
        
        GetNetworkSmDeviceWlanLists200ResponseInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkSmDeviceWlanLists200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkSmDeviceWlanLists200ResponseInner} obj Optional instance to populate.
     * @return {module:model/GetNetworkSmDeviceWlanLists200ResponseInner} The populated <code>GetNetworkSmDeviceWlanLists200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkSmDeviceWlanLists200ResponseInner();

            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('xml')) {
                obj['xml'] = ApiClient.convertToType(data['xml'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkSmDeviceWlanLists200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkSmDeviceWlanLists200ResponseInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['createdAt'] && !(typeof data['createdAt'] === 'string' || data['createdAt'] instanceof String)) {
            throw new Error("Expected the field `createdAt` to be a primitive type in the JSON string but got " + data['createdAt']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['xml'] && !(typeof data['xml'] === 'string' || data['xml'] instanceof String)) {
            throw new Error("Expected the field `xml` to be a primitive type in the JSON string but got " + data['xml']);
        }

        return true;
    }


}



/**
 * When the Meraki record for the wlanList was created.
 * @member {String} createdAt
 */
GetNetworkSmDeviceWlanLists200ResponseInner.prototype['createdAt'] = undefined;

/**
 * The Meraki managed Id of the wlanList record.
 * @member {String} id
 */
GetNetworkSmDeviceWlanLists200ResponseInner.prototype['id'] = undefined;

/**
 * An XML string containing the WLAN List for the device.
 * @member {String} xml
 */
GetNetworkSmDeviceWlanLists200ResponseInner.prototype['xml'] = undefined;






export default GetNetworkSmDeviceWlanLists200ResponseInner;

