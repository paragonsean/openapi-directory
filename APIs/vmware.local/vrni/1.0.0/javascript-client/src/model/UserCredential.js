/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Domain from './Domain';

/**
 * The UserCredential model module.
 * @module model/UserCredential
 * @version 1.0.0
 */
class UserCredential {
    /**
     * Constructs a new <code>UserCredential</code>.
     * @alias module:model/UserCredential
     */
    constructor() { 
        
        UserCredential.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UserCredential</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UserCredential} obj Optional instance to populate.
     * @return {module:model/UserCredential} The populated <code>UserCredential</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UserCredential();

            if (data.hasOwnProperty('domain')) {
                obj['domain'] = Domain.constructFromObject(data['domain']);
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
     * Validates the JSON data with respect to <code>UserCredential</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UserCredential</code>.
     */
    static validateJSON(data) {
        // validate the optional field `domain`
        if (data['domain']) { // data not null
          Domain.validateJSON(data['domain']);
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
 * @member {module:model/Domain} domain
 */
UserCredential.prototype['domain'] = undefined;

/**
 * @member {String} password
 */
UserCredential.prototype['password'] = undefined;

/**
 * @member {String} username
 */
UserCredential.prototype['username'] = undefined;






export default UserCredential;

