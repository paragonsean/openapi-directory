/**
 * Authentication
 * Personio Authentication API
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Response model module.
 * @module model/Response
 * @version 1.0
 */
class Response {
    /**
     * Constructs a new <code>Response</code>.
     * @alias module:model/Response
     * @param data {Object} 
     * @param success {Boolean} 
     */
    constructor(data, success) { 
        
        Response.initialize(this, data, success);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, data, success) { 
        obj['data'] = data;
        obj['success'] = success;
    }

    /**
     * Constructs a <code>Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Response} obj Optional instance to populate.
     * @return {module:model/Response} The populated <code>Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Response();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], Object);
            }
            if (data.hasOwnProperty('success')) {
                obj['success'] = ApiClient.convertToType(data['success'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Response</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Response.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

Response.RequiredProperties = ["data", "success"];

/**
 * @member {Object} data
 */
Response.prototype['data'] = undefined;

/**
 * @member {Boolean} success
 */
Response.prototype['success'] = undefined;






export default Response;

