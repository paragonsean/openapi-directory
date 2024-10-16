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
import GetFavoritesContextByID200ResponseCount from './GetFavoritesContextByID200ResponseCount';

/**
 * The GetPhotoExifByID200ResponsePhotoExifInner model module.
 * @module model/GetPhotoExifByID200ResponsePhotoExifInner
 * @version 1.0.0
 */
class GetPhotoExifByID200ResponsePhotoExifInner {
    /**
     * Constructs a new <code>GetPhotoExifByID200ResponsePhotoExifInner</code>.
     * @alias module:model/GetPhotoExifByID200ResponsePhotoExifInner
     */
    constructor() { 
        
        GetPhotoExifByID200ResponsePhotoExifInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetPhotoExifByID200ResponsePhotoExifInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetPhotoExifByID200ResponsePhotoExifInner} obj Optional instance to populate.
     * @return {module:model/GetPhotoExifByID200ResponsePhotoExifInner} The populated <code>GetPhotoExifByID200ResponsePhotoExifInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetPhotoExifByID200ResponsePhotoExifInner();

            if (data.hasOwnProperty('label')) {
                obj['label'] = ApiClient.convertToType(data['label'], 'String');
            }
            if (data.hasOwnProperty('raw')) {
                obj['raw'] = GetFavoritesContextByID200ResponseCount.constructFromObject(data['raw']);
            }
            if (data.hasOwnProperty('tag')) {
                obj['tag'] = ApiClient.convertToType(data['tag'], 'String');
            }
            if (data.hasOwnProperty('tagspace')) {
                obj['tagspace'] = ApiClient.convertToType(data['tagspace'], 'String');
            }
            if (data.hasOwnProperty('tagspaceid')) {
                obj['tagspaceid'] = ApiClient.convertToType(data['tagspaceid'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetPhotoExifByID200ResponsePhotoExifInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetPhotoExifByID200ResponsePhotoExifInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['label'] && !(typeof data['label'] === 'string' || data['label'] instanceof String)) {
            throw new Error("Expected the field `label` to be a primitive type in the JSON string but got " + data['label']);
        }
        // validate the optional field `raw`
        if (data['raw']) { // data not null
          GetFavoritesContextByID200ResponseCount.validateJSON(data['raw']);
        }
        // ensure the json data is a string
        if (data['tag'] && !(typeof data['tag'] === 'string' || data['tag'] instanceof String)) {
            throw new Error("Expected the field `tag` to be a primitive type in the JSON string but got " + data['tag']);
        }
        // ensure the json data is a string
        if (data['tagspace'] && !(typeof data['tagspace'] === 'string' || data['tagspace'] instanceof String)) {
            throw new Error("Expected the field `tagspace` to be a primitive type in the JSON string but got " + data['tagspace']);
        }
        // ensure the json data is a string
        if (data['tagspaceid'] && !(typeof data['tagspaceid'] === 'string' || data['tagspaceid'] instanceof String)) {
            throw new Error("Expected the field `tagspaceid` to be a primitive type in the JSON string but got " + data['tagspaceid']);
        }

        return true;
    }


}



/**
 * @member {String} label
 */
GetPhotoExifByID200ResponsePhotoExifInner.prototype['label'] = undefined;

/**
 * @member {module:model/GetFavoritesContextByID200ResponseCount} raw
 */
GetPhotoExifByID200ResponsePhotoExifInner.prototype['raw'] = undefined;

/**
 * @member {String} tag
 */
GetPhotoExifByID200ResponsePhotoExifInner.prototype['tag'] = undefined;

/**
 * @member {String} tagspace
 */
GetPhotoExifByID200ResponsePhotoExifInner.prototype['tagspace'] = undefined;

/**
 * @member {String} tagspaceid
 */
GetPhotoExifByID200ResponsePhotoExifInner.prototype['tagspaceid'] = undefined;






export default GetPhotoExifByID200ResponsePhotoExifInner;

