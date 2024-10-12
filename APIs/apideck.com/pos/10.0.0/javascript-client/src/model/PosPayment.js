/**
 * POS API
 * Welcome to the POS API.  You can use this API to access all POS API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CashDetails from './CashDetails';
import Currency from './Currency';
import PosBankAccount from './PosBankAccount';
import PosPaymentCardDetails from './PosPaymentCardDetails';
import PosPaymentExternalDetails from './PosPaymentExternalDetails';
import PosPaymentProcessingFeesInner from './PosPaymentProcessingFeesInner';
import ServiceCharge from './ServiceCharge';
import WalletDetails from './WalletDetails';

/**
 * The PosPayment model module.
 * @module model/PosPayment
 * @version 10.0.0
 */
class PosPayment {
    /**
     * Constructs a new <code>PosPayment</code>.
     * @alias module:model/PosPayment
     * @param amount {Number} 
     * @param currency {module:model/Currency} 
     * @param customerId {String} 
     * @param orderId {String} 
     * @param sourceId {String} The ID for the source of funds for this payment. Square-only: This can be a payment token (card nonce) generated by the payment form or a card on file made linked to the customer. if recording a payment that the seller received outside of Square, specify either `CASH` or `EXTERNAL`.
     * @param tenderId {String} 
     */
    constructor(amount, currency, customerId, orderId, sourceId, tenderId) { 
        
        PosPayment.initialize(this, amount, currency, customerId, orderId, sourceId, tenderId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, amount, currency, customerId, orderId, sourceId, tenderId) { 
        obj['amount'] = amount;
        obj['currency'] = currency;
        obj['customer_id'] = customerId;
        obj['order_id'] = orderId;
        obj['source_id'] = sourceId;
        obj['tender_id'] = tenderId;
    }

    /**
     * Constructs a <code>PosPayment</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PosPayment} obj Optional instance to populate.
     * @return {module:model/PosPayment} The populated <code>PosPayment</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PosPayment();

            if (data.hasOwnProperty('amount')) {
                obj['amount'] = ApiClient.convertToType(data['amount'], 'Number');
            }
            if (data.hasOwnProperty('app_fee')) {
                obj['app_fee'] = ApiClient.convertToType(data['app_fee'], 'Number');
            }
            if (data.hasOwnProperty('approved')) {
                obj['approved'] = ApiClient.convertToType(data['approved'], 'Number');
            }
            if (data.hasOwnProperty('bank_account')) {
                obj['bank_account'] = PosBankAccount.constructFromObject(data['bank_account']);
            }
            if (data.hasOwnProperty('card_details')) {
                obj['card_details'] = PosPaymentCardDetails.constructFromObject(data['card_details']);
            }
            if (data.hasOwnProperty('cash')) {
                obj['cash'] = CashDetails.constructFromObject(data['cash']);
            }
            if (data.hasOwnProperty('change_back_cash_amount')) {
                obj['change_back_cash_amount'] = ApiClient.convertToType(data['change_back_cash_amount'], 'Number');
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'Date');
            }
            if (data.hasOwnProperty('created_by')) {
                obj['created_by'] = ApiClient.convertToType(data['created_by'], 'String');
            }
            if (data.hasOwnProperty('currency')) {
                obj['currency'] = Currency.constructFromObject(data['currency']);
            }
            if (data.hasOwnProperty('custom_mappings')) {
                obj['custom_mappings'] = ApiClient.convertToType(data['custom_mappings'], Object);
            }
            if (data.hasOwnProperty('customer_id')) {
                obj['customer_id'] = ApiClient.convertToType(data['customer_id'], 'String');
            }
            if (data.hasOwnProperty('device_id')) {
                obj['device_id'] = ApiClient.convertToType(data['device_id'], 'String');
            }
            if (data.hasOwnProperty('employee_id')) {
                obj['employee_id'] = ApiClient.convertToType(data['employee_id'], 'String');
            }
            if (data.hasOwnProperty('external_details')) {
                obj['external_details'] = PosPaymentExternalDetails.constructFromObject(data['external_details']);
            }
            if (data.hasOwnProperty('external_payment_id')) {
                obj['external_payment_id'] = ApiClient.convertToType(data['external_payment_id'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('idempotency_key')) {
                obj['idempotency_key'] = ApiClient.convertToType(data['idempotency_key'], 'String');
            }
            if (data.hasOwnProperty('location_id')) {
                obj['location_id'] = ApiClient.convertToType(data['location_id'], 'String');
            }
            if (data.hasOwnProperty('merchant_id')) {
                obj['merchant_id'] = ApiClient.convertToType(data['merchant_id'], 'String');
            }
            if (data.hasOwnProperty('order_id')) {
                obj['order_id'] = ApiClient.convertToType(data['order_id'], 'String');
            }
            if (data.hasOwnProperty('processing_fees')) {
                obj['processing_fees'] = ApiClient.convertToType(data['processing_fees'], [PosPaymentProcessingFeesInner]);
            }
            if (data.hasOwnProperty('refunded')) {
                obj['refunded'] = ApiClient.convertToType(data['refunded'], 'Number');
            }
            if (data.hasOwnProperty('service_charges')) {
                obj['service_charges'] = ApiClient.convertToType(data['service_charges'], [ServiceCharge]);
            }
            if (data.hasOwnProperty('source')) {
                obj['source'] = ApiClient.convertToType(data['source'], 'String');
            }
            if (data.hasOwnProperty('source_id')) {
                obj['source_id'] = ApiClient.convertToType(data['source_id'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('tax')) {
                obj['tax'] = ApiClient.convertToType(data['tax'], 'Number');
            }
            if (data.hasOwnProperty('tender_id')) {
                obj['tender_id'] = ApiClient.convertToType(data['tender_id'], 'String');
            }
            if (data.hasOwnProperty('tip')) {
                obj['tip'] = ApiClient.convertToType(data['tip'], 'Number');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'Date');
            }
            if (data.hasOwnProperty('updated_by')) {
                obj['updated_by'] = ApiClient.convertToType(data['updated_by'], 'String');
            }
            if (data.hasOwnProperty('wallet')) {
                obj['wallet'] = WalletDetails.constructFromObject(data['wallet']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PosPayment</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PosPayment</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PosPayment.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `bank_account`
        if (data['bank_account']) { // data not null
          PosBankAccount.validateJSON(data['bank_account']);
        }
        // validate the optional field `card_details`
        if (data['card_details']) { // data not null
          PosPaymentCardDetails.validateJSON(data['card_details']);
        }
        // validate the optional field `cash`
        if (data['cash']) { // data not null
          CashDetails.validateJSON(data['cash']);
        }
        // ensure the json data is a string
        if (data['created_by'] && !(typeof data['created_by'] === 'string' || data['created_by'] instanceof String)) {
            throw new Error("Expected the field `created_by` to be a primitive type in the JSON string but got " + data['created_by']);
        }
        // ensure the json data is a string
        if (data['customer_id'] && !(typeof data['customer_id'] === 'string' || data['customer_id'] instanceof String)) {
            throw new Error("Expected the field `customer_id` to be a primitive type in the JSON string but got " + data['customer_id']);
        }
        // ensure the json data is a string
        if (data['device_id'] && !(typeof data['device_id'] === 'string' || data['device_id'] instanceof String)) {
            throw new Error("Expected the field `device_id` to be a primitive type in the JSON string but got " + data['device_id']);
        }
        // ensure the json data is a string
        if (data['employee_id'] && !(typeof data['employee_id'] === 'string' || data['employee_id'] instanceof String)) {
            throw new Error("Expected the field `employee_id` to be a primitive type in the JSON string but got " + data['employee_id']);
        }
        // validate the optional field `external_details`
        if (data['external_details']) { // data not null
          PosPaymentExternalDetails.validateJSON(data['external_details']);
        }
        // ensure the json data is a string
        if (data['external_payment_id'] && !(typeof data['external_payment_id'] === 'string' || data['external_payment_id'] instanceof String)) {
            throw new Error("Expected the field `external_payment_id` to be a primitive type in the JSON string but got " + data['external_payment_id']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['idempotency_key'] && !(typeof data['idempotency_key'] === 'string' || data['idempotency_key'] instanceof String)) {
            throw new Error("Expected the field `idempotency_key` to be a primitive type in the JSON string but got " + data['idempotency_key']);
        }
        // ensure the json data is a string
        if (data['location_id'] && !(typeof data['location_id'] === 'string' || data['location_id'] instanceof String)) {
            throw new Error("Expected the field `location_id` to be a primitive type in the JSON string but got " + data['location_id']);
        }
        // ensure the json data is a string
        if (data['merchant_id'] && !(typeof data['merchant_id'] === 'string' || data['merchant_id'] instanceof String)) {
            throw new Error("Expected the field `merchant_id` to be a primitive type in the JSON string but got " + data['merchant_id']);
        }
        // ensure the json data is a string
        if (data['order_id'] && !(typeof data['order_id'] === 'string' || data['order_id'] instanceof String)) {
            throw new Error("Expected the field `order_id` to be a primitive type in the JSON string but got " + data['order_id']);
        }
        if (data['processing_fees']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['processing_fees'])) {
                throw new Error("Expected the field `processing_fees` to be an array in the JSON data but got " + data['processing_fees']);
            }
            // validate the optional field `processing_fees` (array)
            for (const item of data['processing_fees']) {
                PosPaymentProcessingFeesInner.validateJSON(item);
            };
        }
        if (data['service_charges']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['service_charges'])) {
                throw new Error("Expected the field `service_charges` to be an array in the JSON data but got " + data['service_charges']);
            }
            // validate the optional field `service_charges` (array)
            for (const item of data['service_charges']) {
                ServiceCharge.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['source'] && !(typeof data['source'] === 'string' || data['source'] instanceof String)) {
            throw new Error("Expected the field `source` to be a primitive type in the JSON string but got " + data['source']);
        }
        // ensure the json data is a string
        if (data['source_id'] && !(typeof data['source_id'] === 'string' || data['source_id'] instanceof String)) {
            throw new Error("Expected the field `source_id` to be a primitive type in the JSON string but got " + data['source_id']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['tender_id'] && !(typeof data['tender_id'] === 'string' || data['tender_id'] instanceof String)) {
            throw new Error("Expected the field `tender_id` to be a primitive type in the JSON string but got " + data['tender_id']);
        }
        // ensure the json data is a string
        if (data['updated_by'] && !(typeof data['updated_by'] === 'string' || data['updated_by'] instanceof String)) {
            throw new Error("Expected the field `updated_by` to be a primitive type in the JSON string but got " + data['updated_by']);
        }
        // validate the optional field `wallet`
        if (data['wallet']) { // data not null
          WalletDetails.validateJSON(data['wallet']);
        }

        return true;
    }


}

PosPayment.RequiredProperties = ["amount", "currency", "customer_id", "order_id", "source_id", "tender_id"];

/**
 * @member {Number} amount
 */
PosPayment.prototype['amount'] = undefined;

/**
 * The amount the developer is taking as a fee for facilitating the payment on behalf of the seller.
 * @member {Number} app_fee
 */
PosPayment.prototype['app_fee'] = undefined;

/**
 * The initial amount of money approved for this payment.
 * @member {Number} approved
 */
PosPayment.prototype['approved'] = undefined;

/**
 * @member {module:model/PosBankAccount} bank_account
 */
PosPayment.prototype['bank_account'] = undefined;

/**
 * @member {module:model/PosPaymentCardDetails} card_details
 */
PosPayment.prototype['card_details'] = undefined;

/**
 * @member {module:model/CashDetails} cash
 */
PosPayment.prototype['cash'] = undefined;

/**
 * @member {Number} change_back_cash_amount
 */
PosPayment.prototype['change_back_cash_amount'] = undefined;

/**
 * The date and time when the object was created.
 * @member {Date} created_at
 */
PosPayment.prototype['created_at'] = undefined;

/**
 * The user who created the object.
 * @member {String} created_by
 */
PosPayment.prototype['created_by'] = undefined;

/**
 * @member {module:model/Currency} currency
 */
PosPayment.prototype['currency'] = undefined;

/**
 * When custom mappings are configured on the resource, the result is included here.
 * @member {Object} custom_mappings
 */
PosPayment.prototype['custom_mappings'] = undefined;

/**
 * @member {String} customer_id
 */
PosPayment.prototype['customer_id'] = undefined;

/**
 * @member {String} device_id
 */
PosPayment.prototype['device_id'] = undefined;

/**
 * @member {String} employee_id
 */
PosPayment.prototype['employee_id'] = undefined;

/**
 * @member {module:model/PosPaymentExternalDetails} external_details
 */
PosPayment.prototype['external_details'] = undefined;

/**
 * @member {String} external_payment_id
 */
PosPayment.prototype['external_payment_id'] = undefined;

/**
 * A unique identifier for an object.
 * @member {String} id
 */
PosPayment.prototype['id'] = undefined;

/**
 * A value you specify that uniquely identifies this request among requests you have sent.
 * @member {String} idempotency_key
 */
PosPayment.prototype['idempotency_key'] = undefined;

/**
 * @member {String} location_id
 */
PosPayment.prototype['location_id'] = undefined;

/**
 * @member {String} merchant_id
 */
PosPayment.prototype['merchant_id'] = undefined;

/**
 * @member {String} order_id
 */
PosPayment.prototype['order_id'] = undefined;

/**
 * @member {Array.<module:model/PosPaymentProcessingFeesInner>} processing_fees
 */
PosPayment.prototype['processing_fees'] = undefined;

/**
 * The initial amount of money approved for this payment.
 * @member {Number} refunded
 */
PosPayment.prototype['refunded'] = undefined;

/**
 * Optional service charges or gratuity tip applied to the order.
 * @member {Array.<module:model/ServiceCharge>} service_charges
 */
PosPayment.prototype['service_charges'] = undefined;

/**
 * Source of this payment.
 * @member {module:model/PosPayment.SourceEnum} source
 */
PosPayment.prototype['source'] = undefined;

/**
 * The ID for the source of funds for this payment. Square-only: This can be a payment token (card nonce) generated by the payment form or a card on file made linked to the customer. if recording a payment that the seller received outside of Square, specify either `CASH` or `EXTERNAL`.
 * @member {String} source_id
 */
PosPayment.prototype['source_id'] = undefined;

/**
 * Status of this payment.
 * @member {module:model/PosPayment.StatusEnum} status
 */
PosPayment.prototype['status'] = undefined;

/**
 * @member {Number} tax
 */
PosPayment.prototype['tax'] = undefined;

/**
 * @member {String} tender_id
 */
PosPayment.prototype['tender_id'] = undefined;

/**
 * @member {Number} tip
 */
PosPayment.prototype['tip'] = undefined;

/**
 * @member {Number} total
 */
PosPayment.prototype['total'] = undefined;

/**
 * The date and time when the object was last updated.
 * @member {Date} updated_at
 */
PosPayment.prototype['updated_at'] = undefined;

/**
 * The user who last updated the object.
 * @member {String} updated_by
 */
PosPayment.prototype['updated_by'] = undefined;

/**
 * @member {module:model/WalletDetails} wallet
 */
PosPayment.prototype['wallet'] = undefined;





/**
 * Allowed values for the <code>source</code> property.
 * @enum {String}
 * @readonly
 */
PosPayment['SourceEnum'] = {

    /**
     * value: "card"
     * @const
     */
    "card": "card",

    /**
     * value: "bank_account"
     * @const
     */
    "bank_account": "bank_account",

    /**
     * value: "wallet"
     * @const
     */
    "wallet": "wallet",

    /**
     * value: "bnpl"
     * @const
     */
    "bnpl": "bnpl",

    /**
     * value: "cash"
     * @const
     */
    "cash": "cash",

    /**
     * value: "external"
     * @const
     */
    "external": "external",

    /**
     * value: "other"
     * @const
     */
    "other": "other"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
PosPayment['StatusEnum'] = {

    /**
     * value: "approved"
     * @const
     */
    "approved": "approved",

    /**
     * value: "pending"
     * @const
     */
    "pending": "pending",

    /**
     * value: "completed"
     * @const
     */
    "completed": "completed",

    /**
     * value: "canceled"
     * @const
     */
    "canceled": "canceled",

    /**
     * value: "failed"
     * @const
     */
    "failed": "failed",

    /**
     * value: "other"
     * @const
     */
    "other": "other"
};



export default PosPayment;

