/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AddActionDaemonRequestConfig from './AddActionDaemonRequestConfig';

/**
 * The AddActionDaemonRequest model module.
 * @module model/AddActionDaemonRequest
 * @version 0.4.0
 */
class AddActionDaemonRequest {
    /**
     * Constructs a new <code>AddActionDaemonRequest</code>.
     * @alias module:model/AddActionDaemonRequest
     * @param config {module:model/AddActionDaemonRequestConfig} 
     * @param name {String} 
     * @param type {module:model/AddActionDaemonRequest.TypeEnum} 
     */
    constructor(config, name, type) { 
        
        AddActionDaemonRequest.initialize(this, config, name, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, config, name, type) { 
        obj['config'] = config;
        obj['name'] = name;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>AddActionDaemonRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AddActionDaemonRequest} obj Optional instance to populate.
     * @return {module:model/AddActionDaemonRequest} The populated <code>AddActionDaemonRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AddActionDaemonRequest();

            if (data.hasOwnProperty('config')) {
                obj['config'] = AddActionDaemonRequestConfig.constructFromObject(data['config']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AddActionDaemonRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AddActionDaemonRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AddActionDaemonRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `config`
        if (data['config']) { // data not null
          AddActionDaemonRequestConfig.validateJSON(data['config']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

AddActionDaemonRequest.RequiredProperties = ["config", "name", "type"];

/**
 * @member {module:model/AddActionDaemonRequestConfig} config
 */
AddActionDaemonRequest.prototype['config'] = undefined;

/**
 * @member {String} name
 */
AddActionDaemonRequest.prototype['name'] = undefined;

/**
 * @member {module:model/AddActionDaemonRequest.TypeEnum} type
 */
AddActionDaemonRequest.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
AddActionDaemonRequest['TypeEnum'] = {

    /**
     * value: "daemon"
     * @const
     */
    "daemon": "daemon"
};



export default AddActionDaemonRequest;

