/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
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
import AccountResourceRelationshipsTransactionsLinks from './AccountResourceRelationshipsTransactionsLinks';
import WebhookEventResourceRelationshipsTransactionData from './WebhookEventResourceRelationshipsTransactionData';

/**
 * The WebhookEventResourceRelationshipsTransaction model module.
 * @module model/WebhookEventResourceRelationshipsTransaction
 * @version v1
 */
class WebhookEventResourceRelationshipsTransaction {
    /**
     * Constructs a new <code>WebhookEventResourceRelationshipsTransaction</code>.
     * @alias module:model/WebhookEventResourceRelationshipsTransaction
     * @param data {module:model/WebhookEventResourceRelationshipsTransactionData} 
     */
    constructor(data) { 
        
        WebhookEventResourceRelationshipsTransaction.initialize(this, data);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, data) { 
        obj['data'] = data;
    }

    /**
     * Constructs a <code>WebhookEventResourceRelationshipsTransaction</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WebhookEventResourceRelationshipsTransaction} obj Optional instance to populate.
     * @return {module:model/WebhookEventResourceRelationshipsTransaction} The populated <code>WebhookEventResourceRelationshipsTransaction</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WebhookEventResourceRelationshipsTransaction();

            if (data.hasOwnProperty('data')) {
                obj['data'] = WebhookEventResourceRelationshipsTransactionData.constructFromObject(data['data']);
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = AccountResourceRelationshipsTransactionsLinks.constructFromObject(data['links']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WebhookEventResourceRelationshipsTransaction</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WebhookEventResourceRelationshipsTransaction</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of WebhookEventResourceRelationshipsTransaction.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `data`
        if (data['data']) { // data not null
          WebhookEventResourceRelationshipsTransactionData.validateJSON(data['data']);
        }
        // validate the optional field `links`
        if (data['links']) { // data not null
          AccountResourceRelationshipsTransactionsLinks.validateJSON(data['links']);
        }

        return true;
    }


}

WebhookEventResourceRelationshipsTransaction.RequiredProperties = ["data"];

/**
 * @member {module:model/WebhookEventResourceRelationshipsTransactionData} data
 */
WebhookEventResourceRelationshipsTransaction.prototype['data'] = undefined;

/**
 * @member {module:model/AccountResourceRelationshipsTransactionsLinks} links
 */
WebhookEventResourceRelationshipsTransaction.prototype['links'] = undefined;






export default WebhookEventResourceRelationshipsTransaction;

