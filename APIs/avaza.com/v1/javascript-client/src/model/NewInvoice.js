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
import NewInvoiceLineItem from './NewInvoiceLineItem';

/**
 * The NewInvoice model module.
 * @module model/NewInvoice
 * @version v1
 */
class NewInvoice {
    /**
     * Constructs a new <code>NewInvoice</code>.
     * New invoice to be created
     * @alias module:model/NewInvoice
     */
    constructor() { 
        
        NewInvoice.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>NewInvoice</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/NewInvoice} obj Optional instance to populate.
     * @return {module:model/NewInvoice} The populated <code>NewInvoice</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new NewInvoice();

            if (data.hasOwnProperty('CompanyIDFK')) {
                obj['CompanyIDFK'] = ApiClient.convertToType(data['CompanyIDFK'], 'Number');
            }
            if (data.hasOwnProperty('CompanyName')) {
                obj['CompanyName'] = ApiClient.convertToType(data['CompanyName'], 'String');
            }
            if (data.hasOwnProperty('CurrencyCode')) {
                obj['CurrencyCode'] = ApiClient.convertToType(data['CurrencyCode'], 'String');
            }
            if (data.hasOwnProperty('CustomerPONumber')) {
                obj['CustomerPONumber'] = ApiClient.convertToType(data['CustomerPONumber'], 'String');
            }
            if (data.hasOwnProperty('DateIssued')) {
                obj['DateIssued'] = ApiClient.convertToType(data['DateIssued'], 'Date');
            }
            if (data.hasOwnProperty('DueDate')) {
                obj['DueDate'] = ApiClient.convertToType(data['DueDate'], 'Date');
            }
            if (data.hasOwnProperty('Email')) {
                obj['Email'] = ApiClient.convertToType(data['Email'], 'String');
            }
            if (data.hasOwnProperty('ExchangeRate')) {
                obj['ExchangeRate'] = ApiClient.convertToType(data['ExchangeRate'], 'Number');
            }
            if (data.hasOwnProperty('Firstname')) {
                obj['Firstname'] = ApiClient.convertToType(data['Firstname'], 'String');
            }
            if (data.hasOwnProperty('InvoiceNumber')) {
                obj['InvoiceNumber'] = ApiClient.convertToType(data['InvoiceNumber'], 'String');
            }
            if (data.hasOwnProperty('InvoiceTemplateIDFK')) {
                obj['InvoiceTemplateIDFK'] = ApiClient.convertToType(data['InvoiceTemplateIDFK'], 'Number');
            }
            if (data.hasOwnProperty('Lastname')) {
                obj['Lastname'] = ApiClient.convertToType(data['Lastname'], 'String');
            }
            if (data.hasOwnProperty('LineItems')) {
                obj['LineItems'] = ApiClient.convertToType(data['LineItems'], [NewInvoiceLineItem]);
            }
            if (data.hasOwnProperty('Notes')) {
                obj['Notes'] = ApiClient.convertToType(data['Notes'], 'String');
            }
            if (data.hasOwnProperty('PaymentTerms')) {
                obj['PaymentTerms'] = ApiClient.convertToType(data['PaymentTerms'], 'Number');
            }
            if (data.hasOwnProperty('Subject')) {
                obj['Subject'] = ApiClient.convertToType(data['Subject'], 'String');
            }
            if (data.hasOwnProperty('TransactionPrefix')) {
                obj['TransactionPrefix'] = ApiClient.convertToType(data['TransactionPrefix'], 'String');
            }
            if (data.hasOwnProperty('TransactionTaxConfigCode')) {
                obj['TransactionTaxConfigCode'] = ApiClient.convertToType(data['TransactionTaxConfigCode'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>NewInvoice</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>NewInvoice</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['CompanyName'] && !(typeof data['CompanyName'] === 'string' || data['CompanyName'] instanceof String)) {
            throw new Error("Expected the field `CompanyName` to be a primitive type in the JSON string but got " + data['CompanyName']);
        }
        // ensure the json data is a string
        if (data['CurrencyCode'] && !(typeof data['CurrencyCode'] === 'string' || data['CurrencyCode'] instanceof String)) {
            throw new Error("Expected the field `CurrencyCode` to be a primitive type in the JSON string but got " + data['CurrencyCode']);
        }
        // ensure the json data is a string
        if (data['CustomerPONumber'] && !(typeof data['CustomerPONumber'] === 'string' || data['CustomerPONumber'] instanceof String)) {
            throw new Error("Expected the field `CustomerPONumber` to be a primitive type in the JSON string but got " + data['CustomerPONumber']);
        }
        // ensure the json data is a string
        if (data['Email'] && !(typeof data['Email'] === 'string' || data['Email'] instanceof String)) {
            throw new Error("Expected the field `Email` to be a primitive type in the JSON string but got " + data['Email']);
        }
        // ensure the json data is a string
        if (data['Firstname'] && !(typeof data['Firstname'] === 'string' || data['Firstname'] instanceof String)) {
            throw new Error("Expected the field `Firstname` to be a primitive type in the JSON string but got " + data['Firstname']);
        }
        // ensure the json data is a string
        if (data['InvoiceNumber'] && !(typeof data['InvoiceNumber'] === 'string' || data['InvoiceNumber'] instanceof String)) {
            throw new Error("Expected the field `InvoiceNumber` to be a primitive type in the JSON string but got " + data['InvoiceNumber']);
        }
        // ensure the json data is a string
        if (data['Lastname'] && !(typeof data['Lastname'] === 'string' || data['Lastname'] instanceof String)) {
            throw new Error("Expected the field `Lastname` to be a primitive type in the JSON string but got " + data['Lastname']);
        }
        if (data['LineItems']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['LineItems'])) {
                throw new Error("Expected the field `LineItems` to be an array in the JSON data but got " + data['LineItems']);
            }
            // validate the optional field `LineItems` (array)
            for (const item of data['LineItems']) {
                NewInvoiceLineItem.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['Notes'] && !(typeof data['Notes'] === 'string' || data['Notes'] instanceof String)) {
            throw new Error("Expected the field `Notes` to be a primitive type in the JSON string but got " + data['Notes']);
        }
        // ensure the json data is a string
        if (data['Subject'] && !(typeof data['Subject'] === 'string' || data['Subject'] instanceof String)) {
            throw new Error("Expected the field `Subject` to be a primitive type in the JSON string but got " + data['Subject']);
        }
        // ensure the json data is a string
        if (data['TransactionPrefix'] && !(typeof data['TransactionPrefix'] === 'string' || data['TransactionPrefix'] instanceof String)) {
            throw new Error("Expected the field `TransactionPrefix` to be a primitive type in the JSON string but got " + data['TransactionPrefix']);
        }
        // ensure the json data is a string
        if (data['TransactionTaxConfigCode'] && !(typeof data['TransactionTaxConfigCode'] === 'string' || data['TransactionTaxConfigCode'] instanceof String)) {
            throw new Error("Expected the field `TransactionTaxConfigCode` to be a primitive type in the JSON string but got " + data['TransactionTaxConfigCode']);
        }

        return true;
    }


}



/**
 * If left blank then you must specify Company Name.
 * @member {Number} CompanyIDFK
 */
NewInvoice.prototype['CompanyIDFK'] = undefined;

/**
 * If left blank then you must specify Company ID. Specified Name will be used to match existing customer record. If not matched then it will be used to create a new customer. First Name, Last Name and Email will only be used if it is a new company. If the Company name appears multiple times we will check the email address to find a matching company. If email address doesn't identify a matching company then the invoice creation will be rejected.
 * @member {String} CompanyName
 */
NewInvoice.prototype['CompanyName'] = undefined;

/**
 * Expects ISO Standard 3 character currency code. If left blank the currency will default to account's currency in general setting. For existing companies this field will be ignored and the invoice will use the currency of the customer. For new customers if the currency is not specified then account currency will be used otherwise the specified currency will be used.
 * @member {String} CurrencyCode
 */
NewInvoice.prototype['CurrencyCode'] = undefined;

/**
 * Plain UTF8 text. 100 characters max
 * @member {String} CustomerPONumber
 */
NewInvoice.prototype['CustomerPONumber'] = undefined;

/**
 * If not specified it will use today's date. The date should be specified as local date.
 * @member {Date} DateIssued
 */
NewInvoice.prototype['DateIssued'] = undefined;

/**
 * It will be auto calculated based on the payment term and issue date. Due Date must be greater than or equal to Issue Date. If the Due Date is specified then Payment Terms will be set to -1 (Custom)
 * @member {Date} DueDate
 */
NewInvoice.prototype['DueDate'] = undefined;

/**
 * Specified value will be used to create a new customer contact only if a new customer is being created.
 * @member {String} Email
 */
NewInvoice.prototype['Email'] = undefined;

/**
 * Exchange rate is only valid for invoices in currency other than default account currency. If not specified it will get the market rate based on the Date Issued.
 * @member {Number} ExchangeRate
 */
NewInvoice.prototype['ExchangeRate'] = undefined;

/**
 * Specified value will be used to create a new customer contact only if a new customer is being created.
 * @member {String} Firstname
 */
NewInvoice.prototype['Firstname'] = undefined;

/**
 * Pass any string. If left blank it will use the next number in the auto incrementing sequence. If an integer is passed then the largest integer will be use as the seed to auto generate the next invoice number in the sequence.
 * @member {String} InvoiceNumber
 */
NewInvoice.prototype['InvoiceNumber'] = undefined;

/**
 * If left blank the account default invoice template will be used.
 * @member {Number} InvoiceTemplateIDFK
 */
NewInvoice.prototype['InvoiceTemplateIDFK'] = undefined;

/**
 * Specified value will be used to create a new customer contact only if a new customer is being created.
 * @member {String} Lastname
 */
NewInvoice.prototype['Lastname'] = undefined;

/**
 * @member {Array.<module:model/NewInvoiceLineItem>} LineItems
 */
NewInvoice.prototype['LineItems'] = undefined;

/**
 * Plain UTF8 text. (no HTML). Max 2000 characters
 * @member {String} Notes
 */
NewInvoice.prototype['Notes'] = undefined;

/**
 *  \"If left blank we will set it to customer default. If specified then it must match one of your existing pre configured payment term periods. Your account starts with:  (-1 --- Custom, 0 --- Upon Receipt, 7 --- 7 Days, 15 --- 15 Days, 30 --- 30 Days, 45 --- 45 Days, 60 --- 60 Days)
 * @member {Number} PaymentTerms
 */
NewInvoice.prototype['PaymentTerms'] = undefined;

/**
 * Plain UTF8 text. (no HTML). 255 characters max
 * @member {String} Subject
 */
NewInvoice.prototype['Subject'] = undefined;

/**
 * A prefix for the Invoice number. e.g. 'INV'. If left blank it will be set to the account default. Max length 20 characters.
 * @member {String} TransactionPrefix
 */
NewInvoice.prototype['TransactionPrefix'] = undefined;

/**
 * Possible values are (EX --- Tax Exclusive, INC --- Tax Inclusive). If left empty it will use the account default.
 * @member {String} TransactionTaxConfigCode
 */
NewInvoice.prototype['TransactionTaxConfigCode'] = undefined;






export default NewInvoice;

