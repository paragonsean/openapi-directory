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
 * The PersonalisedMusicClipParentProgramme model module.
 * @module model/PersonalisedMusicClipParentProgramme
 * @version 1.0.0
 */
class PersonalisedMusicClipParentProgramme {
    /**
     * Constructs a new <code>PersonalisedMusicClipParentProgramme</code>.
     * @alias module:model/PersonalisedMusicClipParentProgramme
     */
    constructor() { 
        
        PersonalisedMusicClipParentProgramme.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PersonalisedMusicClipParentProgramme</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PersonalisedMusicClipParentProgramme} obj Optional instance to populate.
     * @return {module:model/PersonalisedMusicClipParentProgramme} The populated <code>PersonalisedMusicClipParentProgramme</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PersonalisedMusicClipParentProgramme();

            if (data.hasOwnProperty('entityType')) {
                obj['entityType'] = ApiClient.convertToType(data['entityType'], 'String');
            }
            if (data.hasOwnProperty('pid')) {
                obj['pid'] = ApiClient.convertToType(data['pid'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PersonalisedMusicClipParentProgramme</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PersonalisedMusicClipParentProgramme</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['entityType'] && !(typeof data['entityType'] === 'string' || data['entityType'] instanceof String)) {
            throw new Error("Expected the field `entityType` to be a primitive type in the JSON string but got " + data['entityType']);
        }
        // ensure the json data is a string
        if (data['pid'] && !(typeof data['pid'] === 'string' || data['pid'] instanceof String)) {
            throw new Error("Expected the field `pid` to be a primitive type in the JSON string but got " + data['pid']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}



/**
 * @member {String} entityType
 */
PersonalisedMusicClipParentProgramme.prototype['entityType'] = undefined;

/**
 * @member {String} pid
 */
PersonalisedMusicClipParentProgramme.prototype['pid'] = undefined;

/**
 * @member {String} title
 */
PersonalisedMusicClipParentProgramme.prototype['title'] = undefined;






export default PersonalisedMusicClipParentProgramme;

