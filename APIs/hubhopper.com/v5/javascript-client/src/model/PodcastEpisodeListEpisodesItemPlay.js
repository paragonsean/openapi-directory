/**
 * Hubhopper Partner Integration API(s) - Production
 * This is an interactive document explaining the API(s) that could be used to fetch data from [Hubhopper](https://hubhopper.com). Use the api key provided to authorize `x-api-key` and test the API(s). The output data models are also available for reference.
 *
 * The version of the OpenAPI document: v5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PodcastEpisodeListEpisodesItemPlay model module.
 * @module model/PodcastEpisodeListEpisodesItemPlay
 * @version v5
 */
class PodcastEpisodeListEpisodesItemPlay {
    /**
     * Constructs a new <code>PodcastEpisodeListEpisodesItemPlay</code>.
     * @alias module:model/PodcastEpisodeListEpisodesItemPlay
     */
    constructor() { 
        
        PodcastEpisodeListEpisodesItemPlay.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PodcastEpisodeListEpisodesItemPlay</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PodcastEpisodeListEpisodesItemPlay} obj Optional instance to populate.
     * @return {module:model/PodcastEpisodeListEpisodesItemPlay} The populated <code>PodcastEpisodeListEpisodesItemPlay</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PodcastEpisodeListEpisodesItemPlay();

            if (data.hasOwnProperty('duration')) {
                obj['duration'] = ApiClient.convertToType(data['duration'], 'String');
            }
            if (data.hasOwnProperty('durationInSec')) {
                obj['durationInSec'] = ApiClient.convertToType(data['durationInSec'], 'Number');
            }
            if (data.hasOwnProperty('size')) {
                obj['size'] = ApiClient.convertToType(data['size'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PodcastEpisodeListEpisodesItemPlay</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PodcastEpisodeListEpisodesItemPlay</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['duration'] && !(typeof data['duration'] === 'string' || data['duration'] instanceof String)) {
            throw new Error("Expected the field `duration` to be a primitive type in the JSON string but got " + data['duration']);
        }
        // ensure the json data is a string
        if (data['size'] && !(typeof data['size'] === 'string' || data['size'] instanceof String)) {
            throw new Error("Expected the field `size` to be a primitive type in the JSON string but got " + data['size']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}



/**
 * @member {String} duration
 */
PodcastEpisodeListEpisodesItemPlay.prototype['duration'] = undefined;

/**
 * @member {Number} durationInSec
 */
PodcastEpisodeListEpisodesItemPlay.prototype['durationInSec'] = undefined;

/**
 * @member {String} size
 */
PodcastEpisodeListEpisodesItemPlay.prototype['size'] = undefined;

/**
 * @member {String} type
 */
PodcastEpisodeListEpisodesItemPlay.prototype['type'] = undefined;

/**
 * @member {String} url
 */
PodcastEpisodeListEpisodesItemPlay.prototype['url'] = undefined;






export default PodcastEpisodeListEpisodesItemPlay;

