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
import PodcastListPodcastsItemCategory from './PodcastListPodcastsItemCategory';

/**
 * The PodcastListPodcastsItem model module.
 * @module model/PodcastListPodcastsItem
 * @version v5
 */
class PodcastListPodcastsItem {
    /**
     * Constructs a new <code>PodcastListPodcastsItem</code>.
     * @alias module:model/PodcastListPodcastsItem
     */
    constructor() { 
        
        PodcastListPodcastsItem.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PodcastListPodcastsItem</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PodcastListPodcastsItem} obj Optional instance to populate.
     * @return {module:model/PodcastListPodcastsItem} The populated <code>PodcastListPodcastsItem</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PodcastListPodcastsItem();

            if (data.hasOwnProperty('author')) {
                obj['author'] = ApiClient.convertToType(data['author'], 'String');
            }
            if (data.hasOwnProperty('category')) {
                obj['category'] = PodcastListPodcastsItemCategory.constructFromObject(data['category']);
            }
            if (data.hasOwnProperty('categoryId')) {
                obj['categoryId'] = ApiClient.convertToType(data['categoryId'], 'Number');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('episodes')) {
                obj['episodes'] = ApiClient.convertToType(data['episodes'], 'Number');
            }
            if (data.hasOwnProperty('featured')) {
                obj['featured'] = PodcastListPodcastsItemCategory.constructFromObject(data['featured']);
            }
            if (data.hasOwnProperty('featuredId')) {
                obj['featuredId'] = ApiClient.convertToType(data['featuredId'], 'Number');
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = ApiClient.convertToType(data['image'], 'String');
            }
            if (data.hasOwnProperty('keywords')) {
                obj['keywords'] = ApiClient.convertToType(data['keywords'], 'String');
            }
            if (data.hasOwnProperty('latestEpisodeTime')) {
                obj['latestEpisodeTime'] = ApiClient.convertToType(data['latestEpisodeTime'], 'String');
            }
            if (data.hasOwnProperty('podcastId')) {
                obj['podcastId'] = ApiClient.convertToType(data['podcastId'], 'Number');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PodcastListPodcastsItem</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PodcastListPodcastsItem</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['author'] && !(typeof data['author'] === 'string' || data['author'] instanceof String)) {
            throw new Error("Expected the field `author` to be a primitive type in the JSON string but got " + data['author']);
        }
        // validate the optional field `category`
        if (data['category']) { // data not null
          PodcastListPodcastsItemCategory.validateJSON(data['category']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // validate the optional field `featured`
        if (data['featured']) { // data not null
          PodcastListPodcastsItemCategory.validateJSON(data['featured']);
        }
        // ensure the json data is a string
        if (data['image'] && !(typeof data['image'] === 'string' || data['image'] instanceof String)) {
            throw new Error("Expected the field `image` to be a primitive type in the JSON string but got " + data['image']);
        }
        // ensure the json data is a string
        if (data['keywords'] && !(typeof data['keywords'] === 'string' || data['keywords'] instanceof String)) {
            throw new Error("Expected the field `keywords` to be a primitive type in the JSON string but got " + data['keywords']);
        }
        // ensure the json data is a string
        if (data['latestEpisodeTime'] && !(typeof data['latestEpisodeTime'] === 'string' || data['latestEpisodeTime'] instanceof String)) {
            throw new Error("Expected the field `latestEpisodeTime` to be a primitive type in the JSON string but got " + data['latestEpisodeTime']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}



/**
 * @member {String} author
 */
PodcastListPodcastsItem.prototype['author'] = undefined;

/**
 * @member {module:model/PodcastListPodcastsItemCategory} category
 */
PodcastListPodcastsItem.prototype['category'] = undefined;

/**
 * @member {Number} categoryId
 */
PodcastListPodcastsItem.prototype['categoryId'] = undefined;

/**
 * @member {String} description
 */
PodcastListPodcastsItem.prototype['description'] = undefined;

/**
 * @member {Number} episodes
 */
PodcastListPodcastsItem.prototype['episodes'] = undefined;

/**
 * @member {module:model/PodcastListPodcastsItemCategory} featured
 */
PodcastListPodcastsItem.prototype['featured'] = undefined;

/**
 * @member {Number} featuredId
 */
PodcastListPodcastsItem.prototype['featuredId'] = undefined;

/**
 * @member {String} image
 */
PodcastListPodcastsItem.prototype['image'] = undefined;

/**
 * @member {String} keywords
 */
PodcastListPodcastsItem.prototype['keywords'] = undefined;

/**
 * @member {String} latestEpisodeTime
 */
PodcastListPodcastsItem.prototype['latestEpisodeTime'] = undefined;

/**
 * @member {Number} podcastId
 */
PodcastListPodcastsItem.prototype['podcastId'] = undefined;

/**
 * @member {String} title
 */
PodcastListPodcastsItem.prototype['title'] = undefined;

/**
 * @member {String} url
 */
PodcastListPodcastsItem.prototype['url'] = undefined;






export default PodcastListPodcastsItem;

