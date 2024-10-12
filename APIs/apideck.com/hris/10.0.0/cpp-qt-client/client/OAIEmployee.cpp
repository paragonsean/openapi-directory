/**
 * HRIS API
 * Welcome to the HRIS API.  You can use this API to access all HRIS API endpoints.  ## Base URL  The base URL for all API requests is `https://unify.apideck.com`  ## Headers  Custom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.  | Name                  | Type    | Required | Description                                                                                                                                                    | | --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | | x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. | | x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             | | x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      | | x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             | | Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |  ## Authorization  You can interact with the API through the authorization methods below.  <!-- ReDoc-Inject: <security-definitions> -->  ## Pagination  All API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.  To fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you're at the end of the list.  In the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.  ### Query Parameters  | Name   | Type   | Required | Description                                                                                                        | | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ | | cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. | | limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |  ### Response Body  | Name                  | Type   | Description                                                        | | --------------------- | ------ | ------------------------------------------------------------------ | | meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API | | meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  | | meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     | | meta.items_on_page    | Number | Number of items returned in the data property of the response      | | links.previous        | String | Link to navigate to the previous page of results through the API   | | links.current         | String | Link to navigate to the current page of results through the API    | | links.next            | String | Link to navigate to the next page of results through the API       |  ⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.  ## SDKs and API Clients  We currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK. Need another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).  ## Debugging  Because of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.  ## Errors  The API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.  | Code | Title                | Description                                                                                                                                                                                              | | ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                | | 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              | | 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          | | 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. | | 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              | | 402  | Payment Required     | Subscription data is incomplete or out of date. You'll need to provide payment details to continue.                                                                                                      | | 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            | | 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           | | 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      | | 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     | | 429  | Too Many Requests    | You sent too many requests in a given amount of time (\"rate limit\"). Try again later                                                                                                                     | | 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |  ### Handling errors  The Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.  ### Error Types  #### RequestValidationError  Request is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.  #### UnsupportedFiltersError  Filters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.  #### UnsupportedSortFieldError  Sort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.  #### InvalidCursorError  Pagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.  #### ConnectorExecutionError  A Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.  #### UnauthorizedError  We were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: 'Bearer sk_live_***'`  #### ConnectorCredentialsError  A request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.  #### ConnectorDisabledError  A request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.  #### ConnectorRateLimitError  You sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.  #### RequestLimitError  You have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.  #### EntityNotFoundError  You've made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.  #### OAuthCredentialsNotFoundError  When adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.  #### IntegrationNotFoundError  The requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.  #### ConnectionNotFoundError  A valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.  #### ConnectionSettingsError  The connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.  #### ConnectorNotFoundError  A request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.  #### OAuthRedirectUriError  A request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.  #### OAuthInvalidStateError  The state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.  #### OAuthCodeExchangeError  When attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.  #### OAuthConnectorError  It seems something went wrong on the connector side. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### MappingError  There was an error attempting to retrieve the mapping for a given attribute. We've been notified and are working to fix this issue.  #### ConnectorMappingNotFoundError  It seems the implementation for this connector is incomplete. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorResponseMappingNotFoundError  We were unable to retrieve the response mapping for this connector. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationMappingNotFoundError  Connector mapping has not been implemented for the requested operation. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorWorkflowMappingError  The composite api calls required for this operation have not been mapped entirely. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  #### ConnectorOperationUnsupportedError  You're attempting a call that is not supported by the connector. It's likely this operation is supported by another connector, but we're unable to implement for this one.  #### PaginationNotSupportedError  Pagination is not yet supported for this connector, try removing limit and/or cursor from the query. It's possible this connector is in `beta` or still under development. We've been notified and are working to fix this issue.  ## API Design  ### API Styles and data formats  #### REST API  The API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.  ##### Available HTTP methods  The Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.  ``` POST /messages GET /messages GET /messages/{messageId} PATCH /messages/{messageId} DELETE /messages/{messageId} ```  Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.  ### Schema  All API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.  ### Meta  Meta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.  ### Idempotence (upcoming)  To prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.  Uniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)  ### Request IDs  Each API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.  ### Fixed field types  #### Dates  The dates returned by the API are all represented in UTC (ISO8601 format).  This example `2019-11-14T00:55:31.820Z` is defined by the ISO 8601 standard. The T in the middle separates the year-month-day portion from the hour-minute-second portion. The Z on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The Z is pronounced \"Zulu\" per military/aviation tradition.  The ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.  #### Prices and Currencies  All prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).  For zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.  All currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).  ## Support  If you have problems or need help with your case, you can always reach out to our Support.  
 *
 * The version of the OpenAPI document: 10.0.0
 * Contact: hello@apideck.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEmployee.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEmployee::OAIEmployee(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEmployee::OAIEmployee() {
    this->initializeModel();
}

OAIEmployee::~OAIEmployee() {}

void OAIEmployee::initializeModel() {

    m_addresses_isSet = false;
    m_addresses_isValid = false;

    m_bank_accounts_isSet = false;
    m_bank_accounts_isValid = false;

    m_birthday_isSet = false;
    m_birthday_isValid = false;

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_company_name_isSet = false;
    m_company_name_isValid = false;

    m_compensations_isSet = false;
    m_compensations_isValid = false;

    m_country_of_birth_isSet = false;
    m_country_of_birth_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_custom_mappings_isSet = false;
    m_custom_mappings_isValid = false;

    m_deceased_on_isSet = false;
    m_deceased_on_isValid = false;

    m_deleted_isSet = false;
    m_deleted_isValid = false;

    m_department_isSet = false;
    m_department_isValid = false;

    m_department_id_isSet = false;
    m_department_id_isValid = false;

    m_department_name_isSet = false;
    m_department_name_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_dietary_preference_isSet = false;
    m_dietary_preference_isValid = false;

    m_direct_reports_isSet = false;
    m_direct_reports_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_division_isSet = false;
    m_division_isValid = false;

    m_division_id_isSet = false;
    m_division_id_isValid = false;

    m_emails_isSet = false;
    m_emails_isValid = false;

    m_employee_number_isSet = false;
    m_employee_number_isValid = false;

    m_employment_end_date_isSet = false;
    m_employment_end_date_isValid = false;

    m_employment_role_isSet = false;
    m_employment_role_isValid = false;

    m_employment_start_date_isSet = false;
    m_employment_start_date_isValid = false;

    m_employment_status_isSet = false;
    m_employment_status_isValid = false;

    m_ethnicity_isSet = false;
    m_ethnicity_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_food_allergies_isSet = false;
    m_food_allergies_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_initials_isSet = false;
    m_initials_isValid = false;

    m_jobs_isSet = false;
    m_jobs_isValid = false;

    m_languages_isSet = false;
    m_languages_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_leaving_reason_isSet = false;
    m_leaving_reason_isValid = false;

    m_manager_isSet = false;
    m_manager_isValid = false;

    m_marital_status_isSet = false;
    m_marital_status_isValid = false;

    m_middle_name_isSet = false;
    m_middle_name_isValid = false;

    m_nationalities_isSet = false;
    m_nationalities_isValid = false;

    m_partner_isSet = false;
    m_partner_isValid = false;

    m_phone_numbers_isSet = false;
    m_phone_numbers_isValid = false;

    m_photo_url_isSet = false;
    m_photo_url_isValid = false;

    m_preferred_language_isSet = false;
    m_preferred_language_isValid = false;

    m_preferred_name_isSet = false;
    m_preferred_name_isValid = false;

    m_probation_period_isSet = false;
    m_probation_period_isValid = false;

    m_pronouns_isSet = false;
    m_pronouns_isValid = false;

    m_record_url_isSet = false;
    m_record_url_isValid = false;

    m_row_version_isSet = false;
    m_row_version_isValid = false;

    m_salutation_isSet = false;
    m_salutation_isValid = false;

    m_social_links_isSet = false;
    m_social_links_isValid = false;

    m_social_security_number_isSet = false;
    m_social_security_number_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_source_id_isSet = false;
    m_source_id_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_tax_code_isSet = false;
    m_tax_code_isValid = false;

    m_tax_id_isSet = false;
    m_tax_id_isValid = false;

    m_team_isSet = false;
    m_team_isValid = false;

    m_timezone_isSet = false;
    m_timezone_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_updated_by_isSet = false;
    m_updated_by_isValid = false;

    m_works_remote_isSet = false;
    m_works_remote_isValid = false;
}

void OAIEmployee::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEmployee::fromJsonObject(QJsonObject json) {

    m_addresses_isValid = ::OpenAPI::fromJsonValue(m_addresses, json[QString("addresses")]);
    m_addresses_isSet = !json[QString("addresses")].isNull() && m_addresses_isValid;

    m_bank_accounts_isValid = ::OpenAPI::fromJsonValue(m_bank_accounts, json[QString("bank_accounts")]);
    m_bank_accounts_isSet = !json[QString("bank_accounts")].isNull() && m_bank_accounts_isValid;

    m_birthday_isValid = ::OpenAPI::fromJsonValue(m_birthday, json[QString("birthday")]);
    m_birthday_isSet = !json[QString("birthday")].isNull() && m_birthday_isValid;

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("company_id")]);
    m_company_id_isSet = !json[QString("company_id")].isNull() && m_company_id_isValid;

    m_company_name_isValid = ::OpenAPI::fromJsonValue(m_company_name, json[QString("company_name")]);
    m_company_name_isSet = !json[QString("company_name")].isNull() && m_company_name_isValid;

    m_compensations_isValid = ::OpenAPI::fromJsonValue(m_compensations, json[QString("compensations")]);
    m_compensations_isSet = !json[QString("compensations")].isNull() && m_compensations_isValid;

    m_country_of_birth_isValid = ::OpenAPI::fromJsonValue(m_country_of_birth, json[QString("country_of_birth")]);
    m_country_of_birth_isSet = !json[QString("country_of_birth")].isNull() && m_country_of_birth_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_custom_mappings_isValid = ::OpenAPI::fromJsonValue(m_custom_mappings, json[QString("custom_mappings")]);
    m_custom_mappings_isSet = !json[QString("custom_mappings")].isNull() && m_custom_mappings_isValid;

    m_deceased_on_isValid = ::OpenAPI::fromJsonValue(m_deceased_on, json[QString("deceased_on")]);
    m_deceased_on_isSet = !json[QString("deceased_on")].isNull() && m_deceased_on_isValid;

    m_deleted_isValid = ::OpenAPI::fromJsonValue(m_deleted, json[QString("deleted")]);
    m_deleted_isSet = !json[QString("deleted")].isNull() && m_deleted_isValid;

    m_department_isValid = ::OpenAPI::fromJsonValue(m_department, json[QString("department")]);
    m_department_isSet = !json[QString("department")].isNull() && m_department_isValid;

    m_department_id_isValid = ::OpenAPI::fromJsonValue(m_department_id, json[QString("department_id")]);
    m_department_id_isSet = !json[QString("department_id")].isNull() && m_department_id_isValid;

    m_department_name_isValid = ::OpenAPI::fromJsonValue(m_department_name, json[QString("department_name")]);
    m_department_name_isSet = !json[QString("department_name")].isNull() && m_department_name_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_dietary_preference_isValid = ::OpenAPI::fromJsonValue(m_dietary_preference, json[QString("dietary_preference")]);
    m_dietary_preference_isSet = !json[QString("dietary_preference")].isNull() && m_dietary_preference_isValid;

    m_direct_reports_isValid = ::OpenAPI::fromJsonValue(m_direct_reports, json[QString("direct_reports")]);
    m_direct_reports_isSet = !json[QString("direct_reports")].isNull() && m_direct_reports_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("display_name")]);
    m_display_name_isSet = !json[QString("display_name")].isNull() && m_display_name_isValid;

    m_division_isValid = ::OpenAPI::fromJsonValue(m_division, json[QString("division")]);
    m_division_isSet = !json[QString("division")].isNull() && m_division_isValid;

    m_division_id_isValid = ::OpenAPI::fromJsonValue(m_division_id, json[QString("division_id")]);
    m_division_id_isSet = !json[QString("division_id")].isNull() && m_division_id_isValid;

    m_emails_isValid = ::OpenAPI::fromJsonValue(m_emails, json[QString("emails")]);
    m_emails_isSet = !json[QString("emails")].isNull() && m_emails_isValid;

    m_employee_number_isValid = ::OpenAPI::fromJsonValue(m_employee_number, json[QString("employee_number")]);
    m_employee_number_isSet = !json[QString("employee_number")].isNull() && m_employee_number_isValid;

    m_employment_end_date_isValid = ::OpenAPI::fromJsonValue(m_employment_end_date, json[QString("employment_end_date")]);
    m_employment_end_date_isSet = !json[QString("employment_end_date")].isNull() && m_employment_end_date_isValid;

    m_employment_role_isValid = ::OpenAPI::fromJsonValue(m_employment_role, json[QString("employment_role")]);
    m_employment_role_isSet = !json[QString("employment_role")].isNull() && m_employment_role_isValid;

    m_employment_start_date_isValid = ::OpenAPI::fromJsonValue(m_employment_start_date, json[QString("employment_start_date")]);
    m_employment_start_date_isSet = !json[QString("employment_start_date")].isNull() && m_employment_start_date_isValid;

    m_employment_status_isValid = ::OpenAPI::fromJsonValue(m_employment_status, json[QString("employment_status")]);
    m_employment_status_isSet = !json[QString("employment_status")].isNull() && m_employment_status_isValid;

    m_ethnicity_isValid = ::OpenAPI::fromJsonValue(m_ethnicity, json[QString("ethnicity")]);
    m_ethnicity_isSet = !json[QString("ethnicity")].isNull() && m_ethnicity_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_food_allergies_isValid = ::OpenAPI::fromJsonValue(m_food_allergies, json[QString("food_allergies")]);
    m_food_allergies_isSet = !json[QString("food_allergies")].isNull() && m_food_allergies_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("gender")]);
    m_gender_isSet = !json[QString("gender")].isNull() && m_gender_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_initials_isValid = ::OpenAPI::fromJsonValue(m_initials, json[QString("initials")]);
    m_initials_isSet = !json[QString("initials")].isNull() && m_initials_isValid;

    m_jobs_isValid = ::OpenAPI::fromJsonValue(m_jobs, json[QString("jobs")]);
    m_jobs_isSet = !json[QString("jobs")].isNull() && m_jobs_isValid;

    m_languages_isValid = ::OpenAPI::fromJsonValue(m_languages, json[QString("languages")]);
    m_languages_isSet = !json[QString("languages")].isNull() && m_languages_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_leaving_reason_isValid = ::OpenAPI::fromJsonValue(m_leaving_reason, json[QString("leaving_reason")]);
    m_leaving_reason_isSet = !json[QString("leaving_reason")].isNull() && m_leaving_reason_isValid;

    m_manager_isValid = ::OpenAPI::fromJsonValue(m_manager, json[QString("manager")]);
    m_manager_isSet = !json[QString("manager")].isNull() && m_manager_isValid;

    m_marital_status_isValid = ::OpenAPI::fromJsonValue(m_marital_status, json[QString("marital_status")]);
    m_marital_status_isSet = !json[QString("marital_status")].isNull() && m_marital_status_isValid;

    m_middle_name_isValid = ::OpenAPI::fromJsonValue(m_middle_name, json[QString("middle_name")]);
    m_middle_name_isSet = !json[QString("middle_name")].isNull() && m_middle_name_isValid;

    m_nationalities_isValid = ::OpenAPI::fromJsonValue(m_nationalities, json[QString("nationalities")]);
    m_nationalities_isSet = !json[QString("nationalities")].isNull() && m_nationalities_isValid;

    m_partner_isValid = ::OpenAPI::fromJsonValue(m_partner, json[QString("partner")]);
    m_partner_isSet = !json[QString("partner")].isNull() && m_partner_isValid;

    m_phone_numbers_isValid = ::OpenAPI::fromJsonValue(m_phone_numbers, json[QString("phone_numbers")]);
    m_phone_numbers_isSet = !json[QString("phone_numbers")].isNull() && m_phone_numbers_isValid;

    m_photo_url_isValid = ::OpenAPI::fromJsonValue(m_photo_url, json[QString("photo_url")]);
    m_photo_url_isSet = !json[QString("photo_url")].isNull() && m_photo_url_isValid;

    m_preferred_language_isValid = ::OpenAPI::fromJsonValue(m_preferred_language, json[QString("preferred_language")]);
    m_preferred_language_isSet = !json[QString("preferred_language")].isNull() && m_preferred_language_isValid;

    m_preferred_name_isValid = ::OpenAPI::fromJsonValue(m_preferred_name, json[QString("preferred_name")]);
    m_preferred_name_isSet = !json[QString("preferred_name")].isNull() && m_preferred_name_isValid;

    m_probation_period_isValid = ::OpenAPI::fromJsonValue(m_probation_period, json[QString("probation_period")]);
    m_probation_period_isSet = !json[QString("probation_period")].isNull() && m_probation_period_isValid;

    m_pronouns_isValid = ::OpenAPI::fromJsonValue(m_pronouns, json[QString("pronouns")]);
    m_pronouns_isSet = !json[QString("pronouns")].isNull() && m_pronouns_isValid;

    m_record_url_isValid = ::OpenAPI::fromJsonValue(m_record_url, json[QString("record_url")]);
    m_record_url_isSet = !json[QString("record_url")].isNull() && m_record_url_isValid;

    m_row_version_isValid = ::OpenAPI::fromJsonValue(m_row_version, json[QString("row_version")]);
    m_row_version_isSet = !json[QString("row_version")].isNull() && m_row_version_isValid;

    m_salutation_isValid = ::OpenAPI::fromJsonValue(m_salutation, json[QString("salutation")]);
    m_salutation_isSet = !json[QString("salutation")].isNull() && m_salutation_isValid;

    m_social_links_isValid = ::OpenAPI::fromJsonValue(m_social_links, json[QString("social_links")]);
    m_social_links_isSet = !json[QString("social_links")].isNull() && m_social_links_isValid;

    m_social_security_number_isValid = ::OpenAPI::fromJsonValue(m_social_security_number, json[QString("social_security_number")]);
    m_social_security_number_isSet = !json[QString("social_security_number")].isNull() && m_social_security_number_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_source_id_isValid = ::OpenAPI::fromJsonValue(m_source_id, json[QString("source_id")]);
    m_source_id_isSet = !json[QString("source_id")].isNull() && m_source_id_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_tax_code_isValid = ::OpenAPI::fromJsonValue(m_tax_code, json[QString("tax_code")]);
    m_tax_code_isSet = !json[QString("tax_code")].isNull() && m_tax_code_isValid;

    m_tax_id_isValid = ::OpenAPI::fromJsonValue(m_tax_id, json[QString("tax_id")]);
    m_tax_id_isSet = !json[QString("tax_id")].isNull() && m_tax_id_isValid;

    m_team_isValid = ::OpenAPI::fromJsonValue(m_team, json[QString("team")]);
    m_team_isSet = !json[QString("team")].isNull() && m_team_isValid;

    m_timezone_isValid = ::OpenAPI::fromJsonValue(m_timezone, json[QString("timezone")]);
    m_timezone_isSet = !json[QString("timezone")].isNull() && m_timezone_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_updated_by_isValid = ::OpenAPI::fromJsonValue(m_updated_by, json[QString("updated_by")]);
    m_updated_by_isSet = !json[QString("updated_by")].isNull() && m_updated_by_isValid;

    m_works_remote_isValid = ::OpenAPI::fromJsonValue(m_works_remote, json[QString("works_remote")]);
    m_works_remote_isSet = !json[QString("works_remote")].isNull() && m_works_remote_isValid;
}

QString OAIEmployee::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEmployee::asJsonObject() const {
    QJsonObject obj;
    if (m_addresses.size() > 0) {
        obj.insert(QString("addresses"), ::OpenAPI::toJsonValue(m_addresses));
    }
    if (m_bank_accounts.size() > 0) {
        obj.insert(QString("bank_accounts"), ::OpenAPI::toJsonValue(m_bank_accounts));
    }
    if (m_birthday_isSet) {
        obj.insert(QString("birthday"), ::OpenAPI::toJsonValue(m_birthday));
    }
    if (m_company_id_isSet) {
        obj.insert(QString("company_id"), ::OpenAPI::toJsonValue(m_company_id));
    }
    if (m_company_name_isSet) {
        obj.insert(QString("company_name"), ::OpenAPI::toJsonValue(m_company_name));
    }
    if (m_compensations.size() > 0) {
        obj.insert(QString("compensations"), ::OpenAPI::toJsonValue(m_compensations));
    }
    if (m_country_of_birth_isSet) {
        obj.insert(QString("country_of_birth"), ::OpenAPI::toJsonValue(m_country_of_birth));
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
    if (m_deceased_on_isSet) {
        obj.insert(QString("deceased_on"), ::OpenAPI::toJsonValue(m_deceased_on));
    }
    if (m_deleted_isSet) {
        obj.insert(QString("deleted"), ::OpenAPI::toJsonValue(m_deleted));
    }
    if (m_department_isSet) {
        obj.insert(QString("department"), ::OpenAPI::toJsonValue(m_department));
    }
    if (m_department_id_isSet) {
        obj.insert(QString("department_id"), ::OpenAPI::toJsonValue(m_department_id));
    }
    if (m_department_name_isSet) {
        obj.insert(QString("department_name"), ::OpenAPI::toJsonValue(m_department_name));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_dietary_preference_isSet) {
        obj.insert(QString("dietary_preference"), ::OpenAPI::toJsonValue(m_dietary_preference));
    }
    if (m_direct_reports.size() > 0) {
        obj.insert(QString("direct_reports"), ::OpenAPI::toJsonValue(m_direct_reports));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("display_name"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_division_isSet) {
        obj.insert(QString("division"), ::OpenAPI::toJsonValue(m_division));
    }
    if (m_division_id_isSet) {
        obj.insert(QString("division_id"), ::OpenAPI::toJsonValue(m_division_id));
    }
    if (m_emails.size() > 0) {
        obj.insert(QString("emails"), ::OpenAPI::toJsonValue(m_emails));
    }
    if (m_employee_number_isSet) {
        obj.insert(QString("employee_number"), ::OpenAPI::toJsonValue(m_employee_number));
    }
    if (m_employment_end_date_isSet) {
        obj.insert(QString("employment_end_date"), ::OpenAPI::toJsonValue(m_employment_end_date));
    }
    if (m_employment_role.isSet()) {
        obj.insert(QString("employment_role"), ::OpenAPI::toJsonValue(m_employment_role));
    }
    if (m_employment_start_date_isSet) {
        obj.insert(QString("employment_start_date"), ::OpenAPI::toJsonValue(m_employment_start_date));
    }
    if (m_employment_status.isSet()) {
        obj.insert(QString("employment_status"), ::OpenAPI::toJsonValue(m_employment_status));
    }
    if (m_ethnicity_isSet) {
        obj.insert(QString("ethnicity"), ::OpenAPI::toJsonValue(m_ethnicity));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_food_allergies.size() > 0) {
        obj.insert(QString("food_allergies"), ::OpenAPI::toJsonValue(m_food_allergies));
    }
    if (m_gender.isSet()) {
        obj.insert(QString("gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_initials_isSet) {
        obj.insert(QString("initials"), ::OpenAPI::toJsonValue(m_initials));
    }
    if (m_jobs.size() > 0) {
        obj.insert(QString("jobs"), ::OpenAPI::toJsonValue(m_jobs));
    }
    if (m_languages.size() > 0) {
        obj.insert(QString("languages"), ::OpenAPI::toJsonValue(m_languages));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_leaving_reason_isSet) {
        obj.insert(QString("leaving_reason"), ::OpenAPI::toJsonValue(m_leaving_reason));
    }
    if (m_manager.isSet()) {
        obj.insert(QString("manager"), ::OpenAPI::toJsonValue(m_manager));
    }
    if (m_marital_status_isSet) {
        obj.insert(QString("marital_status"), ::OpenAPI::toJsonValue(m_marital_status));
    }
    if (m_middle_name_isSet) {
        obj.insert(QString("middle_name"), ::OpenAPI::toJsonValue(m_middle_name));
    }
    if (m_nationalities.size() > 0) {
        obj.insert(QString("nationalities"), ::OpenAPI::toJsonValue(m_nationalities));
    }
    if (m_partner.isSet()) {
        obj.insert(QString("partner"), ::OpenAPI::toJsonValue(m_partner));
    }
    if (m_phone_numbers.size() > 0) {
        obj.insert(QString("phone_numbers"), ::OpenAPI::toJsonValue(m_phone_numbers));
    }
    if (m_photo_url_isSet) {
        obj.insert(QString("photo_url"), ::OpenAPI::toJsonValue(m_photo_url));
    }
    if (m_preferred_language_isSet) {
        obj.insert(QString("preferred_language"), ::OpenAPI::toJsonValue(m_preferred_language));
    }
    if (m_preferred_name_isSet) {
        obj.insert(QString("preferred_name"), ::OpenAPI::toJsonValue(m_preferred_name));
    }
    if (m_probation_period.isSet()) {
        obj.insert(QString("probation_period"), ::OpenAPI::toJsonValue(m_probation_period));
    }
    if (m_pronouns_isSet) {
        obj.insert(QString("pronouns"), ::OpenAPI::toJsonValue(m_pronouns));
    }
    if (m_record_url_isSet) {
        obj.insert(QString("record_url"), ::OpenAPI::toJsonValue(m_record_url));
    }
    if (m_row_version_isSet) {
        obj.insert(QString("row_version"), ::OpenAPI::toJsonValue(m_row_version));
    }
    if (m_salutation_isSet) {
        obj.insert(QString("salutation"), ::OpenAPI::toJsonValue(m_salutation));
    }
    if (m_social_links.size() > 0) {
        obj.insert(QString("social_links"), ::OpenAPI::toJsonValue(m_social_links));
    }
    if (m_social_security_number_isSet) {
        obj.insert(QString("social_security_number"), ::OpenAPI::toJsonValue(m_social_security_number));
    }
    if (m_source_isSet) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_source_id_isSet) {
        obj.insert(QString("source_id"), ::OpenAPI::toJsonValue(m_source_id));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_tax_code_isSet) {
        obj.insert(QString("tax_code"), ::OpenAPI::toJsonValue(m_tax_code));
    }
    if (m_tax_id_isSet) {
        obj.insert(QString("tax_id"), ::OpenAPI::toJsonValue(m_tax_id));
    }
    if (m_team.isSet()) {
        obj.insert(QString("team"), ::OpenAPI::toJsonValue(m_team));
    }
    if (m_timezone_isSet) {
        obj.insert(QString("timezone"), ::OpenAPI::toJsonValue(m_timezone));
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
    if (m_works_remote_isSet) {
        obj.insert(QString("works_remote"), ::OpenAPI::toJsonValue(m_works_remote));
    }
    return obj;
}

QList<OAIAddress> OAIEmployee::getAddresses() const {
    return m_addresses;
}
void OAIEmployee::setAddresses(const QList<OAIAddress> &addresses) {
    m_addresses = addresses;
    m_addresses_isSet = true;
}

bool OAIEmployee::is_addresses_Set() const{
    return m_addresses_isSet;
}

bool OAIEmployee::is_addresses_Valid() const{
    return m_addresses_isValid;
}

QList<OAIBankAccount> OAIEmployee::getBankAccounts() const {
    return m_bank_accounts;
}
void OAIEmployee::setBankAccounts(const QList<OAIBankAccount> &bank_accounts) {
    m_bank_accounts = bank_accounts;
    m_bank_accounts_isSet = true;
}

bool OAIEmployee::is_bank_accounts_Set() const{
    return m_bank_accounts_isSet;
}

bool OAIEmployee::is_bank_accounts_Valid() const{
    return m_bank_accounts_isValid;
}

QDate OAIEmployee::getBirthday() const {
    return m_birthday;
}
void OAIEmployee::setBirthday(const QDate &birthday) {
    m_birthday = birthday;
    m_birthday_isSet = true;
}

bool OAIEmployee::is_birthday_Set() const{
    return m_birthday_isSet;
}

bool OAIEmployee::is_birthday_Valid() const{
    return m_birthday_isValid;
}

QString OAIEmployee::getCompanyId() const {
    return m_company_id;
}
void OAIEmployee::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIEmployee::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIEmployee::is_company_id_Valid() const{
    return m_company_id_isValid;
}

QString OAIEmployee::getCompanyName() const {
    return m_company_name;
}
void OAIEmployee::setCompanyName(const QString &company_name) {
    m_company_name = company_name;
    m_company_name_isSet = true;
}

bool OAIEmployee::is_company_name_Set() const{
    return m_company_name_isSet;
}

bool OAIEmployee::is_company_name_Valid() const{
    return m_company_name_isValid;
}

QList<OAIEmployeeCompensation> OAIEmployee::getCompensations() const {
    return m_compensations;
}
void OAIEmployee::setCompensations(const QList<OAIEmployeeCompensation> &compensations) {
    m_compensations = compensations;
    m_compensations_isSet = true;
}

bool OAIEmployee::is_compensations_Set() const{
    return m_compensations_isSet;
}

bool OAIEmployee::is_compensations_Valid() const{
    return m_compensations_isValid;
}

QString OAIEmployee::getCountryOfBirth() const {
    return m_country_of_birth;
}
void OAIEmployee::setCountryOfBirth(const QString &country_of_birth) {
    m_country_of_birth = country_of_birth;
    m_country_of_birth_isSet = true;
}

bool OAIEmployee::is_country_of_birth_Set() const{
    return m_country_of_birth_isSet;
}

bool OAIEmployee::is_country_of_birth_Valid() const{
    return m_country_of_birth_isValid;
}

QDateTime OAIEmployee::getCreatedAt() const {
    return m_created_at;
}
void OAIEmployee::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIEmployee::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIEmployee::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIEmployee::getCreatedBy() const {
    return m_created_by;
}
void OAIEmployee::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIEmployee::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIEmployee::is_created_by_Valid() const{
    return m_created_by_isValid;
}

QList<OAICustomField> OAIEmployee::getCustomFields() const {
    return m_custom_fields;
}
void OAIEmployee::setCustomFields(const QList<OAICustomField> &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIEmployee::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIEmployee::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

OAIObject OAIEmployee::getCustomMappings() const {
    return m_custom_mappings;
}
void OAIEmployee::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAIEmployee::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAIEmployee::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

QDate OAIEmployee::getDeceasedOn() const {
    return m_deceased_on;
}
void OAIEmployee::setDeceasedOn(const QDate &deceased_on) {
    m_deceased_on = deceased_on;
    m_deceased_on_isSet = true;
}

bool OAIEmployee::is_deceased_on_Set() const{
    return m_deceased_on_isSet;
}

bool OAIEmployee::is_deceased_on_Valid() const{
    return m_deceased_on_isValid;
}

bool OAIEmployee::isDeleted() const {
    return m_deleted;
}
void OAIEmployee::setDeleted(const bool &deleted) {
    m_deleted = deleted;
    m_deleted_isSet = true;
}

bool OAIEmployee::is_deleted_Set() const{
    return m_deleted_isSet;
}

bool OAIEmployee::is_deleted_Valid() const{
    return m_deleted_isValid;
}

QString OAIEmployee::getDepartment() const {
    return m_department;
}
void OAIEmployee::setDepartment(const QString &department) {
    m_department = department;
    m_department_isSet = true;
}

bool OAIEmployee::is_department_Set() const{
    return m_department_isSet;
}

bool OAIEmployee::is_department_Valid() const{
    return m_department_isValid;
}

QString OAIEmployee::getDepartmentId() const {
    return m_department_id;
}
void OAIEmployee::setDepartmentId(const QString &department_id) {
    m_department_id = department_id;
    m_department_id_isSet = true;
}

bool OAIEmployee::is_department_id_Set() const{
    return m_department_id_isSet;
}

bool OAIEmployee::is_department_id_Valid() const{
    return m_department_id_isValid;
}

QString OAIEmployee::getDepartmentName() const {
    return m_department_name;
}
void OAIEmployee::setDepartmentName(const QString &department_name) {
    m_department_name = department_name;
    m_department_name_isSet = true;
}

bool OAIEmployee::is_department_name_Set() const{
    return m_department_name_isSet;
}

bool OAIEmployee::is_department_name_Valid() const{
    return m_department_name_isValid;
}

QString OAIEmployee::getDescription() const {
    return m_description;
}
void OAIEmployee::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIEmployee::is_description_Set() const{
    return m_description_isSet;
}

bool OAIEmployee::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIEmployee::getDietaryPreference() const {
    return m_dietary_preference;
}
void OAIEmployee::setDietaryPreference(const QString &dietary_preference) {
    m_dietary_preference = dietary_preference;
    m_dietary_preference_isSet = true;
}

bool OAIEmployee::is_dietary_preference_Set() const{
    return m_dietary_preference_isSet;
}

bool OAIEmployee::is_dietary_preference_Valid() const{
    return m_dietary_preference_isValid;
}

QList<QString> OAIEmployee::getDirectReports() const {
    return m_direct_reports;
}
void OAIEmployee::setDirectReports(const QList<QString> &direct_reports) {
    m_direct_reports = direct_reports;
    m_direct_reports_isSet = true;
}

bool OAIEmployee::is_direct_reports_Set() const{
    return m_direct_reports_isSet;
}

bool OAIEmployee::is_direct_reports_Valid() const{
    return m_direct_reports_isValid;
}

QString OAIEmployee::getDisplayName() const {
    return m_display_name;
}
void OAIEmployee::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIEmployee::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIEmployee::is_display_name_Valid() const{
    return m_display_name_isValid;
}

QString OAIEmployee::getDivision() const {
    return m_division;
}
void OAIEmployee::setDivision(const QString &division) {
    m_division = division;
    m_division_isSet = true;
}

bool OAIEmployee::is_division_Set() const{
    return m_division_isSet;
}

bool OAIEmployee::is_division_Valid() const{
    return m_division_isValid;
}

QString OAIEmployee::getDivisionId() const {
    return m_division_id;
}
void OAIEmployee::setDivisionId(const QString &division_id) {
    m_division_id = division_id;
    m_division_id_isSet = true;
}

bool OAIEmployee::is_division_id_Set() const{
    return m_division_id_isSet;
}

bool OAIEmployee::is_division_id_Valid() const{
    return m_division_id_isValid;
}

QList<OAIEmail> OAIEmployee::getEmails() const {
    return m_emails;
}
void OAIEmployee::setEmails(const QList<OAIEmail> &emails) {
    m_emails = emails;
    m_emails_isSet = true;
}

bool OAIEmployee::is_emails_Set() const{
    return m_emails_isSet;
}

bool OAIEmployee::is_emails_Valid() const{
    return m_emails_isValid;
}

QString OAIEmployee::getEmployeeNumber() const {
    return m_employee_number;
}
void OAIEmployee::setEmployeeNumber(const QString &employee_number) {
    m_employee_number = employee_number;
    m_employee_number_isSet = true;
}

bool OAIEmployee::is_employee_number_Set() const{
    return m_employee_number_isSet;
}

bool OAIEmployee::is_employee_number_Valid() const{
    return m_employee_number_isValid;
}

QString OAIEmployee::getEmploymentEndDate() const {
    return m_employment_end_date;
}
void OAIEmployee::setEmploymentEndDate(const QString &employment_end_date) {
    m_employment_end_date = employment_end_date;
    m_employment_end_date_isSet = true;
}

bool OAIEmployee::is_employment_end_date_Set() const{
    return m_employment_end_date_isSet;
}

bool OAIEmployee::is_employment_end_date_Valid() const{
    return m_employment_end_date_isValid;
}

OAIEmployee_employment_role OAIEmployee::getEmploymentRole() const {
    return m_employment_role;
}
void OAIEmployee::setEmploymentRole(const OAIEmployee_employment_role &employment_role) {
    m_employment_role = employment_role;
    m_employment_role_isSet = true;
}

bool OAIEmployee::is_employment_role_Set() const{
    return m_employment_role_isSet;
}

bool OAIEmployee::is_employment_role_Valid() const{
    return m_employment_role_isValid;
}

QString OAIEmployee::getEmploymentStartDate() const {
    return m_employment_start_date;
}
void OAIEmployee::setEmploymentStartDate(const QString &employment_start_date) {
    m_employment_start_date = employment_start_date;
    m_employment_start_date_isSet = true;
}

bool OAIEmployee::is_employment_start_date_Set() const{
    return m_employment_start_date_isSet;
}

bool OAIEmployee::is_employment_start_date_Valid() const{
    return m_employment_start_date_isValid;
}

OAIEmploymentStatus OAIEmployee::getEmploymentStatus() const {
    return m_employment_status;
}
void OAIEmployee::setEmploymentStatus(const OAIEmploymentStatus &employment_status) {
    m_employment_status = employment_status;
    m_employment_status_isSet = true;
}

bool OAIEmployee::is_employment_status_Set() const{
    return m_employment_status_isSet;
}

bool OAIEmployee::is_employment_status_Valid() const{
    return m_employment_status_isValid;
}

QString OAIEmployee::getEthnicity() const {
    return m_ethnicity;
}
void OAIEmployee::setEthnicity(const QString &ethnicity) {
    m_ethnicity = ethnicity;
    m_ethnicity_isSet = true;
}

bool OAIEmployee::is_ethnicity_Set() const{
    return m_ethnicity_isSet;
}

bool OAIEmployee::is_ethnicity_Valid() const{
    return m_ethnicity_isValid;
}

QString OAIEmployee::getFirstName() const {
    return m_first_name;
}
void OAIEmployee::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIEmployee::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIEmployee::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QList<QString> OAIEmployee::getFoodAllergies() const {
    return m_food_allergies;
}
void OAIEmployee::setFoodAllergies(const QList<QString> &food_allergies) {
    m_food_allergies = food_allergies;
    m_food_allergies_isSet = true;
}

bool OAIEmployee::is_food_allergies_Set() const{
    return m_food_allergies_isSet;
}

bool OAIEmployee::is_food_allergies_Valid() const{
    return m_food_allergies_isValid;
}

OAIGender OAIEmployee::getGender() const {
    return m_gender;
}
void OAIEmployee::setGender(const OAIGender &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAIEmployee::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAIEmployee::is_gender_Valid() const{
    return m_gender_isValid;
}

QString OAIEmployee::getId() const {
    return m_id;
}
void OAIEmployee::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIEmployee::is_id_Set() const{
    return m_id_isSet;
}

bool OAIEmployee::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIEmployee::getInitials() const {
    return m_initials;
}
void OAIEmployee::setInitials(const QString &initials) {
    m_initials = initials;
    m_initials_isSet = true;
}

bool OAIEmployee::is_initials_Set() const{
    return m_initials_isSet;
}

bool OAIEmployee::is_initials_Valid() const{
    return m_initials_isValid;
}

QList<OAIEmployeeJob> OAIEmployee::getJobs() const {
    return m_jobs;
}
void OAIEmployee::setJobs(const QList<OAIEmployeeJob> &jobs) {
    m_jobs = jobs;
    m_jobs_isSet = true;
}

bool OAIEmployee::is_jobs_Set() const{
    return m_jobs_isSet;
}

bool OAIEmployee::is_jobs_Valid() const{
    return m_jobs_isValid;
}

QList<QString> OAIEmployee::getLanguages() const {
    return m_languages;
}
void OAIEmployee::setLanguages(const QList<QString> &languages) {
    m_languages = languages;
    m_languages_isSet = true;
}

bool OAIEmployee::is_languages_Set() const{
    return m_languages_isSet;
}

bool OAIEmployee::is_languages_Valid() const{
    return m_languages_isValid;
}

QString OAIEmployee::getLastName() const {
    return m_last_name;
}
void OAIEmployee::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIEmployee::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIEmployee::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIEmployee::getLeavingReason() const {
    return m_leaving_reason;
}
void OAIEmployee::setLeavingReason(const QString &leaving_reason) {
    m_leaving_reason = leaving_reason;
    m_leaving_reason_isSet = true;
}

bool OAIEmployee::is_leaving_reason_Set() const{
    return m_leaving_reason_isSet;
}

bool OAIEmployee::is_leaving_reason_Valid() const{
    return m_leaving_reason_isValid;
}

OAIEmployee_manager OAIEmployee::getManager() const {
    return m_manager;
}
void OAIEmployee::setManager(const OAIEmployee_manager &manager) {
    m_manager = manager;
    m_manager_isSet = true;
}

bool OAIEmployee::is_manager_Set() const{
    return m_manager_isSet;
}

bool OAIEmployee::is_manager_Valid() const{
    return m_manager_isValid;
}

QString OAIEmployee::getMaritalStatus() const {
    return m_marital_status;
}
void OAIEmployee::setMaritalStatus(const QString &marital_status) {
    m_marital_status = marital_status;
    m_marital_status_isSet = true;
}

bool OAIEmployee::is_marital_status_Set() const{
    return m_marital_status_isSet;
}

bool OAIEmployee::is_marital_status_Valid() const{
    return m_marital_status_isValid;
}

QString OAIEmployee::getMiddleName() const {
    return m_middle_name;
}
void OAIEmployee::setMiddleName(const QString &middle_name) {
    m_middle_name = middle_name;
    m_middle_name_isSet = true;
}

bool OAIEmployee::is_middle_name_Set() const{
    return m_middle_name_isSet;
}

bool OAIEmployee::is_middle_name_Valid() const{
    return m_middle_name_isValid;
}

QList<QString> OAIEmployee::getNationalities() const {
    return m_nationalities;
}
void OAIEmployee::setNationalities(const QList<QString> &nationalities) {
    m_nationalities = nationalities;
    m_nationalities_isSet = true;
}

bool OAIEmployee::is_nationalities_Set() const{
    return m_nationalities_isSet;
}

bool OAIEmployee::is_nationalities_Valid() const{
    return m_nationalities_isValid;
}

OAIPerson OAIEmployee::getPartner() const {
    return m_partner;
}
void OAIEmployee::setPartner(const OAIPerson &partner) {
    m_partner = partner;
    m_partner_isSet = true;
}

bool OAIEmployee::is_partner_Set() const{
    return m_partner_isSet;
}

bool OAIEmployee::is_partner_Valid() const{
    return m_partner_isValid;
}

QList<OAIPhoneNumber> OAIEmployee::getPhoneNumbers() const {
    return m_phone_numbers;
}
void OAIEmployee::setPhoneNumbers(const QList<OAIPhoneNumber> &phone_numbers) {
    m_phone_numbers = phone_numbers;
    m_phone_numbers_isSet = true;
}

bool OAIEmployee::is_phone_numbers_Set() const{
    return m_phone_numbers_isSet;
}

bool OAIEmployee::is_phone_numbers_Valid() const{
    return m_phone_numbers_isValid;
}

QString OAIEmployee::getPhotoUrl() const {
    return m_photo_url;
}
void OAIEmployee::setPhotoUrl(const QString &photo_url) {
    m_photo_url = photo_url;
    m_photo_url_isSet = true;
}

bool OAIEmployee::is_photo_url_Set() const{
    return m_photo_url_isSet;
}

bool OAIEmployee::is_photo_url_Valid() const{
    return m_photo_url_isValid;
}

QString OAIEmployee::getPreferredLanguage() const {
    return m_preferred_language;
}
void OAIEmployee::setPreferredLanguage(const QString &preferred_language) {
    m_preferred_language = preferred_language;
    m_preferred_language_isSet = true;
}

bool OAIEmployee::is_preferred_language_Set() const{
    return m_preferred_language_isSet;
}

bool OAIEmployee::is_preferred_language_Valid() const{
    return m_preferred_language_isValid;
}

QString OAIEmployee::getPreferredName() const {
    return m_preferred_name;
}
void OAIEmployee::setPreferredName(const QString &preferred_name) {
    m_preferred_name = preferred_name;
    m_preferred_name_isSet = true;
}

bool OAIEmployee::is_preferred_name_Set() const{
    return m_preferred_name_isSet;
}

bool OAIEmployee::is_preferred_name_Valid() const{
    return m_preferred_name_isValid;
}

OAIProbation_period OAIEmployee::getProbationPeriod() const {
    return m_probation_period;
}
void OAIEmployee::setProbationPeriod(const OAIProbation_period &probation_period) {
    m_probation_period = probation_period;
    m_probation_period_isSet = true;
}

bool OAIEmployee::is_probation_period_Set() const{
    return m_probation_period_isSet;
}

bool OAIEmployee::is_probation_period_Valid() const{
    return m_probation_period_isValid;
}

QString OAIEmployee::getPronouns() const {
    return m_pronouns;
}
void OAIEmployee::setPronouns(const QString &pronouns) {
    m_pronouns = pronouns;
    m_pronouns_isSet = true;
}

bool OAIEmployee::is_pronouns_Set() const{
    return m_pronouns_isSet;
}

bool OAIEmployee::is_pronouns_Valid() const{
    return m_pronouns_isValid;
}

QString OAIEmployee::getRecordUrl() const {
    return m_record_url;
}
void OAIEmployee::setRecordUrl(const QString &record_url) {
    m_record_url = record_url;
    m_record_url_isSet = true;
}

bool OAIEmployee::is_record_url_Set() const{
    return m_record_url_isSet;
}

bool OAIEmployee::is_record_url_Valid() const{
    return m_record_url_isValid;
}

QString OAIEmployee::getRowVersion() const {
    return m_row_version;
}
void OAIEmployee::setRowVersion(const QString &row_version) {
    m_row_version = row_version;
    m_row_version_isSet = true;
}

bool OAIEmployee::is_row_version_Set() const{
    return m_row_version_isSet;
}

bool OAIEmployee::is_row_version_Valid() const{
    return m_row_version_isValid;
}

QString OAIEmployee::getSalutation() const {
    return m_salutation;
}
void OAIEmployee::setSalutation(const QString &salutation) {
    m_salutation = salutation;
    m_salutation_isSet = true;
}

bool OAIEmployee::is_salutation_Set() const{
    return m_salutation_isSet;
}

bool OAIEmployee::is_salutation_Valid() const{
    return m_salutation_isValid;
}

QList<OAISocialLink> OAIEmployee::getSocialLinks() const {
    return m_social_links;
}
void OAIEmployee::setSocialLinks(const QList<OAISocialLink> &social_links) {
    m_social_links = social_links;
    m_social_links_isSet = true;
}

bool OAIEmployee::is_social_links_Set() const{
    return m_social_links_isSet;
}

bool OAIEmployee::is_social_links_Valid() const{
    return m_social_links_isValid;
}

QString OAIEmployee::getSocialSecurityNumber() const {
    return m_social_security_number;
}
void OAIEmployee::setSocialSecurityNumber(const QString &social_security_number) {
    m_social_security_number = social_security_number;
    m_social_security_number_isSet = true;
}

bool OAIEmployee::is_social_security_number_Set() const{
    return m_social_security_number_isSet;
}

bool OAIEmployee::is_social_security_number_Valid() const{
    return m_social_security_number_isValid;
}

QString OAIEmployee::getSource() const {
    return m_source;
}
void OAIEmployee::setSource(const QString &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIEmployee::is_source_Set() const{
    return m_source_isSet;
}

bool OAIEmployee::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIEmployee::getSourceId() const {
    return m_source_id;
}
void OAIEmployee::setSourceId(const QString &source_id) {
    m_source_id = source_id;
    m_source_id_isSet = true;
}

bool OAIEmployee::is_source_id_Set() const{
    return m_source_id_isSet;
}

bool OAIEmployee::is_source_id_Valid() const{
    return m_source_id_isValid;
}

QList<QString> OAIEmployee::getTags() const {
    return m_tags;
}
void OAIEmployee::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIEmployee::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIEmployee::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIEmployee::getTaxCode() const {
    return m_tax_code;
}
void OAIEmployee::setTaxCode(const QString &tax_code) {
    m_tax_code = tax_code;
    m_tax_code_isSet = true;
}

bool OAIEmployee::is_tax_code_Set() const{
    return m_tax_code_isSet;
}

bool OAIEmployee::is_tax_code_Valid() const{
    return m_tax_code_isValid;
}

QString OAIEmployee::getTaxId() const {
    return m_tax_id;
}
void OAIEmployee::setTaxId(const QString &tax_id) {
    m_tax_id = tax_id;
    m_tax_id_isSet = true;
}

bool OAIEmployee::is_tax_id_Set() const{
    return m_tax_id_isSet;
}

bool OAIEmployee::is_tax_id_Valid() const{
    return m_tax_id_isValid;
}

OAITeam OAIEmployee::getTeam() const {
    return m_team;
}
void OAIEmployee::setTeam(const OAITeam &team) {
    m_team = team;
    m_team_isSet = true;
}

bool OAIEmployee::is_team_Set() const{
    return m_team_isSet;
}

bool OAIEmployee::is_team_Valid() const{
    return m_team_isValid;
}

QString OAIEmployee::getTimezone() const {
    return m_timezone;
}
void OAIEmployee::setTimezone(const QString &timezone) {
    m_timezone = timezone;
    m_timezone_isSet = true;
}

bool OAIEmployee::is_timezone_Set() const{
    return m_timezone_isSet;
}

bool OAIEmployee::is_timezone_Valid() const{
    return m_timezone_isValid;
}

QString OAIEmployee::getTitle() const {
    return m_title;
}
void OAIEmployee::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIEmployee::is_title_Set() const{
    return m_title_isSet;
}

bool OAIEmployee::is_title_Valid() const{
    return m_title_isValid;
}

QDateTime OAIEmployee::getUpdatedAt() const {
    return m_updated_at;
}
void OAIEmployee::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIEmployee::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIEmployee::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QString OAIEmployee::getUpdatedBy() const {
    return m_updated_by;
}
void OAIEmployee::setUpdatedBy(const QString &updated_by) {
    m_updated_by = updated_by;
    m_updated_by_isSet = true;
}

bool OAIEmployee::is_updated_by_Set() const{
    return m_updated_by_isSet;
}

bool OAIEmployee::is_updated_by_Valid() const{
    return m_updated_by_isValid;
}

bool OAIEmployee::isWorksRemote() const {
    return m_works_remote;
}
void OAIEmployee::setWorksRemote(const bool &works_remote) {
    m_works_remote = works_remote;
    m_works_remote_isSet = true;
}

bool OAIEmployee::is_works_remote_Set() const{
    return m_works_remote_isSet;
}

bool OAIEmployee::is_works_remote_Valid() const{
    return m_works_remote_isValid;
}

bool OAIEmployee::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_bank_accounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_birthday_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_compensations.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_of_birth_isSet) {
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

        if (m_deceased_on_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_deleted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_department_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_department_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_department_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dietary_preference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_direct_reports.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_division_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_division_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emails.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_employee_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employment_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employment_role.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_employment_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_employment_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ethnicity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_food_allergies.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender.isSet()) {
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

        if (m_jobs.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_languages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_leaving_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_manager.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_marital_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_middle_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nationalities.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_partner.isSet()) {
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

        if (m_preferred_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_preferred_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_probation_period.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_pronouns_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_record_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_row_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_salutation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_social_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_social_security_number_isSet) {
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

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezone_isSet) {
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

        if (m_works_remote_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEmployee::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && true;
}

} // namespace OpenAPI
