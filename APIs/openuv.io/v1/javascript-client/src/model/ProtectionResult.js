/**
 * OpenUV - Global Real-Time UV Index Forecast API
 * The missing minimalistic JSON real-time UV Index API for awesome Developers, Innovators and Smart Home Enthusiasts
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ProtectionResult model module.
 * @module model/ProtectionResult
 * @version v1
 */
class ProtectionResult {
    /**
     * Constructs a new <code>ProtectionResult</code>.
     * @alias module:model/ProtectionResult
     * @param ozone {Number} 
     * @param ozoneTime {String} 
     * @param uv {Number} 
     * @param uvMax {Number} 
     * @param uvMaxTime {String} 
     * @param uvTime {String} 
     */
    constructor(ozone, ozoneTime, uv, uvMax, uvMaxTime, uvTime) { 
        
        ProtectionResult.initialize(this, ozone, ozoneTime, uv, uvMax, uvMaxTime, uvTime);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, ozone, ozoneTime, uv, uvMax, uvMaxTime, uvTime) { 
        obj['ozone'] = ozone;
        obj['ozone_time'] = ozoneTime;
        obj['uv'] = uv;
        obj['uv_max'] = uvMax;
        obj['uv_max_time'] = uvMaxTime;
        obj['uv_time'] = uvTime;
    }

    /**
     * Constructs a <code>ProtectionResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProtectionResult} obj Optional instance to populate.
     * @return {module:model/ProtectionResult} The populated <code>ProtectionResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProtectionResult();

            if (data.hasOwnProperty('ozone')) {
                obj['ozone'] = ApiClient.convertToType(data['ozone'], 'Number');
            }
            if (data.hasOwnProperty('ozone_time')) {
                obj['ozone_time'] = ApiClient.convertToType(data['ozone_time'], 'String');
            }
            if (data.hasOwnProperty('uv')) {
                obj['uv'] = ApiClient.convertToType(data['uv'], 'Number');
            }
            if (data.hasOwnProperty('uv_max')) {
                obj['uv_max'] = ApiClient.convertToType(data['uv_max'], 'Number');
            }
            if (data.hasOwnProperty('uv_max_time')) {
                obj['uv_max_time'] = ApiClient.convertToType(data['uv_max_time'], 'String');
            }
            if (data.hasOwnProperty('uv_time')) {
                obj['uv_time'] = ApiClient.convertToType(data['uv_time'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProtectionResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProtectionResult</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ProtectionResult.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['ozone_time'] && !(typeof data['ozone_time'] === 'string' || data['ozone_time'] instanceof String)) {
            throw new Error("Expected the field `ozone_time` to be a primitive type in the JSON string but got " + data['ozone_time']);
        }
        // ensure the json data is a string
        if (data['uv_max_time'] && !(typeof data['uv_max_time'] === 'string' || data['uv_max_time'] instanceof String)) {
            throw new Error("Expected the field `uv_max_time` to be a primitive type in the JSON string but got " + data['uv_max_time']);
        }
        // ensure the json data is a string
        if (data['uv_time'] && !(typeof data['uv_time'] === 'string' || data['uv_time'] instanceof String)) {
            throw new Error("Expected the field `uv_time` to be a primitive type in the JSON string but got " + data['uv_time']);
        }

        return true;
    }


}

ProtectionResult.RequiredProperties = ["ozone", "ozone_time", "uv", "uv_max", "uv_max_time", "uv_time"];

/**
 * @member {Number} ozone
 */
ProtectionResult.prototype['ozone'] = undefined;

/**
 * @member {String} ozone_time
 */
ProtectionResult.prototype['ozone_time'] = undefined;

/**
 * @member {Number} uv
 */
ProtectionResult.prototype['uv'] = undefined;

/**
 * @member {Number} uv_max
 */
ProtectionResult.prototype['uv_max'] = undefined;

/**
 * @member {String} uv_max_time
 */
ProtectionResult.prototype['uv_max_time'] = undefined;

/**
 * @member {String} uv_time
 */
ProtectionResult.prototype['uv_time'] = undefined;






export default ProtectionResult;

