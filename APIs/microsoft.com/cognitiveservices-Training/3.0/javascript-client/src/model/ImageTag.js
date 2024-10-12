/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ImageTag model module.
 * @module model/ImageTag
 * @version 3.0
 */
class ImageTag {
    /**
     * Constructs a new <code>ImageTag</code>.
     * @alias module:model/ImageTag
     */
    constructor() { 
        
        ImageTag.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageTag</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageTag} obj Optional instance to populate.
     * @return {module:model/ImageTag} The populated <code>ImageTag</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageTag();

            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'Date');
            }
            if (data.hasOwnProperty('tagId')) {
                obj['tagId'] = ApiClient.convertToType(data['tagId'], 'String');
            }
            if (data.hasOwnProperty('tagName')) {
                obj['tagName'] = ApiClient.convertToType(data['tagName'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageTag</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageTag</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['tagId'] && !(typeof data['tagId'] === 'string' || data['tagId'] instanceof String)) {
            throw new Error("Expected the field `tagId` to be a primitive type in the JSON string but got " + data['tagId']);
        }
        // ensure the json data is a string
        if (data['tagName'] && !(typeof data['tagName'] === 'string' || data['tagName'] instanceof String)) {
            throw new Error("Expected the field `tagName` to be a primitive type in the JSON string but got " + data['tagName']);
        }

        return true;
    }


}



/**
 * @member {Date} created
 */
ImageTag.prototype['created'] = undefined;

/**
 * @member {String} tagId
 */
ImageTag.prototype['tagId'] = undefined;

/**
 * @member {String} tagName
 */
ImageTag.prototype['tagName'] = undefined;






export default ImageTag;

