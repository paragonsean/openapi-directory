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
import AddActionSendRequestConfig from './AddActionSendRequestConfig';

/**
 * The AddActionSendRequest model module.
 * @module model/AddActionSendRequest
 * @version 0.4.0
 */
class AddActionSendRequest {
    /**
     * Constructs a new <code>AddActionSendRequest</code>.
     * @alias module:model/AddActionSendRequest
     * @param config {module:model/AddActionSendRequestConfig} 
     * @param name {String} 
     * @param type {module:model/AddActionSendRequest.TypeEnum} 
     */
    constructor(config, name, type) { 
        
        AddActionSendRequest.initialize(this, config, name, type);
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
     * Constructs a <code>AddActionSendRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AddActionSendRequest} obj Optional instance to populate.
     * @return {module:model/AddActionSendRequest} The populated <code>AddActionSendRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AddActionSendRequest();

            if (data.hasOwnProperty('config')) {
                obj['config'] = AddActionSendRequestConfig.constructFromObject(data['config']);
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
     * Validates the JSON data with respect to <code>AddActionSendRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AddActionSendRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AddActionSendRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `config`
        if (data['config']) { // data not null
          AddActionSendRequestConfig.validateJSON(data['config']);
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

AddActionSendRequest.RequiredProperties = ["config", "name", "type"];

/**
 * @member {module:model/AddActionSendRequestConfig} config
 */
AddActionSendRequest.prototype['config'] = undefined;

/**
 * @member {String} name
 */
AddActionSendRequest.prototype['name'] = undefined;

/**
 * @member {module:model/AddActionSendRequest.TypeEnum} type
 */
AddActionSendRequest.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
AddActionSendRequest['TypeEnum'] = {

    /**
     * value: "mailscript-email"
     * @const
     */
    "mailscript-email": "mailscript-email"
};



export default AddActionSendRequest;

