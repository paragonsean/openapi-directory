/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
import TranslatedString from './TranslatedString';

/**
 * The LocalizedString model module.
 * @module model/LocalizedString
 * @version v1
 */
class LocalizedString {
    /**
     * Constructs a new <code>LocalizedString</code>.
     * @alias module:model/LocalizedString
     */
    constructor() { 
        
        LocalizedString.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LocalizedString</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LocalizedString} obj Optional instance to populate.
     * @return {module:model/LocalizedString} The populated <code>LocalizedString</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LocalizedString();

            if (data.hasOwnProperty('defaultValue')) {
                obj['defaultValue'] = TranslatedString.constructFromObject(data['defaultValue']);
            }
            if (data.hasOwnProperty('kind')) {
                obj['kind'] = ApiClient.convertToType(data['kind'], 'String');
            }
            if (data.hasOwnProperty('translatedValues')) {
                obj['translatedValues'] = ApiClient.convertToType(data['translatedValues'], [TranslatedString]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LocalizedString</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LocalizedString</code>.
     */
    static validateJSON(data) {
        // validate the optional field `defaultValue`
        if (data['defaultValue']) { // data not null
          TranslatedString.validateJSON(data['defaultValue']);
        }
        // ensure the json data is a string
        if (data['kind'] && !(typeof data['kind'] === 'string' || data['kind'] instanceof String)) {
            throw new Error("Expected the field `kind` to be a primitive type in the JSON string but got " + data['kind']);
        }
        if (data['translatedValues']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['translatedValues'])) {
                throw new Error("Expected the field `translatedValues` to be an array in the JSON data but got " + data['translatedValues']);
            }
            // validate the optional field `translatedValues` (array)
            for (const item of data['translatedValues']) {
                TranslatedString.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/TranslatedString} defaultValue
 */
LocalizedString.prototype['defaultValue'] = undefined;

/**
 * Identifies what kind of resource this is. Value: the fixed string `\"walletobjects#localizedString\"`.
 * @member {String} kind
 */
LocalizedString.prototype['kind'] = undefined;

/**
 * Contains the translations for the string.
 * @member {Array.<module:model/TranslatedString>} translatedValues
 */
LocalizedString.prototype['translatedValues'] = undefined;






export default LocalizedString;

