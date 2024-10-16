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
import CreateOrganizationBrandingPolicyRequestCustomLogoImage from './CreateOrganizationBrandingPolicyRequestCustomLogoImage';

/**
 * The CreateOrganizationBrandingPolicyRequestCustomLogo model module.
 * @module model/CreateOrganizationBrandingPolicyRequestCustomLogo
 * @version 1.32.0
 */
class CreateOrganizationBrandingPolicyRequestCustomLogo {
    /**
     * Constructs a new <code>CreateOrganizationBrandingPolicyRequestCustomLogo</code>.
     * Properties describing the custom logo attached to the branding policy.
     * @alias module:model/CreateOrganizationBrandingPolicyRequestCustomLogo
     */
    constructor() { 
        
        CreateOrganizationBrandingPolicyRequestCustomLogo.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreateOrganizationBrandingPolicyRequestCustomLogo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateOrganizationBrandingPolicyRequestCustomLogo} obj Optional instance to populate.
     * @return {module:model/CreateOrganizationBrandingPolicyRequestCustomLogo} The populated <code>CreateOrganizationBrandingPolicyRequestCustomLogo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateOrganizationBrandingPolicyRequestCustomLogo();

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = CreateOrganizationBrandingPolicyRequestCustomLogoImage.constructFromObject(data['image']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateOrganizationBrandingPolicyRequestCustomLogo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateOrganizationBrandingPolicyRequestCustomLogo</code>.
     */
    static validateJSON(data) {
        // validate the optional field `image`
        if (data['image']) { // data not null
          CreateOrganizationBrandingPolicyRequestCustomLogoImage.validateJSON(data['image']);
        }

        return true;
    }


}



/**
 * Whether or not there is a custom logo enabled.
 * @member {Boolean} enabled
 */
CreateOrganizationBrandingPolicyRequestCustomLogo.prototype['enabled'] = undefined;

/**
 * @member {module:model/CreateOrganizationBrandingPolicyRequestCustomLogoImage} image
 */
CreateOrganizationBrandingPolicyRequestCustomLogo.prototype['image'] = undefined;






export default CreateOrganizationBrandingPolicyRequestCustomLogo;

