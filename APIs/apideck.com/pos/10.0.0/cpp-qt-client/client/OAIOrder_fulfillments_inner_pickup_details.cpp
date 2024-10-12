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

#include "OAIOrder_fulfillments_inner_pickup_details.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrder_fulfillments_inner_pickup_details::OAIOrder_fulfillments_inner_pickup_details(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrder_fulfillments_inner_pickup_details::OAIOrder_fulfillments_inner_pickup_details() {
    this->initializeModel();
}

OAIOrder_fulfillments_inner_pickup_details::~OAIOrder_fulfillments_inner_pickup_details() {}

void OAIOrder_fulfillments_inner_pickup_details::initializeModel() {

    m_accepted_at_isSet = false;
    m_accepted_at_isValid = false;

    m_auto_complete_duration_isSet = false;
    m_auto_complete_duration_isValid = false;

    m_cancel_reason_isSet = false;
    m_cancel_reason_isValid = false;

    m_canceled_at_isSet = false;
    m_canceled_at_isValid = false;

    m_curbside_pickup_details_isSet = false;
    m_curbside_pickup_details_isValid = false;

    m_expired_at_isSet = false;
    m_expired_at_isValid = false;

    m_expires_at_isSet = false;
    m_expires_at_isValid = false;

    m_is_curbside_pickup_isSet = false;
    m_is_curbside_pickup_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_picked_up_at_isSet = false;
    m_picked_up_at_isValid = false;

    m_pickup_at_isSet = false;
    m_pickup_at_isValid = false;

    m_pickup_window_duration_isSet = false;
    m_pickup_window_duration_isValid = false;

    m_placed_at_isSet = false;
    m_placed_at_isValid = false;

    m_prep_time_duration_isSet = false;
    m_prep_time_duration_isValid = false;

    m_ready_at_isSet = false;
    m_ready_at_isValid = false;

    m_recipient_isSet = false;
    m_recipient_isValid = false;

    m_rejected_at_isSet = false;
    m_rejected_at_isValid = false;

    m_schedule_type_isSet = false;
    m_schedule_type_isValid = false;
}

void OAIOrder_fulfillments_inner_pickup_details::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrder_fulfillments_inner_pickup_details::fromJsonObject(QJsonObject json) {

    m_accepted_at_isValid = ::OpenAPI::fromJsonValue(m_accepted_at, json[QString("accepted_at")]);
    m_accepted_at_isSet = !json[QString("accepted_at")].isNull() && m_accepted_at_isValid;

    m_auto_complete_duration_isValid = ::OpenAPI::fromJsonValue(m_auto_complete_duration, json[QString("auto_complete_duration")]);
    m_auto_complete_duration_isSet = !json[QString("auto_complete_duration")].isNull() && m_auto_complete_duration_isValid;

    m_cancel_reason_isValid = ::OpenAPI::fromJsonValue(m_cancel_reason, json[QString("cancel_reason")]);
    m_cancel_reason_isSet = !json[QString("cancel_reason")].isNull() && m_cancel_reason_isValid;

    m_canceled_at_isValid = ::OpenAPI::fromJsonValue(m_canceled_at, json[QString("canceled_at")]);
    m_canceled_at_isSet = !json[QString("canceled_at")].isNull() && m_canceled_at_isValid;

    m_curbside_pickup_details_isValid = ::OpenAPI::fromJsonValue(m_curbside_pickup_details, json[QString("curbside_pickup_details")]);
    m_curbside_pickup_details_isSet = !json[QString("curbside_pickup_details")].isNull() && m_curbside_pickup_details_isValid;

    m_expired_at_isValid = ::OpenAPI::fromJsonValue(m_expired_at, json[QString("expired_at")]);
    m_expired_at_isSet = !json[QString("expired_at")].isNull() && m_expired_at_isValid;

    m_expires_at_isValid = ::OpenAPI::fromJsonValue(m_expires_at, json[QString("expires_at")]);
    m_expires_at_isSet = !json[QString("expires_at")].isNull() && m_expires_at_isValid;

    m_is_curbside_pickup_isValid = ::OpenAPI::fromJsonValue(m_is_curbside_pickup, json[QString("is_curbside_pickup")]);
    m_is_curbside_pickup_isSet = !json[QString("is_curbside_pickup")].isNull() && m_is_curbside_pickup_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_picked_up_at_isValid = ::OpenAPI::fromJsonValue(m_picked_up_at, json[QString("picked_up_at")]);
    m_picked_up_at_isSet = !json[QString("picked_up_at")].isNull() && m_picked_up_at_isValid;

    m_pickup_at_isValid = ::OpenAPI::fromJsonValue(m_pickup_at, json[QString("pickup_at")]);
    m_pickup_at_isSet = !json[QString("pickup_at")].isNull() && m_pickup_at_isValid;

    m_pickup_window_duration_isValid = ::OpenAPI::fromJsonValue(m_pickup_window_duration, json[QString("pickup_window_duration")]);
    m_pickup_window_duration_isSet = !json[QString("pickup_window_duration")].isNull() && m_pickup_window_duration_isValid;

    m_placed_at_isValid = ::OpenAPI::fromJsonValue(m_placed_at, json[QString("placed_at")]);
    m_placed_at_isSet = !json[QString("placed_at")].isNull() && m_placed_at_isValid;

    m_prep_time_duration_isValid = ::OpenAPI::fromJsonValue(m_prep_time_duration, json[QString("prep_time_duration")]);
    m_prep_time_duration_isSet = !json[QString("prep_time_duration")].isNull() && m_prep_time_duration_isValid;

    m_ready_at_isValid = ::OpenAPI::fromJsonValue(m_ready_at, json[QString("ready_at")]);
    m_ready_at_isSet = !json[QString("ready_at")].isNull() && m_ready_at_isValid;

    m_recipient_isValid = ::OpenAPI::fromJsonValue(m_recipient, json[QString("recipient")]);
    m_recipient_isSet = !json[QString("recipient")].isNull() && m_recipient_isValid;

    m_rejected_at_isValid = ::OpenAPI::fromJsonValue(m_rejected_at, json[QString("rejected_at")]);
    m_rejected_at_isSet = !json[QString("rejected_at")].isNull() && m_rejected_at_isValid;

    m_schedule_type_isValid = ::OpenAPI::fromJsonValue(m_schedule_type, json[QString("schedule_type")]);
    m_schedule_type_isSet = !json[QString("schedule_type")].isNull() && m_schedule_type_isValid;
}

QString OAIOrder_fulfillments_inner_pickup_details::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrder_fulfillments_inner_pickup_details::asJsonObject() const {
    QJsonObject obj;
    if (m_accepted_at_isSet) {
        obj.insert(QString("accepted_at"), ::OpenAPI::toJsonValue(m_accepted_at));
    }
    if (m_auto_complete_duration_isSet) {
        obj.insert(QString("auto_complete_duration"), ::OpenAPI::toJsonValue(m_auto_complete_duration));
    }
    if (m_cancel_reason_isSet) {
        obj.insert(QString("cancel_reason"), ::OpenAPI::toJsonValue(m_cancel_reason));
    }
    if (m_canceled_at_isSet) {
        obj.insert(QString("canceled_at"), ::OpenAPI::toJsonValue(m_canceled_at));
    }
    if (m_curbside_pickup_details.isSet()) {
        obj.insert(QString("curbside_pickup_details"), ::OpenAPI::toJsonValue(m_curbside_pickup_details));
    }
    if (m_expired_at_isSet) {
        obj.insert(QString("expired_at"), ::OpenAPI::toJsonValue(m_expired_at));
    }
    if (m_expires_at_isSet) {
        obj.insert(QString("expires_at"), ::OpenAPI::toJsonValue(m_expires_at));
    }
    if (m_is_curbside_pickup_isSet) {
        obj.insert(QString("is_curbside_pickup"), ::OpenAPI::toJsonValue(m_is_curbside_pickup));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_picked_up_at_isSet) {
        obj.insert(QString("picked_up_at"), ::OpenAPI::toJsonValue(m_picked_up_at));
    }
    if (m_pickup_at_isSet) {
        obj.insert(QString("pickup_at"), ::OpenAPI::toJsonValue(m_pickup_at));
    }
    if (m_pickup_window_duration_isSet) {
        obj.insert(QString("pickup_window_duration"), ::OpenAPI::toJsonValue(m_pickup_window_duration));
    }
    if (m_placed_at_isSet) {
        obj.insert(QString("placed_at"), ::OpenAPI::toJsonValue(m_placed_at));
    }
    if (m_prep_time_duration_isSet) {
        obj.insert(QString("prep_time_duration"), ::OpenAPI::toJsonValue(m_prep_time_duration));
    }
    if (m_ready_at_isSet) {
        obj.insert(QString("ready_at"), ::OpenAPI::toJsonValue(m_ready_at));
    }
    if (m_recipient.isSet()) {
        obj.insert(QString("recipient"), ::OpenAPI::toJsonValue(m_recipient));
    }
    if (m_rejected_at_isSet) {
        obj.insert(QString("rejected_at"), ::OpenAPI::toJsonValue(m_rejected_at));
    }
    if (m_schedule_type_isSet) {
        obj.insert(QString("schedule_type"), ::OpenAPI::toJsonValue(m_schedule_type));
    }
    return obj;
}

QDateTime OAIOrder_fulfillments_inner_pickup_details::getAcceptedAt() const {
    return m_accepted_at;
}
void OAIOrder_fulfillments_inner_pickup_details::setAcceptedAt(const QDateTime &accepted_at) {
    m_accepted_at = accepted_at;
    m_accepted_at_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_accepted_at_Set() const{
    return m_accepted_at_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_accepted_at_Valid() const{
    return m_accepted_at_isValid;
}

QString OAIOrder_fulfillments_inner_pickup_details::getAutoCompleteDuration() const {
    return m_auto_complete_duration;
}
void OAIOrder_fulfillments_inner_pickup_details::setAutoCompleteDuration(const QString &auto_complete_duration) {
    m_auto_complete_duration = auto_complete_duration;
    m_auto_complete_duration_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_auto_complete_duration_Set() const{
    return m_auto_complete_duration_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_auto_complete_duration_Valid() const{
    return m_auto_complete_duration_isValid;
}

QString OAIOrder_fulfillments_inner_pickup_details::getCancelReason() const {
    return m_cancel_reason;
}
void OAIOrder_fulfillments_inner_pickup_details::setCancelReason(const QString &cancel_reason) {
    m_cancel_reason = cancel_reason;
    m_cancel_reason_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_cancel_reason_Set() const{
    return m_cancel_reason_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_cancel_reason_Valid() const{
    return m_cancel_reason_isValid;
}

QDateTime OAIOrder_fulfillments_inner_pickup_details::getCanceledAt() const {
    return m_canceled_at;
}
void OAIOrder_fulfillments_inner_pickup_details::setCanceledAt(const QDateTime &canceled_at) {
    m_canceled_at = canceled_at;
    m_canceled_at_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_canceled_at_Set() const{
    return m_canceled_at_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_canceled_at_Valid() const{
    return m_canceled_at_isValid;
}

OAIOrder_fulfillments_inner_pickup_details_curbside_pickup_details OAIOrder_fulfillments_inner_pickup_details::getCurbsidePickupDetails() const {
    return m_curbside_pickup_details;
}
void OAIOrder_fulfillments_inner_pickup_details::setCurbsidePickupDetails(const OAIOrder_fulfillments_inner_pickup_details_curbside_pickup_details &curbside_pickup_details) {
    m_curbside_pickup_details = curbside_pickup_details;
    m_curbside_pickup_details_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_curbside_pickup_details_Set() const{
    return m_curbside_pickup_details_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_curbside_pickup_details_Valid() const{
    return m_curbside_pickup_details_isValid;
}

QDateTime OAIOrder_fulfillments_inner_pickup_details::getExpiredAt() const {
    return m_expired_at;
}
void OAIOrder_fulfillments_inner_pickup_details::setExpiredAt(const QDateTime &expired_at) {
    m_expired_at = expired_at;
    m_expired_at_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_expired_at_Set() const{
    return m_expired_at_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_expired_at_Valid() const{
    return m_expired_at_isValid;
}

QDateTime OAIOrder_fulfillments_inner_pickup_details::getExpiresAt() const {
    return m_expires_at;
}
void OAIOrder_fulfillments_inner_pickup_details::setExpiresAt(const QDateTime &expires_at) {
    m_expires_at = expires_at;
    m_expires_at_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_expires_at_Set() const{
    return m_expires_at_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_expires_at_Valid() const{
    return m_expires_at_isValid;
}

bool OAIOrder_fulfillments_inner_pickup_details::isIsCurbsidePickup() const {
    return m_is_curbside_pickup;
}
void OAIOrder_fulfillments_inner_pickup_details::setIsCurbsidePickup(const bool &is_curbside_pickup) {
    m_is_curbside_pickup = is_curbside_pickup;
    m_is_curbside_pickup_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_is_curbside_pickup_Set() const{
    return m_is_curbside_pickup_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_is_curbside_pickup_Valid() const{
    return m_is_curbside_pickup_isValid;
}

QString OAIOrder_fulfillments_inner_pickup_details::getNote() const {
    return m_note;
}
void OAIOrder_fulfillments_inner_pickup_details::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_note_Set() const{
    return m_note_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_note_Valid() const{
    return m_note_isValid;
}

QDateTime OAIOrder_fulfillments_inner_pickup_details::getPickedUpAt() const {
    return m_picked_up_at;
}
void OAIOrder_fulfillments_inner_pickup_details::setPickedUpAt(const QDateTime &picked_up_at) {
    m_picked_up_at = picked_up_at;
    m_picked_up_at_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_picked_up_at_Set() const{
    return m_picked_up_at_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_picked_up_at_Valid() const{
    return m_picked_up_at_isValid;
}

QDateTime OAIOrder_fulfillments_inner_pickup_details::getPickupAt() const {
    return m_pickup_at;
}
void OAIOrder_fulfillments_inner_pickup_details::setPickupAt(const QDateTime &pickup_at) {
    m_pickup_at = pickup_at;
    m_pickup_at_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_pickup_at_Set() const{
    return m_pickup_at_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_pickup_at_Valid() const{
    return m_pickup_at_isValid;
}

QString OAIOrder_fulfillments_inner_pickup_details::getPickupWindowDuration() const {
    return m_pickup_window_duration;
}
void OAIOrder_fulfillments_inner_pickup_details::setPickupWindowDuration(const QString &pickup_window_duration) {
    m_pickup_window_duration = pickup_window_duration;
    m_pickup_window_duration_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_pickup_window_duration_Set() const{
    return m_pickup_window_duration_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_pickup_window_duration_Valid() const{
    return m_pickup_window_duration_isValid;
}

QDateTime OAIOrder_fulfillments_inner_pickup_details::getPlacedAt() const {
    return m_placed_at;
}
void OAIOrder_fulfillments_inner_pickup_details::setPlacedAt(const QDateTime &placed_at) {
    m_placed_at = placed_at;
    m_placed_at_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_placed_at_Set() const{
    return m_placed_at_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_placed_at_Valid() const{
    return m_placed_at_isValid;
}

QString OAIOrder_fulfillments_inner_pickup_details::getPrepTimeDuration() const {
    return m_prep_time_duration;
}
void OAIOrder_fulfillments_inner_pickup_details::setPrepTimeDuration(const QString &prep_time_duration) {
    m_prep_time_duration = prep_time_duration;
    m_prep_time_duration_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_prep_time_duration_Set() const{
    return m_prep_time_duration_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_prep_time_duration_Valid() const{
    return m_prep_time_duration_isValid;
}

QDateTime OAIOrder_fulfillments_inner_pickup_details::getReadyAt() const {
    return m_ready_at;
}
void OAIOrder_fulfillments_inner_pickup_details::setReadyAt(const QDateTime &ready_at) {
    m_ready_at = ready_at;
    m_ready_at_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_ready_at_Set() const{
    return m_ready_at_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_ready_at_Valid() const{
    return m_ready_at_isValid;
}

OAIOrder_fulfillments_inner_pickup_details_recipient OAIOrder_fulfillments_inner_pickup_details::getRecipient() const {
    return m_recipient;
}
void OAIOrder_fulfillments_inner_pickup_details::setRecipient(const OAIOrder_fulfillments_inner_pickup_details_recipient &recipient) {
    m_recipient = recipient;
    m_recipient_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_recipient_Set() const{
    return m_recipient_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_recipient_Valid() const{
    return m_recipient_isValid;
}

QDateTime OAIOrder_fulfillments_inner_pickup_details::getRejectedAt() const {
    return m_rejected_at;
}
void OAIOrder_fulfillments_inner_pickup_details::setRejectedAt(const QDateTime &rejected_at) {
    m_rejected_at = rejected_at;
    m_rejected_at_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_rejected_at_Set() const{
    return m_rejected_at_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_rejected_at_Valid() const{
    return m_rejected_at_isValid;
}

QString OAIOrder_fulfillments_inner_pickup_details::getScheduleType() const {
    return m_schedule_type;
}
void OAIOrder_fulfillments_inner_pickup_details::setScheduleType(const QString &schedule_type) {
    m_schedule_type = schedule_type;
    m_schedule_type_isSet = true;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_schedule_type_Set() const{
    return m_schedule_type_isSet;
}

bool OAIOrder_fulfillments_inner_pickup_details::is_schedule_type_Valid() const{
    return m_schedule_type_isValid;
}

bool OAIOrder_fulfillments_inner_pickup_details::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_accepted_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_auto_complete_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cancel_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_canceled_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_curbside_pickup_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_expired_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expires_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_curbside_pickup_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_picked_up_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pickup_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pickup_window_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_placed_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_prep_time_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ready_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recipient.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_rejected_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedule_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrder_fulfillments_inner_pickup_details::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
