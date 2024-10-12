/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ImageTagCreateEntry from './ImageTagCreateEntry';

/**
 * The ImageTagCreateBatch model module.
 * @module model/ImageTagCreateBatch
 * @version 1.2
 */
class ImageTagCreateBatch {
    /**
     * Constructs a new <code>ImageTagCreateBatch</code>.
     * @alias module:model/ImageTagCreateBatch
     */
    constructor() { 
        
        ImageTagCreateBatch.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageTagCreateBatch</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageTagCreateBatch} obj Optional instance to populate.
     * @return {module:model/ImageTagCreateBatch} The populated <code>ImageTagCreateBatch</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageTagCreateBatch();

            if (data.hasOwnProperty('Tags')) {
                obj['Tags'] = ApiClient.convertToType(data['Tags'], [ImageTagCreateEntry]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageTagCreateBatch</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageTagCreateBatch</code>.
     */
    static validateJSON(data) {
        if (data['Tags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Tags'])) {
                throw new Error("Expected the field `Tags` to be an array in the JSON data but got " + data['Tags']);
            }
            // validate the optional field `Tags` (array)
            for (const item of data['Tags']) {
                ImageTagCreateEntry.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ImageTagCreateEntry>} Tags
 */
ImageTagCreateBatch.prototype['Tags'] = undefined;






export default ImageTagCreateBatch;

