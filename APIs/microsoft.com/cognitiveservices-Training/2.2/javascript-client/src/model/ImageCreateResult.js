/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Image from './Image';

/**
 * The ImageCreateResult model module.
 * @module model/ImageCreateResult
 * @version 2.2
 */
class ImageCreateResult {
    /**
     * Constructs a new <code>ImageCreateResult</code>.
     * @alias module:model/ImageCreateResult
     */
    constructor() { 
        
        ImageCreateResult.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ImageCreateResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageCreateResult} obj Optional instance to populate.
     * @return {module:model/ImageCreateResult} The populated <code>ImageCreateResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageCreateResult();

            if (data.hasOwnProperty('image')) {
                obj['image'] = Image.constructFromObject(data['image']);
            }
            if (data.hasOwnProperty('sourceUrl')) {
                obj['sourceUrl'] = ApiClient.convertToType(data['sourceUrl'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageCreateResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageCreateResult</code>.
     */
    static validateJSON(data) {
        // validate the optional field `image`
        if (data['image']) { // data not null
          Image.validateJSON(data['image']);
        }
        // ensure the json data is a string
        if (data['sourceUrl'] && !(typeof data['sourceUrl'] === 'string' || data['sourceUrl'] instanceof String)) {
            throw new Error("Expected the field `sourceUrl` to be a primitive type in the JSON string but got " + data['sourceUrl']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * @member {module:model/Image} image
 */
ImageCreateResult.prototype['image'] = undefined;

/**
 * Source URL of the image.
 * @member {String} sourceUrl
 */
ImageCreateResult.prototype['sourceUrl'] = undefined;

/**
 * Status of the image creation.
 * @member {module:model/ImageCreateResult.StatusEnum} status
 */
ImageCreateResult.prototype['status'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
ImageCreateResult['StatusEnum'] = {

    /**
     * value: "OK"
     * @const
     */
    "OK": "OK",

    /**
     * value: "OKDuplicate"
     * @const
     */
    "OKDuplicate": "OKDuplicate",

    /**
     * value: "ErrorSource"
     * @const
     */
    "ErrorSource": "ErrorSource",

    /**
     * value: "ErrorImageFormat"
     * @const
     */
    "ErrorImageFormat": "ErrorImageFormat",

    /**
     * value: "ErrorImageSize"
     * @const
     */
    "ErrorImageSize": "ErrorImageSize",

    /**
     * value: "ErrorStorage"
     * @const
     */
    "ErrorStorage": "ErrorStorage",

    /**
     * value: "ErrorLimitExceed"
     * @const
     */
    "ErrorLimitExceed": "ErrorLimitExceed",

    /**
     * value: "ErrorTagLimitExceed"
     * @const
     */
    "ErrorTagLimitExceed": "ErrorTagLimitExceed",

    /**
     * value: "ErrorRegionLimitExceed"
     * @const
     */
    "ErrorRegionLimitExceed": "ErrorRegionLimitExceed",

    /**
     * value: "ErrorUnknown"
     * @const
     */
    "ErrorUnknown": "ErrorUnknown",

    /**
     * value: "ErrorNegativeAndRegularTagOnSameImage"
     * @const
     */
    "ErrorNegativeAndRegularTagOnSameImage": "ErrorNegativeAndRegularTagOnSameImage"
};



export default ImageCreateResult;

