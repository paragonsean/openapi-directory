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
import GetNetworkApplianceSsids200ResponseInnerRadiusServersInner from './GetNetworkApplianceSsids200ResponseInnerRadiusServersInner';

/**
 * The GetNetworkApplianceSsids200ResponseInner model module.
 * @module model/GetNetworkApplianceSsids200ResponseInner
 * @version 1.32.0
 */
class GetNetworkApplianceSsids200ResponseInner {
    /**
     * Constructs a new <code>GetNetworkApplianceSsids200ResponseInner</code>.
     * @alias module:model/GetNetworkApplianceSsids200ResponseInner
     */
    constructor() { 
        
        GetNetworkApplianceSsids200ResponseInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkApplianceSsids200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkApplianceSsids200ResponseInner} obj Optional instance to populate.
     * @return {module:model/GetNetworkApplianceSsids200ResponseInner} The populated <code>GetNetworkApplianceSsids200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkApplianceSsids200ResponseInner();

            if (data.hasOwnProperty('authMode')) {
                obj['authMode'] = ApiClient.convertToType(data['authMode'], 'String');
            }
            if (data.hasOwnProperty('defaultVlanId')) {
                obj['defaultVlanId'] = ApiClient.convertToType(data['defaultVlanId'], 'Number');
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('encryptionMode')) {
                obj['encryptionMode'] = ApiClient.convertToType(data['encryptionMode'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('number')) {
                obj['number'] = ApiClient.convertToType(data['number'], 'Number');
            }
            if (data.hasOwnProperty('radiusServers')) {
                obj['radiusServers'] = ApiClient.convertToType(data['radiusServers'], [GetNetworkApplianceSsids200ResponseInnerRadiusServersInner]);
            }
            if (data.hasOwnProperty('visible')) {
                obj['visible'] = ApiClient.convertToType(data['visible'], 'Boolean');
            }
            if (data.hasOwnProperty('wpaEncryptionMode')) {
                obj['wpaEncryptionMode'] = ApiClient.convertToType(data['wpaEncryptionMode'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkApplianceSsids200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkApplianceSsids200ResponseInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['authMode'] && !(typeof data['authMode'] === 'string' || data['authMode'] instanceof String)) {
            throw new Error("Expected the field `authMode` to be a primitive type in the JSON string but got " + data['authMode']);
        }
        // ensure the json data is a string
        if (data['encryptionMode'] && !(typeof data['encryptionMode'] === 'string' || data['encryptionMode'] instanceof String)) {
            throw new Error("Expected the field `encryptionMode` to be a primitive type in the JSON string but got " + data['encryptionMode']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        if (data['radiusServers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['radiusServers'])) {
                throw new Error("Expected the field `radiusServers` to be an array in the JSON data but got " + data['radiusServers']);
            }
            // validate the optional field `radiusServers` (array)
            for (const item of data['radiusServers']) {
                GetNetworkApplianceSsids200ResponseInnerRadiusServersInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['wpaEncryptionMode'] && !(typeof data['wpaEncryptionMode'] === 'string' || data['wpaEncryptionMode'] instanceof String)) {
            throw new Error("Expected the field `wpaEncryptionMode` to be a primitive type in the JSON string but got " + data['wpaEncryptionMode']);
        }

        return true;
    }


}



/**
 * The association control method for the SSID.
 * @member {String} authMode
 */
GetNetworkApplianceSsids200ResponseInner.prototype['authMode'] = undefined;

/**
 * The VLAN ID of the VLAN associated to this SSID.
 * @member {Number} defaultVlanId
 */
GetNetworkApplianceSsids200ResponseInner.prototype['defaultVlanId'] = undefined;

/**
 * Whether or not the SSID is enabled.
 * @member {Boolean} enabled
 */
GetNetworkApplianceSsids200ResponseInner.prototype['enabled'] = undefined;

/**
 * The psk encryption mode for the SSID.
 * @member {String} encryptionMode
 */
GetNetworkApplianceSsids200ResponseInner.prototype['encryptionMode'] = undefined;

/**
 * The name of the SSID.
 * @member {String} name
 */
GetNetworkApplianceSsids200ResponseInner.prototype['name'] = undefined;

/**
 * The number of the SSID.
 * @member {Number} number
 */
GetNetworkApplianceSsids200ResponseInner.prototype['number'] = undefined;

/**
 * The RADIUS 802.1x servers to be used for authentication.
 * @member {Array.<module:model/GetNetworkApplianceSsids200ResponseInnerRadiusServersInner>} radiusServers
 */
GetNetworkApplianceSsids200ResponseInner.prototype['radiusServers'] = undefined;

/**
 * Boolean indicating whether the MX should advertise or hide this SSID.
 * @member {Boolean} visible
 */
GetNetworkApplianceSsids200ResponseInner.prototype['visible'] = undefined;

/**
 * WPA encryption mode for the SSID.
 * @member {String} wpaEncryptionMode
 */
GetNetworkApplianceSsids200ResponseInner.prototype['wpaEncryptionMode'] = undefined;






export default GetNetworkApplianceSsids200ResponseInner;

