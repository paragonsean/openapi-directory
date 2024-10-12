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

/**
 * The Activity model module.
 * @module model/Activity
 * @version v1
 */
class Activity {
    /**
     * Constructs a new <code>Activity</code>.
     * @alias module:model/Activity
     */
    constructor() { 
        
        Activity.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Activity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Activity} obj Optional instance to populate.
     * @return {module:model/Activity} The populated <code>Activity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Activity();

            if (data.hasOwnProperty('EstimationId')) {
                obj['EstimationId'] = ApiClient.convertToType(data['EstimationId'], 'Number');
            }
            if (data.hasOwnProperty('EstimationNumber')) {
                obj['EstimationNumber'] = ApiClient.convertToType(data['EstimationNumber'], 'String');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('InvoiceId')) {
                obj['InvoiceId'] = ApiClient.convertToType(data['InvoiceId'], 'Number');
            }
            if (data.hasOwnProperty('InvoiceNumber')) {
                obj['InvoiceNumber'] = ApiClient.convertToType(data['InvoiceNumber'], 'String');
            }
            if (data.hasOwnProperty('Link')) {
                obj['Link'] = ApiClient.convertToType(data['Link'], 'String');
            }
            if (data.hasOwnProperty('Message')) {
                obj['Message'] = ApiClient.convertToType(data['Message'], 'String');
            }
            if (data.hasOwnProperty('OrderId')) {
                obj['OrderId'] = ApiClient.convertToType(data['OrderId'], 'Number');
            }
            if (data.hasOwnProperty('OrderNumber')) {
                obj['OrderNumber'] = ApiClient.convertToType(data['OrderNumber'], 'String');
            }
            if (data.hasOwnProperty('Type')) {
                obj['Type'] = ApiClient.convertToType(data['Type'], 'String');
            }
            if (data.hasOwnProperty('UserId')) {
                obj['UserId'] = ApiClient.convertToType(data['UserId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Activity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Activity</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['EstimationNumber'] && !(typeof data['EstimationNumber'] === 'string' || data['EstimationNumber'] instanceof String)) {
            throw new Error("Expected the field `EstimationNumber` to be a primitive type in the JSON string but got " + data['EstimationNumber']);
        }
        // ensure the json data is a string
        if (data['InvoiceNumber'] && !(typeof data['InvoiceNumber'] === 'string' || data['InvoiceNumber'] instanceof String)) {
            throw new Error("Expected the field `InvoiceNumber` to be a primitive type in the JSON string but got " + data['InvoiceNumber']);
        }
        // ensure the json data is a string
        if (data['Link'] && !(typeof data['Link'] === 'string' || data['Link'] instanceof String)) {
            throw new Error("Expected the field `Link` to be a primitive type in the JSON string but got " + data['Link']);
        }
        // ensure the json data is a string
        if (data['Message'] && !(typeof data['Message'] === 'string' || data['Message'] instanceof String)) {
            throw new Error("Expected the field `Message` to be a primitive type in the JSON string but got " + data['Message']);
        }
        // ensure the json data is a string
        if (data['OrderNumber'] && !(typeof data['OrderNumber'] === 'string' || data['OrderNumber'] instanceof String)) {
            throw new Error("Expected the field `OrderNumber` to be a primitive type in the JSON string but got " + data['OrderNumber']);
        }
        // ensure the json data is a string
        if (data['Type'] && !(typeof data['Type'] === 'string' || data['Type'] instanceof String)) {
            throw new Error("Expected the field `Type` to be a primitive type in the JSON string but got " + data['Type']);
        }

        return true;
    }


}



/**
 * @member {Number} EstimationId
 */
Activity.prototype['EstimationId'] = undefined;

/**
 * @member {String} EstimationNumber
 */
Activity.prototype['EstimationNumber'] = undefined;

/**
 * @member {Number} Id
 */
Activity.prototype['Id'] = undefined;

/**
 * @member {Number} InvoiceId
 */
Activity.prototype['InvoiceId'] = undefined;

/**
 * @member {String} InvoiceNumber
 */
Activity.prototype['InvoiceNumber'] = undefined;

/**
 * @member {String} Link
 */
Activity.prototype['Link'] = undefined;

/**
 * @member {String} Message
 */
Activity.prototype['Message'] = undefined;

/**
 * @member {Number} OrderId
 */
Activity.prototype['OrderId'] = undefined;

/**
 * @member {String} OrderNumber
 */
Activity.prototype['OrderNumber'] = undefined;

/**
 * @member {module:model/Activity.TypeEnum} Type
 */
Activity.prototype['Type'] = undefined;

/**
 * @member {Number} UserId
 */
Activity.prototype['UserId'] = undefined;





/**
 * Allowed values for the <code>Type</code> property.
 * @enum {String}
 * @readonly
 */
Activity['TypeEnum'] = {

    /**
     * value: "Created"
     * @const
     */
    "Created": "Created",

    /**
     * value: "Draft"
     * @const
     */
    "Draft": "Draft",

    /**
     * value: "Cloned"
     * @const
     */
    "Cloned": "Cloned",

    /**
     * value: "SentViaEmail"
     * @const
     */
    "SentViaEmail": "SentViaEmail",

    /**
     * value: "SentViaSms"
     * @const
     */
    "SentViaSms": "SentViaSms",

    /**
     * value: "SentReminderViaEmail"
     * @const
     */
    "SentReminderViaEmail": "SentReminderViaEmail",

    /**
     * value: "SentReminderViaSms"
     * @const
     */
    "SentReminderViaSms": "SentReminderViaSms",

    /**
     * value: "Opened"
     * @const
     */
    "Opened": "Opened",

    /**
     * value: "Viewed"
     * @const
     */
    "Viewed": "Viewed",

    /**
     * value: "Rejected"
     * @const
     */
    "Rejected": "Rejected",

    /**
     * value: "Updated"
     * @const
     */
    "Updated": "Updated",

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
     * value: "NewManualPayment"
     * @const
     */
    "NewManualPayment": "NewManualPayment",

    /**
     * value: "NewPaymentWithPaypal"
     * @const
     */
    "NewPaymentWithPaypal": "NewPaymentWithPaypal",

    /**
     * value: "NewPaymentWithStripe"
     * @const
     */
    "NewPaymentWithStripe": "NewPaymentWithStripe",

    /**
     * value: "NewPaymentWithPayoneer"
     * @const
     */
    "NewPaymentWithPayoneer": "NewPaymentWithPayoneer",

    /**
     * value: "SentToAccountant"
     * @const
     */
    "SentToAccountant": "SentToAccountant",

    /**
     * value: "DownloadedAsPdf"
     * @const
     */
    "DownloadedAsPdf": "DownloadedAsPdf",

    /**
     * value: "MarkAsPaidByTheClient"
     * @const
     */
    "MarkAsPaidByTheClient": "MarkAsPaidByTheClient",

    /**
     * value: "OpenedAttachment"
     * @const
     */
    "OpenedAttachment": "OpenedAttachment",

    /**
     * value: "NewPaymentWithSquare"
     * @const
     */
    "NewPaymentWithSquare": "NewPaymentWithSquare",

    /**
     * value: "NewPaymentWithKlikAndPay"
     * @const
     */
    "NewPaymentWithKlikAndPay": "NewPaymentWithKlikAndPay",

    /**
     * value: "NewPaymentWithRazorpay"
     * @const
     */
    "NewPaymentWithRazorpay": "NewPaymentWithRazorpay",

    /**
     * value: "NewPaymentWithWepay"
     * @const
     */
    "NewPaymentWithWepay": "NewPaymentWithWepay",

    /**
     * value: "NewPaymentWithHalkbank"
     * @const
     */
    "NewPaymentWithHalkbank": "NewPaymentWithHalkbank",

    /**
     * value: "ChangeStatus"
     * @const
     */
    "ChangeStatus": "ChangeStatus",

    /**
     * value: "OrderUpdated"
     * @const
     */
    "OrderUpdated": "OrderUpdated",

    /**
     * value: "OrderCreated"
     * @const
     */
    "OrderCreated": "OrderCreated",

    /**
     * value: "NewPaymentWithTwoCheckout"
     * @const
     */
    "NewPaymentWithTwoCheckout": "NewPaymentWithTwoCheckout",

    /**
     * value: "NewPaymentWithPaymentWall"
     * @const
     */
    "NewPaymentWithPaymentWall": "NewPaymentWithPaymentWall",

    /**
     * value: "NewPaymentWithBamboraEU"
     * @const
     */
    "NewPaymentWithBamboraEU": "NewPaymentWithBamboraEU",

    /**
     * value: "NewPaymentWithBamboraNA"
     * @const
     */
    "NewPaymentWithBamboraNA": "NewPaymentWithBamboraNA",

    /**
     * value: "Void"
     * @const
     */
    "Void": "Void",

    /**
     * value: "NewPaymentWithNlb"
     * @const
     */
    "NewPaymentWithNlb": "NewPaymentWithNlb",

    /**
     * value: "NewPaymentWithAuthorizeNet"
     * @const
     */
    "NewPaymentWithAuthorizeNet": "NewPaymentWithAuthorizeNet",

    /**
     * value: "NewPaymentWithBraintree"
     * @const
     */
    "NewPaymentWithBraintree": "NewPaymentWithBraintree",

    /**
     * value: "EstimationCreated"
     * @const
     */
    "EstimationCreated": "EstimationCreated",

    /**
     * value: "EstimationDraft"
     * @const
     */
    "EstimationDraft": "EstimationDraft",

    /**
     * value: "EstimationCloned"
     * @const
     */
    "EstimationCloned": "EstimationCloned",

    /**
     * value: "EstimationSentViaEmail"
     * @const
     */
    "EstimationSentViaEmail": "EstimationSentViaEmail",

    /**
     * value: "EstimationOpened"
     * @const
     */
    "EstimationOpened": "EstimationOpened",

    /**
     * value: "EstimationViewed"
     * @const
     */
    "EstimationViewed": "EstimationViewed",

    /**
     * value: "EstimationAccepted"
     * @const
     */
    "EstimationAccepted": "EstimationAccepted",

    /**
     * value: "EstimationRejected"
     * @const
     */
    "EstimationRejected": "EstimationRejected",

    /**
     * value: "EstimationUpdated"
     * @const
     */
    "EstimationUpdated": "EstimationUpdated",

    /**
     * value: "EstimationDownloadedAsPdf"
     * @const
     */
    "EstimationDownloadedAsPdf": "EstimationDownloadedAsPdf",

    /**
     * value: "InvoiceDigitallySigned"
     * @const
     */
    "InvoiceDigitallySigned": "InvoiceDigitallySigned"
};



export default Activity;

