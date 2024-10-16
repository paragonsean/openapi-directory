/**
 * LH Public API
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

/**
 * The Name model module.
 * @module model/Name
 * @version 1.0
 */
class Name {
    /**
     * Constructs a new <code>Name</code>.
     * 2-letter ISO 639-1 language code for the corresponding item.
     * @alias module:model/Name
     */
    constructor() { 
        
        Name.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Name</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Name} obj Optional instance to populate.
     * @return {module:model/Name} The populated <code>Name</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Name();

            if (data.hasOwnProperty('$')) {
                obj['$'] = ApiClient.convertToType(data['$'], 'String');
            }
            if (data.hasOwnProperty('@LanguageCode')) {
                obj['@LanguageCode'] = ApiClient.convertToType(data['@LanguageCode'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Name</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Name</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['$'] && !(typeof data['$'] === 'string' || data['$'] instanceof String)) {
            throw new Error("Expected the field `$` to be a primitive type in the JSON string but got " + data['$']);
        }
        // ensure the json data is a string
        if (data['@LanguageCode'] && !(typeof data['@LanguageCode'] === 'string' || data['@LanguageCode'] instanceof String)) {
            throw new Error("Expected the field `@LanguageCode` to be a primitive type in the JSON string but got " + data['@LanguageCode']);
        }

        return true;
    }


}



/**
 * @member {String} $
 */
Name.prototype['$'] = undefined;

/**
 * @member {String} @LanguageCode
 */
Name.prototype['@LanguageCode'] = undefined;






export default Name;

