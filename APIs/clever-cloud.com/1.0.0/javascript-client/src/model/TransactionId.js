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

/**
 * The TransactionId model module.
 * @module model/TransactionId
 * @version 1.0.0
 */
class TransactionId {
    /**
     * Constructs a new <code>TransactionId</code>.
     * A simple transaction id
     * @alias module:model/TransactionId
     * @param transactionId {String} The transaction Id
     */
    constructor(transactionId) { 
        
        TransactionId.initialize(this, transactionId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, transactionId) { 
        obj['transactionId'] = transactionId;
    }

    /**
     * Constructs a <code>TransactionId</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TransactionId} obj Optional instance to populate.
     * @return {module:model/TransactionId} The populated <code>TransactionId</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TransactionId();

            if (data.hasOwnProperty('transactionId')) {
                obj['transactionId'] = ApiClient.convertToType(data['transactionId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TransactionId</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TransactionId</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TransactionId.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['transactionId'] && !(typeof data['transactionId'] === 'string' || data['transactionId'] instanceof String)) {
            throw new Error("Expected the field `transactionId` to be a primitive type in the JSON string but got " + data['transactionId']);
        }

        return true;
    }


}

TransactionId.RequiredProperties = ["transactionId"];

/**
 * The transaction Id
 * @member {String} transactionId
 */
TransactionId.prototype['transactionId'] = undefined;






export default TransactionId;

