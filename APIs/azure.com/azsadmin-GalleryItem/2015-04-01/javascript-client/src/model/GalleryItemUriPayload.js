/**
 * GalleryManagementClient
 * The Admin Gallery Management Client.
 *
 * The version of the OpenAPI document: 2015-04-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GalleryItemUriPayload model module.
 * @module model/GalleryItemUriPayload
 * @version 2015-04-01
 */
class GalleryItemUriPayload {
    /**
     * Constructs a new <code>GalleryItemUriPayload</code>.
     * Location of gallery item payload.
     * @alias module:model/GalleryItemUriPayload
     */
    constructor() { 
        
        GalleryItemUriPayload.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GalleryItemUriPayload</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GalleryItemUriPayload} obj Optional instance to populate.
     * @return {module:model/GalleryItemUriPayload} The populated <code>GalleryItemUriPayload</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GalleryItemUriPayload();

            if (data.hasOwnProperty('galleryItemUri')) {
                obj['galleryItemUri'] = ApiClient.convertToType(data['galleryItemUri'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GalleryItemUriPayload</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GalleryItemUriPayload</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['galleryItemUri'] && !(typeof data['galleryItemUri'] === 'string' || data['galleryItemUri'] instanceof String)) {
            throw new Error("Expected the field `galleryItemUri` to be a primitive type in the JSON string but got " + data['galleryItemUri']);
        }

        return true;
    }


}



/**
 * URI for your gallery package that has already been uploaded online.
 * @member {String} galleryItemUri
 */
GalleryItemUriPayload.prototype['galleryItemUri'] = undefined;






export default GalleryItemUriPayload;

