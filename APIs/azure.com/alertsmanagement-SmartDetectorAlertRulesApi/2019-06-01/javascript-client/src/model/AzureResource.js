/**
 * Azure Alerts Management Service Resource Provider
 * APIs for Azure Smart Detector Alert Rules CRUD operations.
 *
 * The version of the OpenAPI document: 2019-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AzureResource model module.
 * @module model/AzureResource
 * @version 2019-06-01
 */
class AzureResource {
    /**
     * Constructs a new <code>AzureResource</code>.
     * An Azure resource object
     * @alias module:model/AzureResource
     */
    constructor() { 
        
        AzureResource.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['location'] = 'global';
    }

    /**
     * Constructs a <code>AzureResource</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AzureResource} obj Optional instance to populate.
     * @return {module:model/AzureResource} The populated <code>AzureResource</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AzureResource();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('location')) {
                obj['location'] = ApiClient.convertToType(data['location'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], Object);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AzureResource</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AzureResource</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['location'] && !(typeof data['location'] === 'string' || data['location'] instanceof String)) {
            throw new Error("Expected the field `location` to be a primitive type in the JSON string but got " + data['location']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * The resource ID.
 * @member {String} id
 */
AzureResource.prototype['id'] = undefined;

/**
 * The resource location.
 * @member {String} location
 * @default 'global'
 */
AzureResource.prototype['location'] = 'global';

/**
 * The resource name.
 * @member {String} name
 */
AzureResource.prototype['name'] = undefined;

/**
 * The resource tags.
 * @member {Object} tags
 */
AzureResource.prototype['tags'] = undefined;

/**
 * The resource type.
 * @member {String} type
 */
AzureResource.prototype['type'] = undefined;






export default AzureResource;

