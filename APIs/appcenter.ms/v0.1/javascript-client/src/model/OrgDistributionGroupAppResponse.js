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
import AppsList200ResponseInnerAllOfOwner from './AppsList200ResponseInnerAllOfOwner';

/**
 * The OrgDistributionGroupAppResponse model module.
 * @module model/OrgDistributionGroupAppResponse
 * @version v0.1
 */
class OrgDistributionGroupAppResponse {
    /**
     * Constructs a new <code>OrgDistributionGroupAppResponse</code>.
     * @alias module:model/OrgDistributionGroupAppResponse
     * @param displayName {String} The display name of the app
     * @param id {String} The unique ID (UUID) of the app
     * @param name {String} The name of the app used in URLs
     * @param os {module:model/OrgDistributionGroupAppResponse.OsEnum} The OS the app will be running on
     * @param owner {module:model/AppsList200ResponseInnerAllOfOwner} 
     */
    constructor(displayName, id, name, os, owner) { 
        
        OrgDistributionGroupAppResponse.initialize(this, displayName, id, name, os, owner);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, displayName, id, name, os, owner) { 
        obj['display_name'] = displayName;
        obj['id'] = id;
        obj['name'] = name;
        obj['os'] = os;
        obj['owner'] = owner;
    }

    /**
     * Constructs a <code>OrgDistributionGroupAppResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrgDistributionGroupAppResponse} obj Optional instance to populate.
     * @return {module:model/OrgDistributionGroupAppResponse} The populated <code>OrgDistributionGroupAppResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrgDistributionGroupAppResponse();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
            if (data.hasOwnProperty('icon_source')) {
                obj['icon_source'] = ApiClient.convertToType(data['icon_source'], 'String');
            }
            if (data.hasOwnProperty('icon_url')) {
                obj['icon_url'] = ApiClient.convertToType(data['icon_url'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('os')) {
                obj['os'] = ApiClient.convertToType(data['os'], 'String');
            }
            if (data.hasOwnProperty('owner')) {
                obj['owner'] = AppsList200ResponseInnerAllOfOwner.constructFromObject(data['owner']);
            }
            if (data.hasOwnProperty('release_type')) {
                obj['release_type'] = ApiClient.convertToType(data['release_type'], 'String');
            }
            if (data.hasOwnProperty('origin')) {
                obj['origin'] = ApiClient.convertToType(data['origin'], 'String');
            }
            if (data.hasOwnProperty('platform')) {
                obj['platform'] = ApiClient.convertToType(data['platform'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrgDistributionGroupAppResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrgDistributionGroupAppResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OrgDistributionGroupAppResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['display_name'] && !(typeof data['display_name'] === 'string' || data['display_name'] instanceof String)) {
            throw new Error("Expected the field `display_name` to be a primitive type in the JSON string but got " + data['display_name']);
        }
        // ensure the json data is a string
        if (data['icon_source'] && !(typeof data['icon_source'] === 'string' || data['icon_source'] instanceof String)) {
            throw new Error("Expected the field `icon_source` to be a primitive type in the JSON string but got " + data['icon_source']);
        }
        // ensure the json data is a string
        if (data['icon_url'] && !(typeof data['icon_url'] === 'string' || data['icon_url'] instanceof String)) {
            throw new Error("Expected the field `icon_url` to be a primitive type in the JSON string but got " + data['icon_url']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['os'] && !(typeof data['os'] === 'string' || data['os'] instanceof String)) {
            throw new Error("Expected the field `os` to be a primitive type in the JSON string but got " + data['os']);
        }
        // validate the optional field `owner`
        if (data['owner']) { // data not null
          AppsList200ResponseInnerAllOfOwner.validateJSON(data['owner']);
        }
        // ensure the json data is a string
        if (data['release_type'] && !(typeof data['release_type'] === 'string' || data['release_type'] instanceof String)) {
            throw new Error("Expected the field `release_type` to be a primitive type in the JSON string but got " + data['release_type']);
        }
        // ensure the json data is a string
        if (data['origin'] && !(typeof data['origin'] === 'string' || data['origin'] instanceof String)) {
            throw new Error("Expected the field `origin` to be a primitive type in the JSON string but got " + data['origin']);
        }
        // ensure the json data is a string
        if (data['platform'] && !(typeof data['platform'] === 'string' || data['platform'] instanceof String)) {
            throw new Error("Expected the field `platform` to be a primitive type in the JSON string but got " + data['platform']);
        }

        return true;
    }


}

OrgDistributionGroupAppResponse.RequiredProperties = ["display_name", "id", "name", "os", "owner"];

/**
 * The description of the app
 * @member {String} description
 */
OrgDistributionGroupAppResponse.prototype['description'] = undefined;

/**
 * The display name of the app
 * @member {String} display_name
 */
OrgDistributionGroupAppResponse.prototype['display_name'] = undefined;

/**
 * The string representation of the source of the app's icon
 * @member {String} icon_source
 */
OrgDistributionGroupAppResponse.prototype['icon_source'] = undefined;

/**
 * The string representation of the URL pointing to the app's icon
 * @member {String} icon_url
 */
OrgDistributionGroupAppResponse.prototype['icon_url'] = undefined;

/**
 * The unique ID (UUID) of the app
 * @member {String} id
 */
OrgDistributionGroupAppResponse.prototype['id'] = undefined;

/**
 * The name of the app used in URLs
 * @member {String} name
 */
OrgDistributionGroupAppResponse.prototype['name'] = undefined;

/**
 * The OS the app will be running on
 * @member {module:model/OrgDistributionGroupAppResponse.OsEnum} os
 */
OrgDistributionGroupAppResponse.prototype['os'] = undefined;

/**
 * @member {module:model/AppsList200ResponseInnerAllOfOwner} owner
 */
OrgDistributionGroupAppResponse.prototype['owner'] = undefined;

/**
 * A one-word descriptive release-type value that starts with a capital letter but is otherwise lowercase
 * @member {String} release_type
 */
OrgDistributionGroupAppResponse.prototype['release_type'] = undefined;

/**
 * The creation origin of this app
 * @member {String} origin
 */
OrgDistributionGroupAppResponse.prototype['origin'] = undefined;

/**
 * The platform of the app
 * @member {String} platform
 */
OrgDistributionGroupAppResponse.prototype['platform'] = undefined;





/**
 * Allowed values for the <code>os</code> property.
 * @enum {String}
 * @readonly
 */
OrgDistributionGroupAppResponse['OsEnum'] = {

    /**
     * value: "Android"
     * @const
     */
    "Android": "Android",

    /**
     * value: "iOS"
     * @const
     */
    "iOS": "iOS",

    /**
     * value: "macOS"
     * @const
     */
    "macOS": "macOS",

    /**
     * value: "Tizen"
     * @const
     */
    "Tizen": "Tizen",

    /**
     * value: "tvOS"
     * @const
     */
    "tvOS": "tvOS",

    /**
     * value: "Windows"
     * @const
     */
    "Windows": "Windows",

    /**
     * value: "Linux"
     * @const
     */
    "Linux": "Linux",

    /**
     * value: "Custom"
     * @const
     */
    "Custom": "Custom"
};



export default OrgDistributionGroupAppResponse;

