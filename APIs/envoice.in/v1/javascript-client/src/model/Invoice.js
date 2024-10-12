/**
 * API v1.0.0
 * [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/80638214aa04722c9203)  <span style='margin-left: 0.5em;'>or</span>  <a href='https://documenter.getpostman.com/view/3559821/TVeqcn2L' class='openapi-button' _ngcontent-c6>View Postman docs</a>    # Quickstart    Visit [github](https://github.com/EmitKnowledge/Envoice) to view the quickstart tutorial.    <div class='postman-tutorial'>    # Tutorial for running the API in postman    Click on \"\"Run in Postman\"\" button  <br /><br />  ![postman - tutorial - 1](/Assets/images/api/postman-tutorial/postman-tutorial-1.png)     ---     A new page will open.  Click the \"\"Postman for windows\"\" to run postman as a desktop app.  Make sure you have already [installed](https://www.getpostman.com/docs/postman/launching_postman/installation_and_updates) Postman.  <br /><br />  ![postman - tutorial - 2](/Assets/images/api/postman-tutorial/postman-tutorial-2.png)     ---     In chrome an alert might show up to set a default app for opening postman links. Click on \"\"Open Postman\"\".  <br /><br />  ![postman - tutorial - 3](/Assets/images/api/postman-tutorial/postman-tutorial-3.png)     ---     The OpenAPI specification will be imported in Postman as a new collection named \"\"Envoice api\"\"  <br /><br />  ![postman - tutorial - 4](/Assets/images/api/postman-tutorial/postman-tutorial-4.png)     ---     When testing be sure to check and modify the environment variables to suit your api key and secret. The domain is set to envoice's endpoint so you don't really need to change that.    <sub>\\*Eye button in top right corner </sub>  <br /><br />   ![postman - tutorial - 5](/Assets/images/api/postman-tutorial/postman-tutorial-5.png)  <br /><br />   ![postman - tutorial - 6](/Assets/images/api/postman-tutorial/postman-tutorial-6.png)     ---     You don't need to change the values of the header parameters, because they will be replaced automatically when you send a request with real values from the environment configured in the previous step.  <br /><br />  ![postman - tutorial - 7](/Assets/images/api/postman-tutorial/postman-tutorial-7.png)     ---     Modify the example data to suit your needs and send a request.  <br /><br />  ![postman - tutorial - 8](/Assets/images/api/postman-tutorial/postman-tutorial-8.png)  </div>    # Webhooks    Webhooks allow you to build or set up Envoice Apps which subscribe to invoice activities.   When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL.   Webhooks can be used to update an external invoice data storage.    In order to use webhooks visit [this link](/account/settings#api-tab) and add upto 10 webhook urls that will return status `200` in order to signal that the webhook is working.  All nonworking webhooks will be ignored after a certain period of time and several retry attempts.  If after several attempts the webhook starts to work, we will send you all activities, both past and present, in chronological order.    The payload of the webhook is in format:  ```  {      Signature: \"\"sha256 string\"\",      Timestamp: \"\"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"\",      Activity: {          Message: \"string\",          Link: \"share url\",          Type: int,                  InvoiceNumber: \"string\",          InvoiceId: int,                  OrderNumber: \"string\",          OrderId: int,          Id: int,          CreatedOn: \"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"      }  }  ```            
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
import Activity from './Activity';
import InvoiceAttachment from './InvoiceAttachment';
import InvoiceItem from './InvoiceItem';
import Payment from './Payment';
import PaymentGatewayForInvoice from './PaymentGatewayForInvoice';

/**
 * The Invoice model module.
 * @module model/Invoice
 * @version v1
 */
class Invoice {
    /**
     * Constructs a new <code>Invoice</code>.
     * @alias module:model/Invoice
     */
    constructor() { 
        
        Invoice.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Invoice</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Invoice} obj Optional instance to populate.
     * @return {module:model/Invoice} The populated <code>Invoice</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Invoice();

            if (data.hasOwnProperty('AccessToken')) {
                obj['AccessToken'] = ApiClient.convertToType(data['AccessToken'], 'String');
            }
            if (data.hasOwnProperty('Activities')) {
                obj['Activities'] = ApiClient.convertToType(data['Activities'], [Activity]);
            }
            if (data.hasOwnProperty('Attachments')) {
                obj['Attachments'] = ApiClient.convertToType(data['Attachments'], [InvoiceAttachment]);
            }
            if (data.hasOwnProperty('ClientId')) {
                obj['ClientId'] = ApiClient.convertToType(data['ClientId'], 'Number');
            }
            if (data.hasOwnProperty('ClonedFromId')) {
                obj['ClonedFromId'] = ApiClient.convertToType(data['ClonedFromId'], 'Number');
            }
            if (data.hasOwnProperty('CurrencyId')) {
                obj['CurrencyId'] = ApiClient.convertToType(data['CurrencyId'], 'Number');
            }
            if (data.hasOwnProperty('DiscountAmount')) {
                obj['DiscountAmount'] = ApiClient.convertToType(data['DiscountAmount'], 'Number');
            }
            if (data.hasOwnProperty('Duedate')) {
                obj['Duedate'] = ApiClient.convertToType(data['Duedate'], 'Date');
            }
            if (data.hasOwnProperty('EnablePartialPayments')) {
                obj['EnablePartialPayments'] = ApiClient.convertToType(data['EnablePartialPayments'], 'Boolean');
            }
            if (data.hasOwnProperty('EstimationId')) {
                obj['EstimationId'] = ApiClient.convertToType(data['EstimationId'], 'Number');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('InvoiceCategoryId')) {
                obj['InvoiceCategoryId'] = ApiClient.convertToType(data['InvoiceCategoryId'], 'Number');
            }
            if (data.hasOwnProperty('IsDigitallySigned')) {
                obj['IsDigitallySigned'] = ApiClient.convertToType(data['IsDigitallySigned'], 'Boolean');
            }
            if (data.hasOwnProperty('IssuedOn')) {
                obj['IssuedOn'] = ApiClient.convertToType(data['IssuedOn'], 'Date');
            }
            if (data.hasOwnProperty('Items')) {
                obj['Items'] = ApiClient.convertToType(data['Items'], [InvoiceItem]);
            }
            if (data.hasOwnProperty('Notes')) {
                obj['Notes'] = ApiClient.convertToType(data['Notes'], 'String');
            }
            if (data.hasOwnProperty('Number')) {
                obj['Number'] = ApiClient.convertToType(data['Number'], 'String');
            }
            if (data.hasOwnProperty('OrderId')) {
                obj['OrderId'] = ApiClient.convertToType(data['OrderId'], 'Number');
            }
            if (data.hasOwnProperty('PaymentGateways')) {
                obj['PaymentGateways'] = ApiClient.convertToType(data['PaymentGateways'], [PaymentGatewayForInvoice]);
            }
            if (data.hasOwnProperty('PaymentLinkId')) {
                obj['PaymentLinkId'] = ApiClient.convertToType(data['PaymentLinkId'], 'Number');
            }
            if (data.hasOwnProperty('Payments')) {
                obj['Payments'] = ApiClient.convertToType(data['Payments'], [Payment]);
            }
            if (data.hasOwnProperty('PoNumber')) {
                obj['PoNumber'] = ApiClient.convertToType(data['PoNumber'], 'String');
            }
            if (data.hasOwnProperty('RecurringProfileId')) {
                obj['RecurringProfileId'] = ApiClient.convertToType(data['RecurringProfileId'], 'Number');
            }
            if (data.hasOwnProperty('ShouldSendReminders')) {
                obj['ShouldSendReminders'] = ApiClient.convertToType(data['ShouldSendReminders'], 'Boolean');
            }
            if (data.hasOwnProperty('Status')) {
                obj['Status'] = ApiClient.convertToType(data['Status'], 'String');
            }
            if (data.hasOwnProperty('SubTotalAmount')) {
                obj['SubTotalAmount'] = ApiClient.convertToType(data['SubTotalAmount'], 'Number');
            }
            if (data.hasOwnProperty('TaxAmount')) {
                obj['TaxAmount'] = ApiClient.convertToType(data['TaxAmount'], 'Number');
            }
            if (data.hasOwnProperty('Terms')) {
                obj['Terms'] = ApiClient.convertToType(data['Terms'], 'String');
            }
            if (data.hasOwnProperty('TotalAmount')) {
                obj['TotalAmount'] = ApiClient.convertToType(data['TotalAmount'], 'Number');
            }
            if (data.hasOwnProperty('UserId')) {
                obj['UserId'] = ApiClient.convertToType(data['UserId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Invoice</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Invoice</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AccessToken'] && !(typeof data['AccessToken'] === 'string' || data['AccessToken'] instanceof String)) {
            throw new Error("Expected the field `AccessToken` to be a primitive type in the JSON string but got " + data['AccessToken']);
        }
        if (data['Activities']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Activities'])) {
                throw new Error("Expected the field `Activities` to be an array in the JSON data but got " + data['Activities']);
            }
            // validate the optional field `Activities` (array)
            for (const item of data['Activities']) {
                Activity.validateJSON(item);
            };
        }
        if (data['Attachments']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Attachments'])) {
                throw new Error("Expected the field `Attachments` to be an array in the JSON data but got " + data['Attachments']);
            }
            // validate the optional field `Attachments` (array)
            for (const item of data['Attachments']) {
                InvoiceAttachment.validateJSON(item);
            };
        }
        if (data['Items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Items'])) {
                throw new Error("Expected the field `Items` to be an array in the JSON data but got " + data['Items']);
            }
            // validate the optional field `Items` (array)
            for (const item of data['Items']) {
                InvoiceItem.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['Notes'] && !(typeof data['Notes'] === 'string' || data['Notes'] instanceof String)) {
            throw new Error("Expected the field `Notes` to be a primitive type in the JSON string but got " + data['Notes']);
        }
        // ensure the json data is a string
        if (data['Number'] && !(typeof data['Number'] === 'string' || data['Number'] instanceof String)) {
            throw new Error("Expected the field `Number` to be a primitive type in the JSON string but got " + data['Number']);
        }
        if (data['PaymentGateways']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['PaymentGateways'])) {
                throw new Error("Expected the field `PaymentGateways` to be an array in the JSON data but got " + data['PaymentGateways']);
            }
            // validate the optional field `PaymentGateways` (array)
            for (const item of data['PaymentGateways']) {
                PaymentGatewayForInvoice.validateJSON(item);
            };
        }
        if (data['Payments']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Payments'])) {
                throw new Error("Expected the field `Payments` to be an array in the JSON data but got " + data['Payments']);
            }
            // validate the optional field `Payments` (array)
            for (const item of data['Payments']) {
                Payment.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['PoNumber'] && !(typeof data['PoNumber'] === 'string' || data['PoNumber'] instanceof String)) {
            throw new Error("Expected the field `PoNumber` to be a primitive type in the JSON string but got " + data['PoNumber']);
        }
        // ensure the json data is a string
        if (data['Status'] && !(typeof data['Status'] === 'string' || data['Status'] instanceof String)) {
            throw new Error("Expected the field `Status` to be a primitive type in the JSON string but got " + data['Status']);
        }
        // ensure the json data is a string
        if (data['Terms'] && !(typeof data['Terms'] === 'string' || data['Terms'] instanceof String)) {
            throw new Error("Expected the field `Terms` to be a primitive type in the JSON string but got " + data['Terms']);
        }

        return true;
    }


}



/**
 * @member {String} AccessToken
 */
Invoice.prototype['AccessToken'] = undefined;

/**
 * @member {Array.<module:model/Activity>} Activities
 */
Invoice.prototype['Activities'] = undefined;

/**
 * @member {Array.<module:model/InvoiceAttachment>} Attachments
 */
Invoice.prototype['Attachments'] = undefined;

/**
 * @member {Number} ClientId
 */
Invoice.prototype['ClientId'] = undefined;

/**
 * @member {Number} ClonedFromId
 */
Invoice.prototype['ClonedFromId'] = undefined;

/**
 * @member {Number} CurrencyId
 */
Invoice.prototype['CurrencyId'] = undefined;

/**
 * @member {Number} DiscountAmount
 */
Invoice.prototype['DiscountAmount'] = undefined;

/**
 * @member {Date} Duedate
 */
Invoice.prototype['Duedate'] = undefined;

/**
 * @member {Boolean} EnablePartialPayments
 */
Invoice.prototype['EnablePartialPayments'] = undefined;

/**
 * @member {Number} EstimationId
 */
Invoice.prototype['EstimationId'] = undefined;

/**
 * @member {Number} Id
 */
Invoice.prototype['Id'] = undefined;

/**
 * @member {Number} InvoiceCategoryId
 */
Invoice.prototype['InvoiceCategoryId'] = undefined;

/**
 * @member {Boolean} IsDigitallySigned
 */
Invoice.prototype['IsDigitallySigned'] = undefined;

/**
 * @member {Date} IssuedOn
 */
Invoice.prototype['IssuedOn'] = undefined;

/**
 * @member {Array.<module:model/InvoiceItem>} Items
 */
Invoice.prototype['Items'] = undefined;

/**
 * @member {String} Notes
 */
Invoice.prototype['Notes'] = undefined;

/**
 * @member {String} Number
 */
Invoice.prototype['Number'] = undefined;

/**
 * @member {Number} OrderId
 */
Invoice.prototype['OrderId'] = undefined;

/**
 * @member {Array.<module:model/PaymentGatewayForInvoice>} PaymentGateways
 */
Invoice.prototype['PaymentGateways'] = undefined;

/**
 * @member {Number} PaymentLinkId
 */
Invoice.prototype['PaymentLinkId'] = undefined;

/**
 * @member {Array.<module:model/Payment>} Payments
 */
Invoice.prototype['Payments'] = undefined;

/**
 * @member {String} PoNumber
 */
Invoice.prototype['PoNumber'] = undefined;

/**
 * @member {Number} RecurringProfileId
 */
Invoice.prototype['RecurringProfileId'] = undefined;

/**
 * @member {Boolean} ShouldSendReminders
 */
Invoice.prototype['ShouldSendReminders'] = undefined;

/**
 * @member {module:model/Invoice.StatusEnum} Status
 */
Invoice.prototype['Status'] = undefined;

/**
 * @member {Number} SubTotalAmount
 */
Invoice.prototype['SubTotalAmount'] = undefined;

/**
 * @member {Number} TaxAmount
 */
Invoice.prototype['TaxAmount'] = undefined;

/**
 * @member {String} Terms
 */
Invoice.prototype['Terms'] = undefined;

/**
 * @member {Number} TotalAmount
 */
Invoice.prototype['TotalAmount'] = undefined;

/**
 * @member {Number} UserId
 */
Invoice.prototype['UserId'] = undefined;





/**
 * Allowed values for the <code>Status</code> property.
 * @enum {String}
 * @readonly
 */
Invoice['StatusEnum'] = {

    /**
     * value: "Draft"
     * @const
     */
    "Draft": "Draft",

    /**
     * value: "Paid"
     * @const
     */
    "Paid": "Paid",

    /**
     * value: "Unpaid"
     * @const
     */
    "Unpaid": "Unpaid",

    /**
     * value: "Overdue"
     * @const
     */
    "Overdue": "Overdue",

    /**
     * value: "Void"
     * @const
     */
    "Void": "Void"
};



export default Invoice;

