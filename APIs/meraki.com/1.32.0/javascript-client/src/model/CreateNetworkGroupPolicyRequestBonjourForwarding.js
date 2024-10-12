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
import CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner from './CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner';

/**
 * The CreateNetworkGroupPolicyRequestBonjourForwarding model module.
 * @module model/CreateNetworkGroupPolicyRequestBonjourForwarding
 * @version 1.32.0
 */
class CreateNetworkGroupPolicyRequestBonjourForwarding {
    /**
     * Constructs a new <code>CreateNetworkGroupPolicyRequestBonjourForwarding</code>.
     * The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.
     * @alias module:model/CreateNetworkGroupPolicyRequestBonjourForwarding
     */
    constructor() { 
        
        CreateNetworkGroupPolicyRequestBonjourForwarding.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreateNetworkGroupPolicyRequestBonjourForwarding</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkGroupPolicyRequestBonjourForwarding} obj Optional instance to populate.
     * @return {module:model/CreateNetworkGroupPolicyRequestBonjourForwarding} The populated <code>CreateNetworkGroupPolicyRequestBonjourForwarding</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkGroupPolicyRequestBonjourForwarding();

            if (data.hasOwnProperty('rules')) {
                obj['rules'] = ApiClient.convertToType(data['rules'], [CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner]);
            }
            if (data.hasOwnProperty('settings')) {
                obj['settings'] = ApiClient.convertToType(data['settings'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateNetworkGroupPolicyRequestBonjourForwarding</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkGroupPolicyRequestBonjourForwarding</code>.
     */
    static validateJSON(data) {
        if (data['rules']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['rules'])) {
                throw new Error("Expected the field `rules` to be an array in the JSON data but got " + data['rules']);
            }
            // validate the optional field `rules` (array)
            for (const item of data['rules']) {
                CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['settings'] && !(typeof data['settings'] === 'string' || data['settings'] instanceof String)) {
            throw new Error("Expected the field `settings` to be a primitive type in the JSON string but got " + data['settings']);
        }

        return true;
    }


}



/**
 * A list of the Bonjour forwarding rules for your group policy. If 'settings' is set to 'custom', at least one rule must be specified.
 * @member {Array.<module:model/CreateNetworkGroupPolicyRequestBonjourForwardingRulesInner>} rules
 */
CreateNetworkGroupPolicyRequestBonjourForwarding.prototype['rules'] = undefined;

/**
 * How Bonjour rules are applied. Can be 'network default', 'ignore' or 'custom'.
 * @member {module:model/CreateNetworkGroupPolicyRequestBonjourForwarding.SettingsEnum} settings
 */
CreateNetworkGroupPolicyRequestBonjourForwarding.prototype['settings'] = undefined;





/**
 * Allowed values for the <code>settings</code> property.
 * @enum {String}
 * @readonly
 */
CreateNetworkGroupPolicyRequestBonjourForwarding['SettingsEnum'] = {

    /**
     * value: "custom"
     * @const
     */
    "custom": "custom",

    /**
     * value: "ignore"
     * @const
     */
    "ignore": "ignore",

    /**
     * value: "network default"
     * @const
     */
    "network default": "network default"
};



export default CreateNetworkGroupPolicyRequestBonjourForwarding;

