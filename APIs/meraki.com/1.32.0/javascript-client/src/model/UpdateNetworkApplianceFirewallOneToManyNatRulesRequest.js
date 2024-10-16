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
import UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInner from './UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInner';

/**
 * The UpdateNetworkApplianceFirewallOneToManyNatRulesRequest model module.
 * @module model/UpdateNetworkApplianceFirewallOneToManyNatRulesRequest
 * @version 1.32.0
 */
class UpdateNetworkApplianceFirewallOneToManyNatRulesRequest {
    /**
     * Constructs a new <code>UpdateNetworkApplianceFirewallOneToManyNatRulesRequest</code>.
     * @alias module:model/UpdateNetworkApplianceFirewallOneToManyNatRulesRequest
     * @param rules {Array.<module:model/UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInner>} An array of 1:Many nat rules
     */
    constructor(rules) { 
        
        UpdateNetworkApplianceFirewallOneToManyNatRulesRequest.initialize(this, rules);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, rules) { 
        obj['rules'] = rules;
    }

    /**
     * Constructs a <code>UpdateNetworkApplianceFirewallOneToManyNatRulesRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkApplianceFirewallOneToManyNatRulesRequest} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkApplianceFirewallOneToManyNatRulesRequest} The populated <code>UpdateNetworkApplianceFirewallOneToManyNatRulesRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkApplianceFirewallOneToManyNatRulesRequest();

            if (data.hasOwnProperty('rules')) {
                obj['rules'] = ApiClient.convertToType(data['rules'], [UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkApplianceFirewallOneToManyNatRulesRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkApplianceFirewallOneToManyNatRulesRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateNetworkApplianceFirewallOneToManyNatRulesRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['rules']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['rules'])) {
                throw new Error("Expected the field `rules` to be an array in the JSON data but got " + data['rules']);
            }
            // validate the optional field `rules` (array)
            for (const item of data['rules']) {
                UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInner.validateJSON(item);
            };
        }

        return true;
    }


}

UpdateNetworkApplianceFirewallOneToManyNatRulesRequest.RequiredProperties = ["rules"];

/**
 * An array of 1:Many nat rules
 * @member {Array.<module:model/UpdateNetworkApplianceFirewallOneToManyNatRulesRequestRulesInner>} rules
 */
UpdateNetworkApplianceFirewallOneToManyNatRulesRequest.prototype['rules'] = undefined;






export default UpdateNetworkApplianceFirewallOneToManyNatRulesRequest;

