/**
 * ATS API
 * Welcome to the ATS API.  You can use this API to access all ATS API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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
import Address from './Address';
import Branch from './Branch';
import CustomField from './CustomField';
import Department from './Department';
import JobBlocksInner from './JobBlocksInner';
import JobLinksInner from './JobLinksInner';
import JobSalary from './JobSalary';
import JobStatus from './JobStatus';

/**
 * The Job model module.
 * @module model/Job
 * @version 10.0.0
 */
class Job {
    /**
     * Constructs a new <code>Job</code>.
     * @alias module:model/Job
     */
    constructor() { 
        
        Job.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Job</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Job} obj Optional instance to populate.
     * @return {module:model/Job} The populated <code>Job</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Job();

            if (data.hasOwnProperty('addresses')) {
                obj['addresses'] = ApiClient.convertToType(data['addresses'], [Address]);
            }
            if (data.hasOwnProperty('available_to_employees')) {
                obj['available_to_employees'] = ApiClient.convertToType(data['available_to_employees'], 'Boolean');
            }
            if (data.hasOwnProperty('blocks')) {
                obj['blocks'] = ApiClient.convertToType(data['blocks'], [JobBlocksInner]);
            }
            if (data.hasOwnProperty('branch')) {
                obj['branch'] = Branch.constructFromObject(data['branch']);
            }
            if (data.hasOwnProperty('closing')) {
                obj['closing'] = ApiClient.convertToType(data['closing'], 'String');
            }
            if (data.hasOwnProperty('closing_date')) {
                obj['closing_date'] = ApiClient.convertToType(data['closing_date'], 'Date');
            }
            if (data.hasOwnProperty('closing_html')) {
                obj['closing_html'] = ApiClient.convertToType(data['closing_html'], 'String');
            }
            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('confidential')) {
                obj['confidential'] = ApiClient.convertToType(data['confidential'], 'Boolean');
            }
            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'Date');
            }
            if (data.hasOwnProperty('created_by')) {
                obj['created_by'] = ApiClient.convertToType(data['created_by'], 'String');
            }
            if (data.hasOwnProperty('custom_fields')) {
                obj['custom_fields'] = ApiClient.convertToType(data['custom_fields'], [CustomField]);
            }
            if (data.hasOwnProperty('custom_mappings')) {
                obj['custom_mappings'] = ApiClient.convertToType(data['custom_mappings'], Object);
            }
            if (data.hasOwnProperty('deleted')) {
                obj['deleted'] = ApiClient.convertToType(data['deleted'], 'Boolean');
            }
            if (data.hasOwnProperty('department')) {
                obj['department'] = Department.constructFromObject(data['department']);
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('description_html')) {
                obj['description_html'] = ApiClient.convertToType(data['description_html'], 'String');
            }
            if (data.hasOwnProperty('employment_terms')) {
                obj['employment_terms'] = ApiClient.convertToType(data['employment_terms'], 'String');
            }
            if (data.hasOwnProperty('experience')) {
                obj['experience'] = ApiClient.convertToType(data['experience'], 'String');
            }
            if (data.hasOwnProperty('followers')) {
                obj['followers'] = ApiClient.convertToType(data['followers'], ['String']);
            }
            if (data.hasOwnProperty('hiring_managers')) {
                obj['hiring_managers'] = ApiClient.convertToType(data['hiring_managers'], ['String']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('job_portal_url')) {
                obj['job_portal_url'] = ApiClient.convertToType(data['job_portal_url'], 'String');
            }
            if (data.hasOwnProperty('language')) {
                obj['language'] = ApiClient.convertToType(data['language'], 'String');
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = ApiClient.convertToType(data['links'], [JobLinksInner]);
            }
            if (data.hasOwnProperty('location')) {
                obj['location'] = ApiClient.convertToType(data['location'], 'String');
            }
            if (data.hasOwnProperty('owner_id')) {
                obj['owner_id'] = ApiClient.convertToType(data['owner_id'], 'String');
            }
            if (data.hasOwnProperty('published_at')) {
                obj['published_at'] = ApiClient.convertToType(data['published_at'], 'Date');
            }
            if (data.hasOwnProperty('record_url')) {
                obj['record_url'] = ApiClient.convertToType(data['record_url'], 'String');
            }
            if (data.hasOwnProperty('recruiters')) {
                obj['recruiters'] = ApiClient.convertToType(data['recruiters'], ['String']);
            }
            if (data.hasOwnProperty('remote')) {
                obj['remote'] = ApiClient.convertToType(data['remote'], 'Boolean');
            }
            if (data.hasOwnProperty('requisition_id')) {
                obj['requisition_id'] = ApiClient.convertToType(data['requisition_id'], 'String');
            }
            if (data.hasOwnProperty('salary')) {
                obj['salary'] = JobSalary.constructFromObject(data['salary']);
            }
            if (data.hasOwnProperty('sequence')) {
                obj['sequence'] = ApiClient.convertToType(data['sequence'], 'Number');
            }
            if (data.hasOwnProperty('slug')) {
                obj['slug'] = ApiClient.convertToType(data['slug'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = JobStatus.constructFromObject(data['status']);
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], ['String']);
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'Date');
            }
            if (data.hasOwnProperty('updated_by')) {
                obj['updated_by'] = ApiClient.convertToType(data['updated_by'], 'String');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
            if (data.hasOwnProperty('visibility')) {
                obj['visibility'] = ApiClient.convertToType(data['visibility'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Job</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Job</code>.
     */
    static validateJSON(data) {
        if (data['addresses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['addresses'])) {
                throw new Error("Expected the field `addresses` to be an array in the JSON data but got " + data['addresses']);
            }
            // validate the optional field `addresses` (array)
            for (const item of data['addresses']) {
                Address.validateJSON(item);
            };
        }
        if (data['blocks']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['blocks'])) {
                throw new Error("Expected the field `blocks` to be an array in the JSON data but got " + data['blocks']);
            }
            // validate the optional field `blocks` (array)
            for (const item of data['blocks']) {
                JobBlocksInner.validateJSON(item);
            };
        }
        // validate the optional field `branch`
        if (data['branch']) { // data not null
          Branch.validateJSON(data['branch']);
        }
        // ensure the json data is a string
        if (data['closing'] && !(typeof data['closing'] === 'string' || data['closing'] instanceof String)) {
            throw new Error("Expected the field `closing` to be a primitive type in the JSON string but got " + data['closing']);
        }
        // ensure the json data is a string
        if (data['closing_html'] && !(typeof data['closing_html'] === 'string' || data['closing_html'] instanceof String)) {
            throw new Error("Expected the field `closing_html` to be a primitive type in the JSON string but got " + data['closing_html']);
        }
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
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
        // validate the optional field `department`
        if (data['department']) { // data not null
          Department.validateJSON(data['department']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['description_html'] && !(typeof data['description_html'] === 'string' || data['description_html'] instanceof String)) {
            throw new Error("Expected the field `description_html` to be a primitive type in the JSON string but got " + data['description_html']);
        }
        // ensure the json data is a string
        if (data['employment_terms'] && !(typeof data['employment_terms'] === 'string' || data['employment_terms'] instanceof String)) {
            throw new Error("Expected the field `employment_terms` to be a primitive type in the JSON string but got " + data['employment_terms']);
        }
        // ensure the json data is a string
        if (data['experience'] && !(typeof data['experience'] === 'string' || data['experience'] instanceof String)) {
            throw new Error("Expected the field `experience` to be a primitive type in the JSON string but got " + data['experience']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['followers'])) {
            throw new Error("Expected the field `followers` to be an array in the JSON data but got " + data['followers']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['hiring_managers'])) {
            throw new Error("Expected the field `hiring_managers` to be an array in the JSON data but got " + data['hiring_managers']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['job_portal_url'] && !(typeof data['job_portal_url'] === 'string' || data['job_portal_url'] instanceof String)) {
            throw new Error("Expected the field `job_portal_url` to be a primitive type in the JSON string but got " + data['job_portal_url']);
        }
        // ensure the json data is a string
        if (data['language'] && !(typeof data['language'] === 'string' || data['language'] instanceof String)) {
            throw new Error("Expected the field `language` to be a primitive type in the JSON string but got " + data['language']);
        }
        if (data['links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['links'])) {
                throw new Error("Expected the field `links` to be an array in the JSON data but got " + data['links']);
            }
            // validate the optional field `links` (array)
            for (const item of data['links']) {
                JobLinksInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['location'] && !(typeof data['location'] === 'string' || data['location'] instanceof String)) {
            throw new Error("Expected the field `location` to be a primitive type in the JSON string but got " + data['location']);
        }
        // ensure the json data is a string
        if (data['owner_id'] && !(typeof data['owner_id'] === 'string' || data['owner_id'] instanceof String)) {
            throw new Error("Expected the field `owner_id` to be a primitive type in the JSON string but got " + data['owner_id']);
        }
        // ensure the json data is a string
        if (data['record_url'] && !(typeof data['record_url'] === 'string' || data['record_url'] instanceof String)) {
            throw new Error("Expected the field `record_url` to be a primitive type in the JSON string but got " + data['record_url']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['recruiters'])) {
            throw new Error("Expected the field `recruiters` to be an array in the JSON data but got " + data['recruiters']);
        }
        // ensure the json data is a string
        if (data['requisition_id'] && !(typeof data['requisition_id'] === 'string' || data['requisition_id'] instanceof String)) {
            throw new Error("Expected the field `requisition_id` to be a primitive type in the JSON string but got " + data['requisition_id']);
        }
        // validate the optional field `salary`
        if (data['salary']) { // data not null
          JobSalary.validateJSON(data['salary']);
        }
        // ensure the json data is a string
        if (data['slug'] && !(typeof data['slug'] === 'string' || data['slug'] instanceof String)) {
            throw new Error("Expected the field `slug` to be a primitive type in the JSON string but got " + data['slug']);
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
        if (data['updated_by'] && !(typeof data['updated_by'] === 'string' || data['updated_by'] instanceof String)) {
            throw new Error("Expected the field `updated_by` to be a primitive type in the JSON string but got " + data['updated_by']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }
        // ensure the json data is a string
        if (data['visibility'] && !(typeof data['visibility'] === 'string' || data['visibility'] instanceof String)) {
            throw new Error("Expected the field `visibility` to be a primitive type in the JSON string but got " + data['visibility']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Address>} addresses
 */
Job.prototype['addresses'] = undefined;

/**
 * Specifies whether an employee of the organization can apply for the job.
 * @member {Boolean} available_to_employees
 */
Job.prototype['available_to_employees'] = undefined;

/**
 * @member {Array.<module:model/JobBlocksInner>} blocks
 */
Job.prototype['blocks'] = undefined;

/**
 * @member {module:model/Branch} branch
 */
Job.prototype['branch'] = undefined;

/**
 * @member {String} closing
 */
Job.prototype['closing'] = undefined;

/**
 * @member {Date} closing_date
 */
Job.prototype['closing_date'] = undefined;

/**
 * The closing section of the job description in HTML format
 * @member {String} closing_html
 */
Job.prototype['closing_html'] = undefined;

/**
 * The code of the job.
 * @member {String} code
 */
Job.prototype['code'] = undefined;

/**
 * @member {Boolean} confidential
 */
Job.prototype['confidential'] = undefined;

/**
 * The date and time when the object was created.
 * @member {Date} created_at
 */
Job.prototype['created_at'] = undefined;

/**
 * The user who created the object.
 * @member {String} created_by
 */
Job.prototype['created_by'] = undefined;

/**
 * @member {Array.<module:model/CustomField>} custom_fields
 */
Job.prototype['custom_fields'] = undefined;

/**
 * When custom mappings are configured on the resource, the result is included here.
 * @member {Object} custom_mappings
 */
Job.prototype['custom_mappings'] = undefined;

/**
 * Flag to indicate if the object is deleted.
 * @member {Boolean} deleted
 */
Job.prototype['deleted'] = undefined;

/**
 * @member {module:model/Department} department
 */
Job.prototype['department'] = undefined;

/**
 * A description of the object.
 * @member {String} description
 */
Job.prototype['description'] = undefined;

/**
 * The job description in HTML format
 * @member {String} description_html
 */
Job.prototype['description_html'] = undefined;

/**
 * @member {module:model/Job.EmploymentTermsEnum} employment_terms
 */
Job.prototype['employment_terms'] = undefined;

/**
 * Level of experience required for the job role.
 * @member {String} experience
 */
Job.prototype['experience'] = undefined;

/**
 * @member {Array.<String>} followers
 */
Job.prototype['followers'] = undefined;

/**
 * @member {Array.<String>} hiring_managers
 */
Job.prototype['hiring_managers'] = undefined;

/**
 * A unique identifier for an object.
 * @member {String} id
 */
Job.prototype['id'] = undefined;

/**
 * URL of the job portal
 * @member {String} job_portal_url
 */
Job.prototype['job_portal_url'] = undefined;

/**
 * language code according to ISO 639-1. For the United States - EN
 * @member {String} language
 */
Job.prototype['language'] = undefined;

/**
 * @member {Array.<module:model/JobLinksInner>} links
 */
Job.prototype['links'] = undefined;

/**
 * Specifies the location for the job posting.
 * @member {String} location
 */
Job.prototype['location'] = undefined;

/**
 * @member {String} owner_id
 */
Job.prototype['owner_id'] = undefined;

/**
 * @member {Date} published_at
 */
Job.prototype['published_at'] = undefined;

/**
 * @member {String} record_url
 */
Job.prototype['record_url'] = undefined;

/**
 * The recruiter is generally someone who is tasked to help the hiring manager find and screen qualified applicant
 * @member {Array.<String>} recruiters
 */
Job.prototype['recruiters'] = undefined;

/**
 * Specifies whether the posting is for a remote job.
 * @member {Boolean} remote
 */
Job.prototype['remote'] = undefined;

/**
 * A job's Requisition ID (Req ID) allows your organization to identify and track a job based on alphanumeric naming conventions unique to your company's internal processes.
 * @member {String} requisition_id
 */
Job.prototype['requisition_id'] = undefined;

/**
 * @member {module:model/JobSalary} salary
 */
Job.prototype['salary'] = undefined;

/**
 * Sequence in relation to other jobs.
 * @member {Number} sequence
 */
Job.prototype['sequence'] = undefined;

/**
 * @member {String} slug
 */
Job.prototype['slug'] = undefined;

/**
 * @member {module:model/JobStatus} status
 */
Job.prototype['status'] = undefined;

/**
 * @member {Array.<String>} tags
 */
Job.prototype['tags'] = undefined;

/**
 * The job title of the person.
 * @member {String} title
 */
Job.prototype['title'] = undefined;

/**
 * The date and time when the object was last updated.
 * @member {Date} updated_at
 */
Job.prototype['updated_at'] = undefined;

/**
 * The user who last updated the object.
 * @member {String} updated_by
 */
Job.prototype['updated_by'] = undefined;

/**
 * URL of the job description
 * @member {String} url
 */
Job.prototype['url'] = undefined;

/**
 * The visibility of the job
 * @member {module:model/Job.VisibilityEnum} visibility
 */
Job.prototype['visibility'] = undefined;





/**
 * Allowed values for the <code>employment_terms</code> property.
 * @enum {String}
 * @readonly
 */
Job['EmploymentTermsEnum'] = {

    /**
     * value: "full-time"
     * @const
     */
    "full-time": "full-time",

    /**
     * value: "part-time"
     * @const
     */
    "part-time": "part-time",

    /**
     * value: "internship"
     * @const
     */
    "internship": "internship",

    /**
     * value: "contractor"
     * @const
     */
    "contractor": "contractor",

    /**
     * value: "employee"
     * @const
     */
    "employee": "employee",

    /**
     * value: "freelance"
     * @const
     */
    "freelance": "freelance",

    /**
     * value: "temp"
     * @const
     */
    "temp": "temp",

    /**
     * value: "seasonal"
     * @const
     */
    "seasonal": "seasonal",

    /**
     * value: "volunteer"
     * @const
     */
    "volunteer": "volunteer",

    /**
     * value: "other"
     * @const
     */
    "other": "other"
};


/**
 * Allowed values for the <code>visibility</code> property.
 * @enum {String}
 * @readonly
 */
Job['VisibilityEnum'] = {

    /**
     * value: "draft"
     * @const
     */
    "draft": "draft",

    /**
     * value: "public"
     * @const
     */
    "public": "public",

    /**
     * value: "internal"
     * @const
     */
    "internal": "internal"
};



export default Job;

