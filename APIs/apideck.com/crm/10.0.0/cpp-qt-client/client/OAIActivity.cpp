/**
 * CRM API
 * Welcome to the CRM API.  You can use this API to access all CRM API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIActivity.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIActivity::OAIActivity(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIActivity::OAIActivity() {
    this->initializeModel();
}

OAIActivity::~OAIActivity() {}

void OAIActivity::initializeModel() {

    m_account_id_isSet = false;
    m_account_id_isValid = false;

    m_activity_date_isSet = false;
    m_activity_date_isValid = false;

    m_activity_datetime_isSet = false;
    m_activity_datetime_isValid = false;

    m_all_day_event_isSet = false;
    m_all_day_event_isValid = false;

    m_archived_isSet = false;
    m_archived_isValid = false;

    m_asset_id_isSet = false;
    m_asset_id_isValid = false;

    m_attendees_isSet = false;
    m_attendees_isValid = false;

    m_campaign_id_isSet = false;
    m_campaign_id_isValid = false;

    m_case_id_isSet = false;
    m_case_id_isValid = false;

    m_child_isSet = false;
    m_child_isValid = false;

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_contact_id_isSet = false;
    m_contact_id_isValid = false;

    m_contract_id_isSet = false;
    m_contract_id_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_custom_mappings_isSet = false;
    m_custom_mappings_isValid = false;

    m_custom_object_id_isSet = false;
    m_custom_object_id_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_done_isSet = false;
    m_done_isValid = false;

    m_downstream_id_isSet = false;
    m_downstream_id_isValid = false;

    m_duration_minutes_isSet = false;
    m_duration_minutes_isValid = false;

    m_duration_seconds_isSet = false;
    m_duration_seconds_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_end_datetime_isSet = false;
    m_end_datetime_isValid = false;

    m_event_sub_type_isSet = false;
    m_event_sub_type_isValid = false;

    m_group_event_isSet = false;
    m_group_event_isValid = false;

    m_group_event_type_isSet = false;
    m_group_event_type_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_lead_id_isSet = false;
    m_lead_id_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_location_address_isSet = false;
    m_location_address_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_opportunity_id_isSet = false;
    m_opportunity_id_isValid = false;

    m_owner_id_isSet = false;
    m_owner_id_isValid = false;

    m_r_private_isSet = false;
    m_r_private_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_recurrent_isSet = false;
    m_recurrent_isValid = false;

    m_reminder_datetime_isSet = false;
    m_reminder_datetime_isValid = false;

    m_reminder_set_isSet = false;
    m_reminder_set_isValid = false;

    m_show_as_isSet = false;
    m_show_as_isValid = false;

    m_solution_id_isSet = false;
    m_solution_id_isValid = false;

    m_start_datetime_isSet = false;
    m_start_datetime_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;

    m_video_conference_id_isSet = false;
    m_video_conference_id_isValid = false;

    m_video_conference_url_isSet = false;
    m_video_conference_url_isValid = false;
}

void OAIActivity::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIActivity::fromJsonObject(QJsonObject json) {

    m_account_id_isValid = ::OpenAPI::fromJsonValue(m_account_id, json[QString("account_id")]);
    m_account_id_isSet = !json[QString("account_id")].isNull() && m_account_id_isValid;

    m_activity_date_isValid = ::OpenAPI::fromJsonValue(m_activity_date, json[QString("activity_date")]);
    m_activity_date_isSet = !json[QString("activity_date")].isNull() && m_activity_date_isValid;

    m_activity_datetime_isValid = ::OpenAPI::fromJsonValue(m_activity_datetime, json[QString("activity_datetime")]);
    m_activity_datetime_isSet = !json[QString("activity_datetime")].isNull() && m_activity_datetime_isValid;

    m_all_day_event_isValid = ::OpenAPI::fromJsonValue(m_all_day_event, json[QString("all_day_event")]);
    m_all_day_event_isSet = !json[QString("all_day_event")].isNull() && m_all_day_event_isValid;

    m_archived_isValid = ::OpenAPI::fromJsonValue(m_archived, json[QString("archived")]);
    m_archived_isSet = !json[QString("archived")].isNull() && m_archived_isValid;

    m_asset_id_isValid = ::OpenAPI::fromJsonValue(m_asset_id, json[QString("asset_id")]);
    m_asset_id_isSet = !json[QString("asset_id")].isNull() && m_asset_id_isValid;

    m_attendees_isValid = ::OpenAPI::fromJsonValue(m_attendees, json[QString("attendees")]);
    m_attendees_isSet = !json[QString("attendees")].isNull() && m_attendees_isValid;

    m_campaign_id_isValid = ::OpenAPI::fromJsonValue(m_campaign_id, json[QString("campaign_id")]);
    m_campaign_id_isSet = !json[QString("campaign_id")].isNull() && m_campaign_id_isValid;

    m_case_id_isValid = ::OpenAPI::fromJsonValue(m_case_id, json[QString("case_id")]);
    m_case_id_isSet = !json[QString("case_id")].isNull() && m_case_id_isValid;

    m_child_isValid = ::OpenAPI::fromJsonValue(m_child, json[QString("child")]);
    m_child_isSet = !json[QString("child")].isNull() && m_child_isValid;

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("company_id")]);
    m_company_id_isSet = !json[QString("company_id")].isNull() && m_company_id_isValid;

    m_contact_id_isValid = ::OpenAPI::fromJsonValue(m_contact_id, json[QString("contact_id")]);
    m_contact_id_isSet = !json[QString("contact_id")].isNull() && m_contact_id_isValid;

    m_contract_id_isValid = ::OpenAPI::fromJsonValue(m_contract_id, json[QString("contract_id")]);
    m_contract_id_isSet = !json[QString("contract_id")].isNull() && m_contract_id_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_custom_mappings_isValid = ::OpenAPI::fromJsonValue(m_custom_mappings, json[QString("custom_mappings")]);
    m_custom_mappings_isSet = !json[QString("custom_mappings")].isNull() && m_custom_mappings_isValid;

    m_custom_object_id_isValid = ::OpenAPI::fromJsonValue(m_custom_object_id, json[QString("custom_object_id")]);
    m_custom_object_id_isSet = !json[QString("custom_object_id")].isNull() && m_custom_object_id_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_done_isValid = ::OpenAPI::fromJsonValue(m_done, json[QString("done")]);
    m_done_isSet = !json[QString("done")].isNull() && m_done_isValid;

    m_downstream_id_isValid = ::OpenAPI::fromJsonValue(m_downstream_id, json[QString("downstream_id")]);
    m_downstream_id_isSet = !json[QString("downstream_id")].isNull() && m_downstream_id_isValid;

    m_duration_minutes_isValid = ::OpenAPI::fromJsonValue(m_duration_minutes, json[QString("duration_minutes")]);
    m_duration_minutes_isSet = !json[QString("duration_minutes")].isNull() && m_duration_minutes_isValid;

    m_duration_seconds_isValid = ::OpenAPI::fromJsonValue(m_duration_seconds, json[QString("duration_seconds")]);
    m_duration_seconds_isSet = !json[QString("duration_seconds")].isNull() && m_duration_seconds_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("end_date")]);
    m_end_date_isSet = !json[QString("end_date")].isNull() && m_end_date_isValid;

    m_end_datetime_isValid = ::OpenAPI::fromJsonValue(m_end_datetime, json[QString("end_datetime")]);
    m_end_datetime_isSet = !json[QString("end_datetime")].isNull() && m_end_datetime_isValid;

    m_event_sub_type_isValid = ::OpenAPI::fromJsonValue(m_event_sub_type, json[QString("event_sub_type")]);
    m_event_sub_type_isSet = !json[QString("event_sub_type")].isNull() && m_event_sub_type_isValid;

    m_group_event_isValid = ::OpenAPI::fromJsonValue(m_group_event, json[QString("group_event")]);
    m_group_event_isSet = !json[QString("group_event")].isNull() && m_group_event_isValid;

    m_group_event_type_isValid = ::OpenAPI::fromJsonValue(m_group_event_type, json[QString("group_event_type")]);
    m_group_event_type_isSet = !json[QString("group_event_type")].isNull() && m_group_event_type_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_lead_id_isValid = ::OpenAPI::fromJsonValue(m_lead_id, json[QString("lead_id")]);
    m_lead_id_isSet = !json[QString("lead_id")].isNull() && m_lead_id_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_location_address_isValid = ::OpenAPI::fromJsonValue(m_location_address, json[QString("location_address")]);
    m_location_address_isSet = !json[QString("location_address")].isNull() && m_location_address_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_opportunity_id_isValid = ::OpenAPI::fromJsonValue(m_opportunity_id, json[QString("opportunity_id")]);
    m_opportunity_id_isSet = !json[QString("opportunity_id")].isNull() && m_opportunity_id_isValid;

    m_owner_id_isValid = ::OpenAPI::fromJsonValue(m_owner_id, json[QString("owner_id")]);
    m_owner_id_isSet = !json[QString("owner_id")].isNull() && m_owner_id_isValid;

    m_r_private_isValid = ::OpenAPI::fromJsonValue(m_r_private, json[QString("private")]);
    m_r_private_isSet = !json[QString("private")].isNull() && m_r_private_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("product_id")]);
    m_product_id_isSet = !json[QString("product_id")].isNull() && m_product_id_isValid;

    m_recurrent_isValid = ::OpenAPI::fromJsonValue(m_recurrent, json[QString("recurrent")]);
    m_recurrent_isSet = !json[QString("recurrent")].isNull() && m_recurrent_isValid;

    m_reminder_datetime_isValid = ::OpenAPI::fromJsonValue(m_reminder_datetime, json[QString("reminder_datetime")]);
    m_reminder_datetime_isSet = !json[QString("reminder_datetime")].isNull() && m_reminder_datetime_isValid;

    m_reminder_set_isValid = ::OpenAPI::fromJsonValue(m_reminder_set, json[QString("reminder_set")]);
    m_reminder_set_isSet = !json[QString("reminder_set")].isNull() && m_reminder_set_isValid;

    m_show_as_isValid = ::OpenAPI::fromJsonValue(m_show_as, json[QString("show_as")]);
    m_show_as_isSet = !json[QString("show_as")].isNull() && m_show_as_isValid;

    m_solution_id_isValid = ::OpenAPI::fromJsonValue(m_solution_id, json[QString("solution_id")]);
    m_solution_id_isSet = !json[QString("solution_id")].isNull() && m_solution_id_isValid;

    m_start_datetime_isValid = ::OpenAPI::fromJsonValue(m_start_datetime, json[QString("start_datetime")]);
    m_start_datetime_isSet = !json[QString("start_datetime")].isNull() && m_start_datetime_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updated_by")]);
    m_updated_by_isSet = !json[QString("updated_by")].isNull() && m_updated_by_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;

    m_video_conference_id_isValid = ::OpenAPI::fromJsonValue(m_video_conference_id, json[QString("video_conference_id")]);
    m_video_conference_id_isSet = !json[QString("video_conference_id")].isNull() && m_video_conference_id_isValid;

    m_video_conference_url_isValid = ::OpenAPI::fromJsonValue(m_video_conference_url, json[QString("video_conference_url")]);
    m_video_conference_url_isSet = !json[QString("video_conference_url")].isNull() && m_video_conference_url_isValid;
}

QString OAIActivity::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIActivity::asJsonObject() const {
    QJsonObject obj;
    if (m_account_id_isSet) {
        obj.insert(QString("account_id"), ::OpenAPI::toJsonValue(m_account_id));
    }
    if (m_activity_date_isSet) {
        obj.insert(QString("activity_date"), ::OpenAPI::toJsonValue(m_activity_date));
    }
    if (m_activity_datetime_isSet) {
        obj.insert(QString("activity_datetime"), ::OpenAPI::toJsonValue(m_activity_datetime));
    }
    if (m_all_day_event_isSet) {
        obj.insert(QString("all_day_event"), ::OpenAPI::toJsonValue(m_all_day_event));
    }
    if (m_archived_isSet) {
        obj.insert(QString("archived"), ::OpenAPI::toJsonValue(m_archived));
    }
    if (m_asset_id_isSet) {
        obj.insert(QString("asset_id"), ::OpenAPI::toJsonValue(m_asset_id));
    }
    if (m_attendees.size() > 0) {
        obj.insert(QString("attendees"), ::OpenAPI::toJsonValue(m_attendees));
    }
    if (m_campaign_id_isSet) {
        obj.insert(QString("campaign_id"), ::OpenAPI::toJsonValue(m_campaign_id));
    }
    if (m_case_id_isSet) {
        obj.insert(QString("case_id"), ::OpenAPI::toJsonValue(m_case_id));
    }
    if (m_child_isSet) {
        obj.insert(QString("child"), ::OpenAPI::toJsonValue(m_child));
    }
    if (m_company_id_isSet) {
        obj.insert(QString("company_id"), ::OpenAPI::toJsonValue(m_company_id));
    }
    if (m_contact_id_isSet) {
        obj.insert(QString("contact_id"), ::OpenAPI::toJsonValue(m_contact_id));
    }
    if (m_contract_id_isSet) {
        obj.insert(QString("contract_id"), ::OpenAPI::toJsonValue(m_contract_id));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_created_by_isSet) {
        obj.insert(QString("created_by"), ::OpenAPI::toJsonValue(m_created_by));
    }
    if (m_custom_fields.size() > 0) {
        obj.insert(QString("custom_fields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_custom_mappings_isSet) {
        obj.insert(QString("custom_mappings"), ::OpenAPI::toJsonValue(m_custom_mappings));
    }
    if (m_custom_object_id_isSet) {
        obj.insert(QString("custom_object_id"), ::OpenAPI::toJsonValue(m_custom_object_id));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_done_isSet) {
        obj.insert(QString("done"), ::OpenAPI::toJsonValue(m_done));
    }
    if (m_downstream_id_isSet) {
        obj.insert(QString("downstream_id"), ::OpenAPI::toJsonValue(m_downstream_id));
    }
    if (m_duration_minutes_isSet) {
        obj.insert(QString("duration_minutes"), ::OpenAPI::toJsonValue(m_duration_minutes));
    }
    if (m_duration_seconds_isSet) {
        obj.insert(QString("duration_seconds"), ::OpenAPI::toJsonValue(m_duration_seconds));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("end_date"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_end_datetime_isSet) {
        obj.insert(QString("end_datetime"), ::OpenAPI::toJsonValue(m_end_datetime));
    }
    if (m_event_sub_type_isSet) {
        obj.insert(QString("event_sub_type"), ::OpenAPI::toJsonValue(m_event_sub_type));
    }
    if (m_group_event_isSet) {
        obj.insert(QString("group_event"), ::OpenAPI::toJsonValue(m_group_event));
    }
    if (m_group_event_type_isSet) {
        obj.insert(QString("group_event_type"), ::OpenAPI::toJsonValue(m_group_event_type));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_lead_id_isSet) {
        obj.insert(QString("lead_id"), ::OpenAPI::toJsonValue(m_lead_id));
    }
    if (m_location_isSet) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_location_address.isSet()) {
        obj.insert(QString("location_address"), ::OpenAPI::toJsonValue(m_location_address));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_opportunity_id_isSet) {
        obj.insert(QString("opportunity_id"), ::OpenAPI::toJsonValue(m_opportunity_id));
    }
    if (m_owner_id_isSet) {
        obj.insert(QString("owner_id"), ::OpenAPI::toJsonValue(m_owner_id));
    }
    if (m_r_private_isSet) {
        obj.insert(QString("private"), ::OpenAPI::toJsonValue(m_r_private));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("product_id"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_recurrent_isSet) {
        obj.insert(QString("recurrent"), ::OpenAPI::toJsonValue(m_recurrent));
    }
    if (m_reminder_datetime_isSet) {
        obj.insert(QString("reminder_datetime"), ::OpenAPI::toJsonValue(m_reminder_datetime));
    }
    if (m_reminder_set_isSet) {
        obj.insert(QString("reminder_set"), ::OpenAPI::toJsonValue(m_reminder_set));
    }
    if (m_show_as_isSet) {
        obj.insert(QString("show_as"), ::OpenAPI::toJsonValue(m_show_as));
    }
    if (m_solution_id_isSet) {
        obj.insert(QString("solution_id"), ::OpenAPI::toJsonValue(m_solution_id));
    }
    if (m_start_datetime_isSet) {
        obj.insert(QString("start_datetime"), ::OpenAPI::toJsonValue(m_start_datetime));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
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
    if (m_user_id_isSet) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    if (m_video_conference_id_isSet) {
        obj.insert(QString("video_conference_id"), ::OpenAPI::toJsonValue(m_video_conference_id));
    }
    if (m_video_conference_url_isSet) {
        obj.insert(QString("video_conference_url"), ::OpenAPI::toJsonValue(m_video_conference_url));
    }
    return obj;
}

QString OAIActivity::getAccountId() const {
    return m_account_id;
}
void OAIActivity::setAccountId(const QString &account_id) {
    m_account_id = account_id;
    m_account_id_isSet = true;
}

bool OAIActivity::is_account_id_Set() const{
    return m_account_id_isSet;
}

bool OAIActivity::is_account_id_Valid() const{
    return m_account_id_isValid;
}

QString OAIActivity::getActivityDate() const {
    return m_activity_date;
}
void OAIActivity::setActivityDate(const QString &activity_date) {
    m_activity_date = activity_date;
    m_activity_date_isSet = true;
}

bool OAIActivity::is_activity_date_Set() const{
    return m_activity_date_isSet;
}

bool OAIActivity::is_activity_date_Valid() const{
    return m_activity_date_isValid;
}

QString OAIActivity::getActivityDatetime() const {
    return m_activity_datetime;
}
void OAIActivity::setActivityDatetime(const QString &activity_datetime) {
    m_activity_datetime = activity_datetime;
    m_activity_datetime_isSet = true;
}

bool OAIActivity::is_activity_datetime_Set() const{
    return m_activity_datetime_isSet;
}

bool OAIActivity::is_activity_datetime_Valid() const{
    return m_activity_datetime_isValid;
}

bool OAIActivity::isAllDayEvent() const {
    return m_all_day_event;
}
void OAIActivity::setAllDayEvent(const bool &all_day_event) {
    m_all_day_event = all_day_event;
    m_all_day_event_isSet = true;
}

bool OAIActivity::is_all_day_event_Set() const{
    return m_all_day_event_isSet;
}

bool OAIActivity::is_all_day_event_Valid() const{
    return m_all_day_event_isValid;
}

bool OAIActivity::isArchived() const {
    return m_archived;
}
void OAIActivity::setArchived(const bool &archived) {
    m_archived = archived;
    m_archived_isSet = true;
}

bool OAIActivity::is_archived_Set() const{
    return m_archived_isSet;
}

bool OAIActivity::is_archived_Valid() const{
    return m_archived_isValid;
}

QString OAIActivity::getAssetId() const {
    return m_asset_id;
}
void OAIActivity::setAssetId(const QString &asset_id) {
    m_asset_id = asset_id;
    m_asset_id_isSet = true;
}

bool OAIActivity::is_asset_id_Set() const{
    return m_asset_id_isSet;
}

bool OAIActivity::is_asset_id_Valid() const{
    return m_asset_id_isValid;
}

QList<OAIActivityAttendee> OAIActivity::getAttendees() const {
    return m_attendees;
}
void OAIActivity::setAttendees(const QList<OAIActivityAttendee> &attendees) {
    m_attendees = attendees;
    m_attendees_isSet = true;
}

bool OAIActivity::is_attendees_Set() const{
    return m_attendees_isSet;
}

bool OAIActivity::is_attendees_Valid() const{
    return m_attendees_isValid;
}

QString OAIActivity::getCampaignId() const {
    return m_campaign_id;
}
void OAIActivity::setCampaignId(const QString &campaign_id) {
    m_campaign_id = campaign_id;
    m_campaign_id_isSet = true;
}

bool OAIActivity::is_campaign_id_Set() const{
    return m_campaign_id_isSet;
}

bool OAIActivity::is_campaign_id_Valid() const{
    return m_campaign_id_isValid;
}

QString OAIActivity::getCaseId() const {
    return m_case_id;
}
void OAIActivity::setCaseId(const QString &case_id) {
    m_case_id = case_id;
    m_case_id_isSet = true;
}

bool OAIActivity::is_case_id_Set() const{
    return m_case_id_isSet;
}

bool OAIActivity::is_case_id_Valid() const{
    return m_case_id_isValid;
}

bool OAIActivity::isChild() const {
    return m_child;
}
void OAIActivity::setChild(const bool &child) {
    m_child = child;
    m_child_isSet = true;
}

bool OAIActivity::is_child_Set() const{
    return m_child_isSet;
}

bool OAIActivity::is_child_Valid() const{
    return m_child_isValid;
}

QString OAIActivity::getCompanyId() const {
    return m_company_id;
}
void OAIActivity::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIActivity::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIActivity::is_company_id_Valid() const{
    return m_company_id_isValid;
}

QString OAIActivity::getContactId() const {
    return m_contact_id;
}
void OAIActivity::setContactId(const QString &contact_id) {
    m_contact_id = contact_id;
    m_contact_id_isSet = true;
}

bool OAIActivity::is_contact_id_Set() const{
    return m_contact_id_isSet;
}

bool OAIActivity::is_contact_id_Valid() const{
    return m_contact_id_isValid;
}

QString OAIActivity::getContractId() const {
    return m_contract_id;
}
void OAIActivity::setContractId(const QString &contract_id) {
    m_contract_id = contract_id;
    m_contract_id_isSet = true;
}

bool OAIActivity::is_contract_id_Set() const{
    return m_contract_id_isSet;
}

bool OAIActivity::is_contract_id_Valid() const{
    return m_contract_id_isValid;
}

QString OAIActivity::getCreatedAt() const {
    return m_created_at;
}
void OAIActivity::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIActivity::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIActivity::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIActivity::getCreatedBy() const {
    return m_created_by;
}
void OAIActivity::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIActivity::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIActivity::is_created_by_Valid() const{
    return m_created_by_isValid;
}

QList<OAICustomField> OAIActivity::getCustomFields() const {
    return m_custom_fields;
}
void OAIActivity::setCustomFields(const QList<OAICustomField> &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIActivity::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIActivity::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

OAIObject OAIActivity::getCustomMappings() const {
    return m_custom_mappings;
}
void OAIActivity::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAIActivity::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAIActivity::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

QString OAIActivity::getCustomObjectId() const {
    return m_custom_object_id;
}
void OAIActivity::setCustomObjectId(const QString &custom_object_id) {
    m_custom_object_id = custom_object_id;
    m_custom_object_id_isSet = true;
}

bool OAIActivity::is_custom_object_id_Set() const{
    return m_custom_object_id_isSet;
}

bool OAIActivity::is_custom_object_id_Valid() const{
    return m_custom_object_id_isValid;
}

bool OAIActivity::isDeleted() const {
    return m_deleted;
}
void OAIActivity::setDeleted(const bool &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIActivity::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIActivity::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIActivity::getDescription() const {
    return m_description;
}
void OAIActivity::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIActivity::is_description_Set() const{
    return m_description_isSet;
}

bool OAIActivity::is_description_Valid() const{
    return m_description_isValid;
}

bool OAIActivity::isDone() const {
    return m_done;
}
void OAIActivity::setDone(const bool &done) {
    m_done = done;
    m_done_isSet = true;
}

bool OAIActivity::is_done_Set() const{
    return m_done_isSet;
}

bool OAIActivity::is_done_Valid() const{
    return m_done_isValid;
}

QString OAIActivity::getDownstreamId() const {
    return m_downstream_id;
}
void OAIActivity::setDownstreamId(const QString &downstream_id) {
    m_downstream_id = downstream_id;
    m_downstream_id_isSet = true;
}

bool OAIActivity::is_downstream_id_Set() const{
    return m_downstream_id_isSet;
}

bool OAIActivity::is_downstream_id_Valid() const{
    return m_downstream_id_isValid;
}

qint32 OAIActivity::getDurationMinutes() const {
    return m_duration_minutes;
}
void OAIActivity::setDurationMinutes(const qint32 &duration_minutes) {
    m_duration_minutes = duration_minutes;
    m_duration_minutes_isSet = true;
}

bool OAIActivity::is_duration_minutes_Set() const{
    return m_duration_minutes_isSet;
}

bool OAIActivity::is_duration_minutes_Valid() const{
    return m_duration_minutes_isValid;
}

qint32 OAIActivity::getDurationSeconds() const {
    return m_duration_seconds;
}
void OAIActivity::setDurationSeconds(const qint32 &duration_seconds) {
    m_duration_seconds = duration_seconds;
    m_duration_seconds_isSet = true;
}

bool OAIActivity::is_duration_seconds_Set() const{
    return m_duration_seconds_isSet;
}

bool OAIActivity::is_duration_seconds_Valid() const{
    return m_duration_seconds_isValid;
}

QString OAIActivity::getEndDate() const {
    return m_end_date;
}
void OAIActivity::setEndDate(const QString &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIActivity::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIActivity::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QString OAIActivity::getEndDatetime() const {
    return m_end_datetime;
}
void OAIActivity::setEndDatetime(const QString &end_datetime) {
    m_end_datetime = end_datetime;
    m_end_datetime_isSet = true;
}

bool OAIActivity::is_end_datetime_Set() const{
    return m_end_datetime_isSet;
}

bool OAIActivity::is_end_datetime_Valid() const{
    return m_end_datetime_isValid;
}

QString OAIActivity::getEventSubType() const {
    return m_event_sub_type;
}
void OAIActivity::setEventSubType(const QString &event_sub_type) {
    m_event_sub_type = event_sub_type;
    m_event_sub_type_isSet = true;
}

bool OAIActivity::is_event_sub_type_Set() const{
    return m_event_sub_type_isSet;
}

bool OAIActivity::is_event_sub_type_Valid() const{
    return m_event_sub_type_isValid;
}

bool OAIActivity::isGroupEvent() const {
    return m_group_event;
}
void OAIActivity::setGroupEvent(const bool &group_event) {
    m_group_event = group_event;
    m_group_event_isSet = true;
}

bool OAIActivity::is_group_event_Set() const{
    return m_group_event_isSet;
}

bool OAIActivity::is_group_event_Valid() const{
    return m_group_event_isValid;
}

QString OAIActivity::getGroupEventType() const {
    return m_group_event_type;
}
void OAIActivity::setGroupEventType(const QString &group_event_type) {
    m_group_event_type = group_event_type;
    m_group_event_type_isSet = true;
}

bool OAIActivity::is_group_event_type_Set() const{
    return m_group_event_type_isSet;
}

bool OAIActivity::is_group_event_type_Valid() const{
    return m_group_event_type_isValid;
}

QString OAIActivity::getId() const {
    return m_id;
}
void OAIActivity::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIActivity::is_id_Set() const{
    return m_id_isSet;
}

bool OAIActivity::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIActivity::getLeadId() const {
    return m_lead_id;
}
void OAIActivity::setLeadId(const QString &lead_id) {
    m_lead_id = lead_id;
    m_lead_id_isSet = true;
}

bool OAIActivity::is_lead_id_Set() const{
    return m_lead_id_isSet;
}

bool OAIActivity::is_lead_id_Valid() const{
    return m_lead_id_isValid;
}

QString OAIActivity::getLocation() const {
    return m_location;
}
void OAIActivity::setLocation(const QString &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAIActivity::is_location_Set() const{
    return m_location_isSet;
}

bool OAIActivity::is_location_Valid() const{
    return m_location_isValid;
}

OAIAddress OAIActivity::getLocationAddress() const {
    return m_location_address;
}
void OAIActivity::setLocationAddress(const OAIAddress &location_address) {
    m_location_address = location_address;
    m_location_address_isSet = true;
}

bool OAIActivity::is_location_address_Set() const{
    return m_location_address_isSet;
}

bool OAIActivity::is_location_address_Valid() const{
    return m_location_address_isValid;
}

QString OAIActivity::getNote() const {
    return m_note;
}
void OAIActivity::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAIActivity::is_note_Set() const{
    return m_note_isSet;
}

bool OAIActivity::is_note_Valid() const{
    return m_note_isValid;
}

QString OAIActivity::getOpportunityId() const {
    return m_opportunity_id;
}
void OAIActivity::setOpportunityId(const QString &opportunity_id) {
    m_opportunity_id = opportunity_id;
    m_opportunity_id_isSet = true;
}

bool OAIActivity::is_opportunity_id_Set() const{
    return m_opportunity_id_isSet;
}

bool OAIActivity::is_opportunity_id_Valid() const{
    return m_opportunity_id_isValid;
}

QString OAIActivity::getOwnerId() const {
    return m_owner_id;
}
void OAIActivity::setOwnerId(const QString &owner_id) {
    m_owner_id = owner_id;
    m_owner_id_isSet = true;
}

bool OAIActivity::is_owner_id_Set() const{
    return m_owner_id_isSet;
}

bool OAIActivity::is_owner_id_Valid() const{
    return m_owner_id_isValid;
}

bool OAIActivity::isRPrivate() const {
    return m_r_private;
}
void OAIActivity::setRPrivate(const bool &r_private) {
    m_r_private = r_private;
    m_r_private_isSet = true;
}

bool OAIActivity::is_r_private_Set() const{
    return m_r_private_isSet;
}

bool OAIActivity::is_r_private_Valid() const{
    return m_r_private_isValid;
}

QString OAIActivity::getProductId() const {
    return m_product_id;
}
void OAIActivity::setProductId(const QString &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAIActivity::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAIActivity::is_product_id_Valid() const{
    return m_product_id_isValid;
}

bool OAIActivity::isRecurrent() const {
    return m_recurrent;
}
void OAIActivity::setRecurrent(const bool &recurrent) {
    m_recurrent = recurrent;
    m_recurrent_isSet = true;
}

bool OAIActivity::is_recurrent_Set() const{
    return m_recurrent_isSet;
}

bool OAIActivity::is_recurrent_Valid() const{
    return m_recurrent_isValid;
}

QString OAIActivity::getReminderDatetime() const {
    return m_reminder_datetime;
}
void OAIActivity::setReminderDatetime(const QString &reminder_datetime) {
    m_reminder_datetime = reminder_datetime;
    m_reminder_datetime_isSet = true;
}

bool OAIActivity::is_reminder_datetime_Set() const{
    return m_reminder_datetime_isSet;
}

bool OAIActivity::is_reminder_datetime_Valid() const{
    return m_reminder_datetime_isValid;
}

bool OAIActivity::isReminderSet() const {
    return m_reminder_set;
}
void OAIActivity::setReminderSet(const bool &reminder_set) {
    m_reminder_set = reminder_set;
    m_reminder_set_isSet = true;
}

bool OAIActivity::is_reminder_set_Set() const{
    return m_reminder_set_isSet;
}

bool OAIActivity::is_reminder_set_Valid() const{
    return m_reminder_set_isValid;
}

QString OAIActivity::getShowAs() const {
    return m_show_as;
}
void OAIActivity::setShowAs(const QString &show_as) {
    m_show_as = show_as;
    m_show_as_isSet = true;
}

bool OAIActivity::is_show_as_Set() const{
    return m_show_as_isSet;
}

bool OAIActivity::is_show_as_Valid() const{
    return m_show_as_isValid;
}

QString OAIActivity::getSolutionId() const {
    return m_solution_id;
}
void OAIActivity::setSolutionId(const QString &solution_id) {
    m_solution_id = solution_id;
    m_solution_id_isSet = true;
}

bool OAIActivity::is_solution_id_Set() const{
    return m_solution_id_isSet;
}

bool OAIActivity::is_solution_id_Valid() const{
    return m_solution_id_isValid;
}

QString OAIActivity::getStartDatetime() const {
    return m_start_datetime;
}
void OAIActivity::setStartDatetime(const QString &start_datetime) {
    m_start_datetime = start_datetime;
    m_start_datetime_isSet = true;
}

bool OAIActivity::is_start_datetime_Set() const{
    return m_start_datetime_isSet;
}

bool OAIActivity::is_start_datetime_Valid() const{
    return m_start_datetime_isValid;
}

QString OAIActivity::getTitle() const {
    return m_title;
}
void OAIActivity::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIActivity::is_title_Set() const{
    return m_title_isSet;
}

bool OAIActivity::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIActivity::getType() const {
    return m_type;
}
void OAIActivity::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIActivity::is_type_Set() const{
    return m_type_isSet;
}

bool OAIActivity::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIActivity::getUpdatedAt() const {
    return m_updated_at;
}
void OAIActivity::setUpdatedAt(const QString &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIActivity::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIActivity::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIActivity::getUpdatedBy() const {
    return m_updated_by;
}
void OAIActivity::setUpdatedBy(const QString &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAIActivity::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAIActivity::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

QString OAIActivity::getUserId() const {
    return m_user_id;
}
void OAIActivity::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIActivity::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIActivity::is_user_id_Valid() const{
    return m_user_id_isValid;
}

QString OAIActivity::getVideoConferenceId() const {
    return m_video_conference_id;
}
void OAIActivity::setVideoConferenceId(const QString &video_conference_id) {
    m_video_conference_id = video_conference_id;
    m_video_conference_id_isSet = true;
}

bool OAIActivity::is_video_conference_id_Set() const{
    return m_video_conference_id_isSet;
}

bool OAIActivity::is_video_conference_id_Valid() const{
    return m_video_conference_id_isValid;
}

QString OAIActivity::getVideoConferenceUrl() const {
    return m_video_conference_url;
}
void OAIActivity::setVideoConferenceUrl(const QString &video_conference_url) {
    m_video_conference_url = video_conference_url;
    m_video_conference_url_isSet = true;
}

bool OAIActivity::is_video_conference_url_Set() const{
    return m_video_conference_url_isSet;
}

bool OAIActivity::is_video_conference_url_Valid() const{
    return m_video_conference_url_isValid;
}

bool OAIActivity::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_activity_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_activity_datetime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_all_day_event_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_archived_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_asset_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_attendees.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_campaign_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_case_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_child_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contact_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contract_id_isSet) {
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

        if (m_custom_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_mappings_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_object_id_isSet) {
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

        if (m_done_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_downstream_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_minutes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_seconds_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_datetime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_event_sub_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_event_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_event_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lead_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_opportunity_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_private_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recurrent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reminder_datetime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reminder_set_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_as_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_solution_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_datetime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
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

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_conference_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_conference_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIActivity::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_type_isValid && true;
}

} // namespace OpenAPI
