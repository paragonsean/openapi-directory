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

/*
 * OAIEmployee.h
 *
 * 
 */

#ifndef OAIEmployee_H
#define OAIEmployee_H

#include <QJsonObject>

#include "OAIAddress.h"
#include "OAIBankAccount.h"
#include "OAICustomField.h"
#include "OAIEmail.h"
#include "OAIEmployeeCompensation.h"
#include "OAIEmployeeJob.h"
#include "OAIEmployee_employment_role.h"
#include "OAIEmployee_manager.h"
#include "OAIEmploymentStatus.h"
#include "OAIGender.h"
#include "OAIObject.h"
#include "OAIPerson.h"
#include "OAIPhoneNumber.h"
#include "OAIProbation_period.h"
#include "OAISocialLink.h"
#include "OAITeam.h"
#include <QDate>
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAddress;
class OAIBankAccount;
class OAIEmployeeCompensation;
class OAICustomField;
class OAIEmail;
class OAIEmployee_employment_role;
class OAIEmployeeJob;
class OAIEmployee_manager;
class OAIPerson;
class OAIPhoneNumber;
class OAIProbation_period;
class OAISocialLink;
class OAITeam;

class OAIEmployee : public OAIObject {
public:
    OAIEmployee();
    OAIEmployee(QString json);
    ~OAIEmployee() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIAddress> getAddresses() const;
    void setAddresses(const QList<OAIAddress> &addresses);
    bool is_addresses_Set() const;
    bool is_addresses_Valid() const;

    QList<OAIBankAccount> getBankAccounts() const;
    void setBankAccounts(const QList<OAIBankAccount> &bank_accounts);
    bool is_bank_accounts_Set() const;
    bool is_bank_accounts_Valid() const;

    QDate getBirthday() const;
    void setBirthday(const QDate &birthday);
    bool is_birthday_Set() const;
    bool is_birthday_Valid() const;

    QString getCompanyId() const;
    void setCompanyId(const QString &company_id);
    bool is_company_id_Set() const;
    bool is_company_id_Valid() const;

    QString getCompanyName() const;
    void setCompanyName(const QString &company_name);
    bool is_company_name_Set() const;
    bool is_company_name_Valid() const;

    QList<OAIEmployeeCompensation> getCompensations() const;
    void setCompensations(const QList<OAIEmployeeCompensation> &compensations);
    bool is_compensations_Set() const;
    bool is_compensations_Valid() const;

    QString getCountryOfBirth() const;
    void setCountryOfBirth(const QString &country_of_birth);
    bool is_country_of_birth_Set() const;
    bool is_country_of_birth_Valid() const;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getCreatedBy() const;
    void setCreatedBy(const QString &created_by);
    bool is_created_by_Set() const;
    bool is_created_by_Valid() const;

    QList<OAICustomField> getCustomFields() const;
    void setCustomFields(const QList<OAICustomField> &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    OAIObject getCustomMappings() const;
    void setCustomMappings(const OAIObject &custom_mappings);
    bool is_custom_mappings_Set() const;
    bool is_custom_mappings_Valid() const;

    QDate getDeceasedOn() const;
    void setDeceasedOn(const QDate &deceased_on);
    bool is_deceased_on_Set() const;
    bool is_deceased_on_Valid() const;

    bool isDeleted() const;
    void setDeleted(const bool &deleted);
    bool is_deleted_Set() const;
    bool is_deleted_Valid() const;

    Q_DECL_DEPRECATED QString getDepartment() const;
    Q_DECL_DEPRECATED void setDepartment(const QString &department);
    Q_DECL_DEPRECATED bool is_department_Set() const;
    Q_DECL_DEPRECATED bool is_department_Valid() const;

    QString getDepartmentId() const;
    void setDepartmentId(const QString &department_id);
    bool is_department_id_Set() const;
    bool is_department_id_Valid() const;

    QString getDepartmentName() const;
    void setDepartmentName(const QString &department_name);
    bool is_department_name_Set() const;
    bool is_department_name_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getDietaryPreference() const;
    void setDietaryPreference(const QString &dietary_preference);
    bool is_dietary_preference_Set() const;
    bool is_dietary_preference_Valid() const;

    QList<QString> getDirectReports() const;
    void setDirectReports(const QList<QString> &direct_reports);
    bool is_direct_reports_Set() const;
    bool is_direct_reports_Valid() const;

    QString getDisplayName() const;
    void setDisplayName(const QString &display_name);
    bool is_display_name_Set() const;
    bool is_display_name_Valid() const;

    QString getDivision() const;
    void setDivision(const QString &division);
    bool is_division_Set() const;
    bool is_division_Valid() const;

    QString getDivisionId() const;
    void setDivisionId(const QString &division_id);
    bool is_division_id_Set() const;
    bool is_division_id_Valid() const;

    QList<OAIEmail> getEmails() const;
    void setEmails(const QList<OAIEmail> &emails);
    bool is_emails_Set() const;
    bool is_emails_Valid() const;

    QString getEmployeeNumber() const;
    void setEmployeeNumber(const QString &employee_number);
    bool is_employee_number_Set() const;
    bool is_employee_number_Valid() const;

    QString getEmploymentEndDate() const;
    void setEmploymentEndDate(const QString &employment_end_date);
    bool is_employment_end_date_Set() const;
    bool is_employment_end_date_Valid() const;

    OAIEmployee_employment_role getEmploymentRole() const;
    void setEmploymentRole(const OAIEmployee_employment_role &employment_role);
    bool is_employment_role_Set() const;
    bool is_employment_role_Valid() const;

    QString getEmploymentStartDate() const;
    void setEmploymentStartDate(const QString &employment_start_date);
    bool is_employment_start_date_Set() const;
    bool is_employment_start_date_Valid() const;

    OAIEmploymentStatus getEmploymentStatus() const;
    void setEmploymentStatus(const OAIEmploymentStatus &employment_status);
    bool is_employment_status_Set() const;
    bool is_employment_status_Valid() const;

    QString getEthnicity() const;
    void setEthnicity(const QString &ethnicity);
    bool is_ethnicity_Set() const;
    bool is_ethnicity_Valid() const;

    QString getFirstName() const;
    void setFirstName(const QString &first_name);
    bool is_first_name_Set() const;
    bool is_first_name_Valid() const;

    QList<QString> getFoodAllergies() const;
    void setFoodAllergies(const QList<QString> &food_allergies);
    bool is_food_allergies_Set() const;
    bool is_food_allergies_Valid() const;

    OAIGender getGender() const;
    void setGender(const OAIGender &gender);
    bool is_gender_Set() const;
    bool is_gender_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getInitials() const;
    void setInitials(const QString &initials);
    bool is_initials_Set() const;
    bool is_initials_Valid() const;

    QList<OAIEmployeeJob> getJobs() const;
    void setJobs(const QList<OAIEmployeeJob> &jobs);
    bool is_jobs_Set() const;
    bool is_jobs_Valid() const;

    QList<QString> getLanguages() const;
    void setLanguages(const QList<QString> &languages);
    bool is_languages_Set() const;
    bool is_languages_Valid() const;

    QString getLastName() const;
    void setLastName(const QString &last_name);
    bool is_last_name_Set() const;
    bool is_last_name_Valid() const;

    QString getLeavingReason() const;
    void setLeavingReason(const QString &leaving_reason);
    bool is_leaving_reason_Set() const;
    bool is_leaving_reason_Valid() const;

    OAIEmployee_manager getManager() const;
    void setManager(const OAIEmployee_manager &manager);
    bool is_manager_Set() const;
    bool is_manager_Valid() const;

    QString getMaritalStatus() const;
    void setMaritalStatus(const QString &marital_status);
    bool is_marital_status_Set() const;
    bool is_marital_status_Valid() const;

    QString getMiddleName() const;
    void setMiddleName(const QString &middle_name);
    bool is_middle_name_Set() const;
    bool is_middle_name_Valid() const;

    QList<QString> getNationalities() const;
    void setNationalities(const QList<QString> &nationalities);
    bool is_nationalities_Set() const;
    bool is_nationalities_Valid() const;

    OAIPerson getPartner() const;
    void setPartner(const OAIPerson &partner);
    bool is_partner_Set() const;
    bool is_partner_Valid() const;

    QList<OAIPhoneNumber> getPhoneNumbers() const;
    void setPhoneNumbers(const QList<OAIPhoneNumber> &phone_numbers);
    bool is_phone_numbers_Set() const;
    bool is_phone_numbers_Valid() const;

    QString getPhotoUrl() const;
    void setPhotoUrl(const QString &photo_url);
    bool is_photo_url_Set() const;
    bool is_photo_url_Valid() const;

    QString getPreferredLanguage() const;
    void setPreferredLanguage(const QString &preferred_language);
    bool is_preferred_language_Set() const;
    bool is_preferred_language_Valid() const;

    QString getPreferredName() const;
    void setPreferredName(const QString &preferred_name);
    bool is_preferred_name_Set() const;
    bool is_preferred_name_Valid() const;

    OAIProbation_period getProbationPeriod() const;
    void setProbationPeriod(const OAIProbation_period &probation_period);
    bool is_probation_period_Set() const;
    bool is_probation_period_Valid() const;

    QString getPronouns() const;
    void setPronouns(const QString &pronouns);
    bool is_pronouns_Set() const;
    bool is_pronouns_Valid() const;

    QString getRecordUrl() const;
    void setRecordUrl(const QString &record_url);
    bool is_record_url_Set() const;
    bool is_record_url_Valid() const;

    QString getRowVersion() const;
    void setRowVersion(const QString &row_version);
    bool is_row_version_Set() const;
    bool is_row_version_Valid() const;

    QString getSalutation() const;
    void setSalutation(const QString &salutation);
    bool is_salutation_Set() const;
    bool is_salutation_Valid() const;

    QList<OAISocialLink> getSocialLinks() const;
    void setSocialLinks(const QList<OAISocialLink> &social_links);
    bool is_social_links_Set() const;
    bool is_social_links_Valid() const;

    QString getSocialSecurityNumber() const;
    void setSocialSecurityNumber(const QString &social_security_number);
    bool is_social_security_number_Set() const;
    bool is_social_security_number_Valid() const;

    QString getSource() const;
    void setSource(const QString &source);
    bool is_source_Set() const;
    bool is_source_Valid() const;

    QString getSourceId() const;
    void setSourceId(const QString &source_id);
    bool is_source_id_Set() const;
    bool is_source_id_Valid() const;

    QList<QString> getTags() const;
    void setTags(const QList<QString> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    QString getTaxCode() const;
    void setTaxCode(const QString &tax_code);
    bool is_tax_code_Set() const;
    bool is_tax_code_Valid() const;

    QString getTaxId() const;
    void setTaxId(const QString &tax_id);
    bool is_tax_id_Set() const;
    bool is_tax_id_Valid() const;

    OAITeam getTeam() const;
    void setTeam(const OAITeam &team);
    bool is_team_Set() const;
    bool is_team_Valid() const;

    QString getTimezone() const;
    void setTimezone(const QString &timezone);
    bool is_timezone_Set() const;
    bool is_timezone_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    QString getUpdatedBy() const;
    void setUpdatedBy(const QString &updated_by);
    bool is_updated_by_Set() const;
    bool is_updated_by_Valid() const;

    bool isWorksRemote() const;
    void setWorksRemote(const bool &works_remote);
    bool is_works_remote_Set() const;
    bool is_works_remote_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIAddress> m_addresses;
    bool m_addresses_isSet;
    bool m_addresses_isValid;

    QList<OAIBankAccount> m_bank_accounts;
    bool m_bank_accounts_isSet;
    bool m_bank_accounts_isValid;

    QDate m_birthday;
    bool m_birthday_isSet;
    bool m_birthday_isValid;

    QString m_company_id;
    bool m_company_id_isSet;
    bool m_company_id_isValid;

    QString m_company_name;
    bool m_company_name_isSet;
    bool m_company_name_isValid;

    QList<OAIEmployeeCompensation> m_compensations;
    bool m_compensations_isSet;
    bool m_compensations_isValid;

    QString m_country_of_birth;
    bool m_country_of_birth_isSet;
    bool m_country_of_birth_isValid;

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_created_by;
    bool m_created_by_isSet;
    bool m_created_by_isValid;

    QList<OAICustomField> m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    OAIObject m_custom_mappings;
    bool m_custom_mappings_isSet;
    bool m_custom_mappings_isValid;

    QDate m_deceased_on;
    bool m_deceased_on_isSet;
    bool m_deceased_on_isValid;

    bool m_deleted;
    bool m_deleted_isSet;
    bool m_deleted_isValid;

    QString m_department;
    bool m_department_isSet;
    bool m_department_isValid;

    QString m_department_id;
    bool m_department_id_isSet;
    bool m_department_id_isValid;

    QString m_department_name;
    bool m_department_name_isSet;
    bool m_department_name_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_dietary_preference;
    bool m_dietary_preference_isSet;
    bool m_dietary_preference_isValid;

    QList<QString> m_direct_reports;
    bool m_direct_reports_isSet;
    bool m_direct_reports_isValid;

    QString m_display_name;
    bool m_display_name_isSet;
    bool m_display_name_isValid;

    QString m_division;
    bool m_division_isSet;
    bool m_division_isValid;

    QString m_division_id;
    bool m_division_id_isSet;
    bool m_division_id_isValid;

    QList<OAIEmail> m_emails;
    bool m_emails_isSet;
    bool m_emails_isValid;

    QString m_employee_number;
    bool m_employee_number_isSet;
    bool m_employee_number_isValid;

    QString m_employment_end_date;
    bool m_employment_end_date_isSet;
    bool m_employment_end_date_isValid;

    OAIEmployee_employment_role m_employment_role;
    bool m_employment_role_isSet;
    bool m_employment_role_isValid;

    QString m_employment_start_date;
    bool m_employment_start_date_isSet;
    bool m_employment_start_date_isValid;

    OAIEmploymentStatus m_employment_status;
    bool m_employment_status_isSet;
    bool m_employment_status_isValid;

    QString m_ethnicity;
    bool m_ethnicity_isSet;
    bool m_ethnicity_isValid;

    QString m_first_name;
    bool m_first_name_isSet;
    bool m_first_name_isValid;

    QList<QString> m_food_allergies;
    bool m_food_allergies_isSet;
    bool m_food_allergies_isValid;

    OAIGender m_gender;
    bool m_gender_isSet;
    bool m_gender_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_initials;
    bool m_initials_isSet;
    bool m_initials_isValid;

    QList<OAIEmployeeJob> m_jobs;
    bool m_jobs_isSet;
    bool m_jobs_isValid;

    QList<QString> m_languages;
    bool m_languages_isSet;
    bool m_languages_isValid;

    QString m_last_name;
    bool m_last_name_isSet;
    bool m_last_name_isValid;

    QString m_leaving_reason;
    bool m_leaving_reason_isSet;
    bool m_leaving_reason_isValid;

    OAIEmployee_manager m_manager;
    bool m_manager_isSet;
    bool m_manager_isValid;

    QString m_marital_status;
    bool m_marital_status_isSet;
    bool m_marital_status_isValid;

    QString m_middle_name;
    bool m_middle_name_isSet;
    bool m_middle_name_isValid;

    QList<QString> m_nationalities;
    bool m_nationalities_isSet;
    bool m_nationalities_isValid;

    OAIPerson m_partner;
    bool m_partner_isSet;
    bool m_partner_isValid;

    QList<OAIPhoneNumber> m_phone_numbers;
    bool m_phone_numbers_isSet;
    bool m_phone_numbers_isValid;

    QString m_photo_url;
    bool m_photo_url_isSet;
    bool m_photo_url_isValid;

    QString m_preferred_language;
    bool m_preferred_language_isSet;
    bool m_preferred_language_isValid;

    QString m_preferred_name;
    bool m_preferred_name_isSet;
    bool m_preferred_name_isValid;

    OAIProbation_period m_probation_period;
    bool m_probation_period_isSet;
    bool m_probation_period_isValid;

    QString m_pronouns;
    bool m_pronouns_isSet;
    bool m_pronouns_isValid;

    QString m_record_url;
    bool m_record_url_isSet;
    bool m_record_url_isValid;

    QString m_row_version;
    bool m_row_version_isSet;
    bool m_row_version_isValid;

    QString m_salutation;
    bool m_salutation_isSet;
    bool m_salutation_isValid;

    QList<OAISocialLink> m_social_links;
    bool m_social_links_isSet;
    bool m_social_links_isValid;

    QString m_social_security_number;
    bool m_social_security_number_isSet;
    bool m_social_security_number_isValid;

    QString m_source;
    bool m_source_isSet;
    bool m_source_isValid;

    QString m_source_id;
    bool m_source_id_isSet;
    bool m_source_id_isValid;

    QList<QString> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;

    QString m_tax_code;
    bool m_tax_code_isSet;
    bool m_tax_code_isValid;

    QString m_tax_id;
    bool m_tax_id_isSet;
    bool m_tax_id_isValid;

    OAITeam m_team;
    bool m_team_isSet;
    bool m_team_isValid;

    QString m_timezone;
    bool m_timezone_isSet;
    bool m_timezone_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    QString m_updated_by;
    bool m_updated_by_isSet;
    bool m_updated_by_isValid;

    bool m_works_remote;
    bool m_works_remote_isSet;
    bool m_works_remote_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIEmployee)

#endif // OAIEmployee_H
