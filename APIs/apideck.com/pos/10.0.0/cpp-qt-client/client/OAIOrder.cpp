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

#include "OAIOrder.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrder::OAIOrder(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrder::OAIOrder() {
    this->initializeModel();
}

OAIOrder::~OAIOrder() {}

void OAIOrder::initializeModel() {

    m_closed_date_isSet = false;
    m_closed_date_isValid = false;

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

    m_customers_isSet = false;
    m_customers_isValid = false;

    m_discounts_isSet = false;
    m_discounts_isValid = false;

    m_employee_id_isSet = false;
    m_employee_id_isValid = false;

    m_fulfillments_isSet = false;
    m_fulfillments_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_idempotency_key_isSet = false;
    m_idempotency_key_isValid = false;

    m_line_items_isSet = false;
    m_line_items_isValid = false;

    m_location_id_isSet = false;
    m_location_id_isValid = false;

    m_merchant_id_isSet = false;
    m_merchant_id_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_order_date_isSet = false;
    m_order_date_isValid = false;

    m_order_number_isSet = false;
    m_order_number_isValid = false;

    m_order_type_id_isSet = false;
    m_order_type_id_isValid = false;

    m_payment_status_isSet = false;
    m_payment_status_isValid = false;

    m_payments_isSet = false;
    m_payments_isValid = false;

    m_reference_id_isSet = false;
    m_reference_id_isValid = false;

    m_refunded_isSet = false;
    m_refunded_isValid = false;

    m_refunds_isSet = false;
    m_refunds_isValid = false;

    m_seat_isSet = false;
    m_seat_isValid = false;

    m_service_charges_isSet = false;
    m_service_charges_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_table_isSet = false;
    m_table_isValid = false;

    m_taxes_isSet = false;
    m_taxes_isValid = false;

    m_tenders_isSet = false;
    m_tenders_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_total_amount_isSet = false;
    m_total_amount_isValid = false;

    m_total_discount_isSet = false;
    m_total_discount_isValid = false;

    m_total_refund_isSet = false;
    m_total_refund_isValid = false;

    m_total_service_charge_isSet = false;
    m_total_service_charge_isValid = false;

    m_total_tax_isSet = false;
    m_total_tax_isValid = false;

    m_total_tip_isSet = false;
    m_total_tip_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;

    m_voided_isSet = false;
    m_voided_isValid = false;

    m_voided_at_isSet = false;
    m_voided_at_isValid = false;
}

void OAIOrder::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrder::fromJsonObject(QJsonObject json) {

    m_closed_date_isValid = ::OpenAPI::fromJsonValue(m_closed_date, json[QString("closed_date")]);
    m_closed_date_isSet = !json[QString("closed_date")].isNull() && m_closed_date_isValid;

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

    m_customers_isValid = ::OpenAPI::fromJsonValue(m_customers, json[QString("customers")]);
    m_customers_isSet = !json[QString("customers")].isNull() && m_customers_isValid;

    m_discounts_isValid = ::OpenAPI::fromJsonValue(m_discounts, json[QString("discounts")]);
    m_discounts_isSet = !json[QString("discounts")].isNull() && m_discounts_isValid;

    m_employee_id_isValid = ::OpenAPI::fromJsonValue(m_employee_id, json[QString("employee_id")]);
    m_employee_id_isSet = !json[QString("employee_id")].isNull() && m_employee_id_isValid;

    m_fulfillments_isValid = ::OpenAPI::fromJsonValue(m_fulfillments, json[QString("fulfillments")]);
    m_fulfillments_isSet = !json[QString("fulfillments")].isNull() && m_fulfillments_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_idempotency_key_isValid = ::OpenAPI::fromJsonValue(m_idempotency_key, json[QString("idempotency_key")]);
    m_idempotency_key_isSet = !json[QString("idempotency_key")].isNull() && m_idempotency_key_isValid;

    m_line_items_isValid = ::OpenAPI::fromJsonValue(m_line_items, json[QString("line_items")]);
    m_line_items_isSet = !json[QString("line_items")].isNull() && m_line_items_isValid;

    m_location_id_isValid = ::OpenAPI::fromJsonValue(m_location_id, json[QString("location_id")]);
    m_location_id_isSet = !json[QString("location_id")].isNull() && m_location_id_isValid;

    m_merchant_id_isValid = ::OpenAPI::fromJsonValue(m_merchant_id, json[QString("merchant_id")]);
    m_merchant_id_isSet = !json[QString("merchant_id")].isNull() && m_merchant_id_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_order_date_isValid = ::OpenAPI::fromJsonValue(m_order_date, json[QString("order_date")]);
    m_order_date_isSet = !json[QString("order_date")].isNull() && m_order_date_isValid;

    m_order_number_isValid = ::OpenAPI::fromJsonValue(m_order_number, json[QString("order_number")]);
    m_order_number_isSet = !json[QString("order_number")].isNull() && m_order_number_isValid;

    m_order_type_id_isValid = ::OpenAPI::fromJsonValue(m_order_type_id, json[QString("order_type_id")]);
    m_order_type_id_isSet = !json[QString("order_type_id")].isNull() && m_order_type_id_isValid;

    m_payment_status_isValid = ::OpenAPI::fromJsonValue(m_payment_status, json[QString("payment_status")]);
    m_payment_status_isSet = !json[QString("payment_status")].isNull() && m_payment_status_isValid;

    m_payments_isValid = ::OpenAPI::fromJsonValue(m_payments, json[QString("payments")]);
    m_payments_isSet = !json[QString("payments")].isNull() && m_payments_isValid;

    m_reference_id_isValid = ::OpenAPI::fromJsonValue(m_reference_id, json[QString("reference_id")]);
    m_reference_id_isSet = !json[QString("reference_id")].isNull() && m_reference_id_isValid;

    m_refunded_isValid = ::OpenAPI::fromJsonValue(m_refunded, json[QString("refunded")]);
    m_refunded_isSet = !json[QString("refunded")].isNull() && m_refunded_isValid;

    m_refunds_isValid = ::OpenAPI::fromJsonValue(m_refunds, json[QString("refunds")]);
    m_refunds_isSet = !json[QString("refunds")].isNull() && m_refunds_isValid;

    m_seat_isValid = ::OpenAPI::fromJsonValue(m_seat, json[QString("seat")]);
    m_seat_isSet = !json[QString("seat")].isNull() && m_seat_isValid;

    m_service_charges_isValid = ::OpenAPI::fromJsonValue(m_service_charges, json[QString("service_charges")]);
    m_service_charges_isSet = !json[QString("service_charges")].isNull() && m_service_charges_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_table_isValid = ::OpenAPI::fromJsonValue(m_table, json[QString("table")]);
    m_table_isSet = !json[QString("table")].isNull() && m_table_isValid;

    m_taxes_isValid = ::OpenAPI::fromJsonValue(m_taxes, json[QString("taxes")]);
    m_taxes_isSet = !json[QString("taxes")].isNull() && m_taxes_isValid;

    m_tenders_isValid = ::OpenAPI::fromJsonValue(m_tenders, json[QString("tenders")]);
    m_tenders_isSet = !json[QString("tenders")].isNull() && m_tenders_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_total_amount_isValid = ::OpenAPI::fromJsonValue(m_total_amount, json[QString("total_amount")]);
    m_total_amount_isSet = !json[QString("total_amount")].isNull() && m_total_amount_isValid;

    m_total_discount_isValid = ::OpenAPI::fromJsonValue(m_total_discount, json[QString("total_discount")]);
    m_total_discount_isSet = !json[QString("total_discount")].isNull() && m_total_discount_isValid;

    m_total_refund_isValid = ::OpenAPI::fromJsonValue(m_total_refund, json[QString("total_refund")]);
    m_total_refund_isSet = !json[QString("total_refund")].isNull() && m_total_refund_isValid;

    m_total_service_charge_isValid = ::OpenAPI::fromJsonValue(m_total_service_charge, json[QString("total_service_charge")]);
    m_total_service_charge_isSet = !json[QString("total_service_charge")].isNull() && m_total_service_charge_isValid;

    m_total_tax_isValid = ::OpenAPI::fromJsonValue(m_total_tax, json[QString("total_tax")]);
    m_total_tax_isSet = !json[QString("total_tax")].isNull() && m_total_tax_isValid;

    m_total_tip_isValid = ::OpenAPI::fromJsonValue(m_total_tip, json[QString("total_tip")]);
    m_total_tip_isSet = !json[QString("total_tip")].isNull() && m_total_tip_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updated_by")]);
    m_updated_by_isSet = !json[QString("updated_by")].isNull() && m_updated_by_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;

    m_voided_isValid = ::OpenAPI::fromJsonValue(m_voided, json[QString("voided")]);
    m_voided_isSet = !json[QString("voided")].isNull() && m_voided_isValid;

    m_voided_at_isValid = ::OpenAPI::fromJsonValue(m_voided_at, json[QString("voided_at")]);
    m_voided_at_isSet = !json[QString("voided_at")].isNull() && m_voided_at_isValid;
}

QString OAIOrder::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrder::asJsonObject() const {
    QJsonObject obj;
    if (m_closed_date_isSet) {
        obj.insert(QString("closed_date"), ::OpenAPI::toJsonValue(m_closed_date));
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
    if (m_customers.size() > 0) {
        obj.insert(QString("customers"), ::OpenAPI::toJsonValue(m_customers));
    }
    if (m_discounts.size() > 0) {
        obj.insert(QString("discounts"), ::OpenAPI::toJsonValue(m_discounts));
    }
    if (m_employee_id_isSet) {
        obj.insert(QString("employee_id"), ::OpenAPI::toJsonValue(m_employee_id));
    }
    if (m_fulfillments.size() > 0) {
        obj.insert(QString("fulfillments"), ::OpenAPI::toJsonValue(m_fulfillments));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_idempotency_key_isSet) {
        obj.insert(QString("idempotency_key"), ::OpenAPI::toJsonValue(m_idempotency_key));
    }
    if (m_line_items.size() > 0) {
        obj.insert(QString("line_items"), ::OpenAPI::toJsonValue(m_line_items));
    }
    if (m_location_id_isSet) {
        obj.insert(QString("location_id"), ::OpenAPI::toJsonValue(m_location_id));
    }
    if (m_merchant_id_isSet) {
        obj.insert(QString("merchant_id"), ::OpenAPI::toJsonValue(m_merchant_id));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_order_date_isSet) {
        obj.insert(QString("order_date"), ::OpenAPI::toJsonValue(m_order_date));
    }
    if (m_order_number_isSet) {
        obj.insert(QString("order_number"), ::OpenAPI::toJsonValue(m_order_number));
    }
    if (m_order_type_id_isSet) {
        obj.insert(QString("order_type_id"), ::OpenAPI::toJsonValue(m_order_type_id));
    }
    if (m_payment_status_isSet) {
        obj.insert(QString("payment_status"), ::OpenAPI::toJsonValue(m_payment_status));
    }
    if (m_payments.size() > 0) {
        obj.insert(QString("payments"), ::OpenAPI::toJsonValue(m_payments));
    }
    if (m_reference_id_isSet) {
        obj.insert(QString("reference_id"), ::OpenAPI::toJsonValue(m_reference_id));
    }
    if (m_refunded_isSet) {
        obj.insert(QString("refunded"), ::OpenAPI::toJsonValue(m_refunded));
    }
    if (m_refunds.size() > 0) {
        obj.insert(QString("refunds"), ::OpenAPI::toJsonValue(m_refunds));
    }
    if (m_seat_isSet) {
        obj.insert(QString("seat"), ::OpenAPI::toJsonValue(m_seat));
    }
    if (m_service_charges.size() > 0) {
        obj.insert(QString("service_charges"), ::OpenAPI::toJsonValue(m_service_charges));
    }
    if (m_source_isSet) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_table_isSet) {
        obj.insert(QString("table"), ::OpenAPI::toJsonValue(m_table));
    }
    if (m_taxes.size() > 0) {
        obj.insert(QString("taxes"), ::OpenAPI::toJsonValue(m_taxes));
    }
    if (m_tenders.size() > 0) {
        obj.insert(QString("tenders"), ::OpenAPI::toJsonValue(m_tenders));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_total_amount_isSet) {
        obj.insert(QString("total_amount"), ::OpenAPI::toJsonValue(m_total_amount));
    }
    if (m_total_discount_isSet) {
        obj.insert(QString("total_discount"), ::OpenAPI::toJsonValue(m_total_discount));
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
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_updated_by_isSet) {
        obj.insert(QString("updated_by"), ::OpenAPI::toJsonValue(m_updated_by));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    if (m_voided_isSet) {
        obj.insert(QString("voided"), ::OpenAPI::toJsonValue(m_voided));
    }
    if (m_voided_at_isSet) {
        obj.insert(QString("voided_at"), ::OpenAPI::toJsonValue(m_voided_at));
    }
    return obj;
}

QDate OAIOrder::getClosedDate() const {
    return m_closed_date;
}
void OAIOrder::setClosedDate(const QDate &closed_date) {
    m_closed_date = closed_date;
    m_closed_date_isSet = true;
}

bool OAIOrder::is_closed_date_Set() const{
    return m_closed_date_isSet;
}

bool OAIOrder::is_closed_date_Valid() const{
    return m_closed_date_isValid;
}

QDateTime OAIOrder::getCreatedAt() const {
    return m_created_at;
}
void OAIOrder::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIOrder::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIOrder::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIOrder::getCreatedBy() const {
    return m_created_by;
}
void OAIOrder::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIOrder::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIOrder::is_created_by_Valid() const{
    return m_created_by_isValid;
}

OAICurrency OAIOrder::getCurrency() const {
    return m_currency;
}
void OAIOrder::setCurrency(const OAICurrency &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIOrder::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIOrder::is_currency_Valid() const{
    return m_currency_isValid;
}

OAIObject OAIOrder::getCustomMappings() const {
    return m_custom_mappings;
}
void OAIOrder::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAIOrder::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAIOrder::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

QString OAIOrder::getCustomerId() const {
    return m_customer_id;
}
void OAIOrder::setCustomerId(const QString &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAIOrder::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAIOrder::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

QList<OAIOrder_customers_inner> OAIOrder::getCustomers() const {
    return m_customers;
}
void OAIOrder::setCustomers(const QList<OAIOrder_customers_inner> &customers) {
    m_customers = customers;
    m_customers_isSet = true;
}

bool OAIOrder::is_customers_Set() const{
    return m_customers_isSet;
}

bool OAIOrder::is_customers_Valid() const{
    return m_customers_isValid;
}

QList<OAIOrder_discounts_inner> OAIOrder::getDiscounts() const {
    return m_discounts;
}
void OAIOrder::setDiscounts(const QList<OAIOrder_discounts_inner> &discounts) {
    m_discounts = discounts;
    m_discounts_isSet = true;
}

bool OAIOrder::is_discounts_Set() const{
    return m_discounts_isSet;
}

bool OAIOrder::is_discounts_Valid() const{
    return m_discounts_isValid;
}

QString OAIOrder::getEmployeeId() const {
    return m_employee_id;
}
void OAIOrder::setEmployeeId(const QString &employee_id) {
    m_employee_id = employee_id;
    m_employee_id_isSet = true;
}

bool OAIOrder::is_employee_id_Set() const{
    return m_employee_id_isSet;
}

bool OAIOrder::is_employee_id_Valid() const{
    return m_employee_id_isValid;
}

QList<OAIOrder_fulfillments_inner> OAIOrder::getFulfillments() const {
    return m_fulfillments;
}
void OAIOrder::setFulfillments(const QList<OAIOrder_fulfillments_inner> &fulfillments) {
    m_fulfillments = fulfillments;
    m_fulfillments_isSet = true;
}

bool OAIOrder::is_fulfillments_Set() const{
    return m_fulfillments_isSet;
}

bool OAIOrder::is_fulfillments_Valid() const{
    return m_fulfillments_isValid;
}

QString OAIOrder::getId() const {
    return m_id;
}
void OAIOrder::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOrder::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOrder::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIOrder::getIdempotencyKey() const {
    return m_idempotency_key;
}
void OAIOrder::setIdempotencyKey(const QString &idempotency_key) {
    m_idempotency_key = idempotency_key;
    m_idempotency_key_isSet = true;
}

bool OAIOrder::is_idempotency_key_Set() const{
    return m_idempotency_key_isSet;
}

bool OAIOrder::is_idempotency_key_Valid() const{
    return m_idempotency_key_isValid;
}

QList<OAIOrder_line_items_inner> OAIOrder::getLineItems() const {
    return m_line_items;
}
void OAIOrder::setLineItems(const QList<OAIOrder_line_items_inner> &line_items) {
    m_line_items = line_items;
    m_line_items_isSet = true;
}

bool OAIOrder::is_line_items_Set() const{
    return m_line_items_isSet;
}

bool OAIOrder::is_line_items_Valid() const{
    return m_line_items_isValid;
}

QString OAIOrder::getLocationId() const {
    return m_location_id;
}
void OAIOrder::setLocationId(const QString &location_id) {
    m_location_id = location_id;
    m_location_id_isSet = true;
}

bool OAIOrder::is_location_id_Set() const{
    return m_location_id_isSet;
}

bool OAIOrder::is_location_id_Valid() const{
    return m_location_id_isValid;
}

QString OAIOrder::getMerchantId() const {
    return m_merchant_id;
}
void OAIOrder::setMerchantId(const QString &merchant_id) {
    m_merchant_id = merchant_id;
    m_merchant_id_isSet = true;
}

bool OAIOrder::is_merchant_id_Set() const{
    return m_merchant_id_isSet;
}

bool OAIOrder::is_merchant_id_Valid() const{
    return m_merchant_id_isValid;
}

QString OAIOrder::getNote() const {
    return m_note;
}
void OAIOrder::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAIOrder::is_note_Set() const{
    return m_note_isSet;
}

bool OAIOrder::is_note_Valid() const{
    return m_note_isValid;
}

QDate OAIOrder::getOrderDate() const {
    return m_order_date;
}
void OAIOrder::setOrderDate(const QDate &order_date) {
    m_order_date = order_date;
    m_order_date_isSet = true;
}

bool OAIOrder::is_order_date_Set() const{
    return m_order_date_isSet;
}

bool OAIOrder::is_order_date_Valid() const{
    return m_order_date_isValid;
}

QString OAIOrder::getOrderNumber() const {
    return m_order_number;
}
void OAIOrder::setOrderNumber(const QString &order_number) {
    m_order_number = order_number;
    m_order_number_isSet = true;
}

bool OAIOrder::is_order_number_Set() const{
    return m_order_number_isSet;
}

bool OAIOrder::is_order_number_Valid() const{
    return m_order_number_isValid;
}

QString OAIOrder::getOrderTypeId() const {
    return m_order_type_id;
}
void OAIOrder::setOrderTypeId(const QString &order_type_id) {
    m_order_type_id = order_type_id;
    m_order_type_id_isSet = true;
}

bool OAIOrder::is_order_type_id_Set() const{
    return m_order_type_id_isSet;
}

bool OAIOrder::is_order_type_id_Valid() const{
    return m_order_type_id_isValid;
}

QString OAIOrder::getPaymentStatus() const {
    return m_payment_status;
}
void OAIOrder::setPaymentStatus(const QString &payment_status) {
    m_payment_status = payment_status;
    m_payment_status_isSet = true;
}

bool OAIOrder::is_payment_status_Set() const{
    return m_payment_status_isSet;
}

bool OAIOrder::is_payment_status_Valid() const{
    return m_payment_status_isValid;
}

QList<OAIOrder_payments_inner> OAIOrder::getPayments() const {
    return m_payments;
}
void OAIOrder::setPayments(const QList<OAIOrder_payments_inner> &payments) {
    m_payments = payments;
    m_payments_isSet = true;
}

bool OAIOrder::is_payments_Set() const{
    return m_payments_isSet;
}

bool OAIOrder::is_payments_Valid() const{
    return m_payments_isValid;
}

QString OAIOrder::getReferenceId() const {
    return m_reference_id;
}
void OAIOrder::setReferenceId(const QString &reference_id) {
    m_reference_id = reference_id;
    m_reference_id_isSet = true;
}

bool OAIOrder::is_reference_id_Set() const{
    return m_reference_id_isSet;
}

bool OAIOrder::is_reference_id_Valid() const{
    return m_reference_id_isValid;
}

bool OAIOrder::isRefunded() const {
    return m_refunded;
}
void OAIOrder::setRefunded(const bool &refunded) {
    m_refunded = refunded;
    m_refunded_isSet = true;
}

bool OAIOrder::is_refunded_Set() const{
    return m_refunded_isSet;
}

bool OAIOrder::is_refunded_Valid() const{
    return m_refunded_isValid;
}

QList<OAIOrder_refunds_inner> OAIOrder::getRefunds() const {
    return m_refunds;
}
void OAIOrder::setRefunds(const QList<OAIOrder_refunds_inner> &refunds) {
    m_refunds = refunds;
    m_refunds_isSet = true;
}

bool OAIOrder::is_refunds_Set() const{
    return m_refunds_isSet;
}

bool OAIOrder::is_refunds_Valid() const{
    return m_refunds_isValid;
}

QString OAIOrder::getSeat() const {
    return m_seat;
}
void OAIOrder::setSeat(const QString &seat) {
    m_seat = seat;
    m_seat_isSet = true;
}

bool OAIOrder::is_seat_Set() const{
    return m_seat_isSet;
}

bool OAIOrder::is_seat_Valid() const{
    return m_seat_isValid;
}

QList<OAIServiceCharge> OAIOrder::getServiceCharges() const {
    return m_service_charges;
}
void OAIOrder::setServiceCharges(const QList<OAIServiceCharge> &service_charges) {
    m_service_charges = service_charges;
    m_service_charges_isSet = true;
}

bool OAIOrder::is_service_charges_Set() const{
    return m_service_charges_isSet;
}

bool OAIOrder::is_service_charges_Valid() const{
    return m_service_charges_isValid;
}

QString OAIOrder::getSource() const {
    return m_source;
}
void OAIOrder::setSource(const QString &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIOrder::is_source_Set() const{
    return m_source_isSet;
}

bool OAIOrder::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIOrder::getStatus() const {
    return m_status;
}
void OAIOrder::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIOrder::is_status_Set() const{
    return m_status_isSet;
}

bool OAIOrder::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIOrder::getTable() const {
    return m_table;
}
void OAIOrder::setTable(const QString &table) {
    m_table = table;
    m_table_isSet = true;
}

bool OAIOrder::is_table_Set() const{
    return m_table_isSet;
}

bool OAIOrder::is_table_Valid() const{
    return m_table_isValid;
}

QList<OAIOrder_taxes_inner> OAIOrder::getTaxes() const {
    return m_taxes;
}
void OAIOrder::setTaxes(const QList<OAIOrder_taxes_inner> &taxes) {
    m_taxes = taxes;
    m_taxes_isSet = true;
}

bool OAIOrder::is_taxes_Set() const{
    return m_taxes_isSet;
}

bool OAIOrder::is_taxes_Valid() const{
    return m_taxes_isValid;
}

QList<OAIOrder_tenders_inner> OAIOrder::getTenders() const {
    return m_tenders;
}
void OAIOrder::setTenders(const QList<OAIOrder_tenders_inner> &tenders) {
    m_tenders = tenders;
    m_tenders_isSet = true;
}

bool OAIOrder::is_tenders_Set() const{
    return m_tenders_isSet;
}

bool OAIOrder::is_tenders_Valid() const{
    return m_tenders_isValid;
}

QString OAIOrder::getTitle() const {
    return m_title;
}
void OAIOrder::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIOrder::is_title_Set() const{
    return m_title_isSet;
}

bool OAIOrder::is_title_Valid() const{
    return m_title_isValid;
}

qint32 OAIOrder::getTotalAmount() const {
    return m_total_amount;
}
void OAIOrder::setTotalAmount(const qint32 &total_amount) {
    m_total_amount = total_amount;
    m_total_amount_isSet = true;
}

bool OAIOrder::is_total_amount_Set() const{
    return m_total_amount_isSet;
}

bool OAIOrder::is_total_amount_Valid() const{
    return m_total_amount_isValid;
}

qint32 OAIOrder::getTotalDiscount() const {
    return m_total_discount;
}
void OAIOrder::setTotalDiscount(const qint32 &total_discount) {
    m_total_discount = total_discount;
    m_total_discount_isSet = true;
}

bool OAIOrder::is_total_discount_Set() const{
    return m_total_discount_isSet;
}

bool OAIOrder::is_total_discount_Valid() const{
    return m_total_discount_isValid;
}

qint32 OAIOrder::getTotalRefund() const {
    return m_total_refund;
}
void OAIOrder::setTotalRefund(const qint32 &total_refund) {
    m_total_refund = total_refund;
    m_total_refund_isSet = true;
}

bool OAIOrder::is_total_refund_Set() const{
    return m_total_refund_isSet;
}

bool OAIOrder::is_total_refund_Valid() const{
    return m_total_refund_isValid;
}

qint32 OAIOrder::getTotalServiceCharge() const {
    return m_total_service_charge;
}
void OAIOrder::setTotalServiceCharge(const qint32 &total_service_charge) {
    m_total_service_charge = total_service_charge;
    m_total_service_charge_isSet = true;
}

bool OAIOrder::is_total_service_charge_Set() const{
    return m_total_service_charge_isSet;
}

bool OAIOrder::is_total_service_charge_Valid() const{
    return m_total_service_charge_isValid;
}

qint32 OAIOrder::getTotalTax() const {
    return m_total_tax;
}
void OAIOrder::setTotalTax(const qint32 &total_tax) {
    m_total_tax = total_tax;
    m_total_tax_isSet = true;
}

bool OAIOrder::is_total_tax_Set() const{
    return m_total_tax_isSet;
}

bool OAIOrder::is_total_tax_Valid() const{
    return m_total_tax_isValid;
}

qint32 OAIOrder::getTotalTip() const {
    return m_total_tip;
}
void OAIOrder::setTotalTip(const qint32 &total_tip) {
    m_total_tip = total_tip;
    m_total_tip_isSet = true;
}

bool OAIOrder::is_total_tip_Set() const{
    return m_total_tip_isSet;
}

bool OAIOrder::is_total_tip_Valid() const{
    return m_total_tip_isValid;
}

QDateTime OAIOrder::getUpdatedAt() const {
    return m_updated_at;
}
void OAIOrder::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIOrder::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIOrder::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIOrder::getUpdatedBy() const {
    return m_updated_by;
}
void OAIOrder::setUpdatedBy(const QString &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAIOrder::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAIOrder::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

QString OAIOrder::getVersion() const {
    return m_version;
}
void OAIOrder::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIOrder::is_version_Set() const{
    return m_version_isSet;
}

bool OAIOrder::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIOrder::isVoided() const {
    return m_voided;
}
void OAIOrder::setVoided(const bool &voided) {
    m_voided = voided;
    m_voided_isSet = true;
}

bool OAIOrder::is_voided_Set() const{
    return m_voided_isSet;
}

bool OAIOrder::is_voided_Valid() const{
    return m_voided_isValid;
}

QDateTime OAIOrder::getVoidedAt() const {
    return m_voided_at;
}
void OAIOrder::setVoidedAt(const QDateTime &voided_at) {
    m_voided_at = voided_at;
    m_voided_at_isSet = true;
}

bool OAIOrder::is_voided_at_Set() const{
    return m_voided_at_isSet;
}

bool OAIOrder::is_voided_at_Valid() const{
    return m_voided_at_isValid;
}

bool OAIOrder::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_closed_date_isSet) {
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

        if (m_customers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_discounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_employee_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fulfillments.size() > 0) {
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

        if (m_line_items.size() > 0) {
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

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payments.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_refunded_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_refunds.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_seat_isSet) {
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

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_table_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_taxes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tenders.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
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

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_voided_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_voided_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrder::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_location_id_isValid && m_merchant_id_isValid && true;
}

} // namespace OpenAPI
