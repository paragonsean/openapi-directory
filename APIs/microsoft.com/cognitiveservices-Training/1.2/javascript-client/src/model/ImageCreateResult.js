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
import Image from './Image';

/**
 * The ImageCreateResult model module.
 * @module model/ImageCreateResult
 * @version 1.2
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

            if (data.hasOwnProperty('Image')) {
                obj['Image'] = Image.constructFromObject(data['Image']);
            }
            if (data.hasOwnProperty('SourceUrl')) {
                obj['SourceUrl'] = ApiClient.convertToType(data['SourceUrl'], 'String');
            }
            if (data.hasOwnProperty('Status')) {
                obj['Status'] = ApiClient.convertToType(data['Status'], 'String');
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
        // validate the optional field `Image`
        if (data['Image']) { // data not null
          Image.validateJSON(data['Image']);
        }
        // ensure the json data is a string
        if (data['SourceUrl'] && !(typeof data['SourceUrl'] === 'string' || data['SourceUrl'] instanceof String)) {
            throw new Error("Expected the field `SourceUrl` to be a primitive type in the JSON string but got " + data['SourceUrl']);
        }
        // ensure the json data is a string
        if (data['Status'] && !(typeof data['Status'] === 'string' || data['Status'] instanceof String)) {
            throw new Error("Expected the field `Status` to be a primitive type in the JSON string but got " + data['Status']);
        }

        return true;
    }


}



/**
 * @member {module:model/Image} Image
 */
ImageCreateResult.prototype['Image'] = undefined;

/**
 * @member {String} SourceUrl
 */
ImageCreateResult.prototype['SourceUrl'] = undefined;

/**
 * @member {module:model/ImageCreateResult.StatusEnum} Status
 */
ImageCreateResult.prototype['Status'] = undefined;





/**
 * Allowed values for the <code>Status</code> property.
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
     * value: "ErrorUnknown"
     * @const
     */
    "ErrorUnknown": "ErrorUnknown"
};



export default ImageCreateResult;

