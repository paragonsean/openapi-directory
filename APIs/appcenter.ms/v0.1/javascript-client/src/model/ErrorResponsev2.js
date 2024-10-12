/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import UsersGetUserMetadataDefaultResponseError from './UsersGetUserMetadataDefaultResponseError';

/**
 * The ErrorResponsev2 model module.
 * @module model/ErrorResponsev2
 * @version v0.1
 */
class ErrorResponsev2 {
    /**
     * Constructs a new <code>ErrorResponsev2</code>.
     * @alias module:model/ErrorResponsev2
     * @param error {module:model/UsersGetUserMetadataDefaultResponseError} 
     */
    constructor(error) { 
        
        ErrorResponsev2.initialize(this, error);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, error) { 
        obj['error'] = error;
    }

    /**
     * Constructs a <code>ErrorResponsev2</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ErrorResponsev2} obj Optional instance to populate.
     * @return {module:model/ErrorResponsev2} The populated <code>ErrorResponsev2</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ErrorResponsev2();

            if (data.hasOwnProperty('error')) {
                obj['error'] = UsersGetUserMetadataDefaultResponseError.constructFromObject(data['error']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ErrorResponsev2</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ErrorResponsev2</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ErrorResponsev2.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `error`
        if (data['error']) { // data not null
          UsersGetUserMetadataDefaultResponseError.validateJSON(data['error']);
        }

        return true;
    }


}

ErrorResponsev2.RequiredProperties = ["error"];

/**
 * @member {module:model/UsersGetUserMetadataDefaultResponseError} error
 */
ErrorResponsev2.prototype['error'] = undefined;






export default ErrorResponsev2;

