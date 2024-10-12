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
 * The APIModelsRoleUserChange model module.
 * @module model/APIModelsRoleUserChange
 * @version v1
 */
class APIModelsRoleUserChange {
    /**
     * Constructs a new <code>APIModelsRoleUserChange</code>.
     * @alias module:model/APIModelsRoleUserChange
     * @param action {module:model/APIModelsRoleUserChange.ActionEnum} The action to take with the user
     * @param id {Number} The Id of the User
     */
    constructor(action, id) { 
        
        APIModelsRoleUserChange.initialize(this, action, id);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, action, id) { 
        obj['Action'] = action;
        obj['Id'] = id;
    }

    /**
     * Constructs a <code>APIModelsRoleUserChange</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/APIModelsRoleUserChange} obj Optional instance to populate.
     * @return {module:model/APIModelsRoleUserChange} The populated <code>APIModelsRoleUserChange</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new APIModelsRoleUserChange();

            if (data.hasOwnProperty('Action')) {
                obj['Action'] = ApiClient.convertToType(data['Action'], 'String');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>APIModelsRoleUserChange</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>APIModelsRoleUserChange</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of APIModelsRoleUserChange.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['Action'] && !(typeof data['Action'] === 'string' || data['Action'] instanceof String)) {
            throw new Error("Expected the field `Action` to be a primitive type in the JSON string but got " + data['Action']);
        }

        return true;
    }


}

APIModelsRoleUserChange.RequiredProperties = ["Action", "Id"];

/**
 * The action to take with the user
 * @member {module:model/APIModelsRoleUserChange.ActionEnum} Action
 */
APIModelsRoleUserChange.prototype['Action'] = undefined;

/**
 * The Id of the User
 * @member {Number} Id
 */
APIModelsRoleUserChange.prototype['Id'] = undefined;





/**
 * Allowed values for the <code>Action</code> property.
 * @enum {String}
 * @readonly
 */
APIModelsRoleUserChange['ActionEnum'] = {

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



export default APIModelsRoleUserChange;

