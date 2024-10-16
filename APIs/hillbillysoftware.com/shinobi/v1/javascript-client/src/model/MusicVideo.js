/**
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The MusicVideo model module.
 * @module model/MusicVideo
 * @version v1
 */
class MusicVideo {
    /**
     * Constructs a new <code>MusicVideo</code>.
     * @alias module:model/MusicVideo
     */
    constructor() { 
        
        MusicVideo.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MusicVideo</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MusicVideo} obj Optional instance to populate.
     * @return {module:model/MusicVideo} The populated <code>MusicVideo</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MusicVideo();

            if (data.hasOwnProperty('AlbumID')) {
                obj['AlbumID'] = ApiClient.convertToType(data['AlbumID'], 'String');
            }
            if (data.hasOwnProperty('ArtistID')) {
                obj['ArtistID'] = ApiClient.convertToType(data['ArtistID'], 'String');
            }
            if (data.hasOwnProperty('Decription')) {
                obj['Decription'] = ApiClient.convertToType(data['Decription'], 'String');
            }
            if (data.hasOwnProperty('Video')) {
                obj['Video'] = ApiClient.convertToType(data['Video'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MusicVideo</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MusicVideo</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AlbumID'] && !(typeof data['AlbumID'] === 'string' || data['AlbumID'] instanceof String)) {
            throw new Error("Expected the field `AlbumID` to be a primitive type in the JSON string but got " + data['AlbumID']);
        }
        // ensure the json data is a string
        if (data['ArtistID'] && !(typeof data['ArtistID'] === 'string' || data['ArtistID'] instanceof String)) {
            throw new Error("Expected the field `ArtistID` to be a primitive type in the JSON string but got " + data['ArtistID']);
        }
        // ensure the json data is a string
        if (data['Decription'] && !(typeof data['Decription'] === 'string' || data['Decription'] instanceof String)) {
            throw new Error("Expected the field `Decription` to be a primitive type in the JSON string but got " + data['Decription']);
        }
        // ensure the json data is a string
        if (data['Video'] && !(typeof data['Video'] === 'string' || data['Video'] instanceof String)) {
            throw new Error("Expected the field `Video` to be a primitive type in the JSON string but got " + data['Video']);
        }

        return true;
    }


}



/**
 * @member {String} AlbumID
 */
MusicVideo.prototype['AlbumID'] = undefined;

/**
 * @member {String} ArtistID
 */
MusicVideo.prototype['ArtistID'] = undefined;

/**
 * @member {String} Decription
 */
MusicVideo.prototype['Decription'] = undefined;

/**
 * @member {String} Video
 */
MusicVideo.prototype['Video'] = undefined;






export default MusicVideo;

