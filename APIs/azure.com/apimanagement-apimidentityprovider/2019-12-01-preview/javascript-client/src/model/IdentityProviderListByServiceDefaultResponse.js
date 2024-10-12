/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2019-12-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import IdentityProviderListByServiceDefaultResponseError from './IdentityProviderListByServiceDefaultResponseError';

/**
 * The IdentityProviderListByServiceDefaultResponse model module.
 * @module model/IdentityProviderListByServiceDefaultResponse
 * @version 2019-12-01-preview
 */
class IdentityProviderListByServiceDefaultResponse {
    /**
     * Constructs a new <code>IdentityProviderListByServiceDefaultResponse</code>.
     * Error Response.
     * @alias module:model/IdentityProviderListByServiceDefaultResponse
     */
    constructor() { 
        
        IdentityProviderListByServiceDefaultResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IdentityProviderListByServiceDefaultResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IdentityProviderListByServiceDefaultResponse} obj Optional instance to populate.
     * @return {module:model/IdentityProviderListByServiceDefaultResponse} The populated <code>IdentityProviderListByServiceDefaultResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IdentityProviderListByServiceDefaultResponse();

            if (data.hasOwnProperty('error')) {
                obj['error'] = IdentityProviderListByServiceDefaultResponseError.constructFromObject(data['error']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IdentityProviderListByServiceDefaultResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IdentityProviderListByServiceDefaultResponse</code>.
     */
    static validateJSON(data) {
        // validate the optional field `error`
        if (data['error']) { // data not null
          IdentityProviderListByServiceDefaultResponseError.validateJSON(data['error']);
        }

        return true;
    }


}



/**
 * @member {module:model/IdentityProviderListByServiceDefaultResponseError} error
 */
IdentityProviderListByServiceDefaultResponse.prototype['error'] = undefined;






export default IdentityProviderListByServiceDefaultResponse;

