/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UserLiteProfileResponse model module.
 * @module model/UserLiteProfileResponse
 * @version v0.1
 */
class UserLiteProfileResponse {
    /**
     * Constructs a new <code>UserLiteProfileResponse</code>.
     * @alias module:model/UserLiteProfileResponse
     * @param displayName {String} The full name of the user. Might for example be first and last name
     * @param email {String} The email address of the user
     * @param id {String} The unique id (UUID) of the user
     */
    constructor(displayName, email, id) { 
        
        UserLiteProfileResponse.initialize(this, displayName, email, id);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, displayName, email, id) { 
        obj['display_name'] = displayName;
        obj['email'] = email;
        obj['id'] = id;
    }

    /**
     * Constructs a <code>UserLiteProfileResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UserLiteProfileResponse} obj Optional instance to populate.
     * @return {module:model/UserLiteProfileResponse} The populated <code>UserLiteProfileResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UserLiteProfileResponse();

            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UserLiteProfileResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UserLiteProfileResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UserLiteProfileResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['display_name'] && !(typeof data['display_name'] === 'string' || data['display_name'] instanceof String)) {
            throw new Error("Expected the field `display_name` to be a primitive type in the JSON string but got " + data['display_name']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }

        return true;
    }


}

UserLiteProfileResponse.RequiredProperties = ["display_name", "email", "id"];

/**
 * The full name of the user. Might for example be first and last name
 * @member {String} display_name
 */
UserLiteProfileResponse.prototype['display_name'] = undefined;

/**
 * The email address of the user
 * @member {String} email
 */
UserLiteProfileResponse.prototype['email'] = undefined;

/**
 * The unique id (UUID) of the user
 * @member {String} id
 */
UserLiteProfileResponse.prototype['id'] = undefined;






export default UserLiteProfileResponse;

