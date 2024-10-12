/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The BuildArgument model module.
 * @module model/BuildArgument
 * @version 2018-02-01-preview
 */
class BuildArgument {
    /**
     * Constructs a new <code>BuildArgument</code>.
     * Properties of a build argument.
     * @alias module:model/BuildArgument
     * @param name {String} The name of the argument.
     * @param type {module:model/BuildArgument.TypeEnum} The type of the argument.
     * @param value {String} The value of the argument.
     */
    constructor(name, type, value) { 
        
        BuildArgument.initialize(this, name, type, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name, type, value) { 
        obj['isSecret'] = false;
        obj['name'] = name;
        obj['type'] = type;
        obj['value'] = value;
    }

    /**
     * Constructs a <code>BuildArgument</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BuildArgument} obj Optional instance to populate.
     * @return {module:model/BuildArgument} The populated <code>BuildArgument</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BuildArgument();

            if (data.hasOwnProperty('isSecret')) {
                obj['isSecret'] = ApiClient.convertToType(data['isSecret'], 'Boolean');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BuildArgument</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BuildArgument</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BuildArgument.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}

BuildArgument.RequiredProperties = ["name", "type", "value"];

/**
 * Flag to indicate whether the argument represents a secret and want to be removed from build logs.
 * @member {Boolean} isSecret
 * @default false
 */
BuildArgument.prototype['isSecret'] = false;

/**
 * The name of the argument.
 * @member {String} name
 */
BuildArgument.prototype['name'] = undefined;

/**
 * The type of the argument.
 * @member {module:model/BuildArgument.TypeEnum} type
 */
BuildArgument.prototype['type'] = undefined;

/**
 * The value of the argument.
 * @member {String} value
 */
BuildArgument.prototype['value'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
BuildArgument['TypeEnum'] = {

    /**
     * value: "DockerBuildArgument"
     * @const
     */
    "DockerBuildArgument": "DockerBuildArgument"
};



export default BuildArgument;

