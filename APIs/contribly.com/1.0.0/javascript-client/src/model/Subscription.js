/**
 * Contribly
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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

/**
 * The Subscription model module.
 * @module model/Subscription
 * @version 1.0.0
 */
class Subscription {
    /**
     * Constructs a new <code>Subscription</code>.
     * @alias module:model/Subscription
     * @param id {String} 
     * @param includeBody {Boolean} 
     * @param token {String} 
     * @param types {Array.<String>} 
     * @param user {String} 
     */
    constructor(id, includeBody, token, types, user) { 
        
        Subscription.initialize(this, id, includeBody, token, types, user);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, includeBody, token, types, user) { 
        obj['id'] = id;
        obj['includeBody'] = includeBody;
        obj['token'] = token;
        obj['types'] = types;
        obj['user'] = user;
    }

    /**
     * Constructs a <code>Subscription</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Subscription} obj Optional instance to populate.
     * @return {module:model/Subscription} The populated <code>Subscription</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Subscription();

            if (data.hasOwnProperty('assignment')) {
                obj['assignment'] = ApiClient.convertToType(data['assignment'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('includeBody')) {
                obj['includeBody'] = ApiClient.convertToType(data['includeBody'], 'Boolean');
            }
            if (data.hasOwnProperty('includeThumbenail')) {
                obj['includeThumbenail'] = ApiClient.convertToType(data['includeThumbenail'], 'Boolean');
            }
            if (data.hasOwnProperty('slackChannel')) {
                obj['slackChannel'] = ApiClient.convertToType(data['slackChannel'], 'String');
            }
            if (data.hasOwnProperty('token')) {
                obj['token'] = ApiClient.convertToType(data['token'], 'String');
            }
            if (data.hasOwnProperty('types')) {
                obj['types'] = ApiClient.convertToType(data['types'], ['String']);
            }
            if (data.hasOwnProperty('user')) {
                obj['user'] = ApiClient.convertToType(data['user'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Subscription</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Subscription</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Subscription.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['assignment'] && !(typeof data['assignment'] === 'string' || data['assignment'] instanceof String)) {
            throw new Error("Expected the field `assignment` to be a primitive type in the JSON string but got " + data['assignment']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['slackChannel'] && !(typeof data['slackChannel'] === 'string' || data['slackChannel'] instanceof String)) {
            throw new Error("Expected the field `slackChannel` to be a primitive type in the JSON string but got " + data['slackChannel']);
        }
        // ensure the json data is a string
        if (data['token'] && !(typeof data['token'] === 'string' || data['token'] instanceof String)) {
            throw new Error("Expected the field `token` to be a primitive type in the JSON string but got " + data['token']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['types'])) {
            throw new Error("Expected the field `types` to be an array in the JSON data but got " + data['types']);
        }
        // ensure the json data is a string
        if (data['user'] && !(typeof data['user'] === 'string' || data['user'] instanceof String)) {
            throw new Error("Expected the field `user` to be a primitive type in the JSON string but got " + data['user']);
        }

        return true;
    }


}

Subscription.RequiredProperties = ["id", "includeBody", "token", "types", "user"];

/**
 * @member {String} assignment
 */
Subscription.prototype['assignment'] = undefined;

/**
 * @member {String} email
 */
Subscription.prototype['email'] = undefined;

/**
 * @member {String} id
 */
Subscription.prototype['id'] = undefined;

/**
 * @member {Boolean} includeBody
 */
Subscription.prototype['includeBody'] = undefined;

/**
 * @member {Boolean} includeThumbenail
 */
Subscription.prototype['includeThumbenail'] = undefined;

/**
 * @member {String} slackChannel
 */
Subscription.prototype['slackChannel'] = undefined;

/**
 * @member {String} token
 */
Subscription.prototype['token'] = undefined;

/**
 * @member {Array.<String>} types
 */
Subscription.prototype['types'] = undefined;

/**
 * @member {String} user
 */
Subscription.prototype['user'] = undefined;






export default Subscription;

