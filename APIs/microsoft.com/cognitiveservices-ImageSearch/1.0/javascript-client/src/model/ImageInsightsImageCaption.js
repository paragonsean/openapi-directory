/**
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Query from './Query';

/**
 * The ImageInsightsImageCaption model module.
 * @module model/ImageInsightsImageCaption
 * @version 1.0
 */
class ImageInsightsImageCaption {
    /**
     * Constructs a new <code>ImageInsightsImageCaption</code>.
     * Defines an image&#39;s caption.
     * @alias module:model/ImageInsightsImageCaption
     * @param caption {String} A caption about the image.
     * @param dataSourceUrl {String} The URL to the website where the caption was found. You must attribute the caption to the source. For example, by displaying the domain name from the URL next to the caption and using the URL to link to the source website.
     * @param relatedSearches {Array.<module:model/Query>} A list of entities found in the caption. Use the contents of the Query object to find the entity in the caption and create a link. The link takes the user to images of the entity.
     */
    constructor(caption, dataSourceUrl, relatedSearches) { 
        
        ImageInsightsImageCaption.initialize(this, caption, dataSourceUrl, relatedSearches);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, caption, dataSourceUrl, relatedSearches) { 
        obj['caption'] = caption;
        obj['dataSourceUrl'] = dataSourceUrl;
        obj['relatedSearches'] = relatedSearches;
    }

    /**
     * Constructs a <code>ImageInsightsImageCaption</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ImageInsightsImageCaption} obj Optional instance to populate.
     * @return {module:model/ImageInsightsImageCaption} The populated <code>ImageInsightsImageCaption</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ImageInsightsImageCaption();

            if (data.hasOwnProperty('caption')) {
                obj['caption'] = ApiClient.convertToType(data['caption'], 'String');
            }
            if (data.hasOwnProperty('dataSourceUrl')) {
                obj['dataSourceUrl'] = ApiClient.convertToType(data['dataSourceUrl'], 'String');
            }
            if (data.hasOwnProperty('relatedSearches')) {
                obj['relatedSearches'] = ApiClient.convertToType(data['relatedSearches'], [Query]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ImageInsightsImageCaption</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageInsightsImageCaption</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ImageInsightsImageCaption.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['caption'] && !(typeof data['caption'] === 'string' || data['caption'] instanceof String)) {
            throw new Error("Expected the field `caption` to be a primitive type in the JSON string but got " + data['caption']);
        }
        // ensure the json data is a string
        if (data['dataSourceUrl'] && !(typeof data['dataSourceUrl'] === 'string' || data['dataSourceUrl'] instanceof String)) {
            throw new Error("Expected the field `dataSourceUrl` to be a primitive type in the JSON string but got " + data['dataSourceUrl']);
        }
        if (data['relatedSearches']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['relatedSearches'])) {
                throw new Error("Expected the field `relatedSearches` to be an array in the JSON data but got " + data['relatedSearches']);
            }
            // validate the optional field `relatedSearches` (array)
            for (const item of data['relatedSearches']) {
                Query.validateJSON(item);
            };
        }

        return true;
    }


}

ImageInsightsImageCaption.RequiredProperties = ["caption", "dataSourceUrl", "relatedSearches"];

/**
 * A caption about the image.
 * @member {String} caption
 */
ImageInsightsImageCaption.prototype['caption'] = undefined;

/**
 * The URL to the website where the caption was found. You must attribute the caption to the source. For example, by displaying the domain name from the URL next to the caption and using the URL to link to the source website.
 * @member {String} dataSourceUrl
 */
ImageInsightsImageCaption.prototype['dataSourceUrl'] = undefined;

/**
 * A list of entities found in the caption. Use the contents of the Query object to find the entity in the caption and create a link. The link takes the user to images of the entity.
 * @member {Array.<module:model/Query>} relatedSearches
 */
ImageInsightsImageCaption.prototype['relatedSearches'] = undefined;






export default ImageInsightsImageCaption;

