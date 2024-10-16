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
 * The UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks model module.
 * @module model/UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks
 * @version 0.0.0-streaming
 */
class UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks {
    /**
     * Constructs a new <code>UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks</code>.
     * Set the included/excluded networks from the intrusion engine (optional - omitting will leave current config unchanged). This is available only in &#39;passthrough&#39; mode
     * @alias module:model/UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks
     */
    constructor() { 
        
        UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks} The populated <code>UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks();

            if (data.hasOwnProperty('excludedCidr')) {
                obj['excludedCidr'] = ApiClient.convertToType(data['excludedCidr'], ['String']);
            }
            if (data.hasOwnProperty('includedCidr')) {
                obj['includedCidr'] = ApiClient.convertToType(data['includedCidr'], ['String']);
            }
            if (data.hasOwnProperty('useDefault')) {
                obj['useDefault'] = ApiClient.convertToType(data['useDefault'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['excludedCidr'])) {
            throw new Error("Expected the field `excludedCidr` to be an array in the JSON data but got " + data['excludedCidr']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['includedCidr'])) {
            throw new Error("Expected the field `includedCidr` to be an array in the JSON data but got " + data['includedCidr']);
        }

        return true;
    }


}



/**
 * list of IP addresses or subnets being excluded from protection (required if 'useDefault' is false)
 * @member {Array.<String>} excludedCidr
 */
UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks.prototype['excludedCidr'] = undefined;

/**
 * list of IP addresses or subnets being protected (required if 'useDefault' is false)
 * @member {Array.<String>} includedCidr
 */
UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks.prototype['includedCidr'] = undefined;

/**
 * true/false whether to use special IPv4 addresses: https://tools.ietf.org/html/rfc5735 (required). Default value is true if none currently saved
 * @member {Boolean} useDefault
 */
UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks.prototype['useDefault'] = undefined;






export default UpdateNetworkSecurityIntrusionSettingsRequestProtectedNetworks;

