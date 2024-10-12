/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The HSAlgoSettings model module.
 * @module model/HSAlgoSettings
 * @version 1.5.0-dev
 */
class HSAlgoSettings {
    /**
     * Constructs a new <code>HSAlgoSettings</code>.
     * Settings for an HMAC + SHA signing algorithm
     * @alias module:model/HSAlgoSettings
     * @param secret {String} The secret value for the HMAC function
     * @param size {Number} Size for SHA function. can be 256, 384 or 512
     * @param type {String} String with value HSAlgoSettings
     */
    constructor(secret, size, type) { 
        
        HSAlgoSettings.initialize(this, secret, size, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, secret, size, type) { 
        obj['secret'] = secret;
        obj['size'] = size;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>HSAlgoSettings</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HSAlgoSettings} obj Optional instance to populate.
     * @return {module:model/HSAlgoSettings} The populated <code>HSAlgoSettings</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HSAlgoSettings();

            if (data.hasOwnProperty('secret')) {
                obj['secret'] = ApiClient.convertToType(data['secret'], 'String');
            }
            if (data.hasOwnProperty('size')) {
                obj['size'] = ApiClient.convertToType(data['size'], 'Number');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HSAlgoSettings</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HSAlgoSettings</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HSAlgoSettings.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['secret'] && !(typeof data['secret'] === 'string' || data['secret'] instanceof String)) {
            throw new Error("Expected the field `secret` to be a primitive type in the JSON string but got " + data['secret']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

HSAlgoSettings.RequiredProperties = ["secret", "size", "type"];

/**
 * The secret value for the HMAC function
 * @member {String} secret
 */
HSAlgoSettings.prototype['secret'] = undefined;

/**
 * Size for SHA function. can be 256, 384 or 512
 * @member {Number} size
 */
HSAlgoSettings.prototype['size'] = undefined;

/**
 * String with value HSAlgoSettings
 * @member {String} type
 */
HSAlgoSettings.prototype['type'] = undefined;






export default HSAlgoSettings;

