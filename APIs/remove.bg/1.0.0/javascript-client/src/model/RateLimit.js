/**
 * Background Removal API
 * Remove the background of any image
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import RateLimitErrorsInner from './RateLimitErrorsInner';

/**
 * The RateLimit model module.
 * @module model/RateLimit
 * @version 1.0.0
 */
class RateLimit {
    /**
     * Constructs a new <code>RateLimit</code>.
     * @alias module:model/RateLimit
     */
    constructor() { 
        
        RateLimit.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RateLimit</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RateLimit} obj Optional instance to populate.
     * @return {module:model/RateLimit} The populated <code>RateLimit</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RateLimit();

            if (data.hasOwnProperty('errors')) {
                obj['errors'] = ApiClient.convertToType(data['errors'], [RateLimitErrorsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RateLimit</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RateLimit</code>.
     */
    static validateJSON(data) {
        if (data['errors']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['errors'])) {
                throw new Error("Expected the field `errors` to be an array in the JSON data but got " + data['errors']);
            }
            // validate the optional field `errors` (array)
            for (const item of data['errors']) {
                RateLimitErrorsInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/RateLimitErrorsInner>} errors
 */
RateLimit.prototype['errors'] = undefined;






export default RateLimit;

