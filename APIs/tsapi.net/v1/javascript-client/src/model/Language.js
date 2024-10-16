/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Language model module.
 * @module model/Language
 * @version v1
 */
class Language {
    /**
     * Constructs a new <code>Language</code>.
     * @alias module:model/Language
     */
    constructor() { 
        
        Language.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Language</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Language} obj Optional instance to populate.
     * @return {module:model/Language} The populated <code>Language</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Language();

            if (data.hasOwnProperty('ident')) {
                obj['ident'] = ApiClient.convertToType(data['ident'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('subLanguages')) {
                obj['subLanguages'] = ApiClient.convertToType(data['subLanguages'], [Language]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Language</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Language</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['ident'] && !(typeof data['ident'] === 'string' || data['ident'] instanceof String)) {
            throw new Error("Expected the field `ident` to be a primitive type in the JSON string but got " + data['ident']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        if (data['subLanguages']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['subLanguages'])) {
                throw new Error("Expected the field `subLanguages` to be an array in the JSON data but got " + data['subLanguages']);
            }
            // validate the optional field `subLanguages` (array)
            for (const item of data['subLanguages']) {
                Language.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {String} ident
 */
Language.prototype['ident'] = undefined;

/**
 * @member {String} name
 */
Language.prototype['name'] = undefined;

/**
 * @member {Array.<module:model/Language>} subLanguages
 */
Language.prototype['subLanguages'] = undefined;






export default Language;

