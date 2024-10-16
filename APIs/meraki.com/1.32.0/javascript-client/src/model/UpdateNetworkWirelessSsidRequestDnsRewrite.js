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
 * The UpdateNetworkWirelessSsidRequestDnsRewrite model module.
 * @module model/UpdateNetworkWirelessSsidRequestDnsRewrite
 * @version 1.32.0
 */
class UpdateNetworkWirelessSsidRequestDnsRewrite {
    /**
     * Constructs a new <code>UpdateNetworkWirelessSsidRequestDnsRewrite</code>.
     * DNS servers rewrite settings
     * @alias module:model/UpdateNetworkWirelessSsidRequestDnsRewrite
     */
    constructor() { 
        
        UpdateNetworkWirelessSsidRequestDnsRewrite.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkWirelessSsidRequestDnsRewrite</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkWirelessSsidRequestDnsRewrite} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkWirelessSsidRequestDnsRewrite} The populated <code>UpdateNetworkWirelessSsidRequestDnsRewrite</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkWirelessSsidRequestDnsRewrite();

            if (data.hasOwnProperty('dnsCustomNameservers')) {
                obj['dnsCustomNameservers'] = ApiClient.convertToType(data['dnsCustomNameservers'], ['String']);
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkWirelessSsidRequestDnsRewrite</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkWirelessSsidRequestDnsRewrite</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['dnsCustomNameservers'])) {
            throw new Error("Expected the field `dnsCustomNameservers` to be an array in the JSON data but got " + data['dnsCustomNameservers']);
        }

        return true;
    }


}



/**
 * User specified DNS servers (up to two servers)
 * @member {Array.<String>} dnsCustomNameservers
 */
UpdateNetworkWirelessSsidRequestDnsRewrite.prototype['dnsCustomNameservers'] = undefined;

/**
 * Boolean indicating whether or not DNS server rewrite is enabled. If disabled, upstream DNS will be used
 * @member {Boolean} enabled
 */
UpdateNetworkWirelessSsidRequestDnsRewrite.prototype['enabled'] = undefined;






export default UpdateNetworkWirelessSsidRequestDnsRewrite;

