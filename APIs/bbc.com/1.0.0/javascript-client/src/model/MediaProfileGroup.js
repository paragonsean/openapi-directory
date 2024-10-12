/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The MediaProfileGroup model module.
 * @module model/MediaProfileGroup
 * @version 1.0.0
 */
class MediaProfileGroup {
    /**
     * Constructs a new <code>MediaProfileGroup</code>.
     * @alias module:model/MediaProfileGroup
     */
    constructor() { 
        
        MediaProfileGroup.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>MediaProfileGroup</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MediaProfileGroup} obj Optional instance to populate.
     * @return {module:model/MediaProfileGroup} The populated <code>MediaProfileGroup</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MediaProfileGroup();

            if (data.hasOwnProperty('#text')) {
                obj['#text'] = ApiClient.convertToType(data['#text'], 'String');
            }
            if (data.hasOwnProperty('context')) {
                obj['context'] = ApiClient.convertToType(data['context'], 'String');
            }
            if (data.hasOwnProperty('pid')) {
                obj['pid'] = ApiClient.convertToType(data['pid'], 'String');
            }
            if (data.hasOwnProperty('platform')) {
                obj['platform'] = ApiClient.convertToType(data['platform'], 'String');
            }
            if (data.hasOwnProperty('territory')) {
                obj['territory'] = ApiClient.convertToType(data['territory'], 'String');
            }
            if (data.hasOwnProperty('transport')) {
                obj['transport'] = ApiClient.convertToType(data['transport'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MediaProfileGroup</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MediaProfileGroup</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['#text'] && !(typeof data['#text'] === 'string' || data['#text'] instanceof String)) {
            throw new Error("Expected the field `#text` to be a primitive type in the JSON string but got " + data['#text']);
        }
        // ensure the json data is a string
        if (data['context'] && !(typeof data['context'] === 'string' || data['context'] instanceof String)) {
            throw new Error("Expected the field `context` to be a primitive type in the JSON string but got " + data['context']);
        }
        // ensure the json data is a string
        if (data['pid'] && !(typeof data['pid'] === 'string' || data['pid'] instanceof String)) {
            throw new Error("Expected the field `pid` to be a primitive type in the JSON string but got " + data['pid']);
        }
        // ensure the json data is a string
        if (data['platform'] && !(typeof data['platform'] === 'string' || data['platform'] instanceof String)) {
            throw new Error("Expected the field `platform` to be a primitive type in the JSON string but got " + data['platform']);
        }
        // ensure the json data is a string
        if (data['territory'] && !(typeof data['territory'] === 'string' || data['territory'] instanceof String)) {
            throw new Error("Expected the field `territory` to be a primitive type in the JSON string but got " + data['territory']);
        }
        // ensure the json data is a string
        if (data['transport'] && !(typeof data['transport'] === 'string' || data['transport'] instanceof String)) {
            throw new Error("Expected the field `transport` to be a primitive type in the JSON string but got " + data['transport']);
        }

        return true;
    }


}



/**
 * @member {String} #text
 */
MediaProfileGroup.prototype['#text'] = undefined;

/**
 * @member {String} context
 */
MediaProfileGroup.prototype['context'] = undefined;

/**
 * @member {String} pid
 */
MediaProfileGroup.prototype['pid'] = undefined;

/**
 * @member {String} platform
 */
MediaProfileGroup.prototype['platform'] = undefined;

/**
 * @member {String} territory
 */
MediaProfileGroup.prototype['territory'] = undefined;

/**
 * @member {String} transport
 */
MediaProfileGroup.prototype['transport'] = undefined;






export default MediaProfileGroup;

