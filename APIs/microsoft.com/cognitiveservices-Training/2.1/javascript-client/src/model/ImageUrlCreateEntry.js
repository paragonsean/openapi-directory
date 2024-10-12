/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Region from './Region';

/**
 * The ImageUrlCreateEntry model module.
 * @module model/ImageUrlCreateEntry
 * @version 2.1
 */
class ImageUrlCreateEntry {
    /**
     * Constructs a new <code>ImageUrlCreateEntry</code>.
     * @alias module:model/ImageUrlCreateEntry
     */
    constructor() { 
        
        ImageUrlCreateEntry.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageUrlCreateEntry</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageUrlCreateEntry} obj Optional instance to populate.
     * @return {module:model/ImageUrlCreateEntry} The populated <code>ImageUrlCreateEntry</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageUrlCreateEntry();

            if (data.hasOwnProperty('regions')) {
                obj['regions'] = ApiClient.convertToType(data['regions'], [Region]);
            }
            if (data.hasOwnProperty('tagIds')) {
                obj['tagIds'] = ApiClient.convertToType(data['tagIds'], ['String']);
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageUrlCreateEntry</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageUrlCreateEntry</code>.
     */
    static validateJSON(data) {
        if (data['regions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['regions'])) {
                throw new Error("Expected the field `regions` to be an array in the JSON data but got " + data['regions']);
            }
            // validate the optional field `regions` (array)
            for (const item of data['regions']) {
                Region.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['tagIds'])) {
            throw new Error("Expected the field `tagIds` to be an array in the JSON data but got " + data['tagIds']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Region>} regions
 */
ImageUrlCreateEntry.prototype['regions'] = undefined;

/**
 * @member {Array.<String>} tagIds
 */
ImageUrlCreateEntry.prototype['tagIds'] = undefined;

/**
 * @member {String} url
 */
ImageUrlCreateEntry.prototype['url'] = undefined;






export default ImageUrlCreateEntry;

