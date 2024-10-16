/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
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
import PersonalisedMusicTrackContribution from './PersonalisedMusicTrackContribution';
import PersonalisedMusicTrackImage from './PersonalisedMusicTrackImage';
import PersonalisedMusicTrackMedia from './PersonalisedMusicTrackMedia';
import PersonalisedMusicVersion from './PersonalisedMusicVersion';

/**
 * The PersonalisedMusicTrack model module.
 * @module model/PersonalisedMusicTrack
 * @version 1.0.0
 */
class PersonalisedMusicTrack {
    /**
     * Constructs a new <code>PersonalisedMusicTrack</code>.
     * @alias module:model/PersonalisedMusicTrack
     * @param contributions {Array.<module:model/PersonalisedMusicTrackContribution>} 
     * @param id {String} 
     * @param images {Array.<module:model/PersonalisedMusicTrackImage>} 
     * @param media {Array.<module:model/PersonalisedMusicTrackMedia>} 
     * @param title {String} 
     * @param type {String} 
     * @param version {module:model/PersonalisedMusicVersion} 
     */
    constructor(contributions, id, images, media, title, type, version) { 
        
        PersonalisedMusicTrack.initialize(this, contributions, id, images, media, title, type, version);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, contributions, id, images, media, title, type, version) { 
        obj['contributions'] = contributions;
        obj['id'] = id;
        obj['images'] = images;
        obj['media'] = media;
        obj['title'] = title;
        obj['type'] = type;
        obj['version'] = version;
    }

    /**
     * Constructs a <code>PersonalisedMusicTrack</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PersonalisedMusicTrack} obj Optional instance to populate.
     * @return {module:model/PersonalisedMusicTrack} The populated <code>PersonalisedMusicTrack</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PersonalisedMusicTrack();

            if (data.hasOwnProperty('contributions')) {
                obj['contributions'] = ApiClient.convertToType(data['contributions'], [PersonalisedMusicTrackContribution]);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('images')) {
                obj['images'] = ApiClient.convertToType(data['images'], [PersonalisedMusicTrackImage]);
            }
            if (data.hasOwnProperty('media')) {
                obj['media'] = ApiClient.convertToType(data['media'], [PersonalisedMusicTrackMedia]);
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('version')) {
                obj['version'] = PersonalisedMusicVersion.constructFromObject(data['version']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PersonalisedMusicTrack</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PersonalisedMusicTrack</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PersonalisedMusicTrack.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['contributions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['contributions'])) {
                throw new Error("Expected the field `contributions` to be an array in the JSON data but got " + data['contributions']);
            }
            // validate the optional field `contributions` (array)
            for (const item of data['contributions']) {
                PersonalisedMusicTrackContribution.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        if (data['images']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['images'])) {
                throw new Error("Expected the field `images` to be an array in the JSON data but got " + data['images']);
            }
            // validate the optional field `images` (array)
            for (const item of data['images']) {
                PersonalisedMusicTrackImage.validateJSON(item);
            };
        }
        if (data['media']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['media'])) {
                throw new Error("Expected the field `media` to be an array in the JSON data but got " + data['media']);
            }
            // validate the optional field `media` (array)
            for (const item of data['media']) {
                PersonalisedMusicTrackMedia.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // validate the optional field `version`
        if (data['version']) { // data not null
          PersonalisedMusicVersion.validateJSON(data['version']);
        }

        return true;
    }


}

PersonalisedMusicTrack.RequiredProperties = ["contributions", "id", "images", "media", "title", "type", "version"];

/**
 * @member {Array.<module:model/PersonalisedMusicTrackContribution>} contributions
 */
PersonalisedMusicTrack.prototype['contributions'] = undefined;

/**
 * @member {String} id
 */
PersonalisedMusicTrack.prototype['id'] = undefined;

/**
 * @member {Array.<module:model/PersonalisedMusicTrackImage>} images
 */
PersonalisedMusicTrack.prototype['images'] = undefined;

/**
 * @member {Array.<module:model/PersonalisedMusicTrackMedia>} media
 */
PersonalisedMusicTrack.prototype['media'] = undefined;

/**
 * @member {String} title
 */
PersonalisedMusicTrack.prototype['title'] = undefined;

/**
 * @member {String} type
 */
PersonalisedMusicTrack.prototype['type'] = undefined;

/**
 * @member {module:model/PersonalisedMusicVersion} version
 */
PersonalisedMusicTrack.prototype['version'] = undefined;






export default PersonalisedMusicTrack;

