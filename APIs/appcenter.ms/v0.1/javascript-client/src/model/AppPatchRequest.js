/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AppPatchRequest model module.
 * @module model/AppPatchRequest
 * @version v0.1
 */
class AppPatchRequest {
    /**
     * Constructs a new <code>AppPatchRequest</code>.
     * @alias module:model/AppPatchRequest
     */
    constructor() { 
        
        AppPatchRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppPatchRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppPatchRequest} obj Optional instance to populate.
     * @return {module:model/AppPatchRequest} The populated <code>AppPatchRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppPatchRequest();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
            if (data.hasOwnProperty('icon_asset_id')) {
                obj['icon_asset_id'] = ApiClient.convertToType(data['icon_asset_id'], 'String');
            }
            if (data.hasOwnProperty('icon_url')) {
                obj['icon_url'] = ApiClient.convertToType(data['icon_url'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('release_type')) {
                obj['release_type'] = ApiClient.convertToType(data['release_type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppPatchRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppPatchRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['display_name'] && !(typeof data['display_name'] === 'string' || data['display_name'] instanceof String)) {
            throw new Error("Expected the field `display_name` to be a primitive type in the JSON string but got " + data['display_name']);
        }
        // ensure the json data is a string
        if (data['icon_asset_id'] && !(typeof data['icon_asset_id'] === 'string' || data['icon_asset_id'] instanceof String)) {
            throw new Error("Expected the field `icon_asset_id` to be a primitive type in the JSON string but got " + data['icon_asset_id']);
        }
        // ensure the json data is a string
        if (data['icon_url'] && !(typeof data['icon_url'] === 'string' || data['icon_url'] instanceof String)) {
            throw new Error("Expected the field `icon_url` to be a primitive type in the JSON string but got " + data['icon_url']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['release_type'] && !(typeof data['release_type'] === 'string' || data['release_type'] instanceof String)) {
            throw new Error("Expected the field `release_type` to be a primitive type in the JSON string but got " + data['release_type']);
        }

        return true;
    }


}



/**
 * A short text describing the app
 * @member {String} description
 */
AppPatchRequest.prototype['description'] = undefined;

/**
 * The display name of the app
 * @member {String} display_name
 */
AppPatchRequest.prototype['display_name'] = undefined;

/**
 * The uuid for the icon's asset id from ACFUS
 * @member {String} icon_asset_id
 */
AppPatchRequest.prototype['icon_asset_id'] = undefined;

/**
 * The string representation of the URL pointing to the app's icon
 * @member {String} icon_url
 */
AppPatchRequest.prototype['icon_url'] = undefined;

/**
 * The name of the app used in URLs
 * @member {String} name
 */
AppPatchRequest.prototype['name'] = undefined;

/**
 * A one-word descriptive release type value that starts with a capital letter but is otherwise lowercase
 * @member {String} release_type
 */
AppPatchRequest.prototype['release_type'] = undefined;






export default AppPatchRequest;

