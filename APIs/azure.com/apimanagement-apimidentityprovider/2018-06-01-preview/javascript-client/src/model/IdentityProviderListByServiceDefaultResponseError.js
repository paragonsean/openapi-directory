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
import IdentityProviderListByServiceDefaultResponseErrorDetailsInner from './IdentityProviderListByServiceDefaultResponseErrorDetailsInner';

/**
 * The IdentityProviderListByServiceDefaultResponseError model module.
 * @module model/IdentityProviderListByServiceDefaultResponseError
 * @version 2018-06-01-preview
 */
class IdentityProviderListByServiceDefaultResponseError {
    /**
     * Constructs a new <code>IdentityProviderListByServiceDefaultResponseError</code>.
     * Error Body contract.
     * @alias module:model/IdentityProviderListByServiceDefaultResponseError
     */
    constructor() { 
        
        IdentityProviderListByServiceDefaultResponseError.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IdentityProviderListByServiceDefaultResponseError</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IdentityProviderListByServiceDefaultResponseError} obj Optional instance to populate.
     * @return {module:model/IdentityProviderListByServiceDefaultResponseError} The populated <code>IdentityProviderListByServiceDefaultResponseError</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IdentityProviderListByServiceDefaultResponseError();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('details')) {
                obj['details'] = ApiClient.convertToType(data['details'], [IdentityProviderListByServiceDefaultResponseErrorDetailsInner]);
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IdentityProviderListByServiceDefaultResponseError</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IdentityProviderListByServiceDefaultResponseError</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        if (data['details']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['details'])) {
                throw new Error("Expected the field `details` to be an array in the JSON data but got " + data['details']);
            }
            // validate the optional field `details` (array)
            for (const item of data['details']) {
                IdentityProviderListByServiceDefaultResponseErrorDetailsInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }

        return true;
    }


}



/**
 * Service-defined error code. This code serves as a sub-status for the HTTP error code specified in the response.
 * @member {String} code
 */
IdentityProviderListByServiceDefaultResponseError.prototype['code'] = undefined;

/**
 * The list of invalid fields send in request, in case of validation error.
 * @member {Array.<module:model/IdentityProviderListByServiceDefaultResponseErrorDetailsInner>} details
 */
IdentityProviderListByServiceDefaultResponseError.prototype['details'] = undefined;

/**
 * Human-readable representation of the error.
 * @member {String} message
 */
IdentityProviderListByServiceDefaultResponseError.prototype['message'] = undefined;






export default IdentityProviderListByServiceDefaultResponseError;

