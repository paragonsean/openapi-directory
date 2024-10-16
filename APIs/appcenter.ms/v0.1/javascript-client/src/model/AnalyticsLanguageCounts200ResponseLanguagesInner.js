/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AnalyticsLanguageCounts200ResponseLanguagesInner model module.
 * @module model/AnalyticsLanguageCounts200ResponseLanguagesInner
 * @version v0.1
 */
class AnalyticsLanguageCounts200ResponseLanguagesInner {
    /**
     * Constructs a new <code>AnalyticsLanguageCounts200ResponseLanguagesInner</code>.
     * @alias module:model/AnalyticsLanguageCounts200ResponseLanguagesInner
     */
    constructor() { 
        
        AnalyticsLanguageCounts200ResponseLanguagesInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnalyticsLanguageCounts200ResponseLanguagesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnalyticsLanguageCounts200ResponseLanguagesInner} obj Optional instance to populate.
     * @return {module:model/AnalyticsLanguageCounts200ResponseLanguagesInner} The populated <code>AnalyticsLanguageCounts200ResponseLanguagesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnalyticsLanguageCounts200ResponseLanguagesInner();

            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('language_name')) {
                obj['language_name'] = ApiClient.convertToType(data['language_name'], 'String');
            }
            if (data.hasOwnProperty('previous_count')) {
                obj['previous_count'] = ApiClient.convertToType(data['previous_count'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AnalyticsLanguageCounts200ResponseLanguagesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AnalyticsLanguageCounts200ResponseLanguagesInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['language_name'] && !(typeof data['language_name'] === 'string' || data['language_name'] instanceof String)) {
            throw new Error("Expected the field `language_name` to be a primitive type in the JSON string but got " + data['language_name']);
        }

        return true;
    }


}



/**
 * Count current of language.
 * @member {Number} count
 */
AnalyticsLanguageCounts200ResponseLanguagesInner.prototype['count'] = undefined;

/**
 * Language's name.
 * @member {String} language_name
 */
AnalyticsLanguageCounts200ResponseLanguagesInner.prototype['language_name'] = undefined;

/**
 * Count of previous lanugage.
 * @member {Number} previous_count
 */
AnalyticsLanguageCounts200ResponseLanguagesInner.prototype['previous_count'] = undefined;






export default AnalyticsLanguageCounts200ResponseLanguagesInner;

