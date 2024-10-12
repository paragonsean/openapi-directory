/**
 * Issue Tracking API
 * Welcome to the Issue Tracking API.  You can use this API to access all Issue Tracking API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It's most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency's smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
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
/**
* Enum class Currency.
* @enum {}
* @readonly
*/
export default class Currency {
    
        /**
         * value: "UNKNOWN_CURRENCY"
         * @const
         */
        "UNKNOWN_CURRENCY" = "UNKNOWN_CURRENCY";

    
        /**
         * value: "AED"
         * @const
         */
        "AED" = "AED";

    
        /**
         * value: "AFN"
         * @const
         */
        "AFN" = "AFN";

    
        /**
         * value: "ALL"
         * @const
         */
        "ALL" = "ALL";

    
        /**
         * value: "AMD"
         * @const
         */
        "AMD" = "AMD";

    
        /**
         * value: "ANG"
         * @const
         */
        "ANG" = "ANG";

    
        /**
         * value: "AOA"
         * @const
         */
        "AOA" = "AOA";

    
        /**
         * value: "ARS"
         * @const
         */
        "ARS" = "ARS";

    
        /**
         * value: "AUD"
         * @const
         */
        "AUD" = "AUD";

    
        /**
         * value: "AWG"
         * @const
         */
        "AWG" = "AWG";

    
        /**
         * value: "AZN"
         * @const
         */
        "AZN" = "AZN";

    
        /**
         * value: "BAM"
         * @const
         */
        "BAM" = "BAM";

    
        /**
         * value: "BBD"
         * @const
         */
        "BBD" = "BBD";

    
        /**
         * value: "BDT"
         * @const
         */
        "BDT" = "BDT";

    
        /**
         * value: "BGN"
         * @const
         */
        "BGN" = "BGN";

    
        /**
         * value: "BHD"
         * @const
         */
        "BHD" = "BHD";

    
        /**
         * value: "BIF"
         * @const
         */
        "BIF" = "BIF";

    
        /**
         * value: "BMD"
         * @const
         */
        "BMD" = "BMD";

    
        /**
         * value: "BND"
         * @const
         */
        "BND" = "BND";

    
        /**
         * value: "BOB"
         * @const
         */
        "BOB" = "BOB";

    
        /**
         * value: "BOV"
         * @const
         */
        "BOV" = "BOV";

    
        /**
         * value: "BRL"
         * @const
         */
        "BRL" = "BRL";

    
        /**
         * value: "BSD"
         * @const
         */
        "BSD" = "BSD";

    
        /**
         * value: "BTN"
         * @const
         */
        "BTN" = "BTN";

    
        /**
         * value: "BWP"
         * @const
         */
        "BWP" = "BWP";

    
        /**
         * value: "BYR"
         * @const
         */
        "BYR" = "BYR";

    
        /**
         * value: "BZD"
         * @const
         */
        "BZD" = "BZD";

    
        /**
         * value: "CAD"
         * @const
         */
        "CAD" = "CAD";

    
        /**
         * value: "CDF"
         * @const
         */
        "CDF" = "CDF";

    
        /**
         * value: "CHE"
         * @const
         */
        "CHE" = "CHE";

    
        /**
         * value: "CHF"
         * @const
         */
        "CHF" = "CHF";

    
        /**
         * value: "CHW"
         * @const
         */
        "CHW" = "CHW";

    
        /**
         * value: "CLF"
         * @const
         */
        "CLF" = "CLF";

    
        /**
         * value: "CLP"
         * @const
         */
        "CLP" = "CLP";

    
        /**
         * value: "CNY"
         * @const
         */
        "CNY" = "CNY";

    
        /**
         * value: "COP"
         * @const
         */
        "COP" = "COP";

    
        /**
         * value: "COU"
         * @const
         */
        "COU" = "COU";

    
        /**
         * value: "CRC"
         * @const
         */
        "CRC" = "CRC";

    
        /**
         * value: "CUC"
         * @const
         */
        "CUC" = "CUC";

    
        /**
         * value: "CUP"
         * @const
         */
        "CUP" = "CUP";

    
        /**
         * value: "CVE"
         * @const
         */
        "CVE" = "CVE";

    
        /**
         * value: "CZK"
         * @const
         */
        "CZK" = "CZK";

    
        /**
         * value: "DJF"
         * @const
         */
        "DJF" = "DJF";

    
        /**
         * value: "DKK"
         * @const
         */
        "DKK" = "DKK";

    
        /**
         * value: "DOP"
         * @const
         */
        "DOP" = "DOP";

    
        /**
         * value: "DZD"
         * @const
         */
        "DZD" = "DZD";

    
        /**
         * value: "EGP"
         * @const
         */
        "EGP" = "EGP";

    
        /**
         * value: "ERN"
         * @const
         */
        "ERN" = "ERN";

    
        /**
         * value: "ETB"
         * @const
         */
        "ETB" = "ETB";

    
        /**
         * value: "EUR"
         * @const
         */
        "EUR" = "EUR";

    
        /**
         * value: "FJD"
         * @const
         */
        "FJD" = "FJD";

    
        /**
         * value: "FKP"
         * @const
         */
        "FKP" = "FKP";

    
        /**
         * value: "GBP"
         * @const
         */
        "GBP" = "GBP";

    
        /**
         * value: "GEL"
         * @const
         */
        "GEL" = "GEL";

    
        /**
         * value: "GHS"
         * @const
         */
        "GHS" = "GHS";

    
        /**
         * value: "GIP"
         * @const
         */
        "GIP" = "GIP";

    
        /**
         * value: "GMD"
         * @const
         */
        "GMD" = "GMD";

    
        /**
         * value: "GNF"
         * @const
         */
        "GNF" = "GNF";

    
        /**
         * value: "GTQ"
         * @const
         */
        "GTQ" = "GTQ";

    
        /**
         * value: "GYD"
         * @const
         */
        "GYD" = "GYD";

    
        /**
         * value: "HKD"
         * @const
         */
        "HKD" = "HKD";

    
        /**
         * value: "HNL"
         * @const
         */
        "HNL" = "HNL";

    
        /**
         * value: "HRK"
         * @const
         */
        "HRK" = "HRK";

    
        /**
         * value: "HTG"
         * @const
         */
        "HTG" = "HTG";

    
        /**
         * value: "HUF"
         * @const
         */
        "HUF" = "HUF";

    
        /**
         * value: "IDR"
         * @const
         */
        "IDR" = "IDR";

    
        /**
         * value: "ILS"
         * @const
         */
        "ILS" = "ILS";

    
        /**
         * value: "INR"
         * @const
         */
        "INR" = "INR";

    
        /**
         * value: "IQD"
         * @const
         */
        "IQD" = "IQD";

    
        /**
         * value: "IRR"
         * @const
         */
        "IRR" = "IRR";

    
        /**
         * value: "ISK"
         * @const
         */
        "ISK" = "ISK";

    
        /**
         * value: "JMD"
         * @const
         */
        "JMD" = "JMD";

    
        /**
         * value: "JOD"
         * @const
         */
        "JOD" = "JOD";

    
        /**
         * value: "JPY"
         * @const
         */
        "JPY" = "JPY";

    
        /**
         * value: "KES"
         * @const
         */
        "KES" = "KES";

    
        /**
         * value: "KGS"
         * @const
         */
        "KGS" = "KGS";

    
        /**
         * value: "KHR"
         * @const
         */
        "KHR" = "KHR";

    
        /**
         * value: "KMF"
         * @const
         */
        "KMF" = "KMF";

    
        /**
         * value: "KPW"
         * @const
         */
        "KPW" = "KPW";

    
        /**
         * value: "KRW"
         * @const
         */
        "KRW" = "KRW";

    
        /**
         * value: "KWD"
         * @const
         */
        "KWD" = "KWD";

    
        /**
         * value: "KYD"
         * @const
         */
        "KYD" = "KYD";

    
        /**
         * value: "KZT"
         * @const
         */
        "KZT" = "KZT";

    
        /**
         * value: "LAK"
         * @const
         */
        "LAK" = "LAK";

    
        /**
         * value: "LBP"
         * @const
         */
        "LBP" = "LBP";

    
        /**
         * value: "LKR"
         * @const
         */
        "LKR" = "LKR";

    
        /**
         * value: "LRD"
         * @const
         */
        "LRD" = "LRD";

    
        /**
         * value: "LSL"
         * @const
         */
        "LSL" = "LSL";

    
        /**
         * value: "LTL"
         * @const
         */
        "LTL" = "LTL";

    
        /**
         * value: "LVL"
         * @const
         */
        "LVL" = "LVL";

    
        /**
         * value: "LYD"
         * @const
         */
        "LYD" = "LYD";

    
        /**
         * value: "MAD"
         * @const
         */
        "MAD" = "MAD";

    
        /**
         * value: "MDL"
         * @const
         */
        "MDL" = "MDL";

    
        /**
         * value: "MGA"
         * @const
         */
        "MGA" = "MGA";

    
        /**
         * value: "MKD"
         * @const
         */
        "MKD" = "MKD";

    
        /**
         * value: "MMK"
         * @const
         */
        "MMK" = "MMK";

    
        /**
         * value: "MNT"
         * @const
         */
        "MNT" = "MNT";

    
        /**
         * value: "MOP"
         * @const
         */
        "MOP" = "MOP";

    
        /**
         * value: "MRO"
         * @const
         */
        "MRO" = "MRO";

    
        /**
         * value: "MUR"
         * @const
         */
        "MUR" = "MUR";

    
        /**
         * value: "MVR"
         * @const
         */
        "MVR" = "MVR";

    
        /**
         * value: "MWK"
         * @const
         */
        "MWK" = "MWK";

    
        /**
         * value: "MXN"
         * @const
         */
        "MXN" = "MXN";

    
        /**
         * value: "MXV"
         * @const
         */
        "MXV" = "MXV";

    
        /**
         * value: "MYR"
         * @const
         */
        "MYR" = "MYR";

    
        /**
         * value: "MZN"
         * @const
         */
        "MZN" = "MZN";

    
        /**
         * value: "NAD"
         * @const
         */
        "NAD" = "NAD";

    
        /**
         * value: "NGN"
         * @const
         */
        "NGN" = "NGN";

    
        /**
         * value: "NIO"
         * @const
         */
        "NIO" = "NIO";

    
        /**
         * value: "NOK"
         * @const
         */
        "NOK" = "NOK";

    
        /**
         * value: "NPR"
         * @const
         */
        "NPR" = "NPR";

    
        /**
         * value: "NZD"
         * @const
         */
        "NZD" = "NZD";

    
        /**
         * value: "OMR"
         * @const
         */
        "OMR" = "OMR";

    
        /**
         * value: "PAB"
         * @const
         */
        "PAB" = "PAB";

    
        /**
         * value: "PEN"
         * @const
         */
        "PEN" = "PEN";

    
        /**
         * value: "PGK"
         * @const
         */
        "PGK" = "PGK";

    
        /**
         * value: "PHP"
         * @const
         */
        "PHP" = "PHP";

    
        /**
         * value: "PKR"
         * @const
         */
        "PKR" = "PKR";

    
        /**
         * value: "PLN"
         * @const
         */
        "PLN" = "PLN";

    
        /**
         * value: "PYG"
         * @const
         */
        "PYG" = "PYG";

    
        /**
         * value: "QAR"
         * @const
         */
        "QAR" = "QAR";

    
        /**
         * value: "RON"
         * @const
         */
        "RON" = "RON";

    
        /**
         * value: "RSD"
         * @const
         */
        "RSD" = "RSD";

    
        /**
         * value: "RUB"
         * @const
         */
        "RUB" = "RUB";

    
        /**
         * value: "RWF"
         * @const
         */
        "RWF" = "RWF";

    
        /**
         * value: "SAR"
         * @const
         */
        "SAR" = "SAR";

    
        /**
         * value: "SBD"
         * @const
         */
        "SBD" = "SBD";

    
        /**
         * value: "SCR"
         * @const
         */
        "SCR" = "SCR";

    
        /**
         * value: "SDG"
         * @const
         */
        "SDG" = "SDG";

    
        /**
         * value: "SEK"
         * @const
         */
        "SEK" = "SEK";

    
        /**
         * value: "SGD"
         * @const
         */
        "SGD" = "SGD";

    
        /**
         * value: "SHP"
         * @const
         */
        "SHP" = "SHP";

    
        /**
         * value: "SLL"
         * @const
         */
        "SLL" = "SLL";

    
        /**
         * value: "SOS"
         * @const
         */
        "SOS" = "SOS";

    
        /**
         * value: "SRD"
         * @const
         */
        "SRD" = "SRD";

    
        /**
         * value: "SSP"
         * @const
         */
        "SSP" = "SSP";

    
        /**
         * value: "STD"
         * @const
         */
        "STD" = "STD";

    
        /**
         * value: "SVC"
         * @const
         */
        "SVC" = "SVC";

    
        /**
         * value: "SYP"
         * @const
         */
        "SYP" = "SYP";

    
        /**
         * value: "SZL"
         * @const
         */
        "SZL" = "SZL";

    
        /**
         * value: "THB"
         * @const
         */
        "THB" = "THB";

    
        /**
         * value: "TJS"
         * @const
         */
        "TJS" = "TJS";

    
        /**
         * value: "TMT"
         * @const
         */
        "TMT" = "TMT";

    
        /**
         * value: "TND"
         * @const
         */
        "TND" = "TND";

    
        /**
         * value: "TOP"
         * @const
         */
        "TOP" = "TOP";

    
        /**
         * value: "TRC"
         * @const
         */
        "TRC" = "TRC";

    
        /**
         * value: "TRY"
         * @const
         */
        "TRY" = "TRY";

    
        /**
         * value: "TTD"
         * @const
         */
        "TTD" = "TTD";

    
        /**
         * value: "TWD"
         * @const
         */
        "TWD" = "TWD";

    
        /**
         * value: "TZS"
         * @const
         */
        "TZS" = "TZS";

    
        /**
         * value: "UAH"
         * @const
         */
        "UAH" = "UAH";

    
        /**
         * value: "UGX"
         * @const
         */
        "UGX" = "UGX";

    
        /**
         * value: "USD"
         * @const
         */
        "USD" = "USD";

    
        /**
         * value: "USN"
         * @const
         */
        "USN" = "USN";

    
        /**
         * value: "USS"
         * @const
         */
        "USS" = "USS";

    
        /**
         * value: "UYI"
         * @const
         */
        "UYI" = "UYI";

    
        /**
         * value: "UYU"
         * @const
         */
        "UYU" = "UYU";

    
        /**
         * value: "UZS"
         * @const
         */
        "UZS" = "UZS";

    
        /**
         * value: "VEF"
         * @const
         */
        "VEF" = "VEF";

    
        /**
         * value: "VND"
         * @const
         */
        "VND" = "VND";

    
        /**
         * value: "VUV"
         * @const
         */
        "VUV" = "VUV";

    
        /**
         * value: "WST"
         * @const
         */
        "WST" = "WST";

    
        /**
         * value: "XAF"
         * @const
         */
        "XAF" = "XAF";

    
        /**
         * value: "XAG"
         * @const
         */
        "XAG" = "XAG";

    
        /**
         * value: "XAU"
         * @const
         */
        "XAU" = "XAU";

    
        /**
         * value: "XBA"
         * @const
         */
        "XBA" = "XBA";

    
        /**
         * value: "XBB"
         * @const
         */
        "XBB" = "XBB";

    
        /**
         * value: "XBC"
         * @const
         */
        "XBC" = "XBC";

    
        /**
         * value: "XBD"
         * @const
         */
        "XBD" = "XBD";

    
        /**
         * value: "XCD"
         * @const
         */
        "XCD" = "XCD";

    
        /**
         * value: "XDR"
         * @const
         */
        "XDR" = "XDR";

    
        /**
         * value: "XOF"
         * @const
         */
        "XOF" = "XOF";

    
        /**
         * value: "XPD"
         * @const
         */
        "XPD" = "XPD";

    
        /**
         * value: "XPF"
         * @const
         */
        "XPF" = "XPF";

    
        /**
         * value: "XPT"
         * @const
         */
        "XPT" = "XPT";

    
        /**
         * value: "XTS"
         * @const
         */
        "XTS" = "XTS";

    
        /**
         * value: "XXX"
         * @const
         */
        "XXX" = "XXX";

    
        /**
         * value: "YER"
         * @const
         */
        "YER" = "YER";

    
        /**
         * value: "ZAR"
         * @const
         */
        "ZAR" = "ZAR";

    
        /**
         * value: "ZMK"
         * @const
         */
        "ZMK" = "ZMK";

    
        /**
         * value: "ZMW"
         * @const
         */
        "ZMW" = "ZMW";

    
        /**
         * value: "BTC"
         * @const
         */
        "BTC" = "BTC";

    
        /**
         * value: "ETH"
         * @const
         */
        "ETH" = "ETH";

    

    /**
    * Returns a <code>Currency</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/Currency} The enum <code>Currency</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

