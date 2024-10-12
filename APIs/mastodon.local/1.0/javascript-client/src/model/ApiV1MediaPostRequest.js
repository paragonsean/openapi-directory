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
 * The ApiV1MediaPostRequest model module.
 * @module model/ApiV1MediaPostRequest
 * @version 1.0
 */
class ApiV1MediaPostRequest {
    /**
     * Constructs a new <code>ApiV1MediaPostRequest</code>.
     * @alias module:model/ApiV1MediaPostRequest
     * @param file {File} The file to be attached, using multipart form data.
     */
    constructor(file) { 
        
        ApiV1MediaPostRequest.initialize(this, file);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, file) { 
        obj['file'] = file;
    }

    /**
     * Constructs a <code>ApiV1MediaPostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiV1MediaPostRequest} obj Optional instance to populate.
     * @return {module:model/ApiV1MediaPostRequest} The populated <code>ApiV1MediaPostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiV1MediaPostRequest();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('file')) {
                obj['file'] = ApiClient.convertToType(data['file'], File);
            }
            if (data.hasOwnProperty('focus')) {
                obj['focus'] = ApiClient.convertToType(data['focus'], 'String');
            }
            if (data.hasOwnProperty('thumbnail')) {
                obj['thumbnail'] = ApiClient.convertToType(data['thumbnail'], File);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiV1MediaPostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiV1MediaPostRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ApiV1MediaPostRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['focus'] && !(typeof data['focus'] === 'string' || data['focus'] instanceof String)) {
            throw new Error("Expected the field `focus` to be a primitive type in the JSON string but got " + data['focus']);
        }

        return true;
    }


}

ApiV1MediaPostRequest.RequiredProperties = ["file"];

/**
 * A plain-text description of the media, for accessibility purposes.
 * @member {String} description
 */
ApiV1MediaPostRequest.prototype['description'] = undefined;

/**
 * The file to be attached, using multipart form data.
 * @member {File} file
 */
ApiV1MediaPostRequest.prototype['file'] = undefined;

/**
 * Two floating points (x,y), comma-delimited, ranging from -1.0 to 1.0 (see “Focal points” below)
 * @member {String} focus
 */
ApiV1MediaPostRequest.prototype['focus'] = undefined;

/**
 * The custom thumbnail of the media to be attached, using multipart form data.
 * @member {File} thumbnail
 */
ApiV1MediaPostRequest.prototype['thumbnail'] = undefined;






export default ApiV1MediaPostRequest;

