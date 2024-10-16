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
import UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtectionIpSourceGuard from './UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtectionIpSourceGuard';

/**
 * The UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection model module.
 * @module model/UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection
 * @version 1.32.0
 */
class UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection {
    /**
     * Constructs a new <code>UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection</code>.
     * Spoofing protection settings
     * @alias module:model/UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection
     */
    constructor() { 
        
        UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection} The populated <code>UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection();

            if (data.hasOwnProperty('ipSourceGuard')) {
                obj['ipSourceGuard'] = UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtectionIpSourceGuard.constructFromObject(data['ipSourceGuard']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection</code>.
     */
    static validateJSON(data) {
        // validate the optional field `ipSourceGuard`
        if (data['ipSourceGuard']) { // data not null
          UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtectionIpSourceGuard.validateJSON(data['ipSourceGuard']);
        }

        return true;
    }


}



/**
 * @member {module:model/UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtectionIpSourceGuard} ipSourceGuard
 */
UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection.prototype['ipSourceGuard'] = undefined;






export default UpdateNetworkApplianceFirewallSettingsRequestSpoofingProtection;

