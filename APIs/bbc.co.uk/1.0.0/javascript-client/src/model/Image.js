/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
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
 * The Image model module.
 * @module model/Image
 * @version 1.0.0
 */
class Image {
    /**
     * Constructs a new <code>Image</code>.
     * @alias module:model/Image
     * @param id {String} 
     * @param imageType {String} 
     * @param templateUrl {String} 
     * @param type {String} 
     */
    constructor(id, imageType, templateUrl, type) { 
        
        Image.initialize(this, id, imageType, templateUrl, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, imageType, templateUrl, type) { 
        obj['id'] = id;
        obj['image_type'] = imageType;
        obj['template_url'] = templateUrl;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>Image</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Image} obj Optional instance to populate.
     * @return {module:model/Image} The populated <code>Image</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Image();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('image_type')) {
                obj['image_type'] = ApiClient.convertToType(data['image_type'], 'String');
            }
            if (data.hasOwnProperty('template_url')) {
                obj['template_url'] = ApiClient.convertToType(data['template_url'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Image</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Image</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Image.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['image_type'] && !(typeof data['image_type'] === 'string' || data['image_type'] instanceof String)) {
            throw new Error("Expected the field `image_type` to be a primitive type in the JSON string but got " + data['image_type']);
        }
        // ensure the json data is a string
        if (data['template_url'] && !(typeof data['template_url'] === 'string' || data['template_url'] instanceof String)) {
            throw new Error("Expected the field `template_url` to be a primitive type in the JSON string but got " + data['template_url']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

Image.RequiredProperties = ["id", "image_type", "template_url", "type"];

/**
 * @member {String} id
 */
Image.prototype['id'] = undefined;

/**
 * @member {String} image_type
 */
Image.prototype['image_type'] = undefined;

/**
 * @member {String} template_url
 */
Image.prototype['template_url'] = undefined;

/**
 * @member {String} type
 */
Image.prototype['type'] = undefined;






export default Image;

