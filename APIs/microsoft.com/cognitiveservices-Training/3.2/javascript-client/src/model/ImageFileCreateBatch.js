/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ImageFileCreateEntry from './ImageFileCreateEntry';

/**
 * The ImageFileCreateBatch model module.
 * @module model/ImageFileCreateBatch
 * @version 3.2
 */
class ImageFileCreateBatch {
    /**
     * Constructs a new <code>ImageFileCreateBatch</code>.
     * @alias module:model/ImageFileCreateBatch
     */
    constructor() { 
        
        ImageFileCreateBatch.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageFileCreateBatch</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageFileCreateBatch} obj Optional instance to populate.
     * @return {module:model/ImageFileCreateBatch} The populated <code>ImageFileCreateBatch</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageFileCreateBatch();

            if (data.hasOwnProperty('images')) {
                obj['images'] = ApiClient.convertToType(data['images'], [ImageFileCreateEntry]);
            }
            if (data.hasOwnProperty('tagIds')) {
                obj['tagIds'] = ApiClient.convertToType(data['tagIds'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageFileCreateBatch</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageFileCreateBatch</code>.
     */
    static validateJSON(data) {
        if (data['images']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['images'])) {
                throw new Error("Expected the field `images` to be an array in the JSON data but got " + data['images']);
            }
            // validate the optional field `images` (array)
            for (const item of data['images']) {
                ImageFileCreateEntry.validateJSON(item);
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
 * @member {Array.<module:model/ImageFileCreateEntry>} images
 */
ImageFileCreateBatch.prototype['images'] = undefined;

/**
 * @member {Array.<String>} tagIds
 */
ImageFileCreateBatch.prototype['tagIds'] = undefined;






export default ImageFileCreateBatch;

