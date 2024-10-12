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

/**
 * The VnetValidationTestFailure model module.
 * @module model/VnetValidationTestFailure
 * @version 2016-03-01
 */
class VnetValidationTestFailure {
    /**
     * Constructs a new <code>VnetValidationTestFailure</code>.
     * A class that describes a test that failed during NSG and UDR validation.
     * @alias module:model/VnetValidationTestFailure
     */
    constructor() { 
        
        VnetValidationTestFailure.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>VnetValidationTestFailure</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VnetValidationTestFailure} obj Optional instance to populate.
     * @return {module:model/VnetValidationTestFailure} The populated <code>VnetValidationTestFailure</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VnetValidationTestFailure();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ApiClient.convertToType(data['properties'], Object);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('kind')) {
                obj['kind'] = ApiClient.convertToType(data['kind'], 'String');
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
     * Validates the JSON data with respect to <code>VnetValidationTestFailure</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VnetValidationTestFailure</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          Object.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['kind'] && !(typeof data['kind'] === 'string' || data['kind'] instanceof String)) {
            throw new Error("Expected the field `kind` to be a primitive type in the JSON string but got " + data['kind']);
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



/**
 * VnetValidationTestFailure resource specific properties
 * @member {Object} properties
 */
VnetValidationTestFailure.prototype['properties'] = undefined;

/**
 * Resource Id.
 * @member {String} id
 */
VnetValidationTestFailure.prototype['id'] = undefined;

/**
 * Kind of resource.
 * @member {String} kind
 */
VnetValidationTestFailure.prototype['kind'] = undefined;

/**
 * Resource Name.
 * @member {String} name
 */
VnetValidationTestFailure.prototype['name'] = undefined;

/**
 * Resource type.
 * @member {String} type
 */
VnetValidationTestFailure.prototype['type'] = undefined;






export default VnetValidationTestFailure;

