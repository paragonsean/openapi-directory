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
 * The InputCollectionFilter model module.
 * @module model/InputCollectionFilter
 * @version 2021.1.01
 */
class InputCollectionFilter {
    /**
     * Constructs a new <code>InputCollectionFilter</code>.
     * @alias module:model/InputCollectionFilter
     * @param input {Array.<String>} Collection of strings to filter
     * @param keywords {String} Keywords (separate multiple values with commas)
     * @param match {module:model/InputCollectionFilter.MatchEnum} Match type
     */
    constructor(input, keywords, match) { 
        
        InputCollectionFilter.initialize(this, input, keywords, match);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, input, keywords, match) { 
        obj['input'] = input;
        obj['keywords'] = keywords;
        obj['match'] = match || 'Any';
    }

    /**
     * Constructs a <code>InputCollectionFilter</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InputCollectionFilter} obj Optional instance to populate.
     * @return {module:model/InputCollectionFilter} The populated <code>InputCollectionFilter</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InputCollectionFilter();

            if (data.hasOwnProperty('input')) {
                obj['input'] = ApiClient.convertToType(data['input'], ['String']);
            }
            if (data.hasOwnProperty('keywords')) {
                obj['keywords'] = ApiClient.convertToType(data['keywords'], 'String');
            }
            if (data.hasOwnProperty('match')) {
                obj['match'] = ApiClient.convertToType(data['match'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>InputCollectionFilter</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>InputCollectionFilter</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of InputCollectionFilter.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['input'])) {
            throw new Error("Expected the field `input` to be an array in the JSON data but got " + data['input']);
        }
        // ensure the json data is a string
        if (data['keywords'] && !(typeof data['keywords'] === 'string' || data['keywords'] instanceof String)) {
            throw new Error("Expected the field `keywords` to be a primitive type in the JSON string but got " + data['keywords']);
        }
        // ensure the json data is a string
        if (data['match'] && !(typeof data['match'] === 'string' || data['match'] instanceof String)) {
            throw new Error("Expected the field `match` to be a primitive type in the JSON string but got " + data['match']);
        }

        return true;
    }


}

InputCollectionFilter.RequiredProperties = ["input", "keywords", "match"];

/**
 * Collection of strings to filter
 * @member {Array.<String>} input
 */
InputCollectionFilter.prototype['input'] = undefined;

/**
 * Keywords (separate multiple values with commas)
 * @member {String} keywords
 */
InputCollectionFilter.prototype['keywords'] = undefined;

/**
 * Match type
 * @member {module:model/InputCollectionFilter.MatchEnum} match
 * @default 'Any'
 */
InputCollectionFilter.prototype['match'] = 'Any';





/**
 * Allowed values for the <code>match</code> property.
 * @enum {String}
 * @readonly
 */
InputCollectionFilter['MatchEnum'] = {

    /**
     * value: "Any"
     * @const
     */
    "Any": "Any",

    /**
     * value: "All"
     * @const
     */
    "All": "All",

    /**
     * value: "None"
     * @const
     */
    "None": "None"
};



export default InputCollectionFilter;

