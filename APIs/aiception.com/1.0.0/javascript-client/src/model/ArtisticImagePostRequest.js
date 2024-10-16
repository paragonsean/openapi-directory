/**
 * AIception Interactive
 * Here you can play & test & prototype all the endpoints using just your browser! Go ahead!
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

/**
 * The ArtisticImagePostRequest model module.
 * @module model/ArtisticImagePostRequest
 * @version 1.0.0
 */
class ArtisticImagePostRequest {
    /**
     * Constructs a new <code>ArtisticImagePostRequest</code>.
     * @alias module:model/ArtisticImagePostRequest
     * @param imageUrl {String} 
     * @param styleUrl {String} 
     */
    constructor(imageUrl, styleUrl) { 
        
        ArtisticImagePostRequest.initialize(this, imageUrl, styleUrl);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, imageUrl, styleUrl) { 
        obj['async'] = true;
        obj['image_url'] = imageUrl;
        obj['style_url'] = styleUrl;
    }

    /**
     * Constructs a <code>ArtisticImagePostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ArtisticImagePostRequest} obj Optional instance to populate.
     * @return {module:model/ArtisticImagePostRequest} The populated <code>ArtisticImagePostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ArtisticImagePostRequest();

            if (data.hasOwnProperty('async')) {
                obj['async'] = ApiClient.convertToType(data['async'], 'Boolean');
            }
            if (data.hasOwnProperty('image_url')) {
                obj['image_url'] = ApiClient.convertToType(data['image_url'], 'String');
            }
            if (data.hasOwnProperty('style_url')) {
                obj['style_url'] = ApiClient.convertToType(data['style_url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ArtisticImagePostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ArtisticImagePostRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ArtisticImagePostRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['image_url'] && !(typeof data['image_url'] === 'string' || data['image_url'] instanceof String)) {
            throw new Error("Expected the field `image_url` to be a primitive type in the JSON string but got " + data['image_url']);
        }
        // ensure the json data is a string
        if (data['style_url'] && !(typeof data['style_url'] === 'string' || data['style_url'] instanceof String)) {
            throw new Error("Expected the field `style_url` to be a primitive type in the JSON string but got " + data['style_url']);
        }

        return true;
    }


}

ArtisticImagePostRequest.RequiredProperties = ["image_url", "style_url"];

/**
 * @member {Boolean} async
 * @default true
 */
ArtisticImagePostRequest.prototype['async'] = true;

/**
 * @member {String} image_url
 */
ArtisticImagePostRequest.prototype['image_url'] = undefined;

/**
 * @member {String} style_url
 */
ArtisticImagePostRequest.prototype['style_url'] = undefined;






export default ArtisticImagePostRequest;

