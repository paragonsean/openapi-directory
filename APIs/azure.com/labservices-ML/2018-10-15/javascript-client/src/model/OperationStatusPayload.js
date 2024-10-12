/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The OperationStatusPayload model module.
 * @module model/OperationStatusPayload
 * @version 2018-10-15
 */
class OperationStatusPayload {
    /**
     * Constructs a new <code>OperationStatusPayload</code>.
     * Payload to get the status of an operation
     * @alias module:model/OperationStatusPayload
     * @param operationUrl {String} The operation url of long running operation
     */
    constructor(operationUrl) { 
        
        OperationStatusPayload.initialize(this, operationUrl);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, operationUrl) { 
        obj['operationUrl'] = operationUrl;
    }

    /**
     * Constructs a <code>OperationStatusPayload</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OperationStatusPayload} obj Optional instance to populate.
     * @return {module:model/OperationStatusPayload} The populated <code>OperationStatusPayload</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OperationStatusPayload();

            if (data.hasOwnProperty('operationUrl')) {
                obj['operationUrl'] = ApiClient.convertToType(data['operationUrl'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OperationStatusPayload</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OperationStatusPayload</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OperationStatusPayload.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['operationUrl'] && !(typeof data['operationUrl'] === 'string' || data['operationUrl'] instanceof String)) {
            throw new Error("Expected the field `operationUrl` to be a primitive type in the JSON string but got " + data['operationUrl']);
        }

        return true;
    }


}

OperationStatusPayload.RequiredProperties = ["operationUrl"];

/**
 * The operation url of long running operation
 * @member {String} operationUrl
 */
OperationStatusPayload.prototype['operationUrl'] = undefined;






export default OperationStatusPayload;

