/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ImageIdCreateEntry from './ImageIdCreateEntry';

/**
 * The ImageIdCreateBatch model module.
 * @module model/ImageIdCreateBatch
 * @version 3.1
 */
class ImageIdCreateBatch {
    /**
     * Constructs a new <code>ImageIdCreateBatch</code>.
     * @alias module:model/ImageIdCreateBatch
     */
    constructor() { 
        
        ImageIdCreateBatch.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageIdCreateBatch</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageIdCreateBatch} obj Optional instance to populate.
     * @return {module:model/ImageIdCreateBatch} The populated <code>ImageIdCreateBatch</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageIdCreateBatch();

            if (data.hasOwnProperty('images')) {
                obj['images'] = ApiClient.convertToType(data['images'], [ImageIdCreateEntry]);
            }
            if (data.hasOwnProperty('tagIds')) {
                obj['tagIds'] = ApiClient.convertToType(data['tagIds'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageIdCreateBatch</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageIdCreateBatch</code>.
     */
    static validateJSON(data) {
        if (data['images']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['images'])) {
                throw new Error("Expected the field `images` to be an array in the JSON data but got " + data['images']);
            }
            // validate the optional field `images` (array)
            for (const item of data['images']) {
                ImageIdCreateEntry.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['tagIds'])) {
            throw new Error("Expected the field `tagIds` to be an array in the JSON data but got " + data['tagIds']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ImageIdCreateEntry>} images
 */
ImageIdCreateBatch.prototype['images'] = undefined;

/**
 * @member {Array.<String>} tagIds
 */
ImageIdCreateBatch.prototype['tagIds'] = undefined;






export default ImageIdCreateBatch;

