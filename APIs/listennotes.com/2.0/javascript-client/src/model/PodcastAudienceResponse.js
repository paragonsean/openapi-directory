/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PodcastAudienceResponseByRegionsInner from './PodcastAudienceResponseByRegionsInner';

/**
 * The PodcastAudienceResponse model module.
 * @module model/PodcastAudienceResponse
 * @version 2.0
 */
class PodcastAudienceResponse {
    /**
     * Constructs a new <code>PodcastAudienceResponse</code>.
     * @alias module:model/PodcastAudienceResponse
     */
    constructor() { 
        
        PodcastAudienceResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PodcastAudienceResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PodcastAudienceResponse} obj Optional instance to populate.
     * @return {module:model/PodcastAudienceResponse} The populated <code>PodcastAudienceResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PodcastAudienceResponse();

            if (data.hasOwnProperty('by_regions')) {
                obj['by_regions'] = ApiClient.convertToType(data['by_regions'], [PodcastAudienceResponseByRegionsInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PodcastAudienceResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PodcastAudienceResponse</code>.
     */
    static validateJSON(data) {
        if (data['by_regions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['by_regions'])) {
                throw new Error("Expected the field `by_regions` to be an array in the JSON data but got " + data['by_regions']);
            }
            // validate the optional field `by_regions` (array)
            for (const item of data['by_regions']) {
                PodcastAudienceResponseByRegionsInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/PodcastAudienceResponseByRegionsInner>} by_regions
 */
PodcastAudienceResponse.prototype['by_regions'] = undefined;






export default PodcastAudienceResponse;

