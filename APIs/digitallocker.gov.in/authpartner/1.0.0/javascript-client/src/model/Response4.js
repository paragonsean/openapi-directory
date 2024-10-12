/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Response4 model module.
 * @module model/Response4
 * @version 1.0.0
 */
class Response4 {
    /**
     * Constructs a new <code>Response4</code>.
     * @alias module:model/Response4
     */
    constructor() { 
        
        Response4.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Response4</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Response4} obj Optional instance to populate.
     * @return {module:model/Response4} The populated <code>Response4</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Response4();

            if (data.hasOwnProperty('error')) {
                obj['error'] = ApiClient.convertToType(data['error'], 'String');
            }
            if (data.hasOwnProperty('error_description')) {
                obj['error_description'] = ApiClient.convertToType(data['error_description'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Response4</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Response4</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['error'] && !(typeof data['error'] === 'string' || data['error'] instanceof String)) {
            throw new Error("Expected the field `error` to be a primitive type in the JSON string but got " + data['error']);
        }
        // ensure the json data is a string
        if (data['error_description'] && !(typeof data['error_description'] === 'string' || data['error_description'] instanceof String)) {
            throw new Error("Expected the field `error_description` to be a primitive type in the JSON string but got " + data['error_description']);
        }

        return true;
    }


}



/**
 * repository_service_configerror
 * @member {String} error
 */
Response4.prototype['error'] = undefined;

/**
 * Internal server error
 * @member {String} error_description
 */
Response4.prototype['error_description'] = undefined;






export default Response4;

