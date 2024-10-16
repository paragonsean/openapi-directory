/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The APIModelsUserRoleChange model module.
 * @module model/APIModelsUserRoleChange
 * @version v1
 */
class APIModelsUserRoleChange {
    /**
     * Constructs a new <code>APIModelsUserRoleChange</code>.
     * @alias module:model/APIModelsUserRoleChange
     * @param action {module:model/APIModelsUserRoleChange.ActionEnum} The action to take with the role
     * @param name {String} The name of the role
     */
    constructor(action, name) { 
        
        APIModelsUserRoleChange.initialize(this, action, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, action, name) { 
        obj['Action'] = action;
        obj['Name'] = name;
    }

    /**
     * Constructs a <code>APIModelsUserRoleChange</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/APIModelsUserRoleChange} obj Optional instance to populate.
     * @return {module:model/APIModelsUserRoleChange} The populated <code>APIModelsUserRoleChange</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new APIModelsUserRoleChange();

            if (data.hasOwnProperty('Action')) {
                obj['Action'] = ApiClient.convertToType(data['Action'], 'String');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>APIModelsUserRoleChange</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>APIModelsUserRoleChange</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of APIModelsUserRoleChange.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['Action'] && !(typeof data['Action'] === 'string' || data['Action'] instanceof String)) {
            throw new Error("Expected the field `Action` to be a primitive type in the JSON string but got " + data['Action']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }

        return true;
    }


}

APIModelsUserRoleChange.RequiredProperties = ["Action", "Name"];

/**
 * The action to take with the role
 * @member {module:model/APIModelsUserRoleChange.ActionEnum} Action
 */
APIModelsUserRoleChange.prototype['Action'] = undefined;

/**
 * The name of the role
 * @member {String} Name
 */
APIModelsUserRoleChange.prototype['Name'] = undefined;





/**
 * Allowed values for the <code>Action</code> property.
 * @enum {String}
 * @readonly
 */
APIModelsUserRoleChange['ActionEnum'] = {

    /**
     * value: "Grant"
     * @const
     */
    "Grant": "Grant",

    /**
     * value: "Revoke"
     * @const
     */
    "Revoke": "Revoke"
};



export default APIModelsUserRoleChange;

