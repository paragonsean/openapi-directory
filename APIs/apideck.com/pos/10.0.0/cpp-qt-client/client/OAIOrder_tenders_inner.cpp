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

#include "OAIOrder_tenders_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrder_tenders_inner::OAIOrder_tenders_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrder_tenders_inner::OAIOrder_tenders_inner() {
    this->initializeModel();
}

OAIOrder_tenders_inner::~OAIOrder_tenders_inner() {}

void OAIOrder_tenders_inner::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_buyer_tendered_cash_amount_isSet = false;
    m_buyer_tendered_cash_amount_isValid = false;

    m_card_isSet = false;
    m_card_isValid = false;

    m_card_entry_method_isSet = false;
    m_card_entry_method_isValid = false;

    m_card_status_isSet = false;
    m_card_status_isValid = false;

    m_change_back_cash_amount_isSet = false;
    m_change_back_cash_amount_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_location_id_isSet = false;
    m_location_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_payment_id_isSet = false;
    m_payment_id_isValid = false;

    m_percentage_isSet = false;
    m_percentage_isValid = false;

    m_total_amount_isSet = false;
    m_total_amount_isValid = false;

    m_total_discount_isSet = false;
    m_total_discount_isValid = false;

    m_total_processing_fee_isSet = false;
    m_total_processing_fee_isValid = false;

    m_total_refund_isSet = false;
    m_total_refund_isValid = false;

    m_total_service_charge_isSet = false;
    m_total_service_charge_isValid = false;

    m_total_tax_isSet = false;
    m_total_tax_isValid = false;

    m_total_tip_isSet = false;
    m_total_tip_isValid = false;

    m_transaction_id_isSet = false;
    m_transaction_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIOrder_tenders_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrder_tenders_inner::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_buyer_tendered_cash_amount_isValid = ::OpenAPI::fromJsonValue(m_buyer_tendered_cash_amount, json[QString("buyer_tendered_cash_amount")]);
    m_buyer_tendered_cash_amount_isSet = !json[QString("buyer_tendered_cash_amount")].isNull() && m_buyer_tendered_cash_amount_isValid;

    m_card_isValid = ::OpenAPI::fromJsonValue(m_card, json[QString("card")]);
    m_card_isSet = !json[QString("card")].isNull() && m_card_isValid;

    m_card_entry_method_isValid = ::OpenAPI::fromJsonValue(m_card_entry_method, json[QString("card_entry_method")]);
    m_card_entry_method_isSet = !json[QString("card_entry_method")].isNull() && m_card_entry_method_isValid;

    m_card_status_isValid = ::OpenAPI::fromJsonValue(m_card_status, json[QString("card_status")]);
    m_card_status_isSet = !json[QString("card_status")].isNull() && m_card_status_isValid;

    m_change_back_cash_amount_isValid = ::OpenAPI::fromJsonValue(m_change_back_cash_amount, json[QString("change_back_cash_amount")]);
    m_change_back_cash_amount_isSet = !json[QString("change_back_cash_amount")].isNull() && m_change_back_cash_amount_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_location_id_isValid = ::OpenAPI::fromJsonValue(m_location_id, json[QString("location_id")]);
    m_location_id_isSet = !json[QString("location_id")].isNull() && m_location_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_payment_id_isValid = ::OpenAPI::fromJsonValue(m_payment_id, json[QString("payment_id")]);
    m_payment_id_isSet = !json[QString("payment_id")].isNull() && m_payment_id_isValid;

    m_percentage_isValid = ::OpenAPI::fromJsonValue(m_percentage, json[QString("percentage")]);
    m_percentage_isSet = !json[QString("percentage")].isNull() && m_percentage_isValid;

    m_total_amount_isValid = ::OpenAPI::fromJsonValue(m_total_amount, json[QString("total_amount")]);
    m_total_amount_isSet = !json[QString("total_amount")].isNull() && m_total_amount_isValid;

    m_total_discount_isValid = ::OpenAPI::fromJsonValue(m_total_discount, json[QString("total_discount")]);
    m_total_discount_isSet = !json[QString("total_discount")].isNull() && m_total_discount_isValid;

    m_total_processing_fee_isValid = ::OpenAPI::fromJsonValue(m_total_processing_fee, json[QString("total_processing_fee")]);
    m_total_processing_fee_isSet = !json[QString("total_processing_fee")].isNull() && m_total_processing_fee_isValid;

    m_total_refund_isValid = ::OpenAPI::fromJsonValue(m_total_refund, json[QString("total_refund")]);
    m_total_refund_isSet = !json[QString("total_refund")].isNull() && m_total_refund_isValid;

    m_total_service_charge_isValid = ::OpenAPI::fromJsonValue(m_total_service_charge, json[QString("total_service_charge")]);
    m_total_service_charge_isSet = !json[QString("total_service_charge")].isNull() && m_total_service_charge_isValid;

    m_total_tax_isValid = ::OpenAPI::fromJsonValue(m_total_tax, json[QString("total_tax")]);
    m_total_tax_isSet = !json[QString("total_tax")].isNull() && m_total_tax_isValid;

    m_total_tip_isValid = ::OpenAPI::fromJsonValue(m_total_tip, json[QString("total_tip")]);
    m_total_tip_isSet = !json[QString("total_tip")].isNull() && m_total_tip_isValid;

    m_transaction_id_isValid = ::OpenAPI::fromJsonValue(m_transaction_id, json[QString("transaction_id")]);
    m_transaction_id_isSet = !json[QString("transaction_id")].isNull() && m_transaction_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIOrder_tenders_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrder_tenders_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_buyer_tendered_cash_amount_isSet) {
        obj.insert(QString("buyer_tendered_cash_amount"), ::OpenAPI::toJsonValue(m_buyer_tendered_cash_amount));
    }
    if (m_card.isSet()) {
        obj.insert(QString("card"), ::OpenAPI::toJsonValue(m_card));
    }
    if (m_card_entry_method_isSet) {
        obj.insert(QString("card_entry_method"), ::OpenAPI::toJsonValue(m_card_entry_method));
    }
    if (m_card_status_isSet) {
        obj.insert(QString("card_status"), ::OpenAPI::toJsonValue(m_card_status));
    }
    if (m_change_back_cash_amount_isSet) {
        obj.insert(QString("change_back_cash_amount"), ::OpenAPI::toJsonValue(m_change_back_cash_amount));
    }
    if (m_currency.isSet()) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_location_id_isSet) {
        obj.insert(QString("location_id"), ::OpenAPI::toJsonValue(m_location_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_payment_id_isSet) {
        obj.insert(QString("payment_id"), ::OpenAPI::toJsonValue(m_payment_id));
    }
    if (m_percentage_isSet) {
        obj.insert(QString("percentage"), ::OpenAPI::toJsonValue(m_percentage));
    }
    if (m_total_amount_isSet) {
        obj.insert(QString("total_amount"), ::OpenAPI::toJsonValue(m_total_amount));
    }
    if (m_total_discount_isSet) {
        obj.insert(QString("total_discount"), ::OpenAPI::toJsonValue(m_total_discount));
    }
    if (m_total_processing_fee_isSet) {
        obj.insert(QString("total_processing_fee"), ::OpenAPI::toJsonValue(m_total_processing_fee));
    }
    if (m_total_refund_isSet) {
        obj.insert(QString("total_refund"), ::OpenAPI::toJsonValue(m_total_refund));
    }
    if (m_total_service_charge_isSet) {
        obj.insert(QString("total_service_charge"), ::OpenAPI::toJsonValue(m_total_service_charge));
    }
    if (m_total_tax_isSet) {
        obj.insert(QString("total_tax"), ::OpenAPI::toJsonValue(m_total_tax));
    }
    if (m_total_tip_isSet) {
        obj.insert(QString("total_tip"), ::OpenAPI::toJsonValue(m_total_tip));
    }
    if (m_transaction_id_isSet) {
        obj.insert(QString("transaction_id"), ::OpenAPI::toJsonValue(m_transaction_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

double OAIOrder_tenders_inner::getAmount() const {
    return m_amount;
}
void OAIOrder_tenders_inner::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIOrder_tenders_inner::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIOrder_tenders_inner::is_amount_Valid() const{
    return m_amount_isValid;
}

qint32 OAIOrder_tenders_inner::getBuyerTenderedCashAmount() const {
    return m_buyer_tendered_cash_amount;
}
void OAIOrder_tenders_inner::setBuyerTenderedCashAmount(const qint32 &buyer_tendered_cash_amount) {
    m_buyer_tendered_cash_amount = buyer_tendered_cash_amount;
    m_buyer_tendered_cash_amount_isSet = true;
}

bool OAIOrder_tenders_inner::is_buyer_tendered_cash_amount_Set() const{
    return m_buyer_tendered_cash_amount_isSet;
}

bool OAIOrder_tenders_inner::is_buyer_tendered_cash_amount_Valid() const{
    return m_buyer_tendered_cash_amount_isValid;
}

OAIPaymentCard OAIOrder_tenders_inner::getCard() const {
    return m_card;
}
void OAIOrder_tenders_inner::setCard(const OAIPaymentCard &card) {
    m_card = card;
    m_card_isSet = true;
}

bool OAIOrder_tenders_inner::is_card_Set() const{
    return m_card_isSet;
}

bool OAIOrder_tenders_inner::is_card_Valid() const{
    return m_card_isValid;
}

QString OAIOrder_tenders_inner::getCardEntryMethod() const {
    return m_card_entry_method;
}
void OAIOrder_tenders_inner::setCardEntryMethod(const QString &card_entry_method) {
    m_card_entry_method = card_entry_method;
    m_card_entry_method_isSet = true;
}

bool OAIOrder_tenders_inner::is_card_entry_method_Set() const{
    return m_card_entry_method_isSet;
}

bool OAIOrder_tenders_inner::is_card_entry_method_Valid() const{
    return m_card_entry_method_isValid;
}

QString OAIOrder_tenders_inner::getCardStatus() const {
    return m_card_status;
}
void OAIOrder_tenders_inner::setCardStatus(const QString &card_status) {
    m_card_status = card_status;
    m_card_status_isSet = true;
}

bool OAIOrder_tenders_inner::is_card_status_Set() const{
    return m_card_status_isSet;
}

bool OAIOrder_tenders_inner::is_card_status_Valid() const{
    return m_card_status_isValid;
}

qint32 OAIOrder_tenders_inner::getChangeBackCashAmount() const {
    return m_change_back_cash_amount;
}
void OAIOrder_tenders_inner::setChangeBackCashAmount(const qint32 &change_back_cash_amount) {
    m_change_back_cash_amount = change_back_cash_amount;
    m_change_back_cash_amount_isSet = true;
}

bool OAIOrder_tenders_inner::is_change_back_cash_amount_Set() const{
    return m_change_back_cash_amount_isSet;
}

bool OAIOrder_tenders_inner::is_change_back_cash_amount_Valid() const{
    return m_change_back_cash_amount_isValid;
}

OAICurrency OAIOrder_tenders_inner::getCurrency() const {
    return m_currency;
}
void OAIOrder_tenders_inner::setCurrency(const OAICurrency &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIOrder_tenders_inner::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIOrder_tenders_inner::is_currency_Valid() const{
    return m_currency_isValid;
}

QString OAIOrder_tenders_inner::getId() const {
    return m_id;
}
void OAIOrder_tenders_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOrder_tenders_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOrder_tenders_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIOrder_tenders_inner::getLocationId() const {
    return m_location_id;
}
void OAIOrder_tenders_inner::setLocationId(const QString &location_id) {
    m_location_id = location_id;
    m_location_id_isSet = true;
}

bool OAIOrder_tenders_inner::is_location_id_Set() const{
    return m_location_id_isSet;
}

bool OAIOrder_tenders_inner::is_location_id_Valid() const{
    return m_location_id_isValid;
}

QString OAIOrder_tenders_inner::getName() const {
    return m_name;
}
void OAIOrder_tenders_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIOrder_tenders_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIOrder_tenders_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIOrder_tenders_inner::getNote() const {
    return m_note;
}
void OAIOrder_tenders_inner::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAIOrder_tenders_inner::is_note_Set() const{
    return m_note_isSet;
}

bool OAIOrder_tenders_inner::is_note_Valid() const{
    return m_note_isValid;
}

QString OAIOrder_tenders_inner::getPaymentId() const {
    return m_payment_id;
}
void OAIOrder_tenders_inner::setPaymentId(const QString &payment_id) {
    m_payment_id = payment_id;
    m_payment_id_isSet = true;
}

bool OAIOrder_tenders_inner::is_payment_id_Set() const{
    return m_payment_id_isSet;
}

bool OAIOrder_tenders_inner::is_payment_id_Valid() const{
    return m_payment_id_isValid;
}

double OAIOrder_tenders_inner::getPercentage() const {
    return m_percentage;
}
void OAIOrder_tenders_inner::setPercentage(const double &percentage) {
    m_percentage = percentage;
    m_percentage_isSet = true;
}

bool OAIOrder_tenders_inner::is_percentage_Set() const{
    return m_percentage_isSet;
}

bool OAIOrder_tenders_inner::is_percentage_Valid() const{
    return m_percentage_isValid;
}

qint32 OAIOrder_tenders_inner::getTotalAmount() const {
    return m_total_amount;
}
void OAIOrder_tenders_inner::setTotalAmount(const qint32 &total_amount) {
    m_total_amount = total_amount;
    m_total_amount_isSet = true;
}

bool OAIOrder_tenders_inner::is_total_amount_Set() const{
    return m_total_amount_isSet;
}

bool OAIOrder_tenders_inner::is_total_amount_Valid() const{
    return m_total_amount_isValid;
}

qint32 OAIOrder_tenders_inner::getTotalDiscount() const {
    return m_total_discount;
}
void OAIOrder_tenders_inner::setTotalDiscount(const qint32 &total_discount) {
    m_total_discount = total_discount;
    m_total_discount_isSet = true;
}

bool OAIOrder_tenders_inner::is_total_discount_Set() const{
    return m_total_discount_isSet;
}

bool OAIOrder_tenders_inner::is_total_discount_Valid() const{
    return m_total_discount_isValid;
}

qint32 OAIOrder_tenders_inner::getTotalProcessingFee() const {
    return m_total_processing_fee;
}
void OAIOrder_tenders_inner::setTotalProcessingFee(const qint32 &total_processing_fee) {
    m_total_processing_fee = total_processing_fee;
    m_total_processing_fee_isSet = true;
}

bool OAIOrder_tenders_inner::is_total_processing_fee_Set() const{
    return m_total_processing_fee_isSet;
}

bool OAIOrder_tenders_inner::is_total_processing_fee_Valid() const{
    return m_total_processing_fee_isValid;
}

qint32 OAIOrder_tenders_inner::getTotalRefund() const {
    return m_total_refund;
}
void OAIOrder_tenders_inner::setTotalRefund(const qint32 &total_refund) {
    m_total_refund = total_refund;
    m_total_refund_isSet = true;
}

bool OAIOrder_tenders_inner::is_total_refund_Set() const{
    return m_total_refund_isSet;
}

bool OAIOrder_tenders_inner::is_total_refund_Valid() const{
    return m_total_refund_isValid;
}

qint32 OAIOrder_tenders_inner::getTotalServiceCharge() const {
    return m_total_service_charge;
}
void OAIOrder_tenders_inner::setTotalServiceCharge(const qint32 &total_service_charge) {
    m_total_service_charge = total_service_charge;
    m_total_service_charge_isSet = true;
}

bool OAIOrder_tenders_inner::is_total_service_charge_Set() const{
    return m_total_service_charge_isSet;
}

bool OAIOrder_tenders_inner::is_total_service_charge_Valid() const{
    return m_total_service_charge_isValid;
}

qint32 OAIOrder_tenders_inner::getTotalTax() const {
    return m_total_tax;
}
void OAIOrder_tenders_inner::setTotalTax(const qint32 &total_tax) {
    m_total_tax = total_tax;
    m_total_tax_isSet = true;
}

bool OAIOrder_tenders_inner::is_total_tax_Set() const{
    return m_total_tax_isSet;
}

bool OAIOrder_tenders_inner::is_total_tax_Valid() const{
    return m_total_tax_isValid;
}

qint32 OAIOrder_tenders_inner::getTotalTip() const {
    return m_total_tip;
}
void OAIOrder_tenders_inner::setTotalTip(const qint32 &total_tip) {
    m_total_tip = total_tip;
    m_total_tip_isSet = true;
}

bool OAIOrder_tenders_inner::is_total_tip_Set() const{
    return m_total_tip_isSet;
}

bool OAIOrder_tenders_inner::is_total_tip_Valid() const{
    return m_total_tip_isValid;
}

QString OAIOrder_tenders_inner::getTransactionId() const {
    return m_transaction_id;
}
void OAIOrder_tenders_inner::setTransactionId(const QString &transaction_id) {
    m_transaction_id = transaction_id;
    m_transaction_id_isSet = true;
}

bool OAIOrder_tenders_inner::is_transaction_id_Set() const{
    return m_transaction_id_isSet;
}

bool OAIOrder_tenders_inner::is_transaction_id_Valid() const{
    return m_transaction_id_isValid;
}

QString OAIOrder_tenders_inner::getType() const {
    return m_type;
}
void OAIOrder_tenders_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIOrder_tenders_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIOrder_tenders_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIOrder_tenders_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_buyer_tendered_cash_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_card.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_card_entry_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_card_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_change_back_cash_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_discount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_processing_fee_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_refund_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_service_charge_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_tip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrder_tenders_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
