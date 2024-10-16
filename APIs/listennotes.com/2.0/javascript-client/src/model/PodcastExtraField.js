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

/**
 * The PodcastExtraField model module.
 * @module model/PodcastExtraField
 * @version 2.0
 */
class PodcastExtraField {
    /**
     * Constructs a new <code>PodcastExtraField</code>.
     * @alias module:model/PodcastExtraField
     */
    constructor() { 
        
        PodcastExtraField.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PodcastExtraField</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PodcastExtraField} obj Optional instance to populate.
     * @return {module:model/PodcastExtraField} The populated <code>PodcastExtraField</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PodcastExtraField();

            if (data.hasOwnProperty('amazon_music_url')) {
                obj['amazon_music_url'] = ApiClient.convertToType(data['amazon_music_url'], 'String');
            }
            if (data.hasOwnProperty('facebook_handle')) {
                obj['facebook_handle'] = ApiClient.convertToType(data['facebook_handle'], 'String');
            }
            if (data.hasOwnProperty('google_url')) {
                obj['google_url'] = ApiClient.convertToType(data['google_url'], 'String');
            }
            if (data.hasOwnProperty('instagram_handle')) {
                obj['instagram_handle'] = ApiClient.convertToType(data['instagram_handle'], 'String');
            }
            if (data.hasOwnProperty('linkedin_url')) {
                obj['linkedin_url'] = ApiClient.convertToType(data['linkedin_url'], 'String');
            }
            if (data.hasOwnProperty('patreon_handle')) {
                obj['patreon_handle'] = ApiClient.convertToType(data['patreon_handle'], 'String');
            }
            if (data.hasOwnProperty('spotify_url')) {
                obj['spotify_url'] = ApiClient.convertToType(data['spotify_url'], 'String');
            }
            if (data.hasOwnProperty('twitter_handle')) {
                obj['twitter_handle'] = ApiClient.convertToType(data['twitter_handle'], 'String');
            }
            if (data.hasOwnProperty('url1')) {
                obj['url1'] = ApiClient.convertToType(data['url1'], 'String');
            }
            if (data.hasOwnProperty('url2')) {
                obj['url2'] = ApiClient.convertToType(data['url2'], 'String');
            }
            if (data.hasOwnProperty('url3')) {
                obj['url3'] = ApiClient.convertToType(data['url3'], 'String');
            }
            if (data.hasOwnProperty('wechat_handle')) {
                obj['wechat_handle'] = ApiClient.convertToType(data['wechat_handle'], 'String');
            }
            if (data.hasOwnProperty('youtube_url')) {
                obj['youtube_url'] = ApiClient.convertToType(data['youtube_url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PodcastExtraField</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PodcastExtraField</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['amazon_music_url'] && !(typeof data['amazon_music_url'] === 'string' || data['amazon_music_url'] instanceof String)) {
            throw new Error("Expected the field `amazon_music_url` to be a primitive type in the JSON string but got " + data['amazon_music_url']);
        }
        // ensure the json data is a string
        if (data['facebook_handle'] && !(typeof data['facebook_handle'] === 'string' || data['facebook_handle'] instanceof String)) {
            throw new Error("Expected the field `facebook_handle` to be a primitive type in the JSON string but got " + data['facebook_handle']);
        }
        // ensure the json data is a string
        if (data['google_url'] && !(typeof data['google_url'] === 'string' || data['google_url'] instanceof String)) {
            throw new Error("Expected the field `google_url` to be a primitive type in the JSON string but got " + data['google_url']);
        }
        // ensure the json data is a string
        if (data['instagram_handle'] && !(typeof data['instagram_handle'] === 'string' || data['instagram_handle'] instanceof String)) {
            throw new Error("Expected the field `instagram_handle` to be a primitive type in the JSON string but got " + data['instagram_handle']);
        }
        // ensure the json data is a string
        if (data['linkedin_url'] && !(typeof data['linkedin_url'] === 'string' || data['linkedin_url'] instanceof String)) {
            throw new Error("Expected the field `linkedin_url` to be a primitive type in the JSON string but got " + data['linkedin_url']);
        }
        // ensure the json data is a string
        if (data['patreon_handle'] && !(typeof data['patreon_handle'] === 'string' || data['patreon_handle'] instanceof String)) {
            throw new Error("Expected the field `patreon_handle` to be a primitive type in the JSON string but got " + data['patreon_handle']);
        }
        // ensure the json data is a string
        if (data['spotify_url'] && !(typeof data['spotify_url'] === 'string' || data['spotify_url'] instanceof String)) {
            throw new Error("Expected the field `spotify_url` to be a primitive type in the JSON string but got " + data['spotify_url']);
        }
        // ensure the json data is a string
        if (data['twitter_handle'] && !(typeof data['twitter_handle'] === 'string' || data['twitter_handle'] instanceof String)) {
            throw new Error("Expected the field `twitter_handle` to be a primitive type in the JSON string but got " + data['twitter_handle']);
        }
        // ensure the json data is a string
        if (data['url1'] && !(typeof data['url1'] === 'string' || data['url1'] instanceof String)) {
            throw new Error("Expected the field `url1` to be a primitive type in the JSON string but got " + data['url1']);
        }
        // ensure the json data is a string
        if (data['url2'] && !(typeof data['url2'] === 'string' || data['url2'] instanceof String)) {
            throw new Error("Expected the field `url2` to be a primitive type in the JSON string but got " + data['url2']);
        }
        // ensure the json data is a string
        if (data['url3'] && !(typeof data['url3'] === 'string' || data['url3'] instanceof String)) {
            throw new Error("Expected the field `url3` to be a primitive type in the JSON string but got " + data['url3']);
        }
        // ensure the json data is a string
        if (data['wechat_handle'] && !(typeof data['wechat_handle'] === 'string' || data['wechat_handle'] instanceof String)) {
            throw new Error("Expected the field `wechat_handle` to be a primitive type in the JSON string but got " + data['wechat_handle']);
        }
        // ensure the json data is a string
        if (data['youtube_url'] && !(typeof data['youtube_url'] === 'string' || data['youtube_url'] instanceof String)) {
            throw new Error("Expected the field `youtube_url` to be a primitive type in the JSON string but got " + data['youtube_url']);
        }

        return true;
    }


}



/**
 * Amazon Music url for this podcast
 * @member {String} amazon_music_url
 */
PodcastExtraField.prototype['amazon_music_url'] = undefined;

/**
 * Facebook username affiliated with this podcast
 * @member {String} facebook_handle
 */
PodcastExtraField.prototype['facebook_handle'] = undefined;

/**
 * Google Podcasts url for this podcast
 * @member {String} google_url
 */
PodcastExtraField.prototype['google_url'] = undefined;

/**
 * Instagram username affiliated with this podcast
 * @member {String} instagram_handle
 */
PodcastExtraField.prototype['instagram_handle'] = undefined;

/**
 * LinkedIn url affiliated with this podcast
 * @member {String} linkedin_url
 */
PodcastExtraField.prototype['linkedin_url'] = undefined;

/**
 * Patreon username affiliated with this podcast
 * @member {String} patreon_handle
 */
PodcastExtraField.prototype['patreon_handle'] = undefined;

/**
 * Spotify url for this podcast
 * @member {String} spotify_url
 */
PodcastExtraField.prototype['spotify_url'] = undefined;

/**
 * Twitter username affiliated with this podcast
 * @member {String} twitter_handle
 */
PodcastExtraField.prototype['twitter_handle'] = undefined;

/**
 * Url affiliated with this podcast
 * @member {String} url1
 */
PodcastExtraField.prototype['url1'] = undefined;

/**
 * Url affiliated with this podcast
 * @member {String} url2
 */
PodcastExtraField.prototype['url2'] = undefined;

/**
 * Url affiliated with this podcast
 * @member {String} url3
 */
PodcastExtraField.prototype['url3'] = undefined;

/**
 * WeChat username affiliated with this podcast
 * @member {String} wechat_handle
 */
PodcastExtraField.prototype['wechat_handle'] = undefined;

/**
 * YouTube url affiliated with this podcast
 * @member {String} youtube_url
 */
PodcastExtraField.prototype['youtube_url'] = undefined;






export default PodcastExtraField;

