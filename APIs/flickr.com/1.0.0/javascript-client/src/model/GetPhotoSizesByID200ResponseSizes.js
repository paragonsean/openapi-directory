/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Size from './Size';

/**
 * The GetPhotoSizesByID200ResponseSizes model module.
 * @module model/GetPhotoSizesByID200ResponseSizes
 * @version 1.0.0
 */
class GetPhotoSizesByID200ResponseSizes {
    /**
     * Constructs a new <code>GetPhotoSizesByID200ResponseSizes</code>.
     * @alias module:model/GetPhotoSizesByID200ResponseSizes
     */
    constructor() { 
        
        GetPhotoSizesByID200ResponseSizes.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetPhotoSizesByID200ResponseSizes</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetPhotoSizesByID200ResponseSizes} obj Optional instance to populate.
     * @return {module:model/GetPhotoSizesByID200ResponseSizes} The populated <code>GetPhotoSizesByID200ResponseSizes</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetPhotoSizesByID200ResponseSizes();

            if (data.hasOwnProperty('canblog')) {
                obj['canblog'] = ApiClient.convertToType(data['canblog'], 'Number');
            }
            if (data.hasOwnProperty('candownload')) {
                obj['candownload'] = ApiClient.convertToType(data['candownload'], 'Number');
            }
            if (data.hasOwnProperty('canprint')) {
                obj['canprint'] = ApiClient.convertToType(data['canprint'], 'Number');
            }
            if (data.hasOwnProperty('sizes')) {
                obj['sizes'] = ApiClient.convertToType(data['sizes'], [Size]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetPhotoSizesByID200ResponseSizes</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetPhotoSizesByID200ResponseSizes</code>.
     */
    static validateJSON(data) {
        if (data['sizes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['sizes'])) {
                throw new Error("Expected the field `sizes` to be an array in the JSON data but got " + data['sizes']);
            }
            // validate the optional field `sizes` (array)
            for (const item of data['sizes']) {
                Size.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Number} canblog
 */
GetPhotoSizesByID200ResponseSizes.prototype['canblog'] = undefined;

/**
 * @member {Number} candownload
 */
GetPhotoSizesByID200ResponseSizes.prototype['candownload'] = undefined;

/**
 * @member {Number} canprint
 */
GetPhotoSizesByID200ResponseSizes.prototype['canprint'] = undefined;

/**
 * @member {Array.<module:model/Size>} sizes
 */
GetPhotoSizesByID200ResponseSizes.prototype['sizes'] = undefined;






export default GetPhotoSizesByID200ResponseSizes;

