/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ValidateResponseError from './ValidateResponseError';

/**
 * The ValidateResponse model module.
 * @module model/ValidateResponse
 * @version 2016-03-01
 */
class ValidateResponse {
    /**
     * Constructs a new <code>ValidateResponse</code>.
     * Describes the result of resource validation.
     * @alias module:model/ValidateResponse
     */
    constructor() { 
        
        ValidateResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ValidateResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ValidateResponse} obj Optional instance to populate.
     * @return {module:model/ValidateResponse} The populated <code>ValidateResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ValidateResponse();

            if (data.hasOwnProperty('error')) {
                obj['error'] = ValidateResponseError.constructFromObject(data['error']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ValidateResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ValidateResponse</code>.
     */
    static validateJSON(data) {
        // validate the optional field `error`
        if (data['error']) { // data not null
          ValidateResponseError.validateJSON(data['error']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * @member {module:model/ValidateResponseError} error
 */
ValidateResponse.prototype['error'] = undefined;

/**
 * Result of validation.
 * @member {String} status
 */
ValidateResponse.prototype['status'] = undefined;






export default ValidateResponse;

