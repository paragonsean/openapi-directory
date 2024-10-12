/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ValidateProperties from './ValidateProperties';

/**
 * The ValidateRequest model module.
 * @module model/ValidateRequest
 * @version 2016-03-01
 */
class ValidateRequest {
    /**
     * Constructs a new <code>ValidateRequest</code>.
     * Resource validation request content.
     * @alias module:model/ValidateRequest
     * @param location {String} Expected location of the resource.
     * @param name {String} Resource name to verify.
     * @param properties {module:model/ValidateProperties} 
     * @param type {module:model/ValidateRequest.TypeEnum} Resource type used for verification.
     */
    constructor(location, name, properties, type) { 
        
        ValidateRequest.initialize(this, location, name, properties, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, location, name, properties, type) { 
        obj['location'] = location;
        obj['name'] = name;
        obj['properties'] = properties;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>ValidateRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ValidateRequest} obj Optional instance to populate.
     * @return {module:model/ValidateRequest} The populated <code>ValidateRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ValidateRequest();

            if (data.hasOwnProperty('location')) {
                obj['location'] = ApiClient.convertToType(data['location'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ValidateProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ValidateRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ValidateRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ValidateRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['location'] && !(typeof data['location'] === 'string' || data['location'] instanceof String)) {
            throw new Error("Expected the field `location` to be a primitive type in the JSON string but got " + data['location']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          ValidateProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

ValidateRequest.RequiredProperties = ["location", "name", "properties", "type"];

/**
 * Expected location of the resource.
 * @member {String} location
 */
ValidateRequest.prototype['location'] = undefined;

/**
 * Resource name to verify.
 * @member {String} name
 */
ValidateRequest.prototype['name'] = undefined;

/**
 * @member {module:model/ValidateProperties} properties
 */
ValidateRequest.prototype['properties'] = undefined;

/**
 * Resource type used for verification.
 * @member {module:model/ValidateRequest.TypeEnum} type
 */
ValidateRequest.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
ValidateRequest['TypeEnum'] = {

    /**
     * value: "ServerFarm"
     * @const
     */
    "ServerFarm": "ServerFarm",

    /**
     * value: "Site"
     * @const
     */
    "Site": "Site"
};



export default ValidateRequest;

