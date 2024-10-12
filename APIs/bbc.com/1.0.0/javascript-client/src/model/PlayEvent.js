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
import PlayedInLinks from './PlayedInLinks';
import Synopses from './Synopses';

/**
 * The PlayEvent model module.
 * @module model/PlayEvent
 * @version 1.0.0
 */
class PlayEvent {
    /**
     * Constructs a new <code>PlayEvent</code>.
     * @alias module:model/PlayEvent
     * @param pid {String} 
     */
    constructor(pid) { 
        
        PlayEvent.initialize(this, pid);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, pid) { 
        obj['pid'] = pid;
    }

    /**
     * Constructs a <code>PlayEvent</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PlayEvent} obj Optional instance to populate.
     * @return {module:model/PlayEvent} The populated <code>PlayEvent</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PlayEvent();

            if (data.hasOwnProperty('offset')) {
                obj['offset'] = ApiClient.convertToType(data['offset'], 'Number');
            }
            if (data.hasOwnProperty('pid')) {
                obj['pid'] = ApiClient.convertToType(data['pid'], 'String');
            }
            if (data.hasOwnProperty('played_in_links')) {
                obj['played_in_links'] = ApiClient.convertToType(data['played_in_links'], [PlayedInLinks]);
            }
            if (data.hasOwnProperty('position')) {
                obj['position'] = ApiClient.convertToType(data['position'], 'Number');
            }
            if (data.hasOwnProperty('synopses')) {
                obj['synopses'] = Synopses.constructFromObject(data['synopses']);
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PlayEvent</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PlayEvent</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PlayEvent.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['pid'] && !(typeof data['pid'] === 'string' || data['pid'] instanceof String)) {
            throw new Error("Expected the field `pid` to be a primitive type in the JSON string but got " + data['pid']);
        }
        if (data['played_in_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['played_in_links'])) {
                throw new Error("Expected the field `played_in_links` to be an array in the JSON data but got " + data['played_in_links']);
            }
            // validate the optional field `played_in_links` (array)
            for (const item of data['played_in_links']) {
                PlayedInLinks.validateJSON(item);
            };
        }
        // validate the optional field `synopses`
        if (data['synopses']) { // data not null
          Synopses.validateJSON(data['synopses']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}

PlayEvent.RequiredProperties = ["pid"];

/**
 * @member {Number} offset
 */
PlayEvent.prototype['offset'] = undefined;

/**
 * @member {String} pid
 */
PlayEvent.prototype['pid'] = undefined;

/**
 * @member {Array.<module:model/PlayedInLinks>} played_in_links
 */
PlayEvent.prototype['played_in_links'] = undefined;

/**
 * @member {Number} position
 */
PlayEvent.prototype['position'] = undefined;

/**
 * @member {module:model/Synopses} synopses
 */
PlayEvent.prototype['synopses'] = undefined;

/**
 * @member {String} title
 */
PlayEvent.prototype['title'] = undefined;






export default PlayEvent;

