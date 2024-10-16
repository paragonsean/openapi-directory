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
 * The TeamUserResponse model module.
 * @module model/TeamUserResponse
 * @version v0.1
 */
class TeamUserResponse {
    /**
     * Constructs a new <code>TeamUserResponse</code>.
     * @alias module:model/TeamUserResponse
     * @param displayName {String} The full name of the user. Might for example be first and last name
     * @param email {String} The email address of the user
     * @param name {String} The unique name that is used to identify the user.
     * @param role {module:model/TeamUserResponse.RoleEnum} The role of the user has within the team
     */
    constructor(displayName, email, name, role) { 
        
        TeamUserResponse.initialize(this, displayName, email, name, role);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, displayName, email, name, role) { 
        obj['display_name'] = displayName;
        obj['email'] = email;
        obj['name'] = name;
        obj['role'] = role;
    }

    /**
     * Constructs a <code>TeamUserResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TeamUserResponse} obj Optional instance to populate.
     * @return {module:model/TeamUserResponse} The populated <code>TeamUserResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TeamUserResponse();

            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('role')) {
                obj['role'] = ApiClient.convertToType(data['role'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TeamUserResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TeamUserResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TeamUserResponse.RequiredProperties) {
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
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['role'] && !(typeof data['role'] === 'string' || data['role'] instanceof String)) {
            throw new Error("Expected the field `role` to be a primitive type in the JSON string but got " + data['role']);
        }

        return true;
    }


}

TeamUserResponse.RequiredProperties = ["display_name", "email", "name", "role"];

/**
 * The full name of the user. Might for example be first and last name
 * @member {String} display_name
 */
TeamUserResponse.prototype['display_name'] = undefined;

/**
 * The email address of the user
 * @member {String} email
 */
TeamUserResponse.prototype['email'] = undefined;

/**
 * The unique name that is used to identify the user.
 * @member {String} name
 */
TeamUserResponse.prototype['name'] = undefined;

/**
 * The role of the user has within the team
 * @member {module:model/TeamUserResponse.RoleEnum} role
 */
TeamUserResponse.prototype['role'] = undefined;





/**
 * Allowed values for the <code>role</code> property.
 * @enum {String}
 * @readonly
 */
TeamUserResponse['RoleEnum'] = {

    /**
     * value: "maintainer"
     * @const
     */
    "maintainer": "maintainer",

    /**
     * value: "collaborator"
     * @const
     */
    "collaborator": "collaborator"
};



export default TeamUserResponse;

