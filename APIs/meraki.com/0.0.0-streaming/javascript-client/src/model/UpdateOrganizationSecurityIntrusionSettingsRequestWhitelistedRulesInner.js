/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner model module.
 * @module model/UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner
 * @version 0.0.0-streaming
 */
class UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner {
    /**
     * Constructs a new <code>UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner</code>.
     * @alias module:model/UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner
     * @param ruleId {String} A rule identifier of the format meraki:intrusion/snort/GID/<gid>/SID/<sid>. gid and sid can be obtained from either https://www.snort.org/rule-docs or as ruleIds from the security events in /organization/[orgId]/securityEvents
     */
    constructor(ruleId) { 
        
        UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner.initialize(this, ruleId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, ruleId) { 
        obj['ruleId'] = ruleId;
    }

    /**
     * Constructs a <code>UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner} obj Optional instance to populate.
     * @return {module:model/UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner} The populated <code>UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner();

            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('ruleId')) {
                obj['ruleId'] = ApiClient.convertToType(data['ruleId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['ruleId'] && !(typeof data['ruleId'] === 'string' || data['ruleId'] instanceof String)) {
            throw new Error("Expected the field `ruleId` to be a primitive type in the JSON string but got " + data['ruleId']);
        }

        return true;
    }


}

UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner.RequiredProperties = ["ruleId"];

/**
 * Message is optional and is ignored on a PUT call. It is allowed in order for PUT to be compatible with GET
 * @member {String} message
 */
UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner.prototype['message'] = undefined;

/**
 * A rule identifier of the format meraki:intrusion/snort/GID/<gid>/SID/<sid>. gid and sid can be obtained from either https://www.snort.org/rule-docs or as ruleIds from the security events in /organization/[orgId]/securityEvents
 * @member {String} ruleId
 */
UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner.prototype['ruleId'] = undefined;






export default UpdateOrganizationSecurityIntrusionSettingsRequestWhitelistedRulesInner;

