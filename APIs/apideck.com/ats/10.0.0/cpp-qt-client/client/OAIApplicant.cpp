/**
 * ATS API
 * Welcome to the ATS API.  You can use this API to access all ATS API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApplicant.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApplicant::OAIApplicant(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApplicant::OAIApplicant() {
    this->initializeModel();
}

OAIApplicant::~OAIApplicant() {}

void OAIApplicant::initializeModel() {

    m_addresses_isSet = false;
    m_addresses_isValid = false;

    m_anonymized_isSet = false;
    m_anonymized_isValid = false;

    m_application_ids_isSet = false;
    m_application_ids_isValid = false;

    m_applications_isSet = false;
    m_applications_isValid = false;

    m_archived_isSet = false;
    m_archived_isValid = false;

    m_birthday_isSet = false;
    m_birthday_isValid = false;

    m_confidential_isSet = false;
    m_confidential_isValid = false;

    m_coordinator_id_isSet = false;
    m_coordinator_id_isValid = false;

    m_cover_letter_isSet = false;
    m_cover_letter_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_custom_mappings_isSet = false;
    m_custom_mappings_isValid = false;

    m_cv_url_isSet = false;
    m_cv_url_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_deleted_at_isSet = false;
    m_deleted_at_isValid = false;

    m_deleted_by_isSet = false;
    m_deleted_by_isValid = false;

    m_emails_isSet = false;
    m_emails_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_followers_isSet = false;
    m_followers_isValid = false;

    m_headline_isSet = false;
    m_headline_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_initials_isSet = false;
    m_initials_isValid = false;

    m_job_url_isSet = false;
    m_job_url_isValid = false;

    m_last_interaction_at_isSet = false;
    m_last_interaction_at_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_middle_name_isSet = false;
    m_middle_name_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_owner_id_isSet = false;
    m_owner_id_isValid = false;

    m_phone_numbers_isSet = false;
    m_phone_numbers_isValid = false;

    m_photo_url_isSet = false;
    m_photo_url_isValid = false;

    m_position_id_isSet = false;
    m_position_id_isValid = false;

    m_record_url_isSet = false;
    m_record_url_isValid = false;

    m_recruiter_id_isSet = false;
    m_recruiter_id_isValid = false;

    m_rejected_at_isSet = false;
    m_rejected_at_isValid = false;

    m_social_links_isSet = false;
    m_social_links_isValid = false;

    m_source_id_isSet = false;
    m_source_id_isValid = false;

    m_sourced_by_isSet = false;
    m_sourced_by_isValid = false;

    m_sources_isSet = false;
    m_sources_isValid = false;

    m_stage_id_isSet = false;
    m_stage_id_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;

    m_websites_isSet = false;
    m_websites_isValid = false;
}

void OAIApplicant::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApplicant::fromJsonObject(QJsonObject json) {

    m_addresses_isValid = ::OpenAPI::fromJsonValue(m_addresses, json[QString("addresses")]);
    m_addresses_isSet = !json[QString("addresses")].isNull() && m_addresses_isValid;

    m_anonymized_isValid = ::OpenAPI::fromJsonValue(m_anonymized, json[QString("anonymized")]);
    m_anonymized_isSet = !json[QString("anonymized")].isNull() && m_anonymized_isValid;

    m_application_ids_isValid = ::OpenAPI::fromJsonValue(m_application_ids, json[QString("application_ids")]);
    m_application_ids_isSet = !json[QString("application_ids")].isNull() && m_application_ids_isValid;

    m_applications_isValid = ::OpenAPI::fromJsonValue(m_applications, json[QString("applications")]);
    m_applications_isSet = !json[QString("applications")].isNull() && m_applications_isValid;

    m_archived_isValid = ::OpenAPI::fromJsonValue(m_archived, json[QString("archived")]);
    m_archived_isSet = !json[QString("archived")].isNull() && m_archived_isValid;

    m_birthday_isValid = ::OpenAPI::fromJsonValue(m_birthday, json[QString("birthday")]);
    m_birthday_isSet = !json[QString("birthday")].isNull() && m_birthday_isValid;

    m_confidential_isValid = ::OpenAPI::fromJsonValue(m_confidential, json[QString("confidential")]);
    m_confidential_isSet = !json[QString("confidential")].isNull() && m_confidential_isValid;

    m_coordinator_id_isValid = ::OpenAPI::fromJsonValue(m_coordinator_id, json[QString("coordinator_id")]);
    m_coordinator_id_isSet = !json[QString("coordinator_id")].isNull() && m_coordinator_id_isValid;

    m_cover_letter_isValid = ::OpenAPI::fromJsonValue(m_cover_letter, json[QString("cover_letter")]);
    m_cover_letter_isSet = !json[QString("cover_letter")].isNull() && m_cover_letter_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_custom_mappings_isValid = ::OpenAPI::fromJsonValue(m_custom_mappings, json[QString("custom_mappings")]);
    m_custom_mappings_isSet = !json[QString("custom_mappings")].isNull() && m_custom_mappings_isValid;

    m_cv_url_isValid = ::OpenAPI::fromJsonValue(m_cv_url, json[QString("cv_url")]);
    m_cv_url_isSet = !json[QString("cv_url")].isNull() && m_cv_url_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_deleted_at_isValid = ::OpenAPI::fromJsonValue(m_deleted_at, json[QString("deleted_at")]);
    m_deleted_at_isSet = !json[QString("deleted_at")].isNull() && m_deleted_at_isValid;

    m_deleted_by_isValid = ::OpenAPI::fromJsonValue(m_deleted_by, json[QString("deleted_by")]);
    m_deleted_by_isSet = !json[QString("deleted_by")].isNull() && m_deleted_by_isValid;

    m_emails_isValid = ::OpenAPI::fromJsonValue(m_emails, json[QString("emails")]);
    m_emails_isSet = !json[QString("emails")].isNull() && m_emails_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_followers_isValid = ::OpenAPI::fromJsonValue(m_followers, json[QString("followers")]);
    m_followers_isSet = !json[QString("followers")].isNull() && m_followers_isValid;

    m_headline_isValid = ::OpenAPI::fromJsonValue(m_headline, json[QString("headline")]);
    m_headline_isSet = !json[QString("headline")].isNull() && m_headline_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_initials_isValid = ::OpenAPI::fromJsonValue(m_initials, json[QString("initials")]);
    m_initials_isSet = !json[QString("initials")].isNull() && m_initials_isValid;

    m_job_url_isValid = ::OpenAPI::fromJsonValue(m_job_url, json[QString("job_url")]);
    m_job_url_isSet = !json[QString("job_url")].isNull() && m_job_url_isValid;

    m_last_interaction_at_isValid = ::OpenAPI::fromJsonValue(m_last_interaction_at, json[QString("last_interaction_at")]);
    m_last_interaction_at_isSet = !json[QString("last_interaction_at")].isNull() && m_last_interaction_at_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_middle_name_isValid = ::OpenAPI::fromJsonValue(m_middle_name, json[QString("middle_name")]);
    m_middle_name_isSet = !json[QString("middle_name")].isNull() && m_middle_name_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_owner_id_isValid = ::OpenAPI::fromJsonValue(m_owner_id, json[QString("owner_id")]);
    m_owner_id_isSet = !json[QString("owner_id")].isNull() && m_owner_id_isValid;

    m_phone_numbers_isValid = ::OpenAPI::fromJsonValue(m_phone_numbers, json[QString("phone_numbers")]);
    m_phone_numbers_isSet = !json[QString("phone_numbers")].isNull() && m_phone_numbers_isValid;

    m_photo_url_isValid = ::OpenAPI::fromJsonValue(m_photo_url, json[QString("photo_url")]);
    m_photo_url_isSet = !json[QString("photo_url")].isNull() && m_photo_url_isValid;

    m_position_id_isValid = ::OpenAPI::fromJsonValue(m_position_id, json[QString("position_id")]);
    m_position_id_isSet = !json[QString("position_id")].isNull() && m_position_id_isValid;

    m_record_url_isValid = ::OpenAPI::fromJsonValue(m_record_url, json[QString("record_url")]);
    m_record_url_isSet = !json[QString("record_url")].isNull() && m_record_url_isValid;

    m_recruiter_id_isValid = ::OpenAPI::fromJsonValue(m_recruiter_id, json[QString("recruiter_id")]);
    m_recruiter_id_isSet = !json[QString("recruiter_id")].isNull() && m_recruiter_id_isValid;

    m_rejected_at_isValid = ::OpenAPI::fromJsonValue(m_rejected_at, json[QString("rejected_at")]);
    m_rejected_at_isSet = !json[QString("rejected_at")].isNull() && m_rejected_at_isValid;

    m_social_links_isValid = ::OpenAPI::fromJsonValue(m_social_links, json[QString("social_links")]);
    m_social_links_isSet = !json[QString("social_links")].isNull() && m_social_links_isValid;

    m_source_id_isValid = ::OpenAPI::fromJsonValue(m_source_id, json[QString("source_id")]);
    m_source_id_isSet = !json[QString("source_id")].isNull() && m_source_id_isValid;

    m_sourced_by_isValid = ::OpenAPI::fromJsonValue(m_sourced_by, json[QString("sourced_by")]);
    m_sourced_by_isSet = !json[QString("sourced_by")].isNull() && m_sourced_by_isValid;

    m_sources_isValid = ::OpenAPI::fromJsonValue(m_sources, json[QString("sources")]);
    m_sources_isSet = !json[QString("sources")].isNull() && m_sources_isValid;

    m_stage_id_isValid = ::OpenAPI::fromJsonValue(m_stage_id, json[QString("stage_id")]);
    m_stage_id_isSet = !json[QString("stage_id")].isNull() && m_stage_id_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updated_by")]);
    m_updated_by_isSet = !json[QString("updated_by")].isNull() && m_updated_by_isValid;

    m_websites_isValid = ::OpenAPI::fromJsonValue(m_websites, json[QString("websites")]);
    m_websites_isSet = !json[QString("websites")].isNull() && m_websites_isValid;
}

QString OAIApplicant::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApplicant::asJsonObject() const {
    QJsonObject obj;
    if (m_addresses.size() > 0) {
        obj.insert(QString("addresses"), ::OpenAPI::toJsonValue(m_addresses));
    }
    if (m_anonymized_isSet) {
        obj.insert(QString("anonymized"), ::OpenAPI::toJsonValue(m_anonymized));
    }
    if (m_application_ids.size() > 0) {
        obj.insert(QString("application_ids"), ::OpenAPI::toJsonValue(m_application_ids));
    }
    if (m_applications.size() > 0) {
        obj.insert(QString("applications"), ::OpenAPI::toJsonValue(m_applications));
    }
    if (m_archived_isSet) {
        obj.insert(QString("archived"), ::OpenAPI::toJsonValue(m_archived));
    }
    if (m_birthday_isSet) {
        obj.insert(QString("birthday"), ::OpenAPI::toJsonValue(m_birthday));
    }
    if (m_confidential_isSet) {
        obj.insert(QString("confidential"), ::OpenAPI::toJsonValue(m_confidential));
    }
    if (m_coordinator_id_isSet) {
        obj.insert(QString("coordinator_id"), ::OpenAPI::toJsonValue(m_coordinator_id));
    }
    if (m_cover_letter_isSet) {
        obj.insert(QString("cover_letter"), ::OpenAPI::toJsonValue(m_cover_letter));
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
    if (m_cv_url_isSet) {
        obj.insert(QString("cv_url"), ::OpenAPI::toJsonValue(m_cv_url));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_deleted_at_isSet) {
        obj.insert(QString("deleted_at"), ::OpenAPI::toJsonValue(m_deleted_at));
    }
    if (m_deleted_by_isSet) {
        obj.insert(QString("deleted_by"), ::OpenAPI::toJsonValue(m_deleted_by));
    }
    if (m_emails.size() > 0) {
        obj.insert(QString("emails"), ::OpenAPI::toJsonValue(m_emails));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_followers.size() > 0) {
        obj.insert(QString("followers"), ::OpenAPI::toJsonValue(m_followers));
    }
    if (m_headline_isSet) {
        obj.insert(QString("headline"), ::OpenAPI::toJsonValue(m_headline));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_initials_isSet) {
        obj.insert(QString("initials"), ::OpenAPI::toJsonValue(m_initials));
    }
    if (m_job_url_isSet) {
        obj.insert(QString("job_url"), ::OpenAPI::toJsonValue(m_job_url));
    }
    if (m_last_interaction_at_isSet) {
        obj.insert(QString("last_interaction_at"), ::OpenAPI::toJsonValue(m_last_interaction_at));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_middle_name_isSet) {
        obj.insert(QString("middle_name"), ::OpenAPI::toJsonValue(m_middle_name));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_owner_id_isSet) {
        obj.insert(QString("owner_id"), ::OpenAPI::toJsonValue(m_owner_id));
    }
    if (m_phone_numbers.size() > 0) {
        obj.insert(QString("phone_numbers"), ::OpenAPI::toJsonValue(m_phone_numbers));
    }
    if (m_photo_url_isSet) {
        obj.insert(QString("photo_url"), ::OpenAPI::toJsonValue(m_photo_url));
    }
    if (m_position_id_isSet) {
        obj.insert(QString("position_id"), ::OpenAPI::toJsonValue(m_position_id));
    }
    if (m_record_url_isSet) {
        obj.insert(QString("record_url"), ::OpenAPI::toJsonValue(m_record_url));
    }
    if (m_recruiter_id_isSet) {
        obj.insert(QString("recruiter_id"), ::OpenAPI::toJsonValue(m_recruiter_id));
    }
    if (m_rejected_at_isSet) {
        obj.insert(QString("rejected_at"), ::OpenAPI::toJsonValue(m_rejected_at));
    }
    if (m_social_links.size() > 0) {
        obj.insert(QString("social_links"), ::OpenAPI::toJsonValue(m_social_links));
    }
    if (m_source_id_isSet) {
        obj.insert(QString("source_id"), ::OpenAPI::toJsonValue(m_source_id));
    }
    if (m_sourced_by_isSet) {
        obj.insert(QString("sourced_by"), ::OpenAPI::toJsonValue(m_sourced_by));
    }
    if (m_sources.size() > 0) {
        obj.insert(QString("sources"), ::OpenAPI::toJsonValue(m_sources));
    }
    if (m_stage_id_isSet) {
        obj.insert(QString("stage_id"), ::OpenAPI::toJsonValue(m_stage_id));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_updated_by_isSet) {
        obj.insert(QString("updated_by"), ::OpenAPI::toJsonValue(m_updated_by));
    }
    if (m_websites.size() > 0) {
        obj.insert(QString("websites"), ::OpenAPI::toJsonValue(m_websites));
    }
    return obj;
}

QList<OAIAddress> OAIApplicant::getAddresses() const {
    return m_addresses;
}
void OAIApplicant::setAddresses(const QList<OAIAddress> &addresses) {
    m_addresses = addresses;
    m_addresses_isSet = true;
}

bool OAIApplicant::is_addresses_Set() const{
    return m_addresses_isSet;
}

bool OAIApplicant::is_addresses_Valid() const{
    return m_addresses_isValid;
}

bool OAIApplicant::isAnonymized() const {
    return m_anonymized;
}
void OAIApplicant::setAnonymized(const bool &anonymized) {
    m_anonymized = anonymized;
    m_anonymized_isSet = true;
}

bool OAIApplicant::is_anonymized_Set() const{
    return m_anonymized_isSet;
}

bool OAIApplicant::is_anonymized_Valid() const{
    return m_anonymized_isValid;
}

QList<QString> OAIApplicant::getApplicationIds() const {
    return m_application_ids;
}
void OAIApplicant::setApplicationIds(const QList<QString> &application_ids) {
    m_application_ids = application_ids;
    m_application_ids_isSet = true;
}

bool OAIApplicant::is_application_ids_Set() const{
    return m_application_ids_isSet;
}

bool OAIApplicant::is_application_ids_Valid() const{
    return m_application_ids_isValid;
}

QList<QString> OAIApplicant::getApplications() const {
    return m_applications;
}
void OAIApplicant::setApplications(const QList<QString> &applications) {
    m_applications = applications;
    m_applications_isSet = true;
}

bool OAIApplicant::is_applications_Set() const{
    return m_applications_isSet;
}

bool OAIApplicant::is_applications_Valid() const{
    return m_applications_isValid;
}

bool OAIApplicant::isArchived() const {
    return m_archived;
}
void OAIApplicant::setArchived(const bool &archived) {
    m_archived = archived;
    m_archived_isSet = true;
}

bool OAIApplicant::is_archived_Set() const{
    return m_archived_isSet;
}

bool OAIApplicant::is_archived_Valid() const{
    return m_archived_isValid;
}

QDate OAIApplicant::getBirthday() const {
    return m_birthday;
}
void OAIApplicant::setBirthday(const QDate &birthday) {
    m_birthday = birthday;
    m_birthday_isSet = true;
}

bool OAIApplicant::is_birthday_Set() const{
    return m_birthday_isSet;
}

bool OAIApplicant::is_birthday_Valid() const{
    return m_birthday_isValid;
}

bool OAIApplicant::isConfidential() const {
    return m_confidential;
}
void OAIApplicant::setConfidential(const bool &confidential) {
    m_confidential = confidential;
    m_confidential_isSet = true;
}

bool OAIApplicant::is_confidential_Set() const{
    return m_confidential_isSet;
}

bool OAIApplicant::is_confidential_Valid() const{
    return m_confidential_isValid;
}

QString OAIApplicant::getCoordinatorId() const {
    return m_coordinator_id;
}
void OAIApplicant::setCoordinatorId(const QString &coordinator_id) {
    m_coordinator_id = coordinator_id;
    m_coordinator_id_isSet = true;
}

bool OAIApplicant::is_coordinator_id_Set() const{
    return m_coordinator_id_isSet;
}

bool OAIApplicant::is_coordinator_id_Valid() const{
    return m_coordinator_id_isValid;
}

QString OAIApplicant::getCoverLetter() const {
    return m_cover_letter;
}
void OAIApplicant::setCoverLetter(const QString &cover_letter) {
    m_cover_letter = cover_letter;
    m_cover_letter_isSet = true;
}

bool OAIApplicant::is_cover_letter_Set() const{
    return m_cover_letter_isSet;
}

bool OAIApplicant::is_cover_letter_Valid() const{
    return m_cover_letter_isValid;
}

QDateTime OAIApplicant::getCreatedAt() const {
    return m_created_at;
}
void OAIApplicant::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIApplicant::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIApplicant::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIApplicant::getCreatedBy() const {
    return m_created_by;
}
void OAIApplicant::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIApplicant::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIApplicant::is_created_by_Valid() const{
    return m_created_by_isValid;
}

QList<OAICustomField> OAIApplicant::getCustomFields() const {
    return m_custom_fields;
}
void OAIApplicant::setCustomFields(const QList<OAICustomField> &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIApplicant::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIApplicant::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

OAIObject OAIApplicant::getCustomMappings() const {
    return m_custom_mappings;
}
void OAIApplicant::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAIApplicant::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAIApplicant::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

QString OAIApplicant::getCvUrl() const {
    return m_cv_url;
}
void OAIApplicant::setCvUrl(const QString &cv_url) {
    m_cv_url = cv_url;
    m_cv_url_isSet = true;
}

bool OAIApplicant::is_cv_url_Set() const{
    return m_cv_url_isSet;
}

bool OAIApplicant::is_cv_url_Valid() const{
    return m_cv_url_isValid;
}

bool OAIApplicant::isDeleted() const {
    return m_deleted;
}
void OAIApplicant::setDeleted(const bool &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIApplicant::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIApplicant::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QDateTime OAIApplicant::getDeletedAt() const {
    return m_deleted_at;
}
void OAIApplicant::setDeletedAt(const QDateTime &deleted_at) {
    m_deleted_at = deleted_at;
    m_deleted_at_isSet = true;
}

bool OAIApplicant::is_deleted_at_Set() const{
    return m_deleted_at_isSet;
}

bool OAIApplicant::is_deleted_at_Valid() const{
    return m_deleted_at_isValid;
}

QString OAIApplicant::getDeletedBy() const {
    return m_deleted_by;
}
void OAIApplicant::setDeletedBy(const QString &deleted_by) {
    m_deleted_by = deleted_by;
    m_deleted_by_isSet = true;
}

bool OAIApplicant::is_deleted_by_Set() const{
    return m_deleted_by_isSet;
}

bool OAIApplicant::is_deleted_by_Valid() const{
    return m_deleted_by_isValid;
}

QList<OAIEmail> OAIApplicant::getEmails() const {
    return m_emails;
}
void OAIApplicant::setEmails(const QList<OAIEmail> &emails) {
    m_emails = emails;
    m_emails_isSet = true;
}

bool OAIApplicant::is_emails_Set() const{
    return m_emails_isSet;
}

bool OAIApplicant::is_emails_Valid() const{
    return m_emails_isValid;
}

QString OAIApplicant::getFirstName() const {
    return m_first_name;
}
void OAIApplicant::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIApplicant::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIApplicant::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QList<QString> OAIApplicant::getFollowers() const {
    return m_followers;
}
void OAIApplicant::setFollowers(const QList<QString> &followers) {
    m_followers = followers;
    m_followers_isSet = true;
}

bool OAIApplicant::is_followers_Set() const{
    return m_followers_isSet;
}

bool OAIApplicant::is_followers_Valid() const{
    return m_followers_isValid;
}

QString OAIApplicant::getHeadline() const {
    return m_headline;
}
void OAIApplicant::setHeadline(const QString &headline) {
    m_headline = headline;
    m_headline_isSet = true;
}

bool OAIApplicant::is_headline_Set() const{
    return m_headline_isSet;
}

bool OAIApplicant::is_headline_Valid() const{
    return m_headline_isValid;
}

QString OAIApplicant::getId() const {
    return m_id;
}
void OAIApplicant::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIApplicant::is_id_Set() const{
    return m_id_isSet;
}

bool OAIApplicant::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIApplicant::getInitials() const {
    return m_initials;
}
void OAIApplicant::setInitials(const QString &initials) {
    m_initials = initials;
    m_initials_isSet = true;
}

bool OAIApplicant::is_initials_Set() const{
    return m_initials_isSet;
}

bool OAIApplicant::is_initials_Valid() const{
    return m_initials_isValid;
}

QString OAIApplicant::getJobUrl() const {
    return m_job_url;
}
void OAIApplicant::setJobUrl(const QString &job_url) {
    m_job_url = job_url;
    m_job_url_isSet = true;
}

bool OAIApplicant::is_job_url_Set() const{
    return m_job_url_isSet;
}

bool OAIApplicant::is_job_url_Valid() const{
    return m_job_url_isValid;
}

QDateTime OAIApplicant::getLastInteractionAt() const {
    return m_last_interaction_at;
}
void OAIApplicant::setLastInteractionAt(const QDateTime &last_interaction_at) {
    m_last_interaction_at = last_interaction_at;
    m_last_interaction_at_isSet = true;
}

bool OAIApplicant::is_last_interaction_at_Set() const{
    return m_last_interaction_at_isSet;
}

bool OAIApplicant::is_last_interaction_at_Valid() const{
    return m_last_interaction_at_isValid;
}

QString OAIApplicant::getLastName() const {
    return m_last_name;
}
void OAIApplicant::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIApplicant::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIApplicant::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIApplicant::getMiddleName() const {
    return m_middle_name;
}
void OAIApplicant::setMiddleName(const QString &middle_name) {
    m_middle_name = middle_name;
    m_middle_name_isSet = true;
}

bool OAIApplicant::is_middle_name_Set() const{
    return m_middle_name_isSet;
}

bool OAIApplicant::is_middle_name_Valid() const{
    return m_middle_name_isValid;
}

QString OAIApplicant::getName() const {
    return m_name;
}
void OAIApplicant::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIApplicant::is_name_Set() const{
    return m_name_isSet;
}

bool OAIApplicant::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIApplicant::getOwnerId() const {
    return m_owner_id;
}
void OAIApplicant::setOwnerId(const QString &owner_id) {
    m_owner_id = owner_id;
    m_owner_id_isSet = true;
}

bool OAIApplicant::is_owner_id_Set() const{
    return m_owner_id_isSet;
}

bool OAIApplicant::is_owner_id_Valid() const{
    return m_owner_id_isValid;
}

QList<OAIPhoneNumber> OAIApplicant::getPhoneNumbers() const {
    return m_phone_numbers;
}
void OAIApplicant::setPhoneNumbers(const QList<OAIPhoneNumber> &phone_numbers) {
    m_phone_numbers = phone_numbers;
    m_phone_numbers_isSet = true;
}

bool OAIApplicant::is_phone_numbers_Set() const{
    return m_phone_numbers_isSet;
}

bool OAIApplicant::is_phone_numbers_Valid() const{
    return m_phone_numbers_isValid;
}

QString OAIApplicant::getPhotoUrl() const {
    return m_photo_url;
}
void OAIApplicant::setPhotoUrl(const QString &photo_url) {
    m_photo_url = photo_url;
    m_photo_url_isSet = true;
}

bool OAIApplicant::is_photo_url_Set() const{
    return m_photo_url_isSet;
}

bool OAIApplicant::is_photo_url_Valid() const{
    return m_photo_url_isValid;
}

QString OAIApplicant::getPositionId() const {
    return m_position_id;
}
void OAIApplicant::setPositionId(const QString &position_id) {
    m_position_id = position_id;
    m_position_id_isSet = true;
}

bool OAIApplicant::is_position_id_Set() const{
    return m_position_id_isSet;
}

bool OAIApplicant::is_position_id_Valid() const{
    return m_position_id_isValid;
}

QString OAIApplicant::getRecordUrl() const {
    return m_record_url;
}
void OAIApplicant::setRecordUrl(const QString &record_url) {
    m_record_url = record_url;
    m_record_url_isSet = true;
}

bool OAIApplicant::is_record_url_Set() const{
    return m_record_url_isSet;
}

bool OAIApplicant::is_record_url_Valid() const{
    return m_record_url_isValid;
}

QString OAIApplicant::getRecruiterId() const {
    return m_recruiter_id;
}
void OAIApplicant::setRecruiterId(const QString &recruiter_id) {
    m_recruiter_id = recruiter_id;
    m_recruiter_id_isSet = true;
}

bool OAIApplicant::is_recruiter_id_Set() const{
    return m_recruiter_id_isSet;
}

bool OAIApplicant::is_recruiter_id_Valid() const{
    return m_recruiter_id_isValid;
}

QDateTime OAIApplicant::getRejectedAt() const {
    return m_rejected_at;
}
void OAIApplicant::setRejectedAt(const QDateTime &rejected_at) {
    m_rejected_at = rejected_at;
    m_rejected_at_isSet = true;
}

bool OAIApplicant::is_rejected_at_Set() const{
    return m_rejected_at_isSet;
}

bool OAIApplicant::is_rejected_at_Valid() const{
    return m_rejected_at_isValid;
}

QList<OAIApplicant_social_links_inner> OAIApplicant::getSocialLinks() const {
    return m_social_links;
}
void OAIApplicant::setSocialLinks(const QList<OAIApplicant_social_links_inner> &social_links) {
    m_social_links = social_links;
    m_social_links_isSet = true;
}

bool OAIApplicant::is_social_links_Set() const{
    return m_social_links_isSet;
}

bool OAIApplicant::is_social_links_Valid() const{
    return m_social_links_isValid;
}

QString OAIApplicant::getSourceId() const {
    return m_source_id;
}
void OAIApplicant::setSourceId(const QString &source_id) {
    m_source_id = source_id;
    m_source_id_isSet = true;
}

bool OAIApplicant::is_source_id_Set() const{
    return m_source_id_isSet;
}

bool OAIApplicant::is_source_id_Valid() const{
    return m_source_id_isValid;
}

QString OAIApplicant::getSourcedBy() const {
    return m_sourced_by;
}
void OAIApplicant::setSourcedBy(const QString &sourced_by) {
    m_sourced_by = sourced_by;
    m_sourced_by_isSet = true;
}

bool OAIApplicant::is_sourced_by_Set() const{
    return m_sourced_by_isSet;
}

bool OAIApplicant::is_sourced_by_Valid() const{
    return m_sourced_by_isValid;
}

QList<QString> OAIApplicant::getSources() const {
    return m_sources;
}
void OAIApplicant::setSources(const QList<QString> &sources) {
    m_sources = sources;
    m_sources_isSet = true;
}

bool OAIApplicant::is_sources_Set() const{
    return m_sources_isSet;
}

bool OAIApplicant::is_sources_Valid() const{
    return m_sources_isValid;
}

QString OAIApplicant::getStageId() const {
    return m_stage_id;
}
void OAIApplicant::setStageId(const QString &stage_id) {
    m_stage_id = stage_id;
    m_stage_id_isSet = true;
}

bool OAIApplicant::is_stage_id_Set() const{
    return m_stage_id_isSet;
}

bool OAIApplicant::is_stage_id_Valid() const{
    return m_stage_id_isValid;
}

QList<QString> OAIApplicant::getTags() const {
    return m_tags;
}
void OAIApplicant::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIApplicant::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIApplicant::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIApplicant::getTitle() const {
    return m_title;
}
void OAIApplicant::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIApplicant::is_title_Set() const{
    return m_title_isSet;
}

bool OAIApplicant::is_title_Valid() const{
    return m_title_isValid;
}

QDateTime OAIApplicant::getUpdatedAt() const {
    return m_updated_at;
}
void OAIApplicant::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIApplicant::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIApplicant::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIApplicant::getUpdatedBy() const {
    return m_updated_by;
}
void OAIApplicant::setUpdatedBy(const QString &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAIApplicant::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAIApplicant::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

QList<OAIApplicant_websites_inner> OAIApplicant::getWebsites() const {
    return m_websites;
}
void OAIApplicant::setWebsites(const QList<OAIApplicant_websites_inner> &websites) {
    m_websites = websites;
    m_websites_isSet = true;
}

bool OAIApplicant::is_websites_Set() const{
    return m_websites_isSet;
}

bool OAIApplicant::is_websites_Valid() const{
    return m_websites_isValid;
}

bool OAIApplicant::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_anonymized_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_application_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_applications.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_archived_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_birthday_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_confidential_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coordinator_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cover_letter_isSet) {
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

        if (m_cv_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emails.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_followers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_headline_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_initials_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_interaction_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_middle_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_numbers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_photo_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_record_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recruiter_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rejected_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_social_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sourced_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sources.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_stage_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
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

        if (m_websites.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApplicant::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
