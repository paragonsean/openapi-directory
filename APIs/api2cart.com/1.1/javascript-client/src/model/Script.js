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
import A2CDateTime from './A2CDateTime';

/**
 * The Script model module.
 * @module model/Script
 * @version 1.1
 */
class Script {
    /**
     * Constructs a new <code>Script</code>.
     * @alias module:model/Script
     */
    constructor() { 
        
        Script.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Script</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Script} obj Optional instance to populate.
     * @return {module:model/Script} The populated <code>Script</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Script();

            if (data.hasOwnProperty('additional_fields')) {
                obj['additional_fields'] = ApiClient.convertToType(data['additional_fields'], Object);
            }
            if (data.hasOwnProperty('created_time')) {
                obj['created_time'] = A2CDateTime.constructFromObject(data['created_time']);
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], Object);
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('event')) {
                obj['event'] = ApiClient.convertToType(data['event'], 'String');
            }
            if (data.hasOwnProperty('html')) {
                obj['html'] = ApiClient.convertToType(data['html'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('load_method')) {
                obj['load_method'] = ApiClient.convertToType(data['load_method'], 'String');
            }
            if (data.hasOwnProperty('modified_time')) {
                obj['modified_time'] = A2CDateTime.constructFromObject(data['modified_time']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('scope')) {
                obj['scope'] = ApiClient.convertToType(data['scope'], 'String');
            }
            if (data.hasOwnProperty('src')) {
                obj['src'] = ApiClient.convertToType(data['src'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Script</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Script</code>.
     */
    static validateJSON(data) {
        // validate the optional field `created_time`
        if (data['created_time']) { // data not null
          A2CDateTime.validateJSON(data['created_time']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['event'] && !(typeof data['event'] === 'string' || data['event'] instanceof String)) {
            throw new Error("Expected the field `event` to be a primitive type in the JSON string but got " + data['event']);
        }
        // ensure the json data is a string
        if (data['html'] && !(typeof data['html'] === 'string' || data['html'] instanceof String)) {
            throw new Error("Expected the field `html` to be a primitive type in the JSON string but got " + data['html']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['load_method'] && !(typeof data['load_method'] === 'string' || data['load_method'] instanceof String)) {
            throw new Error("Expected the field `load_method` to be a primitive type in the JSON string but got " + data['load_method']);
        }
        // validate the optional field `modified_time`
        if (data['modified_time']) { // data not null
          A2CDateTime.validateJSON(data['modified_time']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['scope'] && !(typeof data['scope'] === 'string' || data['scope'] instanceof String)) {
            throw new Error("Expected the field `scope` to be a primitive type in the JSON string but got " + data['scope']);
        }
        // ensure the json data is a string
        if (data['src'] && !(typeof data['src'] === 'string' || data['src'] instanceof String)) {
            throw new Error("Expected the field `src` to be a primitive type in the JSON string but got " + data['src']);
        }

        return true;
    }


}



/**
 * @member {Object} additional_fields
 */
Script.prototype['additional_fields'] = undefined;

/**
 * @member {module:model/A2CDateTime} created_time
 */
Script.prototype['created_time'] = undefined;

/**
 * @member {Object} custom_fields
 */
Script.prototype['custom_fields'] = undefined;

/**
 * @member {String} description
 */
Script.prototype['description'] = undefined;

/**
 * @member {String} event
 */
Script.prototype['event'] = undefined;

/**
 * @member {String} html
 */
Script.prototype['html'] = undefined;

/**
 * @member {String} id
 */
Script.prototype['id'] = undefined;

/**
 * @member {String} load_method
 */
Script.prototype['load_method'] = undefined;

/**
 * @member {module:model/A2CDateTime} modified_time
 */
Script.prototype['modified_time'] = undefined;

/**
 * @member {String} name
 */
Script.prototype['name'] = undefined;

/**
 * @member {String} scope
 */
Script.prototype['scope'] = undefined;

/**
 * @member {String} src
 */
Script.prototype['src'] = undefined;






export default Script;

