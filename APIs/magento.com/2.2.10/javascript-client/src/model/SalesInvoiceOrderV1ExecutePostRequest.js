/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import SalesDataInvoiceCommentCreationInterface from './SalesDataInvoiceCommentCreationInterface';
import SalesDataInvoiceCreationArgumentsInterface from './SalesDataInvoiceCreationArgumentsInterface';
import SalesDataInvoiceItemCreationInterface from './SalesDataInvoiceItemCreationInterface';

/**
 * The SalesInvoiceOrderV1ExecutePostRequest model module.
 * @module model/SalesInvoiceOrderV1ExecutePostRequest
 * @version 2.2.10
 */
class SalesInvoiceOrderV1ExecutePostRequest {
    /**
     * Constructs a new <code>SalesInvoiceOrderV1ExecutePostRequest</code>.
     * @alias module:model/SalesInvoiceOrderV1ExecutePostRequest
     */
    constructor() { 
        
        SalesInvoiceOrderV1ExecutePostRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SalesInvoiceOrderV1ExecutePostRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SalesInvoiceOrderV1ExecutePostRequest} obj Optional instance to populate.
     * @return {module:model/SalesInvoiceOrderV1ExecutePostRequest} The populated <code>SalesInvoiceOrderV1ExecutePostRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SalesInvoiceOrderV1ExecutePostRequest();

            if (data.hasOwnProperty('appendComment')) {
                obj['appendComment'] = ApiClient.convertToType(data['appendComment'], 'Boolean');
            }
            if (data.hasOwnProperty('arguments')) {
                obj['arguments'] = SalesDataInvoiceCreationArgumentsInterface.constructFromObject(data['arguments']);
            }
            if (data.hasOwnProperty('capture')) {
                obj['capture'] = ApiClient.convertToType(data['capture'], 'Boolean');
            }
            if (data.hasOwnProperty('comment')) {
                obj['comment'] = SalesDataInvoiceCommentCreationInterface.constructFromObject(data['comment']);
            }
            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [SalesDataInvoiceItemCreationInterface]);
            }
            if (data.hasOwnProperty('notify')) {
                obj['notify'] = ApiClient.convertToType(data['notify'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SalesInvoiceOrderV1ExecutePostRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SalesInvoiceOrderV1ExecutePostRequest</code>.
     */
    static validateJSON(data) {
        // validate the optional field `arguments`
        if (data['arguments']) { // data not null
          SalesDataInvoiceCreationArgumentsInterface.validateJSON(data['arguments']);
        }
        // validate the optional field `comment`
        if (data['comment']) { // data not null
          SalesDataInvoiceCommentCreationInterface.validateJSON(data['comment']);
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                SalesDataInvoiceItemCreationInterface.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Boolean} appendComment
 */
SalesInvoiceOrderV1ExecutePostRequest.prototype['appendComment'] = undefined;

/**
 * @member {module:model/SalesDataInvoiceCreationArgumentsInterface} arguments
 */
SalesInvoiceOrderV1ExecutePostRequest.prototype['arguments'] = undefined;

/**
 * @member {Boolean} capture
 */
SalesInvoiceOrderV1ExecutePostRequest.prototype['capture'] = undefined;

/**
 * @member {module:model/SalesDataInvoiceCommentCreationInterface} comment
 */
SalesInvoiceOrderV1ExecutePostRequest.prototype['comment'] = undefined;

/**
 * @member {Array.<module:model/SalesDataInvoiceItemCreationInterface>} items
 */
SalesInvoiceOrderV1ExecutePostRequest.prototype['items'] = undefined;

/**
 * @member {Boolean} notify
 */
SalesInvoiceOrderV1ExecutePostRequest.prototype['notify'] = undefined;






export default SalesInvoiceOrderV1ExecutePostRequest;

