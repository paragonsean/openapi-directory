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
 * The InputTranslateString model module.
 * @module model/InputTranslateString
 * @version 2021.1.01
 */
class InputTranslateString {
    /**
     * Constructs a new <code>InputTranslateString</code>.
     * @alias module:model/InputTranslateString
     * @param input {String} String containing the text to be translated
     * @param language {module:model/InputTranslateString.LanguageEnum} Translation language
     */
    constructor(input, language) { 
        
        InputTranslateString.initialize(this, input, language);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, input, language) { 
        obj['input'] = input;
        obj['language'] = language;
    }

    /**
     * Constructs a <code>InputTranslateString</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InputTranslateString} obj Optional instance to populate.
     * @return {module:model/InputTranslateString} The populated <code>InputTranslateString</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InputTranslateString();

            if (data.hasOwnProperty('input')) {
                obj['input'] = ApiClient.convertToType(data['input'], 'String');
            }
            if (data.hasOwnProperty('language')) {
                obj['language'] = ApiClient.convertToType(data['language'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>InputTranslateString</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>InputTranslateString</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of InputTranslateString.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['input'] && !(typeof data['input'] === 'string' || data['input'] instanceof String)) {
            throw new Error("Expected the field `input` to be a primitive type in the JSON string but got " + data['input']);
        }
        // ensure the json data is a string
        if (data['language'] && !(typeof data['language'] === 'string' || data['language'] instanceof String)) {
            throw new Error("Expected the field `language` to be a primitive type in the JSON string but got " + data['language']);
        }

        return true;
    }


}

InputTranslateString.RequiredProperties = ["input", "language"];

/**
 * String containing the text to be translated
 * @member {String} input
 */
InputTranslateString.prototype['input'] = undefined;

/**
 * Translation language
 * @member {module:model/InputTranslateString.LanguageEnum} language
 */
InputTranslateString.prototype['language'] = undefined;





/**
 * Allowed values for the <code>language</code> property.
 * @enum {String}
 * @readonly
 */
InputTranslateString['LanguageEnum'] = {

    /**
     * value: "Arabic"
     * @const
     */
    "Arabic": "Arabic",

    /**
     * value: "Chinese (Simplified)"
     * @const
     */
    "Chinese (Simplified)": "Chinese (Simplified)",

    /**
     * value: "Czech"
     * @const
     */
    "Czech": "Czech",

    /**
     * value: "Danish"
     * @const
     */
    "Danish": "Danish",

    /**
     * value: "Dutch"
     * @const
     */
    "Dutch": "Dutch",

    /**
     * value: "English"
     * @const
     */
    "English": "English",

    /**
     * value: "Finnish"
     * @const
     */
    "Finnish": "Finnish",

    /**
     * value: "French"
     * @const
     */
    "French": "French",

    /**
     * value: "German"
     * @const
     */
    "German": "German",

    /**
     * value: "Greek"
     * @const
     */
    "Greek": "Greek",

    /**
     * value: "Hindi"
     * @const
     */
    "Hindi": "Hindi",

    /**
     * value: "Hungarian"
     * @const
     */
    "Hungarian": "Hungarian",

    /**
     * value: "Italian"
     * @const
     */
    "Italian": "Italian",

    /**
     * value: "Japanese"
     * @const
     */
    "Japanese": "Japanese",

    /**
     * value: "Klingon"
     * @const
     */
    "Klingon": "Klingon",

    /**
     * value: "Korean"
     * @const
     */
    "Korean": "Korean",

    /**
     * value: "Norweigan"
     * @const
     */
    "Norweigan": "Norweigan",

    /**
     * value: "Polish"
     * @const
     */
    "Polish": "Polish",

    /**
     * value: "Portuguese"
     * @const
     */
    "Portuguese": "Portuguese",

    /**
     * value: "Russian"
     * @const
     */
    "Russian": "Russian",

    /**
     * value: "Spanish"
     * @const
     */
    "Spanish": "Spanish",

    /**
     * value: "Swedish"
     * @const
     */
    "Swedish": "Swedish",

    /**
     * value: "Turkish"
     * @const
     */
    "Turkish": "Turkish",

    /**
     * value: "Vietnamese"
     * @const
     */
    "Vietnamese": "Vietnamese",

    /**
     * value: "Welsh"
     * @const
     */
    "Welsh": "Welsh"
};



export default InputTranslateString;

