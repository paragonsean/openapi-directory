/**
 * Connector API
 * Welcome to the Connector API.  You can use this API to access all Connector API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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
import ConnectorDoc from './ConnectorDoc';
import ConnectorEvent from './ConnectorEvent';
import ConnectorOauthScopesInner from './ConnectorOauthScopesInner';
import ConnectorSetting from './ConnectorSetting';
import ConnectorStatus from './ConnectorStatus';
import ConnectorTlsSupport from './ConnectorTlsSupport';
import ConnectorUnifiedApisInner from './ConnectorUnifiedApisInner';
import LinkedConnectorResource from './LinkedConnectorResource';
import SchemaSupport from './SchemaSupport';
import WebhookSupport from './WebhookSupport';

/**
 * The Connector model module.
 * @module model/Connector
 * @version 10.0.0
 */
class Connector {
    /**
     * Constructs a new <code>Connector</code>.
     * @alias module:model/Connector
     */
    constructor() { 
        
        Connector.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Connector</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Connector} obj Optional instance to populate.
     * @return {module:model/Connector} The populated <code>Connector</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Connector();

            if (data.hasOwnProperty('auth_only')) {
                obj['auth_only'] = ApiClient.convertToType(data['auth_only'], 'Boolean');
            }
            if (data.hasOwnProperty('auth_type')) {
                obj['auth_type'] = ApiClient.convertToType(data['auth_type'], 'String');
            }
            if (data.hasOwnProperty('blind_mapped')) {
                obj['blind_mapped'] = ApiClient.convertToType(data['blind_mapped'], 'Boolean');
            }
            if (data.hasOwnProperty('configurable_resources')) {
                obj['configurable_resources'] = ApiClient.convertToType(data['configurable_resources'], ['String']);
            }
            if (data.hasOwnProperty('custom_scopes')) {
                obj['custom_scopes'] = ApiClient.convertToType(data['custom_scopes'], 'Boolean');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('docs')) {
                obj['docs'] = ApiClient.convertToType(data['docs'], [ConnectorDoc]);
            }
            if (data.hasOwnProperty('free_trial_available')) {
                obj['free_trial_available'] = ApiClient.convertToType(data['free_trial_available'], 'Boolean');
            }
            if (data.hasOwnProperty('has_sandbox_credentials')) {
                obj['has_sandbox_credentials'] = ApiClient.convertToType(data['has_sandbox_credentials'], 'Boolean');
            }
            if (data.hasOwnProperty('icon_url')) {
                obj['icon_url'] = ApiClient.convertToType(data['icon_url'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('logo_url')) {
                obj['logo_url'] = ApiClient.convertToType(data['logo_url'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('oauth_credentials_source')) {
                obj['oauth_credentials_source'] = ApiClient.convertToType(data['oauth_credentials_source'], 'String');
            }
            if (data.hasOwnProperty('oauth_grant_type')) {
                obj['oauth_grant_type'] = ApiClient.convertToType(data['oauth_grant_type'], 'String');
            }
            if (data.hasOwnProperty('oauth_scopes')) {
                obj['oauth_scopes'] = ApiClient.convertToType(data['oauth_scopes'], [ConnectorOauthScopesInner]);
            }
            if (data.hasOwnProperty('partner_signup_url')) {
                obj['partner_signup_url'] = ApiClient.convertToType(data['partner_signup_url'], 'String');
            }
            if (data.hasOwnProperty('schema_support')) {
                obj['schema_support'] = SchemaSupport.constructFromObject(data['schema_support']);
            }
            if (data.hasOwnProperty('service_id')) {
                obj['service_id'] = ApiClient.convertToType(data['service_id'], 'String');
            }
            if (data.hasOwnProperty('settings')) {
                obj['settings'] = ApiClient.convertToType(data['settings'], [ConnectorSetting]);
            }
            if (data.hasOwnProperty('signup_url')) {
                obj['signup_url'] = ApiClient.convertToType(data['signup_url'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ConnectorStatus.constructFromObject(data['status']);
            }
            if (data.hasOwnProperty('supported_events')) {
                obj['supported_events'] = ApiClient.convertToType(data['supported_events'], [ConnectorEvent]);
            }
            if (data.hasOwnProperty('supported_resources')) {
                obj['supported_resources'] = ApiClient.convertToType(data['supported_resources'], [LinkedConnectorResource]);
            }
            if (data.hasOwnProperty('tls_support')) {
                obj['tls_support'] = ConnectorTlsSupport.constructFromObject(data['tls_support']);
            }
            if (data.hasOwnProperty('unified_apis')) {
                obj['unified_apis'] = ApiClient.convertToType(data['unified_apis'], [ConnectorUnifiedApisInner]);
            }
            if (data.hasOwnProperty('webhook_support')) {
                obj['webhook_support'] = WebhookSupport.constructFromObject(data['webhook_support']);
            }
            if (data.hasOwnProperty('website_url')) {
                obj['website_url'] = ApiClient.convertToType(data['website_url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Connector</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Connector</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['auth_type'] && !(typeof data['auth_type'] === 'string' || data['auth_type'] instanceof String)) {
            throw new Error("Expected the field `auth_type` to be a primitive type in the JSON string but got " + data['auth_type']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['configurable_resources'])) {
            throw new Error("Expected the field `configurable_resources` to be an array in the JSON data but got " + data['configurable_resources']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        if (data['docs']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['docs'])) {
                throw new Error("Expected the field `docs` to be an array in the JSON data but got " + data['docs']);
            }
            // validate the optional field `docs` (array)
            for (const item of data['docs']) {
                ConnectorDoc.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['icon_url'] && !(typeof data['icon_url'] === 'string' || data['icon_url'] instanceof String)) {
            throw new Error("Expected the field `icon_url` to be a primitive type in the JSON string but got " + data['icon_url']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['logo_url'] && !(typeof data['logo_url'] === 'string' || data['logo_url'] instanceof String)) {
            throw new Error("Expected the field `logo_url` to be a primitive type in the JSON string but got " + data['logo_url']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['oauth_credentials_source'] && !(typeof data['oauth_credentials_source'] === 'string' || data['oauth_credentials_source'] instanceof String)) {
            throw new Error("Expected the field `oauth_credentials_source` to be a primitive type in the JSON string but got " + data['oauth_credentials_source']);
        }
        // ensure the json data is a string
        if (data['oauth_grant_type'] && !(typeof data['oauth_grant_type'] === 'string' || data['oauth_grant_type'] instanceof String)) {
            throw new Error("Expected the field `oauth_grant_type` to be a primitive type in the JSON string but got " + data['oauth_grant_type']);
        }
        if (data['oauth_scopes']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['oauth_scopes'])) {
                throw new Error("Expected the field `oauth_scopes` to be an array in the JSON data but got " + data['oauth_scopes']);
            }
            // validate the optional field `oauth_scopes` (array)
            for (const item of data['oauth_scopes']) {
                ConnectorOauthScopesInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['partner_signup_url'] && !(typeof data['partner_signup_url'] === 'string' || data['partner_signup_url'] instanceof String)) {
            throw new Error("Expected the field `partner_signup_url` to be a primitive type in the JSON string but got " + data['partner_signup_url']);
        }
        // validate the optional field `schema_support`
        if (data['schema_support']) { // data not null
          SchemaSupport.validateJSON(data['schema_support']);
        }
        // ensure the json data is a string
        if (data['service_id'] && !(typeof data['service_id'] === 'string' || data['service_id'] instanceof String)) {
            throw new Error("Expected the field `service_id` to be a primitive type in the JSON string but got " + data['service_id']);
        }
        if (data['settings']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['settings'])) {
                throw new Error("Expected the field `settings` to be an array in the JSON data but got " + data['settings']);
            }
            // validate the optional field `settings` (array)
            for (const item of data['settings']) {
                ConnectorSetting.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['signup_url'] && !(typeof data['signup_url'] === 'string' || data['signup_url'] instanceof String)) {
            throw new Error("Expected the field `signup_url` to be a primitive type in the JSON string but got " + data['signup_url']);
        }
        if (data['supported_events']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['supported_events'])) {
                throw new Error("Expected the field `supported_events` to be an array in the JSON data but got " + data['supported_events']);
            }
            // validate the optional field `supported_events` (array)
            for (const item of data['supported_events']) {
                ConnectorEvent.validateJSON(item);
            };
        }
        if (data['supported_resources']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['supported_resources'])) {
                throw new Error("Expected the field `supported_resources` to be an array in the JSON data but got " + data['supported_resources']);
            }
            // validate the optional field `supported_resources` (array)
            for (const item of data['supported_resources']) {
                LinkedConnectorResource.validateJSON(item);
            };
        }
        // validate the optional field `tls_support`
        if (data['tls_support']) { // data not null
          ConnectorTlsSupport.validateJSON(data['tls_support']);
        }
        if (data['unified_apis']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['unified_apis'])) {
                throw new Error("Expected the field `unified_apis` to be an array in the JSON data but got " + data['unified_apis']);
            }
            // validate the optional field `unified_apis` (array)
            for (const item of data['unified_apis']) {
                ConnectorUnifiedApisInner.validateJSON(item);
            };
        }
        // validate the optional field `webhook_support`
        if (data['webhook_support']) { // data not null
          WebhookSupport.validateJSON(data['webhook_support']);
        }
        // ensure the json data is a string
        if (data['website_url'] && !(typeof data['website_url'] === 'string' || data['website_url'] instanceof String)) {
            throw new Error("Expected the field `website_url` to be a primitive type in the JSON string but got " + data['website_url']);
        }

        return true;
    }


}



/**
 * Indicates whether a connector only supports authentication. In this case the connector is not mapped to a Unified API, but can be used with the Proxy API
 * @member {Boolean} auth_only
 */
Connector.prototype['auth_only'] = undefined;

/**
 * Type of authorization used by the connector
 * @member {module:model/Connector.AuthTypeEnum} auth_type
 */
Connector.prototype['auth_type'] = undefined;

/**
 * Set to `true` when connector was implemented from downstream docs only and without API access. This state indicates that integration will require Apideck support, and access to downstream API to validate mapping quality.
 * @member {Boolean} blind_mapped
 */
Connector.prototype['blind_mapped'] = undefined;

/**
 * List of resources that have settings that can be configured.
 * @member {Array.<String>} configurable_resources
 */
Connector.prototype['configurable_resources'] = undefined;

/**
 * Set to `true` when connector allows the definition of custom scopes.
 * @member {Boolean} custom_scopes
 */
Connector.prototype['custom_scopes'] = undefined;

/**
 * A description of the object.
 * @member {String} description
 */
Connector.prototype['description'] = undefined;

/**
 * @member {Array.<module:model/ConnectorDoc>} docs
 */
Connector.prototype['docs'] = undefined;

/**
 * Set to `true` when the connector offers a free trial. Use `signup_url` to sign up for a free trial
 * @member {Boolean} free_trial_available
 */
Connector.prototype['free_trial_available'] = undefined;

/**
 * Indicates whether Apideck Sandbox OAuth credentials are available.
 * @member {Boolean} has_sandbox_credentials
 */
Connector.prototype['has_sandbox_credentials'] = undefined;

/**
 * Link to a small square icon for the connector.
 * @member {String} icon_url
 */
Connector.prototype['icon_url'] = undefined;

/**
 * ID of the connector.
 * @member {String} id
 */
Connector.prototype['id'] = undefined;

/**
 * Link to the full logo for the connector.
 * @member {String} logo_url
 */
Connector.prototype['logo_url'] = undefined;

/**
 * Name of the connector.
 * @member {String} name
 */
Connector.prototype['name'] = undefined;

/**
 * Location of the OAuth client credentials. For most connectors the OAuth client credentials are stored on integration and managed by the application owner. For others they are stored on connection and managed by the consumer in Vault.
 * @member {module:model/Connector.OauthCredentialsSourceEnum} oauth_credentials_source
 */
Connector.prototype['oauth_credentials_source'] = undefined;

/**
 * OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types
 * @member {module:model/Connector.OauthGrantTypeEnum} oauth_grant_type
 */
Connector.prototype['oauth_grant_type'] = undefined;

/**
 * List of OAuth Scopes available for this connector.
 * @member {Array.<module:model/ConnectorOauthScopesInner>} oauth_scopes
 */
Connector.prototype['oauth_scopes'] = undefined;

/**
 * Link to the connector's partner program signup page.
 * @member {String} partner_signup_url
 */
Connector.prototype['partner_signup_url'] = undefined;

/**
 * @member {module:model/SchemaSupport} schema_support
 */
Connector.prototype['schema_support'] = undefined;

/**
 * Service provider identifier
 * @member {String} service_id
 */
Connector.prototype['service_id'] = undefined;

/**
 * @member {Array.<module:model/ConnectorSetting>} settings
 */
Connector.prototype['settings'] = undefined;

/**
 * Link to the connector's signup page.
 * @member {String} signup_url
 */
Connector.prototype['signup_url'] = undefined;

/**
 * @member {module:model/ConnectorStatus} status
 */
Connector.prototype['status'] = undefined;

/**
 * List of events that are supported on the connector across all Unified APIs.
 * @member {Array.<module:model/ConnectorEvent>} supported_events
 */
Connector.prototype['supported_events'] = undefined;

/**
 * List of resources that are supported on the connector.
 * @member {Array.<module:model/LinkedConnectorResource>} supported_resources
 */
Connector.prototype['supported_resources'] = undefined;

/**
 * @member {module:model/ConnectorTlsSupport} tls_support
 */
Connector.prototype['tls_support'] = undefined;

/**
 * List of Unified APIs that feature this connector.
 * @member {Array.<module:model/ConnectorUnifiedApisInner>} unified_apis
 */
Connector.prototype['unified_apis'] = undefined;

/**
 * @member {module:model/WebhookSupport} webhook_support
 */
Connector.prototype['webhook_support'] = undefined;

/**
 * Link to the connector's website.
 * @member {String} website_url
 */
Connector.prototype['website_url'] = undefined;





/**
 * Allowed values for the <code>auth_type</code> property.
 * @enum {String}
 * @readonly
 */
Connector['AuthTypeEnum'] = {

    /**
     * value: "oauth2"
     * @const
     */
    "oauth2": "oauth2",

    /**
     * value: "apiKey"
     * @const
     */
    "apiKey": "apiKey",

    /**
     * value: "basic"
     * @const
     */
    "basic": "basic",

    /**
     * value: "custom"
     * @const
     */
    "custom": "custom",

    /**
     * value: "none"
     * @const
     */
    "none": "none"
};


/**
 * Allowed values for the <code>oauth_credentials_source</code> property.
 * @enum {String}
 * @readonly
 */
Connector['OauthCredentialsSourceEnum'] = {

    /**
     * value: "integration"
     * @const
     */
    "integration": "integration",

    /**
     * value: "connection"
     * @const
     */
    "connection": "connection"
};


/**
 * Allowed values for the <code>oauth_grant_type</code> property.
 * @enum {String}
 * @readonly
 */
Connector['OauthGrantTypeEnum'] = {

    /**
     * value: "authorization_code"
     * @const
     */
    "authorization_code": "authorization_code",

    /**
     * value: "client_credentials"
     * @const
     */
    "client_credentials": "client_credentials",

    /**
     * value: "password"
     * @const
     */
    "password": "password"
};



export default Connector;

