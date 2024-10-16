/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ClaimNetworkDevicesRequest model module.
 * @module model/ClaimNetworkDevicesRequest
 * @version 0.0.0-streaming
 */
class ClaimNetworkDevicesRequest {
    /**
     * Constructs a new <code>ClaimNetworkDevicesRequest</code>.
     * @alias module:model/ClaimNetworkDevicesRequest
     */
    constructor() { 
        
        ClaimNetworkDevicesRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ClaimNetworkDevicesRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ClaimNetworkDevicesRequest} obj Optional instance to populate.
     * @return {module:model/ClaimNetworkDevicesRequest} The populated <code>ClaimNetworkDevicesRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ClaimNetworkDevicesRequest();

            if (data.hasOwnProperty('serial')) {
                obj['serial'] = ApiClient.convertToType(data['serial'], 'String');
            }
            if (data.hasOwnProperty('serials')) {
                obj['serials'] = ApiClient.convertToType(data['serials'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ClaimNetworkDevicesRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ClaimNetworkDevicesRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['serial'] && !(typeof data['serial'] === 'string' || data['serial'] instanceof String)) {
            throw new Error("Expected the field `serial` to be a primitive type in the JSON string but got " + data['serial']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['serials'])) {
            throw new Error("Expected the field `serials` to be an array in the JSON data but got " + data['serials']);
        }

        return true;
    }


}



/**
 * [DEPRECATED] The serial of a device to claim
 * @member {String} serial
 */
ClaimNetworkDevicesRequest.prototype['serial'] = undefined;

/**
 * A list of serials of devices to claim
 * @member {Array.<String>} serials
 */
ClaimNetworkDevicesRequest.prototype['serials'] = undefined;






export default ClaimNetworkDevicesRequest;

