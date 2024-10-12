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

#include "OAIPosPayment.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPosPayment::OAIPosPayment(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPosPayment::OAIPosPayment() {
    this->initializeModel();
}

OAIPosPayment::~OAIPosPayment() {}

void OAIPosPayment::initializeModel() {

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_app_fee_isSet = false;
    m_app_fee_isValid = false;

    m_approved_isSet = false;
    m_approved_isValid = false;

    m_bank_account_isSet = false;
    m_bank_account_isValid = false;

    m_card_details_isSet = false;
    m_card_details_isValid = false;

    m_cash_isSet = false;
    m_cash_isValid = false;

    m_change_back_cash_amount_isSet = false;
    m_change_back_cash_amount_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_custom_mappings_isSet = false;
    m_custom_mappings_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_device_id_isSet = false;
    m_device_id_isValid = false;

    m_employee_id_isSet = false;
    m_employee_id_isValid = false;

    m_external_details_isSet = false;
    m_external_details_isValid = false;

    m_external_payment_id_isSet = false;
    m_external_payment_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_idempotency_key_isSet = false;
    m_idempotency_key_isValid = false;

    m_location_id_isSet = false;
    m_location_id_isValid = false;

    m_merchant_id_isSet = false;
    m_merchant_id_isValid = false;

    m_order_id_isSet = false;
    m_order_id_isValid = false;

    m_processing_fees_isSet = false;
    m_processing_fees_isValid = false;

    m_refunded_isSet = false;
    m_refunded_isValid = false;

    m_service_charges_isSet = false;
    m_service_charges_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_source_id_isSet = false;
    m_source_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_tax_isSet = false;
    m_tax_isValid = false;

    m_tender_id_isSet = false;
    m_tender_id_isValid = false;

    m_tip_isSet = false;
    m_tip_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;

    m_wallet_isSet = false;
    m_wallet_isValid = false;
}

void OAIPosPayment::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPosPayment::fromJsonObject(QJsonObject json) {

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_app_fee_isValid = ::OpenAPI::fromJsonValue(m_app_fee, json[QString("app_fee")]);
    m_app_fee_isSet = !json[QString("app_fee")].isNull() && m_app_fee_isValid;

    m_approved_isValid = ::OpenAPI::fromJsonValue(m_approved, json[QString("approved")]);
    m_approved_isSet = !json[QString("approved")].isNull() && m_approved_isValid;

    m_bank_account_isValid = ::OpenAPI::fromJsonValue(m_bank_account, json[QString("bank_account")]);
    m_bank_account_isSet = !json[QString("bank_account")].isNull() && m_bank_account_isValid;

    m_card_details_isValid = ::OpenAPI::fromJsonValue(m_card_details, json[QString("card_details")]);
    m_card_details_isSet = !json[QString("card_details")].isNull() && m_card_details_isValid;

    m_cash_isValid = ::OpenAPI::fromJsonValue(m_cash, json[QString("cash")]);
    m_cash_isSet = !json[QString("cash")].isNull() && m_cash_isValid;

    m_change_back_cash_amount_isValid = ::OpenAPI::fromJsonValue(m_change_back_cash_amount, json[QString("change_back_cash_amount")]);
    m_change_back_cash_amount_isSet = !json[QString("change_back_cash_amount")].isNull() && m_change_back_cash_amount_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_custom_mappings_isValid = ::OpenAPI::fromJsonValue(m_custom_mappings, json[QString("custom_mappings")]);
    m_custom_mappings_isSet = !json[QString("custom_mappings")].isNull() && m_custom_mappings_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customer_id")]);
    m_customer_id_isSet = !json[QString("customer_id")].isNull() && m_customer_id_isValid;

    m_device_id_isValid = ::OpenAPI::fromJsonValue(m_device_id, json[QString("device_id")]);
    m_device_id_isSet = !json[QString("device_id")].isNull() && m_device_id_isValid;

    m_employee_id_isValid = ::OpenAPI::fromJsonValue(m_employee_id, json[QString("employee_id")]);
    m_employee_id_isSet = !json[QString("employee_id")].isNull() && m_employee_id_isValid;

    m_external_details_isValid = ::OpenAPI::fromJsonValue(m_external_details, json[QString("external_details")]);
    m_external_details_isSet = !json[QString("external_details")].isNull() && m_external_details_isValid;

    m_external_payment_id_isValid = ::OpenAPI::fromJsonValue(m_external_payment_id, json[QString("external_payment_id")]);
    m_external_payment_id_isSet = !json[QString("external_payment_id")].isNull() && m_external_payment_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_idempotency_key_isValid = ::OpenAPI::fromJsonValue(m_idempotency_key, json[QString("idempotency_key")]);
    m_idempotency_key_isSet = !json[QString("idempotency_key")].isNull() && m_idempotency_key_isValid;

    m_location_id_isValid = ::OpenAPI::fromJsonValue(m_location_id, json[QString("location_id")]);
    m_location_id_isSet = !json[QString("location_id")].isNull() && m_location_id_isValid;

    m_merchant_id_isValid = ::OpenAPI::fromJsonValue(m_merchant_id, json[QString("merchant_id")]);
    m_merchant_id_isSet = !json[QString("merchant_id")].isNull() && m_merchant_id_isValid;

    m_order_id_isValid = ::OpenAPI::fromJsonValue(m_order_id, json[QString("order_id")]);
    m_order_id_isSet = !json[QString("order_id")].isNull() && m_order_id_isValid;

    m_processing_fees_isValid = ::OpenAPI::fromJsonValue(m_processing_fees, json[QString("processing_fees")]);
    m_processing_fees_isSet = !json[QString("processing_fees")].isNull() && m_processing_fees_isValid;

    m_refunded_isValid = ::OpenAPI::fromJsonValue(m_refunded, json[QString("refunded")]);
    m_refunded_isSet = !json[QString("refunded")].isNull() && m_refunded_isValid;

    m_service_charges_isValid = ::OpenAPI::fromJsonValue(m_service_charges, json[QString("service_charges")]);
    m_service_charges_isSet = !json[QString("service_charges")].isNull() && m_service_charges_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_source_id_isValid = ::OpenAPI::fromJsonValue(m_source_id, json[QString("source_id")]);
    m_source_id_isSet = !json[QString("source_id")].isNull() && m_source_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_tax_isValid = ::OpenAPI::fromJsonValue(m_tax, json[QString("tax")]);
    m_tax_isSet = !json[QString("tax")].isNull() && m_tax_isValid;

    m_tender_id_isValid = ::OpenAPI::fromJsonValue(m_tender_id, json[QString("tender_id")]);
    m_tender_id_isSet = !json[QString("tender_id")].isNull() && m_tender_id_isValid;

    m_tip_isValid = ::OpenAPI::fromJsonValue(m_tip, json[QString("tip")]);
    m_tip_isSet = !json[QString("tip")].isNull() && m_tip_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updated_by")]);
    m_updated_by_isSet = !json[QString("updated_by")].isNull() && m_updated_by_isValid;

    m_wallet_isValid = ::OpenAPI::fromJsonValue(m_wallet, json[QString("wallet")]);
    m_wallet_isSet = !json[QString("wallet")].isNull() && m_wallet_isValid;
}

QString OAIPosPayment::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPosPayment::asJsonObject() const {
    QJsonObject obj;
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_app_fee_isSet) {
        obj.insert(QString("app_fee"), ::OpenAPI::toJsonValue(m_app_fee));
    }
    if (m_approved_isSet) {
        obj.insert(QString("approved"), ::OpenAPI::toJsonValue(m_approved));
    }
    if (m_bank_account.isSet()) {
        obj.insert(QString("bank_account"), ::OpenAPI::toJsonValue(m_bank_account));
    }
    if (m_card_details.isSet()) {
        obj.insert(QString("card_details"), ::OpenAPI::toJsonValue(m_card_details));
    }
    if (m_cash.isSet()) {
        obj.insert(QString("cash"), ::OpenAPI::toJsonValue(m_cash));
    }
    if (m_change_back_cash_amount_isSet) {
        obj.insert(QString("change_back_cash_amount"), ::OpenAPI::toJsonValue(m_change_back_cash_amount));
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
    if (m_customer_id_isSet) {
        obj.insert(QString("customer_id"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_device_id_isSet) {
        obj.insert(QString("device_id"), ::OpenAPI::toJsonValue(m_device_id));
    }
    if (m_employee_id_isSet) {
        obj.insert(QString("employee_id"), ::OpenAPI::toJsonValue(m_employee_id));
    }
    if (m_external_details.isSet()) {
        obj.insert(QString("external_details"), ::OpenAPI::toJsonValue(m_external_details));
    }
    if (m_external_payment_id_isSet) {
        obj.insert(QString("external_payment_id"), ::OpenAPI::toJsonValue(m_external_payment_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_idempotency_key_isSet) {
        obj.insert(QString("idempotency_key"), ::OpenAPI::toJsonValue(m_idempotency_key));
    }
    if (m_location_id_isSet) {
        obj.insert(QString("location_id"), ::OpenAPI::toJsonValue(m_location_id));
    }
    if (m_merchant_id_isSet) {
        obj.insert(QString("merchant_id"), ::OpenAPI::toJsonValue(m_merchant_id));
    }
    if (m_order_id_isSet) {
        obj.insert(QString("order_id"), ::OpenAPI::toJsonValue(m_order_id));
    }
    if (m_processing_fees.size() > 0) {
        obj.insert(QString("processing_fees"), ::OpenAPI::toJsonValue(m_processing_fees));
    }
    if (m_refunded_isSet) {
        obj.insert(QString("refunded"), ::OpenAPI::toJsonValue(m_refunded));
    }
    if (m_service_charges.size() > 0) {
        obj.insert(QString("service_charges"), ::OpenAPI::toJsonValue(m_service_charges));
    }
    if (m_source_isSet) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_source_id_isSet) {
        obj.insert(QString("source_id"), ::OpenAPI::toJsonValue(m_source_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_tax_isSet) {
        obj.insert(QString("tax"), ::OpenAPI::toJsonValue(m_tax));
    }
    if (m_tender_id_isSet) {
        obj.insert(QString("tender_id"), ::OpenAPI::toJsonValue(m_tender_id));
    }
    if (m_tip_isSet) {
        obj.insert(QString("tip"), ::OpenAPI::toJsonValue(m_tip));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_updated_by_isSet) {
        obj.insert(QString("updated_by"), ::OpenAPI::toJsonValue(m_updated_by));
    }
    if (m_wallet.isSet()) {
        obj.insert(QString("wallet"), ::OpenAPI::toJsonValue(m_wallet));
    }
    return obj;
}

double OAIPosPayment::getAmount() const {
    return m_amount;
}
void OAIPosPayment::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIPosPayment::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIPosPayment::is_amount_Valid() const{
    return m_amount_isValid;
}

double OAIPosPayment::getAppFee() const {
    return m_app_fee;
}
void OAIPosPayment::setAppFee(const double &app_fee) {
    m_app_fee = app_fee;
    m_app_fee_isSet = true;
}

bool OAIPosPayment::is_app_fee_Set() const{
    return m_app_fee_isSet;
}

bool OAIPosPayment::is_app_fee_Valid() const{
    return m_app_fee_isValid;
}

double OAIPosPayment::getApproved() const {
    return m_approved;
}
void OAIPosPayment::setApproved(const double &approved) {
    m_approved = approved;
    m_approved_isSet = true;
}

bool OAIPosPayment::is_approved_Set() const{
    return m_approved_isSet;
}

bool OAIPosPayment::is_approved_Valid() const{
    return m_approved_isValid;
}

OAIPosBankAccount OAIPosPayment::getBankAccount() const {
    return m_bank_account;
}
void OAIPosPayment::setBankAccount(const OAIPosBankAccount &bank_account) {
    m_bank_account = bank_account;
    m_bank_account_isSet = true;
}

bool OAIPosPayment::is_bank_account_Set() const{
    return m_bank_account_isSet;
}

bool OAIPosPayment::is_bank_account_Valid() const{
    return m_bank_account_isValid;
}

OAIPosPayment_card_details OAIPosPayment::getCardDetails() const {
    return m_card_details;
}
void OAIPosPayment::setCardDetails(const OAIPosPayment_card_details &card_details) {
    m_card_details = card_details;
    m_card_details_isSet = true;
}

bool OAIPosPayment::is_card_details_Set() const{
    return m_card_details_isSet;
}

bool OAIPosPayment::is_card_details_Valid() const{
    return m_card_details_isValid;
}

OAICash_details OAIPosPayment::getCash() const {
    return m_cash;
}
void OAIPosPayment::setCash(const OAICash_details &cash) {
    m_cash = cash;
    m_cash_isSet = true;
}

bool OAIPosPayment::is_cash_Set() const{
    return m_cash_isSet;
}

bool OAIPosPayment::is_cash_Valid() const{
    return m_cash_isValid;
}

double OAIPosPayment::getChangeBackCashAmount() const {
    return m_change_back_cash_amount;
}
void OAIPosPayment::setChangeBackCashAmount(const double &change_back_cash_amount) {
    m_change_back_cash_amount = change_back_cash_amount;
    m_change_back_cash_amount_isSet = true;
}

bool OAIPosPayment::is_change_back_cash_amount_Set() const{
    return m_change_back_cash_amount_isSet;
}

bool OAIPosPayment::is_change_back_cash_amount_Valid() const{
    return m_change_back_cash_amount_isValid;
}

QDateTime OAIPosPayment::getCreatedAt() const {
    return m_created_at;
}
void OAIPosPayment::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIPosPayment::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIPosPayment::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIPosPayment::getCreatedBy() const {
    return m_created_by;
}
void OAIPosPayment::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIPosPayment::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIPosPayment::is_created_by_Valid() const{
    return m_created_by_isValid;
}

OAICurrency OAIPosPayment::getCurrency() const {
    return m_currency;
}
void OAIPosPayment::setCurrency(const OAICurrency &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIPosPayment::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIPosPayment::is_currency_Valid() const{
    return m_currency_isValid;
}

OAIObject OAIPosPayment::getCustomMappings() const {
    return m_custom_mappings;
}
void OAIPosPayment::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAIPosPayment::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAIPosPayment::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

QString OAIPosPayment::getCustomerId() const {
    return m_customer_id;
}
void OAIPosPayment::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAIPosPayment::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAIPosPayment::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

QString OAIPosPayment::getDeviceId() const {
    return m_device_id;
}
void OAIPosPayment::setDeviceId(const QString &device_id) {
    m_device_id = device_id;
    m_device_id_isSet = true;
}

bool OAIPosPayment::is_device_id_Set() const{
    return m_device_id_isSet;
}

bool OAIPosPayment::is_device_id_Valid() const{
    return m_device_id_isValid;
}

QString OAIPosPayment::getEmployeeId() const {
    return m_employee_id;
}
void OAIPosPayment::setEmployeeId(const QString &employee_id) {
    m_employee_id = employee_id;
    m_employee_id_isSet = true;
}

bool OAIPosPayment::is_employee_id_Set() const{
    return m_employee_id_isSet;
}

bool OAIPosPayment::is_employee_id_Valid() const{
    return m_employee_id_isValid;
}

OAIPosPayment_external_details OAIPosPayment::getExternalDetails() const {
    return m_external_details;
}
void OAIPosPayment::setExternalDetails(const OAIPosPayment_external_details &external_details) {
    m_external_details = external_details;
    m_external_details_isSet = true;
}

bool OAIPosPayment::is_external_details_Set() const{
    return m_external_details_isSet;
}

bool OAIPosPayment::is_external_details_Valid() const{
    return m_external_details_isValid;
}

QString OAIPosPayment::getExternalPaymentId() const {
    return m_external_payment_id;
}
void OAIPosPayment::setExternalPaymentId(const QString &external_payment_id) {
    m_external_payment_id = external_payment_id;
    m_external_payment_id_isSet = true;
}

bool OAIPosPayment::is_external_payment_id_Set() const{
    return m_external_payment_id_isSet;
}

bool OAIPosPayment::is_external_payment_id_Valid() const{
    return m_external_payment_id_isValid;
}

QString OAIPosPayment::getId() const {
    return m_id;
}
void OAIPosPayment::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPosPayment::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPosPayment::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPosPayment::getIdempotencyKey() const {
    return m_idempotency_key;
}
void OAIPosPayment::setIdempotencyKey(const QString &idempotency_key) {
    m_idempotency_key = idempotency_key;
    m_idempotency_key_isSet = true;
}

bool OAIPosPayment::is_idempotency_key_Set() const{
    return m_idempotency_key_isSet;
}

bool OAIPosPayment::is_idempotency_key_Valid() const{
    return m_idempotency_key_isValid;
}

QString OAIPosPayment::getLocationId() const {
    return m_location_id;
}
void OAIPosPayment::setLocationId(const QString &location_id) {
    m_location_id = location_id;
    m_location_id_isSet = true;
}

bool OAIPosPayment::is_location_id_Set() const{
    return m_location_id_isSet;
}

bool OAIPosPayment::is_location_id_Valid() const{
    return m_location_id_isValid;
}

QString OAIPosPayment::getMerchantId() const {
    return m_merchant_id;
}
void OAIPosPayment::setMerchantId(const QString &merchant_id) {
    m_merchant_id = merchant_id;
    m_merchant_id_isSet = true;
}

bool OAIPosPayment::is_merchant_id_Set() const{
    return m_merchant_id_isSet;
}

bool OAIPosPayment::is_merchant_id_Valid() const{
    return m_merchant_id_isValid;
}

QString OAIPosPayment::getOrderId() const {
    return m_order_id;
}
void OAIPosPayment::setOrderId(const QString &order_id) {
    m_order_id = order_id;
    m_order_id_isSet = true;
}

bool OAIPosPayment::is_order_id_Set() const{
    return m_order_id_isSet;
}

bool OAIPosPayment::is_order_id_Valid() const{
    return m_order_id_isValid;
}

QList<OAIPosPayment_processing_fees_inner> OAIPosPayment::getProcessingFees() const {
    return m_processing_fees;
}
void OAIPosPayment::setProcessingFees(const QList<OAIPosPayment_processing_fees_inner> &processing_fees) {
    m_processing_fees = processing_fees;
    m_processing_fees_isSet = true;
}

bool OAIPosPayment::is_processing_fees_Set() const{
    return m_processing_fees_isSet;
}

bool OAIPosPayment::is_processing_fees_Valid() const{
    return m_processing_fees_isValid;
}

double OAIPosPayment::getRefunded() const {
    return m_refunded;
}
void OAIPosPayment::setRefunded(const double &refunded) {
    m_refunded = refunded;
    m_refunded_isSet = true;
}

bool OAIPosPayment::is_refunded_Set() const{
    return m_refunded_isSet;
}

bool OAIPosPayment::is_refunded_Valid() const{
    return m_refunded_isValid;
}

QList<OAIServiceCharge> OAIPosPayment::getServiceCharges() const {
    return m_service_charges;
}
void OAIPosPayment::setServiceCharges(const QList<OAIServiceCharge> &service_charges) {
    m_service_charges = service_charges;
    m_service_charges_isSet = true;
}

bool OAIPosPayment::is_service_charges_Set() const{
    return m_service_charges_isSet;
}

bool OAIPosPayment::is_service_charges_Valid() const{
    return m_service_charges_isValid;
}

QString OAIPosPayment::getSource() const {
    return m_source;
}
void OAIPosPayment::setSource(const QString &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIPosPayment::is_source_Set() const{
    return m_source_isSet;
}

bool OAIPosPayment::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIPosPayment::getSourceId() const {
    return m_source_id;
}
void OAIPosPayment::setSourceId(const QString &source_id) {
    m_source_id = source_id;
    m_source_id_isSet = true;
}

bool OAIPosPayment::is_source_id_Set() const{
    return m_source_id_isSet;
}

bool OAIPosPayment::is_source_id_Valid() const{
    return m_source_id_isValid;
}

QString OAIPosPayment::getStatus() const {
    return m_status;
}
void OAIPosPayment::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIPosPayment::is_status_Set() const{
    return m_status_isSet;
}

bool OAIPosPayment::is_status_Valid() const{
    return m_status_isValid;
}

double OAIPosPayment::getTax() const {
    return m_tax;
}
void OAIPosPayment::setTax(const double &tax) {
    m_tax = tax;
    m_tax_isSet = true;
}

bool OAIPosPayment::is_tax_Set() const{
    return m_tax_isSet;
}

bool OAIPosPayment::is_tax_Valid() const{
    return m_tax_isValid;
}

QString OAIPosPayment::getTenderId() const {
    return m_tender_id;
}
void OAIPosPayment::setTenderId(const QString &tender_id) {
    m_tender_id = tender_id;
    m_tender_id_isSet = true;
}

bool OAIPosPayment::is_tender_id_Set() const{
    return m_tender_id_isSet;
}

bool OAIPosPayment::is_tender_id_Valid() const{
    return m_tender_id_isValid;
}

double OAIPosPayment::getTip() const {
    return m_tip;
}
void OAIPosPayment::setTip(const double &tip) {
    m_tip = tip;
    m_tip_isSet = true;
}

bool OAIPosPayment::is_tip_Set() const{
    return m_tip_isSet;
}

bool OAIPosPayment::is_tip_Valid() const{
    return m_tip_isValid;
}

double OAIPosPayment::getTotal() const {
    return m_total;
}
void OAIPosPayment::setTotal(const double &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIPosPayment::is_total_Set() const{
    return m_total_isSet;
}

bool OAIPosPayment::is_total_Valid() const{
    return m_total_isValid;
}

QDateTime OAIPosPayment::getUpdatedAt() const {
    return m_updated_at;
}
void OAIPosPayment::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIPosPayment::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIPosPayment::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIPosPayment::getUpdatedBy() const {
    return m_updated_by;
}
void OAIPosPayment::setUpdatedBy(const QString &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAIPosPayment::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAIPosPayment::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

OAIWallet_details OAIPosPayment::getWallet() const {
    return m_wallet;
}
void OAIPosPayment::setWallet(const OAIWallet_details &wallet) {
    m_wallet = wallet;
    m_wallet_isSet = true;
}

bool OAIPosPayment::is_wallet_Set() const{
    return m_wallet_isSet;
}

bool OAIPosPayment::is_wallet_Valid() const{
    return m_wallet_isValid;
}

bool OAIPosPayment::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_app_fee_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_approved_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bank_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_card_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cash.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_change_back_cash_amount_isSet) {
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

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_device_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employee_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_payment_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_idempotency_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merchant_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_processing_fees.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_refunded_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_service_charges.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tender_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
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

        if (m_wallet.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPosPayment::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_amount_isValid && m_currency_isValid && m_customer_id_isValid && m_order_id_isValid && m_source_id_isValid && m_tender_id_isValid && true;
}

} // namespace OpenAPI
