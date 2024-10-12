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
 * The OperationBatchStatusResponseItem model module.
 * @module model/OperationBatchStatusResponseItem
 * @version 2018-10-15
 */
class OperationBatchStatusResponseItem {
    /**
     * Constructs a new <code>OperationBatchStatusResponseItem</code>.
     * Represents the status of an operation that used the batch API.
     * @alias module:model/OperationBatchStatusResponseItem
     */
    constructor() { 
        
        OperationBatchStatusResponseItem.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OperationBatchStatusResponseItem</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OperationBatchStatusResponseItem} obj Optional instance to populate.
     * @return {module:model/OperationBatchStatusResponseItem} The populated <code>OperationBatchStatusResponseItem</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OperationBatchStatusResponseItem();

            if (data.hasOwnProperty('operationUrl')) {
                obj['operationUrl'] = ApiClient.convertToType(data['operationUrl'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OperationBatchStatusResponseItem</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OperationBatchStatusResponseItem</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['operationUrl'] && !(typeof data['operationUrl'] === 'string' || data['operationUrl'] instanceof String)) {
            throw new Error("Expected the field `operationUrl` to be a primitive type in the JSON string but got " + data['operationUrl']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * status of the long running operation for an environment
 * @member {String} operationUrl
 */
OperationBatchStatusResponseItem.prototype['operationUrl'] = undefined;

/**
 * status of the long running operation for an environment
 * @member {String} status
 */
OperationBatchStatusResponseItem.prototype['status'] = undefined;






export default OperationBatchStatusResponseItem;

