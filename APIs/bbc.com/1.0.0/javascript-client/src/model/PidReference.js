/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The PidReference model module.
 * @module model/PidReference
 * @version 1.0.0
 */
class PidReference {
    /**
     * Constructs a new <code>PidReference</code>.
     * @alias module:model/PidReference
     * @param pid {String} 
     * @param resultType {String} 
     */
    constructor(pid, resultType) { 
        
        PidReference.initialize(this, pid, resultType);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, pid, resultType) { 
        obj['pid'] = pid;
        obj['result_type'] = resultType;
    }

    /**
     * Constructs a <code>PidReference</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PidReference} obj Optional instance to populate.
     * @return {module:model/PidReference} The populated <code>PidReference</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PidReference();

            if (data.hasOwnProperty('href')) {
                obj['href'] = ApiClient.convertToType(data['href'], 'String');
            }
            if (data.hasOwnProperty('pid')) {
                obj['pid'] = ApiClient.convertToType(data['pid'], 'String');
            }
            if (data.hasOwnProperty('position')) {
                obj['position'] = ApiClient.convertToType(data['position'], 'Number');
            }
            if (data.hasOwnProperty('result_type')) {
                obj['result_type'] = ApiClient.convertToType(data['result_type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PidReference</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PidReference</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PidReference.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['href'] && !(typeof data['href'] === 'string' || data['href'] instanceof String)) {
            throw new Error("Expected the field `href` to be a primitive type in the JSON string but got " + data['href']);
        }
        // ensure the json data is a string
        if (data['pid'] && !(typeof data['pid'] === 'string' || data['pid'] instanceof String)) {
            throw new Error("Expected the field `pid` to be a primitive type in the JSON string but got " + data['pid']);
        }
        // ensure the json data is a string
        if (data['result_type'] && !(typeof data['result_type'] === 'string' || data['result_type'] instanceof String)) {
            throw new Error("Expected the field `result_type` to be a primitive type in the JSON string but got " + data['result_type']);
        }

        return true;
    }


}

PidReference.RequiredProperties = ["pid", "result_type"];

/**
 * @member {String} href
 */
PidReference.prototype['href'] = undefined;

/**
 * @member {String} pid
 */
PidReference.prototype['pid'] = undefined;

/**
 * @member {Number} position
 */
PidReference.prototype['position'] = undefined;

/**
 * @member {String} result_type
 */
PidReference.prototype['result_type'] = undefined;






export default PidReference;

