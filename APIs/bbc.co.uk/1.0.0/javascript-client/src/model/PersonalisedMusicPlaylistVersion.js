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

/**
 * The PersonalisedMusicPlaylistVersion model module.
 * @module model/PersonalisedMusicPlaylistVersion
 * @version 1.0.0
 */
class PersonalisedMusicPlaylistVersion {
    /**
     * Constructs a new <code>PersonalisedMusicPlaylistVersion</code>.
     * @alias module:model/PersonalisedMusicPlaylistVersion
     * @param warnings {Array.<String>} 
     */
    constructor(warnings) { 
        
        PersonalisedMusicPlaylistVersion.initialize(this, warnings);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, warnings) { 
        obj['warnings'] = warnings;
    }

    /**
     * Constructs a <code>PersonalisedMusicPlaylistVersion</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PersonalisedMusicPlaylistVersion} obj Optional instance to populate.
     * @return {module:model/PersonalisedMusicPlaylistVersion} The populated <code>PersonalisedMusicPlaylistVersion</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PersonalisedMusicPlaylistVersion();

            if (data.hasOwnProperty('duration')) {
                obj['duration'] = ApiClient.convertToType(data['duration'], 'String');
            }
            if (data.hasOwnProperty('expires_at')) {
                obj['expires_at'] = ApiClient.convertToType(data['expires_at'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('starts_at')) {
                obj['starts_at'] = ApiClient.convertToType(data['starts_at'], 'String');
            }
            if (data.hasOwnProperty('warnings')) {
                obj['warnings'] = ApiClient.convertToType(data['warnings'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PersonalisedMusicPlaylistVersion</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PersonalisedMusicPlaylistVersion</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PersonalisedMusicPlaylistVersion.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['duration'] && !(typeof data['duration'] === 'string' || data['duration'] instanceof String)) {
            throw new Error("Expected the field `duration` to be a primitive type in the JSON string but got " + data['duration']);
        }
        // ensure the json data is a string
        if (data['expires_at'] && !(typeof data['expires_at'] === 'string' || data['expires_at'] instanceof String)) {
            throw new Error("Expected the field `expires_at` to be a primitive type in the JSON string but got " + data['expires_at']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['starts_at'] && !(typeof data['starts_at'] === 'string' || data['starts_at'] instanceof String)) {
            throw new Error("Expected the field `starts_at` to be a primitive type in the JSON string but got " + data['starts_at']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['warnings'])) {
            throw new Error("Expected the field `warnings` to be an array in the JSON data but got " + data['warnings']);
        }

        return true;
    }


}

PersonalisedMusicPlaylistVersion.RequiredProperties = ["warnings"];

/**
 * @member {String} duration
 */
PersonalisedMusicPlaylistVersion.prototype['duration'] = undefined;

/**
 * @member {String} expires_at
 */
PersonalisedMusicPlaylistVersion.prototype['expires_at'] = undefined;

/**
 * @member {String} id
 */
PersonalisedMusicPlaylistVersion.prototype['id'] = undefined;

/**
 * @member {String} starts_at
 */
PersonalisedMusicPlaylistVersion.prototype['starts_at'] = undefined;

/**
 * @member {Array.<String>} warnings
 */
PersonalisedMusicPlaylistVersion.prototype['warnings'] = undefined;






export default PersonalisedMusicPlaylistVersion;

