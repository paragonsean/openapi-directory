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
import UpdateOrganizationApplianceVpnVpnFirewallRulesRequestRulesInner from './UpdateOrganizationApplianceVpnVpnFirewallRulesRequestRulesInner';

/**
 * The UpdateOrganizationApplianceVpnVpnFirewallRulesRequest model module.
 * @module model/UpdateOrganizationApplianceVpnVpnFirewallRulesRequest
 * @version 1.32.0
 */
class UpdateOrganizationApplianceVpnVpnFirewallRulesRequest {
    /**
     * Constructs a new <code>UpdateOrganizationApplianceVpnVpnFirewallRulesRequest</code>.
     * @alias module:model/UpdateOrganizationApplianceVpnVpnFirewallRulesRequest
     */
    constructor() { 
        
        UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateOrganizationApplianceVpnVpnFirewallRulesRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateOrganizationApplianceVpnVpnFirewallRulesRequest} obj Optional instance to populate.
     * @return {module:model/UpdateOrganizationApplianceVpnVpnFirewallRulesRequest} The populated <code>UpdateOrganizationApplianceVpnVpnFirewallRulesRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateOrganizationApplianceVpnVpnFirewallRulesRequest();

            if (data.hasOwnProperty('rules')) {
                obj['rules'] = ApiClient.convertToType(data['rules'], [UpdateOrganizationApplianceVpnVpnFirewallRulesRequestRulesInner]);
            }
            if (data.hasOwnProperty('syslogDefaultRule')) {
                obj['syslogDefaultRule'] = ApiClient.convertToType(data['syslogDefaultRule'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateOrganizationApplianceVpnVpnFirewallRulesRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateOrganizationApplianceVpnVpnFirewallRulesRequest</code>.
     */
    static validateJSON(data) {
        if (data['rules']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['rules'])) {
                throw new Error("Expected the field `rules` to be an array in the JSON data but got " + data['rules']);
            }
            // validate the optional field `rules` (array)
            for (const item of data['rules']) {
                UpdateOrganizationApplianceVpnVpnFirewallRulesRequestRulesInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * An ordered array of the firewall rules (not including the default rule)
 * @member {Array.<module:model/UpdateOrganizationApplianceVpnVpnFirewallRulesRequestRulesInner>} rules
 */
UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.prototype['rules'] = undefined;

/**
 * Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)
 * @member {Boolean} syslogDefaultRule
 */
UpdateOrganizationApplianceVpnVpnFirewallRulesRequest.prototype['syslogDefaultRule'] = undefined;






export default UpdateOrganizationApplianceVpnVpnFirewallRulesRequest;

