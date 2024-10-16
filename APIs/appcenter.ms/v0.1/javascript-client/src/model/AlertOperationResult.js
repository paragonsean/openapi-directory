/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AlertOperationResult model module.
 * @module model/AlertOperationResult
 * @version v0.1
 */
class AlertOperationResult {
    /**
     * Constructs a new <code>AlertOperationResult</code>.
     * Generic result for any alerting API operation
     * @alias module:model/AlertOperationResult
     * @param requestId {String} Unique request identifier for tracking
     */
    constructor(requestId) { 
        
        AlertOperationResult.initialize(this, requestId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, requestId) { 
        obj['request_id'] = requestId;
    }

    /**
     * Constructs a <code>AlertOperationResult</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AlertOperationResult} obj Optional instance to populate.
     * @return {module:model/AlertOperationResult} The populated <code>AlertOperationResult</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AlertOperationResult();

            if (data.hasOwnProperty('request_id')) {
                obj['request_id'] = ApiClient.convertToType(data['request_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AlertOperationResult</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AlertOperationResult</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AlertOperationResult.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['request_id'] && !(typeof data['request_id'] === 'string' || data['request_id'] instanceof String)) {
            throw new Error("Expected the field `request_id` to be a primitive type in the JSON string but got " + data['request_id']);
        }

        return true;
    }


}

AlertOperationResult.RequiredProperties = ["request_id"];

/**
 * Unique request identifier for tracking
 * @member {String} request_id
 */
AlertOperationResult.prototype['request_id'] = undefined;






export default AlertOperationResult;

