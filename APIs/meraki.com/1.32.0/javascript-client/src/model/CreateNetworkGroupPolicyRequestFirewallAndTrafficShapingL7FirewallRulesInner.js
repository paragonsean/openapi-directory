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
 * The CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner model module.
 * @module model/CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner
 * @version 1.32.0
 */
class CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner {
    /**
     * Constructs a new <code>CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner</code>.
     * @alias module:model/CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner
     */
    constructor() { 
        
        CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner} obj Optional instance to populate.
     * @return {module:model/CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner} The populated <code>CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner();

            if (data.hasOwnProperty('policy')) {
                obj['policy'] = ApiClient.convertToType(data['policy'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['policy'] && !(typeof data['policy'] === 'string' || data['policy'] instanceof String)) {
            throw new Error("Expected the field `policy` to be a primitive type in the JSON string but got " + data['policy']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}



/**
 * The policy applied to matching traffic. Must be 'deny'.
 * @member {module:model/CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner.PolicyEnum} policy
 */
CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner.prototype['policy'] = undefined;

/**
 * Type of the L7 Rule. Must be 'application', 'applicationCategory', 'host', 'port' or 'ipRange'
 * @member {module:model/CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner.TypeEnum} type
 */
CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner.prototype['type'] = undefined;

/**
 * The 'value' of what you want to block. If 'type' is 'host', 'port' or 'ipRange', 'value' must be a string matching either a hostname (e.g. somewhere.com), a port (e.g. 8080), or an IP range (e.g. 192.1.0.0/16). If 'type' is 'application' or 'applicationCategory', then 'value' must be an object with an ID for the application.
 * @member {String} value
 */
CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner.prototype['value'] = undefined;





/**
 * Allowed values for the <code>policy</code> property.
 * @enum {String}
 * @readonly
 */
CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner['PolicyEnum'] = {

    /**
     * value: "deny"
     * @const
     */
    "deny": "deny"
};


/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner['TypeEnum'] = {

    /**
     * value: "application"
     * @const
     */
    "application": "application",

    /**
     * value: "applicationCategory"
     * @const
     */
    "applicationCategory": "applicationCategory",

    /**
     * value: "host"
     * @const
     */
    "host": "host",

    /**
     * value: "ipRange"
     * @const
     */
    "ipRange": "ipRange",

    /**
     * value: "port"
     * @const
     */
    "port": "port"
};



export default CreateNetworkGroupPolicyRequestFirewallAndTrafficShapingL7FirewallRulesInner;

