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
import ReturnV2Order from './ReturnV2Order';
import ReturnV2Reason from './ReturnV2Reason';
import RmaItemV2 from './RmaItemV2';
import UserV2 from './UserV2';

/**
 * The ReturnV2 model module.
 * @module model/ReturnV2
 * @version 2.0
 */
class ReturnV2 {
    /**
     * Constructs a new <code>ReturnV2</code>.
     * @alias module:model/ReturnV2
     * @param createdAt {Date} 
     * @param createdBy {Object} 
     * @param id {Number} 
     * @param reason {module:model/ReturnV2Reason} 
     * @param status {module:model/ReturnV2Reason} 
     * @param updatedAt {Date} 
     * @param updatedBy {module:model/UserV2} 
     */
    constructor(createdAt, createdBy, id, reason, status, updatedAt, updatedBy) { 
        
        ReturnV2.initialize(this, createdAt, createdBy, id, reason, status, updatedAt, updatedBy);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, createdAt, createdBy, id, reason, status, updatedAt, updatedBy) { 
        obj['createdAt'] = createdAt;
        obj['createdBy'] = createdBy;
        obj['id'] = id;
        obj['reason'] = reason;
        obj['status'] = status;
        obj['updatedAt'] = updatedAt;
        obj['updatedBy'] = updatedBy;
    }

    /**
     * Constructs a <code>ReturnV2</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ReturnV2} obj Optional instance to populate.
     * @return {module:model/ReturnV2} The populated <code>ReturnV2</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ReturnV2();

            if (data.hasOwnProperty('comments')) {
                obj['comments'] = ApiClient.convertToType(data['comments'], 'String');
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'Date');
            }
            if (data.hasOwnProperty('createdBy')) {
                obj['createdBy'] = Object.constructFromObject(data['createdBy']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('order')) {
                obj['order'] = ReturnV2Order.constructFromObject(data['order']);
            }
            if (data.hasOwnProperty('reason')) {
                obj['reason'] = ReturnV2Reason.constructFromObject(data['reason']);
            }
            if (data.hasOwnProperty('returnedBy')) {
                obj['returnedBy'] = ApiClient.convertToType(data['returnedBy'], 'String');
            }
            if (data.hasOwnProperty('rmaItems')) {
                obj['rmaItems'] = ApiClient.convertToType(data['rmaItems'], [RmaItemV2]);
            }
            if (data.hasOwnProperty('rmaNumber')) {
                obj['rmaNumber'] = ApiClient.convertToType(data['rmaNumber'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ReturnV2Reason.constructFromObject(data['status']);
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Date');
            }
            if (data.hasOwnProperty('updatedBy')) {
                obj['updatedBy'] = UserV2.constructFromObject(data['updatedBy']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ReturnV2</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ReturnV2</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ReturnV2.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['comments'] && !(typeof data['comments'] === 'string' || data['comments'] instanceof String)) {
            throw new Error("Expected the field `comments` to be a primitive type in the JSON string but got " + data['comments']);
        }
        // validate the optional field `order`
        if (data['order']) { // data not null
          ReturnV2Order.validateJSON(data['order']);
        }
        // validate the optional field `reason`
        if (data['reason']) { // data not null
          ReturnV2Reason.validateJSON(data['reason']);
        }
        // ensure the json data is a string
        if (data['returnedBy'] && !(typeof data['returnedBy'] === 'string' || data['returnedBy'] instanceof String)) {
            throw new Error("Expected the field `returnedBy` to be a primitive type in the JSON string but got " + data['returnedBy']);
        }
        if (data['rmaItems']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['rmaItems'])) {
                throw new Error("Expected the field `rmaItems` to be an array in the JSON data but got " + data['rmaItems']);
            }
            // validate the optional field `rmaItems` (array)
            for (const item of data['rmaItems']) {
                RmaItemV2.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['rmaNumber'] && !(typeof data['rmaNumber'] === 'string' || data['rmaNumber'] instanceof String)) {
            throw new Error("Expected the field `rmaNumber` to be a primitive type in the JSON string but got " + data['rmaNumber']);
        }
        // validate the optional field `status`
        if (data['status']) { // data not null
          ReturnV2Reason.validateJSON(data['status']);
        }
        // validate the optional field `updatedBy`
        if (data['updatedBy']) { // data not null
          UserV2.validateJSON(data['updatedBy']);
        }

        return true;
    }


}

ReturnV2.RequiredProperties = ["createdAt", "createdBy", "id", "reason", "status", "updatedAt", "updatedBy"];

/**
 * @member {String} comments
 */
ReturnV2.prototype['comments'] = undefined;

/**
 * @member {Date} createdAt
 */
ReturnV2.prototype['createdAt'] = undefined;

/**
 * @member {Object} createdBy
 */
ReturnV2.prototype['createdBy'] = undefined;

/**
 * @member {Number} id
 */
ReturnV2.prototype['id'] = undefined;

/**
 * @member {module:model/ReturnV2Order} order
 */
ReturnV2.prototype['order'] = undefined;

/**
 * @member {module:model/ReturnV2Reason} reason
 */
ReturnV2.prototype['reason'] = undefined;

/**
 * @member {String} returnedBy
 */
ReturnV2.prototype['returnedBy'] = undefined;

/**
 * @member {Array.<module:model/RmaItemV2>} rmaItems
 */
ReturnV2.prototype['rmaItems'] = undefined;

/**
 * @member {String} rmaNumber
 */
ReturnV2.prototype['rmaNumber'] = undefined;

/**
 * @member {module:model/ReturnV2Reason} status
 */
ReturnV2.prototype['status'] = undefined;

/**
 * @member {Date} updatedAt
 */
ReturnV2.prototype['updatedAt'] = undefined;

/**
 * @member {module:model/UserV2} updatedBy
 */
ReturnV2.prototype['updatedBy'] = undefined;






export default ReturnV2;

