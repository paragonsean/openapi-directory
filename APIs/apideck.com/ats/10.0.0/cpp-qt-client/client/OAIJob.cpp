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

#include "OAIJob.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIJob::OAIJob(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIJob::OAIJob() {
    this->initializeModel();
}

OAIJob::~OAIJob() {}

void OAIJob::initializeModel() {

    m_addresses_isSet = false;
    m_addresses_isValid = false;

    m_available_to_employees_isSet = false;
    m_available_to_employees_isValid = false;

    m_blocks_isSet = false;
    m_blocks_isValid = false;

    m_branch_isSet = false;
    m_branch_isValid = false;

    m_closing_isSet = false;
    m_closing_isValid = false;

    m_closing_date_isSet = false;
    m_closing_date_isValid = false;

    m_closing_html_isSet = false;
    m_closing_html_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_confidential_isSet = false;
    m_confidential_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_custom_mappings_isSet = false;
    m_custom_mappings_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_department_isSet = false;
    m_department_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_description_html_isSet = false;
    m_description_html_isValid = false;

    m_employment_terms_isSet = false;
    m_employment_terms_isValid = false;

    m_experience_isSet = false;
    m_experience_isValid = false;

    m_followers_isSet = false;
    m_followers_isValid = false;

    m_hiring_managers_isSet = false;
    m_hiring_managers_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_job_portal_url_isSet = false;
    m_job_portal_url_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_links_isSet = false;
    m_links_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_owner_id_isSet = false;
    m_owner_id_isValid = false;

    m_published_at_isSet = false;
    m_published_at_isValid = false;

    m_record_url_isSet = false;
    m_record_url_isValid = false;

    m_recruiters_isSet = false;
    m_recruiters_isValid = false;

    m_remote_isSet = false;
    m_remote_isValid = false;

    m_requisition_id_isSet = false;
    m_requisition_id_isValid = false;

    m_salary_isSet = false;
    m_salary_isValid = false;

    m_sequence_isSet = false;
    m_sequence_isValid = false;

    m_slug_isSet = false;
    m_slug_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_visibility_isSet = false;
    m_visibility_isValid = false;
}

void OAIJob::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIJob::fromJsonObject(QJsonObject json) {

    m_addresses_isValid = ::OpenAPI::fromJsonValue(m_addresses, json[QString("addresses")]);
    m_addresses_isSet = !json[QString("addresses")].isNull() && m_addresses_isValid;

    m_available_to_employees_isValid = ::OpenAPI::fromJsonValue(m_available_to_employees, json[QString("available_to_employees")]);
    m_available_to_employees_isSet = !json[QString("available_to_employees")].isNull() && m_available_to_employees_isValid;

    m_blocks_isValid = ::OpenAPI::fromJsonValue(m_blocks, json[QString("blocks")]);
    m_blocks_isSet = !json[QString("blocks")].isNull() && m_blocks_isValid;

    m_branch_isValid = ::OpenAPI::fromJsonValue(m_branch, json[QString("branch")]);
    m_branch_isSet = !json[QString("branch")].isNull() && m_branch_isValid;

    m_closing_isValid = ::OpenAPI::fromJsonValue(m_closing, json[QString("closing")]);
    m_closing_isSet = !json[QString("closing")].isNull() && m_closing_isValid;

    m_closing_date_isValid = ::OpenAPI::fromJsonValue(m_closing_date, json[QString("closing_date")]);
    m_closing_date_isSet = !json[QString("closing_date")].isNull() && m_closing_date_isValid;

    m_closing_html_isValid = ::OpenAPI::fromJsonValue(m_closing_html, json[QString("closing_html")]);
    m_closing_html_isSet = !json[QString("closing_html")].isNull() && m_closing_html_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_confidential_isValid = ::OpenAPI::fromJsonValue(m_confidential, json[QString("confidential")]);
    m_confidential_isSet = !json[QString("confidential")].isNull() && m_confidential_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_custom_mappings_isValid = ::OpenAPI::fromJsonValue(m_custom_mappings, json[QString("custom_mappings")]);
    m_custom_mappings_isSet = !json[QString("custom_mappings")].isNull() && m_custom_mappings_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_department_isValid = ::OpenAPI::fromJsonValue(m_department, json[QString("department")]);
    m_department_isSet = !json[QString("department")].isNull() && m_department_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_description_html_isValid = ::OpenAPI::fromJsonValue(m_description_html, json[QString("description_html")]);
    m_description_html_isSet = !json[QString("description_html")].isNull() && m_description_html_isValid;

    m_employment_terms_isValid = ::OpenAPI::fromJsonValue(m_employment_terms, json[QString("employment_terms")]);
    m_employment_terms_isSet = !json[QString("employment_terms")].isNull() && m_employment_terms_isValid;

    m_experience_isValid = ::OpenAPI::fromJsonValue(m_experience, json[QString("experience")]);
    m_experience_isSet = !json[QString("experience")].isNull() && m_experience_isValid;

    m_followers_isValid = ::OpenAPI::fromJsonValue(m_followers, json[QString("followers")]);
    m_followers_isSet = !json[QString("followers")].isNull() && m_followers_isValid;

    m_hiring_managers_isValid = ::OpenAPI::fromJsonValue(m_hiring_managers, json[QString("hiring_managers")]);
    m_hiring_managers_isSet = !json[QString("hiring_managers")].isNull() && m_hiring_managers_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_job_portal_url_isValid = ::OpenAPI::fromJsonValue(m_job_portal_url, json[QString("job_portal_url")]);
    m_job_portal_url_isSet = !json[QString("job_portal_url")].isNull() && m_job_portal_url_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_owner_id_isValid = ::OpenAPI::fromJsonValue(m_owner_id, json[QString("owner_id")]);
    m_owner_id_isSet = !json[QString("owner_id")].isNull() && m_owner_id_isValid;

    m_published_at_isValid = ::OpenAPI::fromJsonValue(m_published_at, json[QString("published_at")]);
    m_published_at_isSet = !json[QString("published_at")].isNull() && m_published_at_isValid;

    m_record_url_isValid = ::OpenAPI::fromJsonValue(m_record_url, json[QString("record_url")]);
    m_record_url_isSet = !json[QString("record_url")].isNull() && m_record_url_isValid;

    m_recruiters_isValid = ::OpenAPI::fromJsonValue(m_recruiters, json[QString("recruiters")]);
    m_recruiters_isSet = !json[QString("recruiters")].isNull() && m_recruiters_isValid;

    m_remote_isValid = ::OpenAPI::fromJsonValue(m_remote, json[QString("remote")]);
    m_remote_isSet = !json[QString("remote")].isNull() && m_remote_isValid;

    m_requisition_id_isValid = ::OpenAPI::fromJsonValue(m_requisition_id, json[QString("requisition_id")]);
    m_requisition_id_isSet = !json[QString("requisition_id")].isNull() && m_requisition_id_isValid;

    m_salary_isValid = ::OpenAPI::fromJsonValue(m_salary, json[QString("salary")]);
    m_salary_isSet = !json[QString("salary")].isNull() && m_salary_isValid;

    m_sequence_isValid = ::OpenAPI::fromJsonValue(m_sequence, json[QString("sequence")]);
    m_sequence_isSet = !json[QString("sequence")].isNull() && m_sequence_isValid;

    m_slug_isValid = ::OpenAPI::fromJsonValue(m_slug, json[QString("slug")]);
    m_slug_isSet = !json[QString("slug")].isNull() && m_slug_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updated_by")]);
    m_updated_by_isSet = !json[QString("updated_by")].isNull() && m_updated_by_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_visibility_isValid = ::OpenAPI::fromJsonValue(m_visibility, json[QString("visibility")]);
    m_visibility_isSet = !json[QString("visibility")].isNull() && m_visibility_isValid;
}

QString OAIJob::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIJob::asJsonObject() const {
    QJsonObject obj;
    if (m_addresses.size() > 0) {
        obj.insert(QString("addresses"), ::OpenAPI::toJsonValue(m_addresses));
    }
    if (m_available_to_employees_isSet) {
        obj.insert(QString("available_to_employees"), ::OpenAPI::toJsonValue(m_available_to_employees));
    }
    if (m_blocks.size() > 0) {
        obj.insert(QString("blocks"), ::OpenAPI::toJsonValue(m_blocks));
    }
    if (m_branch.isSet()) {
        obj.insert(QString("branch"), ::OpenAPI::toJsonValue(m_branch));
    }
    if (m_closing_isSet) {
        obj.insert(QString("closing"), ::OpenAPI::toJsonValue(m_closing));
    }
    if (m_closing_date_isSet) {
        obj.insert(QString("closing_date"), ::OpenAPI::toJsonValue(m_closing_date));
    }
    if (m_closing_html_isSet) {
        obj.insert(QString("closing_html"), ::OpenAPI::toJsonValue(m_closing_html));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_confidential_isSet) {
        obj.insert(QString("confidential"), ::OpenAPI::toJsonValue(m_confidential));
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
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_department.isSet()) {
        obj.insert(QString("department"), ::OpenAPI::toJsonValue(m_department));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_description_html_isSet) {
        obj.insert(QString("description_html"), ::OpenAPI::toJsonValue(m_description_html));
    }
    if (m_employment_terms_isSet) {
        obj.insert(QString("employment_terms"), ::OpenAPI::toJsonValue(m_employment_terms));
    }
    if (m_experience_isSet) {
        obj.insert(QString("experience"), ::OpenAPI::toJsonValue(m_experience));
    }
    if (m_followers.size() > 0) {
        obj.insert(QString("followers"), ::OpenAPI::toJsonValue(m_followers));
    }
    if (m_hiring_managers.size() > 0) {
        obj.insert(QString("hiring_managers"), ::OpenAPI::toJsonValue(m_hiring_managers));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_job_portal_url_isSet) {
        obj.insert(QString("job_portal_url"), ::OpenAPI::toJsonValue(m_job_portal_url));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_links.size() > 0) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    if (m_location_isSet) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_owner_id_isSet) {
        obj.insert(QString("owner_id"), ::OpenAPI::toJsonValue(m_owner_id));
    }
    if (m_published_at_isSet) {
        obj.insert(QString("published_at"), ::OpenAPI::toJsonValue(m_published_at));
    }
    if (m_record_url_isSet) {
        obj.insert(QString("record_url"), ::OpenAPI::toJsonValue(m_record_url));
    }
    if (m_recruiters.size() > 0) {
        obj.insert(QString("recruiters"), ::OpenAPI::toJsonValue(m_recruiters));
    }
    if (m_remote_isSet) {
        obj.insert(QString("remote"), ::OpenAPI::toJsonValue(m_remote));
    }
    if (m_requisition_id_isSet) {
        obj.insert(QString("requisition_id"), ::OpenAPI::toJsonValue(m_requisition_id));
    }
    if (m_salary.isSet()) {
        obj.insert(QString("salary"), ::OpenAPI::toJsonValue(m_salary));
    }
    if (m_sequence_isSet) {
        obj.insert(QString("sequence"), ::OpenAPI::toJsonValue(m_sequence));
    }
    if (m_slug_isSet) {
        obj.insert(QString("slug"), ::OpenAPI::toJsonValue(m_slug));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
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
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_visibility_isSet) {
        obj.insert(QString("visibility"), ::OpenAPI::toJsonValue(m_visibility));
    }
    return obj;
}

QList<OAIAddress> OAIJob::getAddresses() const {
    return m_addresses;
}
void OAIJob::setAddresses(const QList<OAIAddress> &addresses) {
    m_addresses = addresses;
    m_addresses_isSet = true;
}

bool OAIJob::is_addresses_Set() const{
    return m_addresses_isSet;
}

bool OAIJob::is_addresses_Valid() const{
    return m_addresses_isValid;
}

bool OAIJob::isAvailableToEmployees() const {
    return m_available_to_employees;
}
void OAIJob::setAvailableToEmployees(const bool &available_to_employees) {
    m_available_to_employees = available_to_employees;
    m_available_to_employees_isSet = true;
}

bool OAIJob::is_available_to_employees_Set() const{
    return m_available_to_employees_isSet;
}

bool OAIJob::is_available_to_employees_Valid() const{
    return m_available_to_employees_isValid;
}

QList<OAIJob_blocks_inner> OAIJob::getBlocks() const {
    return m_blocks;
}
void OAIJob::setBlocks(const QList<OAIJob_blocks_inner> &blocks) {
    m_blocks = blocks;
    m_blocks_isSet = true;
}

bool OAIJob::is_blocks_Set() const{
    return m_blocks_isSet;
}

bool OAIJob::is_blocks_Valid() const{
    return m_blocks_isValid;
}

OAIBranch OAIJob::getBranch() const {
    return m_branch;
}
void OAIJob::setBranch(const OAIBranch &branch) {
    m_branch = branch;
    m_branch_isSet = true;
}

bool OAIJob::is_branch_Set() const{
    return m_branch_isSet;
}

bool OAIJob::is_branch_Valid() const{
    return m_branch_isValid;
}

QString OAIJob::getClosing() const {
    return m_closing;
}
void OAIJob::setClosing(const QString &closing) {
    m_closing = closing;
    m_closing_isSet = true;
}

bool OAIJob::is_closing_Set() const{
    return m_closing_isSet;
}

bool OAIJob::is_closing_Valid() const{
    return m_closing_isValid;
}

QDate OAIJob::getClosingDate() const {
    return m_closing_date;
}
void OAIJob::setClosingDate(const QDate &closing_date) {
    m_closing_date = closing_date;
    m_closing_date_isSet = true;
}

bool OAIJob::is_closing_date_Set() const{
    return m_closing_date_isSet;
}

bool OAIJob::is_closing_date_Valid() const{
    return m_closing_date_isValid;
}

QString OAIJob::getClosingHtml() const {
    return m_closing_html;
}
void OAIJob::setClosingHtml(const QString &closing_html) {
    m_closing_html = closing_html;
    m_closing_html_isSet = true;
}

bool OAIJob::is_closing_html_Set() const{
    return m_closing_html_isSet;
}

bool OAIJob::is_closing_html_Valid() const{
    return m_closing_html_isValid;
}

QString OAIJob::getCode() const {
    return m_code;
}
void OAIJob::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIJob::is_code_Set() const{
    return m_code_isSet;
}

bool OAIJob::is_code_Valid() const{
    return m_code_isValid;
}

bool OAIJob::isConfidential() const {
    return m_confidential;
}
void OAIJob::setConfidential(const bool &confidential) {
    m_confidential = confidential;
    m_confidential_isSet = true;
}

bool OAIJob::is_confidential_Set() const{
    return m_confidential_isSet;
}

bool OAIJob::is_confidential_Valid() const{
    return m_confidential_isValid;
}

QDateTime OAIJob::getCreatedAt() const {
    return m_created_at;
}
void OAIJob::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIJob::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIJob::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIJob::getCreatedBy() const {
    return m_created_by;
}
void OAIJob::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIJob::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIJob::is_created_by_Valid() const{
    return m_created_by_isValid;
}

QList<OAICustomField> OAIJob::getCustomFields() const {
    return m_custom_fields;
}
void OAIJob::setCustomFields(const QList<OAICustomField> &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIJob::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIJob::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

OAIObject OAIJob::getCustomMappings() const {
    return m_custom_mappings;
}
void OAIJob::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAIJob::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAIJob::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

bool OAIJob::isDeleted() const {
    return m_deleted;
}
void OAIJob::setDeleted(const bool &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIJob::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIJob::is_deleted_Valid() const{
    return m_deleted_isValid;
}

OAIDepartment OAIJob::getDepartment() const {
    return m_department;
}
void OAIJob::setDepartment(const OAIDepartment &department) {
    m_department = department;
    m_department_isSet = true;
}

bool OAIJob::is_department_Set() const{
    return m_department_isSet;
}

bool OAIJob::is_department_Valid() const{
    return m_department_isValid;
}

QString OAIJob::getDescription() const {
    return m_description;
}
void OAIJob::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIJob::is_description_Set() const{
    return m_description_isSet;
}

bool OAIJob::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIJob::getDescriptionHtml() const {
    return m_description_html;
}
void OAIJob::setDescriptionHtml(const QString &description_html) {
    m_description_html = description_html;
    m_description_html_isSet = true;
}

bool OAIJob::is_description_html_Set() const{
    return m_description_html_isSet;
}

bool OAIJob::is_description_html_Valid() const{
    return m_description_html_isValid;
}

QString OAIJob::getEmploymentTerms() const {
    return m_employment_terms;
}
void OAIJob::setEmploymentTerms(const QString &employment_terms) {
    m_employment_terms = employment_terms;
    m_employment_terms_isSet = true;
}

bool OAIJob::is_employment_terms_Set() const{
    return m_employment_terms_isSet;
}

bool OAIJob::is_employment_terms_Valid() const{
    return m_employment_terms_isValid;
}

QString OAIJob::getExperience() const {
    return m_experience;
}
void OAIJob::setExperience(const QString &experience) {
    m_experience = experience;
    m_experience_isSet = true;
}

bool OAIJob::is_experience_Set() const{
    return m_experience_isSet;
}

bool OAIJob::is_experience_Valid() const{
    return m_experience_isValid;
}

QList<QString> OAIJob::getFollowers() const {
    return m_followers;
}
void OAIJob::setFollowers(const QList<QString> &followers) {
    m_followers = followers;
    m_followers_isSet = true;
}

bool OAIJob::is_followers_Set() const{
    return m_followers_isSet;
}

bool OAIJob::is_followers_Valid() const{
    return m_followers_isValid;
}

QList<QString> OAIJob::getHiringManagers() const {
    return m_hiring_managers;
}
void OAIJob::setHiringManagers(const QList<QString> &hiring_managers) {
    m_hiring_managers = hiring_managers;
    m_hiring_managers_isSet = true;
}

bool OAIJob::is_hiring_managers_Set() const{
    return m_hiring_managers_isSet;
}

bool OAIJob::is_hiring_managers_Valid() const{
    return m_hiring_managers_isValid;
}

QString OAIJob::getId() const {
    return m_id;
}
void OAIJob::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIJob::is_id_Set() const{
    return m_id_isSet;
}

bool OAIJob::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIJob::getJobPortalUrl() const {
    return m_job_portal_url;
}
void OAIJob::setJobPortalUrl(const QString &job_portal_url) {
    m_job_portal_url = job_portal_url;
    m_job_portal_url_isSet = true;
}

bool OAIJob::is_job_portal_url_Set() const{
    return m_job_portal_url_isSet;
}

bool OAIJob::is_job_portal_url_Valid() const{
    return m_job_portal_url_isValid;
}

QString OAIJob::getLanguage() const {
    return m_language;
}
void OAIJob::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIJob::is_language_Set() const{
    return m_language_isSet;
}

bool OAIJob::is_language_Valid() const{
    return m_language_isValid;
}

QList<OAIJob_links_inner> OAIJob::getLinks() const {
    return m_links;
}
void OAIJob::setLinks(const QList<OAIJob_links_inner> &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAIJob::is_links_Set() const{
    return m_links_isSet;
}

bool OAIJob::is_links_Valid() const{
    return m_links_isValid;
}

QString OAIJob::getLocation() const {
    return m_location;
}
void OAIJob::setLocation(const QString &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAIJob::is_location_Set() const{
    return m_location_isSet;
}

bool OAIJob::is_location_Valid() const{
    return m_location_isValid;
}

QString OAIJob::getOwnerId() const {
    return m_owner_id;
}
void OAIJob::setOwnerId(const QString &owner_id) {
    m_owner_id = owner_id;
    m_owner_id_isSet = true;
}

bool OAIJob::is_owner_id_Set() const{
    return m_owner_id_isSet;
}

bool OAIJob::is_owner_id_Valid() const{
    return m_owner_id_isValid;
}

QDateTime OAIJob::getPublishedAt() const {
    return m_published_at;
}
void OAIJob::setPublishedAt(const QDateTime &published_at) {
    m_published_at = published_at;
    m_published_at_isSet = true;
}

bool OAIJob::is_published_at_Set() const{
    return m_published_at_isSet;
}

bool OAIJob::is_published_at_Valid() const{
    return m_published_at_isValid;
}

QString OAIJob::getRecordUrl() const {
    return m_record_url;
}
void OAIJob::setRecordUrl(const QString &record_url) {
    m_record_url = record_url;
    m_record_url_isSet = true;
}

bool OAIJob::is_record_url_Set() const{
    return m_record_url_isSet;
}

bool OAIJob::is_record_url_Valid() const{
    return m_record_url_isValid;
}

QList<QString> OAIJob::getRecruiters() const {
    return m_recruiters;
}
void OAIJob::setRecruiters(const QList<QString> &recruiters) {
    m_recruiters = recruiters;
    m_recruiters_isSet = true;
}

bool OAIJob::is_recruiters_Set() const{
    return m_recruiters_isSet;
}

bool OAIJob::is_recruiters_Valid() const{
    return m_recruiters_isValid;
}

bool OAIJob::isRemote() const {
    return m_remote;
}
void OAIJob::setRemote(const bool &remote) {
    m_remote = remote;
    m_remote_isSet = true;
}

bool OAIJob::is_remote_Set() const{
    return m_remote_isSet;
}

bool OAIJob::is_remote_Valid() const{
    return m_remote_isValid;
}

QString OAIJob::getRequisitionId() const {
    return m_requisition_id;
}
void OAIJob::setRequisitionId(const QString &requisition_id) {
    m_requisition_id = requisition_id;
    m_requisition_id_isSet = true;
}

bool OAIJob::is_requisition_id_Set() const{
    return m_requisition_id_isSet;
}

bool OAIJob::is_requisition_id_Valid() const{
    return m_requisition_id_isValid;
}

OAIJob_salary OAIJob::getSalary() const {
    return m_salary;
}
void OAIJob::setSalary(const OAIJob_salary &salary) {
    m_salary = salary;
    m_salary_isSet = true;
}

bool OAIJob::is_salary_Set() const{
    return m_salary_isSet;
}

bool OAIJob::is_salary_Valid() const{
    return m_salary_isValid;
}

qint32 OAIJob::getSequence() const {
    return m_sequence;
}
void OAIJob::setSequence(const qint32 &sequence) {
    m_sequence = sequence;
    m_sequence_isSet = true;
}

bool OAIJob::is_sequence_Set() const{
    return m_sequence_isSet;
}

bool OAIJob::is_sequence_Valid() const{
    return m_sequence_isValid;
}

QString OAIJob::getSlug() const {
    return m_slug;
}
void OAIJob::setSlug(const QString &slug) {
    m_slug = slug;
    m_slug_isSet = true;
}

bool OAIJob::is_slug_Set() const{
    return m_slug_isSet;
}

bool OAIJob::is_slug_Valid() const{
    return m_slug_isValid;
}

OAIJobStatus OAIJob::getStatus() const {
    return m_status;
}
void OAIJob::setStatus(const OAIJobStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIJob::is_status_Set() const{
    return m_status_isSet;
}

bool OAIJob::is_status_Valid() const{
    return m_status_isValid;
}

QList<QString> OAIJob::getTags() const {
    return m_tags;
}
void OAIJob::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIJob::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIJob::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIJob::getTitle() const {
    return m_title;
}
void OAIJob::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIJob::is_title_Set() const{
    return m_title_isSet;
}

bool OAIJob::is_title_Valid() const{
    return m_title_isValid;
}

QDateTime OAIJob::getUpdatedAt() const {
    return m_updated_at;
}
void OAIJob::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIJob::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIJob::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIJob::getUpdatedBy() const {
    return m_updated_by;
}
void OAIJob::setUpdatedBy(const QString &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAIJob::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAIJob::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

QString OAIJob::getUrl() const {
    return m_url;
}
void OAIJob::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIJob::is_url_Set() const{
    return m_url_isSet;
}

bool OAIJob::is_url_Valid() const{
    return m_url_isValid;
}

QString OAIJob::getVisibility() const {
    return m_visibility;
}
void OAIJob::setVisibility(const QString &visibility) {
    m_visibility = visibility;
    m_visibility_isSet = true;
}

bool OAIJob::is_visibility_Set() const{
    return m_visibility_isSet;
}

bool OAIJob::is_visibility_Valid() const{
    return m_visibility_isValid;
}

bool OAIJob::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_available_to_employees_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_blocks.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_branch.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_closing_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_closing_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_closing_html_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_confidential_isSet) {
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

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_department.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_html_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employment_terms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_experience_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_followers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_hiring_managers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_job_portal_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_published_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_record_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recruiters.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_remote_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_requisition_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_salary.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_sequence_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slug_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
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

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_visibility_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIJob::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
