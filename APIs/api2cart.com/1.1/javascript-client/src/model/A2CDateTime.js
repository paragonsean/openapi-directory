/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The A2CDateTime model module.
 * @module model/A2CDateTime
 * @version 1.1
 */
class A2CDateTime {
    /**
     * Constructs a new <code>A2CDateTime</code>.
     * @alias module:model/A2CDateTime
     */
    constructor() { 
        
        A2CDateTime.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>A2CDateTime</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/A2CDateTime} obj Optional instance to populate.
     * @return {module:model/A2CDateTime} The populated <code>A2CDateTime</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new A2CDateTime();

            if (data.hasOwnProperty('additional_fields')) {
                obj['additional_fields'] = ApiClient.convertToType(data['additional_fields'], Object);
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], Object);
            }
            if (data.hasOwnProperty('format')) {
                obj['format'] = ApiClient.convertToType(data['format'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>A2CDateTime</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>A2CDateTime</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['format'] && !(typeof data['format'] === 'string' || data['format'] instanceof String)) {
            throw new Error("Expected the field `format` to be a primitive type in the JSON string but got " + data['format']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}



/**
 * @member {Object} additional_fields
 */
A2CDateTime.prototype['additional_fields'] = undefined;

/**
 * @member {Object} custom_fields
 */
A2CDateTime.prototype['custom_fields'] = undefined;

/**
 * @member {String} format
 */
A2CDateTime.prototype['format'] = undefined;

/**
 * @member {String} value
 */
A2CDateTime.prototype['value'] = undefined;






export default A2CDateTime;

