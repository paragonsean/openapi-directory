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
import OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails from './OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails';
import OrderFulfillmentsInnerPickupDetailsRecipient from './OrderFulfillmentsInnerPickupDetailsRecipient';

/**
 * The OrderFulfillmentsInnerPickupDetails model module.
 * @module model/OrderFulfillmentsInnerPickupDetails
 * @version 10.0.0
 */
class OrderFulfillmentsInnerPickupDetails {
    /**
     * Constructs a new <code>OrderFulfillmentsInnerPickupDetails</code>.
     * @alias module:model/OrderFulfillmentsInnerPickupDetails
     */
    constructor() { 
        
        OrderFulfillmentsInnerPickupDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OrderFulfillmentsInnerPickupDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OrderFulfillmentsInnerPickupDetails} obj Optional instance to populate.
     * @return {module:model/OrderFulfillmentsInnerPickupDetails} The populated <code>OrderFulfillmentsInnerPickupDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OrderFulfillmentsInnerPickupDetails();

            if (data.hasOwnProperty('accepted_at')) {
                obj['accepted_at'] = ApiClient.convertToType(data['accepted_at'], 'Date');
            }
            if (data.hasOwnProperty('auto_complete_duration')) {
                obj['auto_complete_duration'] = ApiClient.convertToType(data['auto_complete_duration'], 'String');
            }
            if (data.hasOwnProperty('cancel_reason')) {
                obj['cancel_reason'] = ApiClient.convertToType(data['cancel_reason'], 'String');
            }
            if (data.hasOwnProperty('canceled_at')) {
                obj['canceled_at'] = ApiClient.convertToType(data['canceled_at'], 'Date');
            }
            if (data.hasOwnProperty('curbside_pickup_details')) {
                obj['curbside_pickup_details'] = OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails.constructFromObject(data['curbside_pickup_details']);
            }
            if (data.hasOwnProperty('expired_at')) {
                obj['expired_at'] = ApiClient.convertToType(data['expired_at'], 'Date');
            }
            if (data.hasOwnProperty('expires_at')) {
                obj['expires_at'] = ApiClient.convertToType(data['expires_at'], 'Date');
            }
            if (data.hasOwnProperty('is_curbside_pickup')) {
                obj['is_curbside_pickup'] = ApiClient.convertToType(data['is_curbside_pickup'], 'Boolean');
            }
            if (data.hasOwnProperty('note')) {
                obj['note'] = ApiClient.convertToType(data['note'], 'String');
            }
            if (data.hasOwnProperty('picked_up_at')) {
                obj['picked_up_at'] = ApiClient.convertToType(data['picked_up_at'], 'Date');
            }
            if (data.hasOwnProperty('pickup_at')) {
                obj['pickup_at'] = ApiClient.convertToType(data['pickup_at'], 'Date');
            }
            if (data.hasOwnProperty('pickup_window_duration')) {
                obj['pickup_window_duration'] = ApiClient.convertToType(data['pickup_window_duration'], 'String');
            }
            if (data.hasOwnProperty('placed_at')) {
                obj['placed_at'] = ApiClient.convertToType(data['placed_at'], 'Date');
            }
            if (data.hasOwnProperty('prep_time_duration')) {
                obj['prep_time_duration'] = ApiClient.convertToType(data['prep_time_duration'], 'String');
            }
            if (data.hasOwnProperty('ready_at')) {
                obj['ready_at'] = ApiClient.convertToType(data['ready_at'], 'Date');
            }
            if (data.hasOwnProperty('recipient')) {
                obj['recipient'] = OrderFulfillmentsInnerPickupDetailsRecipient.constructFromObject(data['recipient']);
            }
            if (data.hasOwnProperty('rejected_at')) {
                obj['rejected_at'] = ApiClient.convertToType(data['rejected_at'], 'Date');
            }
            if (data.hasOwnProperty('schedule_type')) {
                obj['schedule_type'] = ApiClient.convertToType(data['schedule_type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OrderFulfillmentsInnerPickupDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OrderFulfillmentsInnerPickupDetails</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['auto_complete_duration'] && !(typeof data['auto_complete_duration'] === 'string' || data['auto_complete_duration'] instanceof String)) {
            throw new Error("Expected the field `auto_complete_duration` to be a primitive type in the JSON string but got " + data['auto_complete_duration']);
        }
        // ensure the json data is a string
        if (data['cancel_reason'] && !(typeof data['cancel_reason'] === 'string' || data['cancel_reason'] instanceof String)) {
            throw new Error("Expected the field `cancel_reason` to be a primitive type in the JSON string but got " + data['cancel_reason']);
        }
        // validate the optional field `curbside_pickup_details`
        if (data['curbside_pickup_details']) { // data not null
          OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails.validateJSON(data['curbside_pickup_details']);
        }
        // ensure the json data is a string
        if (data['note'] && !(typeof data['note'] === 'string' || data['note'] instanceof String)) {
            throw new Error("Expected the field `note` to be a primitive type in the JSON string but got " + data['note']);
        }
        // ensure the json data is a string
        if (data['pickup_window_duration'] && !(typeof data['pickup_window_duration'] === 'string' || data['pickup_window_duration'] instanceof String)) {
            throw new Error("Expected the field `pickup_window_duration` to be a primitive type in the JSON string but got " + data['pickup_window_duration']);
        }
        // ensure the json data is a string
        if (data['prep_time_duration'] && !(typeof data['prep_time_duration'] === 'string' || data['prep_time_duration'] instanceof String)) {
            throw new Error("Expected the field `prep_time_duration` to be a primitive type in the JSON string but got " + data['prep_time_duration']);
        }
        // validate the optional field `recipient`
        if (data['recipient']) { // data not null
          OrderFulfillmentsInnerPickupDetailsRecipient.validateJSON(data['recipient']);
        }
        // ensure the json data is a string
        if (data['schedule_type'] && !(typeof data['schedule_type'] === 'string' || data['schedule_type'] instanceof String)) {
            throw new Error("Expected the field `schedule_type` to be a primitive type in the JSON string but got " + data['schedule_type']);
        }

        return true;
    }


}



/**
 * @member {Date} accepted_at
 */
OrderFulfillmentsInnerPickupDetails.prototype['accepted_at'] = undefined;

/**
 * The duration of time after which an open and accepted pickup fulfillment is automatically moved to the COMPLETED state. The duration must be in RFC 3339 format (for example, 'P1W3D').
 * @member {String} auto_complete_duration
 */
OrderFulfillmentsInnerPickupDetails.prototype['auto_complete_duration'] = undefined;

/**
 * A description of why the pickup was canceled.
 * @member {String} cancel_reason
 */
OrderFulfillmentsInnerPickupDetails.prototype['cancel_reason'] = undefined;

/**
 * Indicating when the fulfillment was canceled. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").
 * @member {Date} canceled_at
 */
OrderFulfillmentsInnerPickupDetails.prototype['canceled_at'] = undefined;

/**
 * @member {module:model/OrderFulfillmentsInnerPickupDetailsCurbsidePickupDetails} curbside_pickup_details
 */
OrderFulfillmentsInnerPickupDetails.prototype['curbside_pickup_details'] = undefined;

/**
 * Indicating when the fulfillment expired. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").
 * @member {Date} expired_at
 */
OrderFulfillmentsInnerPickupDetails.prototype['expired_at'] = undefined;

/**
 * Indicating when this fulfillment expires if it is not accepted. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\"). The expiration time can only be set up to 7 days in the future. If `expires_at` is not set, this pickup fulfillment is automatically accepted when  placed.
 * @member {Date} expires_at
 */
OrderFulfillmentsInnerPickupDetails.prototype['expires_at'] = undefined;

/**
 * If set to `true`, indicates that this pickup order is for curbside pickup, not in-store pickup.
 * @member {Boolean} is_curbside_pickup
 */
OrderFulfillmentsInnerPickupDetails.prototype['is_curbside_pickup'] = undefined;

/**
 * A note meant to provide additional instructions about the pickup fulfillment displayed in the Square Point of Sale application and set by the API.
 * @member {String} note
 */
OrderFulfillmentsInnerPickupDetails.prototype['note'] = undefined;

/**
 * Indicating when the fulfillment was picked up by the recipient. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").
 * @member {Date} picked_up_at
 */
OrderFulfillmentsInnerPickupDetails.prototype['picked_up_at'] = undefined;

/**
 * The timestamp that represents the start of the pickup window. Must be in RFC 3339 timestamp format, e.g.,  \"2016-09-04T23:59:33.123Z\".  For fulfillments with the schedule type `ASAP`, this is automatically set to the current time plus the expected duration to prepare the fulfillment.
 * @member {Date} pickup_at
 */
OrderFulfillmentsInnerPickupDetails.prototype['pickup_at'] = undefined;

/**
 * The window of time in which the order should be picked up after the `pickup_at` timestamp. Must be in RFC 3339 duration format, e.g., \"P1W3D\". Can be used as an informational guideline for merchants.
 * @member {String} pickup_window_duration
 */
OrderFulfillmentsInnerPickupDetails.prototype['pickup_window_duration'] = undefined;

/**
 * Indicating when the fulfillment was placed. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").
 * @member {Date} placed_at
 */
OrderFulfillmentsInnerPickupDetails.prototype['placed_at'] = undefined;

/**
 * The duration of time it takes to prepare this fulfillment. The duration must be in RFC 3339 format (for example, \"P1W3D\").
 * @member {String} prep_time_duration
 */
OrderFulfillmentsInnerPickupDetails.prototype['prep_time_duration'] = undefined;

/**
 * Indicating when the fulfillment is marked as ready for pickup. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").
 * @member {Date} ready_at
 */
OrderFulfillmentsInnerPickupDetails.prototype['ready_at'] = undefined;

/**
 * @member {module:model/OrderFulfillmentsInnerPickupDetailsRecipient} recipient
 */
OrderFulfillmentsInnerPickupDetails.prototype['recipient'] = undefined;

/**
 * Indicating when the fulfillment was rejected. The timestamp must be in RFC 3339 format (for example, \"2016-09-04T23:59:33.123Z\").
 * @member {Date} rejected_at
 */
OrderFulfillmentsInnerPickupDetails.prototype['rejected_at'] = undefined;

/**
 * The schedule type of the pickup fulfillment.
 * @member {module:model/OrderFulfillmentsInnerPickupDetails.ScheduleTypeEnum} schedule_type
 */
OrderFulfillmentsInnerPickupDetails.prototype['schedule_type'] = undefined;





/**
 * Allowed values for the <code>schedule_type</code> property.
 * @enum {String}
 * @readonly
 */
OrderFulfillmentsInnerPickupDetails['ScheduleTypeEnum'] = {

    /**
     * value: "scheduled"
     * @const
     */
    "scheduled": "scheduled"
};



export default OrderFulfillmentsInnerPickupDetails;

