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
import ImageGallery from './ImageGallery';

/**
 * The RelatedCollectionsModule model module.
 * @module model/RelatedCollectionsModule
 * @version 1.0
 */
class RelatedCollectionsModule {
    /**
     * Constructs a new <code>RelatedCollectionsModule</code>.
     * Defines a list of webpages that contain related images.
     * @alias module:model/RelatedCollectionsModule
     */
    constructor() { 
        
        RelatedCollectionsModule.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RelatedCollectionsModule</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RelatedCollectionsModule} obj Optional instance to populate.
     * @return {module:model/RelatedCollectionsModule} The populated <code>RelatedCollectionsModule</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RelatedCollectionsModule();

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [ImageGallery]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RelatedCollectionsModule</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RelatedCollectionsModule</code>.
     */
    static validateJSON(data) {
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                ImageGallery.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * A list of webpages that contain related images.
 * @member {Array.<module:model/ImageGallery>} value
 */
RelatedCollectionsModule.prototype['value'] = undefined;






export default RelatedCollectionsModule;

