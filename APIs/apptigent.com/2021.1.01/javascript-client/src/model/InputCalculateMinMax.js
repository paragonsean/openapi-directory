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
 * The InputCalculateMinMax model module.
 * @module model/InputCalculateMinMax
 * @version 2021.1.01
 */
class InputCalculateMinMax {
    /**
     * Constructs a new <code>InputCalculateMinMax</code>.
     * @alias module:model/InputCalculateMinMax
     * @param input {Array.<Number>} Colllection of values to calculate
     * @param type {module:model/InputCalculateMinMax.TypeEnum} Minimum or Maximum
     */
    constructor(input, type) { 
        
        InputCalculateMinMax.initialize(this, input, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, input, type) { 
        obj['input'] = input;
        obj['type'] = type || 'Minimum';
    }

    /**
     * Constructs a <code>InputCalculateMinMax</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InputCalculateMinMax} obj Optional instance to populate.
     * @return {module:model/InputCalculateMinMax} The populated <code>InputCalculateMinMax</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InputCalculateMinMax();

            if (data.hasOwnProperty('input')) {
                obj['input'] = ApiClient.convertToType(data['input'], ['Number']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>InputCalculateMinMax</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>InputCalculateMinMax</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of InputCalculateMinMax.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['input'])) {
            throw new Error("Expected the field `input` to be an array in the JSON data but got " + data['input']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

InputCalculateMinMax.RequiredProperties = ["input", "type"];

/**
 * Colllection of values to calculate
 * @member {Array.<Number>} input
 */
InputCalculateMinMax.prototype['input'] = undefined;

/**
 * Minimum or Maximum
 * @member {module:model/InputCalculateMinMax.TypeEnum} type
 * @default 'Minimum'
 */
InputCalculateMinMax.prototype['type'] = 'Minimum';





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
InputCalculateMinMax['TypeEnum'] = {

    /**
     * value: "Minimum"
     * @const
     */
    "Minimum": "Minimum",

    /**
     * value: "Maximum"
     * @const
     */
    "Maximum": "Maximum"
};



export default InputCalculateMinMax;

