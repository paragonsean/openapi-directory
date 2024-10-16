/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The IncomingTransaction model module.
 * @module model/IncomingTransaction
 * @version 2.0
 */
class IncomingTransaction {
    /**
     * Constructs a new <code>IncomingTransaction</code>.
     * @alias module:model/IncomingTransaction
     */
    constructor() { 
        
        IncomingTransaction.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IncomingTransaction</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IncomingTransaction} obj Optional instance to populate.
     * @return {module:model/IncomingTransaction} The populated <code>IncomingTransaction</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IncomingTransaction();

            if (data.hasOwnProperty('boxId')) {
                obj['boxId'] = ApiClient.convertToType(data['boxId'], 'Number');
            }
            if (data.hasOwnProperty('boxName')) {
                obj['boxName'] = ApiClient.convertToType(data['boxName'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('outgoingTransactionId')) {
                obj['outgoingTransactionId'] = ApiClient.convertToType(data['outgoingTransactionId'], 'Number');
            }
            if (data.hasOwnProperty('receivedImageCount')) {
                obj['receivedImageCount'] = ApiClient.convertToType(data['receivedImageCount'], 'Number');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('totalImageCount')) {
                obj['totalImageCount'] = ApiClient.convertToType(data['totalImageCount'], 'Number');
            }
            if (data.hasOwnProperty('updated')) {
                obj['updated'] = ApiClient.convertToType(data['updated'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IncomingTransaction</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IncomingTransaction</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['boxName'] && !(typeof data['boxName'] === 'string' || data['boxName'] instanceof String)) {
            throw new Error("Expected the field `boxName` to be a primitive type in the JSON string but got " + data['boxName']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * @member {Number} boxId
 */
IncomingTransaction.prototype['boxId'] = undefined;

/**
 * @member {String} boxName
 */
IncomingTransaction.prototype['boxName'] = undefined;

/**
 * @member {Number} id
 */
IncomingTransaction.prototype['id'] = undefined;

/**
 * @member {Number} outgoingTransactionId
 */
IncomingTransaction.prototype['outgoingTransactionId'] = undefined;

/**
 * @member {Number} receivedImageCount
 */
IncomingTransaction.prototype['receivedImageCount'] = undefined;

/**
 * @member {String} status
 */
IncomingTransaction.prototype['status'] = undefined;

/**
 * @member {Number} totalImageCount
 */
IncomingTransaction.prototype['totalImageCount'] = undefined;

/**
 * @member {Number} updated
 */
IncomingTransaction.prototype['updated'] = undefined;






export default IncomingTransaction;

