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

#include "OAIAddress.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddress::OAIAddress(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddress::OAIAddress() {
    this->initializeModel();
}

OAIAddress::~OAIAddress() {}

void OAIAddress::initializeModel() {

    m_city_isSet = false;
    m_city_isValid = false;

    m_contact_name_isSet = false;
    m_contact_name_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_county_isSet = false;
    m_county_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_fax_isSet = false;
    m_fax_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_latitude_isSet = false;
    m_latitude_isValid = false;

    m_line1_isSet = false;
    m_line1_isValid = false;

    m_line2_isSet = false;
    m_line2_isValid = false;

    m_line3_isSet = false;
    m_line3_isValid = false;

    m_line4_isSet = false;
    m_line4_isValid = false;

    m_longitude_isSet = false;
    m_longitude_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_phone_number_isSet = false;
    m_phone_number_isValid = false;

    m_postal_code_isSet = false;
    m_postal_code_isValid = false;

    m_row_version_isSet = false;
    m_row_version_isValid = false;

    m_salutation_isSet = false;
    m_salutation_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_street_number_isSet = false;
    m_street_number_isValid = false;

    m_string_isSet = false;
    m_string_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_website_isSet = false;
    m_website_isValid = false;
}

void OAIAddress::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddress::fromJsonObject(QJsonObject json) {

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_contact_name_isValid = ::OpenAPI::fromJsonValue(m_contact_name, json[QString("contact_name")]);
    m_contact_name_isSet = !json[QString("contact_name")].isNull() && m_contact_name_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_county_isValid = ::OpenAPI::fromJsonValue(m_county, json[QString("county")]);
    m_county_isSet = !json[QString("county")].isNull() && m_county_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_fax_isValid = ::OpenAPI::fromJsonValue(m_fax, json[QString("fax")]);
    m_fax_isSet = !json[QString("fax")].isNull() && m_fax_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_latitude_isValid = ::OpenAPI::fromJsonValue(m_latitude, json[QString("latitude")]);
    m_latitude_isSet = !json[QString("latitude")].isNull() && m_latitude_isValid;

    m_line1_isValid = ::OpenAPI::fromJsonValue(m_line1, json[QString("line1")]);
    m_line1_isSet = !json[QString("line1")].isNull() && m_line1_isValid;

    m_line2_isValid = ::OpenAPI::fromJsonValue(m_line2, json[QString("line2")]);
    m_line2_isSet = !json[QString("line2")].isNull() && m_line2_isValid;

    m_line3_isValid = ::OpenAPI::fromJsonValue(m_line3, json[QString("line3")]);
    m_line3_isSet = !json[QString("line3")].isNull() && m_line3_isValid;

    m_line4_isValid = ::OpenAPI::fromJsonValue(m_line4, json[QString("line4")]);
    m_line4_isSet = !json[QString("line4")].isNull() && m_line4_isValid;

    m_longitude_isValid = ::OpenAPI::fromJsonValue(m_longitude, json[QString("longitude")]);
    m_longitude_isSet = !json[QString("longitude")].isNull() && m_longitude_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_phone_number_isValid = ::OpenAPI::fromJsonValue(m_phone_number, json[QString("phone_number")]);
    m_phone_number_isSet = !json[QString("phone_number")].isNull() && m_phone_number_isValid;

    m_postal_code_isValid = ::OpenAPI::fromJsonValue(m_postal_code, json[QString("postal_code")]);
    m_postal_code_isSet = !json[QString("postal_code")].isNull() && m_postal_code_isValid;

    m_row_version_isValid = ::OpenAPI::fromJsonValue(m_row_version, json[QString("row_version")]);
    m_row_version_isSet = !json[QString("row_version")].isNull() && m_row_version_isValid;

    m_salutation_isValid = ::OpenAPI::fromJsonValue(m_salutation, json[QString("salutation")]);
    m_salutation_isSet = !json[QString("salutation")].isNull() && m_salutation_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_street_number_isValid = ::OpenAPI::fromJsonValue(m_street_number, json[QString("street_number")]);
    m_street_number_isSet = !json[QString("street_number")].isNull() && m_street_number_isValid;

    m_string_isValid = ::OpenAPI::fromJsonValue(m_string, json[QString("string")]);
    m_string_isSet = !json[QString("string")].isNull() && m_string_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_website_isValid = ::OpenAPI::fromJsonValue(m_website, json[QString("website")]);
    m_website_isSet = !json[QString("website")].isNull() && m_website_isValid;
}

QString OAIAddress::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddress::asJsonObject() const {
    QJsonObject obj;
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_contact_name_isSet) {
        obj.insert(QString("contact_name"), ::OpenAPI::toJsonValue(m_contact_name));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_county_isSet) {
        obj.insert(QString("county"), ::OpenAPI::toJsonValue(m_county));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_fax_isSet) {
        obj.insert(QString("fax"), ::OpenAPI::toJsonValue(m_fax));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_latitude_isSet) {
        obj.insert(QString("latitude"), ::OpenAPI::toJsonValue(m_latitude));
    }
    if (m_line1_isSet) {
        obj.insert(QString("line1"), ::OpenAPI::toJsonValue(m_line1));
    }
    if (m_line2_isSet) {
        obj.insert(QString("line2"), ::OpenAPI::toJsonValue(m_line2));
    }
    if (m_line3_isSet) {
        obj.insert(QString("line3"), ::OpenAPI::toJsonValue(m_line3));
    }
    if (m_line4_isSet) {
        obj.insert(QString("line4"), ::OpenAPI::toJsonValue(m_line4));
    }
    if (m_longitude_isSet) {
        obj.insert(QString("longitude"), ::OpenAPI::toJsonValue(m_longitude));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_phone_number_isSet) {
        obj.insert(QString("phone_number"), ::OpenAPI::toJsonValue(m_phone_number));
    }
    if (m_postal_code_isSet) {
        obj.insert(QString("postal_code"), ::OpenAPI::toJsonValue(m_postal_code));
    }
    if (m_row_version_isSet) {
        obj.insert(QString("row_version"), ::OpenAPI::toJsonValue(m_row_version));
    }
    if (m_salutation_isSet) {
        obj.insert(QString("salutation"), ::OpenAPI::toJsonValue(m_salutation));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_street_number_isSet) {
        obj.insert(QString("street_number"), ::OpenAPI::toJsonValue(m_street_number));
    }
    if (m_string_isSet) {
        obj.insert(QString("string"), ::OpenAPI::toJsonValue(m_string));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_website_isSet) {
        obj.insert(QString("website"), ::OpenAPI::toJsonValue(m_website));
    }
    return obj;
}

QString OAIAddress::getCity() const {
    return m_city;
}
void OAIAddress::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIAddress::is_city_Set() const{
    return m_city_isSet;
}

bool OAIAddress::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIAddress::getContactName() const {
    return m_contact_name;
}
void OAIAddress::setContactName(const QString &contact_name) {
    m_contact_name = contact_name;
    m_contact_name_isSet = true;
}

bool OAIAddress::is_contact_name_Set() const{
    return m_contact_name_isSet;
}

bool OAIAddress::is_contact_name_Valid() const{
    return m_contact_name_isValid;
}

QString OAIAddress::getCountry() const {
    return m_country;
}
void OAIAddress::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIAddress::is_country_Set() const{
    return m_country_isSet;
}

bool OAIAddress::is_country_Valid() const{
    return m_country_isValid;
}

QString OAIAddress::getCounty() const {
    return m_county;
}
void OAIAddress::setCounty(const QString &county) {
    m_county = county;
    m_county_isSet = true;
}

bool OAIAddress::is_county_Set() const{
    return m_county_isSet;
}

bool OAIAddress::is_county_Valid() const{
    return m_county_isValid;
}

QString OAIAddress::getEmail() const {
    return m_email;
}
void OAIAddress::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIAddress::is_email_Set() const{
    return m_email_isSet;
}

bool OAIAddress::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIAddress::getFax() const {
    return m_fax;
}
void OAIAddress::setFax(const QString &fax) {
    m_fax = fax;
    m_fax_isSet = true;
}

bool OAIAddress::is_fax_Set() const{
    return m_fax_isSet;
}

bool OAIAddress::is_fax_Valid() const{
    return m_fax_isValid;
}

QString OAIAddress::getId() const {
    return m_id;
}
void OAIAddress::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAddress::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAddress::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIAddress::getLatitude() const {
    return m_latitude;
}
void OAIAddress::setLatitude(const QString &latitude) {
    m_latitude = latitude;
    m_latitude_isSet = true;
}

bool OAIAddress::is_latitude_Set() const{
    return m_latitude_isSet;
}

bool OAIAddress::is_latitude_Valid() const{
    return m_latitude_isValid;
}

QString OAIAddress::getLine1() const {
    return m_line1;
}
void OAIAddress::setLine1(const QString &line1) {
    m_line1 = line1;
    m_line1_isSet = true;
}

bool OAIAddress::is_line1_Set() const{
    return m_line1_isSet;
}

bool OAIAddress::is_line1_Valid() const{
    return m_line1_isValid;
}

QString OAIAddress::getLine2() const {
    return m_line2;
}
void OAIAddress::setLine2(const QString &line2) {
    m_line2 = line2;
    m_line2_isSet = true;
}

bool OAIAddress::is_line2_Set() const{
    return m_line2_isSet;
}

bool OAIAddress::is_line2_Valid() const{
    return m_line2_isValid;
}

QString OAIAddress::getLine3() const {
    return m_line3;
}
void OAIAddress::setLine3(const QString &line3) {
    m_line3 = line3;
    m_line3_isSet = true;
}

bool OAIAddress::is_line3_Set() const{
    return m_line3_isSet;
}

bool OAIAddress::is_line3_Valid() const{
    return m_line3_isValid;
}

QString OAIAddress::getLine4() const {
    return m_line4;
}
void OAIAddress::setLine4(const QString &line4) {
    m_line4 = line4;
    m_line4_isSet = true;
}

bool OAIAddress::is_line4_Set() const{
    return m_line4_isSet;
}

bool OAIAddress::is_line4_Valid() const{
    return m_line4_isValid;
}

QString OAIAddress::getLongitude() const {
    return m_longitude;
}
void OAIAddress::setLongitude(const QString &longitude) {
    m_longitude = longitude;
    m_longitude_isSet = true;
}

bool OAIAddress::is_longitude_Set() const{
    return m_longitude_isSet;
}

bool OAIAddress::is_longitude_Valid() const{
    return m_longitude_isValid;
}

QString OAIAddress::getName() const {
    return m_name;
}
void OAIAddress::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAddress::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAddress::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAddress::getNotes() const {
    return m_notes;
}
void OAIAddress::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIAddress::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIAddress::is_notes_Valid() const{
    return m_notes_isValid;
}

QString OAIAddress::getPhoneNumber() const {
    return m_phone_number;
}
void OAIAddress::setPhoneNumber(const QString &phone_number) {
    m_phone_number = phone_number;
    m_phone_number_isSet = true;
}

bool OAIAddress::is_phone_number_Set() const{
    return m_phone_number_isSet;
}

bool OAIAddress::is_phone_number_Valid() const{
    return m_phone_number_isValid;
}

QString OAIAddress::getPostalCode() const {
    return m_postal_code;
}
void OAIAddress::setPostalCode(const QString &postal_code) {
    m_postal_code = postal_code;
    m_postal_code_isSet = true;
}

bool OAIAddress::is_postal_code_Set() const{
    return m_postal_code_isSet;
}

bool OAIAddress::is_postal_code_Valid() const{
    return m_postal_code_isValid;
}

QString OAIAddress::getRowVersion() const {
    return m_row_version;
}
void OAIAddress::setRowVersion(const QString &row_version) {
    m_row_version = row_version;
    m_row_version_isSet = true;
}

bool OAIAddress::is_row_version_Set() const{
    return m_row_version_isSet;
}

bool OAIAddress::is_row_version_Valid() const{
    return m_row_version_isValid;
}

QString OAIAddress::getSalutation() const {
    return m_salutation;
}
void OAIAddress::setSalutation(const QString &salutation) {
    m_salutation = salutation;
    m_salutation_isSet = true;
}

bool OAIAddress::is_salutation_Set() const{
    return m_salutation_isSet;
}

bool OAIAddress::is_salutation_Valid() const{
    return m_salutation_isValid;
}

QString OAIAddress::getState() const {
    return m_state;
}
void OAIAddress::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIAddress::is_state_Set() const{
    return m_state_isSet;
}

bool OAIAddress::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIAddress::getStreetNumber() const {
    return m_street_number;
}
void OAIAddress::setStreetNumber(const QString &street_number) {
    m_street_number = street_number;
    m_street_number_isSet = true;
}

bool OAIAddress::is_street_number_Set() const{
    return m_street_number_isSet;
}

bool OAIAddress::is_street_number_Valid() const{
    return m_street_number_isValid;
}

QString OAIAddress::getString() const {
    return m_string;
}
void OAIAddress::setString(const QString &string) {
    m_string = string;
    m_string_isSet = true;
}

bool OAIAddress::is_string_Set() const{
    return m_string_isSet;
}

bool OAIAddress::is_string_Valid() const{
    return m_string_isValid;
}

QString OAIAddress::getType() const {
    return m_type;
}
void OAIAddress::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAddress::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAddress::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIAddress::getWebsite() const {
    return m_website;
}
void OAIAddress::setWebsite(const QString &website) {
    m_website = website;
    m_website_isSet = true;
}

bool OAIAddress::is_website_Set() const{
    return m_website_isSet;
}

bool OAIAddress::is_website_Valid() const{
    return m_website_isValid;
}

bool OAIAddress::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contact_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_county_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_latitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line3_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line4_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_longitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postal_code_isSet) {
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

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_string_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_website_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddress::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
