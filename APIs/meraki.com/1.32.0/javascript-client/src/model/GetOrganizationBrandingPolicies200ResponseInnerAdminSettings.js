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
 * The GetOrganizationBrandingPolicies200ResponseInnerAdminSettings model module.
 * @module model/GetOrganizationBrandingPolicies200ResponseInnerAdminSettings
 * @version 1.32.0
 */
class GetOrganizationBrandingPolicies200ResponseInnerAdminSettings {
    /**
     * Constructs a new <code>GetOrganizationBrandingPolicies200ResponseInnerAdminSettings</code>.
     * Settings for describing which kinds of admins this policy applies to.
     * @alias module:model/GetOrganizationBrandingPolicies200ResponseInnerAdminSettings
     */
    constructor() { 
        
        GetOrganizationBrandingPolicies200ResponseInnerAdminSettings.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetOrganizationBrandingPolicies200ResponseInnerAdminSettings</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetOrganizationBrandingPolicies200ResponseInnerAdminSettings} obj Optional instance to populate.
     * @return {module:model/GetOrganizationBrandingPolicies200ResponseInnerAdminSettings} The populated <code>GetOrganizationBrandingPolicies200ResponseInnerAdminSettings</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetOrganizationBrandingPolicies200ResponseInnerAdminSettings();

            if (data.hasOwnProperty('appliesTo')) {
                obj['appliesTo'] = ApiClient.convertToType(data['appliesTo'], 'String');
            }
            if (data.hasOwnProperty('values')) {
                obj['values'] = ApiClient.convertToType(data['values'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetOrganizationBrandingPolicies200ResponseInnerAdminSettings</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetOrganizationBrandingPolicies200ResponseInnerAdminSettings</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['appliesTo'] && !(typeof data['appliesTo'] === 'string' || data['appliesTo'] instanceof String)) {
            throw new Error("Expected the field `appliesTo` to be a primitive type in the JSON string but got " + data['appliesTo']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['values'])) {
            throw new Error("Expected the field `values` to be an array in the JSON data but got " + data['values']);
        }

        return true;
    }


}



/**
 * Which kinds of admins this policy applies to. Can be one of 'All organization admins', 'All enterprise admins', 'All network admins', 'All admins of networks...', 'All admins of networks tagged...', 'Specific admins...', 'All admins' or 'All SAML admins'.
 * @member {module:model/GetOrganizationBrandingPolicies200ResponseInnerAdminSettings.AppliesToEnum} appliesTo
 */
GetOrganizationBrandingPolicies200ResponseInnerAdminSettings.prototype['appliesTo'] = undefined;

/**
 *       If 'appliesTo' is set to one of 'Specific admins...', 'All admins of networks...' or 'All admins of networks tagged...', then you must specify this 'values' property to provide the set of       entities to apply the branding policy to. For 'Specific admins...', specify an array of admin IDs. For 'All admins of       networks...', specify an array of network IDs and/or configuration template IDs. For 'All admins of networks tagged...',       specify an array of tag names. 
 * @member {Array.<String>} values
 */
GetOrganizationBrandingPolicies200ResponseInnerAdminSettings.prototype['values'] = undefined;





/**
 * Allowed values for the <code>appliesTo</code> property.
 * @enum {String}
 * @readonly
 */
GetOrganizationBrandingPolicies200ResponseInnerAdminSettings['AppliesToEnum'] = {

    /**
     * value: "All SAML admins"
     * @const
     */
    "All SAML admins": "All SAML admins",

    /**
     * value: "All admins"
     * @const
     */
    "All admins": "All admins",

    /**
     * value: "All admins of networks tagged..."
     * @const
     */
    "All admins of networks tagged...": "All admins of networks tagged...",

    /**
     * value: "All admins of networks..."
     * @const
     */
    "All admins of networks...": "All admins of networks...",

    /**
     * value: "All enterprise admins"
     * @const
     */
    "All enterprise admins": "All enterprise admins",

    /**
     * value: "All network admins"
     * @const
     */
    "All network admins": "All network admins",

    /**
     * value: "All organization admins"
     * @const
     */
    "All organization admins": "All organization admins",

    /**
     * value: "Specific admins..."
     * @const
     */
    "Specific admins...": "Specific admins..."
};



export default GetOrganizationBrandingPolicies200ResponseInnerAdminSettings;

