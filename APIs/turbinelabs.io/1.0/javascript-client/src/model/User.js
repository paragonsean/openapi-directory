/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
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
 * The User model module.
 * @module model/User
 * @version 1.0
 */
class User {
    /**
     * Constructs a new <code>User</code>.
     * @alias module:model/User
     * @param checksum {String} 
     * @param loginEmail {String} 
     * @param userKey {String} 
     */
    constructor(checksum, loginEmail, userKey) { 
        
        User.initialize(this, checksum, loginEmail, userKey);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, checksum, loginEmail, userKey) { 
        obj['checksum'] = checksum;
        obj['login_email'] = loginEmail;
        obj['user_key'] = userKey;
    }

    /**
     * Constructs a <code>User</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/User} obj Optional instance to populate.
     * @return {module:model/User} The populated <code>User</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new User();

            if (data.hasOwnProperty('checksum')) {
                obj['checksum'] = ApiClient.convertToType(data['checksum'], 'String');
            }
            if (data.hasOwnProperty('deleted_at')) {
                obj['deleted_at'] = ApiClient.convertToType(data['deleted_at'], 'String');
            }
            if (data.hasOwnProperty('login_email')) {
                obj['login_email'] = ApiClient.convertToType(data['login_email'], 'String');
            }
            if (data.hasOwnProperty('user_key')) {
                obj['user_key'] = ApiClient.convertToType(data['user_key'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>User</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>User</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of User.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['checksum'] && !(typeof data['checksum'] === 'string' || data['checksum'] instanceof String)) {
            throw new Error("Expected the field `checksum` to be a primitive type in the JSON string but got " + data['checksum']);
        }
        // ensure the json data is a string
        if (data['deleted_at'] && !(typeof data['deleted_at'] === 'string' || data['deleted_at'] instanceof String)) {
            throw new Error("Expected the field `deleted_at` to be a primitive type in the JSON string but got " + data['deleted_at']);
        }
        // ensure the json data is a string
        if (data['login_email'] && !(typeof data['login_email'] === 'string' || data['login_email'] instanceof String)) {
            throw new Error("Expected the field `login_email` to be a primitive type in the JSON string but got " + data['login_email']);
        }
        // ensure the json data is a string
        if (data['user_key'] && !(typeof data['user_key'] === 'string' || data['user_key'] instanceof String)) {
            throw new Error("Expected the field `user_key` to be a primitive type in the JSON string but got " + data['user_key']);
        }

        return true;
    }


}

User.RequiredProperties = ["checksum", "login_email", "user_key"];

/**
 * @member {String} checksum
 */
User.prototype['checksum'] = undefined;

/**
 * A timestamp that marks when a user was deleted. It is in the format yyyy-mm-ddThh:mm:ss.SZ. The timezone will always be UTC. 
 * @member {String} deleted_at
 */
User.prototype['deleted_at'] = undefined;

/**
 * @member {String} login_email
 */
User.prototype['login_email'] = undefined;

/**
 * @member {String} user_key
 */
User.prototype['user_key'] = undefined;






export default User;

