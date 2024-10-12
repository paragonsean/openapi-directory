/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ContentLanguageSelection from './ContentLanguageSelection';

/**
 * The LocalizedStringContract model module.
 * @module model/LocalizedStringContract
 * @version 1.0
 */
class LocalizedStringContract {
    /**
     * Constructs a new <code>LocalizedStringContract</code>.
     * @alias module:model/LocalizedStringContract
     */
    constructor() { 
        
        LocalizedStringContract.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>LocalizedStringContract</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LocalizedStringContract} obj Optional instance to populate.
     * @return {module:model/LocalizedStringContract} The populated <code>LocalizedStringContract</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LocalizedStringContract();

            if (data.hasOwnProperty('language')) {
                obj['language'] = ContentLanguageSelection.constructFromObject(data['language']);
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LocalizedStringContract</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LocalizedStringContract</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}



/**
 * @member {module:model/ContentLanguageSelection} language
 */
LocalizedStringContract.prototype['language'] = undefined;

/**
 * @member {String} value
 */
LocalizedStringContract.prototype['value'] = undefined;






export default LocalizedStringContract;

