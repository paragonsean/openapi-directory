/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ViolatedPasswordPolicy from './ViolatedPasswordPolicy';

/**
 * The PasswordPolicyViolationResponse model module.
 * @module model/PasswordPolicyViolationResponse
 * @version 4.42.3
 */
class PasswordPolicyViolationResponse {
    /**
     * Constructs a new <code>PasswordPolicyViolationResponse</code>.
     * List of violated password policies
     * @alias module:model/PasswordPolicyViolationResponse
     * @param code {Number} HTTP status code
     * @param message {String} HTTP status code description
     */
    constructor(code, message) { 
        
        PasswordPolicyViolationResponse.initialize(this, code, message);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, code, message) { 
        obj['code'] = code;
        obj['message'] = message;
    }

    /**
     * Constructs a <code>PasswordPolicyViolationResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PasswordPolicyViolationResponse} obj Optional instance to populate.
     * @return {module:model/PasswordPolicyViolationResponse} The populated <code>PasswordPolicyViolationResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PasswordPolicyViolationResponse();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'Number');
            }
            if (data.hasOwnProperty('debugInfo')) {
                obj['debugInfo'] = ApiClient.convertToType(data['debugInfo'], 'String');
            }
            if (data.hasOwnProperty('errorCode')) {
                obj['errorCode'] = ApiClient.convertToType(data['errorCode'], 'Number');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('violatedPasswordPolicies')) {
                obj['violatedPasswordPolicies'] = ApiClient.convertToType(data['violatedPasswordPolicies'], [ViolatedPasswordPolicy]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PasswordPolicyViolationResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PasswordPolicyViolationResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PasswordPolicyViolationResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['debugInfo'] && !(typeof data['debugInfo'] === 'string' || data['debugInfo'] instanceof String)) {
            throw new Error("Expected the field `debugInfo` to be a primitive type in the JSON string but got " + data['debugInfo']);
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        if (data['violatedPasswordPolicies']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['violatedPasswordPolicies'])) {
                throw new Error("Expected the field `violatedPasswordPolicies` to be an array in the JSON data but got " + data['violatedPasswordPolicies']);
            }
            // validate the optional field `violatedPasswordPolicies` (array)
            for (const item of data['violatedPasswordPolicies']) {
                ViolatedPasswordPolicy.validateJSON(item);
            };
        }

        return true;
    }


}

PasswordPolicyViolationResponse.RequiredProperties = ["code", "message"];

/**
 * HTTP status code
 * @member {Number} code
 */
PasswordPolicyViolationResponse.prototype['code'] = undefined;

/**
 * Debug information
 * @member {String} debugInfo
 */
PasswordPolicyViolationResponse.prototype['debugInfo'] = undefined;

/**
 * Internal error code
 * @member {Number} errorCode
 */
PasswordPolicyViolationResponse.prototype['errorCode'] = undefined;

/**
 * HTTP status code description
 * @member {String} message
 */
PasswordPolicyViolationResponse.prototype['message'] = undefined;

/**
 * List of violated password policies
 * @member {Array.<module:model/ViolatedPasswordPolicy>} violatedPasswordPolicies
 */
PasswordPolicyViolationResponse.prototype['violatedPasswordPolicies'] = undefined;






export default PasswordPolicyViolationResponse;

