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

/**
 * The AddActionCombineRequest model module.
 * @module model/AddActionCombineRequest
 * @version 0.4.0
 */
class AddActionCombineRequest {
    /**
     * Constructs a new <code>AddActionCombineRequest</code>.
     * @alias module:model/AddActionCombineRequest
     * @param list {Array.<String>} 
     * @param name {String} 
     */
    constructor(list, name) { 
        
        AddActionCombineRequest.initialize(this, list, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, list, name) { 
        obj['list'] = list;
        obj['name'] = name;
    }

    /**
     * Constructs a <code>AddActionCombineRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AddActionCombineRequest} obj Optional instance to populate.
     * @return {module:model/AddActionCombineRequest} The populated <code>AddActionCombineRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AddActionCombineRequest();

            if (data.hasOwnProperty('list')) {
                obj['list'] = ApiClient.convertToType(data['list'], ['String']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AddActionCombineRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AddActionCombineRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AddActionCombineRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['list'])) {
            throw new Error("Expected the field `list` to be an array in the JSON data but got " + data['list']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}

AddActionCombineRequest.RequiredProperties = ["list", "name"];

/**
 * @member {Array.<String>} list
 */
AddActionCombineRequest.prototype['list'] = undefined;

/**
 * @member {String} name
 */
AddActionCombineRequest.prototype['name'] = undefined;






export default AddActionCombineRequest;

