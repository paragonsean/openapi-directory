/**
 * Accounting API
 * Welcome to the Accounting API.  You can use this API to access all Accounting API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICustomer.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomer::OAICustomer(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomer::OAICustomer() {
    this->initializeModel();
}

OAICustomer::~OAICustomer() {}

void OAICustomer::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;

    m_addresses_isSet = false;
    m_addresses_isValid = false;

    m_bank_accounts_isSet = false;
    m_bank_accounts_isValid = false;

    m_channel_isSet = false;
    m_channel_isValid = false;

    m_company_name_isSet = false;
    m_company_name_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_custom_mappings_isSet = false;
    m_custom_mappings_isValid = false;

    m_display_id_isSet = false;
    m_display_id_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_downstream_id_isSet = false;
    m_downstream_id_isValid = false;

    m_emails_isSet = false;
    m_emails_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_individual_isSet = false;
    m_individual_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_middle_name_isSet = false;
    m_middle_name_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_parent_isSet = false;
    m_parent_isValid = false;

    m_payment_method_isSet = false;
    m_payment_method_isValid = false;

    m_phone_numbers_isSet = false;
    m_phone_numbers_isValid = false;

    m_project_isSet = false;
    m_project_isValid = false;

    m_row_version_isSet = false;
    m_row_version_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_suffix_isSet = false;
    m_suffix_isValid = false;

    m_tax_number_isSet = false;
    m_tax_number_isValid = false;

    m_tax_rate_isSet = false;
    m_tax_rate_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;

    m_websites_isSet = false;
    m_websites_isValid = false;
}

void OAICustomer::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomer::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;

    m_addresses_isValid = ::OpenAPI::fromJsonValue(m_addresses, json[QString("addresses")]);
    m_addresses_isSet = !json[QString("addresses")].isNull() && m_addresses_isValid;

    m_bank_accounts_isValid = ::OpenAPI::fromJsonValue(m_bank_accounts, json[QString("bank_accounts")]);
    m_bank_accounts_isSet = !json[QString("bank_accounts")].isNull() && m_bank_accounts_isValid;

    m_channel_isValid = ::OpenAPI::fromJsonValue(m_channel, json[QString("channel")]);
    m_channel_isSet = !json[QString("channel")].isNull() && m_channel_isValid;

    m_company_name_isValid = ::OpenAPI::fromJsonValue(m_company_name, json[QString("company_name")]);
    m_company_name_isSet = !json[QString("company_name")].isNull() && m_company_name_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_custom_mappings_isValid = ::OpenAPI::fromJsonValue(m_custom_mappings, json[QString("custom_mappings")]);
    m_custom_mappings_isSet = !json[QString("custom_mappings")].isNull() && m_custom_mappings_isValid;

    m_display_id_isValid = ::OpenAPI::fromJsonValue(m_display_id, json[QString("display_id")]);
    m_display_id_isSet = !json[QString("display_id")].isNull() && m_display_id_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("display_name")]);
    m_display_name_isSet = !json[QString("display_name")].isNull() && m_display_name_isValid;

    m_downstream_id_isValid = ::OpenAPI::fromJsonValue(m_downstream_id, json[QString("downstream_id")]);
    m_downstream_id_isSet = !json[QString("downstream_id")].isNull() && m_downstream_id_isValid;

    m_emails_isValid = ::OpenAPI::fromJsonValue(m_emails, json[QString("emails")]);
    m_emails_isSet = !json[QString("emails")].isNull() && m_emails_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_individual_isValid = ::OpenAPI::fromJsonValue(m_individual, json[QString("individual")]);
    m_individual_isSet = !json[QString("individual")].isNull() && m_individual_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_middle_name_isValid = ::OpenAPI::fromJsonValue(m_middle_name, json[QString("middle_name")]);
    m_middle_name_isSet = !json[QString("middle_name")].isNull() && m_middle_name_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_parent_isValid = ::OpenAPI::fromJsonValue(m_parent, json[QString("parent")]);
    m_parent_isSet = !json[QString("parent")].isNull() && m_parent_isValid;

    m_payment_method_isValid = ::OpenAPI::fromJsonValue(m_payment_method, json[QString("payment_method")]);
    m_payment_method_isSet = !json[QString("payment_method")].isNull() && m_payment_method_isValid;

    m_phone_numbers_isValid = ::OpenAPI::fromJsonValue(m_phone_numbers, json[QString("phone_numbers")]);
    m_phone_numbers_isSet = !json[QString("phone_numbers")].isNull() && m_phone_numbers_isValid;

    m_project_isValid = ::OpenAPI::fromJsonValue(m_project, json[QString("project")]);
    m_project_isSet = !json[QString("project")].isNull() && m_project_isValid;

    m_row_version_isValid = ::OpenAPI::fromJsonValue(m_row_version, json[QString("row_version")]);
    m_row_version_isSet = !json[QString("row_version")].isNull() && m_row_version_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_suffix_isValid = ::OpenAPI::fromJsonValue(m_suffix, json[QString("suffix")]);
    m_suffix_isSet = !json[QString("suffix")].isNull() && m_suffix_isValid;

    m_tax_number_isValid = ::OpenAPI::fromJsonValue(m_tax_number, json[QString("tax_number")]);
    m_tax_number_isSet = !json[QString("tax_number")].isNull() && m_tax_number_isValid;

    m_tax_rate_isValid = ::OpenAPI::fromJsonValue(m_tax_rate, json[QString("tax_rate")]);
    m_tax_rate_isSet = !json[QString("tax_rate")].isNull() && m_tax_rate_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updated_by")]);
    m_updated_by_isSet = !json[QString("updated_by")].isNull() && m_updated_by_isValid;

    m_websites_isValid = ::OpenAPI::fromJsonValue(m_websites, json[QString("websites")]);
    m_websites_isSet = !json[QString("websites")].isNull() && m_websites_isValid;
}

QString OAICustomer::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomer::asJsonObject() const {
    QJsonObject obj;
    if (m_account.isSet()) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    if (m_addresses.size() > 0) {
        obj.insert(QString("addresses"), ::OpenAPI::toJsonValue(m_addresses));
    }
    if (m_bank_accounts.size() > 0) {
        obj.insert(QString("bank_accounts"), ::OpenAPI::toJsonValue(m_bank_accounts));
    }
    if (m_channel_isSet) {
        obj.insert(QString("channel"), ::OpenAPI::toJsonValue(m_channel));
    }
    if (m_company_name_isSet) {
        obj.insert(QString("company_name"), ::OpenAPI::toJsonValue(m_company_name));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_created_by_isSet) {
        obj.insert(QString("created_by"), ::OpenAPI::toJsonValue(m_created_by));
    }
    if (m_currency.isSet()) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_custom_mappings_isSet) {
        obj.insert(QString("custom_mappings"), ::OpenAPI::toJsonValue(m_custom_mappings));
    }
    if (m_display_id_isSet) {
        obj.insert(QString("display_id"), ::OpenAPI::toJsonValue(m_display_id));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("display_name"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_downstream_id_isSet) {
        obj.insert(QString("downstream_id"), ::OpenAPI::toJsonValue(m_downstream_id));
    }
    if (m_emails.size() > 0) {
        obj.insert(QString("emails"), ::OpenAPI::toJsonValue(m_emails));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_individual_isSet) {
        obj.insert(QString("individual"), ::OpenAPI::toJsonValue(m_individual));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_middle_name_isSet) {
        obj.insert(QString("middle_name"), ::OpenAPI::toJsonValue(m_middle_name));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_parent.isSet()) {
        obj.insert(QString("parent"), ::OpenAPI::toJsonValue(m_parent));
    }
    if (m_payment_method_isSet) {
        obj.insert(QString("payment_method"), ::OpenAPI::toJsonValue(m_payment_method));
    }
    if (m_phone_numbers.size() > 0) {
        obj.insert(QString("phone_numbers"), ::OpenAPI::toJsonValue(m_phone_numbers));
    }
    if (m_project_isSet) {
        obj.insert(QString("project"), ::OpenAPI::toJsonValue(m_project));
    }
    if (m_row_version_isSet) {
        obj.insert(QString("row_version"), ::OpenAPI::toJsonValue(m_row_version));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_suffix_isSet) {
        obj.insert(QString("suffix"), ::OpenAPI::toJsonValue(m_suffix));
    }
    if (m_tax_number_isSet) {
        obj.insert(QString("tax_number"), ::OpenAPI::toJsonValue(m_tax_number));
    }
    if (m_tax_rate.isSet()) {
        obj.insert(QString("tax_rate"), ::OpenAPI::toJsonValue(m_tax_rate));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_updated_by_isSet) {
        obj.insert(QString("updated_by"), ::OpenAPI::toJsonValue(m_updated_by));
    }
    if (m_websites.size() > 0) {
        obj.insert(QString("websites"), ::OpenAPI::toJsonValue(m_websites));
    }
    return obj;
}

OAILinkedLedgerAccount OAICustomer::getAccount() const {
    return m_account;
}
void OAICustomer::setAccount(const OAILinkedLedgerAccount &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAICustomer::is_account_Set() const{
    return m_account_isSet;
}

bool OAICustomer::is_account_Valid() const{
    return m_account_isValid;
}

QList<OAIAddress> OAICustomer::getAddresses() const {
    return m_addresses;
}
void OAICustomer::setAddresses(const QList<OAIAddress> &addresses) {
    m_addresses = addresses;
    m_addresses_isSet = true;
}

bool OAICustomer::is_addresses_Set() const{
    return m_addresses_isSet;
}

bool OAICustomer::is_addresses_Valid() const{
    return m_addresses_isValid;
}

QList<OAIBankAccount> OAICustomer::getBankAccounts() const {
    return m_bank_accounts;
}
void OAICustomer::setBankAccounts(const QList<OAIBankAccount> &bank_accounts) {
    m_bank_accounts = bank_accounts;
    m_bank_accounts_isSet = true;
}

bool OAICustomer::is_bank_accounts_Set() const{
    return m_bank_accounts_isSet;
}

bool OAICustomer::is_bank_accounts_Valid() const{
    return m_bank_accounts_isValid;
}

QString OAICustomer::getChannel() const {
    return m_channel;
}
void OAICustomer::setChannel(const QString &channel) {
    m_channel = channel;
    m_channel_isSet = true;
}

bool OAICustomer::is_channel_Set() const{
    return m_channel_isSet;
}

bool OAICustomer::is_channel_Valid() const{
    return m_channel_isValid;
}

QString OAICustomer::getCompanyName() const {
    return m_company_name;
}
void OAICustomer::setCompanyName(const QString &company_name) {
    m_company_name = company_name;
    m_company_name_isSet = true;
}

bool OAICustomer::is_company_name_Set() const{
    return m_company_name_isSet;
}

bool OAICustomer::is_company_name_Valid() const{
    return m_company_name_isValid;
}

QDateTime OAICustomer::getCreatedAt() const {
    return m_created_at;
}
void OAICustomer::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAICustomer::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAICustomer::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAICustomer::getCreatedBy() const {
    return m_created_by;
}
void OAICustomer::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAICustomer::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAICustomer::is_created_by_Valid() const{
    return m_created_by_isValid;
}

OAICurrency OAICustomer::getCurrency() const {
    return m_currency;
}
void OAICustomer::setCurrency(const OAICurrency &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAICustomer::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAICustomer::is_currency_Valid() const{
    return m_currency_isValid;
}

OAIObject OAICustomer::getCustomMappings() const {
    return m_custom_mappings;
}
void OAICustomer::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAICustomer::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAICustomer::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

QString OAICustomer::getDisplayId() const {
    return m_display_id;
}
void OAICustomer::setDisplayId(const QString &display_id) {
    m_display_id = display_id;
    m_display_id_isSet = true;
}

bool OAICustomer::is_display_id_Set() const{
    return m_display_id_isSet;
}

bool OAICustomer::is_display_id_Valid() const{
    return m_display_id_isValid;
}

QString OAICustomer::getDisplayName() const {
    return m_display_name;
}
void OAICustomer::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAICustomer::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAICustomer::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAICustomer::getDownstreamId() const {
    return m_downstream_id;
}
void OAICustomer::setDownstreamId(const QString &downstream_id) {
    m_downstream_id = downstream_id;
    m_downstream_id_isSet = true;
}

bool OAICustomer::is_downstream_id_Set() const{
    return m_downstream_id_isSet;
}

bool OAICustomer::is_downstream_id_Valid() const{
    return m_downstream_id_isValid;
}

QList<OAIEmail> OAICustomer::getEmails() const {
    return m_emails;
}
void OAICustomer::setEmails(const QList<OAIEmail> &emails) {
    m_emails = emails;
    m_emails_isSet = true;
}

bool OAICustomer::is_emails_Set() const{
    return m_emails_isSet;
}

bool OAICustomer::is_emails_Valid() const{
    return m_emails_isValid;
}

QString OAICustomer::getFirstName() const {
    return m_first_name;
}
void OAICustomer::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAICustomer::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAICustomer::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAICustomer::getId() const {
    return m_id;
}
void OAICustomer::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICustomer::is_id_Set() const{
    return m_id_isSet;
}

bool OAICustomer::is_id_Valid() const{
    return m_id_isValid;
}

bool OAICustomer::isIndividual() const {
    return m_individual;
}
void OAICustomer::setIndividual(const bool &individual) {
    m_individual = individual;
    m_individual_isSet = true;
}

bool OAICustomer::is_individual_Set() const{
    return m_individual_isSet;
}

bool OAICustomer::is_individual_Valid() const{
    return m_individual_isValid;
}

QString OAICustomer::getLastName() const {
    return m_last_name;
}
void OAICustomer::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAICustomer::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAICustomer::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAICustomer::getMiddleName() const {
    return m_middle_name;
}
void OAICustomer::setMiddleName(const QString &middle_name) {
    m_middle_name = middle_name;
    m_middle_name_isSet = true;
}

bool OAICustomer::is_middle_name_Set() const{
    return m_middle_name_isSet;
}

bool OAICustomer::is_middle_name_Valid() const{
    return m_middle_name_isValid;
}

QString OAICustomer::getNotes() const {
    return m_notes;
}
void OAICustomer::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAICustomer::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAICustomer::is_notes_Valid() const{
    return m_notes_isValid;
}

OAILinkedParentCustomer OAICustomer::getParent() const {
    return m_parent;
}
void OAICustomer::setParent(const OAILinkedParentCustomer &parent) {
    m_parent = parent;
    m_parent_isSet = true;
}

bool OAICustomer::is_parent_Set() const{
    return m_parent_isSet;
}

bool OAICustomer::is_parent_Valid() const{
    return m_parent_isValid;
}

QString OAICustomer::getPaymentMethod() const {
    return m_payment_method;
}
void OAICustomer::setPaymentMethod(const QString &payment_method) {
    m_payment_method = payment_method;
    m_payment_method_isSet = true;
}

bool OAICustomer::is_payment_method_Set() const{
    return m_payment_method_isSet;
}

bool OAICustomer::is_payment_method_Valid() const{
    return m_payment_method_isValid;
}

QList<OAIPhoneNumber> OAICustomer::getPhoneNumbers() const {
    return m_phone_numbers;
}
void OAICustomer::setPhoneNumbers(const QList<OAIPhoneNumber> &phone_numbers) {
    m_phone_numbers = phone_numbers;
    m_phone_numbers_isSet = true;
}

bool OAICustomer::is_phone_numbers_Set() const{
    return m_phone_numbers_isSet;
}

bool OAICustomer::is_phone_numbers_Valid() const{
    return m_phone_numbers_isValid;
}

bool OAICustomer::isProject() const {
    return m_project;
}
void OAICustomer::setProject(const bool &project) {
    m_project = project;
    m_project_isSet = true;
}

bool OAICustomer::is_project_Set() const{
    return m_project_isSet;
}

bool OAICustomer::is_project_Valid() const{
    return m_project_isValid;
}

QString OAICustomer::getRowVersion() const {
    return m_row_version;
}
void OAICustomer::setRowVersion(const QString &row_version) {
    m_row_version = row_version;
    m_row_version_isSet = true;
}

bool OAICustomer::is_row_version_Set() const{
    return m_row_version_isSet;
}

bool OAICustomer::is_row_version_Valid() const{
    return m_row_version_isValid;
}

QString OAICustomer::getStatus() const {
    return m_status;
}
void OAICustomer::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAICustomer::is_status_Set() const{
    return m_status_isSet;
}

bool OAICustomer::is_status_Valid() const{
    return m_status_isValid;
}

QString OAICustomer::getSuffix() const {
    return m_suffix;
}
void OAICustomer::setSuffix(const QString &suffix) {
    m_suffix = suffix;
    m_suffix_isSet = true;
}

bool OAICustomer::is_suffix_Set() const{
    return m_suffix_isSet;
}

bool OAICustomer::is_suffix_Valid() const{
    return m_suffix_isValid;
}

QString OAICustomer::getTaxNumber() const {
    return m_tax_number;
}
void OAICustomer::setTaxNumber(const QString &tax_number) {
    m_tax_number = tax_number;
    m_tax_number_isSet = true;
}

bool OAICustomer::is_tax_number_Set() const{
    return m_tax_number_isSet;
}

bool OAICustomer::is_tax_number_Valid() const{
    return m_tax_number_isValid;
}

OAILinkedTaxRate OAICustomer::getTaxRate() const {
    return m_tax_rate;
}
void OAICustomer::setTaxRate(const OAILinkedTaxRate &tax_rate) {
    m_tax_rate = tax_rate;
    m_tax_rate_isSet = true;
}

bool OAICustomer::is_tax_rate_Set() const{
    return m_tax_rate_isSet;
}

bool OAICustomer::is_tax_rate_Valid() const{
    return m_tax_rate_isValid;
}

QString OAICustomer::getTitle() const {
    return m_title;
}
void OAICustomer::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAICustomer::is_title_Set() const{
    return m_title_isSet;
}

bool OAICustomer::is_title_Valid() const{
    return m_title_isValid;
}

QDateTime OAICustomer::getUpdatedAt() const {
    return m_updated_at;
}
void OAICustomer::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAICustomer::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAICustomer::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAICustomer::getUpdatedBy() const {
    return m_updated_by;
}
void OAICustomer::setUpdatedBy(const QString &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAICustomer::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAICustomer::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

QList<OAIWebsite> OAICustomer::getWebsites() const {
    return m_websites;
}
void OAICustomer::setWebsites(const QList<OAIWebsite> &websites) {
    m_websites = websites;
    m_websites_isSet = true;
}

bool OAICustomer::is_websites_Set() const{
    return m_websites_isSet;
}

bool OAICustomer::is_websites_Valid() const{
    return m_websites_isValid;
}

bool OAICustomer::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_bank_accounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_channel_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_mappings_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_downstream_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emails.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_individual_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_middle_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_numbers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_row_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_suffix_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_rate.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_websites.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomer::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && true;
}

} // namespace OpenAPI
