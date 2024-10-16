/**
 * Api Documentation
 * Api Documentation
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
 * The JwtResponse model module.
 * @module model/JwtResponse
 * @version 1.0
 */
class JwtResponse {
    /**
     * Constructs a new <code>JwtResponse</code>.
     * @alias module:model/JwtResponse
     * @param token {String} The value of token
     * @param type {String} The type of token
     */
    constructor(token, type) { 
        
        JwtResponse.initialize(this, token, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, token, type) { 
        obj['token'] = token;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>JwtResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/JwtResponse} obj Optional instance to populate.
     * @return {module:model/JwtResponse} The populated <code>JwtResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new JwtResponse();

            if (data.hasOwnProperty('customerId')) {
                obj['customerId'] = ApiClient.convertToType(data['customerId'], 'Number');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('role')) {
                obj['role'] = ApiClient.convertToType(data['role'], 'String');
            }
            if (data.hasOwnProperty('token')) {
                obj['token'] = ApiClient.convertToType(data['token'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('userId')) {
                obj['userId'] = ApiClient.convertToType(data['userId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>JwtResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>JwtResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of JwtResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['role'] && !(typeof data['role'] === 'string' || data['role'] instanceof String)) {
            throw new Error("Expected the field `role` to be a primitive type in the JSON string but got " + data['role']);
        }
        // ensure the json data is a string
        if (data['token'] && !(typeof data['token'] === 'string' || data['token'] instanceof String)) {
            throw new Error("Expected the field `token` to be a primitive type in the JSON string but got " + data['token']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

JwtResponse.RequiredProperties = ["token", "type"];

/**
 * The ID of the Customer
 * @member {Number} customerId
 */
JwtResponse.prototype['customerId'] = undefined;

/**
 * The Role of the User
 * @member {String} email
 */
JwtResponse.prototype['email'] = undefined;

/**
 * The Role of the User
 * @member {String} role
 */
JwtResponse.prototype['role'] = undefined;

/**
 * The value of token
 * @member {String} token
 */
JwtResponse.prototype['token'] = undefined;

/**
 * The type of token
 * @member {String} type
 */
JwtResponse.prototype['type'] = undefined;

/**
 * The ID of the User
 * @member {Number} userId
 */
JwtResponse.prototype['userId'] = undefined;






export default JwtResponse;

