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
import PlaylistItemData from './PlaylistItemData';

/**
 * The PlaylistItem model module.
 * @module model/PlaylistItem
 * @version 2.0
 */
class PlaylistItem {
    /**
     * Constructs a new <code>PlaylistItem</code>.
     * An item in a playlist
     * @alias module:model/PlaylistItem
     */
    constructor() { 
        
        PlaylistItem.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PlaylistItem</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlaylistItem} obj Optional instance to populate.
     * @return {module:model/PlaylistItem} The populated <code>PlaylistItem</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlaylistItem();

            if (data.hasOwnProperty('added_at_ms')) {
                obj['added_at_ms'] = ApiClient.convertToType(data['added_at_ms'], 'Number');
            }
            if (data.hasOwnProperty('data')) {
                obj['data'] = PlaylistItemData.constructFromObject(data['data']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('notes')) {
                obj['notes'] = ApiClient.convertToType(data['notes'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlaylistItem</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlaylistItem</code>.
     */
    static validateJSON(data) {
        // validate the optional field `data`
        if (data['data']) { // data not null
          PlaylistItemData.validateJSON(data['data']);
        }
        // ensure the json data is a string
        if (data['notes'] && !(typeof data['notes'] === 'string' || data['notes'] instanceof String)) {
            throw new Error("Expected the field `notes` to be a primitive type in the JSON string but got " + data['notes']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * Timestamp (in milliseconds) when this item is added.
 * @member {Number} added_at_ms
 */
PlaylistItem.prototype['added_at_ms'] = undefined;

/**
 * @member {module:model/PlaylistItemData} data
 */
PlaylistItem.prototype['data'] = undefined;

/**
 * Playlist item id.
 * @member {Number} id
 */
PlaylistItem.prototype['id'] = undefined;

/**
 * Notes for this item.
 * @member {String} notes
 */
PlaylistItem.prototype['notes'] = undefined;

/**
 * The type of this playlist item. If a playlist is **episode_list**, then an item could be either **episode** or **custom_audio**. If it's **podcast_list**, then an item can only be **podcast**. 
 * @member {module:model/PlaylistItem.TypeEnum} type
 */
PlaylistItem.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
PlaylistItem['TypeEnum'] = {

    /**
     * value: "episode"
     * @const
     */
    "episode": "episode",

    /**
     * value: "custom_audio"
     * @const
     */
    "custom_audio": "custom_audio",

    /**
     * value: "podcast"
     * @const
     */
    "podcast": "podcast"
};



export default PlaylistItem;

