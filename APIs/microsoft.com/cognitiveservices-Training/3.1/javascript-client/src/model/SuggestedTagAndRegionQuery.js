/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import StoredSuggestedTagAndRegion from './StoredSuggestedTagAndRegion';
import SuggestedTagAndRegionQueryToken from './SuggestedTagAndRegionQueryToken';

/**
 * The SuggestedTagAndRegionQuery model module.
 * @module model/SuggestedTagAndRegionQuery
 * @version 3.1
 */
class SuggestedTagAndRegionQuery {
    /**
     * Constructs a new <code>SuggestedTagAndRegionQuery</code>.
     * The array of result images and token containing session and continuation Ids for the next query.
     * @alias module:model/SuggestedTagAndRegionQuery
     */
    constructor() { 
        
        SuggestedTagAndRegionQuery.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SuggestedTagAndRegionQuery</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SuggestedTagAndRegionQuery} obj Optional instance to populate.
     * @return {module:model/SuggestedTagAndRegionQuery} The populated <code>SuggestedTagAndRegionQuery</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SuggestedTagAndRegionQuery();

            if (data.hasOwnProperty('results')) {
                obj['results'] = ApiClient.convertToType(data['results'], [StoredSuggestedTagAndRegion]);
            }
            if (data.hasOwnProperty('token')) {
                obj['token'] = SuggestedTagAndRegionQueryToken.constructFromObject(data['token']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SuggestedTagAndRegionQuery</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SuggestedTagAndRegionQuery</code>.
     */
    static validateJSON(data) {
        if (data['results']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['results'])) {
                throw new Error("Expected the field `results` to be an array in the JSON data but got " + data['results']);
            }
            // validate the optional field `results` (array)
            for (const item of data['results']) {
                StoredSuggestedTagAndRegion.validateJSON(item);
            };
        }
        // validate the optional field `token`
        if (data['token']) { // data not null
          SuggestedTagAndRegionQueryToken.validateJSON(data['token']);
        }

        return true;
    }


}



/**
 * Result of a suggested tags and regions request of the untagged image.
 * @member {Array.<module:model/StoredSuggestedTagAndRegion>} results
 */
SuggestedTagAndRegionQuery.prototype['results'] = undefined;

/**
 * @member {module:model/SuggestedTagAndRegionQueryToken} token
 */
SuggestedTagAndRegionQuery.prototype['token'] = undefined;






export default SuggestedTagAndRegionQuery;

