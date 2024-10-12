/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
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

/**
 * The Album model module.
 * @module model/Album
 * @version 1.0.0
 */
class Album {
    /**
     * Constructs a new <code>Album</code>.
     * @alias module:model/Album
     */
    constructor() { 
        
        Album.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Album</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Album} obj Optional instance to populate.
     * @return {module:model/Album} The populated <code>Album</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Album();

            if (data.hasOwnProperty('can_comment')) {
                obj['can_comment'] = ApiClient.convertToType(data['can_comment'], 'Boolean');
            }
            if (data.hasOwnProperty('count_comments')) {
                obj['count_comments'] = ApiClient.convertToType(data['count_comments'], 'Number');
            }
            if (data.hasOwnProperty('count_views')) {
                obj['count_views'] = ApiClient.convertToType(data['count_views'], 'Number');
            }
            if (data.hasOwnProperty('date_create')) {
                obj['date_create'] = ApiClient.convertToType(data['date_create'], 'Number');
            }
            if (data.hasOwnProperty('date_update')) {
                obj['date_update'] = ApiClient.convertToType(data['date_update'], 'Number');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('farm')) {
                obj['farm'] = ApiClient.convertToType(data['farm'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('photos')) {
                obj['photos'] = ApiClient.convertToType(data['photos'], 'Number');
            }
            if (data.hasOwnProperty('primary')) {
                obj['primary'] = ApiClient.convertToType(data['primary'], 'String');
            }
            if (data.hasOwnProperty('secret')) {
                obj['secret'] = ApiClient.convertToType(data['secret'], 'String');
            }
            if (data.hasOwnProperty('server')) {
                obj['server'] = ApiClient.convertToType(data['server'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('videos')) {
                obj['videos'] = ApiClient.convertToType(data['videos'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Album</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Album</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['farm'] && !(typeof data['farm'] === 'string' || data['farm'] instanceof String)) {
            throw new Error("Expected the field `farm` to be a primitive type in the JSON string but got " + data['farm']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['primary'] && !(typeof data['primary'] === 'string' || data['primary'] instanceof String)) {
            throw new Error("Expected the field `primary` to be a primitive type in the JSON string but got " + data['primary']);
        }
        // ensure the json data is a string
        if (data['secret'] && !(typeof data['secret'] === 'string' || data['secret'] instanceof String)) {
            throw new Error("Expected the field `secret` to be a primitive type in the JSON string but got " + data['secret']);
        }
        // ensure the json data is a string
        if (data['server'] && !(typeof data['server'] === 'string' || data['server'] instanceof String)) {
            throw new Error("Expected the field `server` to be a primitive type in the JSON string but got " + data['server']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}



/**
 * @member {Boolean} can_comment
 */
Album.prototype['can_comment'] = undefined;

/**
 * @member {Number} count_comments
 */
Album.prototype['count_comments'] = undefined;

/**
 * @member {Number} count_views
 */
Album.prototype['count_views'] = undefined;

/**
 * @member {Number} date_create
 */
Album.prototype['date_create'] = undefined;

/**
 * @member {Number} date_update
 */
Album.prototype['date_update'] = undefined;

/**
 * @member {String} description
 */
Album.prototype['description'] = undefined;

/**
 * @member {String} farm
 */
Album.prototype['farm'] = undefined;

/**
 * @member {String} id
 */
Album.prototype['id'] = undefined;

/**
 * @member {Number} photos
 */
Album.prototype['photos'] = undefined;

/**
 * @member {String} primary
 */
Album.prototype['primary'] = undefined;

/**
 * @member {String} secret
 */
Album.prototype['secret'] = undefined;

/**
 * @member {String} server
 */
Album.prototype['server'] = undefined;

/**
 * @member {String} title
 */
Album.prototype['title'] = undefined;

/**
 * @member {Number} videos
 */
Album.prototype['videos'] = undefined;






export default Album;

