/**
 * Adobe Experience Manager (AEM) API
 * Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 *
 * The version of the OpenAPI document: 3.7.1-pre.0
 * Contact: opensource@shinesolutions.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The SamlConfigurationPropertyItemsArray model module.
 * @module model/SamlConfigurationPropertyItemsArray
 * @version 3.7.1-pre.0
 */
class SamlConfigurationPropertyItemsArray {
    /**
     * Constructs a new <code>SamlConfigurationPropertyItemsArray</code>.
     * @alias module:model/SamlConfigurationPropertyItemsArray
     */
    constructor() { 
        
        SamlConfigurationPropertyItemsArray.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SamlConfigurationPropertyItemsArray</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SamlConfigurationPropertyItemsArray} obj Optional instance to populate.
     * @return {module:model/SamlConfigurationPropertyItemsArray} The populated <code>SamlConfigurationPropertyItemsArray</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SamlConfigurationPropertyItemsArray();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('is_set')) {
                obj['is_set'] = ApiClient.convertToType(data['is_set'], 'Boolean');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('optional')) {
                obj['optional'] = ApiClient.convertToType(data['optional'], 'Boolean');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'Number');
            }
            if (data.hasOwnProperty('values')) {
                obj['values'] = ApiClient.convertToType(data['values'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SamlConfigurationPropertyItemsArray</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SamlConfigurationPropertyItemsArray</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['values'])) {
            throw new Error("Expected the field `values` to be an array in the JSON data but got " + data['values']);
        }

        return true;
    }


}



/**
 * Property description
 * @member {String} description
 */
SamlConfigurationPropertyItemsArray.prototype['description'] = undefined;

/**
 * True if property is set
 * @member {Boolean} is_set
 */
SamlConfigurationPropertyItemsArray.prototype['is_set'] = undefined;

/**
 * property name
 * @member {String} name
 */
SamlConfigurationPropertyItemsArray.prototype['name'] = undefined;

/**
 * True if optional
 * @member {Boolean} optional
 */
SamlConfigurationPropertyItemsArray.prototype['optional'] = undefined;

/**
 * Property type, 1=String, 3=long, 11=boolean, 12=Password
 * @member {Number} type
 */
SamlConfigurationPropertyItemsArray.prototype['type'] = undefined;

/**
 * Property value
 * @member {Array.<String>} values
 */
SamlConfigurationPropertyItemsArray.prototype['values'] = undefined;






export default SamlConfigurationPropertyItemsArray;

