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
 * The GetNetworkApplianceSingleLan200ResponseMandatoryDhcp model module.
 * @module model/GetNetworkApplianceSingleLan200ResponseMandatoryDhcp
 * @version 1.32.0
 */
class GetNetworkApplianceSingleLan200ResponseMandatoryDhcp {
    /**
     * Constructs a new <code>GetNetworkApplianceSingleLan200ResponseMandatoryDhcp</code>.
     * Mandatory DHCP will enforce that clients connecting to this single LAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won&#39;t be able to associate. Only available on firmware versions 17.0 and above
     * @alias module:model/GetNetworkApplianceSingleLan200ResponseMandatoryDhcp
     */
    constructor() { 
        
        GetNetworkApplianceSingleLan200ResponseMandatoryDhcp.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetNetworkApplianceSingleLan200ResponseMandatoryDhcp</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetNetworkApplianceSingleLan200ResponseMandatoryDhcp} obj Optional instance to populate.
     * @return {module:model/GetNetworkApplianceSingleLan200ResponseMandatoryDhcp} The populated <code>GetNetworkApplianceSingleLan200ResponseMandatoryDhcp</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetNetworkApplianceSingleLan200ResponseMandatoryDhcp();

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetNetworkApplianceSingleLan200ResponseMandatoryDhcp</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetNetworkApplianceSingleLan200ResponseMandatoryDhcp</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Enable Mandatory DHCP on single LAN.
 * @member {Boolean} enabled
 */
GetNetworkApplianceSingleLan200ResponseMandatoryDhcp.prototype['enabled'] = undefined;






export default GetNetworkApplianceSingleLan200ResponseMandatoryDhcp;

