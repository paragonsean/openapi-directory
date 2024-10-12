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
import CurrencyDetailsApiModel from './CurrencyDetailsApiModel';
import OrderAttachmentApiModel from './OrderAttachmentApiModel';
import OrderBillingDetailsApiModel from './OrderBillingDetailsApiModel';
import OrderItemApiModel from './OrderItemApiModel';
import OrderShippingDetailsApiModel from './OrderShippingDetailsApiModel';

/**
 * The OrderFullDetailsApiModel model module.
 * @module model/OrderFullDetailsApiModel
 * @version v1
 */
class OrderFullDetailsApiModel {
    /**
     * Constructs a new <code>OrderFullDetailsApiModel</code>.
     * @alias module:model/OrderFullDetailsApiModel
     */
    constructor() { 
        
        OrderFullDetailsApiModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrderFullDetailsApiModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderFullDetailsApiModel} obj Optional instance to populate.
     * @return {module:model/OrderFullDetailsApiModel} The populated <code>OrderFullDetailsApiModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderFullDetailsApiModel();

            if (data.hasOwnProperty('AccessToken')) {
                obj['AccessToken'] = ApiClient.convertToType(data['AccessToken'], 'String');
            }
            if (data.hasOwnProperty('AfterPaymentDescription')) {
                obj['AfterPaymentDescription'] = ApiClient.convertToType(data['AfterPaymentDescription'], 'String');
            }
            if (data.hasOwnProperty('Attachments')) {
                obj['Attachments'] = ApiClient.convertToType(data['Attachments'], [OrderAttachmentApiModel]);
            }
            if (data.hasOwnProperty('CouponCode')) {
                obj['CouponCode'] = ApiClient.convertToType(data['CouponCode'], 'String');
            }
            if (data.hasOwnProperty('Currency')) {
                obj['Currency'] = CurrencyDetailsApiModel.constructFromObject(data['Currency']);
            }
            if (data.hasOwnProperty('CurrencyId')) {
                obj['CurrencyId'] = ApiClient.convertToType(data['CurrencyId'], 'Number');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('DiscountAmount')) {
                obj['DiscountAmount'] = ApiClient.convertToType(data['DiscountAmount'], 'Number');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('Items')) {
                obj['Items'] = ApiClient.convertToType(data['Items'], [OrderItemApiModel]);
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('Note')) {
                obj['Note'] = ApiClient.convertToType(data['Note'], 'String');
            }
            if (data.hasOwnProperty('OrderBillingDetails')) {
                obj['OrderBillingDetails'] = OrderBillingDetailsApiModel.constructFromObject(data['OrderBillingDetails']);
            }
            if (data.hasOwnProperty('OrderShippingDetails')) {
                obj['OrderShippingDetails'] = OrderShippingDetailsApiModel.constructFromObject(data['OrderShippingDetails']);
            }
            if (data.hasOwnProperty('ProductId')) {
                obj['ProductId'] = ApiClient.convertToType(data['ProductId'], 'Number');
            }
            if (data.hasOwnProperty('Referral')) {
                obj['Referral'] = ApiClient.convertToType(data['Referral'], 'String');
            }
            if (data.hasOwnProperty('ShippingAmount')) {
                obj['ShippingAmount'] = ApiClient.convertToType(data['ShippingAmount'], 'Number');
            }
            if (data.hasOwnProperty('ShippingDescription')) {
                obj['ShippingDescription'] = ApiClient.convertToType(data['ShippingDescription'], 'String');
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
            if (data.hasOwnProperty('TotalAmount')) {
                obj['TotalAmount'] = ApiClient.convertToType(data['TotalAmount'], 'Number');
            }
            if (data.hasOwnProperty('TotalWithShipping')) {
                obj['TotalWithShipping'] = ApiClient.convertToType(data['TotalWithShipping'], 'Number');
            }
            if (data.hasOwnProperty('WhatHappensNextDescription')) {
                obj['WhatHappensNextDescription'] = ApiClient.convertToType(data['WhatHappensNextDescription'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderFullDetailsApiModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderFullDetailsApiModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AccessToken'] && !(typeof data['AccessToken'] === 'string' || data['AccessToken'] instanceof String)) {
            throw new Error("Expected the field `AccessToken` to be a primitive type in the JSON string but got " + data['AccessToken']);
        }
        // ensure the json data is a string
        if (data['AfterPaymentDescription'] && !(typeof data['AfterPaymentDescription'] === 'string' || data['AfterPaymentDescription'] instanceof String)) {
            throw new Error("Expected the field `AfterPaymentDescription` to be a primitive type in the JSON string but got " + data['AfterPaymentDescription']);
        }
        if (data['Attachments']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Attachments'])) {
                throw new Error("Expected the field `Attachments` to be an array in the JSON data but got " + data['Attachments']);
            }
            // validate the optional field `Attachments` (array)
            for (const item of data['Attachments']) {
                OrderAttachmentApiModel.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['CouponCode'] && !(typeof data['CouponCode'] === 'string' || data['CouponCode'] instanceof String)) {
            throw new Error("Expected the field `CouponCode` to be a primitive type in the JSON string but got " + data['CouponCode']);
        }
        // validate the optional field `Currency`
        if (data['Currency']) { // data not null
          CurrencyDetailsApiModel.validateJSON(data['Currency']);
        }
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }
        if (data['Items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Items'])) {
                throw new Error("Expected the field `Items` to be an array in the JSON data but got " + data['Items']);
            }
            // validate the optional field `Items` (array)
            for (const item of data['Items']) {
                OrderItemApiModel.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['Note'] && !(typeof data['Note'] === 'string' || data['Note'] instanceof String)) {
            throw new Error("Expected the field `Note` to be a primitive type in the JSON string but got " + data['Note']);
        }
        // validate the optional field `OrderBillingDetails`
        if (data['OrderBillingDetails']) { // data not null
          OrderBillingDetailsApiModel.validateJSON(data['OrderBillingDetails']);
        }
        // validate the optional field `OrderShippingDetails`
        if (data['OrderShippingDetails']) { // data not null
          OrderShippingDetailsApiModel.validateJSON(data['OrderShippingDetails']);
        }
        // ensure the json data is a string
        if (data['Referral'] && !(typeof data['Referral'] === 'string' || data['Referral'] instanceof String)) {
            throw new Error("Expected the field `Referral` to be a primitive type in the JSON string but got " + data['Referral']);
        }
        // ensure the json data is a string
        if (data['ShippingDescription'] && !(typeof data['ShippingDescription'] === 'string' || data['ShippingDescription'] instanceof String)) {
            throw new Error("Expected the field `ShippingDescription` to be a primitive type in the JSON string but got " + data['ShippingDescription']);
        }
        // ensure the json data is a string
        if (data['Status'] && !(typeof data['Status'] === 'string' || data['Status'] instanceof String)) {
            throw new Error("Expected the field `Status` to be a primitive type in the JSON string but got " + data['Status']);
        }
        // ensure the json data is a string
        if (data['WhatHappensNextDescription'] && !(typeof data['WhatHappensNextDescription'] === 'string' || data['WhatHappensNextDescription'] instanceof String)) {
            throw new Error("Expected the field `WhatHappensNextDescription` to be a primitive type in the JSON string but got " + data['WhatHappensNextDescription']);
        }

        return true;
    }


}



/**
 * Product short link
 * @member {String} AccessToken
 */
OrderFullDetailsApiModel.prototype['AccessToken'] = undefined;

/**
 * After payment description
 * @member {String} AfterPaymentDescription
 */
OrderFullDetailsApiModel.prototype['AfterPaymentDescription'] = undefined;

/**
 * List of Order attachments
 * @member {Array.<module:model/OrderAttachmentApiModel>} Attachments
 */
OrderFullDetailsApiModel.prototype['Attachments'] = undefined;

/**
 * Coupon to apply in order to get the discount
 * @member {String} CouponCode
 */
OrderFullDetailsApiModel.prototype['CouponCode'] = undefined;

/**
 * @member {module:model/CurrencyDetailsApiModel} Currency
 */
OrderFullDetailsApiModel.prototype['Currency'] = undefined;

/**
 * Foreign key Currency
 * @member {Number} CurrencyId
 */
OrderFullDetailsApiModel.prototype['CurrencyId'] = undefined;

/**
 * Product description
 * @member {String} Description
 */
OrderFullDetailsApiModel.prototype['Description'] = undefined;

/**
 * Discount amount
 * @member {Number} DiscountAmount
 */
OrderFullDetailsApiModel.prototype['DiscountAmount'] = undefined;

/**
 * Order id
 * @member {Number} Id
 */
OrderFullDetailsApiModel.prototype['Id'] = undefined;

/**
 * List of Order items
 * @member {Array.<module:model/OrderItemApiModel>} Items
 */
OrderFullDetailsApiModel.prototype['Items'] = undefined;

/**
 * Product alias
 * @member {String} Name
 */
OrderFullDetailsApiModel.prototype['Name'] = undefined;

/**
 * Customer note to seller
 * @member {String} Note
 */
OrderFullDetailsApiModel.prototype['Note'] = undefined;

/**
 * @member {module:model/OrderBillingDetailsApiModel} OrderBillingDetails
 */
OrderFullDetailsApiModel.prototype['OrderBillingDetails'] = undefined;

/**
 * @member {module:model/OrderShippingDetailsApiModel} OrderShippingDetails
 */
OrderFullDetailsApiModel.prototype['OrderShippingDetails'] = undefined;

/**
 * Product id
 * @member {Number} ProductId
 */
OrderFullDetailsApiModel.prototype['ProductId'] = undefined;

/**
 * Represent the referral for this order
 * @member {String} Referral
 */
OrderFullDetailsApiModel.prototype['Referral'] = undefined;

/**
 * Cost for shipping the product
 * @member {Number} ShippingAmount
 */
OrderFullDetailsApiModel.prototype['ShippingAmount'] = undefined;

/**
 * Client instructions for shipping
 * @member {String} ShippingDescription
 */
OrderFullDetailsApiModel.prototype['ShippingDescription'] = undefined;

/**
 * Order status
 * @member {module:model/OrderFullDetailsApiModel.StatusEnum} Status
 */
OrderFullDetailsApiModel.prototype['Status'] = undefined;

/**
 * Sub total amount
 * @member {Number} SubTotalAmount
 */
OrderFullDetailsApiModel.prototype['SubTotalAmount'] = undefined;

/**
 * Tax amount
 * @member {Number} TaxAmount
 */
OrderFullDetailsApiModel.prototype['TaxAmount'] = undefined;

/**
 * Total amount
 * @member {Number} TotalAmount
 */
OrderFullDetailsApiModel.prototype['TotalAmount'] = undefined;

/**
 * Total amount with shipping
 * @member {Number} TotalWithShipping
 */
OrderFullDetailsApiModel.prototype['TotalWithShipping'] = undefined;

/**
 * What happens next description
 * @member {String} WhatHappensNextDescription
 */
OrderFullDetailsApiModel.prototype['WhatHappensNextDescription'] = undefined;





/**
 * Allowed values for the <code>Status</code> property.
 * @enum {String}
 * @readonly
 */
OrderFullDetailsApiModel['StatusEnum'] = {

    /**
     * value: "PendingPayment"
     * @const
     */
    "PendingPayment": "PendingPayment",

    /**
     * value: "Processing"
     * @const
     */
    "Processing": "Processing",

    /**
     * value: "Shipped"
     * @const
     */
    "Shipped": "Shipped",

    /**
     * value: "Completed"
     * @const
     */
    "Completed": "Completed",

    /**
     * value: "OnHold"
     * @const
     */
    "OnHold": "OnHold",

    /**
     * value: "Cancelled"
     * @const
     */
    "Cancelled": "Cancelled",

    /**
     * value: "Refunded"
     * @const
     */
    "Refunded": "Refunded",

    /**
     * value: "Failed"
     * @const
     */
    "Failed": "Failed"
};



export default OrderFullDetailsApiModel;

