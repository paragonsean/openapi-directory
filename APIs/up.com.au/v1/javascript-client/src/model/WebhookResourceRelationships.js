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
import AccountResourceRelationshipsTransactions from './AccountResourceRelationshipsTransactions';

/**
 * The WebhookResourceRelationships model module.
 * @module model/WebhookResourceRelationships
 * @version v1
 */
class WebhookResourceRelationships {
    /**
     * Constructs a new <code>WebhookResourceRelationships</code>.
     * @alias module:model/WebhookResourceRelationships
     * @param logs {module:model/AccountResourceRelationshipsTransactions} 
     */
    constructor(logs) { 
        
        WebhookResourceRelationships.initialize(this, logs);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, logs) { 
        obj['logs'] = logs;
    }

    /**
     * Constructs a <code>WebhookResourceRelationships</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WebhookResourceRelationships} obj Optional instance to populate.
     * @return {module:model/WebhookResourceRelationships} The populated <code>WebhookResourceRelationships</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WebhookResourceRelationships();

            if (data.hasOwnProperty('logs')) {
                obj['logs'] = AccountResourceRelationshipsTransactions.constructFromObject(data['logs']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WebhookResourceRelationships</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WebhookResourceRelationships</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of WebhookResourceRelationships.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `logs`
        if (data['logs']) { // data not null
          AccountResourceRelationshipsTransactions.validateJSON(data['logs']);
        }

        return true;
    }


}

WebhookResourceRelationships.RequiredProperties = ["logs"];

/**
 * @member {module:model/AccountResourceRelationshipsTransactions} logs
 */
WebhookResourceRelationships.prototype['logs'] = undefined;






export default WebhookResourceRelationships;

