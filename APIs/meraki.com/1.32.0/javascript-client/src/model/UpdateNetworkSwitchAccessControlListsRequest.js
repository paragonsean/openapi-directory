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
import UpdateNetworkSwitchAccessControlListsRequestRulesInner from './UpdateNetworkSwitchAccessControlListsRequestRulesInner';

/**
 * The UpdateNetworkSwitchAccessControlListsRequest model module.
 * @module model/UpdateNetworkSwitchAccessControlListsRequest
 * @version 1.32.0
 */
class UpdateNetworkSwitchAccessControlListsRequest {
    /**
     * Constructs a new <code>UpdateNetworkSwitchAccessControlListsRequest</code>.
     * @alias module:model/UpdateNetworkSwitchAccessControlListsRequest
     * @param rules {Array.<module:model/UpdateNetworkSwitchAccessControlListsRequestRulesInner>} An ordered array of the access control list rules (not including the default rule). An empty array will clear the rules.
     */
    constructor(rules) { 
        
        UpdateNetworkSwitchAccessControlListsRequest.initialize(this, rules);
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
     * Constructs a <code>UpdateNetworkSwitchAccessControlListsRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkSwitchAccessControlListsRequest} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkSwitchAccessControlListsRequest} The populated <code>UpdateNetworkSwitchAccessControlListsRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkSwitchAccessControlListsRequest();

            if (data.hasOwnProperty('rules')) {
                obj['rules'] = ApiClient.convertToType(data['rules'], [UpdateNetworkSwitchAccessControlListsRequestRulesInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkSwitchAccessControlListsRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkSwitchAccessControlListsRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateNetworkSwitchAccessControlListsRequest.RequiredProperties) {
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
                UpdateNetworkSwitchAccessControlListsRequestRulesInner.validateJSON(item);
            };
        }

        return true;
    }


}

UpdateNetworkSwitchAccessControlListsRequest.RequiredProperties = ["rules"];

/**
 * An ordered array of the access control list rules (not including the default rule). An empty array will clear the rules.
 * @member {Array.<module:model/UpdateNetworkSwitchAccessControlListsRequestRulesInner>} rules
 */
UpdateNetworkSwitchAccessControlListsRequest.prototype['rules'] = undefined;






export default UpdateNetworkSwitchAccessControlListsRequest;

