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

#include "OAIItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIItem::OAIItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIItem::OAIItem() {
    this->initializeModel();
}

OAIItem::~OAIItem() {}

void OAIItem::initializeModel() {

    m_abbreviation_isSet = false;
    m_abbreviation_isValid = false;

    m_absent_at_location_ids_isSet = false;
    m_absent_at_location_ids_isValid = false;

    m_available_isSet = false;
    m_available_isValid = false;

    m_available_for_pickup_isSet = false;
    m_available_for_pickup_isValid = false;

    m_available_online_isSet = false;
    m_available_online_isValid = false;

    m_categories_isSet = false;
    m_categories_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_cost_isSet = false;
    m_cost_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_custom_mappings_isSet = false;
    m_custom_mappings_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_hidden_isSet = false;
    m_hidden_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_idempotency_key_isSet = false;
    m_idempotency_key_isValid = false;

    m_is_revenue_isSet = false;
    m_is_revenue_isValid = false;

    m_modifier_groups_isSet = false;
    m_modifier_groups_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_options_isSet = false;
    m_options_isValid = false;

    m_present_at_all_locations_isSet = false;
    m_present_at_all_locations_isValid = false;

    m_price_amount_isSet = false;
    m_price_amount_isValid = false;

    m_price_currency_isSet = false;
    m_price_currency_isValid = false;

    m_pricing_type_isSet = false;
    m_pricing_type_isValid = false;

    m_product_type_isSet = false;
    m_product_type_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;

    m_tax_ids_isSet = false;
    m_tax_ids_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;

    m_use_default_tax_rates_isSet = false;
    m_use_default_tax_rates_isValid = false;

    m_variations_isSet = false;
    m_variations_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIItem::fromJsonObject(QJsonObject json) {

    m_abbreviation_isValid = ::OpenAPI::fromJsonValue(m_abbreviation, json[QString("abbreviation")]);
    m_abbreviation_isSet = !json[QString("abbreviation")].isNull() && m_abbreviation_isValid;

    m_absent_at_location_ids_isValid = ::OpenAPI::fromJsonValue(m_absent_at_location_ids, json[QString("absent_at_location_ids")]);
    m_absent_at_location_ids_isSet = !json[QString("absent_at_location_ids")].isNull() && m_absent_at_location_ids_isValid;

    m_available_isValid = ::OpenAPI::fromJsonValue(m_available, json[QString("available")]);
    m_available_isSet = !json[QString("available")].isNull() && m_available_isValid;

    m_available_for_pickup_isValid = ::OpenAPI::fromJsonValue(m_available_for_pickup, json[QString("available_for_pickup")]);
    m_available_for_pickup_isSet = !json[QString("available_for_pickup")].isNull() && m_available_for_pickup_isValid;

    m_available_online_isValid = ::OpenAPI::fromJsonValue(m_available_online, json[QString("available_online")]);
    m_available_online_isSet = !json[QString("available_online")].isNull() && m_available_online_isValid;

    m_categories_isValid = ::OpenAPI::fromJsonValue(m_categories, json[QString("categories")]);
    m_categories_isSet = !json[QString("categories")].isNull() && m_categories_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_cost_isValid = ::OpenAPI::fromJsonValue(m_cost, json[QString("cost")]);
    m_cost_isSet = !json[QString("cost")].isNull() && m_cost_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_custom_mappings_isValid = ::OpenAPI::fromJsonValue(m_custom_mappings, json[QString("custom_mappings")]);
    m_custom_mappings_isSet = !json[QString("custom_mappings")].isNull() && m_custom_mappings_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_hidden_isValid = ::OpenAPI::fromJsonValue(m_hidden, json[QString("hidden")]);
    m_hidden_isSet = !json[QString("hidden")].isNull() && m_hidden_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_idempotency_key_isValid = ::OpenAPI::fromJsonValue(m_idempotency_key, json[QString("idempotency_key")]);
    m_idempotency_key_isSet = !json[QString("idempotency_key")].isNull() && m_idempotency_key_isValid;

    m_is_revenue_isValid = ::OpenAPI::fromJsonValue(m_is_revenue, json[QString("is_revenue")]);
    m_is_revenue_isSet = !json[QString("is_revenue")].isNull() && m_is_revenue_isValid;

    m_modifier_groups_isValid = ::OpenAPI::fromJsonValue(m_modifier_groups, json[QString("modifier_groups")]);
    m_modifier_groups_isSet = !json[QString("modifier_groups")].isNull() && m_modifier_groups_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_options_isValid = ::OpenAPI::fromJsonValue(m_options, json[QString("options")]);
    m_options_isSet = !json[QString("options")].isNull() && m_options_isValid;

    m_present_at_all_locations_isValid = ::OpenAPI::fromJsonValue(m_present_at_all_locations, json[QString("present_at_all_locations")]);
    m_present_at_all_locations_isSet = !json[QString("present_at_all_locations")].isNull() && m_present_at_all_locations_isValid;

    m_price_amount_isValid = ::OpenAPI::fromJsonValue(m_price_amount, json[QString("price_amount")]);
    m_price_amount_isSet = !json[QString("price_amount")].isNull() && m_price_amount_isValid;

    m_price_currency_isValid = ::OpenAPI::fromJsonValue(m_price_currency, json[QString("price_currency")]);
    m_price_currency_isSet = !json[QString("price_currency")].isNull() && m_price_currency_isValid;

    m_pricing_type_isValid = ::OpenAPI::fromJsonValue(m_pricing_type, json[QString("pricing_type")]);
    m_pricing_type_isSet = !json[QString("pricing_type")].isNull() && m_pricing_type_isValid;

    m_product_type_isValid = ::OpenAPI::fromJsonValue(m_product_type, json[QString("product_type")]);
    m_product_type_isSet = !json[QString("product_type")].isNull() && m_product_type_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;

    m_tax_ids_isValid = ::OpenAPI::fromJsonValue(m_tax_ids, json[QString("tax_ids")]);
    m_tax_ids_isSet = !json[QString("tax_ids")].isNull() && m_tax_ids_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updated_by")]);
    m_updated_by_isSet = !json[QString("updated_by")].isNull() && m_updated_by_isValid;

    m_use_default_tax_rates_isValid = ::OpenAPI::fromJsonValue(m_use_default_tax_rates, json[QString("use_default_tax_rates")]);
    m_use_default_tax_rates_isSet = !json[QString("use_default_tax_rates")].isNull() && m_use_default_tax_rates_isValid;

    m_variations_isValid = ::OpenAPI::fromJsonValue(m_variations, json[QString("variations")]);
    m_variations_isSet = !json[QString("variations")].isNull() && m_variations_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIItem::asJsonObject() const {
    QJsonObject obj;
    if (m_abbreviation_isSet) {
        obj.insert(QString("abbreviation"), ::OpenAPI::toJsonValue(m_abbreviation));
    }
    if (m_absent_at_location_ids.size() > 0) {
        obj.insert(QString("absent_at_location_ids"), ::OpenAPI::toJsonValue(m_absent_at_location_ids));
    }
    if (m_available_isSet) {
        obj.insert(QString("available"), ::OpenAPI::toJsonValue(m_available));
    }
    if (m_available_for_pickup_isSet) {
        obj.insert(QString("available_for_pickup"), ::OpenAPI::toJsonValue(m_available_for_pickup));
    }
    if (m_available_online_isSet) {
        obj.insert(QString("available_online"), ::OpenAPI::toJsonValue(m_available_online));
    }
    if (m_categories.size() > 0) {
        obj.insert(QString("categories"), ::OpenAPI::toJsonValue(m_categories));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_cost_isSet) {
        obj.insert(QString("cost"), ::OpenAPI::toJsonValue(m_cost));
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
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_hidden_isSet) {
        obj.insert(QString("hidden"), ::OpenAPI::toJsonValue(m_hidden));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_idempotency_key_isSet) {
        obj.insert(QString("idempotency_key"), ::OpenAPI::toJsonValue(m_idempotency_key));
    }
    if (m_is_revenue_isSet) {
        obj.insert(QString("is_revenue"), ::OpenAPI::toJsonValue(m_is_revenue));
    }
    if (m_modifier_groups.size() > 0) {
        obj.insert(QString("modifier_groups"), ::OpenAPI::toJsonValue(m_modifier_groups));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_options.size() > 0) {
        obj.insert(QString("options"), ::OpenAPI::toJsonValue(m_options));
    }
    if (m_present_at_all_locations_isSet) {
        obj.insert(QString("present_at_all_locations"), ::OpenAPI::toJsonValue(m_present_at_all_locations));
    }
    if (m_price_amount_isSet) {
        obj.insert(QString("price_amount"), ::OpenAPI::toJsonValue(m_price_amount));
    }
    if (m_price_currency.isSet()) {
        obj.insert(QString("price_currency"), ::OpenAPI::toJsonValue(m_price_currency));
    }
    if (m_pricing_type_isSet) {
        obj.insert(QString("pricing_type"), ::OpenAPI::toJsonValue(m_pricing_type));
    }
    if (m_product_type_isSet) {
        obj.insert(QString("product_type"), ::OpenAPI::toJsonValue(m_product_type));
    }
    if (m_sku_isSet) {
        obj.insert(QString("sku"), ::OpenAPI::toJsonValue(m_sku));
    }
    if (m_tax_ids.size() > 0) {
        obj.insert(QString("tax_ids"), ::OpenAPI::toJsonValue(m_tax_ids));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_updated_by_isSet) {
        obj.insert(QString("updated_by"), ::OpenAPI::toJsonValue(m_updated_by));
    }
    if (m_use_default_tax_rates_isSet) {
        obj.insert(QString("use_default_tax_rates"), ::OpenAPI::toJsonValue(m_use_default_tax_rates));
    }
    if (m_variations.size() > 0) {
        obj.insert(QString("variations"), ::OpenAPI::toJsonValue(m_variations));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QString OAIItem::getAbbreviation() const {
    return m_abbreviation;
}
void OAIItem::setAbbreviation(const QString &abbreviation) {
    m_abbreviation = abbreviation;
    m_abbreviation_isSet = true;
}

bool OAIItem::is_abbreviation_Set() const{
    return m_abbreviation_isSet;
}

bool OAIItem::is_abbreviation_Valid() const{
    return m_abbreviation_isValid;
}

QList<QString> OAIItem::getAbsentAtLocationIds() const {
    return m_absent_at_location_ids;
}
void OAIItem::setAbsentAtLocationIds(const QList<QString> &absent_at_location_ids) {
    m_absent_at_location_ids = absent_at_location_ids;
    m_absent_at_location_ids_isSet = true;
}

bool OAIItem::is_absent_at_location_ids_Set() const{
    return m_absent_at_location_ids_isSet;
}

bool OAIItem::is_absent_at_location_ids_Valid() const{
    return m_absent_at_location_ids_isValid;
}

bool OAIItem::isAvailable() const {
    return m_available;
}
void OAIItem::setAvailable(const bool &available) {
    m_available = available;
    m_available_isSet = true;
}

bool OAIItem::is_available_Set() const{
    return m_available_isSet;
}

bool OAIItem::is_available_Valid() const{
    return m_available_isValid;
}

bool OAIItem::isAvailableForPickup() const {
    return m_available_for_pickup;
}
void OAIItem::setAvailableForPickup(const bool &available_for_pickup) {
    m_available_for_pickup = available_for_pickup;
    m_available_for_pickup_isSet = true;
}

bool OAIItem::is_available_for_pickup_Set() const{
    return m_available_for_pickup_isSet;
}

bool OAIItem::is_available_for_pickup_Valid() const{
    return m_available_for_pickup_isValid;
}

bool OAIItem::isAvailableOnline() const {
    return m_available_online;
}
void OAIItem::setAvailableOnline(const bool &available_online) {
    m_available_online = available_online;
    m_available_online_isSet = true;
}

bool OAIItem::is_available_online_Set() const{
    return m_available_online_isSet;
}

bool OAIItem::is_available_online_Valid() const{
    return m_available_online_isValid;
}

QList<OAICategories_inner> OAIItem::getCategories() const {
    return m_categories;
}
void OAIItem::setCategories(const QList<OAICategories_inner> &categories) {
    m_categories = categories;
    m_categories_isSet = true;
}

bool OAIItem::is_categories_Set() const{
    return m_categories_isSet;
}

bool OAIItem::is_categories_Valid() const{
    return m_categories_isValid;
}

QString OAIItem::getCode() const {
    return m_code;
}
void OAIItem::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIItem::is_code_Set() const{
    return m_code_isSet;
}

bool OAIItem::is_code_Valid() const{
    return m_code_isValid;
}

double OAIItem::getCost() const {
    return m_cost;
}
void OAIItem::setCost(const double &cost) {
    m_cost = cost;
    m_cost_isSet = true;
}

bool OAIItem::is_cost_Set() const{
    return m_cost_isSet;
}

bool OAIItem::is_cost_Valid() const{
    return m_cost_isValid;
}

QDateTime OAIItem::getCreatedAt() const {
    return m_created_at;
}
void OAIItem::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIItem::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIItem::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIItem::getCreatedBy() const {
    return m_created_by;
}
void OAIItem::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIItem::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIItem::is_created_by_Valid() const{
    return m_created_by_isValid;
}

OAIObject OAIItem::getCustomMappings() const {
    return m_custom_mappings;
}
void OAIItem::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAIItem::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAIItem::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

bool OAIItem::isDeleted() const {
    return m_deleted;
}
void OAIItem::setDeleted(const bool &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIItem::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIItem::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIItem::getDescription() const {
    return m_description;
}
void OAIItem::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIItem::is_description_Set() const{
    return m_description_isSet;
}

bool OAIItem::is_description_Valid() const{
    return m_description_isValid;
}

bool OAIItem::isHidden() const {
    return m_hidden;
}
void OAIItem::setHidden(const bool &hidden) {
    m_hidden = hidden;
    m_hidden_isSet = true;
}

bool OAIItem::is_hidden_Set() const{
    return m_hidden_isSet;
}

bool OAIItem::is_hidden_Valid() const{
    return m_hidden_isValid;
}

QString OAIItem::getId() const {
    return m_id;
}
void OAIItem::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIItem::is_id_Set() const{
    return m_id_isSet;
}

bool OAIItem::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIItem::getIdempotencyKey() const {
    return m_idempotency_key;
}
void OAIItem::setIdempotencyKey(const QString &idempotency_key) {
    m_idempotency_key = idempotency_key;
    m_idempotency_key_isSet = true;
}

bool OAIItem::is_idempotency_key_Set() const{
    return m_idempotency_key_isSet;
}

bool OAIItem::is_idempotency_key_Valid() const{
    return m_idempotency_key_isValid;
}

bool OAIItem::isIsRevenue() const {
    return m_is_revenue;
}
void OAIItem::setIsRevenue(const bool &is_revenue) {
    m_is_revenue = is_revenue;
    m_is_revenue_isSet = true;
}

bool OAIItem::is_is_revenue_Set() const{
    return m_is_revenue_isSet;
}

bool OAIItem::is_is_revenue_Valid() const{
    return m_is_revenue_isValid;
}

QList<OAIVariations_inner> OAIItem::getModifierGroups() const {
    return m_modifier_groups;
}
void OAIItem::setModifierGroups(const QList<OAIVariations_inner> &modifier_groups) {
    m_modifier_groups = modifier_groups;
    m_modifier_groups_isSet = true;
}

bool OAIItem::is_modifier_groups_Set() const{
    return m_modifier_groups_isSet;
}

bool OAIItem::is_modifier_groups_Valid() const{
    return m_modifier_groups_isValid;
}

QString OAIItem::getName() const {
    return m_name;
}
void OAIItem::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIItem::is_name_Set() const{
    return m_name_isSet;
}

bool OAIItem::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIItem_options_inner> OAIItem::getOptions() const {
    return m_options;
}
void OAIItem::setOptions(const QList<OAIItem_options_inner> &options) {
    m_options = options;
    m_options_isSet = true;
}

bool OAIItem::is_options_Set() const{
    return m_options_isSet;
}

bool OAIItem::is_options_Valid() const{
    return m_options_isValid;
}

bool OAIItem::isPresentAtAllLocations() const {
    return m_present_at_all_locations;
}
void OAIItem::setPresentAtAllLocations(const bool &present_at_all_locations) {
    m_present_at_all_locations = present_at_all_locations;
    m_present_at_all_locations_isSet = true;
}

bool OAIItem::is_present_at_all_locations_Set() const{
    return m_present_at_all_locations_isSet;
}

bool OAIItem::is_present_at_all_locations_Valid() const{
    return m_present_at_all_locations_isValid;
}

double OAIItem::getPriceAmount() const {
    return m_price_amount;
}
void OAIItem::setPriceAmount(const double &price_amount) {
    m_price_amount = price_amount;
    m_price_amount_isSet = true;
}

bool OAIItem::is_price_amount_Set() const{
    return m_price_amount_isSet;
}

bool OAIItem::is_price_amount_Valid() const{
    return m_price_amount_isValid;
}

OAICurrency OAIItem::getPriceCurrency() const {
    return m_price_currency;
}
void OAIItem::setPriceCurrency(const OAICurrency &price_currency) {
    m_price_currency = price_currency;
    m_price_currency_isSet = true;
}

bool OAIItem::is_price_currency_Set() const{
    return m_price_currency_isSet;
}

bool OAIItem::is_price_currency_Valid() const{
    return m_price_currency_isValid;
}

QString OAIItem::getPricingType() const {
    return m_pricing_type;
}
void OAIItem::setPricingType(const QString &pricing_type) {
    m_pricing_type = pricing_type;
    m_pricing_type_isSet = true;
}

bool OAIItem::is_pricing_type_Set() const{
    return m_pricing_type_isSet;
}

bool OAIItem::is_pricing_type_Valid() const{
    return m_pricing_type_isValid;
}

QString OAIItem::getProductType() const {
    return m_product_type;
}
void OAIItem::setProductType(const QString &product_type) {
    m_product_type = product_type;
    m_product_type_isSet = true;
}

bool OAIItem::is_product_type_Set() const{
    return m_product_type_isSet;
}

bool OAIItem::is_product_type_Valid() const{
    return m_product_type_isValid;
}

QString OAIItem::getSku() const {
    return m_sku;
}
void OAIItem::setSku(const QString &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAIItem::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAIItem::is_sku_Valid() const{
    return m_sku_isValid;
}

QList<QString> OAIItem::getTaxIds() const {
    return m_tax_ids;
}
void OAIItem::setTaxIds(const QList<QString> &tax_ids) {
    m_tax_ids = tax_ids;
    m_tax_ids_isSet = true;
}

bool OAIItem::is_tax_ids_Set() const{
    return m_tax_ids_isSet;
}

bool OAIItem::is_tax_ids_Valid() const{
    return m_tax_ids_isValid;
}

QDateTime OAIItem::getUpdatedAt() const {
    return m_updated_at;
}
void OAIItem::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIItem::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIItem::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIItem::getUpdatedBy() const {
    return m_updated_by;
}
void OAIItem::setUpdatedBy(const QString &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAIItem::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAIItem::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

bool OAIItem::isUseDefaultTaxRates() const {
    return m_use_default_tax_rates;
}
void OAIItem::setUseDefaultTaxRates(const bool &use_default_tax_rates) {
    m_use_default_tax_rates = use_default_tax_rates;
    m_use_default_tax_rates_isSet = true;
}

bool OAIItem::is_use_default_tax_rates_Set() const{
    return m_use_default_tax_rates_isSet;
}

bool OAIItem::is_use_default_tax_rates_Valid() const{
    return m_use_default_tax_rates_isValid;
}

QList<OAIVariations_inner_1> OAIItem::getVariations() const {
    return m_variations;
}
void OAIItem::setVariations(const QList<OAIVariations_inner_1> &variations) {
    m_variations = variations;
    m_variations_isSet = true;
}

bool OAIItem::is_variations_Set() const{
    return m_variations_isSet;
}

bool OAIItem::is_variations_Valid() const{
    return m_variations_isValid;
}

QString OAIItem::getVersion() const {
    return m_version;
}
void OAIItem::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIItem::is_version_Set() const{
    return m_version_isSet;
}

bool OAIItem::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_abbreviation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_absent_at_location_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_available_for_pickup_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_available_online_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cost_isSet) {
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

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hidden_isSet) {
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

        if (m_is_revenue_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modifier_groups.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_options.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_present_at_all_locations_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_currency.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_pricing_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_ids.size() > 0) {
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

        if (m_use_default_tax_rates_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_variations.size() > 0) {
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

bool OAIItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
