/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ApiV1FeaturedTagsPostRequest model module.
 * @module model/ApiV1FeaturedTagsPostRequest
 * @version 1.0
 */
class ApiV1FeaturedTagsPostRequest {
    /**
     * Constructs a new <code>ApiV1FeaturedTagsPostRequest</code>.
     * @alias module:model/ApiV1FeaturedTagsPostRequest
     */
    constructor() { 
        
        ApiV1FeaturedTagsPostRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiV1FeaturedTagsPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiV1FeaturedTagsPostRequest} obj Optional instance to populate.
     * @return {module:model/ApiV1FeaturedTagsPostRequest} The populated <code>ApiV1FeaturedTagsPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiV1FeaturedTagsPostRequest();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiV1FeaturedTagsPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiV1FeaturedTagsPostRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * @member {String} name
 */
ApiV1FeaturedTagsPostRequest.prototype['name'] = undefined;






export default ApiV1FeaturedTagsPostRequest;

