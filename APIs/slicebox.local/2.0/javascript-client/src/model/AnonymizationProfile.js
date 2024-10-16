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
import ConfidentialityOption from './ConfidentialityOption';

/**
 * The AnonymizationProfile model module.
 * @module model/AnonymizationProfile
 * @version 2.0
 */
class AnonymizationProfile {
    /**
     * Constructs a new <code>AnonymizationProfile</code>.
     * @alias module:model/AnonymizationProfile
     */
    constructor() { 
        
        AnonymizationProfile.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AnonymizationProfile</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AnonymizationProfile} obj Optional instance to populate.
     * @return {module:model/AnonymizationProfile} The populated <code>AnonymizationProfile</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AnonymizationProfile();

            if (data.hasOwnProperty('options')) {
                obj['options'] = ApiClient.convertToType(data['options'], [ConfidentialityOption]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AnonymizationProfile</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AnonymizationProfile</code>.
     */
    static validateJSON(data) {
        if (data['options']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['options'])) {
                throw new Error("Expected the field `options` to be an array in the JSON data but got " + data['options']);
            }
            // validate the optional field `options` (array)
            for (const item of data['options']) {
                ConfidentialityOption.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ConfidentialityOption>} options
 */
AnonymizationProfile.prototype['options'] = undefined;






export default AnonymizationProfile;

