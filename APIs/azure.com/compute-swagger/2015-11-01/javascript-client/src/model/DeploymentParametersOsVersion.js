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
 * The DeploymentParametersOsVersion model module.
 * @module model/DeploymentParametersOsVersion
 * @version 2015-11-01
 */
class DeploymentParametersOsVersion {
    /**
     * Constructs a new <code>DeploymentParametersOsVersion</code>.
     * Deployment operation parameters.
     * @alias module:model/DeploymentParametersOsVersion
     * @param value {module:model/DeploymentParametersOsVersion.ValueEnum} The OS version for the VM. This will pick a fully patched image of this given OS version.
     */
    constructor(value) { 
        
        DeploymentParametersOsVersion.initialize(this, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, value) { 
        obj['value'] = value || '14.04.2-LTS';
    }

    /**
     * Constructs a <code>DeploymentParametersOsVersion</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeploymentParametersOsVersion} obj Optional instance to populate.
     * @return {module:model/DeploymentParametersOsVersion} The populated <code>DeploymentParametersOsVersion</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeploymentParametersOsVersion();

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeploymentParametersOsVersion</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeploymentParametersOsVersion</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DeploymentParametersOsVersion.RequiredProperties) {
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

DeploymentParametersOsVersion.RequiredProperties = ["value"];

/**
 * The OS version for the VM. This will pick a fully patched image of this given OS version.
 * @member {module:model/DeploymentParametersOsVersion.ValueEnum} value
 * @default '14.04.2-LTS'
 */
DeploymentParametersOsVersion.prototype['value'] = '14.04.2-LTS';





/**
 * Allowed values for the <code>value</code> property.
 * @enum {String}
 * @readonly
 */
DeploymentParametersOsVersion['ValueEnum'] = {

    /**
     * value: "12.04.5-LTS"
     * @const
     */
    "12.04.5-LTS": "12.04.5-LTS",

    /**
     * value: "14.04.2-LTS"
     * @const
     */
    "14.04.2-LTS": "14.04.2-LTS",

    /**
     * value: "15.10"
     * @const
     */
    "15.10": "15.10"
};



export default DeploymentParametersOsVersion;

