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
 * The GetNetworkWirelessSsidEapOverride200ResponseIdentity model module.
 * @module model/GetNetworkWirelessSsidEapOverride200ResponseIdentity
 * @version 1.32.0
 */
class GetNetworkWirelessSsidEapOverride200ResponseIdentity {
    /**
     * Constructs a new <code>GetNetworkWirelessSsidEapOverride200ResponseIdentity</code>.
     * EAP settings for identity requests.
     * @alias module:model/GetNetworkWirelessSsidEapOverride200ResponseIdentity
     */
    constructor() { 
        
        GetNetworkWirelessSsidEapOverride200ResponseIdentity.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkWirelessSsidEapOverride200ResponseIdentity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkWirelessSsidEapOverride200ResponseIdentity} obj Optional instance to populate.
     * @return {module:model/GetNetworkWirelessSsidEapOverride200ResponseIdentity} The populated <code>GetNetworkWirelessSsidEapOverride200ResponseIdentity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkWirelessSsidEapOverride200ResponseIdentity();

            if (data.hasOwnProperty('retries')) {
                obj['retries'] = ApiClient.convertToType(data['retries'], 'Number');
            }
            if (data.hasOwnProperty('timeout')) {
                obj['timeout'] = ApiClient.convertToType(data['timeout'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkWirelessSsidEapOverride200ResponseIdentity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkWirelessSsidEapOverride200ResponseIdentity</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Maximum number of EAP retries.
 * @member {Number} retries
 */
GetNetworkWirelessSsidEapOverride200ResponseIdentity.prototype['retries'] = undefined;

/**
 * EAP timeout in seconds.
 * @member {Number} timeout
 */
GetNetworkWirelessSsidEapOverride200ResponseIdentity.prototype['timeout'] = undefined;






export default GetNetworkWirelessSsidEapOverride200ResponseIdentity;

