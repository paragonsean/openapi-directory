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
import ClientDetailsApiModel from './ClientDetailsApiModel';
import CurrencyDetailsApiModel from './CurrencyDetailsApiModel';
import InvoiceRecurringApiModel from './InvoiceRecurringApiModel';

/**
 * The InvoiceDetailsApiModel model module.
 * @module model/InvoiceDetailsApiModel
 * @version v1
 */
class InvoiceDetailsApiModel {
    /**
     * Constructs a new <code>InvoiceDetailsApiModel</code>.
     * @alias module:model/InvoiceDetailsApiModel
     */
    constructor() { 
        
        InvoiceDetailsApiModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>InvoiceDetailsApiModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InvoiceDetailsApiModel} obj Optional instance to populate.
     * @return {module:model/InvoiceDetailsApiModel} The populated <code>InvoiceDetailsApiModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InvoiceDetailsApiModel();

            if (data.hasOwnProperty('AccessToken')) {
                obj['AccessToken'] = ApiClient.convertToType(data['AccessToken'], 'String');
            }
            if (data.hasOwnProperty('Client')) {
                obj['Client'] = ClientDetailsApiModel.constructFromObject(data['Client']);
            }
            if (data.hasOwnProperty('ClonedFromId')) {
                obj['ClonedFromId'] = ApiClient.convertToType(data['ClonedFromId'], 'Number');
            }
            if (data.hasOwnProperty('Currency')) {
                obj['Currency'] = CurrencyDetailsApiModel.constructFromObject(data['Currency']);
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
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('InvoiceCategoryId')) {
                obj['InvoiceCategoryId'] = ApiClient.convertToType(data['InvoiceCategoryId'], 'Number');
            }
            if (data.hasOwnProperty('IssuedOn')) {
                obj['IssuedOn'] = ApiClient.convertToType(data['IssuedOn'], 'Date');
            }
            if (data.hasOwnProperty('Notes')) {
                obj['Notes'] = ApiClient.convertToType(data['Notes'], 'String');
            }
            if (data.hasOwnProperty('Number')) {
                obj['Number'] = ApiClient.convertToType(data['Number'], 'String');
            }
            if (data.hasOwnProperty('PoNumber')) {
                obj['PoNumber'] = ApiClient.convertToType(data['PoNumber'], 'String');
            }
            if (data.hasOwnProperty('RecurringProfile')) {
                obj['RecurringProfile'] = InvoiceRecurringApiModel.constructFromObject(data['RecurringProfile']);
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
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>InvoiceDetailsApiModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>InvoiceDetailsApiModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AccessToken'] && !(typeof data['AccessToken'] === 'string' || data['AccessToken'] instanceof String)) {
            throw new Error("Expected the field `AccessToken` to be a primitive type in the JSON string but got " + data['AccessToken']);
        }
        // validate the optional field `Client`
        if (data['Client']) { // data not null
          ClientDetailsApiModel.validateJSON(data['Client']);
        }
        // validate the optional field `Currency`
        if (data['Currency']) { // data not null
          CurrencyDetailsApiModel.validateJSON(data['Currency']);
        }
        // ensure the json data is a string
        if (data['Notes'] && !(typeof data['Notes'] === 'string' || data['Notes'] instanceof String)) {
            throw new Error("Expected the field `Notes` to be a primitive type in the JSON string but got " + data['Notes']);
        }
        // ensure the json data is a string
        if (data['Number'] && !(typeof data['Number'] === 'string' || data['Number'] instanceof String)) {
            throw new Error("Expected the field `Number` to be a primitive type in the JSON string but got " + data['Number']);
        }
        // ensure the json data is a string
        if (data['PoNumber'] && !(typeof data['PoNumber'] === 'string' || data['PoNumber'] instanceof String)) {
            throw new Error("Expected the field `PoNumber` to be a primitive type in the JSON string but got " + data['PoNumber']);
        }
        // validate the optional field `RecurringProfile`
        if (data['RecurringProfile']) { // data not null
          InvoiceRecurringApiModel.validateJSON(data['RecurringProfile']);
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
 * Security access token used for accessing the invoice anonymously
 * @member {String} AccessToken
 */
InvoiceDetailsApiModel.prototype['AccessToken'] = undefined;

/**
 * @member {module:model/ClientDetailsApiModel} Client
 */
InvoiceDetailsApiModel.prototype['Client'] = undefined;

/**
 * Indicate from which invoice this invoice has been cloned from
 * @member {Number} ClonedFromId
 */
InvoiceDetailsApiModel.prototype['ClonedFromId'] = undefined;

/**
 * @member {module:model/CurrencyDetailsApiModel} Currency
 */
InvoiceDetailsApiModel.prototype['Currency'] = undefined;

/**
 * Amount that goes as a discount
 * @member {Number} DiscountAmount
 */
InvoiceDetailsApiModel.prototype['DiscountAmount'] = undefined;

/**
 * Indicates when the invoice will be proclamed as due
 * @member {Date} Duedate
 */
InvoiceDetailsApiModel.prototype['Duedate'] = undefined;

/**
 * Indicate that the invoice allows the user to pay the invoice partially
 * @member {Boolean} EnablePartialPayments
 */
InvoiceDetailsApiModel.prototype['EnablePartialPayments'] = undefined;

/**
 * Invoice id
 * @member {Number} Id
 */
InvoiceDetailsApiModel.prototype['Id'] = undefined;

/**
 * Hold the id of the invoice category
 * @member {Number} InvoiceCategoryId
 */
InvoiceDetailsApiModel.prototype['InvoiceCategoryId'] = undefined;

/**
 * Indicates when the invoice was issued
 * @member {Date} IssuedOn
 */
InvoiceDetailsApiModel.prototype['IssuedOn'] = undefined;

/**
 * Internal note regarding the invoice
 * @member {String} Notes
 */
InvoiceDetailsApiModel.prototype['Notes'] = undefined;

/**
 * Unique invoice number
 * @member {String} Number
 */
InvoiceDetailsApiModel.prototype['Number'] = undefined;

/**
 * Unique number generated by the buyer
 * @member {String} PoNumber
 */
InvoiceDetailsApiModel.prototype['PoNumber'] = undefined;

/**
 * @member {module:model/InvoiceRecurringApiModel} RecurringProfile
 */
InvoiceDetailsApiModel.prototype['RecurringProfile'] = undefined;

/**
 * Hold the id of the recurring profile
 * @member {Number} RecurringProfileId
 */
InvoiceDetailsApiModel.prototype['RecurringProfileId'] = undefined;

/**
 * Should send email reminders to client?
 * @member {Boolean} ShouldSendReminders
 */
InvoiceDetailsApiModel.prototype['ShouldSendReminders'] = undefined;

/**
 * Indicate the status of the invoice (paid/unpaid/overdue)
 * @member {module:model/InvoiceDetailsApiModel.StatusEnum} Status
 */
InvoiceDetailsApiModel.prototype['Status'] = undefined;

/**
 * Total amount of the invoice without tax
 * @member {Number} SubTotalAmount
 */
InvoiceDetailsApiModel.prototype['SubTotalAmount'] = undefined;

/**
 * Amount that goes to the tax
 * @member {Number} TaxAmount
 */
InvoiceDetailsApiModel.prototype['TaxAmount'] = undefined;

/**
 * Terms of agreement
 * @member {String} Terms
 */
InvoiceDetailsApiModel.prototype['Terms'] = undefined;

/**
 * Total amount of the invoice with tax
 * @member {Number} TotalAmount
 */
InvoiceDetailsApiModel.prototype['TotalAmount'] = undefined;





/**
 * Allowed values for the <code>Status</code> property.
 * @enum {String}
 * @readonly
 */
InvoiceDetailsApiModel['StatusEnum'] = {

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



export default InvoiceDetailsApiModel;

