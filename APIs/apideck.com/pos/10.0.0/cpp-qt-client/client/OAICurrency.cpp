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
 */

#include "OAICurrency.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICurrency::OAICurrency(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICurrency::OAICurrency() {
    this->initializeModel();
}

OAICurrency::~OAICurrency() {}

void OAICurrency::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAICurrency::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAICurrency::fromJson(QString jsonString) {
    
    if ( jsonString.compare("UNKNOWN_CURRENCY", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::UNKNOWN_CURRENCY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AED", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::AED;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AFN", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::AFN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ALL", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::ALL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AMD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::AMD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ANG", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::ANG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AOA", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::AOA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ARS", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::ARS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AUD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::AUD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AWG", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::AWG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("AZN", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::AZN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BAM", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BAM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BBD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BBD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BDT", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BDT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BGN", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BGN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BHD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BHD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BIF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BIF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BMD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BMD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BND", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BND;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BOB", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BOB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BOV", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BOV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BRL", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BRL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BSD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BSD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BTN", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BTN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BWP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BWP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BYR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BYR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BZD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BZD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CAD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CAD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CDF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CDF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CHE", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CHE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CHF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CHF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CHW", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CHW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CLF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CLF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CLP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CLP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CNY", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CNY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("COP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::COP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("COU", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::COU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CRC", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CRC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CUC", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CUC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CUP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CUP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CVE", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CVE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("CZK", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::CZK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DJF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::DJF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DKK", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::DKK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DOP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::DOP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("DZD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::DZD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EGP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::EGP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ERN", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::ERN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ETB", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::ETB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("EUR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::EUR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("FJD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::FJD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("FKP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::FKP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GBP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::GBP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GEL", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::GEL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GHS", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::GHS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GIP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::GIP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GMD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::GMD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GNF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::GNF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GTQ", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::GTQ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("GYD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::GYD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HKD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::HKD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HNL", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::HNL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HRK", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::HRK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HTG", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::HTG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("HUF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::HUF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("IDR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::IDR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ILS", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::ILS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("INR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::INR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("IQD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::IQD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("IRR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::IRR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ISK", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::ISK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("JMD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::JMD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("JOD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::JOD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("JPY", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::JPY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("KES", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::KES;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("KGS", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::KGS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("KHR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::KHR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("KMF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::KMF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("KPW", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::KPW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("KRW", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::KRW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("KWD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::KWD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("KYD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::KYD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("KZT", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::KZT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LAK", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::LAK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LBP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::LBP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LKR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::LKR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LRD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::LRD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LSL", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::LSL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LTL", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::LTL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LVL", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::LVL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("LYD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::LYD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MAD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MAD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MDL", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MDL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MGA", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MGA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MKD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MKD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MMK", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MMK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MNT", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MNT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MOP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MOP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MRO", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MRO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MUR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MUR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MVR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MVR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MWK", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MWK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MXN", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MXN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MXV", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MXV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MYR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MYR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("MZN", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::MZN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NAD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::NAD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NGN", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::NGN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NIO", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::NIO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NOK", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::NOK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NPR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::NPR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("NZD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::NZD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("OMR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::OMR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PAB", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::PAB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PEN", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::PEN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PGK", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::PGK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PHP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::PHP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PKR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::PKR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PLN", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::PLN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("PYG", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::PYG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("QAR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::QAR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("RON", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::RON;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("RSD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::RSD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("RUB", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::RUB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("RWF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::RWF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SAR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SAR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SBD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SBD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SCR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SCR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SDG", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SDG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SEK", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SEK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SGD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SGD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SHP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SHP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SLL", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SLL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SOS", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SOS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SRD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SRD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SSP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SSP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("STD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::STD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SVC", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SVC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SYP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SYP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("SZL", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::SZL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("THB", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::THB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TJS", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::TJS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TMT", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::TMT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TND", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::TND;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TOP", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::TOP;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TRC", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::TRC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TRY", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::TRY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TTD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::TTD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TWD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::TWD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("TZS", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::TZS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UAH", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::UAH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UGX", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::UGX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("USD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::USD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("USN", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::USN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("USS", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::USS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UYI", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::UYI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UYU", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::UYU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("UZS", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::UZS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VEF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::VEF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VND", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::VND;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("VUV", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::VUV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("WST", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::WST;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XAF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XAF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XAG", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XAG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XAU", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XAU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XBA", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XBA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XBB", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XBB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XBC", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XBC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XBD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XBD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XCD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XCD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XDR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XDR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XOF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XOF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XPD", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XPD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XPF", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XPF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XPT", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XPT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XTS", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XTS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("XXX", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::XXX;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("YER", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::YER;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ZAR", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::ZAR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ZMK", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::ZMK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ZMW", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::ZMW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("BTC", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::BTC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ETH", Qt::CaseInsensitive) == 0) {
        m_value = eOAICurrency::ETH;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAICurrency::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAICurrency::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAICurrency::UNKNOWN_CURRENCY:
            val = "UNKNOWN_CURRENCY";
            break;
        case eOAICurrency::AED:
            val = "AED";
            break;
        case eOAICurrency::AFN:
            val = "AFN";
            break;
        case eOAICurrency::ALL:
            val = "ALL";
            break;
        case eOAICurrency::AMD:
            val = "AMD";
            break;
        case eOAICurrency::ANG:
            val = "ANG";
            break;
        case eOAICurrency::AOA:
            val = "AOA";
            break;
        case eOAICurrency::ARS:
            val = "ARS";
            break;
        case eOAICurrency::AUD:
            val = "AUD";
            break;
        case eOAICurrency::AWG:
            val = "AWG";
            break;
        case eOAICurrency::AZN:
            val = "AZN";
            break;
        case eOAICurrency::BAM:
            val = "BAM";
            break;
        case eOAICurrency::BBD:
            val = "BBD";
            break;
        case eOAICurrency::BDT:
            val = "BDT";
            break;
        case eOAICurrency::BGN:
            val = "BGN";
            break;
        case eOAICurrency::BHD:
            val = "BHD";
            break;
        case eOAICurrency::BIF:
            val = "BIF";
            break;
        case eOAICurrency::BMD:
            val = "BMD";
            break;
        case eOAICurrency::BND:
            val = "BND";
            break;
        case eOAICurrency::BOB:
            val = "BOB";
            break;
        case eOAICurrency::BOV:
            val = "BOV";
            break;
        case eOAICurrency::BRL:
            val = "BRL";
            break;
        case eOAICurrency::BSD:
            val = "BSD";
            break;
        case eOAICurrency::BTN:
            val = "BTN";
            break;
        case eOAICurrency::BWP:
            val = "BWP";
            break;
        case eOAICurrency::BYR:
            val = "BYR";
            break;
        case eOAICurrency::BZD:
            val = "BZD";
            break;
        case eOAICurrency::CAD:
            val = "CAD";
            break;
        case eOAICurrency::CDF:
            val = "CDF";
            break;
        case eOAICurrency::CHE:
            val = "CHE";
            break;
        case eOAICurrency::CHF:
            val = "CHF";
            break;
        case eOAICurrency::CHW:
            val = "CHW";
            break;
        case eOAICurrency::CLF:
            val = "CLF";
            break;
        case eOAICurrency::CLP:
            val = "CLP";
            break;
        case eOAICurrency::CNY:
            val = "CNY";
            break;
        case eOAICurrency::COP:
            val = "COP";
            break;
        case eOAICurrency::COU:
            val = "COU";
            break;
        case eOAICurrency::CRC:
            val = "CRC";
            break;
        case eOAICurrency::CUC:
            val = "CUC";
            break;
        case eOAICurrency::CUP:
            val = "CUP";
            break;
        case eOAICurrency::CVE:
            val = "CVE";
            break;
        case eOAICurrency::CZK:
            val = "CZK";
            break;
        case eOAICurrency::DJF:
            val = "DJF";
            break;
        case eOAICurrency::DKK:
            val = "DKK";
            break;
        case eOAICurrency::DOP:
            val = "DOP";
            break;
        case eOAICurrency::DZD:
            val = "DZD";
            break;
        case eOAICurrency::EGP:
            val = "EGP";
            break;
        case eOAICurrency::ERN:
            val = "ERN";
            break;
        case eOAICurrency::ETB:
            val = "ETB";
            break;
        case eOAICurrency::EUR:
            val = "EUR";
            break;
        case eOAICurrency::FJD:
            val = "FJD";
            break;
        case eOAICurrency::FKP:
            val = "FKP";
            break;
        case eOAICurrency::GBP:
            val = "GBP";
            break;
        case eOAICurrency::GEL:
            val = "GEL";
            break;
        case eOAICurrency::GHS:
            val = "GHS";
            break;
        case eOAICurrency::GIP:
            val = "GIP";
            break;
        case eOAICurrency::GMD:
            val = "GMD";
            break;
        case eOAICurrency::GNF:
            val = "GNF";
            break;
        case eOAICurrency::GTQ:
            val = "GTQ";
            break;
        case eOAICurrency::GYD:
            val = "GYD";
            break;
        case eOAICurrency::HKD:
            val = "HKD";
            break;
        case eOAICurrency::HNL:
            val = "HNL";
            break;
        case eOAICurrency::HRK:
            val = "HRK";
            break;
        case eOAICurrency::HTG:
            val = "HTG";
            break;
        case eOAICurrency::HUF:
            val = "HUF";
            break;
        case eOAICurrency::IDR:
            val = "IDR";
            break;
        case eOAICurrency::ILS:
            val = "ILS";
            break;
        case eOAICurrency::INR:
            val = "INR";
            break;
        case eOAICurrency::IQD:
            val = "IQD";
            break;
        case eOAICurrency::IRR:
            val = "IRR";
            break;
        case eOAICurrency::ISK:
            val = "ISK";
            break;
        case eOAICurrency::JMD:
            val = "JMD";
            break;
        case eOAICurrency::JOD:
            val = "JOD";
            break;
        case eOAICurrency::JPY:
            val = "JPY";
            break;
        case eOAICurrency::KES:
            val = "KES";
            break;
        case eOAICurrency::KGS:
            val = "KGS";
            break;
        case eOAICurrency::KHR:
            val = "KHR";
            break;
        case eOAICurrency::KMF:
            val = "KMF";
            break;
        case eOAICurrency::KPW:
            val = "KPW";
            break;
        case eOAICurrency::KRW:
            val = "KRW";
            break;
        case eOAICurrency::KWD:
            val = "KWD";
            break;
        case eOAICurrency::KYD:
            val = "KYD";
            break;
        case eOAICurrency::KZT:
            val = "KZT";
            break;
        case eOAICurrency::LAK:
            val = "LAK";
            break;
        case eOAICurrency::LBP:
            val = "LBP";
            break;
        case eOAICurrency::LKR:
            val = "LKR";
            break;
        case eOAICurrency::LRD:
            val = "LRD";
            break;
        case eOAICurrency::LSL:
            val = "LSL";
            break;
        case eOAICurrency::LTL:
            val = "LTL";
            break;
        case eOAICurrency::LVL:
            val = "LVL";
            break;
        case eOAICurrency::LYD:
            val = "LYD";
            break;
        case eOAICurrency::MAD:
            val = "MAD";
            break;
        case eOAICurrency::MDL:
            val = "MDL";
            break;
        case eOAICurrency::MGA:
            val = "MGA";
            break;
        case eOAICurrency::MKD:
            val = "MKD";
            break;
        case eOAICurrency::MMK:
            val = "MMK";
            break;
        case eOAICurrency::MNT:
            val = "MNT";
            break;
        case eOAICurrency::MOP:
            val = "MOP";
            break;
        case eOAICurrency::MRO:
            val = "MRO";
            break;
        case eOAICurrency::MUR:
            val = "MUR";
            break;
        case eOAICurrency::MVR:
            val = "MVR";
            break;
        case eOAICurrency::MWK:
            val = "MWK";
            break;
        case eOAICurrency::MXN:
            val = "MXN";
            break;
        case eOAICurrency::MXV:
            val = "MXV";
            break;
        case eOAICurrency::MYR:
            val = "MYR";
            break;
        case eOAICurrency::MZN:
            val = "MZN";
            break;
        case eOAICurrency::NAD:
            val = "NAD";
            break;
        case eOAICurrency::NGN:
            val = "NGN";
            break;
        case eOAICurrency::NIO:
            val = "NIO";
            break;
        case eOAICurrency::NOK:
            val = "NOK";
            break;
        case eOAICurrency::NPR:
            val = "NPR";
            break;
        case eOAICurrency::NZD:
            val = "NZD";
            break;
        case eOAICurrency::OMR:
            val = "OMR";
            break;
        case eOAICurrency::PAB:
            val = "PAB";
            break;
        case eOAICurrency::PEN:
            val = "PEN";
            break;
        case eOAICurrency::PGK:
            val = "PGK";
            break;
        case eOAICurrency::PHP:
            val = "PHP";
            break;
        case eOAICurrency::PKR:
            val = "PKR";
            break;
        case eOAICurrency::PLN:
            val = "PLN";
            break;
        case eOAICurrency::PYG:
            val = "PYG";
            break;
        case eOAICurrency::QAR:
            val = "QAR";
            break;
        case eOAICurrency::RON:
            val = "RON";
            break;
        case eOAICurrency::RSD:
            val = "RSD";
            break;
        case eOAICurrency::RUB:
            val = "RUB";
            break;
        case eOAICurrency::RWF:
            val = "RWF";
            break;
        case eOAICurrency::SAR:
            val = "SAR";
            break;
        case eOAICurrency::SBD:
            val = "SBD";
            break;
        case eOAICurrency::SCR:
            val = "SCR";
            break;
        case eOAICurrency::SDG:
            val = "SDG";
            break;
        case eOAICurrency::SEK:
            val = "SEK";
            break;
        case eOAICurrency::SGD:
            val = "SGD";
            break;
        case eOAICurrency::SHP:
            val = "SHP";
            break;
        case eOAICurrency::SLL:
            val = "SLL";
            break;
        case eOAICurrency::SOS:
            val = "SOS";
            break;
        case eOAICurrency::SRD:
            val = "SRD";
            break;
        case eOAICurrency::SSP:
            val = "SSP";
            break;
        case eOAICurrency::STD:
            val = "STD";
            break;
        case eOAICurrency::SVC:
            val = "SVC";
            break;
        case eOAICurrency::SYP:
            val = "SYP";
            break;
        case eOAICurrency::SZL:
            val = "SZL";
            break;
        case eOAICurrency::THB:
            val = "THB";
            break;
        case eOAICurrency::TJS:
            val = "TJS";
            break;
        case eOAICurrency::TMT:
            val = "TMT";
            break;
        case eOAICurrency::TND:
            val = "TND";
            break;
        case eOAICurrency::TOP:
            val = "TOP";
            break;
        case eOAICurrency::TRC:
            val = "TRC";
            break;
        case eOAICurrency::TRY:
            val = "TRY";
            break;
        case eOAICurrency::TTD:
            val = "TTD";
            break;
        case eOAICurrency::TWD:
            val = "TWD";
            break;
        case eOAICurrency::TZS:
            val = "TZS";
            break;
        case eOAICurrency::UAH:
            val = "UAH";
            break;
        case eOAICurrency::UGX:
            val = "UGX";
            break;
        case eOAICurrency::USD:
            val = "USD";
            break;
        case eOAICurrency::USN:
            val = "USN";
            break;
        case eOAICurrency::USS:
            val = "USS";
            break;
        case eOAICurrency::UYI:
            val = "UYI";
            break;
        case eOAICurrency::UYU:
            val = "UYU";
            break;
        case eOAICurrency::UZS:
            val = "UZS";
            break;
        case eOAICurrency::VEF:
            val = "VEF";
            break;
        case eOAICurrency::VND:
            val = "VND";
            break;
        case eOAICurrency::VUV:
            val = "VUV";
            break;
        case eOAICurrency::WST:
            val = "WST";
            break;
        case eOAICurrency::XAF:
            val = "XAF";
            break;
        case eOAICurrency::XAG:
            val = "XAG";
            break;
        case eOAICurrency::XAU:
            val = "XAU";
            break;
        case eOAICurrency::XBA:
            val = "XBA";
            break;
        case eOAICurrency::XBB:
            val = "XBB";
            break;
        case eOAICurrency::XBC:
            val = "XBC";
            break;
        case eOAICurrency::XBD:
            val = "XBD";
            break;
        case eOAICurrency::XCD:
            val = "XCD";
            break;
        case eOAICurrency::XDR:
            val = "XDR";
            break;
        case eOAICurrency::XOF:
            val = "XOF";
            break;
        case eOAICurrency::XPD:
            val = "XPD";
            break;
        case eOAICurrency::XPF:
            val = "XPF";
            break;
        case eOAICurrency::XPT:
            val = "XPT";
            break;
        case eOAICurrency::XTS:
            val = "XTS";
            break;
        case eOAICurrency::XXX:
            val = "XXX";
            break;
        case eOAICurrency::YER:
            val = "YER";
            break;
        case eOAICurrency::ZAR:
            val = "ZAR";
            break;
        case eOAICurrency::ZMK:
            val = "ZMK";
            break;
        case eOAICurrency::ZMW:
            val = "ZMW";
            break;
        case eOAICurrency::BTC:
            val = "BTC";
            break;
        case eOAICurrency::ETH:
            val = "ETH";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAICurrency::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAICurrency::eOAICurrency OAICurrency::getValue() const {
    return m_value;
}

void OAICurrency::setValue(const OAICurrency::eOAICurrency& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAICurrency::isSet() const {
    
    return m_value_isSet;
}

bool OAICurrency::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
