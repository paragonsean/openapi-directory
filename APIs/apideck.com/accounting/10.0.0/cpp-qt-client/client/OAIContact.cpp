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

#include "OAIContact.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIContact::OAIContact(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIContact::OAIContact() {
    this->initializeModel();
}

OAIContact::~OAIContact() {}

void OAIContact::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_addresses_isSet = false;
    m_addresses_isValid = false;

    m_birthday_isSet = false;
    m_birthday_isValid = false;

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_company_name_isSet = false;
    m_company_name_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_current_balance_isSet = false;
    m_current_balance_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_custom_mappings_isSet = false;
    m_custom_mappings_isValid = false;

    m_department_isSet = false;
    m_department_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_email_domain_isSet = false;
    m_email_domain_isValid = false;

    m_emails_isSet = false;
    m_emails_isValid = false;

    m_fax_isSet = false;
    m_fax_isValid = false;

    m_first_call_at_isSet = false;
    m_first_call_at_isValid = false;

    m_first_email_at_isSet = false;
    m_first_email_at_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_last_activity_at_isSet = false;
    m_last_activity_at_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_lead_id_isSet = false;
    m_lead_id_isValid = false;

    m_lead_source_isSet = false;
    m_lead_source_isValid = false;

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

    m_prefix_isSet = false;
    m_prefix_isValid = false;

    m_social_links_isSet = false;
    m_social_links_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_suffix_isSet = false;
    m_suffix_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_websites_isSet = false;
    m_websites_isValid = false;
}

void OAIContact::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIContact::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("active")]);
    m_active_isSet = !json[QString("active")].isNull() && m_active_isValid;

    m_addresses_isValid = ::OpenAPI::fromJsonValue(m_addresses, json[QString("addresses")]);
    m_addresses_isSet = !json[QString("addresses")].isNull() && m_addresses_isValid;

    m_birthday_isValid = ::OpenAPI::fromJsonValue(m_birthday, json[QString("birthday")]);
    m_birthday_isSet = !json[QString("birthday")].isNull() && m_birthday_isValid;

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("company_id")]);
    m_company_id_isSet = !json[QString("company_id")].isNull() && m_company_id_isValid;

    m_company_name_isValid = ::OpenAPI::fromJsonValue(m_company_name, json[QString("company_name")]);
    m_company_name_isSet = !json[QString("company_name")].isNull() && m_company_name_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_current_balance_isValid = ::OpenAPI::fromJsonValue(m_current_balance, json[QString("current_balance")]);
    m_current_balance_isSet = !json[QString("current_balance")].isNull() && m_current_balance_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_custom_mappings_isValid = ::OpenAPI::fromJsonValue(m_custom_mappings, json[QString("custom_mappings")]);
    m_custom_mappings_isSet = !json[QString("custom_mappings")].isNull() && m_custom_mappings_isValid;

    m_department_isValid = ::OpenAPI::fromJsonValue(m_department, json[QString("department")]);
    m_department_isSet = !json[QString("department")].isNull() && m_department_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_email_domain_isValid = ::OpenAPI::fromJsonValue(m_email_domain, json[QString("email_domain")]);
    m_email_domain_isSet = !json[QString("email_domain")].isNull() && m_email_domain_isValid;

    m_emails_isValid = ::OpenAPI::fromJsonValue(m_emails, json[QString("emails")]);
    m_emails_isSet = !json[QString("emails")].isNull() && m_emails_isValid;

    m_fax_isValid = ::OpenAPI::fromJsonValue(m_fax, json[QString("fax")]);
    m_fax_isSet = !json[QString("fax")].isNull() && m_fax_isValid;

    m_first_call_at_isValid = ::OpenAPI::fromJsonValue(m_first_call_at, json[QString("first_call_at")]);
    m_first_call_at_isSet = !json[QString("first_call_at")].isNull() && m_first_call_at_isValid;

    m_first_email_at_isValid = ::OpenAPI::fromJsonValue(m_first_email_at, json[QString("first_email_at")]);
    m_first_email_at_isSet = !json[QString("first_email_at")].isNull() && m_first_email_at_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("gender")]);
    m_gender_isSet = !json[QString("gender")].isNull() && m_gender_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_last_activity_at_isValid = ::OpenAPI::fromJsonValue(m_last_activity_at, json[QString("last_activity_at")]);
    m_last_activity_at_isSet = !json[QString("last_activity_at")].isNull() && m_last_activity_at_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_lead_id_isValid = ::OpenAPI::fromJsonValue(m_lead_id, json[QString("lead_id")]);
    m_lead_id_isSet = !json[QString("lead_id")].isNull() && m_lead_id_isValid;

    m_lead_source_isValid = ::OpenAPI::fromJsonValue(m_lead_source, json[QString("lead_source")]);
    m_lead_source_isSet = !json[QString("lead_source")].isNull() && m_lead_source_isValid;

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

    m_prefix_isValid = ::OpenAPI::fromJsonValue(m_prefix, json[QString("prefix")]);
    m_prefix_isSet = !json[QString("prefix")].isNull() && m_prefix_isValid;

    m_social_links_isValid = ::OpenAPI::fromJsonValue(m_social_links, json[QString("social_links")]);
    m_social_links_isSet = !json[QString("social_links")].isNull() && m_social_links_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_suffix_isValid = ::OpenAPI::fromJsonValue(m_suffix, json[QString("suffix")]);
    m_suffix_isSet = !json[QString("suffix")].isNull() && m_suffix_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_websites_isValid = ::OpenAPI::fromJsonValue(m_websites, json[QString("websites")]);
    m_websites_isSet = !json[QString("websites")].isNull() && m_websites_isValid;
}

QString OAIContact::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIContact::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_addresses.size() > 0) {
        obj.insert(QString("addresses"), ::OpenAPI::toJsonValue(m_addresses));
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
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_current_balance_isSet) {
        obj.insert(QString("current_balance"), ::OpenAPI::toJsonValue(m_current_balance));
    }
    if (m_custom_fields.size() > 0) {
        obj.insert(QString("custom_fields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_custom_mappings_isSet) {
        obj.insert(QString("custom_mappings"), ::OpenAPI::toJsonValue(m_custom_mappings));
    }
    if (m_department_isSet) {
        obj.insert(QString("department"), ::OpenAPI::toJsonValue(m_department));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_email_domain_isSet) {
        obj.insert(QString("email_domain"), ::OpenAPI::toJsonValue(m_email_domain));
    }
    if (m_emails.size() > 0) {
        obj.insert(QString("emails"), ::OpenAPI::toJsonValue(m_emails));
    }
    if (m_fax_isSet) {
        obj.insert(QString("fax"), ::OpenAPI::toJsonValue(m_fax));
    }
    if (m_first_call_at_isSet) {
        obj.insert(QString("first_call_at"), ::OpenAPI::toJsonValue(m_first_call_at));
    }
    if (m_first_email_at_isSet) {
        obj.insert(QString("first_email_at"), ::OpenAPI::toJsonValue(m_first_email_at));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_gender_isSet) {
        obj.insert(QString("gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_last_activity_at_isSet) {
        obj.insert(QString("last_activity_at"), ::OpenAPI::toJsonValue(m_last_activity_at));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_lead_id_isSet) {
        obj.insert(QString("lead_id"), ::OpenAPI::toJsonValue(m_lead_id));
    }
    if (m_lead_source_isSet) {
        obj.insert(QString("lead_source"), ::OpenAPI::toJsonValue(m_lead_source));
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
    if (m_prefix_isSet) {
        obj.insert(QString("prefix"), ::OpenAPI::toJsonValue(m_prefix));
    }
    if (m_social_links.size() > 0) {
        obj.insert(QString("social_links"), ::OpenAPI::toJsonValue(m_social_links));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_suffix_isSet) {
        obj.insert(QString("suffix"), ::OpenAPI::toJsonValue(m_suffix));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
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
    if (m_websites.size() > 0) {
        obj.insert(QString("websites"), ::OpenAPI::toJsonValue(m_websites));
    }
    return obj;
}

bool OAIContact::isActive() const {
    return m_active;
}
void OAIContact::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAIContact::is_active_Set() const{
    return m_active_isSet;
}

bool OAIContact::is_active_Valid() const{
    return m_active_isValid;
}

QList<OAIAddress> OAIContact::getAddresses() const {
    return m_addresses;
}
void OAIContact::setAddresses(const QList<OAIAddress> &addresses) {
    m_addresses = addresses;
    m_addresses_isSet = true;
}

bool OAIContact::is_addresses_Set() const{
    return m_addresses_isSet;
}

bool OAIContact::is_addresses_Valid() const{
    return m_addresses_isValid;
}

QString OAIContact::getBirthday() const {
    return m_birthday;
}
void OAIContact::setBirthday(const QString &birthday) {
    m_birthday = birthday;
    m_birthday_isSet = true;
}

bool OAIContact::is_birthday_Set() const{
    return m_birthday_isSet;
}

bool OAIContact::is_birthday_Valid() const{
    return m_birthday_isValid;
}

QString OAIContact::getCompanyId() const {
    return m_company_id;
}
void OAIContact::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIContact::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIContact::is_company_id_Valid() const{
    return m_company_id_isValid;
}

QString OAIContact::getCompanyName() const {
    return m_company_name;
}
void OAIContact::setCompanyName(const QString &company_name) {
    m_company_name = company_name;
    m_company_name_isSet = true;
}

bool OAIContact::is_company_name_Set() const{
    return m_company_name_isSet;
}

bool OAIContact::is_company_name_Valid() const{
    return m_company_name_isValid;
}

QDateTime OAIContact::getCreatedAt() const {
    return m_created_at;
}
void OAIContact::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIContact::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIContact::is_created_at_Valid() const{
    return m_created_at_isValid;
}

double OAIContact::getCurrentBalance() const {
    return m_current_balance;
}
void OAIContact::setCurrentBalance(const double &current_balance) {
    m_current_balance = current_balance;
    m_current_balance_isSet = true;
}

bool OAIContact::is_current_balance_Set() const{
    return m_current_balance_isSet;
}

bool OAIContact::is_current_balance_Valid() const{
    return m_current_balance_isValid;
}

QList<OAICustomField> OAIContact::getCustomFields() const {
    return m_custom_fields;
}
void OAIContact::setCustomFields(const QList<OAICustomField> &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIContact::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIContact::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

OAIObject OAIContact::getCustomMappings() const {
    return m_custom_mappings;
}
void OAIContact::setCustomMappings(const OAIObject &custom_mappings) {
    m_custom_mappings = custom_mappings;
    m_custom_mappings_isSet = true;
}

bool OAIContact::is_custom_mappings_Set() const{
    return m_custom_mappings_isSet;
}

bool OAIContact::is_custom_mappings_Valid() const{
    return m_custom_mappings_isValid;
}

QString OAIContact::getDepartment() const {
    return m_department;
}
void OAIContact::setDepartment(const QString &department) {
    m_department = department;
    m_department_isSet = true;
}

bool OAIContact::is_department_Set() const{
    return m_department_isSet;
}

bool OAIContact::is_department_Valid() const{
    return m_department_isValid;
}

QString OAIContact::getDescription() const {
    return m_description;
}
void OAIContact::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIContact::is_description_Set() const{
    return m_description_isSet;
}

bool OAIContact::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIContact::getEmailDomain() const {
    return m_email_domain;
}
void OAIContact::setEmailDomain(const QString &email_domain) {
    m_email_domain = email_domain;
    m_email_domain_isSet = true;
}

bool OAIContact::is_email_domain_Set() const{
    return m_email_domain_isSet;
}

bool OAIContact::is_email_domain_Valid() const{
    return m_email_domain_isValid;
}

QList<OAIEmail> OAIContact::getEmails() const {
    return m_emails;
}
void OAIContact::setEmails(const QList<OAIEmail> &emails) {
    m_emails = emails;
    m_emails_isSet = true;
}

bool OAIContact::is_emails_Set() const{
    return m_emails_isSet;
}

bool OAIContact::is_emails_Valid() const{
    return m_emails_isValid;
}

QString OAIContact::getFax() const {
    return m_fax;
}
void OAIContact::setFax(const QString &fax) {
    m_fax = fax;
    m_fax_isSet = true;
}

bool OAIContact::is_fax_Set() const{
    return m_fax_isSet;
}

bool OAIContact::is_fax_Valid() const{
    return m_fax_isValid;
}

QDateTime OAIContact::getFirstCallAt() const {
    return m_first_call_at;
}
void OAIContact::setFirstCallAt(const QDateTime &first_call_at) {
    m_first_call_at = first_call_at;
    m_first_call_at_isSet = true;
}

bool OAIContact::is_first_call_at_Set() const{
    return m_first_call_at_isSet;
}

bool OAIContact::is_first_call_at_Valid() const{
    return m_first_call_at_isValid;
}

QDateTime OAIContact::getFirstEmailAt() const {
    return m_first_email_at;
}
void OAIContact::setFirstEmailAt(const QDateTime &first_email_at) {
    m_first_email_at = first_email_at;
    m_first_email_at_isSet = true;
}

bool OAIContact::is_first_email_at_Set() const{
    return m_first_email_at_isSet;
}

bool OAIContact::is_first_email_at_Valid() const{
    return m_first_email_at_isValid;
}

QString OAIContact::getFirstName() const {
    return m_first_name;
}
void OAIContact::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIContact::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIContact::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIContact::getGender() const {
    return m_gender;
}
void OAIContact::setGender(const QString &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAIContact::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAIContact::is_gender_Valid() const{
    return m_gender_isValid;
}

QString OAIContact::getId() const {
    return m_id;
}
void OAIContact::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIContact::is_id_Set() const{
    return m_id_isSet;
}

bool OAIContact::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIContact::getImage() const {
    return m_image;
}
void OAIContact::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIContact::is_image_Set() const{
    return m_image_isSet;
}

bool OAIContact::is_image_Valid() const{
    return m_image_isValid;
}

QString OAIContact::getLanguage() const {
    return m_language;
}
void OAIContact::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIContact::is_language_Set() const{
    return m_language_isSet;
}

bool OAIContact::is_language_Valid() const{
    return m_language_isValid;
}

QDateTime OAIContact::getLastActivityAt() const {
    return m_last_activity_at;
}
void OAIContact::setLastActivityAt(const QDateTime &last_activity_at) {
    m_last_activity_at = last_activity_at;
    m_last_activity_at_isSet = true;
}

bool OAIContact::is_last_activity_at_Set() const{
    return m_last_activity_at_isSet;
}

bool OAIContact::is_last_activity_at_Valid() const{
    return m_last_activity_at_isValid;
}

QString OAIContact::getLastName() const {
    return m_last_name;
}
void OAIContact::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIContact::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIContact::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIContact::getLeadId() const {
    return m_lead_id;
}
void OAIContact::setLeadId(const QString &lead_id) {
    m_lead_id = lead_id;
    m_lead_id_isSet = true;
}

bool OAIContact::is_lead_id_Set() const{
    return m_lead_id_isSet;
}

bool OAIContact::is_lead_id_Valid() const{
    return m_lead_id_isValid;
}

QString OAIContact::getLeadSource() const {
    return m_lead_source;
}
void OAIContact::setLeadSource(const QString &lead_source) {
    m_lead_source = lead_source;
    m_lead_source_isSet = true;
}

bool OAIContact::is_lead_source_Set() const{
    return m_lead_source_isSet;
}

bool OAIContact::is_lead_source_Valid() const{
    return m_lead_source_isValid;
}

QString OAIContact::getMiddleName() const {
    return m_middle_name;
}
void OAIContact::setMiddleName(const QString &middle_name) {
    m_middle_name = middle_name;
    m_middle_name_isSet = true;
}

bool OAIContact::is_middle_name_Set() const{
    return m_middle_name_isSet;
}

bool OAIContact::is_middle_name_Valid() const{
    return m_middle_name_isValid;
}

QString OAIContact::getName() const {
    return m_name;
}
void OAIContact::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIContact::is_name_Set() const{
    return m_name_isSet;
}

bool OAIContact::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIContact::getOwnerId() const {
    return m_owner_id;
}
void OAIContact::setOwnerId(const QString &owner_id) {
    m_owner_id = owner_id;
    m_owner_id_isSet = true;
}

bool OAIContact::is_owner_id_Set() const{
    return m_owner_id_isSet;
}

bool OAIContact::is_owner_id_Valid() const{
    return m_owner_id_isValid;
}

QList<OAIPhoneNumber> OAIContact::getPhoneNumbers() const {
    return m_phone_numbers;
}
void OAIContact::setPhoneNumbers(const QList<OAIPhoneNumber> &phone_numbers) {
    m_phone_numbers = phone_numbers;
    m_phone_numbers_isSet = true;
}

bool OAIContact::is_phone_numbers_Set() const{
    return m_phone_numbers_isSet;
}

bool OAIContact::is_phone_numbers_Valid() const{
    return m_phone_numbers_isValid;
}

QString OAIContact::getPhotoUrl() const {
    return m_photo_url;
}
void OAIContact::setPhotoUrl(const QString &photo_url) {
    m_photo_url = photo_url;
    m_photo_url_isSet = true;
}

bool OAIContact::is_photo_url_Set() const{
    return m_photo_url_isSet;
}

bool OAIContact::is_photo_url_Valid() const{
    return m_photo_url_isValid;
}

QString OAIContact::getPrefix() const {
    return m_prefix;
}
void OAIContact::setPrefix(const QString &prefix) {
    m_prefix = prefix;
    m_prefix_isSet = true;
}

bool OAIContact::is_prefix_Set() const{
    return m_prefix_isSet;
}

bool OAIContact::is_prefix_Valid() const{
    return m_prefix_isValid;
}

QList<OAISocialLink> OAIContact::getSocialLinks() const {
    return m_social_links;
}
void OAIContact::setSocialLinks(const QList<OAISocialLink> &social_links) {
    m_social_links = social_links;
    m_social_links_isSet = true;
}

bool OAIContact::is_social_links_Set() const{
    return m_social_links_isSet;
}

bool OAIContact::is_social_links_Valid() const{
    return m_social_links_isValid;
}

QString OAIContact::getStatus() const {
    return m_status;
}
void OAIContact::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIContact::is_status_Set() const{
    return m_status_isSet;
}

bool OAIContact::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIContact::getSuffix() const {
    return m_suffix;
}
void OAIContact::setSuffix(const QString &suffix) {
    m_suffix = suffix;
    m_suffix_isSet = true;
}

bool OAIContact::is_suffix_Set() const{
    return m_suffix_isSet;
}

bool OAIContact::is_suffix_Valid() const{
    return m_suffix_isValid;
}

QList<QString> OAIContact::getTags() const {
    return m_tags;
}
void OAIContact::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIContact::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIContact::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIContact::getTitle() const {
    return m_title;
}
void OAIContact::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIContact::is_title_Set() const{
    return m_title_isSet;
}

bool OAIContact::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIContact::getType() const {
    return m_type;
}
void OAIContact::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIContact::is_type_Set() const{
    return m_type_isSet;
}

bool OAIContact::is_type_Valid() const{
    return m_type_isValid;
}

QDateTime OAIContact::getUpdatedAt() const {
    return m_updated_at;
}
void OAIContact::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIContact::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIContact::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

QList<OAIWebsite> OAIContact::getWebsites() const {
    return m_websites;
}
void OAIContact::setWebsites(const QList<OAIWebsite> &websites) {
    m_websites = websites;
    m_websites_isSet = true;
}

bool OAIContact::is_websites_Set() const{
    return m_websites_isSet;
}

bool OAIContact::is_websites_Valid() const{
    return m_websites_isValid;
}

bool OAIContact::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_addresses.size() > 0) {
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

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_current_balance_isSet) {
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

        if (m_department_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_domain_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_emails.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_fax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_call_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_email_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_activity_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lead_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lead_source_isSet) {
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

        if (m_prefix_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_social_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_suffix_isSet) {
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

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
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

bool OAIContact::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
