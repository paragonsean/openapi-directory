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
import UpdateNetworkSwitchDhcpServerPolicyRequestAlerts from './UpdateNetworkSwitchDhcpServerPolicyRequestAlerts';
import UpdateNetworkSwitchDhcpServerPolicyRequestArpInspection from './UpdateNetworkSwitchDhcpServerPolicyRequestArpInspection';

/**
 * The UpdateNetworkSwitchDhcpServerPolicyRequest model module.
 * @module model/UpdateNetworkSwitchDhcpServerPolicyRequest
 * @version 1.32.0
 */
class UpdateNetworkSwitchDhcpServerPolicyRequest {
    /**
     * Constructs a new <code>UpdateNetworkSwitchDhcpServerPolicyRequest</code>.
     * @alias module:model/UpdateNetworkSwitchDhcpServerPolicyRequest
     */
    constructor() { 
        
        UpdateNetworkSwitchDhcpServerPolicyRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkSwitchDhcpServerPolicyRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkSwitchDhcpServerPolicyRequest} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkSwitchDhcpServerPolicyRequest} The populated <code>UpdateNetworkSwitchDhcpServerPolicyRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkSwitchDhcpServerPolicyRequest();

            if (data.hasOwnProperty('alerts')) {
                obj['alerts'] = UpdateNetworkSwitchDhcpServerPolicyRequestAlerts.constructFromObject(data['alerts']);
            }
            if (data.hasOwnProperty('allowedServers')) {
                obj['allowedServers'] = ApiClient.convertToType(data['allowedServers'], ['String']);
            }
            if (data.hasOwnProperty('arpInspection')) {
                obj['arpInspection'] = UpdateNetworkSwitchDhcpServerPolicyRequestArpInspection.constructFromObject(data['arpInspection']);
            }
            if (data.hasOwnProperty('blockedServers')) {
                obj['blockedServers'] = ApiClient.convertToType(data['blockedServers'], ['String']);
            }
            if (data.hasOwnProperty('defaultPolicy')) {
                obj['defaultPolicy'] = ApiClient.convertToType(data['defaultPolicy'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkSwitchDhcpServerPolicyRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkSwitchDhcpServerPolicyRequest</code>.
     */
    static validateJSON(data) {
        // validate the optional field `alerts`
        if (data['alerts']) { // data not null
          UpdateNetworkSwitchDhcpServerPolicyRequestAlerts.validateJSON(data['alerts']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['allowedServers'])) {
            throw new Error("Expected the field `allowedServers` to be an array in the JSON data but got " + data['allowedServers']);
        }
        // validate the optional field `arpInspection`
        if (data['arpInspection']) { // data not null
          UpdateNetworkSwitchDhcpServerPolicyRequestArpInspection.validateJSON(data['arpInspection']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['blockedServers'])) {
            throw new Error("Expected the field `blockedServers` to be an array in the JSON data but got " + data['blockedServers']);
        }
        // ensure the json data is a string
        if (data['defaultPolicy'] && !(typeof data['defaultPolicy'] === 'string' || data['defaultPolicy'] instanceof String)) {
            throw new Error("Expected the field `defaultPolicy` to be a primitive type in the JSON string but got " + data['defaultPolicy']);
        }

        return true;
    }


}



/**
 * @member {module:model/UpdateNetworkSwitchDhcpServerPolicyRequestAlerts} alerts
 */
UpdateNetworkSwitchDhcpServerPolicyRequest.prototype['alerts'] = undefined;

/**
 * List the MAC addresses of DHCP servers to permit on the network when defaultPolicy is set to block. An empty array will clear the entries.
 * @member {Array.<String>} allowedServers
 */
UpdateNetworkSwitchDhcpServerPolicyRequest.prototype['allowedServers'] = undefined;

/**
 * @member {module:model/UpdateNetworkSwitchDhcpServerPolicyRequestArpInspection} arpInspection
 */
UpdateNetworkSwitchDhcpServerPolicyRequest.prototype['arpInspection'] = undefined;

/**
 * List the MAC addresses of DHCP servers to block on the network when defaultPolicy is set to allow. An empty array will clear the entries.
 * @member {Array.<String>} blockedServers
 */
UpdateNetworkSwitchDhcpServerPolicyRequest.prototype['blockedServers'] = undefined;

/**
 * 'allow' or 'block' new DHCP servers. Default value is 'allow'.
 * @member {module:model/UpdateNetworkSwitchDhcpServerPolicyRequest.DefaultPolicyEnum} defaultPolicy
 */
UpdateNetworkSwitchDhcpServerPolicyRequest.prototype['defaultPolicy'] = undefined;





/**
 * Allowed values for the <code>defaultPolicy</code> property.
 * @enum {String}
 * @readonly
 */
UpdateNetworkSwitchDhcpServerPolicyRequest['DefaultPolicyEnum'] = {

    /**
     * value: "allow"
     * @const
     */
    "allow": "allow",

    /**
     * value: "block"
     * @const
     */
    "block": "block"
};



export default UpdateNetworkSwitchDhcpServerPolicyRequest;

