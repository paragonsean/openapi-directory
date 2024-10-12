/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
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
import NewPaymentAllocation from './NewPaymentAllocation';

/**
 * The NewPayment model module.
 * @module model/NewPayment
 * @version v1
 */
class NewPayment {
    /**
     * Constructs a new <code>NewPayment</code>.
     * @alias module:model/NewPayment
     */
    constructor() { 
        
        NewPayment.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>NewPayment</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NewPayment} obj Optional instance to populate.
     * @return {module:model/NewPayment} The populated <code>NewPayment</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NewPayment();

            if (data.hasOwnProperty('Amount')) {
                obj['Amount'] = ApiClient.convertToType(data['Amount'], 'Number');
            }
            if (data.hasOwnProperty('CustomerIDFK')) {
                obj['CustomerIDFK'] = ApiClient.convertToType(data['CustomerIDFK'], 'Number');
            }
            if (data.hasOwnProperty('DateIssued')) {
                obj['DateIssued'] = ApiClient.convertToType(data['DateIssued'], 'Date');
            }
            if (data.hasOwnProperty('ExchangeRate')) {
                obj['ExchangeRate'] = ApiClient.convertToType(data['ExchangeRate'], 'Number');
            }
            if (data.hasOwnProperty('Notes')) {
                obj['Notes'] = ApiClient.convertToType(data['Notes'], 'String');
            }
            if (data.hasOwnProperty('PaymentAllocations')) {
                obj['PaymentAllocations'] = ApiClient.convertToType(data['PaymentAllocations'], [NewPaymentAllocation]);
            }
            if (data.hasOwnProperty('PaymentNumber')) {
                obj['PaymentNumber'] = ApiClient.convertToType(data['PaymentNumber'], 'String');
            }
            if (data.hasOwnProperty('PaymentProviderCode')) {
                obj['PaymentProviderCode'] = ApiClient.convertToType(data['PaymentProviderCode'], 'String');
            }
            if (data.hasOwnProperty('TransactionPrefix')) {
                obj['TransactionPrefix'] = ApiClient.convertToType(data['TransactionPrefix'], 'String');
            }
            if (data.hasOwnProperty('TransactionReference')) {
                obj['TransactionReference'] = ApiClient.convertToType(data['TransactionReference'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NewPayment</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NewPayment</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Notes'] && !(typeof data['Notes'] === 'string' || data['Notes'] instanceof String)) {
            throw new Error("Expected the field `Notes` to be a primitive type in the JSON string but got " + data['Notes']);
        }
        if (data['PaymentAllocations']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['PaymentAllocations'])) {
                throw new Error("Expected the field `PaymentAllocations` to be an array in the JSON data but got " + data['PaymentAllocations']);
            }
            // validate the optional field `PaymentAllocations` (array)
            for (const item of data['PaymentAllocations']) {
                NewPaymentAllocation.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['PaymentNumber'] && !(typeof data['PaymentNumber'] === 'string' || data['PaymentNumber'] instanceof String)) {
            throw new Error("Expected the field `PaymentNumber` to be a primitive type in the JSON string but got " + data['PaymentNumber']);
        }
        // ensure the json data is a string
        if (data['PaymentProviderCode'] && !(typeof data['PaymentProviderCode'] === 'string' || data['PaymentProviderCode'] instanceof String)) {
            throw new Error("Expected the field `PaymentProviderCode` to be a primitive type in the JSON string but got " + data['PaymentProviderCode']);
        }
        // ensure the json data is a string
        if (data['TransactionPrefix'] && !(typeof data['TransactionPrefix'] === 'string' || data['TransactionPrefix'] instanceof String)) {
            throw new Error("Expected the field `TransactionPrefix` to be a primitive type in the JSON string but got " + data['TransactionPrefix']);
        }
        // ensure the json data is a string
        if (data['TransactionReference'] && !(typeof data['TransactionReference'] === 'string' || data['TransactionReference'] instanceof String)) {
            throw new Error("Expected the field `TransactionReference` to be a primitive type in the JSON string but got " + data['TransactionReference']);
        }

        return true;
    }


}



/**
 * @member {Number} Amount
 */
NewPayment.prototype['Amount'] = undefined;

/**
 * Only required if no invoice allocations specified.
 * @member {Number} CustomerIDFK
 */
NewPayment.prototype['CustomerIDFK'] = undefined;

/**
 * Date of Payment. If not specified, assumes today.
 * @member {Date} DateIssued
 */
NewPayment.prototype['DateIssued'] = undefined;

/**
 * Optional. Only used when the Customer's currecy is different from the Avaza account's base currency. Specifies the exchange rate that should apply between the customer currency and base currency. If not provided we will obtain an up to date exchange rate for the Payment Issue Date.
 * @member {Number} ExchangeRate
 */
NewPayment.prototype['ExchangeRate'] = undefined;

/**
 * @member {String} Notes
 */
NewPayment.prototype['Notes'] = undefined;

/**
 * List of amounts within this payment that are allocated to invoices. The sum of these be less than or equal to the payment amount.
 * @member {Array.<module:model/NewPaymentAllocation>} PaymentAllocations
 */
NewPayment.prototype['PaymentAllocations'] = undefined;

/**
 * Optional. If not specified will be automatically generated
 * @member {String} PaymentNumber
 */
NewPayment.prototype['PaymentNumber'] = undefined;

/**
 * Optional for storing the payment provider who was the source of funds.
 * @member {String} PaymentProviderCode
 */
NewPayment.prototype['PaymentProviderCode'] = undefined;

/**
 * Optional to override the default prefix added to Payment Numbers
 * @member {String} TransactionPrefix
 */
NewPayment.prototype['TransactionPrefix'] = undefined;

/**
 * Optional for storing the reference # of the payment method.
 * @member {String} TransactionReference
 */
NewPayment.prototype['TransactionReference'] = undefined;






export default NewPayment;

