/**
 * Highways England API
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
 * The Qualities model module.
 * @module model/Qualities
 * @version v1
 */
class Qualities {
    /**
     * Constructs a new <code>Qualities</code>.
     * @alias module:model/Qualities
     */
    constructor() { 
        
        Qualities.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Qualities</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Qualities} obj Optional instance to populate.
     * @return {module:model/Qualities} The populated <code>Qualities</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Qualities();

            if (data.hasOwnProperty('Date')) {
                obj['Date'] = ApiClient.convertToType(data['Date'], 'Date');
            }
            if (data.hasOwnProperty('Quality')) {
                obj['Quality'] = ApiClient.convertToType(data['Quality'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Qualities</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Qualities</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * @member {Date} Date
 */
Qualities.prototype['Date'] = undefined;

/**
 * @member {Number} Quality
 */
Qualities.prototype['Quality'] = undefined;






export default Qualities;

