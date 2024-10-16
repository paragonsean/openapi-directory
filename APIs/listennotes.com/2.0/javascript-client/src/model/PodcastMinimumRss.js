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
 * The PodcastMinimumRss model module.
 * @module model/PodcastMinimumRss
 * @version 2.0
 */
class PodcastMinimumRss {
    /**
     * Constructs a new <code>PodcastMinimumRss</code>.
     * @alias module:model/PodcastMinimumRss
     */
    constructor() { 
        
        PodcastMinimumRss.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PodcastMinimumRss</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PodcastMinimumRss} obj Optional instance to populate.
     * @return {module:model/PodcastMinimumRss} The populated <code>PodcastMinimumRss</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PodcastMinimumRss();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = ApiClient.convertToType(data['image'], 'String');
            }
            if (data.hasOwnProperty('listennotes_url')) {
                obj['listennotes_url'] = ApiClient.convertToType(data['listennotes_url'], 'String');
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
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PodcastMinimumRss</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PodcastMinimumRss</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['image'] && !(typeof data['image'] === 'string' || data['image'] instanceof String)) {
            throw new Error("Expected the field `image` to be a primitive type in the JSON string but got " + data['image']);
        }
        // ensure the json data is a string
        if (data['listennotes_url'] && !(typeof data['listennotes_url'] === 'string' || data['listennotes_url'] instanceof String)) {
            throw new Error("Expected the field `listennotes_url` to be a primitive type in the JSON string but got " + data['listennotes_url']);
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

        return true;
    }


}



/**
 * Podcast id, which can be used to further fetch detailed podcast metadata via `GET /podcasts/{id}`.
 * @member {String} id
 */
PodcastMinimumRss.prototype['id'] = undefined;

/**
 * Image url for this podcast's artwork. If you are using PRO/ENTERPRISE plan, then it's a high resolution image (1400x1400). If you are using FREE plan, then it's the same as **thumbnail**, low resolution image (300x300). 
 * @member {String} image
 */
PodcastMinimumRss.prototype['image'] = undefined;

/**
 * The url of this podcast on [ListenNotes.com](https://www.ListenNotes.com).
 * @member {String} listennotes_url
 */
PodcastMinimumRss.prototype['listennotes_url'] = undefined;

/**
 * Podcast publisher name.
 * @member {String} publisher
 */
PodcastMinimumRss.prototype['publisher'] = undefined;

/**
 * RSS url of this podcast. This field is available only in the PRO/ENTERPRISE plan.
 * @member {String} rss
 */
PodcastMinimumRss.prototype['rss'] = undefined;

/**
 * Thumbnail image url for this podcast's artwork (300x300).
 * @member {String} thumbnail
 */
PodcastMinimumRss.prototype['thumbnail'] = undefined;

/**
 * Podcast name.
 * @member {String} title
 */
PodcastMinimumRss.prototype['title'] = undefined;






export default PodcastMinimumRss;

