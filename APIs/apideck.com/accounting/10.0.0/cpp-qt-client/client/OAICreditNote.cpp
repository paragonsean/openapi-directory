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

#include "OAICreditNote.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreditNote::OAICreditNote(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreditNote::OAICreditNote() {
    this->initializeModel();
}

OAICreditNote::~OAICreditNote() {}

void OAICreditNote::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;

    m_allocations_isSet = false;
    m_allocations_isValid = false;

    m_balance_isSet = false;
    m_balance_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_currency_rate_isSet = false;
    m_currency_rate_isValid = false;

    m_custom_mappings_isSet = false;
    m_custom_mappings_isValid = false;

    m_customer_isSet = false;
    m_customer_isValid = false;

    m_date_issued_isSet = false;
    m_date_issued_isValid = false;

    m_date_paid_isSet = false;
    m_date_paid_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_line_items_isSet = false;
    m_line_items_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_reference_isSet = false;
    m_reference_isValid = false;

    m_remaining_credit_isSet = false;
    m_remaining_credit_isValid = false;

    m_row_version_isSet = false;
    m_row_version_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_sub_total_isSet = false;
    m_sub_total_isValid = false;

    m_tax_code_isSet = false;
    m_tax_code_isValid = false;

    m_tax_inclusive_isSet = false;
    m_tax_inclusive_isValid = false;

    m_terms_isSet = false;
    m_terms_isValid = false;

    m_total_amount_isSet = false;
    m_total_amount_isValid = false;

    m_total_tax_isSet = false;
    m_total_tax_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;
}

void OAICreditNote::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreditNote::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;

    m_allocations_isValid = ::OpenAPI::fromJsonValue(m_allocations, json[QString("allocations")]);
    m_allocations_isSet = !json[QString("allocations")].isNull() && m_allocations_isValid;

    m_balance_isValid = ::OpenAPI::fromJsonValue(m_balance, json[QString("balance")]);
    m_balance_isSet = !json[QString("balance")].isNull() && m_balance_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_currency_rate_isValid = ::OpenAPI::fromJsonValue(m_currency_rate, json[QString("currency_rate")]);
    m_currency_rate_isSet = !json[QString("currency_rate")].isNull() && m_currency_rate_isValid;

    m_custom_mappings_isValid = ::OpenAPI::fromJsonValue(m_custom_mappings, json[QString("custom_mappings")]);
    m_custom_mappings_isSet = !json[QString("custom_mappings")].isNull() && m_custom_mappings_isValid;

    m_customer_isValid = ::OpenAPI::fromJsonValue(m_customer, json[QString("customer")]);
    m_customer_isSet = !json[QString("customer")].isNull() && m_customer_isValid;

    m_date_issued_isValid = ::OpenAPI::fromJsonValue(m_date_issued, json[QString("date_issued")]);
    m_date_issued_isSet = !json[QString("date_issued")].isNull() && m_date_issued_isValid;

    m_date_paid_isValid = ::OpenAPI::fromJsonValue(m_date_paid, json[QString("date_paid")]);
    m_date_paid_isSet = !json[QString("date_paid")].isNull() && m_date_paid_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_line_items_isValid = ::OpenAPI::fromJsonValue(m_line_items, json[QString("line_items")]);
    m_line_items_isSet = !json[QString("line_items")].isNull() && m_line_items_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("number")]);
    m_number_isSet = !json[QString("number")].isNull() && m_number_isValid;

    m_reference_isValid = ::OpenAPI::fromJsonValue(m_reference, json[QString("reference")]);
    m_reference_isSet = !json[QString("reference")].isNull() && m_reference_isValid;

    m_remaining_credit_isValid = ::OpenAPI::fromJsonValue(m_remaining_credit, json[QString("remaining_credit")]);
    m_remaining_credit_isSet = !json[QString("remaining_credit")].isNull() && m_remaining_credit_isValid;

    m_row_version_isValid = ::OpenAPI::fromJsonValue(m_row_version, json[QString("row_version")]);
    m_row_version_isSet = !json[QString("row_version")].isNull() && m_row_version_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_sub_total_isValid = ::OpenAPI::fromJsonValue(m_sub_total, json[QString("sub_total")]);
    m_sub_total_isSet = !json[QString("sub_total")].isNull() && m_sub_total_isValid;

    m_tax_code_isValid = ::OpenAPI::fromJsonValue(m_tax_code, json[QString("tax_code")]);
    m_tax_code_isSet = !json[QString("tax_code")].isNull() && m_tax_code_isValid;

    m_tax_inclusive_isValid = ::OpenAPI::fromJsonValue(m_tax_inclusive, json[QString("tax_inclusive")]);
    m_tax_inclusive_isSet = !json[QString("tax_inclusive")].isNull() && m_tax_inclusive_isValid;

    m_terms_isValid = ::OpenAPI::fromJsonValue(m_terms, json[QString("terms")]);
    m_terms_isSet = !json[QString("terms")].isNull() && m_terms_isValid;

    m_total_amount_isValid = ::OpenAPI::fromJsonValue(m_total_amount, json[QString("total_amount")]);
    m_total_amount_isSet = !json[QString("total_amount")].isNull() && m_total_amount_isValid;

    m_total_tax_isValid = ::OpenAPI::fromJsonValue(m_total_tax, json[QString("total_tax")]);
    m_total_tax_isSet = !json[QString("total_tax")].isNull() && m_total_tax_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updated_by")]);
    m_updated_by_isSet = !json[QString("updated_by")].isNull() && m_updated_by_isValid;
}

QString OAICreditNote::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreditNote::asJsonObject() const {
    QJsonObject obj;
    if (m_account.isSet()) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    if (m_allocations.size() > 0) {
        obj.insert(QString("allocations"), ::OpenAPI::toJsonValue(m_allocations));
    }
    if (m_balance_isSet) {
        obj.insert(QString("balance"), ::OpenAPI::toJsonValue(m_balance));
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
    if (m_currency_rate_isSet) {
        obj.insert(QString("currency_rate"), ::OpenAPI::toJsonValue(m_currency_rate));
    }
    if (m_custom_mappings_isSet) {
        obj.insert(QString("custom_mappings"), ::OpenAPI::toJsonValue(m_custom_mappings));
    }
    if (m_customer.isSet()) {
        obj.insert(QString("customer"), ::OpenAPI::toJsonValue(m_customer));
    }
    if (m_date_issued_isSet) {
        obj.insert(QString("date_issued"), ::OpenAPI::toJsonValue(m_date_issued));
    }
    if (m_date_paid_isSet) {
        obj.insert(QString("date_paid"), ::OpenAPI::toJsonValue(m_date_paid));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_line_items.size() > 0) {
        obj.insert(QString("line_items"), ::OpenAPI::toJsonValue(m_line_items));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_number_isSet) {
        obj.insert(QString("number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_reference_isSet) {
        obj.insert(QString("reference"), ::OpenAPI::toJsonValue(m_reference));
    }
    if (m_remaining_credit_isSet) {
        obj.insert(QString("remaining_credit"), ::OpenAPI::toJsonValue(m_remaining_credit));
    }
    if (m_row_version_isSet) {
        obj.insert(QString("row_version"), ::OpenAPI::toJsonValue(m_row_version));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_sub_total_isSet) {
        obj.insert(QString("sub_total"), ::OpenAPI::toJsonValue(m_sub_total));
    }
    if (m_tax_code_isSet) {
        obj.insert(QString("tax_code"), ::OpenAPI::toJsonValue(m_tax_code));
    }
    if (m_tax_inclusive_isSet) {
        obj.insert(QString("tax_inclusive"), ::OpenAPI::toJsonValue(m_tax_inclusive));
    }
    if (m_terms_isSet) {
        obj.insert(QString("terms"), ::OpenAPI::toJsonValue(m_terms));
    }
    if (m_total_amount_isSet) {
        obj.insert(QString("total_amount"), ::OpenAPI::toJsonValue(m_total_amount));
    }
    if (m_total_tax_isSet) {
        obj.insert(QString("total_tax"), ::OpenAPI::toJsonValue(m_total_tax));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_updated_by_isSet) {
        obj.insert(QString("updated_by"), ::OpenAPI::toJsonValue(m_updated_by));
    }
    return obj;
}

OAILinkedLedgerAccount OAICreditNote::getAccount() const {
    return m_account;
}
void OAICreditNote::setAccount(const OAILinkedLedgerAccount &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAICreditNote::is_account_Set() const{
    return m_account_isSet;
}

bool OAICreditNote::is_account_Valid() const{
    return m_account_isValid;
}

QList<OAICreditNote_allocations_inner> OAICreditNote::getAllocations() const {
    return m_allocations;
}
void OAICreditNote::setAllocations(const QList<OAICreditNote_allocations_inner> &allocations) {
    m_allocations = allocations;
    m_allocations_isSet = true;
}

bool OAICreditNote::is_allocations_Set() const{
    return m_allocations_isSet;
}

bool OAICreditNote::is_allocations_Valid() const{
    return m_allocations_isValid;
}

double OAICreditNote::getBalance() const {
    return m_balance;
}
void OAICreditNote::setBalance(const double &balance) {
    m_balance = balance;
    m_balance_isSet = true;
}

bool OAICreditNote::is_balance_Set() const{
    return m_balance_isSet;
}

bool OAICreditNote::is_balance_Valid() const{
    return m_balance_isValid;
}

QDateTime OAICreditNote::getCreatedAt() const {
    return m_created_at;
}
void OAICreditNote::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAICreditNote::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAICreditNote::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAICreditNote::getCreatedBy() const {
    return m_created_by;
}
void OAICreditNote::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAICreditNote::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAICreditNote::is_created_by_Valid() const{
    return m_created_by_isValid;
}

OAICurrency OAICreditNote::getCurrency() const {
    return m_currency;
}
void OAICreditNote::setCurrency(const OAICurrency &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAICreditNote::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAICreditNote::is_currency_Valid() const{
    return m_currency_isValid;
}

double OAICreditNote::getCurrencyRate() const {
    return m_currency_rate;
}
void OAICreditNote::setCurrencyRate(const double &currency_rate) {
    m_currency_rate = currency_rate;
    m_currency_rate_isSet = true;
}

bool OAICreditNote::is_currency_rate_Set() const{
    return m_currency_rate_isSet;
}

bool OAICreditNote::is_currency_rate_Valid() const{
    return m_currency_rate_isValid;
}

OAIObject OAICreditNote::getCustomMappings() const {
    return m_custom_mappings;
}
void OAICreditNote::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAICreditNote::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAICreditNote::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

OAILinkedCustomer OAICreditNote::getCustomer() const {
    return m_customer;
}
void OAICreditNote::setCustomer(const OAILinkedCustomer &customer) {
    m_customer = customer;
    m_customer_isSet = true;
}

bool OAICreditNote::is_customer_Set() const{
    return m_customer_isSet;
}

bool OAICreditNote::is_customer_Valid() const{
    return m_customer_isValid;
}

QDateTime OAICreditNote::getDateIssued() const {
    return m_date_issued;
}
void OAICreditNote::setDateIssued(const QDateTime &date_issued) {
    m_date_issued = date_issued;
    m_date_issued_isSet = true;
}

bool OAICreditNote::is_date_issued_Set() const{
    return m_date_issued_isSet;
}

bool OAICreditNote::is_date_issued_Valid() const{
    return m_date_issued_isValid;
}

QDateTime OAICreditNote::getDatePaid() const {
    return m_date_paid;
}
void OAICreditNote::setDatePaid(const QDateTime &date_paid) {
    m_date_paid = date_paid;
    m_date_paid_isSet = true;
}

bool OAICreditNote::is_date_paid_Set() const{
    return m_date_paid_isSet;
}

bool OAICreditNote::is_date_paid_Valid() const{
    return m_date_paid_isValid;
}

QString OAICreditNote::getId() const {
    return m_id;
}
void OAICreditNote::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICreditNote::is_id_Set() const{
    return m_id_isSet;
}

bool OAICreditNote::is_id_Valid() const{
    return m_id_isValid;
}

QList<OAIInvoiceLineItem> OAICreditNote::getLineItems() const {
    return m_line_items;
}
void OAICreditNote::setLineItems(const QList<OAIInvoiceLineItem> &line_items) {
    m_line_items = line_items;
    m_line_items_isSet = true;
}

bool OAICreditNote::is_line_items_Set() const{
    return m_line_items_isSet;
}

bool OAICreditNote::is_line_items_Valid() const{
    return m_line_items_isValid;
}

QString OAICreditNote::getNote() const {
    return m_note;
}
void OAICreditNote::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAICreditNote::is_note_Set() const{
    return m_note_isSet;
}

bool OAICreditNote::is_note_Valid() const{
    return m_note_isValid;
}

QString OAICreditNote::getNumber() const {
    return m_number;
}
void OAICreditNote::setNumber(const QString &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAICreditNote::is_number_Set() const{
    return m_number_isSet;
}

bool OAICreditNote::is_number_Valid() const{
    return m_number_isValid;
}

QString OAICreditNote::getReference() const {
    return m_reference;
}
void OAICreditNote::setReference(const QString &reference) {
    m_reference = reference;
    m_reference_isSet = true;
}

bool OAICreditNote::is_reference_Set() const{
    return m_reference_isSet;
}

bool OAICreditNote::is_reference_Valid() const{
    return m_reference_isValid;
}

double OAICreditNote::getRemainingCredit() const {
    return m_remaining_credit;
}
void OAICreditNote::setRemainingCredit(const double &remaining_credit) {
    m_remaining_credit = remaining_credit;
    m_remaining_credit_isSet = true;
}

bool OAICreditNote::is_remaining_credit_Set() const{
    return m_remaining_credit_isSet;
}

bool OAICreditNote::is_remaining_credit_Valid() const{
    return m_remaining_credit_isValid;
}

QString OAICreditNote::getRowVersion() const {
    return m_row_version;
}
void OAICreditNote::setRowVersion(const QString &row_version) {
    m_row_version = row_version;
    m_row_version_isSet = true;
}

bool OAICreditNote::is_row_version_Set() const{
    return m_row_version_isSet;
}

bool OAICreditNote::is_row_version_Valid() const{
    return m_row_version_isValid;
}

QString OAICreditNote::getStatus() const {
    return m_status;
}
void OAICreditNote::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAICreditNote::is_status_Set() const{
    return m_status_isSet;
}

bool OAICreditNote::is_status_Valid() const{
    return m_status_isValid;
}

double OAICreditNote::getSubTotal() const {
    return m_sub_total;
}
void OAICreditNote::setSubTotal(const double &sub_total) {
    m_sub_total = sub_total;
    m_sub_total_isSet = true;
}

bool OAICreditNote::is_sub_total_Set() const{
    return m_sub_total_isSet;
}

bool OAICreditNote::is_sub_total_Valid() const{
    return m_sub_total_isValid;
}

QString OAICreditNote::getTaxCode() const {
    return m_tax_code;
}
void OAICreditNote::setTaxCode(const QString &tax_code) {
    m_tax_code = tax_code;
    m_tax_code_isSet = true;
}

bool OAICreditNote::is_tax_code_Set() const{
    return m_tax_code_isSet;
}

bool OAICreditNote::is_tax_code_Valid() const{
    return m_tax_code_isValid;
}

bool OAICreditNote::isTaxInclusive() const {
    return m_tax_inclusive;
}
void OAICreditNote::setTaxInclusive(const bool &tax_inclusive) {
    m_tax_inclusive = tax_inclusive;
    m_tax_inclusive_isSet = true;
}

bool OAICreditNote::is_tax_inclusive_Set() const{
    return m_tax_inclusive_isSet;
}

bool OAICreditNote::is_tax_inclusive_Valid() const{
    return m_tax_inclusive_isValid;
}

QString OAICreditNote::getTerms() const {
    return m_terms;
}
void OAICreditNote::setTerms(const QString &terms) {
    m_terms = terms;
    m_terms_isSet = true;
}

bool OAICreditNote::is_terms_Set() const{
    return m_terms_isSet;
}

bool OAICreditNote::is_terms_Valid() const{
    return m_terms_isValid;
}

double OAICreditNote::getTotalAmount() const {
    return m_total_amount;
}
void OAICreditNote::setTotalAmount(const double &total_amount) {
    m_total_amount = total_amount;
    m_total_amount_isSet = true;
}

bool OAICreditNote::is_total_amount_Set() const{
    return m_total_amount_isSet;
}

bool OAICreditNote::is_total_amount_Valid() const{
    return m_total_amount_isValid;
}

double OAICreditNote::getTotalTax() const {
    return m_total_tax;
}
void OAICreditNote::setTotalTax(const double &total_tax) {
    m_total_tax = total_tax;
    m_total_tax_isSet = true;
}

bool OAICreditNote::is_total_tax_Set() const{
    return m_total_tax_isSet;
}

bool OAICreditNote::is_total_tax_Valid() const{
    return m_total_tax_isValid;
}

QString OAICreditNote::getType() const {
    return m_type;
}
void OAICreditNote::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICreditNote::is_type_Set() const{
    return m_type_isSet;
}

bool OAICreditNote::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAICreditNote::getUpdatedAt() const {
    return m_updated_at;
}
void OAICreditNote::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAICreditNote::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAICreditNote::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAICreditNote::getUpdatedBy() const {
    return m_updated_by;
}
void OAICreditNote::setUpdatedBy(const QString &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAICreditNote::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAICreditNote::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

bool OAICreditNote::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_allocations.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_balance_isSet) {
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

        if (m_currency_rate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_mappings_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_issued_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_date_paid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_remaining_credit_isSet) {
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

        if (m_sub_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_inclusive_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_terms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAICreditNote::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_total_amount_isValid && true;
}

} // namespace OpenAPI
