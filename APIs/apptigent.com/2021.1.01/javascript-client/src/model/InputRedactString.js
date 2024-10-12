/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The InputRedactString model module.
 * @module model/InputRedactString
 * @version 2021.1.01
 */
class InputRedactString {
    /**
     * Constructs a new <code>InputRedactString</code>.
     * @alias module:model/InputRedactString
     * @param source {String} String containing the complete text
     */
    constructor(source) { 
        
        InputRedactString.initialize(this, source);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, source) { 
        obj['source'] = source;
    }

    /**
     * Constructs a <code>InputRedactString</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InputRedactString} obj Optional instance to populate.
     * @return {module:model/InputRedactString} The populated <code>InputRedactString</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InputRedactString();

            if (data.hasOwnProperty('regex')) {
                obj['regex'] = ApiClient.convertToType(data['regex'], 'String');
            }
            if (data.hasOwnProperty('source')) {
                obj['source'] = ApiClient.convertToType(data['source'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
            if (data.hasOwnProperty('values')) {
                obj['values'] = ApiClient.convertToType(data['values'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>InputRedactString</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>InputRedactString</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of InputRedactString.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['regex'] && !(typeof data['regex'] === 'string' || data['regex'] instanceof String)) {
            throw new Error("Expected the field `regex` to be a primitive type in the JSON string but got " + data['regex']);
        }
        // ensure the json data is a string
        if (data['source'] && !(typeof data['source'] === 'string' || data['source'] instanceof String)) {
            throw new Error("Expected the field `source` to be a primitive type in the JSON string but got " + data['source']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['values'])) {
            throw new Error("Expected the field `values` to be an array in the JSON data but got " + data['values']);
        }

        return true;
    }


}

InputRedactString.RequiredProperties = ["source"];

/**
 * Regular expression pattern for matching strings
 * @member {String} regex
 */
InputRedactString.prototype['regex'] = undefined;

/**
 * String containing the complete text
 * @member {String} source
 */
InputRedactString.prototype['source'] = undefined;

/**
 * Individual string to redact
 * @member {String} value
 */
InputRedactString.prototype['value'] = undefined;

/**
 * Collection of strings to redact
 * @member {Array.<String>} values
 */
InputRedactString.prototype['values'] = undefined;






export default InputRedactString;

