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
import UpdateNetworkApplianceSsidRequestDhcpEnforcedDeauthentication from './UpdateNetworkApplianceSsidRequestDhcpEnforcedDeauthentication';
import UpdateNetworkApplianceSsidRequestRadiusServersInner from './UpdateNetworkApplianceSsidRequestRadiusServersInner';

/**
 * The UpdateNetworkApplianceSsidRequest model module.
 * @module model/UpdateNetworkApplianceSsidRequest
 * @version 1.32.0
 */
class UpdateNetworkApplianceSsidRequest {
    /**
     * Constructs a new <code>UpdateNetworkApplianceSsidRequest</code>.
     * @alias module:model/UpdateNetworkApplianceSsidRequest
     */
    constructor() { 
        
        UpdateNetworkApplianceSsidRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkApplianceSsidRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkApplianceSsidRequest} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkApplianceSsidRequest} The populated <code>UpdateNetworkApplianceSsidRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkApplianceSsidRequest();

            if (data.hasOwnProperty('authMode')) {
                obj['authMode'] = ApiClient.convertToType(data['authMode'], 'String');
            }
            if (data.hasOwnProperty('defaultVlanId')) {
                obj['defaultVlanId'] = ApiClient.convertToType(data['defaultVlanId'], 'Number');
            }
            if (data.hasOwnProperty('dhcpEnforcedDeauthentication')) {
                obj['dhcpEnforcedDeauthentication'] = UpdateNetworkApplianceSsidRequestDhcpEnforcedDeauthentication.constructFromObject(data['dhcpEnforcedDeauthentication']);
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
            if (data.hasOwnProperty('psk')) {
                obj['psk'] = ApiClient.convertToType(data['psk'], 'String');
            }
            if (data.hasOwnProperty('radiusServers')) {
                obj['radiusServers'] = ApiClient.convertToType(data['radiusServers'], [UpdateNetworkApplianceSsidRequestRadiusServersInner]);
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
     * Validates the JSON data with respect to <code>UpdateNetworkApplianceSsidRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkApplianceSsidRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['authMode'] && !(typeof data['authMode'] === 'string' || data['authMode'] instanceof String)) {
            throw new Error("Expected the field `authMode` to be a primitive type in the JSON string but got " + data['authMode']);
        }
        // validate the optional field `dhcpEnforcedDeauthentication`
        if (data['dhcpEnforcedDeauthentication']) { // data not null
          UpdateNetworkApplianceSsidRequestDhcpEnforcedDeauthentication.validateJSON(data['dhcpEnforcedDeauthentication']);
        }
        // ensure the json data is a string
        if (data['encryptionMode'] && !(typeof data['encryptionMode'] === 'string' || data['encryptionMode'] instanceof String)) {
            throw new Error("Expected the field `encryptionMode` to be a primitive type in the JSON string but got " + data['encryptionMode']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['psk'] && !(typeof data['psk'] === 'string' || data['psk'] instanceof String)) {
            throw new Error("Expected the field `psk` to be a primitive type in the JSON string but got " + data['psk']);
        }
        if (data['radiusServers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['radiusServers'])) {
                throw new Error("Expected the field `radiusServers` to be an array in the JSON data but got " + data['radiusServers']);
            }
            // validate the optional field `radiusServers` (array)
            for (const item of data['radiusServers']) {
                UpdateNetworkApplianceSsidRequestRadiusServersInner.validateJSON(item);
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
 * The association control method for the SSID ('open', 'psk', '8021x-meraki' or '8021x-radius').
 * @member {module:model/UpdateNetworkApplianceSsidRequest.AuthModeEnum} authMode
 */
UpdateNetworkApplianceSsidRequest.prototype['authMode'] = undefined;

/**
 * The VLAN ID of the VLAN associated to this SSID. This parameter is only valid if the network is in routed mode.
 * @member {Number} defaultVlanId
 */
UpdateNetworkApplianceSsidRequest.prototype['defaultVlanId'] = undefined;

/**
 * @member {module:model/UpdateNetworkApplianceSsidRequestDhcpEnforcedDeauthentication} dhcpEnforcedDeauthentication
 */
UpdateNetworkApplianceSsidRequest.prototype['dhcpEnforcedDeauthentication'] = undefined;

/**
 * Whether or not the SSID is enabled.
 * @member {Boolean} enabled
 */
UpdateNetworkApplianceSsidRequest.prototype['enabled'] = undefined;

/**
 * The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'.
 * @member {module:model/UpdateNetworkApplianceSsidRequest.EncryptionModeEnum} encryptionMode
 */
UpdateNetworkApplianceSsidRequest.prototype['encryptionMode'] = undefined;

/**
 * The name of the SSID.
 * @member {String} name
 */
UpdateNetworkApplianceSsidRequest.prototype['name'] = undefined;

/**
 * The passkey for the SSID. This param is only valid if the authMode is 'psk'.
 * @member {String} psk
 */
UpdateNetworkApplianceSsidRequest.prototype['psk'] = undefined;

/**
 * The RADIUS 802.1x servers to be used for authentication. This param is only valid if the authMode is '8021x-radius'.
 * @member {Array.<module:model/UpdateNetworkApplianceSsidRequestRadiusServersInner>} radiusServers
 */
UpdateNetworkApplianceSsidRequest.prototype['radiusServers'] = undefined;

/**
 * Boolean indicating whether the MX should advertise or hide this SSID.
 * @member {Boolean} visible
 */
UpdateNetworkApplianceSsidRequest.prototype['visible'] = undefined;

/**
 * The types of WPA encryption. ('WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode' or 'WPA3 only'). This param is only valid if (1) the authMode is 'psk' & the encryptionMode is 'wpa' OR (2) the authMode is '8021x-meraki' OR (3) the authMode is '8021x-radius'
 * @member {module:model/UpdateNetworkApplianceSsidRequest.WpaEncryptionModeEnum} wpaEncryptionMode
 */
UpdateNetworkApplianceSsidRequest.prototype['wpaEncryptionMode'] = undefined;





/**
 * Allowed values for the <code>authMode</code> property.
 * @enum {String}
 * @readonly
 */
UpdateNetworkApplianceSsidRequest['AuthModeEnum'] = {

    /**
     * value: "8021x-meraki"
     * @const
     */
    "8021x-meraki": "8021x-meraki",

    /**
     * value: "8021x-radius"
     * @const
     */
    "8021x-radius": "8021x-radius",

    /**
     * value: "open"
     * @const
     */
    "open": "open",

    /**
     * value: "psk"
     * @const
     */
    "psk": "psk"
};


/**
 * Allowed values for the <code>encryptionMode</code> property.
 * @enum {String}
 * @readonly
 */
UpdateNetworkApplianceSsidRequest['EncryptionModeEnum'] = {

    /**
     * value: "wep"
     * @const
     */
    "wep": "wep",

    /**
     * value: "wpa"
     * @const
     */
    "wpa": "wpa"
};


/**
 * Allowed values for the <code>wpaEncryptionMode</code> property.
 * @enum {String}
 * @readonly
 */
UpdateNetworkApplianceSsidRequest['WpaEncryptionModeEnum'] = {

    /**
     * value: "WPA1 and WPA2"
     * @const
     */
    "WPA1 and WPA2": "WPA1 and WPA2",

    /**
     * value: "WPA2 only"
     * @const
     */
    "WPA2 only": "WPA2 only",

    /**
     * value: "WPA3 Transition Mode"
     * @const
     */
    "WPA3 Transition Mode": "WPA3 Transition Mode",

    /**
     * value: "WPA3 only"
     * @const
     */
    "WPA3 only": "WPA3 only"
};



export default UpdateNetworkApplianceSsidRequest;

