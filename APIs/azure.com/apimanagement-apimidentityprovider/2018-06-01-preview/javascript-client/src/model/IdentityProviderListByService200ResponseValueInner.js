/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import IdentityProviderListByService200ResponseValueInnerProperties from './IdentityProviderListByService200ResponseValueInnerProperties';

/**
 * The IdentityProviderListByService200ResponseValueInner model module.
 * @module model/IdentityProviderListByService200ResponseValueInner
 * @version 2018-06-01-preview
 */
class IdentityProviderListByService200ResponseValueInner {
    /**
     * Constructs a new <code>IdentityProviderListByService200ResponseValueInner</code>.
     * Identity Provider details.
     * @alias module:model/IdentityProviderListByService200ResponseValueInner
     */
    constructor() { 
        
        IdentityProviderListByService200ResponseValueInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IdentityProviderListByService200ResponseValueInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IdentityProviderListByService200ResponseValueInner} obj Optional instance to populate.
     * @return {module:model/IdentityProviderListByService200ResponseValueInner} The populated <code>IdentityProviderListByService200ResponseValueInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IdentityProviderListByService200ResponseValueInner();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = IdentityProviderListByService200ResponseValueInnerProperties.constructFromObject(data['properties']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IdentityProviderListByService200ResponseValueInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IdentityProviderListByService200ResponseValueInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          IdentityProviderListByService200ResponseValueInnerProperties.validateJSON(data['properties']);
        }

        return true;
    }


}



/**
 * @member {module:model/IdentityProviderListByService200ResponseValueInnerProperties} properties
 */
IdentityProviderListByService200ResponseValueInner.prototype['properties'] = undefined;






export default IdentityProviderListByService200ResponseValueInner;

