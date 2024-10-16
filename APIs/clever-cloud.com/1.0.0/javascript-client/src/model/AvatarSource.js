/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import URL from './URL';

/**
 * The AvatarSource model module.
 * @module model/AvatarSource
 * @version 1.0.0
 */
class AvatarSource {
    /**
     * Constructs a new <code>AvatarSource</code>.
     * 
     * @alias module:model/AvatarSource
     * @param source {String} github or gravatar
     * @param value {module:model/URL} 
     */
    constructor(source, value) { 
        
        AvatarSource.initialize(this, source, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, source, value) { 
        obj['source'] = source;
        obj['value'] = value;
    }

    /**
     * Constructs a <code>AvatarSource</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AvatarSource} obj Optional instance to populate.
     * @return {module:model/AvatarSource} The populated <code>AvatarSource</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AvatarSource();

            if (data.hasOwnProperty('source')) {
                obj['source'] = ApiClient.convertToType(data['source'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = URL.constructFromObject(data['value']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AvatarSource</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AvatarSource</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AvatarSource.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['source'] && !(typeof data['source'] === 'string' || data['source'] instanceof String)) {
            throw new Error("Expected the field `source` to be a primitive type in the JSON string but got " + data['source']);
        }
        // validate the optional field `value`
        if (data['value']) { // data not null
          URL.validateJSON(data['value']);
        }

        return true;
    }


}

AvatarSource.RequiredProperties = ["source", "value"];

/**
 * github or gravatar
 * @member {String} source
 */
AvatarSource.prototype['source'] = undefined;

/**
 * @member {module:model/URL} value
 */
AvatarSource.prototype['value'] = undefined;






export default AvatarSource;

