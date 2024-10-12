/**
 * Fulfillment.com APIv2
 * Welcome to our current iteration of our REST API. While we encourage you to upgrade to v2.0 we will continue support for our [SOAP API](https://github.com/fulfillment/soap-integration).  # Versioning  The Fulfillment.com (FDC) REST API is version controlled and backwards compatible. We have many future APIs scheduled for publication within our v2.0 spec so please be prepared for us to add data nodes in our responses, however, we will not remove knowledge from previously published APIs.  #### A Current Response  ```javascript {   id: 123 } ```  #### A Potential Future Response  ```javascript {   id: 123,   reason: \"More Knowledge\" } ```  # Getting Started  We use OAuth v2.0 to authenticate clients, you can choose [implicit](https://oauth.net/2/grant-types/implicit/) or [password](https://oauth.net/2/grant-types/password/) grant type. To obtain an OAuth `client_id` and `client_secret` contact your account executive.  **Tip**: Generate an additional login and use those credentials for your integration so that changes are accredited to that \"user\".  You are now ready to make requests to our other APIs by filling your `Authorization` header with `Bearer {access_token}`.  ## Perpetuating Access  Perpetuating access to FDC without storing your password locally can be achieved using the `refresh_token` returned by [POST /oauth/access_token](#operation/generateToken).  A simple concept to achieve this is outlined below.  1. Your application/script will ask you for your `username` and `password`, your `client_id` and `client_secret` will be accessible via a DB or ENV. 2. [Request an access_token](#operation/generateToken)   + Your function should be capable of formatting your request for both a `grant_type` of \\\"password\\\" (step 1) and \\\"refresh_token\\\" (step 4). 3. Store the `access_token` and `refresh_token` so future requests can skip step 1 4. When the `access_token` expires request anew using your `refresh_token`, replace both tokens in local storage.  + If this fails you will have to revert to step 1.  Alternatively if you choose for your application/script to have access to your `username` and `password` you can skip step 4.  In all scenarios we recommend storing all credentials outside your codebase.  ## Date Time Definitions  We will report all date-time stamps using the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard. When using listing API's where fromDate and toDate are available note that both dates are inclusive while requiring the fromDate to be before or at the toDate.  ### The Fulfillment Process  Many steps are required to fulfill your order we report back to you three fundamental milestones inside the orders model.  * `recordedOn` When we received your order. This will never change.  * `dispatchDate` When the current iteration of your order was scheduled for fulfillment. This may change however it is an indicator that the physical process of fulfillment has begun and a tracking number has been **assigned** to your order. The tracking number **MAY CHANGE**. You will not be able to cancel an order once it has been dispatched. If you need to recall an order that has been dispatched please contact your account executive.  * `departDate` When we recorded your order passing our final inspection and placed with the carrier. At this point it is **safe to inform the consignee** of the tracking number as it will not change.  ## Evaluating Error Responses  We currently return two different error models, with and without context. All errors will include a `message` node while errors with `context` will include additional information designed to save you time when encountering highly probable errors. For example, when you send us a request to create a duplicate order, we will reject your request and the context will include the FDC order `id` so that you may record it for your records.  ### Without Context  New order with missing required fields.  | Header | Response | | ------ | -------- | | Status | `400 Bad Request` |  ```javascript {       \"message\": \"Invalid request body\" } ```  ### With Context  New order with duplicate `merchantOrderId`.  | Header | Response | | ------ | -------- | | Status | `409 Conflict` |  ```javascript {   \"message\": \"Duplicate Order\",   \"context\": {     \"id\": 123   } } ```  ## Status Codes  Codes are a concatenation of State, Stage, and Detail.  `^([0-9]{2})([0-9]{2})([0-9]{2})$`  | Code | State              | Stage    | Detail         | | ---- | ------------------ | -------- | -------------- | | 010101 | Processing Order | Recieved | Customer Order | | 010102 | Processing Order | Recieved | Recieved | | 010201 | Processing Order | Approved | | | 010301 | Processing Order | Hold | Merchant Stock | | 010302 | Processing Order | Hold | Merchant Funds | | 010303 | Processing Order | Hold | For Merchant | | 010304 | Processing Order | Hold | Oversized Shipment | | 010305 | Processing Order | Hold | Invalid Parent Order | | 010306 | Processing Order | Hold | Invalid Address | | 010307 | Processing Order | Hold | By Admin | | 010401 | Processing Order | Address Problem | Incomplete Address | | 010402 | Processing Order | Address Problem | Invalid Locality | | 010403 | Processing Order | Address Problem | Invalid Region | | 010404 | Processing Order | Address Problem | Address Not Found | | 010405 | Processing Order | Address Problem | Many Addresses Found | | 010406 | Processing Order | Address Problem | Invalid Postal Code | | 010407 | Processing Order | Address Problem | Country Not Mapped | | 010408 | Processing Order | Address Problem | Invalid Recipient Name | | 010409 | Processing Order | Address Problem | Bad UK Address | | 010410 | Processing Order | Address Problem | Invalid Address Line 1 or 2 | | 010501 | Processing Order | Sku Problem | Invalid SKU | | 010501 | Processing Order | Sku Problem | Child Order has Invalid SKUs | | 010601 | Processing Order | Facility Problem | Facility Not Mapped | | 010701 | Processing Order | Ship Method Problem | Unmapped Ship Method | | 010702 | Processing Order | Ship Method Problem | Unmapped Ship Cost | | 010703 | Processing Order | Ship Method Problem | Missing Ship Method | | 010704 | Processing Order | Ship Method Problem | Invalid Ship Method | | 010705 | Processing Order | Ship Method Problem | Order Weight Outside of Ship Method Weight | | 010801 | Processing Order | Inventory Problem | Insufficient Inventory In Facility | | 010802 | Processing Order | Inventory Problem | Issue Encountered During Inventory Adjustment | | 010901 | Processing Order | Released To WMS | Released | | 020101 | Fulfillment In Progress | Postage Problem | Address Issue | | 020102 | Fulfillment In Progress | Postage Problem | Postage OK, OMS Issue Occurred | | 020103 | Fulfillment In Progress | Postage Problem | Postage Void Failed | | 020201 | Fulfillment In Progress | Postage Acquired | | | 020301 | Fulfillment In Progress | Postage Voided | Postage Void Failed Gracefully | | 020301 | Fulfillment In Progress | Hold | Departure Hold Requested | | 020401 | Fulfillment In Progress | 4PL Processing | | | 020501 | Fulfillment In Progress | 4PL Problem | Order is Proccessable, Postage Issue Occurred | | 020601 | Fulfillment In Progress | Label Printed | | | 020701 | Fulfillment In Progress | Shipment Cubed | | | 020801 | Fulfillment In Progress | Picking Inventory | | | 020901 | Fulfillment In Progress | Label Print Verified | | | 021001 | Fulfillment In Progress | Passed Final Inspection | | | 030101 | Shipped | Fulfilled By 4PL | | | 030102 | Shipped | Fulfilled By 4PL | Successfully Fulfilled, OMS Encountered Issue During Processing | | 030201 | Shipped | Fulfilled By FDC | | | 040101 | Returned | Returned | | | 050101 | Cancelled | Cancelled | | | 060101 | Test | Test | Test | 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: dev@fulfillment.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ConsigneeV2 from './ConsigneeV2';
import MerchantV2 from './MerchantV2';
import OrderResponseV2ParentOrder from './OrderResponseV2ParentOrder';
import StatusEventV2 from './StatusEventV2';
import TrackingNumberV2 from './TrackingNumberV2';
import WarehouseV2 from './WarehouseV2';

/**
 * The OrderResponseV2 model module.
 * @module model/OrderResponseV2
 * @version 2.0
 */
class OrderResponseV2 {
    /**
     * Constructs a new <code>OrderResponseV2</code>.
     * @alias module:model/OrderResponseV2
     * @param currentStatus {module:model/StatusEventV2} 
     * @param id {Number} FDC ID for this order
     * @param merchant {module:model/MerchantV2} 
     * @param merchantOrderId {String} Merchant provided ID
     * @param merchantShippingMethod {String} Requested ship method
     * @param originalConsignee {module:model/ConsigneeV2} 
     * @param recordedOn {Date} DateTime order was recorded by FDC
     * @param validatedConsignee {Object} 
     */
    constructor(currentStatus, id, merchant, merchantOrderId, merchantShippingMethod, originalConsignee, recordedOn, validatedConsignee) { 
        
        OrderResponseV2.initialize(this, currentStatus, id, merchant, merchantOrderId, merchantShippingMethod, originalConsignee, recordedOn, validatedConsignee);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, currentStatus, id, merchant, merchantOrderId, merchantShippingMethod, originalConsignee, recordedOn, validatedConsignee) { 
        obj['currentStatus'] = currentStatus;
        obj['id'] = id;
        obj['merchant'] = merchant;
        obj['merchantOrderId'] = merchantOrderId;
        obj['merchantShippingMethod'] = merchantShippingMethod;
        obj['originalConsignee'] = originalConsignee;
        obj['recordedOn'] = recordedOn;
        obj['validatedConsignee'] = validatedConsignee;
    }

    /**
     * Constructs a <code>OrderResponseV2</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderResponseV2} obj Optional instance to populate.
     * @return {module:model/OrderResponseV2} The populated <code>OrderResponseV2</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderResponseV2();

            if (data.hasOwnProperty('currentStatus')) {
                obj['currentStatus'] = StatusEventV2.constructFromObject(data['currentStatus']);
            }
            if (data.hasOwnProperty('departDate')) {
                obj['departDate'] = ApiClient.convertToType(data['departDate'], 'Date');
            }
            if (data.hasOwnProperty('dispatchDate')) {
                obj['dispatchDate'] = ApiClient.convertToType(data['dispatchDate'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('merchant')) {
                obj['merchant'] = MerchantV2.constructFromObject(data['merchant']);
            }
            if (data.hasOwnProperty('merchantOrderId')) {
                obj['merchantOrderId'] = ApiClient.convertToType(data['merchantOrderId'], 'String');
            }
            if (data.hasOwnProperty('merchantShippingMethod')) {
                obj['merchantShippingMethod'] = ApiClient.convertToType(data['merchantShippingMethod'], 'String');
            }
            if (data.hasOwnProperty('originalConsignee')) {
                obj['originalConsignee'] = ConsigneeV2.constructFromObject(data['originalConsignee']);
            }
            if (data.hasOwnProperty('parentOrder')) {
                obj['parentOrder'] = OrderResponseV2ParentOrder.constructFromObject(data['parentOrder']);
            }
            if (data.hasOwnProperty('purchaseOrderNum')) {
                obj['purchaseOrderNum'] = ApiClient.convertToType(data['purchaseOrderNum'], 'String');
            }
            if (data.hasOwnProperty('recordedOn')) {
                obj['recordedOn'] = ApiClient.convertToType(data['recordedOn'], 'Date');
            }
            if (data.hasOwnProperty('trackingNumbers')) {
                obj['trackingNumbers'] = ApiClient.convertToType(data['trackingNumbers'], [TrackingNumberV2]);
            }
            if (data.hasOwnProperty('validatedConsignee')) {
                obj['validatedConsignee'] = Object.constructFromObject(data['validatedConsignee']);
            }
            if (data.hasOwnProperty('warehouse')) {
                obj['warehouse'] = WarehouseV2.constructFromObject(data['warehouse']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderResponseV2</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderResponseV2</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OrderResponseV2.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `currentStatus`
        if (data['currentStatus']) { // data not null
          StatusEventV2.validateJSON(data['currentStatus']);
        }
        // validate the optional field `merchant`
        if (data['merchant']) { // data not null
          MerchantV2.validateJSON(data['merchant']);
        }
        // ensure the json data is a string
        if (data['merchantOrderId'] && !(typeof data['merchantOrderId'] === 'string' || data['merchantOrderId'] instanceof String)) {
            throw new Error("Expected the field `merchantOrderId` to be a primitive type in the JSON string but got " + data['merchantOrderId']);
        }
        // ensure the json data is a string
        if (data['merchantShippingMethod'] && !(typeof data['merchantShippingMethod'] === 'string' || data['merchantShippingMethod'] instanceof String)) {
            throw new Error("Expected the field `merchantShippingMethod` to be a primitive type in the JSON string but got " + data['merchantShippingMethod']);
        }
        // validate the optional field `originalConsignee`
        if (data['originalConsignee']) { // data not null
          ConsigneeV2.validateJSON(data['originalConsignee']);
        }
        // validate the optional field `parentOrder`
        if (data['parentOrder']) { // data not null
          OrderResponseV2ParentOrder.validateJSON(data['parentOrder']);
        }
        // ensure the json data is a string
        if (data['purchaseOrderNum'] && !(typeof data['purchaseOrderNum'] === 'string' || data['purchaseOrderNum'] instanceof String)) {
            throw new Error("Expected the field `purchaseOrderNum` to be a primitive type in the JSON string but got " + data['purchaseOrderNum']);
        }
        if (data['trackingNumbers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['trackingNumbers'])) {
                throw new Error("Expected the field `trackingNumbers` to be an array in the JSON data but got " + data['trackingNumbers']);
            }
            // validate the optional field `trackingNumbers` (array)
            for (const item of data['trackingNumbers']) {
                TrackingNumberV2.validateJSON(item);
            };
        }
        // validate the optional field `warehouse`
        if (data['warehouse']) { // data not null
          WarehouseV2.validateJSON(data['warehouse']);
        }

        return true;
    }


}

OrderResponseV2.RequiredProperties = ["currentStatus", "id", "merchant", "merchantOrderId", "merchantShippingMethod", "originalConsignee", "recordedOn", "validatedConsignee"];

/**
 * @member {module:model/StatusEventV2} currentStatus
 */
OrderResponseV2.prototype['currentStatus'] = undefined;

/**
 * DateTime order departed an FDC warehouse
 * @member {Date} departDate
 */
OrderResponseV2.prototype['departDate'] = undefined;

/**
 * DateTime order was dispatched for fulfillment by FDC
 * @member {Date} dispatchDate
 */
OrderResponseV2.prototype['dispatchDate'] = undefined;

/**
 * FDC ID for this order
 * @member {Number} id
 */
OrderResponseV2.prototype['id'] = undefined;

/**
 * @member {module:model/MerchantV2} merchant
 */
OrderResponseV2.prototype['merchant'] = undefined;

/**
 * Merchant provided ID
 * @member {String} merchantOrderId
 */
OrderResponseV2.prototype['merchantOrderId'] = undefined;

/**
 * Requested ship method
 * @member {String} merchantShippingMethod
 */
OrderResponseV2.prototype['merchantShippingMethod'] = undefined;

/**
 * @member {module:model/ConsigneeV2} originalConsignee
 */
OrderResponseV2.prototype['originalConsignee'] = undefined;

/**
 * @member {module:model/OrderResponseV2ParentOrder} parentOrder
 */
OrderResponseV2.prototype['parentOrder'] = undefined;

/**
 * Merchant provided PO#
 * @member {String} purchaseOrderNum
 */
OrderResponseV2.prototype['purchaseOrderNum'] = undefined;

/**
 * DateTime order was recorded by FDC
 * @member {Date} recordedOn
 */
OrderResponseV2.prototype['recordedOn'] = undefined;

/**
 * @member {Array.<module:model/TrackingNumberV2>} trackingNumbers
 */
OrderResponseV2.prototype['trackingNumbers'] = undefined;

/**
 * @member {Object} validatedConsignee
 */
OrderResponseV2.prototype['validatedConsignee'] = undefined;

/**
 * @member {module:model/WarehouseV2} warehouse
 */
OrderResponseV2.prototype['warehouse'] = undefined;






export default OrderResponseV2;

