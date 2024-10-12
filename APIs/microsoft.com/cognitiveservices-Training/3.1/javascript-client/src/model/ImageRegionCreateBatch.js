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
import ImageRegionCreateEntry from './ImageRegionCreateEntry';

/**
 * The ImageRegionCreateBatch model module.
 * @module model/ImageRegionCreateBatch
 * @version 3.1
 */
class ImageRegionCreateBatch {
    /**
     * Constructs a new <code>ImageRegionCreateBatch</code>.
     * Batch of image region information to create.
     * @alias module:model/ImageRegionCreateBatch
     */
    constructor() { 
        
        ImageRegionCreateBatch.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageRegionCreateBatch</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageRegionCreateBatch} obj Optional instance to populate.
     * @return {module:model/ImageRegionCreateBatch} The populated <code>ImageRegionCreateBatch</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageRegionCreateBatch();

            if (data.hasOwnProperty('regions')) {
                obj['regions'] = ApiClient.convertToType(data['regions'], [ImageRegionCreateEntry]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageRegionCreateBatch</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageRegionCreateBatch</code>.
     */
    static validateJSON(data) {
        if (data['regions']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['regions'])) {
                throw new Error("Expected the field `regions` to be an array in the JSON data but got " + data['regions']);
            }
            // validate the optional field `regions` (array)
            for (const item of data['regions']) {
                ImageRegionCreateEntry.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ImageRegionCreateEntry>} regions
 */
ImageRegionCreateBatch.prototype['regions'] = undefined;






export default ImageRegionCreateBatch;

