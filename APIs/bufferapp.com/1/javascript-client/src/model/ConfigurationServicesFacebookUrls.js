/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ConfigurationServicesFacebookUrls model module.
 * @module model/ConfigurationServicesFacebookUrls
 * @version 1
 */
class ConfigurationServicesFacebookUrls {
    /**
     * Constructs a new <code>ConfigurationServicesFacebookUrls</code>.
     * @alias module:model/ConfigurationServicesFacebookUrls
     */
    constructor() { 
        
        ConfigurationServicesFacebookUrls.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ConfigurationServicesFacebookUrls</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ConfigurationServicesFacebookUrls} obj Optional instance to populate.
     * @return {module:model/ConfigurationServicesFacebookUrls} The populated <code>ConfigurationServicesFacebookUrls</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ConfigurationServicesFacebookUrls();

            if (data.hasOwnProperty('user')) {
                obj['user'] = ApiClient.convertToType(data['user'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ConfigurationServicesFacebookUrls</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ConfigurationServicesFacebookUrls</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['user'] && !(typeof data['user'] === 'string' || data['user'] instanceof String)) {
            throw new Error("Expected the field `user` to be a primitive type in the JSON string but got " + data['user']);
        }

        return true;
    }


}



/**
 * @member {String} user
 */
ConfigurationServicesFacebookUrls.prototype['user'] = undefined;






export default ConfigurationServicesFacebookUrls;

