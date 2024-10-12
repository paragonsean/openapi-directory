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
 */

#include "OAIConnector.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConnector::OAIConnector(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConnector::OAIConnector() {
    this->initializeModel();
}

OAIConnector::~OAIConnector() {}

void OAIConnector::initializeModel() {

    m_auth_only_isSet = false;
    m_auth_only_isValid = false;

    m_auth_type_isSet = false;
    m_auth_type_isValid = false;

    m_blind_mapped_isSet = false;
    m_blind_mapped_isValid = false;

    m_configurable_resources_isSet = false;
    m_configurable_resources_isValid = false;

    m_custom_scopes_isSet = false;
    m_custom_scopes_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_docs_isSet = false;
    m_docs_isValid = false;

    m_free_trial_available_isSet = false;
    m_free_trial_available_isValid = false;

    m_has_sandbox_credentials_isSet = false;
    m_has_sandbox_credentials_isValid = false;

    m_icon_url_isSet = false;
    m_icon_url_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_logo_url_isSet = false;
    m_logo_url_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_oauth_credentials_source_isSet = false;
    m_oauth_credentials_source_isValid = false;

    m_oauth_grant_type_isSet = false;
    m_oauth_grant_type_isValid = false;

    m_oauth_scopes_isSet = false;
    m_oauth_scopes_isValid = false;

    m_partner_signup_url_isSet = false;
    m_partner_signup_url_isValid = false;

    m_schema_support_isSet = false;
    m_schema_support_isValid = false;

    m_service_id_isSet = false;
    m_service_id_isValid = false;

    m_settings_isSet = false;
    m_settings_isValid = false;

    m_signup_url_isSet = false;
    m_signup_url_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_supported_events_isSet = false;
    m_supported_events_isValid = false;

    m_supported_resources_isSet = false;
    m_supported_resources_isValid = false;

    m_tls_support_isSet = false;
    m_tls_support_isValid = false;

    m_unified_apis_isSet = false;
    m_unified_apis_isValid = false;

    m_webhook_support_isSet = false;
    m_webhook_support_isValid = false;

    m_website_url_isSet = false;
    m_website_url_isValid = false;
}

void OAIConnector::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConnector::fromJsonObject(QJsonObject json) {

    m_auth_only_isValid = ::OpenAPI::fromJsonValue(m_auth_only, json[QString("auth_only")]);
    m_auth_only_isSet = !json[QString("auth_only")].isNull() && m_auth_only_isValid;

    m_auth_type_isValid = ::OpenAPI::fromJsonValue(m_auth_type, json[QString("auth_type")]);
    m_auth_type_isSet = !json[QString("auth_type")].isNull() && m_auth_type_isValid;

    m_blind_mapped_isValid = ::OpenAPI::fromJsonValue(m_blind_mapped, json[QString("blind_mapped")]);
    m_blind_mapped_isSet = !json[QString("blind_mapped")].isNull() && m_blind_mapped_isValid;

    m_configurable_resources_isValid = ::OpenAPI::fromJsonValue(m_configurable_resources, json[QString("configurable_resources")]);
    m_configurable_resources_isSet = !json[QString("configurable_resources")].isNull() && m_configurable_resources_isValid;

    m_custom_scopes_isValid = ::OpenAPI::fromJsonValue(m_custom_scopes, json[QString("custom_scopes")]);
    m_custom_scopes_isSet = !json[QString("custom_scopes")].isNull() && m_custom_scopes_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_docs_isValid = ::OpenAPI::fromJsonValue(m_docs, json[QString("docs")]);
    m_docs_isSet = !json[QString("docs")].isNull() && m_docs_isValid;

    m_free_trial_available_isValid = ::OpenAPI::fromJsonValue(m_free_trial_available, json[QString("free_trial_available")]);
    m_free_trial_available_isSet = !json[QString("free_trial_available")].isNull() && m_free_trial_available_isValid;

    m_has_sandbox_credentials_isValid = ::OpenAPI::fromJsonValue(m_has_sandbox_credentials, json[QString("has_sandbox_credentials")]);
    m_has_sandbox_credentials_isSet = !json[QString("has_sandbox_credentials")].isNull() && m_has_sandbox_credentials_isValid;

    m_icon_url_isValid = ::OpenAPI::fromJsonValue(m_icon_url, json[QString("icon_url")]);
    m_icon_url_isSet = !json[QString("icon_url")].isNull() && m_icon_url_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_logo_url_isValid = ::OpenAPI::fromJsonValue(m_logo_url, json[QString("logo_url")]);
    m_logo_url_isSet = !json[QString("logo_url")].isNull() && m_logo_url_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_oauth_credentials_source_isValid = ::OpenAPI::fromJsonValue(m_oauth_credentials_source, json[QString("oauth_credentials_source")]);
    m_oauth_credentials_source_isSet = !json[QString("oauth_credentials_source")].isNull() && m_oauth_credentials_source_isValid;

    m_oauth_grant_type_isValid = ::OpenAPI::fromJsonValue(m_oauth_grant_type, json[QString("oauth_grant_type")]);
    m_oauth_grant_type_isSet = !json[QString("oauth_grant_type")].isNull() && m_oauth_grant_type_isValid;

    m_oauth_scopes_isValid = ::OpenAPI::fromJsonValue(m_oauth_scopes, json[QString("oauth_scopes")]);
    m_oauth_scopes_isSet = !json[QString("oauth_scopes")].isNull() && m_oauth_scopes_isValid;

    m_partner_signup_url_isValid = ::OpenAPI::fromJsonValue(m_partner_signup_url, json[QString("partner_signup_url")]);
    m_partner_signup_url_isSet = !json[QString("partner_signup_url")].isNull() && m_partner_signup_url_isValid;

    m_schema_support_isValid = ::OpenAPI::fromJsonValue(m_schema_support, json[QString("schema_support")]);
    m_schema_support_isSet = !json[QString("schema_support")].isNull() && m_schema_support_isValid;

    m_service_id_isValid = ::OpenAPI::fromJsonValue(m_service_id, json[QString("service_id")]);
    m_service_id_isSet = !json[QString("service_id")].isNull() && m_service_id_isValid;

    m_settings_isValid = ::OpenAPI::fromJsonValue(m_settings, json[QString("settings")]);
    m_settings_isSet = !json[QString("settings")].isNull() && m_settings_isValid;

    m_signup_url_isValid = ::OpenAPI::fromJsonValue(m_signup_url, json[QString("signup_url")]);
    m_signup_url_isSet = !json[QString("signup_url")].isNull() && m_signup_url_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_supported_events_isValid = ::OpenAPI::fromJsonValue(m_supported_events, json[QString("supported_events")]);
    m_supported_events_isSet = !json[QString("supported_events")].isNull() && m_supported_events_isValid;

    m_supported_resources_isValid = ::OpenAPI::fromJsonValue(m_supported_resources, json[QString("supported_resources")]);
    m_supported_resources_isSet = !json[QString("supported_resources")].isNull() && m_supported_resources_isValid;

    m_tls_support_isValid = ::OpenAPI::fromJsonValue(m_tls_support, json[QString("tls_support")]);
    m_tls_support_isSet = !json[QString("tls_support")].isNull() && m_tls_support_isValid;

    m_unified_apis_isValid = ::OpenAPI::fromJsonValue(m_unified_apis, json[QString("unified_apis")]);
    m_unified_apis_isSet = !json[QString("unified_apis")].isNull() && m_unified_apis_isValid;

    m_webhook_support_isValid = ::OpenAPI::fromJsonValue(m_webhook_support, json[QString("webhook_support")]);
    m_webhook_support_isSet = !json[QString("webhook_support")].isNull() && m_webhook_support_isValid;

    m_website_url_isValid = ::OpenAPI::fromJsonValue(m_website_url, json[QString("website_url")]);
    m_website_url_isSet = !json[QString("website_url")].isNull() && m_website_url_isValid;
}

QString OAIConnector::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConnector::asJsonObject() const {
    QJsonObject obj;
    if (m_auth_only_isSet) {
        obj.insert(QString("auth_only"), ::OpenAPI::toJsonValue(m_auth_only));
    }
    if (m_auth_type_isSet) {
        obj.insert(QString("auth_type"), ::OpenAPI::toJsonValue(m_auth_type));
    }
    if (m_blind_mapped_isSet) {
        obj.insert(QString("blind_mapped"), ::OpenAPI::toJsonValue(m_blind_mapped));
    }
    if (m_configurable_resources.size() > 0) {
        obj.insert(QString("configurable_resources"), ::OpenAPI::toJsonValue(m_configurable_resources));
    }
    if (m_custom_scopes_isSet) {
        obj.insert(QString("custom_scopes"), ::OpenAPI::toJsonValue(m_custom_scopes));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_docs.size() > 0) {
        obj.insert(QString("docs"), ::OpenAPI::toJsonValue(m_docs));
    }
    if (m_free_trial_available_isSet) {
        obj.insert(QString("free_trial_available"), ::OpenAPI::toJsonValue(m_free_trial_available));
    }
    if (m_has_sandbox_credentials_isSet) {
        obj.insert(QString("has_sandbox_credentials"), ::OpenAPI::toJsonValue(m_has_sandbox_credentials));
    }
    if (m_icon_url_isSet) {
        obj.insert(QString("icon_url"), ::OpenAPI::toJsonValue(m_icon_url));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_logo_url_isSet) {
        obj.insert(QString("logo_url"), ::OpenAPI::toJsonValue(m_logo_url));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_oauth_credentials_source_isSet) {
        obj.insert(QString("oauth_credentials_source"), ::OpenAPI::toJsonValue(m_oauth_credentials_source));
    }
    if (m_oauth_grant_type_isSet) {
        obj.insert(QString("oauth_grant_type"), ::OpenAPI::toJsonValue(m_oauth_grant_type));
    }
    if (m_oauth_scopes.size() > 0) {
        obj.insert(QString("oauth_scopes"), ::OpenAPI::toJsonValue(m_oauth_scopes));
    }
    if (m_partner_signup_url_isSet) {
        obj.insert(QString("partner_signup_url"), ::OpenAPI::toJsonValue(m_partner_signup_url));
    }
    if (m_schema_support.isSet()) {
        obj.insert(QString("schema_support"), ::OpenAPI::toJsonValue(m_schema_support));
    }
    if (m_service_id_isSet) {
        obj.insert(QString("service_id"), ::OpenAPI::toJsonValue(m_service_id));
    }
    if (m_settings.size() > 0) {
        obj.insert(QString("settings"), ::OpenAPI::toJsonValue(m_settings));
    }
    if (m_signup_url_isSet) {
        obj.insert(QString("signup_url"), ::OpenAPI::toJsonValue(m_signup_url));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_supported_events.size() > 0) {
        obj.insert(QString("supported_events"), ::OpenAPI::toJsonValue(m_supported_events));
    }
    if (m_supported_resources.size() > 0) {
        obj.insert(QString("supported_resources"), ::OpenAPI::toJsonValue(m_supported_resources));
    }
    if (m_tls_support.isSet()) {
        obj.insert(QString("tls_support"), ::OpenAPI::toJsonValue(m_tls_support));
    }
    if (m_unified_apis.size() > 0) {
        obj.insert(QString("unified_apis"), ::OpenAPI::toJsonValue(m_unified_apis));
    }
    if (m_webhook_support.isSet()) {
        obj.insert(QString("webhook_support"), ::OpenAPI::toJsonValue(m_webhook_support));
    }
    if (m_website_url_isSet) {
        obj.insert(QString("website_url"), ::OpenAPI::toJsonValue(m_website_url));
    }
    return obj;
}

bool OAIConnector::isAuthOnly() const {
    return m_auth_only;
}
void OAIConnector::setAuthOnly(const bool &auth_only) {
    m_auth_only = auth_only;
    m_auth_only_isSet = true;
}

bool OAIConnector::is_auth_only_Set() const{
    return m_auth_only_isSet;
}

bool OAIConnector::is_auth_only_Valid() const{
    return m_auth_only_isValid;
}

QString OAIConnector::getAuthType() const {
    return m_auth_type;
}
void OAIConnector::setAuthType(const QString &auth_type) {
    m_auth_type = auth_type;
    m_auth_type_isSet = true;
}

bool OAIConnector::is_auth_type_Set() const{
    return m_auth_type_isSet;
}

bool OAIConnector::is_auth_type_Valid() const{
    return m_auth_type_isValid;
}

bool OAIConnector::isBlindMapped() const {
    return m_blind_mapped;
}
void OAIConnector::setBlindMapped(const bool &blind_mapped) {
    m_blind_mapped = blind_mapped;
    m_blind_mapped_isSet = true;
}

bool OAIConnector::is_blind_mapped_Set() const{
    return m_blind_mapped_isSet;
}

bool OAIConnector::is_blind_mapped_Valid() const{
    return m_blind_mapped_isValid;
}

QList<QString> OAIConnector::getConfigurableResources() const {
    return m_configurable_resources;
}
void OAIConnector::setConfigurableResources(const QList<QString> &configurable_resources) {
    m_configurable_resources = configurable_resources;
    m_configurable_resources_isSet = true;
}

bool OAIConnector::is_configurable_resources_Set() const{
    return m_configurable_resources_isSet;
}

bool OAIConnector::is_configurable_resources_Valid() const{
    return m_configurable_resources_isValid;
}

bool OAIConnector::isCustomScopes() const {
    return m_custom_scopes;
}
void OAIConnector::setCustomScopes(const bool &custom_scopes) {
    m_custom_scopes = custom_scopes;
    m_custom_scopes_isSet = true;
}

bool OAIConnector::is_custom_scopes_Set() const{
    return m_custom_scopes_isSet;
}

bool OAIConnector::is_custom_scopes_Valid() const{
    return m_custom_scopes_isValid;
}

QString OAIConnector::getDescription() const {
    return m_description;
}
void OAIConnector::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIConnector::is_description_Set() const{
    return m_description_isSet;
}

bool OAIConnector::is_description_Valid() const{
    return m_description_isValid;
}

QList<OAIConnectorDoc> OAIConnector::getDocs() const {
    return m_docs;
}
void OAIConnector::setDocs(const QList<OAIConnectorDoc> &docs) {
    m_docs = docs;
    m_docs_isSet = true;
}

bool OAIConnector::is_docs_Set() const{
    return m_docs_isSet;
}

bool OAIConnector::is_docs_Valid() const{
    return m_docs_isValid;
}

bool OAIConnector::isFreeTrialAvailable() const {
    return m_free_trial_available;
}
void OAIConnector::setFreeTrialAvailable(const bool &free_trial_available) {
    m_free_trial_available = free_trial_available;
    m_free_trial_available_isSet = true;
}

bool OAIConnector::is_free_trial_available_Set() const{
    return m_free_trial_available_isSet;
}

bool OAIConnector::is_free_trial_available_Valid() const{
    return m_free_trial_available_isValid;
}

bool OAIConnector::isHasSandboxCredentials() const {
    return m_has_sandbox_credentials;
}
void OAIConnector::setHasSandboxCredentials(const bool &has_sandbox_credentials) {
    m_has_sandbox_credentials = has_sandbox_credentials;
    m_has_sandbox_credentials_isSet = true;
}

bool OAIConnector::is_has_sandbox_credentials_Set() const{
    return m_has_sandbox_credentials_isSet;
}

bool OAIConnector::is_has_sandbox_credentials_Valid() const{
    return m_has_sandbox_credentials_isValid;
}

QString OAIConnector::getIconUrl() const {
    return m_icon_url;
}
void OAIConnector::setIconUrl(const QString &icon_url) {
    m_icon_url = icon_url;
    m_icon_url_isSet = true;
}

bool OAIConnector::is_icon_url_Set() const{
    return m_icon_url_isSet;
}

bool OAIConnector::is_icon_url_Valid() const{
    return m_icon_url_isValid;
}

QString OAIConnector::getId() const {
    return m_id;
}
void OAIConnector::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIConnector::is_id_Set() const{
    return m_id_isSet;
}

bool OAIConnector::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIConnector::getLogoUrl() const {
    return m_logo_url;
}
void OAIConnector::setLogoUrl(const QString &logo_url) {
    m_logo_url = logo_url;
    m_logo_url_isSet = true;
}

bool OAIConnector::is_logo_url_Set() const{
    return m_logo_url_isSet;
}

bool OAIConnector::is_logo_url_Valid() const{
    return m_logo_url_isValid;
}

QString OAIConnector::getName() const {
    return m_name;
}
void OAIConnector::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIConnector::is_name_Set() const{
    return m_name_isSet;
}

bool OAIConnector::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIConnector::getOauthCredentialsSource() const {
    return m_oauth_credentials_source;
}
void OAIConnector::setOauthCredentialsSource(const QString &oauth_credentials_source) {
    m_oauth_credentials_source = oauth_credentials_source;
    m_oauth_credentials_source_isSet = true;
}

bool OAIConnector::is_oauth_credentials_source_Set() const{
    return m_oauth_credentials_source_isSet;
}

bool OAIConnector::is_oauth_credentials_source_Valid() const{
    return m_oauth_credentials_source_isValid;
}

QString OAIConnector::getOauthGrantType() const {
    return m_oauth_grant_type;
}
void OAIConnector::setOauthGrantType(const QString &oauth_grant_type) {
    m_oauth_grant_type = oauth_grant_type;
    m_oauth_grant_type_isSet = true;
}

bool OAIConnector::is_oauth_grant_type_Set() const{
    return m_oauth_grant_type_isSet;
}

bool OAIConnector::is_oauth_grant_type_Valid() const{
    return m_oauth_grant_type_isValid;
}

QList<OAIConnector_oauth_scopes_inner> OAIConnector::getOauthScopes() const {
    return m_oauth_scopes;
}
void OAIConnector::setOauthScopes(const QList<OAIConnector_oauth_scopes_inner> &oauth_scopes) {
    m_oauth_scopes = oauth_scopes;
    m_oauth_scopes_isSet = true;
}

bool OAIConnector::is_oauth_scopes_Set() const{
    return m_oauth_scopes_isSet;
}

bool OAIConnector::is_oauth_scopes_Valid() const{
    return m_oauth_scopes_isValid;
}

QString OAIConnector::getPartnerSignupUrl() const {
    return m_partner_signup_url;
}
void OAIConnector::setPartnerSignupUrl(const QString &partner_signup_url) {
    m_partner_signup_url = partner_signup_url;
    m_partner_signup_url_isSet = true;
}

bool OAIConnector::is_partner_signup_url_Set() const{
    return m_partner_signup_url_isSet;
}

bool OAIConnector::is_partner_signup_url_Valid() const{
    return m_partner_signup_url_isValid;
}

OAISchemaSupport OAIConnector::getSchemaSupport() const {
    return m_schema_support;
}
void OAIConnector::setSchemaSupport(const OAISchemaSupport &schema_support) {
    m_schema_support = schema_support;
    m_schema_support_isSet = true;
}

bool OAIConnector::is_schema_support_Set() const{
    return m_schema_support_isSet;
}

bool OAIConnector::is_schema_support_Valid() const{
    return m_schema_support_isValid;
}

QString OAIConnector::getServiceId() const {
    return m_service_id;
}
void OAIConnector::setServiceId(const QString &service_id) {
    m_service_id = service_id;
    m_service_id_isSet = true;
}

bool OAIConnector::is_service_id_Set() const{
    return m_service_id_isSet;
}

bool OAIConnector::is_service_id_Valid() const{
    return m_service_id_isValid;
}

QList<OAIConnectorSetting> OAIConnector::getSettings() const {
    return m_settings;
}
void OAIConnector::setSettings(const QList<OAIConnectorSetting> &settings) {
    m_settings = settings;
    m_settings_isSet = true;
}

bool OAIConnector::is_settings_Set() const{
    return m_settings_isSet;
}

bool OAIConnector::is_settings_Valid() const{
    return m_settings_isValid;
}

QString OAIConnector::getSignupUrl() const {
    return m_signup_url;
}
void OAIConnector::setSignupUrl(const QString &signup_url) {
    m_signup_url = signup_url;
    m_signup_url_isSet = true;
}

bool OAIConnector::is_signup_url_Set() const{
    return m_signup_url_isSet;
}

bool OAIConnector::is_signup_url_Valid() const{
    return m_signup_url_isValid;
}

OAIConnectorStatus OAIConnector::getStatus() const {
    return m_status;
}
void OAIConnector::setStatus(const OAIConnectorStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIConnector::is_status_Set() const{
    return m_status_isSet;
}

bool OAIConnector::is_status_Valid() const{
    return m_status_isValid;
}

QList<OAIConnectorEvent> OAIConnector::getSupportedEvents() const {
    return m_supported_events;
}
void OAIConnector::setSupportedEvents(const QList<OAIConnectorEvent> &supported_events) {
    m_supported_events = supported_events;
    m_supported_events_isSet = true;
}

bool OAIConnector::is_supported_events_Set() const{
    return m_supported_events_isSet;
}

bool OAIConnector::is_supported_events_Valid() const{
    return m_supported_events_isValid;
}

QList<OAILinkedConnectorResource> OAIConnector::getSupportedResources() const {
    return m_supported_resources;
}
void OAIConnector::setSupportedResources(const QList<OAILinkedConnectorResource> &supported_resources) {
    m_supported_resources = supported_resources;
    m_supported_resources_isSet = true;
}

bool OAIConnector::is_supported_resources_Set() const{
    return m_supported_resources_isSet;
}

bool OAIConnector::is_supported_resources_Valid() const{
    return m_supported_resources_isValid;
}

OAIConnector_tls_support OAIConnector::getTlsSupport() const {
    return m_tls_support;
}
void OAIConnector::setTlsSupport(const OAIConnector_tls_support &tls_support) {
    m_tls_support = tls_support;
    m_tls_support_isSet = true;
}

bool OAIConnector::is_tls_support_Set() const{
    return m_tls_support_isSet;
}

bool OAIConnector::is_tls_support_Valid() const{
    return m_tls_support_isValid;
}

QList<OAIConnector_unified_apis_inner> OAIConnector::getUnifiedApis() const {
    return m_unified_apis;
}
void OAIConnector::setUnifiedApis(const QList<OAIConnector_unified_apis_inner> &unified_apis) {
    m_unified_apis = unified_apis;
    m_unified_apis_isSet = true;
}

bool OAIConnector::is_unified_apis_Set() const{
    return m_unified_apis_isSet;
}

bool OAIConnector::is_unified_apis_Valid() const{
    return m_unified_apis_isValid;
}

OAIWebhookSupport OAIConnector::getWebhookSupport() const {
    return m_webhook_support;
}
void OAIConnector::setWebhookSupport(const OAIWebhookSupport &webhook_support) {
    m_webhook_support = webhook_support;
    m_webhook_support_isSet = true;
}

bool OAIConnector::is_webhook_support_Set() const{
    return m_webhook_support_isSet;
}

bool OAIConnector::is_webhook_support_Valid() const{
    return m_webhook_support_isValid;
}

QString OAIConnector::getWebsiteUrl() const {
    return m_website_url;
}
void OAIConnector::setWebsiteUrl(const QString &website_url) {
    m_website_url = website_url;
    m_website_url_isSet = true;
}

bool OAIConnector::is_website_url_Set() const{
    return m_website_url_isSet;
}

bool OAIConnector::is_website_url_Valid() const{
    return m_website_url_isValid;
}

bool OAIConnector::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auth_only_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_auth_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_blind_mapped_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_configurable_resources.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_scopes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_docs.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_free_trial_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_sandbox_credentials_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_icon_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_logo_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_oauth_credentials_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_oauth_grant_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_oauth_scopes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_partner_signup_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schema_support.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_settings.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_signup_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_supported_events.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_supported_resources.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tls_support.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_unified_apis.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_webhook_support.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConnector::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
