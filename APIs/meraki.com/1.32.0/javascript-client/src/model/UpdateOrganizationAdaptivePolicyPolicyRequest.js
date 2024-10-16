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
import CreateOrganizationAdaptivePolicyPolicyRequestAclsInner from './CreateOrganizationAdaptivePolicyPolicyRequestAclsInner';
import CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup from './CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup';
import CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup from './CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup';

/**
 * The UpdateOrganizationAdaptivePolicyPolicyRequest model module.
 * @module model/UpdateOrganizationAdaptivePolicyPolicyRequest
 * @version 1.32.0
 */
class UpdateOrganizationAdaptivePolicyPolicyRequest {
    /**
     * Constructs a new <code>UpdateOrganizationAdaptivePolicyPolicyRequest</code>.
     * @alias module:model/UpdateOrganizationAdaptivePolicyPolicyRequest
     */
    constructor() { 
        
        UpdateOrganizationAdaptivePolicyPolicyRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateOrganizationAdaptivePolicyPolicyRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateOrganizationAdaptivePolicyPolicyRequest} obj Optional instance to populate.
     * @return {module:model/UpdateOrganizationAdaptivePolicyPolicyRequest} The populated <code>UpdateOrganizationAdaptivePolicyPolicyRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateOrganizationAdaptivePolicyPolicyRequest();

            if (data.hasOwnProperty('acls')) {
                obj['acls'] = ApiClient.convertToType(data['acls'], [CreateOrganizationAdaptivePolicyPolicyRequestAclsInner]);
            }
            if (data.hasOwnProperty('destinationGroup')) {
                obj['destinationGroup'] = CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup.constructFromObject(data['destinationGroup']);
            }
            if (data.hasOwnProperty('lastEntryRule')) {
                obj['lastEntryRule'] = ApiClient.convertToType(data['lastEntryRule'], 'String');
            }
            if (data.hasOwnProperty('sourceGroup')) {
                obj['sourceGroup'] = CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup.constructFromObject(data['sourceGroup']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateOrganizationAdaptivePolicyPolicyRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateOrganizationAdaptivePolicyPolicyRequest</code>.
     */
    static validateJSON(data) {
        if (data['acls']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['acls'])) {
                throw new Error("Expected the field `acls` to be an array in the JSON data but got " + data['acls']);
            }
            // validate the optional field `acls` (array)
            for (const item of data['acls']) {
                CreateOrganizationAdaptivePolicyPolicyRequestAclsInner.validateJSON(item);
            };
        }
        // validate the optional field `destinationGroup`
        if (data['destinationGroup']) { // data not null
          CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup.validateJSON(data['destinationGroup']);
        }
        // ensure the json data is a string
        if (data['lastEntryRule'] && !(typeof data['lastEntryRule'] === 'string' || data['lastEntryRule'] instanceof String)) {
            throw new Error("Expected the field `lastEntryRule` to be a primitive type in the JSON string but got " + data['lastEntryRule']);
        }
        // validate the optional field `sourceGroup`
        if (data['sourceGroup']) { // data not null
          CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup.validateJSON(data['sourceGroup']);
        }

        return true;
    }


}



/**
 * An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy
 * @member {Array.<module:model/CreateOrganizationAdaptivePolicyPolicyRequestAclsInner>} acls
 */
UpdateOrganizationAdaptivePolicyPolicyRequest.prototype['acls'] = undefined;

/**
 * @member {module:model/CreateOrganizationAdaptivePolicyPolicyRequestDestinationGroup} destinationGroup
 */
UpdateOrganizationAdaptivePolicyPolicyRequest.prototype['destinationGroup'] = undefined;

/**
 * The rule to apply if there is no matching ACL
 * @member {module:model/UpdateOrganizationAdaptivePolicyPolicyRequest.LastEntryRuleEnum} lastEntryRule
 */
UpdateOrganizationAdaptivePolicyPolicyRequest.prototype['lastEntryRule'] = undefined;

/**
 * @member {module:model/CreateOrganizationAdaptivePolicyPolicyRequestSourceGroup} sourceGroup
 */
UpdateOrganizationAdaptivePolicyPolicyRequest.prototype['sourceGroup'] = undefined;





/**
 * Allowed values for the <code>lastEntryRule</code> property.
 * @enum {String}
 * @readonly
 */
UpdateOrganizationAdaptivePolicyPolicyRequest['LastEntryRuleEnum'] = {

    /**
     * value: "allow"
     * @const
     */
    "allow": "allow",

    /**
     * value: "default"
     * @const
     */
    "default": "default",

    /**
     * value: "deny"
     * @const
     */
    "deny": "deny"
};



export default UpdateOrganizationAdaptivePolicyPolicyRequest;

