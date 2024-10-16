/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ApiCredential model module.
 * @module model/ApiCredential
 * @version V2
 */
class ApiCredential {
    /**
     * Constructs a new <code>ApiCredential</code>.
     * An object represents API user in CallFire system. Use /me/api/credentials endpoint to manage API users on your account
     * @alias module:model/ApiCredential
     */
    constructor() { 
        
        ApiCredential.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiCredential</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiCredential} obj Optional instance to populate.
     * @return {module:model/ApiCredential} The populated <code>ApiCredential</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiCredential();

            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiCredential</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiCredential</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }

        return true;
    }


}



/**
 * Is credential enabled
 * @member {Boolean} enabled
 */
ApiCredential.prototype['enabled'] = undefined;

/**
 * An id of an API credential
 * @member {Number} id
 */
ApiCredential.prototype['id'] = undefined;

/**
 * A name of an API credential
 * @member {String} name
 */
ApiCredential.prototype['name'] = undefined;

/**
 * A password for credential
 * @member {String} password
 */
ApiCredential.prototype['password'] = undefined;

/**
 * Username for credential
 * @member {String} username
 */
ApiCredential.prototype['username'] = undefined;






export default ApiCredential;

