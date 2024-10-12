/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage caches.
 *
 * The version of the OpenAPI document: 2019-08-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ResourceSkuCapabilities model module.
 * @module model/ResourceSkuCapabilities
 * @version 2019-08-01-preview
 */
class ResourceSkuCapabilities {
    /**
     * Constructs a new <code>ResourceSkuCapabilities</code>.
     * A resource SKU capability.
     * @alias module:model/ResourceSkuCapabilities
     */
    constructor() { 
        
        ResourceSkuCapabilities.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ResourceSkuCapabilities</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ResourceSkuCapabilities} obj Optional instance to populate.
     * @return {module:model/ResourceSkuCapabilities} The populated <code>ResourceSkuCapabilities</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ResourceSkuCapabilities();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ResourceSkuCapabilities</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ResourceSkuCapabilities</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['value'] && !(typeof data['value'] === 'string' || data['value'] instanceof String)) {
            throw new Error("Expected the field `value` to be a primitive type in the JSON string but got " + data['value']);
        }

        return true;
    }


}



/**
 * Name of a capability, such as ops/sec
 * @member {String} name
 */
ResourceSkuCapabilities.prototype['name'] = undefined;

/**
 * Quantity, if the capability is measured by quantity
 * @member {String} value
 */
ResourceSkuCapabilities.prototype['value'] = undefined;






export default ResourceSkuCapabilities;

