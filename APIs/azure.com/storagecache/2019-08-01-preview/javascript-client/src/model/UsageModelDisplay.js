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
 * The UsageModelDisplay model module.
 * @module model/UsageModelDisplay
 * @version 2019-08-01-preview
 */
class UsageModelDisplay {
    /**
     * Constructs a new <code>UsageModelDisplay</code>.
     * Localized information describing this usage model.
     * @alias module:model/UsageModelDisplay
     */
    constructor() { 
        
        UsageModelDisplay.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UsageModelDisplay</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UsageModelDisplay} obj Optional instance to populate.
     * @return {module:model/UsageModelDisplay} The populated <code>UsageModelDisplay</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UsageModelDisplay();

            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UsageModelDisplay</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UsageModelDisplay</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }

        return true;
    }


}



/**
 * String to display for this usage model.
 * @member {String} description
 */
UsageModelDisplay.prototype['description'] = undefined;






export default UsageModelDisplay;

