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

#include "OAIPaymentCard.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPaymentCard::OAIPaymentCard(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPaymentCard::OAIPaymentCard() {
    this->initializeModel();
}

OAIPaymentCard::~OAIPaymentCard() {}

void OAIPaymentCard::initializeModel() {

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_bin_isSet = false;
    m_bin_isValid = false;

    m_card_brand_isSet = false;
    m_card_brand_isValid = false;

    m_card_type_isSet = false;
    m_card_type_isValid = false;

    m_cardholder_name_isSet = false;
    m_cardholder_name_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_exp_month_isSet = false;
    m_exp_month_isValid = false;

    m_exp_year_isSet = false;
    m_exp_year_isValid = false;

    m_fingerprint_isSet = false;
    m_fingerprint_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_4_isSet = false;
    m_last_4_isValid = false;

    m_merchant_id_isSet = false;
    m_merchant_id_isValid = false;

    m_prepaid_type_isSet = false;
    m_prepaid_type_isValid = false;

    m_reference_id_isSet = false;
    m_reference_id_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIPaymentCard::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPaymentCard::fromJsonObject(QJsonObject json) {

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billing_address")]);
    m_billing_address_isSet = !json[QString("billing_address")].isNull() && m_billing_address_isValid;

    m_bin_isValid = ::OpenAPI::fromJsonValue(m_bin, json[QString("bin")]);
    m_bin_isSet = !json[QString("bin")].isNull() && m_bin_isValid;

    m_card_brand_isValid = ::OpenAPI::fromJsonValue(m_card_brand, json[QString("card_brand")]);
    m_card_brand_isSet = !json[QString("card_brand")].isNull() && m_card_brand_isValid;

    m_card_type_isValid = ::OpenAPI::fromJsonValue(m_card_type, json[QString("card_type")]);
    m_card_type_isSet = !json[QString("card_type")].isNull() && m_card_type_isValid;

    m_cardholder_name_isValid = ::OpenAPI::fromJsonValue(m_cardholder_name, json[QString("cardholder_name")]);
    m_cardholder_name_isSet = !json[QString("cardholder_name")].isNull() && m_cardholder_name_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customer_id")]);
    m_customer_id_isSet = !json[QString("customer_id")].isNull() && m_customer_id_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_exp_month_isValid = ::OpenAPI::fromJsonValue(m_exp_month, json[QString("exp_month")]);
    m_exp_month_isSet = !json[QString("exp_month")].isNull() && m_exp_month_isValid;

    m_exp_year_isValid = ::OpenAPI::fromJsonValue(m_exp_year, json[QString("exp_year")]);
    m_exp_year_isSet = !json[QString("exp_year")].isNull() && m_exp_year_isValid;

    m_fingerprint_isValid = ::OpenAPI::fromJsonValue(m_fingerprint, json[QString("fingerprint")]);
    m_fingerprint_isSet = !json[QString("fingerprint")].isNull() && m_fingerprint_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_4_isValid = ::OpenAPI::fromJsonValue(m_last_4, json[QString("last_4")]);
    m_last_4_isSet = !json[QString("last_4")].isNull() && m_last_4_isValid;

    m_merchant_id_isValid = ::OpenAPI::fromJsonValue(m_merchant_id, json[QString("merchant_id")]);
    m_merchant_id_isSet = !json[QString("merchant_id")].isNull() && m_merchant_id_isValid;

    m_prepaid_type_isValid = ::OpenAPI::fromJsonValue(m_prepaid_type, json[QString("prepaid_type")]);
    m_prepaid_type_isSet = !json[QString("prepaid_type")].isNull() && m_prepaid_type_isValid;

    m_reference_id_isValid = ::OpenAPI::fromJsonValue(m_reference_id, json[QString("reference_id")]);
    m_reference_id_isSet = !json[QString("reference_id")].isNull() && m_reference_id_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIPaymentCard::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPaymentCard::asJsonObject() const {
    QJsonObject obj;
    if (m_billing_address.isSet()) {
        obj.insert(QString("billing_address"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_bin_isSet) {
        obj.insert(QString("bin"), ::OpenAPI::toJsonValue(m_bin));
    }
    if (m_card_brand_isSet) {
        obj.insert(QString("card_brand"), ::OpenAPI::toJsonValue(m_card_brand));
    }
    if (m_card_type_isSet) {
        obj.insert(QString("card_type"), ::OpenAPI::toJsonValue(m_card_type));
    }
    if (m_cardholder_name_isSet) {
        obj.insert(QString("cardholder_name"), ::OpenAPI::toJsonValue(m_cardholder_name));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customer_id"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_exp_month_isSet) {
        obj.insert(QString("exp_month"), ::OpenAPI::toJsonValue(m_exp_month));
    }
    if (m_exp_year_isSet) {
        obj.insert(QString("exp_year"), ::OpenAPI::toJsonValue(m_exp_year));
    }
    if (m_fingerprint_isSet) {
        obj.insert(QString("fingerprint"), ::OpenAPI::toJsonValue(m_fingerprint));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_4_isSet) {
        obj.insert(QString("last_4"), ::OpenAPI::toJsonValue(m_last_4));
    }
    if (m_merchant_id_isSet) {
        obj.insert(QString("merchant_id"), ::OpenAPI::toJsonValue(m_merchant_id));
    }
    if (m_prepaid_type_isSet) {
        obj.insert(QString("prepaid_type"), ::OpenAPI::toJsonValue(m_prepaid_type));
    }
    if (m_reference_id_isSet) {
        obj.insert(QString("reference_id"), ::OpenAPI::toJsonValue(m_reference_id));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

OAIAddress OAIPaymentCard::getBillingAddress() const {
    return m_billing_address;
}
void OAIPaymentCard::setBillingAddress(const OAIAddress &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAIPaymentCard::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAIPaymentCard::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAIPaymentCard::getBin() const {
    return m_bin;
}
void OAIPaymentCard::setBin(const QString &bin) {
    m_bin = bin;
    m_bin_isSet = true;
}

bool OAIPaymentCard::is_bin_Set() const{
    return m_bin_isSet;
}

bool OAIPaymentCard::is_bin_Valid() const{
    return m_bin_isValid;
}

QString OAIPaymentCard::getCardBrand() const {
    return m_card_brand;
}
void OAIPaymentCard::setCardBrand(const QString &card_brand) {
    m_card_brand = card_brand;
    m_card_brand_isSet = true;
}

bool OAIPaymentCard::is_card_brand_Set() const{
    return m_card_brand_isSet;
}

bool OAIPaymentCard::is_card_brand_Valid() const{
    return m_card_brand_isValid;
}

QString OAIPaymentCard::getCardType() const {
    return m_card_type;
}
void OAIPaymentCard::setCardType(const QString &card_type) {
    m_card_type = card_type;
    m_card_type_isSet = true;
}

bool OAIPaymentCard::is_card_type_Set() const{
    return m_card_type_isSet;
}

bool OAIPaymentCard::is_card_type_Valid() const{
    return m_card_type_isValid;
}

QString OAIPaymentCard::getCardholderName() const {
    return m_cardholder_name;
}
void OAIPaymentCard::setCardholderName(const QString &cardholder_name) {
    m_cardholder_name = cardholder_name;
    m_cardholder_name_isSet = true;
}

bool OAIPaymentCard::is_cardholder_name_Set() const{
    return m_cardholder_name_isSet;
}

bool OAIPaymentCard::is_cardholder_name_Valid() const{
    return m_cardholder_name_isValid;
}

QString OAIPaymentCard::getCustomerId() const {
    return m_customer_id;
}
void OAIPaymentCard::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAIPaymentCard::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAIPaymentCard::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

bool OAIPaymentCard::isEnabled() const {
    return m_enabled;
}
void OAIPaymentCard::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIPaymentCard::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIPaymentCard::is_enabled_Valid() const{
    return m_enabled_isValid;
}

qint32 OAIPaymentCard::getExpMonth() const {
    return m_exp_month;
}
void OAIPaymentCard::setExpMonth(const qint32 &exp_month) {
    m_exp_month = exp_month;
    m_exp_month_isSet = true;
}

bool OAIPaymentCard::is_exp_month_Set() const{
    return m_exp_month_isSet;
}

bool OAIPaymentCard::is_exp_month_Valid() const{
    return m_exp_month_isValid;
}

qint32 OAIPaymentCard::getExpYear() const {
    return m_exp_year;
}
void OAIPaymentCard::setExpYear(const qint32 &exp_year) {
    m_exp_year = exp_year;
    m_exp_year_isSet = true;
}

bool OAIPaymentCard::is_exp_year_Set() const{
    return m_exp_year_isSet;
}

bool OAIPaymentCard::is_exp_year_Valid() const{
    return m_exp_year_isValid;
}

QString OAIPaymentCard::getFingerprint() const {
    return m_fingerprint;
}
void OAIPaymentCard::setFingerprint(const QString &fingerprint) {
    m_fingerprint = fingerprint;
    m_fingerprint_isSet = true;
}

bool OAIPaymentCard::is_fingerprint_Set() const{
    return m_fingerprint_isSet;
}

bool OAIPaymentCard::is_fingerprint_Valid() const{
    return m_fingerprint_isValid;
}

QString OAIPaymentCard::getId() const {
    return m_id;
}
void OAIPaymentCard::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPaymentCard::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPaymentCard::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPaymentCard::getLast4() const {
    return m_last_4;
}
void OAIPaymentCard::setLast4(const QString &last_4) {
    m_last_4 = last_4;
    m_last_4_isSet = true;
}

bool OAIPaymentCard::is_last_4_Set() const{
    return m_last_4_isSet;
}

bool OAIPaymentCard::is_last_4_Valid() const{
    return m_last_4_isValid;
}

QString OAIPaymentCard::getMerchantId() const {
    return m_merchant_id;
}
void OAIPaymentCard::setMerchantId(const QString &merchant_id) {
    m_merchant_id = merchant_id;
    m_merchant_id_isSet = true;
}

bool OAIPaymentCard::is_merchant_id_Set() const{
    return m_merchant_id_isSet;
}

bool OAIPaymentCard::is_merchant_id_Valid() const{
    return m_merchant_id_isValid;
}

QString OAIPaymentCard::getPrepaidType() const {
    return m_prepaid_type;
}
void OAIPaymentCard::setPrepaidType(const QString &prepaid_type) {
    m_prepaid_type = prepaid_type;
    m_prepaid_type_isSet = true;
}

bool OAIPaymentCard::is_prepaid_type_Set() const{
    return m_prepaid_type_isSet;
}

bool OAIPaymentCard::is_prepaid_type_Valid() const{
    return m_prepaid_type_isValid;
}

QString OAIPaymentCard::getReferenceId() const {
    return m_reference_id;
}
void OAIPaymentCard::setReferenceId(const QString &reference_id) {
    m_reference_id = reference_id;
    m_reference_id_isSet = true;
}

bool OAIPaymentCard::is_reference_id_Set() const{
    return m_reference_id_isSet;
}

bool OAIPaymentCard::is_reference_id_Valid() const{
    return m_reference_id_isValid;
}

QString OAIPaymentCard::getVersion() const {
    return m_version;
}
void OAIPaymentCard::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIPaymentCard::is_version_Set() const{
    return m_version_isSet;
}

bool OAIPaymentCard::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIPaymentCard::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_bin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_card_brand_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_card_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cardholder_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exp_month_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exp_year_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fingerprint_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_4_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merchant_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_prepaid_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPaymentCard::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
