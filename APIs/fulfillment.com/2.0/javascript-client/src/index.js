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


import ApiClient from './ApiClient';
import AccessTokenRequestPasswordV2 from './model/AccessTokenRequestPasswordV2';
import AccessTokenRequestRefreshV2 from './model/AccessTokenRequestRefreshV2';
import AccessTokenRequestV2 from './model/AccessTokenRequestV2';
import AccessTokenResponseV2 from './model/AccessTokenResponseV2';
import AccountingArrayV2 from './model/AccountingArrayV2';
import AccountingArrayV2Meta from './model/AccountingArrayV2Meta';
import AccountingV2 from './model/AccountingV2';
import AccountingV2Fees from './model/AccountingV2Fees';
import AccountingV2ItemsInner from './model/AccountingV2ItemsInner';
import AccountingV2Merchant from './model/AccountingV2Merchant';
import AccountingV2Order from './model/AccountingV2Order';
import AccountingV2Warehouse from './model/AccountingV2Warehouse';
import CarrierHydratedV2 from './model/CarrierHydratedV2';
import CarrierSimpleV2 from './model/CarrierSimpleV2';
import ConsigneeNewV2 from './model/ConsigneeNewV2';
import ConsigneeV2 from './model/ConsigneeV2';
import ErrorStandardV2 from './model/ErrorStandardV2';
import ErrorStandardWithContextV2 from './model/ErrorStandardWithContextV2';
import Feature from './model/Feature';
import FeatureProperties from './model/FeatureProperties';
import Geometry from './model/Geometry';
import GeometryCoordinates from './model/GeometryCoordinates';
import IsoCountryV2 from './model/IsoCountryV2';
import ItemInventoryArrayV2 from './model/ItemInventoryArrayV2';
import ItemInventoryV2 from './model/ItemInventoryV2';
import ItemInventoryV2Item from './model/ItemInventoryV2Item';
import ItemInventoryV2Merchant from './model/ItemInventoryV2Merchant';
import ItemInventoryV2Quantity from './model/ItemInventoryV2Quantity';
import ItemInventoryV2QuantityTotal from './model/ItemInventoryV2QuantityTotal';
import LineItemsResponseV2 from './model/LineItemsResponseV2';
import LineItemsResponseV2InventoryDetailsInner from './model/LineItemsResponseV2InventoryDetailsInner';
import LineItemsResponseV2LineDetails from './model/LineItemsResponseV2LineDetails';
import LineItemsResponseV2RequestedSkuData from './model/LineItemsResponseV2RequestedSkuData';
import MerchantV2 from './model/MerchantV2';
import OrderRequestV2 from './model/OrderRequestV2';
import OrderRequestV2ItemsInner from './model/OrderRequestV2ItemsInner';
import OrderRequestV2Warehouse from './model/OrderRequestV2Warehouse';
import OrderResponseHydrateV2 from './model/OrderResponseHydrateV2';
import OrderResponseHydrateV2AllOfTrackingNumbersInner from './model/OrderResponseHydrateV2AllOfTrackingNumbersInner';
import OrderResponseOneOfV2 from './model/OrderResponseOneOfV2';
import OrderResponseV2 from './model/OrderResponseV2';
import OrderResponseV2ParentOrder from './model/OrderResponseV2ParentOrder';
import OrderShipV2 from './model/OrderShipV2';
import PaginationV2 from './model/PaginationV2';
import ReturnV2 from './model/ReturnV2';
import ReturnV2Order from './model/ReturnV2Order';
import ReturnV2Reason from './model/ReturnV2Reason';
import ReturnsArrayV2 from './model/ReturnsArrayV2';
import RmaItemV2 from './model/RmaItemV2';
import RmaItemV2Item from './model/RmaItemV2Item';
import RmaItemV2NonRestockedReason from './model/RmaItemV2NonRestockedReason';
import RmaRequestV2 from './model/RmaRequestV2';
import RmaRequestV2ItemsInner from './model/RmaRequestV2ItemsInner';
import RmaResponseV2 from './model/RmaResponseV2';
import StatusEventV2 from './model/StatusEventV2';
import StatusTypeSimpleV2 from './model/StatusTypeSimpleV2';
import StatusTypeSimpleV2Status from './model/StatusTypeSimpleV2Status';
import StatusTypeV2 from './model/StatusTypeV2';
import StatusTypeV2ActionRequiredBy from './model/StatusTypeV2ActionRequiredBy';
import StatusTypeV2Stage from './model/StatusTypeV2Stage';
import TrackingEventV2 from './model/TrackingEventV2';
import TrackingNumberV2 from './model/TrackingNumberV2';
import TrackingResponse from './model/TrackingResponse';
import UserContactV2 from './model/UserContactV2';
import UserContactV2Merchant from './model/UserContactV2Merchant';
import UserV2 from './model/UserV2';
import WarehouseV2 from './model/WarehouseV2';
import AccountingApi from './api/AccountingApi';
import AuthApi from './api/AuthApi';
import InventoryApi from './api/InventoryApi';
import OrdersApi from './api/OrdersApi';
import PartnersApi from './api/PartnersApi';
import ReturnsApi from './api/ReturnsApi';
import TrackingApi from './api/TrackingApi';
import UsersApi from './api/UsersApi';


/**
* Welcome to our current iteration of our REST API. While we encourage you to upgrade to v2.0 we will continue support for our [SOAP API](https://github.com/fulfillment/soap-integration).  # Versioning  The Fulfillment.com (FDC) REST API is version controlled and backwards compatible. We have many future APIs scheduled for publication within our v2.0 spec so please be prepared for us to add data nodes in our responses, however, we will not remove knowledge from previously published APIs.  #### A Current Response  &#x60;&#x60;&#x60;javascript {   id: 123 } &#x60;&#x60;&#x60;  #### A Potential Future Response  &#x60;&#x60;&#x60;javascript {   id: 123,   reason: \&quot;More Knowledge\&quot; } &#x60;&#x60;&#x60;  # Getting Started  We use OAuth v2.0 to authenticate clients, you can choose [implicit](https://oauth.net/2/grant-types/implicit/) or [password](https://oauth.net/2/grant-types/password/) grant type. To obtain an OAuth &#x60;client_id&#x60; and &#x60;client_secret&#x60; contact your account executive.  **Tip**: Generate an additional login and use those credentials for your integration so that changes are accredited to that \&quot;user\&quot;.  You are now ready to make requests to our other APIs by filling your &#x60;Authorization&#x60; header with &#x60;Bearer {access_token}&#x60;.  ## Perpetuating Access  Perpetuating access to FDC without storing your password locally can be achieved using the &#x60;refresh_token&#x60; returned by [POST /oauth/access_token](#operation/generateToken).  A simple concept to achieve this is outlined below.  1. Your application/script will ask you for your &#x60;username&#x60; and &#x60;password&#x60;, your &#x60;client_id&#x60; and &#x60;client_secret&#x60; will be accessible via a DB or ENV. 2. [Request an access_token](#operation/generateToken)   + Your function should be capable of formatting your request for both a &#x60;grant_type&#x60; of \\\&quot;password\\\&quot; (step 1) and \\\&quot;refresh_token\\\&quot; (step 4). 3. Store the &#x60;access_token&#x60; and &#x60;refresh_token&#x60; so future requests can skip step 1 4. When the &#x60;access_token&#x60; expires request anew using your &#x60;refresh_token&#x60;, replace both tokens in local storage.  + If this fails you will have to revert to step 1.  Alternatively if you choose for your application/script to have access to your &#x60;username&#x60; and &#x60;password&#x60; you can skip step 4.  In all scenarios we recommend storing all credentials outside your codebase.  ## Date Time Definitions  We will report all date-time stamps using the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard. When using listing API&#39;s where fromDate and toDate are available note that both dates are inclusive while requiring the fromDate to be before or at the toDate.  ### The Fulfillment Process  Many steps are required to fulfill your order we report back to you three fundamental milestones inside the orders model.  * &#x60;recordedOn&#x60; When we received your order. This will never change.  * &#x60;dispatchDate&#x60; When the current iteration of your order was scheduled for fulfillment. This may change however it is an indicator that the physical process of fulfillment has begun and a tracking number has been **assigned** to your order. The tracking number **MAY CHANGE**. You will not be able to cancel an order once it has been dispatched. If you need to recall an order that has been dispatched please contact your account executive.  * &#x60;departDate&#x60; When we recorded your order passing our final inspection and placed with the carrier. At this point it is **safe to inform the consignee** of the tracking number as it will not change.  ## Evaluating Error Responses  We currently return two different error models, with and without context. All errors will include a &#x60;message&#x60; node while errors with &#x60;context&#x60; will include additional information designed to save you time when encountering highly probable errors. For example, when you send us a request to create a duplicate order, we will reject your request and the context will include the FDC order &#x60;id&#x60; so that you may record it for your records.  ### Without Context  New order with missing required fields.  | Header | Response | | ------ | -------- | | Status | &#x60;400 Bad Request&#x60; |  &#x60;&#x60;&#x60;javascript {       \&quot;message\&quot;: \&quot;Invalid request body\&quot; } &#x60;&#x60;&#x60;  ### With Context  New order with duplicate &#x60;merchantOrderId&#x60;.  | Header | Response | | ------ | -------- | | Status | &#x60;409 Conflict&#x60; |  &#x60;&#x60;&#x60;javascript {   \&quot;message\&quot;: \&quot;Duplicate Order\&quot;,   \&quot;context\&quot;: {     \&quot;id\&quot;: 123   } } &#x60;&#x60;&#x60;  ## Status Codes  Codes are a concatenation of State, Stage, and Detail.  &#x60;^([0-9]{2})([0-9]{2})([0-9]{2})$&#x60;  | Code | State              | Stage    | Detail         | | ---- | ------------------ | -------- | -------------- | | 010101 | Processing Order | Recieved | Customer Order | | 010102 | Processing Order | Recieved | Recieved | | 010201 | Processing Order | Approved | | | 010301 | Processing Order | Hold | Merchant Stock | | 010302 | Processing Order | Hold | Merchant Funds | | 010303 | Processing Order | Hold | For Merchant | | 010304 | Processing Order | Hold | Oversized Shipment | | 010305 | Processing Order | Hold | Invalid Parent Order | | 010306 | Processing Order | Hold | Invalid Address | | 010307 | Processing Order | Hold | By Admin | | 010401 | Processing Order | Address Problem | Incomplete Address | | 010402 | Processing Order | Address Problem | Invalid Locality | | 010403 | Processing Order | Address Problem | Invalid Region | | 010404 | Processing Order | Address Problem | Address Not Found | | 010405 | Processing Order | Address Problem | Many Addresses Found | | 010406 | Processing Order | Address Problem | Invalid Postal Code | | 010407 | Processing Order | Address Problem | Country Not Mapped | | 010408 | Processing Order | Address Problem | Invalid Recipient Name | | 010409 | Processing Order | Address Problem | Bad UK Address | | 010410 | Processing Order | Address Problem | Invalid Address Line 1 or 2 | | 010501 | Processing Order | Sku Problem | Invalid SKU | | 010501 | Processing Order | Sku Problem | Child Order has Invalid SKUs | | 010601 | Processing Order | Facility Problem | Facility Not Mapped | | 010701 | Processing Order | Ship Method Problem | Unmapped Ship Method | | 010702 | Processing Order | Ship Method Problem | Unmapped Ship Cost | | 010703 | Processing Order | Ship Method Problem | Missing Ship Method | | 010704 | Processing Order | Ship Method Problem | Invalid Ship Method | | 010705 | Processing Order | Ship Method Problem | Order Weight Outside of Ship Method Weight | | 010801 | Processing Order | Inventory Problem | Insufficient Inventory In Facility | | 010802 | Processing Order | Inventory Problem | Issue Encountered During Inventory Adjustment | | 010901 | Processing Order | Released To WMS | Released | | 020101 | Fulfillment In Progress | Postage Problem | Address Issue | | 020102 | Fulfillment In Progress | Postage Problem | Postage OK, OMS Issue Occurred | | 020103 | Fulfillment In Progress | Postage Problem | Postage Void Failed | | 020201 | Fulfillment In Progress | Postage Acquired | | | 020301 | Fulfillment In Progress | Postage Voided | Postage Void Failed Gracefully | | 020301 | Fulfillment In Progress | Hold | Departure Hold Requested | | 020401 | Fulfillment In Progress | 4PL Processing | | | 020501 | Fulfillment In Progress | 4PL Problem | Order is Proccessable, Postage Issue Occurred | | 020601 | Fulfillment In Progress | Label Printed | | | 020701 | Fulfillment In Progress | Shipment Cubed | | | 020801 | Fulfillment In Progress | Picking Inventory | | | 020901 | Fulfillment In Progress | Label Print Verified | | | 021001 | Fulfillment In Progress | Passed Final Inspection | | | 030101 | Shipped | Fulfilled By 4PL | | | 030102 | Shipped | Fulfilled By 4PL | Successfully Fulfilled, OMS Encountered Issue During Processing | | 030201 | Shipped | Fulfilled By FDC | | | 040101 | Returned | Returned | | | 050101 | Cancelled | Cancelled | | | 060101 | Test | Test | Test | .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var FulfillmentComApiv2 = require('index'); // See note below*.
* var xxxSvc = new FulfillmentComApiv2.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new FulfillmentComApiv2.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new FulfillmentComApiv2.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new FulfillmentComApiv2.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AccessTokenRequestPasswordV2 model constructor.
     * @property {module:model/AccessTokenRequestPasswordV2}
     */
    AccessTokenRequestPasswordV2,

    /**
     * The AccessTokenRequestRefreshV2 model constructor.
     * @property {module:model/AccessTokenRequestRefreshV2}
     */
    AccessTokenRequestRefreshV2,

    /**
     * The AccessTokenRequestV2 model constructor.
     * @property {module:model/AccessTokenRequestV2}
     */
    AccessTokenRequestV2,

    /**
     * The AccessTokenResponseV2 model constructor.
     * @property {module:model/AccessTokenResponseV2}
     */
    AccessTokenResponseV2,

    /**
     * The AccountingArrayV2 model constructor.
     * @property {module:model/AccountingArrayV2}
     */
    AccountingArrayV2,

    /**
     * The AccountingArrayV2Meta model constructor.
     * @property {module:model/AccountingArrayV2Meta}
     */
    AccountingArrayV2Meta,

    /**
     * The AccountingV2 model constructor.
     * @property {module:model/AccountingV2}
     */
    AccountingV2,

    /**
     * The AccountingV2Fees model constructor.
     * @property {module:model/AccountingV2Fees}
     */
    AccountingV2Fees,

    /**
     * The AccountingV2ItemsInner model constructor.
     * @property {module:model/AccountingV2ItemsInner}
     */
    AccountingV2ItemsInner,

    /**
     * The AccountingV2Merchant model constructor.
     * @property {module:model/AccountingV2Merchant}
     */
    AccountingV2Merchant,

    /**
     * The AccountingV2Order model constructor.
     * @property {module:model/AccountingV2Order}
     */
    AccountingV2Order,

    /**
     * The AccountingV2Warehouse model constructor.
     * @property {module:model/AccountingV2Warehouse}
     */
    AccountingV2Warehouse,

    /**
     * The CarrierHydratedV2 model constructor.
     * @property {module:model/CarrierHydratedV2}
     */
    CarrierHydratedV2,

    /**
     * The CarrierSimpleV2 model constructor.
     * @property {module:model/CarrierSimpleV2}
     */
    CarrierSimpleV2,

    /**
     * The ConsigneeNewV2 model constructor.
     * @property {module:model/ConsigneeNewV2}
     */
    ConsigneeNewV2,

    /**
     * The ConsigneeV2 model constructor.
     * @property {module:model/ConsigneeV2}
     */
    ConsigneeV2,

    /**
     * The ErrorStandardV2 model constructor.
     * @property {module:model/ErrorStandardV2}
     */
    ErrorStandardV2,

    /**
     * The ErrorStandardWithContextV2 model constructor.
     * @property {module:model/ErrorStandardWithContextV2}
     */
    ErrorStandardWithContextV2,

    /**
     * The Feature model constructor.
     * @property {module:model/Feature}
     */
    Feature,

    /**
     * The FeatureProperties model constructor.
     * @property {module:model/FeatureProperties}
     */
    FeatureProperties,

    /**
     * The Geometry model constructor.
     * @property {module:model/Geometry}
     */
    Geometry,

    /**
     * The GeometryCoordinates model constructor.
     * @property {module:model/GeometryCoordinates}
     */
    GeometryCoordinates,

    /**
     * The IsoCountryV2 model constructor.
     * @property {module:model/IsoCountryV2}
     */
    IsoCountryV2,

    /**
     * The ItemInventoryArrayV2 model constructor.
     * @property {module:model/ItemInventoryArrayV2}
     */
    ItemInventoryArrayV2,

    /**
     * The ItemInventoryV2 model constructor.
     * @property {module:model/ItemInventoryV2}
     */
    ItemInventoryV2,

    /**
     * The ItemInventoryV2Item model constructor.
     * @property {module:model/ItemInventoryV2Item}
     */
    ItemInventoryV2Item,

    /**
     * The ItemInventoryV2Merchant model constructor.
     * @property {module:model/ItemInventoryV2Merchant}
     */
    ItemInventoryV2Merchant,

    /**
     * The ItemInventoryV2Quantity model constructor.
     * @property {module:model/ItemInventoryV2Quantity}
     */
    ItemInventoryV2Quantity,

    /**
     * The ItemInventoryV2QuantityTotal model constructor.
     * @property {module:model/ItemInventoryV2QuantityTotal}
     */
    ItemInventoryV2QuantityTotal,

    /**
     * The LineItemsResponseV2 model constructor.
     * @property {module:model/LineItemsResponseV2}
     */
    LineItemsResponseV2,

    /**
     * The LineItemsResponseV2InventoryDetailsInner model constructor.
     * @property {module:model/LineItemsResponseV2InventoryDetailsInner}
     */
    LineItemsResponseV2InventoryDetailsInner,

    /**
     * The LineItemsResponseV2LineDetails model constructor.
     * @property {module:model/LineItemsResponseV2LineDetails}
     */
    LineItemsResponseV2LineDetails,

    /**
     * The LineItemsResponseV2RequestedSkuData model constructor.
     * @property {module:model/LineItemsResponseV2RequestedSkuData}
     */
    LineItemsResponseV2RequestedSkuData,

    /**
     * The MerchantV2 model constructor.
     * @property {module:model/MerchantV2}
     */
    MerchantV2,

    /**
     * The OrderRequestV2 model constructor.
     * @property {module:model/OrderRequestV2}
     */
    OrderRequestV2,

    /**
     * The OrderRequestV2ItemsInner model constructor.
     * @property {module:model/OrderRequestV2ItemsInner}
     */
    OrderRequestV2ItemsInner,

    /**
     * The OrderRequestV2Warehouse model constructor.
     * @property {module:model/OrderRequestV2Warehouse}
     */
    OrderRequestV2Warehouse,

    /**
     * The OrderResponseHydrateV2 model constructor.
     * @property {module:model/OrderResponseHydrateV2}
     */
    OrderResponseHydrateV2,

    /**
     * The OrderResponseHydrateV2AllOfTrackingNumbersInner model constructor.
     * @property {module:model/OrderResponseHydrateV2AllOfTrackingNumbersInner}
     */
    OrderResponseHydrateV2AllOfTrackingNumbersInner,

    /**
     * The OrderResponseOneOfV2 model constructor.
     * @property {module:model/OrderResponseOneOfV2}
     */
    OrderResponseOneOfV2,

    /**
     * The OrderResponseV2 model constructor.
     * @property {module:model/OrderResponseV2}
     */
    OrderResponseV2,

    /**
     * The OrderResponseV2ParentOrder model constructor.
     * @property {module:model/OrderResponseV2ParentOrder}
     */
    OrderResponseV2ParentOrder,

    /**
     * The OrderShipV2 model constructor.
     * @property {module:model/OrderShipV2}
     */
    OrderShipV2,

    /**
     * The PaginationV2 model constructor.
     * @property {module:model/PaginationV2}
     */
    PaginationV2,

    /**
     * The ReturnV2 model constructor.
     * @property {module:model/ReturnV2}
     */
    ReturnV2,

    /**
     * The ReturnV2Order model constructor.
     * @property {module:model/ReturnV2Order}
     */
    ReturnV2Order,

    /**
     * The ReturnV2Reason model constructor.
     * @property {module:model/ReturnV2Reason}
     */
    ReturnV2Reason,

    /**
     * The ReturnsArrayV2 model constructor.
     * @property {module:model/ReturnsArrayV2}
     */
    ReturnsArrayV2,

    /**
     * The RmaItemV2 model constructor.
     * @property {module:model/RmaItemV2}
     */
    RmaItemV2,

    /**
     * The RmaItemV2Item model constructor.
     * @property {module:model/RmaItemV2Item}
     */
    RmaItemV2Item,

    /**
     * The RmaItemV2NonRestockedReason model constructor.
     * @property {module:model/RmaItemV2NonRestockedReason}
     */
    RmaItemV2NonRestockedReason,

    /**
     * The RmaRequestV2 model constructor.
     * @property {module:model/RmaRequestV2}
     */
    RmaRequestV2,

    /**
     * The RmaRequestV2ItemsInner model constructor.
     * @property {module:model/RmaRequestV2ItemsInner}
     */
    RmaRequestV2ItemsInner,

    /**
     * The RmaResponseV2 model constructor.
     * @property {module:model/RmaResponseV2}
     */
    RmaResponseV2,

    /**
     * The StatusEventV2 model constructor.
     * @property {module:model/StatusEventV2}
     */
    StatusEventV2,

    /**
     * The StatusTypeSimpleV2 model constructor.
     * @property {module:model/StatusTypeSimpleV2}
     */
    StatusTypeSimpleV2,

    /**
     * The StatusTypeSimpleV2Status model constructor.
     * @property {module:model/StatusTypeSimpleV2Status}
     */
    StatusTypeSimpleV2Status,

    /**
     * The StatusTypeV2 model constructor.
     * @property {module:model/StatusTypeV2}
     */
    StatusTypeV2,

    /**
     * The StatusTypeV2ActionRequiredBy model constructor.
     * @property {module:model/StatusTypeV2ActionRequiredBy}
     */
    StatusTypeV2ActionRequiredBy,

    /**
     * The StatusTypeV2Stage model constructor.
     * @property {module:model/StatusTypeV2Stage}
     */
    StatusTypeV2Stage,

    /**
     * The TrackingEventV2 model constructor.
     * @property {module:model/TrackingEventV2}
     */
    TrackingEventV2,

    /**
     * The TrackingNumberV2 model constructor.
     * @property {module:model/TrackingNumberV2}
     */
    TrackingNumberV2,

    /**
     * The TrackingResponse model constructor.
     * @property {module:model/TrackingResponse}
     */
    TrackingResponse,

    /**
     * The UserContactV2 model constructor.
     * @property {module:model/UserContactV2}
     */
    UserContactV2,

    /**
     * The UserContactV2Merchant model constructor.
     * @property {module:model/UserContactV2Merchant}
     */
    UserContactV2Merchant,

    /**
     * The UserV2 model constructor.
     * @property {module:model/UserV2}
     */
    UserV2,

    /**
     * The WarehouseV2 model constructor.
     * @property {module:model/WarehouseV2}
     */
    WarehouseV2,

    /**
    * The AccountingApi service constructor.
    * @property {module:api/AccountingApi}
    */
    AccountingApi,

    /**
    * The AuthApi service constructor.
    * @property {module:api/AuthApi}
    */
    AuthApi,

    /**
    * The InventoryApi service constructor.
    * @property {module:api/InventoryApi}
    */
    InventoryApi,

    /**
    * The OrdersApi service constructor.
    * @property {module:api/OrdersApi}
    */
    OrdersApi,

    /**
    * The PartnersApi service constructor.
    * @property {module:api/PartnersApi}
    */
    PartnersApi,

    /**
    * The ReturnsApi service constructor.
    * @property {module:api/ReturnsApi}
    */
    ReturnsApi,

    /**
    * The TrackingApi service constructor.
    * @property {module:api/TrackingApi}
    */
    TrackingApi,

    /**
    * The UsersApi service constructor.
    * @property {module:api/UsersApi}
    */
    UsersApi
};
