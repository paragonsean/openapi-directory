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

#include "OAIInvoice.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIInvoice::OAIInvoice(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIInvoice::OAIInvoice() {
    this->initializeModel();
}

OAIInvoice::~OAIInvoice() {}

void OAIInvoice::initializeModel() {

    m_accounting_by_row_isSet = false;
    m_accounting_by_row_isValid = false;

    m_balance_isSet = false;
    m_balance_isValid = false;

    m_bank_account_isSet = false;
    m_bank_account_isValid = false;

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_channel_isSet = false;
    m_channel_isValid = false;

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

    m_customer_memo_isSet = false;
    m_customer_memo_isValid = false;

    m_deposit_isSet = false;
    m_deposit_isValid = false;

    m_discount_amount_isSet = false;
    m_discount_amount_isValid = false;

    m_discount_percentage_isSet = false;
    m_discount_percentage_isValid = false;

    m_downstream_id_isSet = false;
    m_downstream_id_isValid = false;

    m_due_date_isSet = false;
    m_due_date_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_invoice_date_isSet = false;
    m_invoice_date_isValid = false;

    m_invoice_sent_isSet = false;
    m_invoice_sent_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_ledger_account_isSet = false;
    m_ledger_account_isValid = false;

    m_line_items_isSet = false;
    m_line_items_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_payment_method_isSet = false;
    m_payment_method_isValid = false;

    m_po_number_isSet = false;
    m_po_number_isValid = false;

    m_reference_isSet = false;
    m_reference_isValid = false;

    m_row_version_isSet = false;
    m_row_version_isValid = false;

    m_shipping_address_isSet = false;
    m_shipping_address_isValid = false;

    m_source_document_url_isSet = false;
    m_source_document_url_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_sub_total_isSet = false;
    m_sub_total_isValid = false;

    m_tax_code_isSet = false;
    m_tax_code_isValid = false;

    m_tax_inclusive_isSet = false;
    m_tax_inclusive_isValid = false;

    m_template_id_isSet = false;
    m_template_id_isValid = false;

    m_terms_isSet = false;
    m_terms_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;

    m_total_tax_isSet = false;
    m_total_tax_isValid = false;

    m_tracking_category_isSet = false;
    m_tracking_category_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;
}

void OAIInvoice::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIInvoice::fromJsonObject(QJsonObject json) {

    m_accounting_by_row_isValid = ::OpenAPI::fromJsonValue(m_accounting_by_row, json[QString("accounting_by_row")]);
    m_accounting_by_row_isSet = !json[QString("accounting_by_row")].isNull() && m_accounting_by_row_isValid;

    m_balance_isValid = ::OpenAPI::fromJsonValue(m_balance, json[QString("balance")]);
    m_balance_isSet = !json[QString("balance")].isNull() && m_balance_isValid;

    m_bank_account_isValid = ::OpenAPI::fromJsonValue(m_bank_account, json[QString("bank_account")]);
    m_bank_account_isSet = !json[QString("bank_account")].isNull() && m_bank_account_isValid;

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billing_address")]);
    m_billing_address_isSet = !json[QString("billing_address")].isNull() && m_billing_address_isValid;

    m_channel_isValid = ::OpenAPI::fromJsonValue(m_channel, json[QString("channel")]);
    m_channel_isSet = !json[QString("channel")].isNull() && m_channel_isValid;

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

    m_customer_memo_isValid = ::OpenAPI::fromJsonValue(m_customer_memo, json[QString("customer_memo")]);
    m_customer_memo_isSet = !json[QString("customer_memo")].isNull() && m_customer_memo_isValid;

    m_deposit_isValid = ::OpenAPI::fromJsonValue(m_deposit, json[QString("deposit")]);
    m_deposit_isSet = !json[QString("deposit")].isNull() && m_deposit_isValid;

    m_discount_amount_isValid = ::OpenAPI::fromJsonValue(m_discount_amount, json[QString("discount_amount")]);
    m_discount_amount_isSet = !json[QString("discount_amount")].isNull() && m_discount_amount_isValid;

    m_discount_percentage_isValid = ::OpenAPI::fromJsonValue(m_discount_percentage, json[QString("discount_percentage")]);
    m_discount_percentage_isSet = !json[QString("discount_percentage")].isNull() && m_discount_percentage_isValid;

    m_downstream_id_isValid = ::OpenAPI::fromJsonValue(m_downstream_id, json[QString("downstream_id")]);
    m_downstream_id_isSet = !json[QString("downstream_id")].isNull() && m_downstream_id_isValid;

    m_due_date_isValid = ::OpenAPI::fromJsonValue(m_due_date, json[QString("due_date")]);
    m_due_date_isSet = !json[QString("due_date")].isNull() && m_due_date_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_invoice_date_isValid = ::OpenAPI::fromJsonValue(m_invoice_date, json[QString("invoice_date")]);
    m_invoice_date_isSet = !json[QString("invoice_date")].isNull() && m_invoice_date_isValid;

    m_invoice_sent_isValid = ::OpenAPI::fromJsonValue(m_invoice_sent, json[QString("invoice_sent")]);
    m_invoice_sent_isSet = !json[QString("invoice_sent")].isNull() && m_invoice_sent_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_ledger_account_isValid = ::OpenAPI::fromJsonValue(m_ledger_account, json[QString("ledger_account")]);
    m_ledger_account_isSet = !json[QString("ledger_account")].isNull() && m_ledger_account_isValid;

    m_line_items_isValid = ::OpenAPI::fromJsonValue(m_line_items, json[QString("line_items")]);
    m_line_items_isSet = !json[QString("line_items")].isNull() && m_line_items_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("number")]);
    m_number_isSet = !json[QString("number")].isNull() && m_number_isValid;

    m_payment_method_isValid = ::OpenAPI::fromJsonValue(m_payment_method, json[QString("payment_method")]);
    m_payment_method_isSet = !json[QString("payment_method")].isNull() && m_payment_method_isValid;

    m_po_number_isValid = ::OpenAPI::fromJsonValue(m_po_number, json[QString("po_number")]);
    m_po_number_isSet = !json[QString("po_number")].isNull() && m_po_number_isValid;

    m_reference_isValid = ::OpenAPI::fromJsonValue(m_reference, json[QString("reference")]);
    m_reference_isSet = !json[QString("reference")].isNull() && m_reference_isValid;

    m_row_version_isValid = ::OpenAPI::fromJsonValue(m_row_version, json[QString("row_version")]);
    m_row_version_isSet = !json[QString("row_version")].isNull() && m_row_version_isValid;

    m_shipping_address_isValid = ::OpenAPI::fromJsonValue(m_shipping_address, json[QString("shipping_address")]);
    m_shipping_address_isSet = !json[QString("shipping_address")].isNull() && m_shipping_address_isValid;

    m_source_document_url_isValid = ::OpenAPI::fromJsonValue(m_source_document_url, json[QString("source_document_url")]);
    m_source_document_url_isSet = !json[QString("source_document_url")].isNull() && m_source_document_url_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_sub_total_isValid = ::OpenAPI::fromJsonValue(m_sub_total, json[QString("sub_total")]);
    m_sub_total_isSet = !json[QString("sub_total")].isNull() && m_sub_total_isValid;

    m_tax_code_isValid = ::OpenAPI::fromJsonValue(m_tax_code, json[QString("tax_code")]);
    m_tax_code_isSet = !json[QString("tax_code")].isNull() && m_tax_code_isValid;

    m_tax_inclusive_isValid = ::OpenAPI::fromJsonValue(m_tax_inclusive, json[QString("tax_inclusive")]);
    m_tax_inclusive_isSet = !json[QString("tax_inclusive")].isNull() && m_tax_inclusive_isValid;

    m_template_id_isValid = ::OpenAPI::fromJsonValue(m_template_id, json[QString("template_id")]);
    m_template_id_isSet = !json[QString("template_id")].isNull() && m_template_id_isValid;

    m_terms_isValid = ::OpenAPI::fromJsonValue(m_terms, json[QString("terms")]);
    m_terms_isSet = !json[QString("terms")].isNull() && m_terms_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;

    m_total_tax_isValid = ::OpenAPI::fromJsonValue(m_total_tax, json[QString("total_tax")]);
    m_total_tax_isSet = !json[QString("total_tax")].isNull() && m_total_tax_isValid;

    m_tracking_category_isValid = ::OpenAPI::fromJsonValue(m_tracking_category, json[QString("tracking_category")]);
    m_tracking_category_isSet = !json[QString("tracking_category")].isNull() && m_tracking_category_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updated_by")]);
    m_updated_by_isSet = !json[QString("updated_by")].isNull() && m_updated_by_isValid;
}

QString OAIInvoice::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIInvoice::asJsonObject() const {
    QJsonObject obj;
    if (m_accounting_by_row_isSet) {
        obj.insert(QString("accounting_by_row"), ::OpenAPI::toJsonValue(m_accounting_by_row));
    }
    if (m_balance_isSet) {
        obj.insert(QString("balance"), ::OpenAPI::toJsonValue(m_balance));
    }
    if (m_bank_account.isSet()) {
        obj.insert(QString("bank_account"), ::OpenAPI::toJsonValue(m_bank_account));
    }
    if (m_billing_address.isSet()) {
        obj.insert(QString("billing_address"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_channel_isSet) {
        obj.insert(QString("channel"), ::OpenAPI::toJsonValue(m_channel));
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
    if (m_customer_memo_isSet) {
        obj.insert(QString("customer_memo"), ::OpenAPI::toJsonValue(m_customer_memo));
    }
    if (m_deposit_isSet) {
        obj.insert(QString("deposit"), ::OpenAPI::toJsonValue(m_deposit));
    }
    if (m_discount_amount_isSet) {
        obj.insert(QString("discount_amount"), ::OpenAPI::toJsonValue(m_discount_amount));
    }
    if (m_discount_percentage_isSet) {
        obj.insert(QString("discount_percentage"), ::OpenAPI::toJsonValue(m_discount_percentage));
    }
    if (m_downstream_id_isSet) {
        obj.insert(QString("downstream_id"), ::OpenAPI::toJsonValue(m_downstream_id));
    }
    if (m_due_date_isSet) {
        obj.insert(QString("due_date"), ::OpenAPI::toJsonValue(m_due_date));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_invoice_date_isSet) {
        obj.insert(QString("invoice_date"), ::OpenAPI::toJsonValue(m_invoice_date));
    }
    if (m_invoice_sent_isSet) {
        obj.insert(QString("invoice_sent"), ::OpenAPI::toJsonValue(m_invoice_sent));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_ledger_account.isSet()) {
        obj.insert(QString("ledger_account"), ::OpenAPI::toJsonValue(m_ledger_account));
    }
    if (m_line_items.size() > 0) {
        obj.insert(QString("line_items"), ::OpenAPI::toJsonValue(m_line_items));
    }
    if (m_number_isSet) {
        obj.insert(QString("number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_payment_method_isSet) {
        obj.insert(QString("payment_method"), ::OpenAPI::toJsonValue(m_payment_method));
    }
    if (m_po_number_isSet) {
        obj.insert(QString("po_number"), ::OpenAPI::toJsonValue(m_po_number));
    }
    if (m_reference_isSet) {
        obj.insert(QString("reference"), ::OpenAPI::toJsonValue(m_reference));
    }
    if (m_row_version_isSet) {
        obj.insert(QString("row_version"), ::OpenAPI::toJsonValue(m_row_version));
    }
    if (m_shipping_address.isSet()) {
        obj.insert(QString("shipping_address"), ::OpenAPI::toJsonValue(m_shipping_address));
    }
    if (m_source_document_url_isSet) {
        obj.insert(QString("source_document_url"), ::OpenAPI::toJsonValue(m_source_document_url));
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
    if (m_template_id_isSet) {
        obj.insert(QString("template_id"), ::OpenAPI::toJsonValue(m_template_id));
    }
    if (m_terms_isSet) {
        obj.insert(QString("terms"), ::OpenAPI::toJsonValue(m_terms));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    if (m_total_tax_isSet) {
        obj.insert(QString("total_tax"), ::OpenAPI::toJsonValue(m_total_tax));
    }
    if (m_tracking_category.isSet()) {
        obj.insert(QString("tracking_category"), ::OpenAPI::toJsonValue(m_tracking_category));
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

bool OAIInvoice::isAccountingByRow() const {
    return m_accounting_by_row;
}
void OAIInvoice::setAccountingByRow(const bool &accounting_by_row) {
    m_accounting_by_row = accounting_by_row;
    m_accounting_by_row_isSet = true;
}

bool OAIInvoice::is_accounting_by_row_Set() const{
    return m_accounting_by_row_isSet;
}

bool OAIInvoice::is_accounting_by_row_Valid() const{
    return m_accounting_by_row_isValid;
}

double OAIInvoice::getBalance() const {
    return m_balance;
}
void OAIInvoice::setBalance(const double &balance) {
    m_balance = balance;
    m_balance_isSet = true;
}

bool OAIInvoice::is_balance_Set() const{
    return m_balance_isSet;
}

bool OAIInvoice::is_balance_Valid() const{
    return m_balance_isValid;
}

OAIBankAccount OAIInvoice::getBankAccount() const {
    return m_bank_account;
}
void OAIInvoice::setBankAccount(const OAIBankAccount &bank_account) {
    m_bank_account = bank_account;
    m_bank_account_isSet = true;
}

bool OAIInvoice::is_bank_account_Set() const{
    return m_bank_account_isSet;
}

bool OAIInvoice::is_bank_account_Valid() const{
    return m_bank_account_isValid;
}

OAIAddress OAIInvoice::getBillingAddress() const {
    return m_billing_address;
}
void OAIInvoice::setBillingAddress(const OAIAddress &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAIInvoice::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAIInvoice::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAIInvoice::getChannel() const {
    return m_channel;
}
void OAIInvoice::setChannel(const QString &channel) {
    m_channel = channel;
    m_channel_isSet = true;
}

bool OAIInvoice::is_channel_Set() const{
    return m_channel_isSet;
}

bool OAIInvoice::is_channel_Valid() const{
    return m_channel_isValid;
}

QDateTime OAIInvoice::getCreatedAt() const {
    return m_created_at;
}
void OAIInvoice::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIInvoice::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIInvoice::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIInvoice::getCreatedBy() const {
    return m_created_by;
}
void OAIInvoice::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIInvoice::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIInvoice::is_created_by_Valid() const{
    return m_created_by_isValid;
}

OAICurrency OAIInvoice::getCurrency() const {
    return m_currency;
}
void OAIInvoice::setCurrency(const OAICurrency &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIInvoice::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIInvoice::is_currency_Valid() const{
    return m_currency_isValid;
}

double OAIInvoice::getCurrencyRate() const {
    return m_currency_rate;
}
void OAIInvoice::setCurrencyRate(const double &currency_rate) {
    m_currency_rate = currency_rate;
    m_currency_rate_isSet = true;
}

bool OAIInvoice::is_currency_rate_Set() const{
    return m_currency_rate_isSet;
}

bool OAIInvoice::is_currency_rate_Valid() const{
    return m_currency_rate_isValid;
}

OAIObject OAIInvoice::getCustomMappings() const {
    return m_custom_mappings;
}
void OAIInvoice::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAIInvoice::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAIInvoice::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

OAILinkedCustomer OAIInvoice::getCustomer() const {
    return m_customer;
}
void OAIInvoice::setCustomer(const OAILinkedCustomer &customer) {
    m_customer = customer;
    m_customer_isSet = true;
}

bool OAIInvoice::is_customer_Set() const{
    return m_customer_isSet;
}

bool OAIInvoice::is_customer_Valid() const{
    return m_customer_isValid;
}

QString OAIInvoice::getCustomerMemo() const {
    return m_customer_memo;
}
void OAIInvoice::setCustomerMemo(const QString &customer_memo) {
    m_customer_memo = customer_memo;
    m_customer_memo_isSet = true;
}

bool OAIInvoice::is_customer_memo_Set() const{
    return m_customer_memo_isSet;
}

bool OAIInvoice::is_customer_memo_Valid() const{
    return m_customer_memo_isValid;
}

double OAIInvoice::getDeposit() const {
    return m_deposit;
}
void OAIInvoice::setDeposit(const double &deposit) {
    m_deposit = deposit;
    m_deposit_isSet = true;
}

bool OAIInvoice::is_deposit_Set() const{
    return m_deposit_isSet;
}

bool OAIInvoice::is_deposit_Valid() const{
    return m_deposit_isValid;
}

double OAIInvoice::getDiscountAmount() const {
    return m_discount_amount;
}
void OAIInvoice::setDiscountAmount(const double &discount_amount) {
    m_discount_amount = discount_amount;
    m_discount_amount_isSet = true;
}

bool OAIInvoice::is_discount_amount_Set() const{
    return m_discount_amount_isSet;
}

bool OAIInvoice::is_discount_amount_Valid() const{
    return m_discount_amount_isValid;
}

double OAIInvoice::getDiscountPercentage() const {
    return m_discount_percentage;
}
void OAIInvoice::setDiscountPercentage(const double &discount_percentage) {
    m_discount_percentage = discount_percentage;
    m_discount_percentage_isSet = true;
}

bool OAIInvoice::is_discount_percentage_Set() const{
    return m_discount_percentage_isSet;
}

bool OAIInvoice::is_discount_percentage_Valid() const{
    return m_discount_percentage_isValid;
}

QString OAIInvoice::getDownstreamId() const {
    return m_downstream_id;
}
void OAIInvoice::setDownstreamId(const QString &downstream_id) {
    m_downstream_id = downstream_id;
    m_downstream_id_isSet = true;
}

bool OAIInvoice::is_downstream_id_Set() const{
    return m_downstream_id_isSet;
}

bool OAIInvoice::is_downstream_id_Valid() const{
    return m_downstream_id_isValid;
}

QDate OAIInvoice::getDueDate() const {
    return m_due_date;
}
void OAIInvoice::setDueDate(const QDate &due_date) {
    m_due_date = due_date;
    m_due_date_isSet = true;
}

bool OAIInvoice::is_due_date_Set() const{
    return m_due_date_isSet;
}

bool OAIInvoice::is_due_date_Valid() const{
    return m_due_date_isValid;
}

QString OAIInvoice::getId() const {
    return m_id;
}
void OAIInvoice::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIInvoice::is_id_Set() const{
    return m_id_isSet;
}

bool OAIInvoice::is_id_Valid() const{
    return m_id_isValid;
}

QDate OAIInvoice::getInvoiceDate() const {
    return m_invoice_date;
}
void OAIInvoice::setInvoiceDate(const QDate &invoice_date) {
    m_invoice_date = invoice_date;
    m_invoice_date_isSet = true;
}

bool OAIInvoice::is_invoice_date_Set() const{
    return m_invoice_date_isSet;
}

bool OAIInvoice::is_invoice_date_Valid() const{
    return m_invoice_date_isValid;
}

bool OAIInvoice::isInvoiceSent() const {
    return m_invoice_sent;
}
void OAIInvoice::setInvoiceSent(const bool &invoice_sent) {
    m_invoice_sent = invoice_sent;
    m_invoice_sent_isSet = true;
}

bool OAIInvoice::is_invoice_sent_Set() const{
    return m_invoice_sent_isSet;
}

bool OAIInvoice::is_invoice_sent_Valid() const{
    return m_invoice_sent_isValid;
}

QString OAIInvoice::getLanguage() const {
    return m_language;
}
void OAIInvoice::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIInvoice::is_language_Set() const{
    return m_language_isSet;
}

bool OAIInvoice::is_language_Valid() const{
    return m_language_isValid;
}

OAILinkedLedgerAccount OAIInvoice::getLedgerAccount() const {
    return m_ledger_account;
}
void OAIInvoice::setLedgerAccount(const OAILinkedLedgerAccount &ledger_account) {
    m_ledger_account = ledger_account;
    m_ledger_account_isSet = true;
}

bool OAIInvoice::is_ledger_account_Set() const{
    return m_ledger_account_isSet;
}

bool OAIInvoice::is_ledger_account_Valid() const{
    return m_ledger_account_isValid;
}

QList<OAIInvoiceLineItem> OAIInvoice::getLineItems() const {
    return m_line_items;
}
void OAIInvoice::setLineItems(const QList<OAIInvoiceLineItem> &line_items) {
    m_line_items = line_items;
    m_line_items_isSet = true;
}

bool OAIInvoice::is_line_items_Set() const{
    return m_line_items_isSet;
}

bool OAIInvoice::is_line_items_Valid() const{
    return m_line_items_isValid;
}

QString OAIInvoice::getNumber() const {
    return m_number;
}
void OAIInvoice::setNumber(const QString &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIInvoice::is_number_Set() const{
    return m_number_isSet;
}

bool OAIInvoice::is_number_Valid() const{
    return m_number_isValid;
}

QString OAIInvoice::getPaymentMethod() const {
    return m_payment_method;
}
void OAIInvoice::setPaymentMethod(const QString &payment_method) {
    m_payment_method = payment_method;
    m_payment_method_isSet = true;
}

bool OAIInvoice::is_payment_method_Set() const{
    return m_payment_method_isSet;
}

bool OAIInvoice::is_payment_method_Valid() const{
    return m_payment_method_isValid;
}

QString OAIInvoice::getPoNumber() const {
    return m_po_number;
}
void OAIInvoice::setPoNumber(const QString &po_number) {
    m_po_number = po_number;
    m_po_number_isSet = true;
}

bool OAIInvoice::is_po_number_Set() const{
    return m_po_number_isSet;
}

bool OAIInvoice::is_po_number_Valid() const{
    return m_po_number_isValid;
}

QString OAIInvoice::getReference() const {
    return m_reference;
}
void OAIInvoice::setReference(const QString &reference) {
    m_reference = reference;
    m_reference_isSet = true;
}

bool OAIInvoice::is_reference_Set() const{
    return m_reference_isSet;
}

bool OAIInvoice::is_reference_Valid() const{
    return m_reference_isValid;
}

QString OAIInvoice::getRowVersion() const {
    return m_row_version;
}
void OAIInvoice::setRowVersion(const QString &row_version) {
    m_row_version = row_version;
    m_row_version_isSet = true;
}

bool OAIInvoice::is_row_version_Set() const{
    return m_row_version_isSet;
}

bool OAIInvoice::is_row_version_Valid() const{
    return m_row_version_isValid;
}

OAIAddress OAIInvoice::getShippingAddress() const {
    return m_shipping_address;
}
void OAIInvoice::setShippingAddress(const OAIAddress &shipping_address) {
    m_shipping_address = shipping_address;
    m_shipping_address_isSet = true;
}

bool OAIInvoice::is_shipping_address_Set() const{
    return m_shipping_address_isSet;
}

bool OAIInvoice::is_shipping_address_Valid() const{
    return m_shipping_address_isValid;
}

QString OAIInvoice::getSourceDocumentUrl() const {
    return m_source_document_url;
}
void OAIInvoice::setSourceDocumentUrl(const QString &source_document_url) {
    m_source_document_url = source_document_url;
    m_source_document_url_isSet = true;
}

bool OAIInvoice::is_source_document_url_Set() const{
    return m_source_document_url_isSet;
}

bool OAIInvoice::is_source_document_url_Valid() const{
    return m_source_document_url_isValid;
}

QString OAIInvoice::getStatus() const {
    return m_status;
}
void OAIInvoice::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIInvoice::is_status_Set() const{
    return m_status_isSet;
}

bool OAIInvoice::is_status_Valid() const{
    return m_status_isValid;
}

double OAIInvoice::getSubTotal() const {
    return m_sub_total;
}
void OAIInvoice::setSubTotal(const double &sub_total) {
    m_sub_total = sub_total;
    m_sub_total_isSet = true;
}

bool OAIInvoice::is_sub_total_Set() const{
    return m_sub_total_isSet;
}

bool OAIInvoice::is_sub_total_Valid() const{
    return m_sub_total_isValid;
}

QString OAIInvoice::getTaxCode() const {
    return m_tax_code;
}
void OAIInvoice::setTaxCode(const QString &tax_code) {
    m_tax_code = tax_code;
    m_tax_code_isSet = true;
}

bool OAIInvoice::is_tax_code_Set() const{
    return m_tax_code_isSet;
}

bool OAIInvoice::is_tax_code_Valid() const{
    return m_tax_code_isValid;
}

bool OAIInvoice::isTaxInclusive() const {
    return m_tax_inclusive;
}
void OAIInvoice::setTaxInclusive(const bool &tax_inclusive) {
    m_tax_inclusive = tax_inclusive;
    m_tax_inclusive_isSet = true;
}

bool OAIInvoice::is_tax_inclusive_Set() const{
    return m_tax_inclusive_isSet;
}

bool OAIInvoice::is_tax_inclusive_Valid() const{
    return m_tax_inclusive_isValid;
}

QString OAIInvoice::getTemplateId() const {
    return m_template_id;
}
void OAIInvoice::setTemplateId(const QString &template_id) {
    m_template_id = template_id;
    m_template_id_isSet = true;
}

bool OAIInvoice::is_template_id_Set() const{
    return m_template_id_isSet;
}

bool OAIInvoice::is_template_id_Valid() const{
    return m_template_id_isValid;
}

QString OAIInvoice::getTerms() const {
    return m_terms;
}
void OAIInvoice::setTerms(const QString &terms) {
    m_terms = terms;
    m_terms_isSet = true;
}

bool OAIInvoice::is_terms_Set() const{
    return m_terms_isSet;
}

bool OAIInvoice::is_terms_Valid() const{
    return m_terms_isValid;
}

double OAIInvoice::getTotal() const {
    return m_total;
}
void OAIInvoice::setTotal(const double &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIInvoice::is_total_Set() const{
    return m_total_isSet;
}

bool OAIInvoice::is_total_Valid() const{
    return m_total_isValid;
}

double OAIInvoice::getTotalTax() const {
    return m_total_tax;
}
void OAIInvoice::setTotalTax(const double &total_tax) {
    m_total_tax = total_tax;
    m_total_tax_isSet = true;
}

bool OAIInvoice::is_total_tax_Set() const{
    return m_total_tax_isSet;
}

bool OAIInvoice::is_total_tax_Valid() const{
    return m_total_tax_isValid;
}

OAILinkedTrackingCategory OAIInvoice::getTrackingCategory() const {
    return m_tracking_category;
}
void OAIInvoice::setTrackingCategory(const OAILinkedTrackingCategory &tracking_category) {
    m_tracking_category = tracking_category;
    m_tracking_category_isSet = true;
}

bool OAIInvoice::is_tracking_category_Set() const{
    return m_tracking_category_isSet;
}

bool OAIInvoice::is_tracking_category_Valid() const{
    return m_tracking_category_isValid;
}

QString OAIInvoice::getType() const {
    return m_type;
}
void OAIInvoice::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIInvoice::is_type_Set() const{
    return m_type_isSet;
}

bool OAIInvoice::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAIInvoice::getUpdatedAt() const {
    return m_updated_at;
}
void OAIInvoice::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIInvoice::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIInvoice::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIInvoice::getUpdatedBy() const {
    return m_updated_by;
}
void OAIInvoice::setUpdatedBy(const QString &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAIInvoice::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAIInvoice::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

bool OAIInvoice::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_accounting_by_row_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_balance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bank_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_channel_isSet) {
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

        if (m_customer_memo_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deposit_isSet) {
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

        if (m_downstream_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_due_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_sent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ledger_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_line_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_method_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_po_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_row_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_document_url_isSet) {
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

        if (m_template_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_terms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tracking_category.isSet()) {
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

bool OAIInvoice::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
