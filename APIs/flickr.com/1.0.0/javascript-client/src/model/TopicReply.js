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
import GetFavoritesContextByID200ResponseCount from './GetFavoritesContextByID200ResponseCount';

/**
 * The TopicReply model module.
 * @module model/TopicReply
 * @version 1.0.0
 */
class TopicReply {
    /**
     * Constructs a new <code>TopicReply</code>.
     * @alias module:model/TopicReply
     */
    constructor() { 
        
        TopicReply.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TopicReply</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TopicReply} obj Optional instance to populate.
     * @return {module:model/TopicReply} The populated <code>TopicReply</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TopicReply();

            if (data.hasOwnProperty('author')) {
                obj['author'] = ApiClient.convertToType(data['author'], 'String');
            }
            if (data.hasOwnProperty('author_is_deleted')) {
                obj['author_is_deleted'] = ApiClient.convertToType(data['author_is_deleted'], 'Boolean');
            }
            if (data.hasOwnProperty('author_path_alias')) {
                obj['author_path_alias'] = ApiClient.convertToType(data['author_path_alias'], 'String');
            }
            if (data.hasOwnProperty('authorname')) {
                obj['authorname'] = ApiClient.convertToType(data['authorname'], 'String');
            }
            if (data.hasOwnProperty('can_delete')) {
                obj['can_delete'] = ApiClient.convertToType(data['can_delete'], 'Boolean');
            }
            if (data.hasOwnProperty('can_edit')) {
                obj['can_edit'] = ApiClient.convertToType(data['can_edit'], 'Boolean');
            }
            if (data.hasOwnProperty('datecreate')) {
                obj['datecreate'] = ApiClient.convertToType(data['datecreate'], 'String');
            }
            if (data.hasOwnProperty('iconfarm')) {
                obj['iconfarm'] = ApiClient.convertToType(data['iconfarm'], 'String');
            }
            if (data.hasOwnProperty('iconserver')) {
                obj['iconserver'] = ApiClient.convertToType(data['iconserver'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('is_pro')) {
                obj['is_pro'] = ApiClient.convertToType(data['is_pro'], 'Boolean');
            }
            if (data.hasOwnProperty('lastedit')) {
                obj['lastedit'] = ApiClient.convertToType(data['lastedit'], 'String');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = GetFavoritesContextByID200ResponseCount.constructFromObject(data['message']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TopicReply</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TopicReply</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['author'] && !(typeof data['author'] === 'string' || data['author'] instanceof String)) {
            throw new Error("Expected the field `author` to be a primitive type in the JSON string but got " + data['author']);
        }
        // ensure the json data is a string
        if (data['author_path_alias'] && !(typeof data['author_path_alias'] === 'string' || data['author_path_alias'] instanceof String)) {
            throw new Error("Expected the field `author_path_alias` to be a primitive type in the JSON string but got " + data['author_path_alias']);
        }
        // ensure the json data is a string
        if (data['authorname'] && !(typeof data['authorname'] === 'string' || data['authorname'] instanceof String)) {
            throw new Error("Expected the field `authorname` to be a primitive type in the JSON string but got " + data['authorname']);
        }
        // ensure the json data is a string
        if (data['datecreate'] && !(typeof data['datecreate'] === 'string' || data['datecreate'] instanceof String)) {
            throw new Error("Expected the field `datecreate` to be a primitive type in the JSON string but got " + data['datecreate']);
        }
        // ensure the json data is a string
        if (data['iconfarm'] && !(typeof data['iconfarm'] === 'string' || data['iconfarm'] instanceof String)) {
            throw new Error("Expected the field `iconfarm` to be a primitive type in the JSON string but got " + data['iconfarm']);
        }
        // ensure the json data is a string
        if (data['iconserver'] && !(typeof data['iconserver'] === 'string' || data['iconserver'] instanceof String)) {
            throw new Error("Expected the field `iconserver` to be a primitive type in the JSON string but got " + data['iconserver']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['lastedit'] && !(typeof data['lastedit'] === 'string' || data['lastedit'] instanceof String)) {
            throw new Error("Expected the field `lastedit` to be a primitive type in the JSON string but got " + data['lastedit']);
        }
        // validate the optional field `message`
        if (data['message']) { // data not null
          GetFavoritesContextByID200ResponseCount.validateJSON(data['message']);
        }

        return true;
    }


}



/**
 * @member {String} author
 */
TopicReply.prototype['author'] = undefined;

/**
 * @member {Boolean} author_is_deleted
 */
TopicReply.prototype['author_is_deleted'] = undefined;

/**
 * @member {String} author_path_alias
 */
TopicReply.prototype['author_path_alias'] = undefined;

/**
 * @member {String} authorname
 */
TopicReply.prototype['authorname'] = undefined;

/**
 * @member {Boolean} can_delete
 */
TopicReply.prototype['can_delete'] = undefined;

/**
 * @member {Boolean} can_edit
 */
TopicReply.prototype['can_edit'] = undefined;

/**
 * @member {String} datecreate
 */
TopicReply.prototype['datecreate'] = undefined;

/**
 * @member {String} iconfarm
 */
TopicReply.prototype['iconfarm'] = undefined;

/**
 * @member {String} iconserver
 */
TopicReply.prototype['iconserver'] = undefined;

/**
 * @member {String} id
 */
TopicReply.prototype['id'] = undefined;

/**
 * @member {Boolean} is_pro
 */
TopicReply.prototype['is_pro'] = undefined;

/**
 * @member {String} lastedit
 */
TopicReply.prototype['lastedit'] = undefined;

/**
 * @member {module:model/GetFavoritesContextByID200ResponseCount} message
 */
TopicReply.prototype['message'] = undefined;






export default TopicReply;

