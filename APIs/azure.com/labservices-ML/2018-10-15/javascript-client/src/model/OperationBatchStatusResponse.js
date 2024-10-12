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
import OperationBatchStatusResponseItem from './OperationBatchStatusResponseItem';

/**
 * The OperationBatchStatusResponse model module.
 * @module model/OperationBatchStatusResponse
 * @version 2018-10-15
 */
class OperationBatchStatusResponse {
    /**
     * Constructs a new <code>OperationBatchStatusResponse</code>.
     * Status Details of the long running operation for an environment
     * @alias module:model/OperationBatchStatusResponse
     */
    constructor() { 
        
        OperationBatchStatusResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OperationBatchStatusResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OperationBatchStatusResponse} obj Optional instance to populate.
     * @return {module:model/OperationBatchStatusResponse} The populated <code>OperationBatchStatusResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OperationBatchStatusResponse();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [OperationBatchStatusResponseItem]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OperationBatchStatusResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OperationBatchStatusResponse</code>.
     */
    static validateJSON(data) {
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                OperationBatchStatusResponseItem.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Gets a collection of items that contain the operation url and status.
 * @member {Array.<module:model/OperationBatchStatusResponseItem>} items
 */
OperationBatchStatusResponse.prototype['items'] = undefined;






export default OperationBatchStatusResponse;

