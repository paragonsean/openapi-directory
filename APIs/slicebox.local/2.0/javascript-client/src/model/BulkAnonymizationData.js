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
import ImageTagValues from './ImageTagValues';

/**
 * The BulkAnonymizationData model module.
 * @module model/BulkAnonymizationData
 * @version 2.0
 */
class BulkAnonymizationData {
    /**
     * Constructs a new <code>BulkAnonymizationData</code>.
     * @alias module:model/BulkAnonymizationData
     */
    constructor() { 
        
        BulkAnonymizationData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BulkAnonymizationData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BulkAnonymizationData} obj Optional instance to populate.
     * @return {module:model/BulkAnonymizationData} The populated <code>BulkAnonymizationData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BulkAnonymizationData();

            if (data.hasOwnProperty('imageTagValuesSet')) {
                obj['imageTagValuesSet'] = ApiClient.convertToType(data['imageTagValuesSet'], [ImageTagValues]);
            }
            if (data.hasOwnProperty('profile')) {
                obj['profile'] = AnonymizationProfile.constructFromObject(data['profile']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BulkAnonymizationData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BulkAnonymizationData</code>.
     */
    static validateJSON(data) {
        if (data['imageTagValuesSet']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['imageTagValuesSet'])) {
                throw new Error("Expected the field `imageTagValuesSet` to be an array in the JSON data but got " + data['imageTagValuesSet']);
            }
            // validate the optional field `imageTagValuesSet` (array)
            for (const item of data['imageTagValuesSet']) {
                ImageTagValues.validateJSON(item);
            };
        }
        // validate the optional field `profile`
        if (data['profile']) { // data not null
          AnonymizationProfile.validateJSON(data['profile']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ImageTagValues>} imageTagValuesSet
 */
BulkAnonymizationData.prototype['imageTagValuesSet'] = undefined;

/**
 * @member {module:model/AnonymizationProfile} profile
 */
BulkAnonymizationData.prototype['profile'] = undefined;






export default BulkAnonymizationData;

