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
 * The Plugin model module.
 * @module model/Plugin
 * @version 1.1
 */
class Plugin {
    /**
     * Constructs a new <code>Plugin</code>.
     * @alias module:model/Plugin
     */
    constructor() { 
        
        Plugin.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Plugin</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Plugin} obj Optional instance to populate.
     * @return {module:model/Plugin} The populated <code>Plugin</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Plugin();

            if (data.hasOwnProperty('active')) {
                obj['active'] = ApiClient.convertToType(data['active'], 'Boolean');
            }
            if (data.hasOwnProperty('additional_fields')) {
                obj['additional_fields'] = ApiClient.convertToType(data['additional_fields'], Object);
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], Object);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Plugin</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Plugin</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {Boolean} active
 */
Plugin.prototype['active'] = undefined;

/**
 * @member {Object} additional_fields
 */
Plugin.prototype['additional_fields'] = undefined;

/**
 * @member {Object} custom_fields
 */
Plugin.prototype['custom_fields'] = undefined;

/**
 * @member {String} name
 */
Plugin.prototype['name'] = undefined;






export default Plugin;

