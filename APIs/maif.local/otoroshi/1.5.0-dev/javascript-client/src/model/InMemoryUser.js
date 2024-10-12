/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The InMemoryUser model module.
 * @module model/InMemoryUser
 * @version 1.5.0-dev
 */
class InMemoryUser {
    /**
     * Constructs a new <code>InMemoryUser</code>.
     * A user
     * @alias module:model/InMemoryUser
     * @param email {String} Email of the user
     * @param metadata {Object.<String, String>} Metadata of the user
     * @param name {String} Name of the user
     * @param password {String} Password of the user (BCrypt hash)
     */
    constructor(email, metadata, name, password) { 
        
        InMemoryUser.initialize(this, email, metadata, name, password);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, email, metadata, name, password) { 
        obj['email'] = email;
        obj['metadata'] = metadata;
        obj['name'] = name;
        obj['password'] = password;
    }

    /**
     * Constructs a <code>InMemoryUser</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InMemoryUser} obj Optional instance to populate.
     * @return {module:model/InMemoryUser} The populated <code>InMemoryUser</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InMemoryUser();

            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('metadata')) {
                obj['metadata'] = ApiClient.convertToType(data['metadata'], {'String': 'String'});
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>InMemoryUser</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>InMemoryUser</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of InMemoryUser.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }

        return true;
    }


}

InMemoryUser.RequiredProperties = ["email", "metadata", "name", "password"];

/**
 * Email of the user
 * @member {String} email
 */
InMemoryUser.prototype['email'] = undefined;

/**
 * Metadata of the user
 * @member {Object.<String, String>} metadata
 */
InMemoryUser.prototype['metadata'] = undefined;

/**
 * Name of the user
 * @member {String} name
 */
InMemoryUser.prototype['name'] = undefined;

/**
 * Password of the user (BCrypt hash)
 * @member {String} password
 */
InMemoryUser.prototype['password'] = undefined;






export default InMemoryUser;

