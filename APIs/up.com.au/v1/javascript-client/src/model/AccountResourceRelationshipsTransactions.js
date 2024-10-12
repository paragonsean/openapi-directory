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

/**
 * The AccountResourceRelationshipsTransactions model module.
 * @module model/AccountResourceRelationshipsTransactions
 * @version v1
 */
class AccountResourceRelationshipsTransactions {
    /**
     * Constructs a new <code>AccountResourceRelationshipsTransactions</code>.
     * @alias module:model/AccountResourceRelationshipsTransactions
     */
    constructor() { 
        
        AccountResourceRelationshipsTransactions.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AccountResourceRelationshipsTransactions</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccountResourceRelationshipsTransactions} obj Optional instance to populate.
     * @return {module:model/AccountResourceRelationshipsTransactions} The populated <code>AccountResourceRelationshipsTransactions</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccountResourceRelationshipsTransactions();

            if (data.hasOwnProperty('links')) {
                obj['links'] = AccountResourceRelationshipsTransactionsLinks.constructFromObject(data['links']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccountResourceRelationshipsTransactions</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccountResourceRelationshipsTransactions</code>.
     */
    static validateJSON(data) {
        // validate the optional field `links`
        if (data['links']) { // data not null
          AccountResourceRelationshipsTransactionsLinks.validateJSON(data['links']);
        }

        return true;
    }


}



/**
 * @member {module:model/AccountResourceRelationshipsTransactionsLinks} links
 */
AccountResourceRelationshipsTransactions.prototype['links'] = undefined;






export default AccountResourceRelationshipsTransactions;

