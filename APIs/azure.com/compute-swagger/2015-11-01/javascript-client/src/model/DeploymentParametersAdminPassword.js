/**
 * ComputeManagementConvenienceClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The DeploymentParametersAdminPassword model module.
 * @module model/DeploymentParametersAdminPassword
 * @version 2015-11-01
 */
class DeploymentParametersAdminPassword {
    /**
     * Constructs a new <code>DeploymentParametersAdminPassword</code>.
     * @alias module:model/DeploymentParametersAdminPassword
     * @param value {String} Password for the Virtual Machine.
     */
    constructor(value) { 
        
        DeploymentParametersAdminPassword.initialize(this, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, value) { 
        obj['value'] = value;
    }

    /**
     * Constructs a <code>DeploymentParametersAdminPassword</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeploymentParametersAdminPassword} obj Optional instance to populate.
     * @return {module:model/DeploymentParametersAdminPassword} The populated <code>DeploymentParametersAdminPassword</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeploymentParametersAdminPassword();

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeploymentParametersAdminPassword</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeploymentParametersAdminPassword</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DeploymentParametersAdminPassword.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}

DeploymentParametersAdminPassword.RequiredProperties = ["value"];

/**
 * Password for the Virtual Machine.
 * @member {String} value
 */
DeploymentParametersAdminPassword.prototype['value'] = undefined;






export default DeploymentParametersAdminPassword;

