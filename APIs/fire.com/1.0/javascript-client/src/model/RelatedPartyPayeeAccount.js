/**
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The RelatedPartyPayeeAccount model module.
 * @module model/RelatedPartyPayeeAccount
 * @version 1.0
 */
class RelatedPartyPayeeAccount {
    /**
     * Constructs a new <code>RelatedPartyPayeeAccount</code>.
     * @alias module:model/RelatedPartyPayeeAccount
     */
    constructor() { 
        
        RelatedPartyPayeeAccount.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>RelatedPartyPayeeAccount</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RelatedPartyPayeeAccount} obj Optional instance to populate.
     * @return {module:model/RelatedPartyPayeeAccount} The populated <code>RelatedPartyPayeeAccount</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RelatedPartyPayeeAccount();

            if (data.hasOwnProperty('accountNumber')) {
                obj['accountNumber'] = ApiClient.convertToType(data['accountNumber'], 'String');
            }
            if (data.hasOwnProperty('alias')) {
                obj['alias'] = ApiClient.convertToType(data['alias'], 'String');
            }
            if (data.hasOwnProperty('bic')) {
                obj['bic'] = ApiClient.convertToType(data['bic'], 'String');
            }
            if (data.hasOwnProperty('iban')) {
                obj['iban'] = ApiClient.convertToType(data['iban'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('nsc')) {
                obj['nsc'] = ApiClient.convertToType(data['nsc'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RelatedPartyPayeeAccount</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RelatedPartyPayeeAccount</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['accountNumber'] && !(typeof data['accountNumber'] === 'string' || data['accountNumber'] instanceof String)) {
            throw new Error("Expected the field `accountNumber` to be a primitive type in the JSON string but got " + data['accountNumber']);
        }
        // ensure the json data is a string
        if (data['alias'] && !(typeof data['alias'] === 'string' || data['alias'] instanceof String)) {
            throw new Error("Expected the field `alias` to be a primitive type in the JSON string but got " + data['alias']);
        }
        // ensure the json data is a string
        if (data['bic'] && !(typeof data['bic'] === 'string' || data['bic'] instanceof String)) {
            throw new Error("Expected the field `bic` to be a primitive type in the JSON string but got " + data['bic']);
        }
        // ensure the json data is a string
        if (data['iban'] && !(typeof data['iban'] === 'string' || data['iban'] instanceof String)) {
            throw new Error("Expected the field `iban` to be a primitive type in the JSON string but got " + data['iban']);
        }
        // ensure the json data is a string
        if (data['nsc'] && !(typeof data['nsc'] === 'string' || data['nsc'] instanceof String)) {
            throw new Error("Expected the field `nsc` to be a primitive type in the JSON string but got " + data['nsc']);
        }

        return true;
    }


}



/**
 * The account number of the Withdrawl account in reference
 * @member {String} accountNumber
 */
RelatedPartyPayeeAccount.prototype['accountNumber'] = undefined;

/**
 * The Alias name of the Withdrawl account in reference
 * @member {String} alias
 */
RelatedPartyPayeeAccount.prototype['alias'] = undefined;

/**
 * The BIC of the Withdrawl account in reference
 * @member {String} bic
 */
RelatedPartyPayeeAccount.prototype['bic'] = undefined;

/**
 * The BIC of the Withdrawl account in reference
 * @member {String} iban
 */
RelatedPartyPayeeAccount.prototype['iban'] = undefined;

/**
 * The ID number of the Withdrawl account in reference
 * @member {Number} id
 */
RelatedPartyPayeeAccount.prototype['id'] = undefined;

/**
 * (Conditional) Provide this field if using Mode 2 and the payee account is in GBP.
 * @member {String} nsc
 */
RelatedPartyPayeeAccount.prototype['nsc'] = undefined;






export default RelatedPartyPayeeAccount;

