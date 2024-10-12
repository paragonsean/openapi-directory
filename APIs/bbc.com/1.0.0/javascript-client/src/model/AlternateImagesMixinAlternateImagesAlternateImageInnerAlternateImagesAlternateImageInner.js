/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner model module.
 * @module model/AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner
 * @version 1.0.0
 */
class AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner {
    /**
     * Constructs a new <code>AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner</code>.
     * @alias module:model/AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner
     * @param templateUrl {String} 
     */
    constructor(templateUrl) { 
        
        AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner.initialize(this, templateUrl);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, templateUrl) { 
        obj['template_url'] = templateUrl;
    }

    /**
     * Constructs a <code>AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner} obj Optional instance to populate.
     * @return {module:model/AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner} The populated <code>AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner();

            if (data.hasOwnProperty('href')) {
                obj['href'] = ApiClient.convertToType(data['href'], 'String');
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
     * Validates the JSON data with respect to <code>AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['href'] && !(typeof data['href'] === 'string' || data['href'] instanceof String)) {
            throw new Error("Expected the field `href` to be a primitive type in the JSON string but got " + data['href']);
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

AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner.RequiredProperties = ["template_url"];

/**
 * @member {String} href
 */
AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner.prototype['href'] = undefined;

/**
 * @member {String} template_url
 */
AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner.prototype['template_url'] = undefined;

/**
 * @member {String} type
 */
AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner.prototype['type'] = undefined;






export default AlternateImagesMixinAlternateImagesAlternateImageInnerAlternateImagesAlternateImageInner;

