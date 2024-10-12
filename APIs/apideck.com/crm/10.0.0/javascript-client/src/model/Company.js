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
import Address from './Address';
import BankAccount from './BankAccount';
import CompanyRowType from './CompanyRowType';
import Currency from './Currency';
import CustomField from './CustomField';
import Email from './Email';
import PhoneNumber from './PhoneNumber';
import SocialLink from './SocialLink';
import Website from './Website';

/**
 * The Company model module.
 * @module model/Company
 * @version 10.0.0
 */
class Company {
    /**
     * Constructs a new <code>Company</code>.
     * @alias module:model/Company
     * @param name {String} Name of the company
     */
    constructor(name) { 
        
        Company.initialize(this, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name) { 
        obj['name'] = name;
    }

    /**
     * Constructs a <code>Company</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Company} obj Optional instance to populate.
     * @return {module:model/Company} The populated <code>Company</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Company();

            if (data.hasOwnProperty('abn_branch')) {
                obj['abn_branch'] = ApiClient.convertToType(data['abn_branch'], 'String');
            }
            if (data.hasOwnProperty('abn_or_tfn')) {
                obj['abn_or_tfn'] = ApiClient.convertToType(data['abn_or_tfn'], 'String');
            }
            if (data.hasOwnProperty('acn')) {
                obj['acn'] = ApiClient.convertToType(data['acn'], 'String');
            }
            if (data.hasOwnProperty('addresses')) {
                obj['addresses'] = ApiClient.convertToType(data['addresses'], [Address]);
            }
            if (data.hasOwnProperty('annual_revenue')) {
                obj['annual_revenue'] = ApiClient.convertToType(data['annual_revenue'], 'String');
            }
            if (data.hasOwnProperty('bank_accounts')) {
                obj['bank_accounts'] = ApiClient.convertToType(data['bank_accounts'], [BankAccount]);
            }
            if (data.hasOwnProperty('birthday')) {
                obj['birthday'] = ApiClient.convertToType(data['birthday'], 'Date');
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
            if (data.hasOwnProperty('deleted')) {
                obj['deleted'] = ApiClient.convertToType(data['deleted'], 'Boolean');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('emails')) {
                obj['emails'] = ApiClient.convertToType(data['emails'], [Email]);
            }
            if (data.hasOwnProperty('fax')) {
                obj['fax'] = ApiClient.convertToType(data['fax'], 'String');
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = ApiClient.convertToType(data['image'], 'String');
            }
            if (data.hasOwnProperty('industry')) {
                obj['industry'] = ApiClient.convertToType(data['industry'], 'String');
            }
            if (data.hasOwnProperty('interaction_count')) {
                obj['interaction_count'] = ApiClient.convertToType(data['interaction_count'], 'Number');
            }
            if (data.hasOwnProperty('last_activity_at')) {
                obj['last_activity_at'] = ApiClient.convertToType(data['last_activity_at'], 'Date');
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('number_of_employees')) {
                obj['number_of_employees'] = ApiClient.convertToType(data['number_of_employees'], 'String');
            }
            if (data.hasOwnProperty('owner_id')) {
                obj['owner_id'] = ApiClient.convertToType(data['owner_id'], 'String');
            }
            if (data.hasOwnProperty('ownership')) {
                obj['ownership'] = ApiClient.convertToType(data['ownership'], 'String');
            }
            if (data.hasOwnProperty('parent_id')) {
                obj['parent_id'] = ApiClient.convertToType(data['parent_id'], 'String');
            }
            if (data.hasOwnProperty('payee_number')) {
                obj['payee_number'] = ApiClient.convertToType(data['payee_number'], 'String');
            }
            if (data.hasOwnProperty('phone_numbers')) {
                obj['phone_numbers'] = ApiClient.convertToType(data['phone_numbers'], [PhoneNumber]);
            }
            if (data.hasOwnProperty('read_only')) {
                obj['read_only'] = ApiClient.convertToType(data['read_only'], 'Boolean');
            }
            if (data.hasOwnProperty('row_type')) {
                obj['row_type'] = CompanyRowType.constructFromObject(data['row_type']);
            }
            if (data.hasOwnProperty('sales_tax_number')) {
                obj['sales_tax_number'] = ApiClient.convertToType(data['sales_tax_number'], 'String');
            }
            if (data.hasOwnProperty('salutation')) {
                obj['salutation'] = ApiClient.convertToType(data['salutation'], 'String');
            }
            if (data.hasOwnProperty('social_links')) {
                obj['social_links'] = ApiClient.convertToType(data['social_links'], [SocialLink]);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], ['String']);
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'Date');
            }
            if (data.hasOwnProperty('updated_by')) {
                obj['updated_by'] = ApiClient.convertToType(data['updated_by'], 'String');
            }
            if (data.hasOwnProperty('vat_number')) {
                obj['vat_number'] = ApiClient.convertToType(data['vat_number'], 'String');
            }
            if (data.hasOwnProperty('websites')) {
                obj['websites'] = ApiClient.convertToType(data['websites'], [Website]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Company</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Company</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Company.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['abn_branch'] && !(typeof data['abn_branch'] === 'string' || data['abn_branch'] instanceof String)) {
            throw new Error("Expected the field `abn_branch` to be a primitive type in the JSON string but got " + data['abn_branch']);
        }
        // ensure the json data is a string
        if (data['abn_or_tfn'] && !(typeof data['abn_or_tfn'] === 'string' || data['abn_or_tfn'] instanceof String)) {
            throw new Error("Expected the field `abn_or_tfn` to be a primitive type in the JSON string but got " + data['abn_or_tfn']);
        }
        // ensure the json data is a string
        if (data['acn'] && !(typeof data['acn'] === 'string' || data['acn'] instanceof String)) {
            throw new Error("Expected the field `acn` to be a primitive type in the JSON string but got " + data['acn']);
        }
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
        // ensure the json data is a string
        if (data['annual_revenue'] && !(typeof data['annual_revenue'] === 'string' || data['annual_revenue'] instanceof String)) {
            throw new Error("Expected the field `annual_revenue` to be a primitive type in the JSON string but got " + data['annual_revenue']);
        }
        if (data['bank_accounts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['bank_accounts'])) {
                throw new Error("Expected the field `bank_accounts` to be an array in the JSON data but got " + data['bank_accounts']);
            }
            // validate the optional field `bank_accounts` (array)
            for (const item of data['bank_accounts']) {
                BankAccount.validateJSON(item);
            };
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
        if (data['emails']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['emails'])) {
                throw new Error("Expected the field `emails` to be an array in the JSON data but got " + data['emails']);
            }
            // validate the optional field `emails` (array)
            for (const item of data['emails']) {
                Email.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['fax'] && !(typeof data['fax'] === 'string' || data['fax'] instanceof String)) {
            throw new Error("Expected the field `fax` to be a primitive type in the JSON string but got " + data['fax']);
        }
        // ensure the json data is a string
        if (data['first_name'] && !(typeof data['first_name'] === 'string' || data['first_name'] instanceof String)) {
            throw new Error("Expected the field `first_name` to be a primitive type in the JSON string but got " + data['first_name']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['image'] && !(typeof data['image'] === 'string' || data['image'] instanceof String)) {
            throw new Error("Expected the field `image` to be a primitive type in the JSON string but got " + data['image']);
        }
        // ensure the json data is a string
        if (data['industry'] && !(typeof data['industry'] === 'string' || data['industry'] instanceof String)) {
            throw new Error("Expected the field `industry` to be a primitive type in the JSON string but got " + data['industry']);
        }
        // ensure the json data is a string
        if (data['last_name'] && !(typeof data['last_name'] === 'string' || data['last_name'] instanceof String)) {
            throw new Error("Expected the field `last_name` to be a primitive type in the JSON string but got " + data['last_name']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['number_of_employees'] && !(typeof data['number_of_employees'] === 'string' || data['number_of_employees'] instanceof String)) {
            throw new Error("Expected the field `number_of_employees` to be a primitive type in the JSON string but got " + data['number_of_employees']);
        }
        // ensure the json data is a string
        if (data['owner_id'] && !(typeof data['owner_id'] === 'string' || data['owner_id'] instanceof String)) {
            throw new Error("Expected the field `owner_id` to be a primitive type in the JSON string but got " + data['owner_id']);
        }
        // ensure the json data is a string
        if (data['ownership'] && !(typeof data['ownership'] === 'string' || data['ownership'] instanceof String)) {
            throw new Error("Expected the field `ownership` to be a primitive type in the JSON string but got " + data['ownership']);
        }
        // ensure the json data is a string
        if (data['parent_id'] && !(typeof data['parent_id'] === 'string' || data['parent_id'] instanceof String)) {
            throw new Error("Expected the field `parent_id` to be a primitive type in the JSON string but got " + data['parent_id']);
        }
        // ensure the json data is a string
        if (data['payee_number'] && !(typeof data['payee_number'] === 'string' || data['payee_number'] instanceof String)) {
            throw new Error("Expected the field `payee_number` to be a primitive type in the JSON string but got " + data['payee_number']);
        }
        if (data['phone_numbers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['phone_numbers'])) {
                throw new Error("Expected the field `phone_numbers` to be an array in the JSON data but got " + data['phone_numbers']);
            }
            // validate the optional field `phone_numbers` (array)
            for (const item of data['phone_numbers']) {
                PhoneNumber.validateJSON(item);
            };
        }
        // validate the optional field `row_type`
        if (data['row_type']) { // data not null
          CompanyRowType.validateJSON(data['row_type']);
        }
        // ensure the json data is a string
        if (data['sales_tax_number'] && !(typeof data['sales_tax_number'] === 'string' || data['sales_tax_number'] instanceof String)) {
            throw new Error("Expected the field `sales_tax_number` to be a primitive type in the JSON string but got " + data['sales_tax_number']);
        }
        // ensure the json data is a string
        if (data['salutation'] && !(typeof data['salutation'] === 'string' || data['salutation'] instanceof String)) {
            throw new Error("Expected the field `salutation` to be a primitive type in the JSON string but got " + data['salutation']);
        }
        if (data['social_links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['social_links'])) {
                throw new Error("Expected the field `social_links` to be an array in the JSON data but got " + data['social_links']);
            }
            // validate the optional field `social_links` (array)
            for (const item of data['social_links']) {
                SocialLink.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['tags'])) {
            throw new Error("Expected the field `tags` to be an array in the JSON data but got " + data['tags']);
        }
        // ensure the json data is a string
        if (data['updated_by'] && !(typeof data['updated_by'] === 'string' || data['updated_by'] instanceof String)) {
            throw new Error("Expected the field `updated_by` to be a primitive type in the JSON string but got " + data['updated_by']);
        }
        // ensure the json data is a string
        if (data['vat_number'] && !(typeof data['vat_number'] === 'string' || data['vat_number'] instanceof String)) {
            throw new Error("Expected the field `vat_number` to be a primitive type in the JSON string but got " + data['vat_number']);
        }
        if (data['websites']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['websites'])) {
                throw new Error("Expected the field `websites` to be an array in the JSON data but got " + data['websites']);
            }
            // validate the optional field `websites` (array)
            for (const item of data['websites']) {
                Website.validateJSON(item);
            };
        }

        return true;
    }


}

Company.RequiredProperties = ["name"];

/**
 * An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity.
 * @member {String} abn_branch
 */
Company.prototype['abn_branch'] = undefined;

/**
 * An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia.
 * @member {String} abn_or_tfn
 */
Company.prototype['abn_or_tfn'] = undefined;

/**
 * The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank.
 * @member {String} acn
 */
Company.prototype['acn'] = undefined;

/**
 * @member {Array.<module:model/Address>} addresses
 */
Company.prototype['addresses'] = undefined;

/**
 * The annual revenue of the company
 * @member {String} annual_revenue
 */
Company.prototype['annual_revenue'] = undefined;

/**
 * @member {Array.<module:model/BankAccount>} bank_accounts
 */
Company.prototype['bank_accounts'] = undefined;

/**
 * The date of birth of the person.
 * @member {Date} birthday
 */
Company.prototype['birthday'] = undefined;

/**
 * Creation date
 * @member {Date} created_at
 */
Company.prototype['created_at'] = undefined;

/**
 * Created by user ID
 * @member {String} created_by
 */
Company.prototype['created_by'] = undefined;

/**
 * @member {module:model/Currency} currency
 */
Company.prototype['currency'] = undefined;

/**
 * @member {Array.<module:model/CustomField>} custom_fields
 */
Company.prototype['custom_fields'] = undefined;

/**
 * When custom mappings are configured on the resource, the result is included here.
 * @member {Object} custom_mappings
 */
Company.prototype['custom_mappings'] = undefined;

/**
 * Whether the company is deleted or not
 * @member {Boolean} deleted
 */
Company.prototype['deleted'] = undefined;

/**
 * A description of the company
 * @member {String} description
 */
Company.prototype['description'] = undefined;

/**
 * @member {Array.<module:model/Email>} emails
 */
Company.prototype['emails'] = undefined;

/**
 * The fax number of the company
 * @member {String} fax
 */
Company.prototype['fax'] = undefined;

/**
 * The first name of the person.
 * @member {String} first_name
 */
Company.prototype['first_name'] = undefined;

/**
 * Unique identifier for the company
 * @member {String} id
 */
Company.prototype['id'] = undefined;

/**
 * The Image URL of the company
 * @member {String} image
 */
Company.prototype['image'] = undefined;

/**
 * The industry represents the type of business the company is in.
 * @member {String} industry
 */
Company.prototype['industry'] = undefined;

/**
 * Number of interactions
 * @member {Number} interaction_count
 */
Company.prototype['interaction_count'] = undefined;

/**
 * Last activity date
 * @member {Date} last_activity_at
 */
Company.prototype['last_activity_at'] = undefined;

/**
 * The last name of the person.
 * @member {String} last_name
 */
Company.prototype['last_name'] = undefined;

/**
 * Name of the company
 * @member {String} name
 */
Company.prototype['name'] = undefined;

/**
 * Number of employees
 * @member {String} number_of_employees
 */
Company.prototype['number_of_employees'] = undefined;

/**
 * Owner ID
 * @member {String} owner_id
 */
Company.prototype['owner_id'] = undefined;

/**
 * The ownership indicates the type of ownership of the company.
 * @member {String} ownership
 */
Company.prototype['ownership'] = undefined;

/**
 * Parent ID
 * @member {String} parent_id
 */
Company.prototype['parent_id'] = undefined;

/**
 * A payee number is a unique number that identifies a payee for tax purposes.
 * @member {String} payee_number
 */
Company.prototype['payee_number'] = undefined;

/**
 * @member {Array.<module:model/PhoneNumber>} phone_numbers
 */
Company.prototype['phone_numbers'] = undefined;

/**
 * Whether the company is read-only or not
 * @member {Boolean} read_only
 */
Company.prototype['read_only'] = undefined;

/**
 * @member {module:model/CompanyRowType} row_type
 */
Company.prototype['row_type'] = undefined;

/**
 * A sales tax number is a unique number that identifies a company for tax purposes.
 * @member {String} sales_tax_number
 */
Company.prototype['sales_tax_number'] = undefined;

/**
 * A formal salutation for the person. For example, 'Mr', 'Mrs'
 * @member {String} salutation
 */
Company.prototype['salutation'] = undefined;

/**
 * @member {Array.<module:model/SocialLink>} social_links
 */
Company.prototype['social_links'] = undefined;

/**
 * The status of the company
 * @member {String} status
 */
Company.prototype['status'] = undefined;

/**
 * @member {Array.<String>} tags
 */
Company.prototype['tags'] = undefined;

/**
 * Last updated date
 * @member {Date} updated_at
 */
Company.prototype['updated_at'] = undefined;

/**
 * Updated by user ID
 * @member {String} updated_by
 */
Company.prototype['updated_by'] = undefined;

/**
 * The VAT number of the company
 * @member {String} vat_number
 */
Company.prototype['vat_number'] = undefined;

/**
 * @member {Array.<module:model/Website>} websites
 */
Company.prototype['websites'] = undefined;






export default Company;

