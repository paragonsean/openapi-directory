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
import EpisodeMinimum from './EpisodeMinimum';
import PodcastExtraField from './PodcastExtraField';
import PodcastLookingForField from './PodcastLookingForField';
import PodcastTypeField from './PodcastTypeField';

/**
 * The PodcastFull model module.
 * @module model/PodcastFull
 * @version 2.0
 */
class PodcastFull {
    /**
     * Constructs a new <code>PodcastFull</code>.
     * @alias module:model/PodcastFull
     */
    constructor() { 
        
        PodcastFull.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PodcastFull</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PodcastFull} obj Optional instance to populate.
     * @return {module:model/PodcastFull} The populated <code>PodcastFull</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PodcastFull();

            if (data.hasOwnProperty('audio_length_sec')) {
                obj['audio_length_sec'] = ApiClient.convertToType(data['audio_length_sec'], 'Number');
            }
            if (data.hasOwnProperty('country')) {
                obj['country'] = ApiClient.convertToType(data['country'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('earliest_pub_date_ms')) {
                obj['earliest_pub_date_ms'] = ApiClient.convertToType(data['earliest_pub_date_ms'], 'Number');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('episodes')) {
                obj['episodes'] = ApiClient.convertToType(data['episodes'], [EpisodeMinimum]);
            }
            if (data.hasOwnProperty('explicit_content')) {
                obj['explicit_content'] = ApiClient.convertToType(data['explicit_content'], 'Boolean');
            }
            if (data.hasOwnProperty('extra')) {
                obj['extra'] = PodcastExtraField.constructFromObject(data['extra']);
            }
            if (data.hasOwnProperty('genre_ids')) {
                obj['genre_ids'] = ApiClient.convertToType(data['genre_ids'], ['Number']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = ApiClient.convertToType(data['image'], 'String');
            }
            if (data.hasOwnProperty('is_claimed')) {
                obj['is_claimed'] = ApiClient.convertToType(data['is_claimed'], 'Boolean');
            }
            if (data.hasOwnProperty('itunes_id')) {
                obj['itunes_id'] = ApiClient.convertToType(data['itunes_id'], 'Number');
            }
            if (data.hasOwnProperty('language')) {
                obj['language'] = ApiClient.convertToType(data['language'], 'String');
            }
            if (data.hasOwnProperty('latest_episode_id')) {
                obj['latest_episode_id'] = ApiClient.convertToType(data['latest_episode_id'], 'String');
            }
            if (data.hasOwnProperty('latest_pub_date_ms')) {
                obj['latest_pub_date_ms'] = ApiClient.convertToType(data['latest_pub_date_ms'], 'Number');
            }
            if (data.hasOwnProperty('listen_score')) {
                obj['listen_score'] = ApiClient.convertToType(data['listen_score'], 'Number');
            }
            if (data.hasOwnProperty('listen_score_global_rank')) {
                obj['listen_score_global_rank'] = ApiClient.convertToType(data['listen_score_global_rank'], 'String');
            }
            if (data.hasOwnProperty('listennotes_url')) {
                obj['listennotes_url'] = ApiClient.convertToType(data['listennotes_url'], 'String');
            }
            if (data.hasOwnProperty('looking_for')) {
                obj['looking_for'] = PodcastLookingForField.constructFromObject(data['looking_for']);
            }
            if (data.hasOwnProperty('next_episode_pub_date')) {
                obj['next_episode_pub_date'] = ApiClient.convertToType(data['next_episode_pub_date'], 'Number');
            }
            if (data.hasOwnProperty('publisher')) {
                obj['publisher'] = ApiClient.convertToType(data['publisher'], 'String');
            }
            if (data.hasOwnProperty('rss')) {
                obj['rss'] = ApiClient.convertToType(data['rss'], 'String');
            }
            if (data.hasOwnProperty('thumbnail')) {
                obj['thumbnail'] = ApiClient.convertToType(data['thumbnail'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('total_episodes')) {
                obj['total_episodes'] = ApiClient.convertToType(data['total_episodes'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = PodcastTypeField.constructFromObject(data['type']);
            }
            if (data.hasOwnProperty('update_frequency_hours')) {
                obj['update_frequency_hours'] = ApiClient.convertToType(data['update_frequency_hours'], 'Number');
            }
            if (data.hasOwnProperty('website')) {
                obj['website'] = ApiClient.convertToType(data['website'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PodcastFull</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PodcastFull</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['country'] && !(typeof data['country'] === 'string' || data['country'] instanceof String)) {
            throw new Error("Expected the field `country` to be a primitive type in the JSON string but got " + data['country']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        if (data['episodes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['episodes'])) {
                throw new Error("Expected the field `episodes` to be an array in the JSON data but got " + data['episodes']);
            }
            // validate the optional field `episodes` (array)
            for (const item of data['episodes']) {
                EpisodeMinimum.validateJSON(item);
            };
        }
        // validate the optional field `extra`
        if (data['extra']) { // data not null
          PodcastExtraField.validateJSON(data['extra']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['genre_ids'])) {
            throw new Error("Expected the field `genre_ids` to be an array in the JSON data but got " + data['genre_ids']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['image'] && !(typeof data['image'] === 'string' || data['image'] instanceof String)) {
            throw new Error("Expected the field `image` to be a primitive type in the JSON string but got " + data['image']);
        }
        // ensure the json data is a string
        if (data['language'] && !(typeof data['language'] === 'string' || data['language'] instanceof String)) {
            throw new Error("Expected the field `language` to be a primitive type in the JSON string but got " + data['language']);
        }
        // ensure the json data is a string
        if (data['latest_episode_id'] && !(typeof data['latest_episode_id'] === 'string' || data['latest_episode_id'] instanceof String)) {
            throw new Error("Expected the field `latest_episode_id` to be a primitive type in the JSON string but got " + data['latest_episode_id']);
        }
        // ensure the json data is a string
        if (data['listen_score_global_rank'] && !(typeof data['listen_score_global_rank'] === 'string' || data['listen_score_global_rank'] instanceof String)) {
            throw new Error("Expected the field `listen_score_global_rank` to be a primitive type in the JSON string but got " + data['listen_score_global_rank']);
        }
        // ensure the json data is a string
        if (data['listennotes_url'] && !(typeof data['listennotes_url'] === 'string' || data['listennotes_url'] instanceof String)) {
            throw new Error("Expected the field `listennotes_url` to be a primitive type in the JSON string but got " + data['listennotes_url']);
        }
        // validate the optional field `looking_for`
        if (data['looking_for']) { // data not null
          PodcastLookingForField.validateJSON(data['looking_for']);
        }
        // ensure the json data is a string
        if (data['publisher'] && !(typeof data['publisher'] === 'string' || data['publisher'] instanceof String)) {
            throw new Error("Expected the field `publisher` to be a primitive type in the JSON string but got " + data['publisher']);
        }
        // ensure the json data is a string
        if (data['rss'] && !(typeof data['rss'] === 'string' || data['rss'] instanceof String)) {
            throw new Error("Expected the field `rss` to be a primitive type in the JSON string but got " + data['rss']);
        }
        // ensure the json data is a string
        if (data['thumbnail'] && !(typeof data['thumbnail'] === 'string' || data['thumbnail'] instanceof String)) {
            throw new Error("Expected the field `thumbnail` to be a primitive type in the JSON string but got " + data['thumbnail']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['website'] && !(typeof data['website'] === 'string' || data['website'] instanceof String)) {
            throw new Error("Expected the field `website` to be a primitive type in the JSON string but got " + data['website']);
        }

        return true;
    }


}



/**
 * Average audio length of all episodes of this podcast. In seconds.
 * @member {Number} audio_length_sec
 */
PodcastFull.prototype['audio_length_sec'] = undefined;

/**
 * The country where this podcast is produced.
 * @member {String} country
 */
PodcastFull.prototype['country'] = undefined;

/**
 * Html of this episode's full description
 * @member {String} description
 */
PodcastFull.prototype['description'] = undefined;

/**
 * The published date of the oldest episode of this podcast. In milliseconds
 * @member {Number} earliest_pub_date_ms
 */
PodcastFull.prototype['earliest_pub_date_ms'] = undefined;

/**
 * The email of this podcast's producer. This field is available only in the PRO/ENTERPRISE plan.
 * @member {String} email
 */
PodcastFull.prototype['email'] = undefined;

/**
 * @member {Array.<module:model/EpisodeMinimum>} episodes
 */
PodcastFull.prototype['episodes'] = undefined;

/**
 * Whether this podcast contains explicit language.
 * @member {Boolean} explicit_content
 */
PodcastFull.prototype['explicit_content'] = undefined;

/**
 * @member {module:model/PodcastExtraField} extra
 */
PodcastFull.prototype['extra'] = undefined;

/**
 * @member {Array.<Number>} genre_ids
 */
PodcastFull.prototype['genre_ids'] = undefined;

/**
 * Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`.
 * @member {String} id
 */
PodcastFull.prototype['id'] = undefined;

/**
 * Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's a high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**, low resolution image (300x300). 
 * @member {String} image
 */
PodcastFull.prototype['image'] = undefined;

/**
 * Whether this podcast is claimed by its producer on [ListenNotes.com](https://www.ListenNotes.com).
 * @member {Boolean} is_claimed
 */
PodcastFull.prototype['is_claimed'] = undefined;

/**
 * iTunes id for this podcast.
 * @member {Number} itunes_id
 */
PodcastFull.prototype['itunes_id'] = undefined;

/**
 * The language of this podcast. You can get all supported languages from `GET /languages`.
 * @member {String} language
 */
PodcastFull.prototype['language'] = undefined;

/**
 * The id of the most recently published episode of this podcast, which can be used to further fetch detailed episode metadata via `GET /episodes/{id}`.
 * @member {String} latest_episode_id
 */
PodcastFull.prototype['latest_episode_id'] = undefined;

/**
 * The published date of the latest episode of this podcast. In milliseconds
 * @member {Number} latest_pub_date_ms
 */
PodcastFull.prototype['latest_pub_date_ms'] = undefined;

/**
 * The estimated popularity score of a podcast compared to all other rss-based public podcasts in the world on a scale from 0 to 100. If the score is not available, it'll be null. Learn more at listennotes.com/listen-score 
 * @member {Number} listen_score
 */
PodcastFull.prototype['listen_score'] = undefined;

/**
 * The estimated popularity ranking of a podcast compared to all other rss-based public podcasts in the world. For example, if the value is 0.5%, then this podcast is one of the top 0.5% most popular shows out of all podcasts globally, ranked by Listen Score. If the ranking is not available, it'll be null. Learn more at listennotes.com/listen-score 
 * @member {String} listen_score_global_rank
 */
PodcastFull.prototype['listen_score_global_rank'] = undefined;

/**
 * The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com).
 * @member {String} listennotes_url
 */
PodcastFull.prototype['listennotes_url'] = undefined;

/**
 * @member {module:model/PodcastLookingForField} looking_for
 */
PodcastFull.prototype['looking_for'] = undefined;

/**
 * Passed to the **next_episode_pub_date** parameter of `GET /podcasts/{id}` to paginate through episodes of that podcast.
 * @member {Number} next_episode_pub_date
 */
PodcastFull.prototype['next_episode_pub_date'] = undefined;

/**
 * Podcast publisher name.
 * @member {String} publisher
 */
PodcastFull.prototype['publisher'] = undefined;

/**
 * RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan.
 * @member {String} rss
 */
PodcastFull.prototype['rss'] = undefined;

/**
 * Thumbnail image url for this podcast's artwork (300x300).
 * @member {String} thumbnail
 */
PodcastFull.prototype['thumbnail'] = undefined;

/**
 * Podcast name.
 * @member {String} title
 */
PodcastFull.prototype['title'] = undefined;

/**
 * Total number of episodes in this podcast.
 * @member {Number} total_episodes
 */
PodcastFull.prototype['total_episodes'] = undefined;

/**
 * @member {module:model/PodcastTypeField} type
 */
PodcastFull.prototype['type'] = undefined;

/**
 * How frequently does this podcast release a new episode? In hours. For example, if the value is 166, then it's every 166 hours (or weekly).
 * @member {Number} update_frequency_hours
 */
PodcastFull.prototype['update_frequency_hours'] = undefined;

/**
 * Website url of this podcast.
 * @member {String} website
 */
PodcastFull.prototype['website'] = undefined;






export default PodcastFull;

