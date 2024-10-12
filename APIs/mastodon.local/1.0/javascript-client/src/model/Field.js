/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Field model module.
 * @module model/Field
 * @version 1.0
 */
class Field {
    /**
     * Constructs a new <code>Field</code>.
     * Represents a profile field as a name-value pair with optional verification.
     * @alias module:model/Field
     */
    constructor() { 
        
        Field.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Field</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Field} obj Optional instance to populate.
     * @return {module:model/Field} The populated <code>Field</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Field();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
            if (data.hasOwnProperty('verified_at')) {
                obj['verified_at'] = ApiClient.convertToType(data['verified_at'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Field</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Field</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}



/**
 * The key of a given field's key-value pair.
 * @member {String} name
 */
Field.prototype['name'] = undefined;

/**
 * The value associated with the `name` key.
 * @member {String} value
 */
Field.prototype['value'] = undefined;

/**
 * Timestamp of when the server verified a URL value for a rel=\"me” link. If `value` is a verified URL. Otherwise, null
 * @member {Date} verified_at
 */
Field.prototype['verified_at'] = undefined;






export default Field;

