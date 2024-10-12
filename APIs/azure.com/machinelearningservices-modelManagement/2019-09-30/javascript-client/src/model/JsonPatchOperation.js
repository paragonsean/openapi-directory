/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The JsonPatchOperation model module.
 * @module model/JsonPatchOperation
 * @version 2019-09-30
 */
class JsonPatchOperation {
    /**
     * Constructs a new <code>JsonPatchOperation</code>.
     * The Json Patch definition.
     * @alias module:model/JsonPatchOperation
     */
    constructor() { 
        
        JsonPatchOperation.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>JsonPatchOperation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/JsonPatchOperation} obj Optional instance to populate.
     * @return {module:model/JsonPatchOperation} The populated <code>JsonPatchOperation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new JsonPatchOperation();

            if (data.hasOwnProperty('from')) {
                obj['from'] = ApiClient.convertToType(data['from'], 'String');
            }
            if (data.hasOwnProperty('op')) {
                obj['op'] = ApiClient.convertToType(data['op'], 'String');
            }
            if (data.hasOwnProperty('path')) {
                obj['path'] = ApiClient.convertToType(data['path'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>JsonPatchOperation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>JsonPatchOperation</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['from'] && !(typeof data['from'] === 'string' || data['from'] instanceof String)) {
            throw new Error("Expected the field `from` to be a primitive type in the JSON string but got " + data['from']);
        }
        // ensure the json data is a string
        if (data['op'] && !(typeof data['op'] === 'string' || data['op'] instanceof String)) {
            throw new Error("Expected the field `op` to be a primitive type in the JSON string but got " + data['op']);
        }
        // ensure the json data is a string
        if (data['path'] && !(typeof data['path'] === 'string' || data['path'] instanceof String)) {
            throw new Error("Expected the field `path` to be a primitive type in the JSON string but got " + data['path']);
        }

        return true;
    }


}



/**
 * The source location.
 * @member {String} from
 */
JsonPatchOperation.prototype['from'] = undefined;

/**
 * The operation.
 * @member {String} op
 */
JsonPatchOperation.prototype['op'] = undefined;

/**
 * The target location.
 * @member {String} path
 */
JsonPatchOperation.prototype['path'] = undefined;

/**
 * The value.
 * @member {Object} value
 */
JsonPatchOperation.prototype['value'] = undefined;






export default JsonPatchOperation;

