/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AnonymizationProfile from './AnonymizationProfile';
import TagValue from './TagValue';

/**
 * The AnonymizationData model module.
 * @module model/AnonymizationData
 * @version 2.0
 */
class AnonymizationData {
    /**
     * Constructs a new <code>AnonymizationData</code>.
     * @alias module:model/AnonymizationData
     */
    constructor() { 
        
        AnonymizationData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnonymizationData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnonymizationData} obj Optional instance to populate.
     * @return {module:model/AnonymizationData} The populated <code>AnonymizationData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnonymizationData();

            if (data.hasOwnProperty('profile')) {
                obj['profile'] = AnonymizationProfile.constructFromObject(data['profile']);
            }
            if (data.hasOwnProperty('tagValues')) {
                obj['tagValues'] = ApiClient.convertToType(data['tagValues'], [TagValue]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AnonymizationData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AnonymizationData</code>.
     */
    static validateJSON(data) {
        // validate the optional field `profile`
        if (data['profile']) { // data not null
          AnonymizationProfile.validateJSON(data['profile']);
        }
        if (data['tagValues']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['tagValues'])) {
                throw new Error("Expected the field `tagValues` to be an array in the JSON data but got " + data['tagValues']);
            }
            // validate the optional field `tagValues` (array)
            for (const item of data['tagValues']) {
                TagValue.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/AnonymizationProfile} profile
 */
AnonymizationData.prototype['profile'] = undefined;

/**
 * @member {Array.<module:model/TagValue>} tagValues
 */
AnonymizationData.prototype['tagValues'] = undefined;






export default AnonymizationData;

