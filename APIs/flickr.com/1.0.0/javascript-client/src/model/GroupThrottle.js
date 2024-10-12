/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
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

/**
 * The GroupThrottle model module.
 * @module model/GroupThrottle
 * @version 1.0.0
 */
class GroupThrottle {
    /**
     * Constructs a new <code>GroupThrottle</code>.
     * @alias module:model/GroupThrottle
     */
    constructor() { 
        
        GroupThrottle.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GroupThrottle</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GroupThrottle} obj Optional instance to populate.
     * @return {module:model/GroupThrottle} The populated <code>GroupThrottle</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GroupThrottle();

            if (data.hasOwnProperty('count')) {
                obj['count'] = ApiClient.convertToType(data['count'], 'Number');
            }
            if (data.hasOwnProperty('mode')) {
                obj['mode'] = ApiClient.convertToType(data['mode'], 'String');
            }
            if (data.hasOwnProperty('remaining')) {
                obj['remaining'] = ApiClient.convertToType(data['remaining'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GroupThrottle</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GroupThrottle</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['mode'] && !(typeof data['mode'] === 'string' || data['mode'] instanceof String)) {
            throw new Error("Expected the field `mode` to be a primitive type in the JSON string but got " + data['mode']);
        }
        // ensure the json data is a string
        if (data['remaining'] && !(typeof data['remaining'] === 'string' || data['remaining'] instanceof String)) {
            throw new Error("Expected the field `remaining` to be a primitive type in the JSON string but got " + data['remaining']);
        }

        return true;
    }


}



/**
 * @member {Number} count
 */
GroupThrottle.prototype['count'] = undefined;

/**
 * @member {String} mode
 */
GroupThrottle.prototype['mode'] = undefined;

/**
 * @member {String} remaining
 */
GroupThrottle.prototype['remaining'] = undefined;






export default GroupThrottle;

