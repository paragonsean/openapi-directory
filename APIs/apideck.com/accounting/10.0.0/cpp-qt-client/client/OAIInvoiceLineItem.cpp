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

#include "OAIInvoiceLineItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInvoiceLineItem::OAIInvoiceLineItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInvoiceLineItem::OAIInvoiceLineItem() {
    this->initializeModel();
}

OAIInvoiceLineItem::~OAIInvoiceLineItem() {}

void OAIInvoiceLineItem::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_custom_mappings_isSet = false;
    m_custom_mappings_isValid = false;

    m_department_id_isSet = false;
    m_department_id_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_discount_amount_isSet = false;
    m_discount_amount_isValid = false;

    m_discount_percentage_isSet = false;
    m_discount_percentage_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_item_isSet = false;
    m_item_isValid = false;

    m_ledger_account_isSet = false;
    m_ledger_account_isValid = false;

    m_line_number_isSet = false;
    m_line_number_isValid = false;

    m_location_id_isSet = false;
    m_location_id_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_row_id_isSet = false;
    m_row_id_isValid = false;

    m_row_version_isSet = false;
    m_row_version_isValid = false;

    m_tax_amount_isSet = false;
    m_tax_amount_isValid = false;

    m_tax_rate_isSet = false;
    m_tax_rate_isValid = false;

    m_total_amount_isSet = false;
    m_total_amount_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_unit_of_measure_isSet = false;
    m_unit_of_measure_isValid = false;

    m_unit_price_isSet = false;
    m_unit_price_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;
}

void OAIInvoiceLineItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInvoiceLineItem::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_custom_mappings_isValid = ::OpenAPI::fromJsonValue(m_custom_mappings, json[QString("custom_mappings")]);
    m_custom_mappings_isSet = !json[QString("custom_mappings")].isNull() && m_custom_mappings_isValid;

    m_department_id_isValid = ::OpenAPI::fromJsonValue(m_department_id, json[QString("department_id")]);
    m_department_id_isSet = !json[QString("department_id")].isNull() && m_department_id_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_discount_amount_isValid = ::OpenAPI::fromJsonValue(m_discount_amount, json[QString("discount_amount")]);
    m_discount_amount_isSet = !json[QString("discount_amount")].isNull() && m_discount_amount_isValid;

    m_discount_percentage_isValid = ::OpenAPI::fromJsonValue(m_discount_percentage, json[QString("discount_percentage")]);
    m_discount_percentage_isSet = !json[QString("discount_percentage")].isNull() && m_discount_percentage_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_item_isValid = ::OpenAPI::fromJsonValue(m_item, json[QString("item")]);
    m_item_isSet = !json[QString("item")].isNull() && m_item_isValid;

    m_ledger_account_isValid = ::OpenAPI::fromJsonValue(m_ledger_account, json[QString("ledger_account")]);
    m_ledger_account_isSet = !json[QString("ledger_account")].isNull() && m_ledger_account_isValid;

    m_line_number_isValid = ::OpenAPI::fromJsonValue(m_line_number, json[QString("line_number")]);
    m_line_number_isSet = !json[QString("line_number")].isNull() && m_line_number_isValid;

    m_location_id_isValid = ::OpenAPI::fromJsonValue(m_location_id, json[QString("location_id")]);
    m_location_id_isSet = !json[QString("location_id")].isNull() && m_location_id_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_row_id_isValid = ::OpenAPI::fromJsonValue(m_row_id, json[QString("row_id")]);
    m_row_id_isSet = !json[QString("row_id")].isNull() && m_row_id_isValid;

    m_row_version_isValid = ::OpenAPI::fromJsonValue(m_row_version, json[QString("row_version")]);
    m_row_version_isSet = !json[QString("row_version")].isNull() && m_row_version_isValid;

    m_tax_amount_isValid = ::OpenAPI::fromJsonValue(m_tax_amount, json[QString("tax_amount")]);
    m_tax_amount_isSet = !json[QString("tax_amount")].isNull() && m_tax_amount_isValid;

    m_tax_rate_isValid = ::OpenAPI::fromJsonValue(m_tax_rate, json[QString("tax_rate")]);
    m_tax_rate_isSet = !json[QString("tax_rate")].isNull() && m_tax_rate_isValid;

    m_total_amount_isValid = ::OpenAPI::fromJsonValue(m_total_amount, json[QString("total_amount")]);
    m_total_amount_isSet = !json[QString("total_amount")].isNull() && m_total_amount_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_unit_of_measure_isValid = ::OpenAPI::fromJsonValue(m_unit_of_measure, json[QString("unit_of_measure")]);
    m_unit_of_measure_isSet = !json[QString("unit_of_measure")].isNull() && m_unit_of_measure_isValid;

    m_unit_price_isValid = ::OpenAPI::fromJsonValue(m_unit_price, json[QString("unit_price")]);
    m_unit_price_isSet = !json[QString("unit_price")].isNull() && m_unit_price_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updated_by")]);
    m_updated_by_isSet = !json[QString("updated_by")].isNull() && m_updated_by_isValid;
}

QString OAIInvoiceLineItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInvoiceLineItem::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_created_by_isSet) {
        obj.insert(QString("created_by"), ::OpenAPI::toJsonValue(m_created_by));
    }
    if (m_custom_mappings_isSet) {
        obj.insert(QString("custom_mappings"), ::OpenAPI::toJsonValue(m_custom_mappings));
    }
    if (m_department_id_isSet) {
        obj.insert(QString("department_id"), ::OpenAPI::toJsonValue(m_department_id));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_discount_amount_isSet) {
        obj.insert(QString("discount_amount"), ::OpenAPI::toJsonValue(m_discount_amount));
    }
    if (m_discount_percentage_isSet) {
        obj.insert(QString("discount_percentage"), ::OpenAPI::toJsonValue(m_discount_percentage));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_item.isSet()) {
        obj.insert(QString("item"), ::OpenAPI::toJsonValue(m_item));
    }
    if (m_ledger_account.isSet()) {
        obj.insert(QString("ledger_account"), ::OpenAPI::toJsonValue(m_ledger_account));
    }
    if (m_line_number_isSet) {
        obj.insert(QString("line_number"), ::OpenAPI::toJsonValue(m_line_number));
    }
    if (m_location_id_isSet) {
        obj.insert(QString("location_id"), ::OpenAPI::toJsonValue(m_location_id));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_row_id_isSet) {
        obj.insert(QString("row_id"), ::OpenAPI::toJsonValue(m_row_id));
    }
    if (m_row_version_isSet) {
        obj.insert(QString("row_version"), ::OpenAPI::toJsonValue(m_row_version));
    }
    if (m_tax_amount_isSet) {
        obj.insert(QString("tax_amount"), ::OpenAPI::toJsonValue(m_tax_amount));
    }
    if (m_tax_rate.isSet()) {
        obj.insert(QString("tax_rate"), ::OpenAPI::toJsonValue(m_tax_rate));
    }
    if (m_total_amount_isSet) {
        obj.insert(QString("total_amount"), ::OpenAPI::toJsonValue(m_total_amount));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_unit_of_measure_isSet) {
        obj.insert(QString("unit_of_measure"), ::OpenAPI::toJsonValue(m_unit_of_measure));
    }
    if (m_unit_price_isSet) {
        obj.insert(QString("unit_price"), ::OpenAPI::toJsonValue(m_unit_price));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_updated_by_isSet) {
        obj.insert(QString("updated_by"), ::OpenAPI::toJsonValue(m_updated_by));
    }
    return obj;
}

QString OAIInvoiceLineItem::getCode() const {
    return m_code;
}
void OAIInvoiceLineItem::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIInvoiceLineItem::is_code_Set() const{
    return m_code_isSet;
}

bool OAIInvoiceLineItem::is_code_Valid() const{
    return m_code_isValid;
}

QDateTime OAIInvoiceLineItem::getCreatedAt() const {
    return m_created_at;
}
void OAIInvoiceLineItem::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIInvoiceLineItem::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIInvoiceLineItem::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIInvoiceLineItem::getCreatedBy() const {
    return m_created_by;
}
void OAIInvoiceLineItem::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIInvoiceLineItem::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIInvoiceLineItem::is_created_by_Valid() const{
    return m_created_by_isValid;
}

OAIObject OAIInvoiceLineItem::getCustomMappings() const {
    return m_custom_mappings;
}
void OAIInvoiceLineItem::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAIInvoiceLineItem::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAIInvoiceLineItem::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

QString OAIInvoiceLineItem::getDepartmentId() const {
    return m_department_id;
}
void OAIInvoiceLineItem::setDepartmentId(const QString &department_id) {
    m_department_id = department_id;
    m_department_id_isSet = true;
}

bool OAIInvoiceLineItem::is_department_id_Set() const{
    return m_department_id_isSet;
}

bool OAIInvoiceLineItem::is_department_id_Valid() const{
    return m_department_id_isValid;
}

QString OAIInvoiceLineItem::getDescription() const {
    return m_description;
}
void OAIInvoiceLineItem::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIInvoiceLineItem::is_description_Set() const{
    return m_description_isSet;
}

bool OAIInvoiceLineItem::is_description_Valid() const{
    return m_description_isValid;
}

double OAIInvoiceLineItem::getDiscountAmount() const {
    return m_discount_amount;
}
void OAIInvoiceLineItem::setDiscountAmount(const double &discount_amount) {
    m_discount_amount = discount_amount;
    m_discount_amount_isSet = true;
}

bool OAIInvoiceLineItem::is_discount_amount_Set() const{
    return m_discount_amount_isSet;
}

bool OAIInvoiceLineItem::is_discount_amount_Valid() const{
    return m_discount_amount_isValid;
}

double OAIInvoiceLineItem::getDiscountPercentage() const {
    return m_discount_percentage;
}
void OAIInvoiceLineItem::setDiscountPercentage(const double &discount_percentage) {
    m_discount_percentage = discount_percentage;
    m_discount_percentage_isSet = true;
}

bool OAIInvoiceLineItem::is_discount_percentage_Set() const{
    return m_discount_percentage_isSet;
}

bool OAIInvoiceLineItem::is_discount_percentage_Valid() const{
    return m_discount_percentage_isValid;
}

QString OAIInvoiceLineItem::getId() const {
    return m_id;
}
void OAIInvoiceLineItem::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIInvoiceLineItem::is_id_Set() const{
    return m_id_isSet;
}

bool OAIInvoiceLineItem::is_id_Valid() const{
    return m_id_isValid;
}

OAILinkedInvoiceItem OAIInvoiceLineItem::getItem() const {
    return m_item;
}
void OAIInvoiceLineItem::setItem(const OAILinkedInvoiceItem &item) {
    m_item = item;
    m_item_isSet = true;
}

bool OAIInvoiceLineItem::is_item_Set() const{
    return m_item_isSet;
}

bool OAIInvoiceLineItem::is_item_Valid() const{
    return m_item_isValid;
}

OAILinkedLedgerAccount OAIInvoiceLineItem::getLedgerAccount() const {
    return m_ledger_account;
}
void OAIInvoiceLineItem::setLedgerAccount(const OAILinkedLedgerAccount &ledger_account) {
    m_ledger_account = ledger_account;
    m_ledger_account_isSet = true;
}

bool OAIInvoiceLineItem::is_ledger_account_Set() const{
    return m_ledger_account_isSet;
}

bool OAIInvoiceLineItem::is_ledger_account_Valid() const{
    return m_ledger_account_isValid;
}

qint32 OAIInvoiceLineItem::getLineNumber() const {
    return m_line_number;
}
void OAIInvoiceLineItem::setLineNumber(const qint32 &line_number) {
    m_line_number = line_number;
    m_line_number_isSet = true;
}

bool OAIInvoiceLineItem::is_line_number_Set() const{
    return m_line_number_isSet;
}

bool OAIInvoiceLineItem::is_line_number_Valid() const{
    return m_line_number_isValid;
}

QString OAIInvoiceLineItem::getLocationId() const {
    return m_location_id;
}
void OAIInvoiceLineItem::setLocationId(const QString &location_id) {
    m_location_id = location_id;
    m_location_id_isSet = true;
}

bool OAIInvoiceLineItem::is_location_id_Set() const{
    return m_location_id_isSet;
}

bool OAIInvoiceLineItem::is_location_id_Valid() const{
    return m_location_id_isValid;
}

double OAIInvoiceLineItem::getQuantity() const {
    return m_quantity;
}
void OAIInvoiceLineItem::setQuantity(const double &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIInvoiceLineItem::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIInvoiceLineItem::is_quantity_Valid() const{
    return m_quantity_isValid;
}

QString OAIInvoiceLineItem::getRowId() const {
    return m_row_id;
}
void OAIInvoiceLineItem::setRowId(const QString &row_id) {
    m_row_id = row_id;
    m_row_id_isSet = true;
}

bool OAIInvoiceLineItem::is_row_id_Set() const{
    return m_row_id_isSet;
}

bool OAIInvoiceLineItem::is_row_id_Valid() const{
    return m_row_id_isValid;
}

QString OAIInvoiceLineItem::getRowVersion() const {
    return m_row_version;
}
void OAIInvoiceLineItem::setRowVersion(const QString &row_version) {
    m_row_version = row_version;
    m_row_version_isSet = true;
}

bool OAIInvoiceLineItem::is_row_version_Set() const{
    return m_row_version_isSet;
}

bool OAIInvoiceLineItem::is_row_version_Valid() const{
    return m_row_version_isValid;
}

double OAIInvoiceLineItem::getTaxAmount() const {
    return m_tax_amount;
}
void OAIInvoiceLineItem::setTaxAmount(const double &tax_amount) {
    m_tax_amount = tax_amount;
    m_tax_amount_isSet = true;
}

bool OAIInvoiceLineItem::is_tax_amount_Set() const{
    return m_tax_amount_isSet;
}

bool OAIInvoiceLineItem::is_tax_amount_Valid() const{
    return m_tax_amount_isValid;
}

OAILinkedTaxRate OAIInvoiceLineItem::getTaxRate() const {
    return m_tax_rate;
}
void OAIInvoiceLineItem::setTaxRate(const OAILinkedTaxRate &tax_rate) {
    m_tax_rate = tax_rate;
    m_tax_rate_isSet = true;
}

bool OAIInvoiceLineItem::is_tax_rate_Set() const{
    return m_tax_rate_isSet;
}

bool OAIInvoiceLineItem::is_tax_rate_Valid() const{
    return m_tax_rate_isValid;
}

double OAIInvoiceLineItem::getTotalAmount() const {
    return m_total_amount;
}
void OAIInvoiceLineItem::setTotalAmount(const double &total_amount) {
    m_total_amount = total_amount;
    m_total_amount_isSet = true;
}

bool OAIInvoiceLineItem::is_total_amount_Set() const{
    return m_total_amount_isSet;
}

bool OAIInvoiceLineItem::is_total_amount_Valid() const{
    return m_total_amount_isValid;
}

QString OAIInvoiceLineItem::getType() const {
    return m_type;
}
void OAIInvoiceLineItem::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIInvoiceLineItem::is_type_Set() const{
    return m_type_isSet;
}

bool OAIInvoiceLineItem::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIInvoiceLineItem::getUnitOfMeasure() const {
    return m_unit_of_measure;
}
void OAIInvoiceLineItem::setUnitOfMeasure(const QString &unit_of_measure) {
    m_unit_of_measure = unit_of_measure;
    m_unit_of_measure_isSet = true;
}

bool OAIInvoiceLineItem::is_unit_of_measure_Set() const{
    return m_unit_of_measure_isSet;
}

bool OAIInvoiceLineItem::is_unit_of_measure_Valid() const{
    return m_unit_of_measure_isValid;
}

double OAIInvoiceLineItem::getUnitPrice() const {
    return m_unit_price;
}
void OAIInvoiceLineItem::setUnitPrice(const double &unit_price) {
    m_unit_price = unit_price;
    m_unit_price_isSet = true;
}

bool OAIInvoiceLineItem::is_unit_price_Set() const{
    return m_unit_price_isSet;
}

bool OAIInvoiceLineItem::is_unit_price_Valid() const{
    return m_unit_price_isValid;
}

QDateTime OAIInvoiceLineItem::getUpdatedAt() const {
    return m_updated_at;
}
void OAIInvoiceLineItem::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIInvoiceLineItem::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIInvoiceLineItem::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIInvoiceLineItem::getUpdatedBy() const {
    return m_updated_by;
}
void OAIInvoiceLineItem::setUpdatedBy(const QString &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAIInvoiceLineItem::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAIInvoiceLineItem::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

bool OAIInvoiceLineItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
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

        if (m_custom_mappings_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_department_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_item.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ledger_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_line_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_row_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_row_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_rate.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_of_measure_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_price_isSet) {
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

bool OAIInvoiceLineItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
