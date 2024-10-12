/**
 * CRM API
 * Welcome to the CRM API.  You can use this API to access all CRM API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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
import Currency from './Currency';
import CustomField from './CustomField';

/**
 * The Opportunity model module.
 * @module model/Opportunity
 * @version 10.0.0
 */
class Opportunity {
    /**
     * Constructs a new <code>Opportunity</code>.
     * @alias module:model/Opportunity
     * @param primaryContactId {String} The unique identifier of the primary contact associated with the opportunity.
     * @param title {String} The title or name of the opportunity.
     */
    constructor(primaryContactId, title) { 
        
        Opportunity.initialize(this, primaryContactId, title);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, primaryContactId, title) { 
        obj['primary_contact_id'] = primaryContactId;
        obj['title'] = title;
    }

    /**
     * Constructs a <code>Opportunity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Opportunity} obj Optional instance to populate.
     * @return {module:model/Opportunity} The populated <code>Opportunity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Opportunity();

            if (data.hasOwnProperty('close_date')) {
                obj['close_date'] = ApiClient.convertToType(data['close_date'], 'Date');
            }
            if (data.hasOwnProperty('company_id')) {
                obj['company_id'] = ApiClient.convertToType(data['company_id'], 'String');
            }
            if (data.hasOwnProperty('company_name')) {
                obj['company_name'] = ApiClient.convertToType(data['company_name'], 'String');
            }
            if (data.hasOwnProperty('contact_id')) {
                obj['contact_id'] = ApiClient.convertToType(data['contact_id'], 'String');
            }
            if (data.hasOwnProperty('contact_ids')) {
                obj['contact_ids'] = ApiClient.convertToType(data['contact_ids'], ['String']);
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
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], [CustomField]);
            }
            if (data.hasOwnProperty('custom_mappings')) {
                obj['custom_mappings'] = ApiClient.convertToType(data['custom_mappings'], Object);
            }
            if (data.hasOwnProperty('date_last_contacted')) {
                obj['date_last_contacted'] = ApiClient.convertToType(data['date_last_contacted'], 'Date');
            }
            if (data.hasOwnProperty('date_lead_created')) {
                obj['date_lead_created'] = ApiClient.convertToType(data['date_lead_created'], 'Date');
            }
            if (data.hasOwnProperty('date_stage_changed')) {
                obj['date_stage_changed'] = ApiClient.convertToType(data['date_stage_changed'], 'Date');
            }
            if (data.hasOwnProperty('deleted')) {
                obj['deleted'] = ApiClient.convertToType(data['deleted'], 'Boolean');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('expected_revenue')) {
                obj['expected_revenue'] = ApiClient.convertToType(data['expected_revenue'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('interaction_count')) {
                obj['interaction_count'] = ApiClient.convertToType(data['interaction_count'], 'Number');
            }
            if (data.hasOwnProperty('last_activity_at')) {
                obj['last_activity_at'] = ApiClient.convertToType(data['last_activity_at'], 'String');
            }
            if (data.hasOwnProperty('lead_id')) {
                obj['lead_id'] = ApiClient.convertToType(data['lead_id'], 'String');
            }
            if (data.hasOwnProperty('lead_source')) {
                obj['lead_source'] = ApiClient.convertToType(data['lead_source'], 'String');
            }
            if (data.hasOwnProperty('loss_reason')) {
                obj['loss_reason'] = ApiClient.convertToType(data['loss_reason'], 'String');
            }
            if (data.hasOwnProperty('loss_reason_id')) {
                obj['loss_reason_id'] = ApiClient.convertToType(data['loss_reason_id'], 'String');
            }
            if (data.hasOwnProperty('monetary_amount')) {
                obj['monetary_amount'] = ApiClient.convertToType(data['monetary_amount'], 'Number');
            }
            if (data.hasOwnProperty('owner_id')) {
                obj['owner_id'] = ApiClient.convertToType(data['owner_id'], 'String');
            }
            if (data.hasOwnProperty('pipeline_id')) {
                obj['pipeline_id'] = ApiClient.convertToType(data['pipeline_id'], 'String');
            }
            if (data.hasOwnProperty('pipeline_stage_id')) {
                obj['pipeline_stage_id'] = ApiClient.convertToType(data['pipeline_stage_id'], 'String');
            }
            if (data.hasOwnProperty('primary_contact_id')) {
                obj['primary_contact_id'] = ApiClient.convertToType(data['primary_contact_id'], 'String');
            }
            if (data.hasOwnProperty('priority')) {
                obj['priority'] = ApiClient.convertToType(data['priority'], 'String');
            }
            if (data.hasOwnProperty('source_id')) {
                obj['source_id'] = ApiClient.convertToType(data['source_id'], 'String');
            }
            if (data.hasOwnProperty('stage_last_changed_at')) {
                obj['stage_last_changed_at'] = ApiClient.convertToType(data['stage_last_changed_at'], 'Date');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('status_id')) {
                obj['status_id'] = ApiClient.convertToType(data['status_id'], 'String');
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], ['String']);
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'Date');
            }
            if (data.hasOwnProperty('updated_by')) {
                obj['updated_by'] = ApiClient.convertToType(data['updated_by'], 'String');
            }
            if (data.hasOwnProperty('win_probability')) {
                obj['win_probability'] = ApiClient.convertToType(data['win_probability'], 'Number');
            }
            if (data.hasOwnProperty('won_reason')) {
                obj['won_reason'] = ApiClient.convertToType(data['won_reason'], 'String');
            }
            if (data.hasOwnProperty('won_reason_id')) {
                obj['won_reason_id'] = ApiClient.convertToType(data['won_reason_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Opportunity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Opportunity</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Opportunity.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['company_id'] && !(typeof data['company_id'] === 'string' || data['company_id'] instanceof String)) {
            throw new Error("Expected the field `company_id` to be a primitive type in the JSON string but got " + data['company_id']);
        }
        // ensure the json data is a string
        if (data['company_name'] && !(typeof data['company_name'] === 'string' || data['company_name'] instanceof String)) {
            throw new Error("Expected the field `company_name` to be a primitive type in the JSON string but got " + data['company_name']);
        }
        // ensure the json data is a string
        if (data['contact_id'] && !(typeof data['contact_id'] === 'string' || data['contact_id'] instanceof String)) {
            throw new Error("Expected the field `contact_id` to be a primitive type in the JSON string but got " + data['contact_id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['contact_ids'])) {
            throw new Error("Expected the field `contact_ids` to be an array in the JSON data but got " + data['contact_ids']);
        }
        // ensure the json data is a string
        if (data['created_by'] && !(typeof data['created_by'] === 'string' || data['created_by'] instanceof String)) {
            throw new Error("Expected the field `created_by` to be a primitive type in the JSON string but got " + data['created_by']);
        }
        if (data['custom_fields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['custom_fields'])) {
                throw new Error("Expected the field `custom_fields` to be an array in the JSON data but got " + data['custom_fields']);
            }
            // validate the optional field `custom_fields` (array)
            for (const item of data['custom_fields']) {
                CustomField.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['last_activity_at'] && !(typeof data['last_activity_at'] === 'string' || data['last_activity_at'] instanceof String)) {
            throw new Error("Expected the field `last_activity_at` to be a primitive type in the JSON string but got " + data['last_activity_at']);
        }
        // ensure the json data is a string
        if (data['lead_id'] && !(typeof data['lead_id'] === 'string' || data['lead_id'] instanceof String)) {
            throw new Error("Expected the field `lead_id` to be a primitive type in the JSON string but got " + data['lead_id']);
        }
        // ensure the json data is a string
        if (data['lead_source'] && !(typeof data['lead_source'] === 'string' || data['lead_source'] instanceof String)) {
            throw new Error("Expected the field `lead_source` to be a primitive type in the JSON string but got " + data['lead_source']);
        }
        // ensure the json data is a string
        if (data['loss_reason'] && !(typeof data['loss_reason'] === 'string' || data['loss_reason'] instanceof String)) {
            throw new Error("Expected the field `loss_reason` to be a primitive type in the JSON string but got " + data['loss_reason']);
        }
        // ensure the json data is a string
        if (data['loss_reason_id'] && !(typeof data['loss_reason_id'] === 'string' || data['loss_reason_id'] instanceof String)) {
            throw new Error("Expected the field `loss_reason_id` to be a primitive type in the JSON string but got " + data['loss_reason_id']);
        }
        // ensure the json data is a string
        if (data['owner_id'] && !(typeof data['owner_id'] === 'string' || data['owner_id'] instanceof String)) {
            throw new Error("Expected the field `owner_id` to be a primitive type in the JSON string but got " + data['owner_id']);
        }
        // ensure the json data is a string
        if (data['pipeline_id'] && !(typeof data['pipeline_id'] === 'string' || data['pipeline_id'] instanceof String)) {
            throw new Error("Expected the field `pipeline_id` to be a primitive type in the JSON string but got " + data['pipeline_id']);
        }
        // ensure the json data is a string
        if (data['pipeline_stage_id'] && !(typeof data['pipeline_stage_id'] === 'string' || data['pipeline_stage_id'] instanceof String)) {
            throw new Error("Expected the field `pipeline_stage_id` to be a primitive type in the JSON string but got " + data['pipeline_stage_id']);
        }
        // ensure the json data is a string
        if (data['primary_contact_id'] && !(typeof data['primary_contact_id'] === 'string' || data['primary_contact_id'] instanceof String)) {
            throw new Error("Expected the field `primary_contact_id` to be a primitive type in the JSON string but got " + data['primary_contact_id']);
        }
        // ensure the json data is a string
        if (data['priority'] && !(typeof data['priority'] === 'string' || data['priority'] instanceof String)) {
            throw new Error("Expected the field `priority` to be a primitive type in the JSON string but got " + data['priority']);
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
        if (data['status_id'] && !(typeof data['status_id'] === 'string' || data['status_id'] instanceof String)) {
            throw new Error("Expected the field `status_id` to be a primitive type in the JSON string but got " + data['status_id']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['tags'])) {
            throw new Error("Expected the field `tags` to be an array in the JSON data but got " + data['tags']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }
        // ensure the json data is a string
        if (data['updated_by'] && !(typeof data['updated_by'] === 'string' || data['updated_by'] instanceof String)) {
            throw new Error("Expected the field `updated_by` to be a primitive type in the JSON string but got " + data['updated_by']);
        }
        // ensure the json data is a string
        if (data['won_reason'] && !(typeof data['won_reason'] === 'string' || data['won_reason'] instanceof String)) {
            throw new Error("Expected the field `won_reason` to be a primitive type in the JSON string but got " + data['won_reason']);
        }
        // ensure the json data is a string
        if (data['won_reason_id'] && !(typeof data['won_reason_id'] === 'string' || data['won_reason_id'] instanceof String)) {
            throw new Error("Expected the field `won_reason_id` to be a primitive type in the JSON string but got " + data['won_reason_id']);
        }

        return true;
    }


}

Opportunity.RequiredProperties = ["primary_contact_id", "title"];

/**
 * The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet.
 * @member {Date} close_date
 */
Opportunity.prototype['close_date'] = undefined;

/**
 * The unique identifier of the company associated with the opportunity.
 * @member {String} company_id
 */
Opportunity.prototype['company_id'] = undefined;

/**
 * The name of the company associated with the opportunity.
 * @member {String} company_name
 */
Opportunity.prototype['company_name'] = undefined;

/**
 * The unique identifier of the contact associated with the opportunity.
 * @member {String} contact_id
 */
Opportunity.prototype['contact_id'] = undefined;

/**
 * An array of unique identifiers of all contacts associated with the opportunity.
 * @member {Array.<String>} contact_ids
 */
Opportunity.prototype['contact_ids'] = undefined;

/**
 * The date and time when the opportunity was created.
 * @member {Date} created_at
 */
Opportunity.prototype['created_at'] = undefined;

/**
 * The unique identifier of the user who created the opportunity.
 * @member {String} created_by
 */
Opportunity.prototype['created_by'] = undefined;

/**
 * @member {module:model/Currency} currency
 */
Opportunity.prototype['currency'] = undefined;

/**
 * @member {Array.<module:model/CustomField>} custom_fields
 */
Opportunity.prototype['custom_fields'] = undefined;

/**
 * When custom mappings are configured on the resource, the result is included here.
 * @member {Object} custom_mappings
 */
Opportunity.prototype['custom_mappings'] = undefined;

/**
 * The date and time when the opportunity was last contacted.
 * @member {Date} date_last_contacted
 */
Opportunity.prototype['date_last_contacted'] = undefined;

/**
 * The date and time when the lead associated with the opportunity was created.
 * @member {Date} date_lead_created
 */
Opportunity.prototype['date_lead_created'] = undefined;

/**
 * The date and time when the stage of the opportunity was last changed.
 * @member {Date} date_stage_changed
 */
Opportunity.prototype['date_stage_changed'] = undefined;

/**
 * Indicates whether the opportunity has been deleted.
 * @member {Boolean} deleted
 */
Opportunity.prototype['deleted'] = undefined;

/**
 * A description of the opportunity.
 * @member {String} description
 */
Opportunity.prototype['description'] = undefined;

/**
 * The expected revenue from the opportunity
 * @member {Number} expected_revenue
 */
Opportunity.prototype['expected_revenue'] = undefined;

/**
 * A unique identifier for the opportunity.
 * @member {String} id
 */
Opportunity.prototype['id'] = undefined;

/**
 * The number of interactions with the opportunity.
 * @member {Number} interaction_count
 */
Opportunity.prototype['interaction_count'] = undefined;

/**
 * The date and time of the last activity associated with the opportunity.
 * @member {String} last_activity_at
 */
Opportunity.prototype['last_activity_at'] = undefined;

/**
 * The unique identifier of the lead associated with the opportunity.
 * @member {String} lead_id
 */
Opportunity.prototype['lead_id'] = undefined;

/**
 * The source of the lead associated with the opportunity.
 * @member {String} lead_source
 */
Opportunity.prototype['lead_source'] = undefined;

/**
 * The reason why the opportunity was lost.
 * @member {String} loss_reason
 */
Opportunity.prototype['loss_reason'] = undefined;

/**
 * The unique identifier of the reason why the opportunity was lost.
 * @member {String} loss_reason_id
 */
Opportunity.prototype['loss_reason_id'] = undefined;

/**
 * The monetary value associated with the opportunity
 * @member {Number} monetary_amount
 */
Opportunity.prototype['monetary_amount'] = undefined;

/**
 * The unique identifier of the user who owns the opportunity.
 * @member {String} owner_id
 */
Opportunity.prototype['owner_id'] = undefined;

/**
 * The unique identifier of the pipeline associated with the opportunity
 * @member {String} pipeline_id
 */
Opportunity.prototype['pipeline_id'] = undefined;

/**
 * The unique identifier of the stage in the pipeline associated with the opportunity.
 * @member {String} pipeline_stage_id
 */
Opportunity.prototype['pipeline_stage_id'] = undefined;

/**
 * The unique identifier of the primary contact associated with the opportunity.
 * @member {String} primary_contact_id
 */
Opportunity.prototype['primary_contact_id'] = undefined;

/**
 * The priority level of the opportunity.
 * @member {String} priority
 */
Opportunity.prototype['priority'] = undefined;

/**
 * The unique identifier of the source of the opportunity.
 * @member {String} source_id
 */
Opportunity.prototype['source_id'] = undefined;

/**
 * The date and time when the stage of the opportunity was last changed.
 * @member {Date} stage_last_changed_at
 */
Opportunity.prototype['stage_last_changed_at'] = undefined;

/**
 * The current status of the opportunity.
 * @member {String} status
 */
Opportunity.prototype['status'] = undefined;

/**
 * The unique identifier of the current status of the opportunity.
 * @member {String} status_id
 */
Opportunity.prototype['status_id'] = undefined;

/**
 * @member {Array.<String>} tags
 */
Opportunity.prototype['tags'] = undefined;

/**
 * The title or name of the opportunity.
 * @member {String} title
 */
Opportunity.prototype['title'] = undefined;

/**
 * The type of the opportunity
 * @member {String} type
 */
Opportunity.prototype['type'] = undefined;

/**
 * The date and time when the opportunity was last updated.
 * @member {Date} updated_at
 */
Opportunity.prototype['updated_at'] = undefined;

/**
 * The unique identifier of the user who last updated the opportunity.
 * @member {String} updated_by
 */
Opportunity.prototype['updated_by'] = undefined;

/**
 * The probability of winning the opportunity, expressed as a percentage.
 * @member {Number} win_probability
 */
Opportunity.prototype['win_probability'] = undefined;

/**
 * The reason why the opportunity was won.
 * @member {String} won_reason
 */
Opportunity.prototype['won_reason'] = undefined;

/**
 * The unique identifier of the reason why the opportunity was won.
 * @member {String} won_reason_id
 */
Opportunity.prototype['won_reason_id'] = undefined;






export default Opportunity;

