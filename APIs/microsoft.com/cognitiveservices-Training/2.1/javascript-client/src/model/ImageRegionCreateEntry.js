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

/**
 * The ImageRegionCreateEntry model module.
 * @module model/ImageRegionCreateEntry
 * @version 2.1
 */
class ImageRegionCreateEntry {
    /**
     * Constructs a new <code>ImageRegionCreateEntry</code>.
     * @alias module:model/ImageRegionCreateEntry
     */
    constructor() { 
        
        ImageRegionCreateEntry.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageRegionCreateEntry</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageRegionCreateEntry} obj Optional instance to populate.
     * @return {module:model/ImageRegionCreateEntry} The populated <code>ImageRegionCreateEntry</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageRegionCreateEntry();

            if (data.hasOwnProperty('height')) {
                obj['height'] = ApiClient.convertToType(data['height'], 'Number');
            }
            if (data.hasOwnProperty('imageId')) {
                obj['imageId'] = ApiClient.convertToType(data['imageId'], 'String');
            }
            if (data.hasOwnProperty('left')) {
                obj['left'] = ApiClient.convertToType(data['left'], 'Number');
            }
            if (data.hasOwnProperty('tagId')) {
                obj['tagId'] = ApiClient.convertToType(data['tagId'], 'String');
            }
            if (data.hasOwnProperty('top')) {
                obj['top'] = ApiClient.convertToType(data['top'], 'Number');
            }
            if (data.hasOwnProperty('width')) {
                obj['width'] = ApiClient.convertToType(data['width'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageRegionCreateEntry</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageRegionCreateEntry</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['imageId'] && !(typeof data['imageId'] === 'string' || data['imageId'] instanceof String)) {
            throw new Error("Expected the field `imageId` to be a primitive type in the JSON string but got " + data['imageId']);
        }
        // ensure the json data is a string
        if (data['tagId'] && !(typeof data['tagId'] === 'string' || data['tagId'] instanceof String)) {
            throw new Error("Expected the field `tagId` to be a primitive type in the JSON string but got " + data['tagId']);
        }

        return true;
    }


}



/**
 * @member {Number} height
 */
ImageRegionCreateEntry.prototype['height'] = undefined;

/**
 * @member {String} imageId
 */
ImageRegionCreateEntry.prototype['imageId'] = undefined;

/**
 * @member {Number} left
 */
ImageRegionCreateEntry.prototype['left'] = undefined;

/**
 * @member {String} tagId
 */
ImageRegionCreateEntry.prototype['tagId'] = undefined;

/**
 * @member {Number} top
 */
ImageRegionCreateEntry.prototype['top'] = undefined;

/**
 * @member {Number} width
 */
ImageRegionCreateEntry.prototype['width'] = undefined;






export default ImageRegionCreateEntry;

