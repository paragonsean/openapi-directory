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

/*
 * OAIActivity.h
 *
 * 
 */

#ifndef OAIActivity_H
#define OAIActivity_H

#include <QJsonObject>

#include "OAIActivityAttendee.h"
#include "OAIAddress.h"
#include "OAICustomField.h"
#include "OAIObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIActivityAttendee;
class OAICustomField;
class OAIAddress;

class OAIActivity : public OAIObject {
public:
    OAIActivity();
    OAIActivity(QString json);
    ~OAIActivity() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccountId() const;
    void setAccountId(const QString &account_id);
    bool is_account_id_Set() const;
    bool is_account_id_Valid() const;

    QString getActivityDate() const;
    void setActivityDate(const QString &activity_date);
    bool is_activity_date_Set() const;
    bool is_activity_date_Valid() const;

    QString getActivityDatetime() const;
    void setActivityDatetime(const QString &activity_datetime);
    bool is_activity_datetime_Set() const;
    bool is_activity_datetime_Valid() const;

    bool isAllDayEvent() const;
    void setAllDayEvent(const bool &all_day_event);
    bool is_all_day_event_Set() const;
    bool is_all_day_event_Valid() const;

    bool isArchived() const;
    void setArchived(const bool &archived);
    bool is_archived_Set() const;
    bool is_archived_Valid() const;

    QString getAssetId() const;
    void setAssetId(const QString &asset_id);
    bool is_asset_id_Set() const;
    bool is_asset_id_Valid() const;

    QList<OAIActivityAttendee> getAttendees() const;
    void setAttendees(const QList<OAIActivityAttendee> &attendees);
    bool is_attendees_Set() const;
    bool is_attendees_Valid() const;

    QString getCampaignId() const;
    void setCampaignId(const QString &campaign_id);
    bool is_campaign_id_Set() const;
    bool is_campaign_id_Valid() const;

    QString getCaseId() const;
    void setCaseId(const QString &case_id);
    bool is_case_id_Set() const;
    bool is_case_id_Valid() const;

    bool isChild() const;
    void setChild(const bool &child);
    bool is_child_Set() const;
    bool is_child_Valid() const;

    QString getCompanyId() const;
    void setCompanyId(const QString &company_id);
    bool is_company_id_Set() const;
    bool is_company_id_Valid() const;

    QString getContactId() const;
    void setContactId(const QString &contact_id);
    bool is_contact_id_Set() const;
    bool is_contact_id_Valid() const;

    QString getContractId() const;
    void setContractId(const QString &contract_id);
    bool is_contract_id_Set() const;
    bool is_contract_id_Valid() const;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
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

    QString getCustomObjectId() const;
    void setCustomObjectId(const QString &custom_object_id);
    bool is_custom_object_id_Set() const;
    bool is_custom_object_id_Valid() const;

    bool isDeleted() const;
    void setDeleted(const bool &deleted);
    bool is_deleted_Set() const;
    bool is_deleted_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    bool isDone() const;
    void setDone(const bool &done);
    bool is_done_Set() const;
    bool is_done_Valid() const;

    QString getDownstreamId() const;
    void setDownstreamId(const QString &downstream_id);
    bool is_downstream_id_Set() const;
    bool is_downstream_id_Valid() const;

    qint32 getDurationMinutes() const;
    void setDurationMinutes(const qint32 &duration_minutes);
    bool is_duration_minutes_Set() const;
    bool is_duration_minutes_Valid() const;

    qint32 getDurationSeconds() const;
    void setDurationSeconds(const qint32 &duration_seconds);
    bool is_duration_seconds_Set() const;
    bool is_duration_seconds_Valid() const;

    QString getEndDate() const;
    void setEndDate(const QString &end_date);
    bool is_end_date_Set() const;
    bool is_end_date_Valid() const;

    QString getEndDatetime() const;
    void setEndDatetime(const QString &end_datetime);
    bool is_end_datetime_Set() const;
    bool is_end_datetime_Valid() const;

    QString getEventSubType() const;
    void setEventSubType(const QString &event_sub_type);
    bool is_event_sub_type_Set() const;
    bool is_event_sub_type_Valid() const;

    bool isGroupEvent() const;
    void setGroupEvent(const bool &group_event);
    bool is_group_event_Set() const;
    bool is_group_event_Valid() const;

    QString getGroupEventType() const;
    void setGroupEventType(const QString &group_event_type);
    bool is_group_event_type_Set() const;
    bool is_group_event_type_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getLeadId() const;
    void setLeadId(const QString &lead_id);
    bool is_lead_id_Set() const;
    bool is_lead_id_Valid() const;

    QString getLocation() const;
    void setLocation(const QString &location);
    bool is_location_Set() const;
    bool is_location_Valid() const;

    OAIAddress getLocationAddress() const;
    void setLocationAddress(const OAIAddress &location_address);
    bool is_location_address_Set() const;
    bool is_location_address_Valid() const;

    QString getNote() const;
    void setNote(const QString &note);
    bool is_note_Set() const;
    bool is_note_Valid() const;

    QString getOpportunityId() const;
    void setOpportunityId(const QString &opportunity_id);
    bool is_opportunity_id_Set() const;
    bool is_opportunity_id_Valid() const;

    QString getOwnerId() const;
    void setOwnerId(const QString &owner_id);
    bool is_owner_id_Set() const;
    bool is_owner_id_Valid() const;

    bool isRPrivate() const;
    void setRPrivate(const bool &r_private);
    bool is_r_private_Set() const;
    bool is_r_private_Valid() const;

    QString getProductId() const;
    void setProductId(const QString &product_id);
    bool is_product_id_Set() const;
    bool is_product_id_Valid() const;

    bool isRecurrent() const;
    void setRecurrent(const bool &recurrent);
    bool is_recurrent_Set() const;
    bool is_recurrent_Valid() const;

    QString getReminderDatetime() const;
    void setReminderDatetime(const QString &reminder_datetime);
    bool is_reminder_datetime_Set() const;
    bool is_reminder_datetime_Valid() const;

    bool isReminderSet() const;
    void setReminderSet(const bool &reminder_set);
    bool is_reminder_set_Set() const;
    bool is_reminder_set_Valid() const;

    QString getShowAs() const;
    void setShowAs(const QString &show_as);
    bool is_show_as_Set() const;
    bool is_show_as_Valid() const;

    QString getSolutionId() const;
    void setSolutionId(const QString &solution_id);
    bool is_solution_id_Set() const;
    bool is_solution_id_Valid() const;

    QString getStartDatetime() const;
    void setStartDatetime(const QString &start_datetime);
    bool is_start_datetime_Set() const;
    bool is_start_datetime_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getUpdatedAt() const;
    void setUpdatedAt(const QString &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    QString getUpdatedBy() const;
    void setUpdatedBy(const QString &updated_by);
    bool is_updated_by_Set() const;
    bool is_updated_by_Valid() const;

    QString getUserId() const;
    void setUserId(const QString &user_id);
    bool is_user_id_Set() const;
    bool is_user_id_Valid() const;

    QString getVideoConferenceId() const;
    void setVideoConferenceId(const QString &video_conference_id);
    bool is_video_conference_id_Set() const;
    bool is_video_conference_id_Valid() const;

    QString getVideoConferenceUrl() const;
    void setVideoConferenceUrl(const QString &video_conference_url);
    bool is_video_conference_url_Set() const;
    bool is_video_conference_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_account_id;
    bool m_account_id_isSet;
    bool m_account_id_isValid;

    QString m_activity_date;
    bool m_activity_date_isSet;
    bool m_activity_date_isValid;

    QString m_activity_datetime;
    bool m_activity_datetime_isSet;
    bool m_activity_datetime_isValid;

    bool m_all_day_event;
    bool m_all_day_event_isSet;
    bool m_all_day_event_isValid;

    bool m_archived;
    bool m_archived_isSet;
    bool m_archived_isValid;

    QString m_asset_id;
    bool m_asset_id_isSet;
    bool m_asset_id_isValid;

    QList<OAIActivityAttendee> m_attendees;
    bool m_attendees_isSet;
    bool m_attendees_isValid;

    QString m_campaign_id;
    bool m_campaign_id_isSet;
    bool m_campaign_id_isValid;

    QString m_case_id;
    bool m_case_id_isSet;
    bool m_case_id_isValid;

    bool m_child;
    bool m_child_isSet;
    bool m_child_isValid;

    QString m_company_id;
    bool m_company_id_isSet;
    bool m_company_id_isValid;

    QString m_contact_id;
    bool m_contact_id_isSet;
    bool m_contact_id_isValid;

    QString m_contract_id;
    bool m_contract_id_isSet;
    bool m_contract_id_isValid;

    QString m_created_at;
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

    QString m_custom_object_id;
    bool m_custom_object_id_isSet;
    bool m_custom_object_id_isValid;

    bool m_deleted;
    bool m_deleted_isSet;
    bool m_deleted_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    bool m_done;
    bool m_done_isSet;
    bool m_done_isValid;

    QString m_downstream_id;
    bool m_downstream_id_isSet;
    bool m_downstream_id_isValid;

    qint32 m_duration_minutes;
    bool m_duration_minutes_isSet;
    bool m_duration_minutes_isValid;

    qint32 m_duration_seconds;
    bool m_duration_seconds_isSet;
    bool m_duration_seconds_isValid;

    QString m_end_date;
    bool m_end_date_isSet;
    bool m_end_date_isValid;

    QString m_end_datetime;
    bool m_end_datetime_isSet;
    bool m_end_datetime_isValid;

    QString m_event_sub_type;
    bool m_event_sub_type_isSet;
    bool m_event_sub_type_isValid;

    bool m_group_event;
    bool m_group_event_isSet;
    bool m_group_event_isValid;

    QString m_group_event_type;
    bool m_group_event_type_isSet;
    bool m_group_event_type_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_lead_id;
    bool m_lead_id_isSet;
    bool m_lead_id_isValid;

    QString m_location;
    bool m_location_isSet;
    bool m_location_isValid;

    OAIAddress m_location_address;
    bool m_location_address_isSet;
    bool m_location_address_isValid;

    QString m_note;
    bool m_note_isSet;
    bool m_note_isValid;

    QString m_opportunity_id;
    bool m_opportunity_id_isSet;
    bool m_opportunity_id_isValid;

    QString m_owner_id;
    bool m_owner_id_isSet;
    bool m_owner_id_isValid;

    bool m_r_private;
    bool m_r_private_isSet;
    bool m_r_private_isValid;

    QString m_product_id;
    bool m_product_id_isSet;
    bool m_product_id_isValid;

    bool m_recurrent;
    bool m_recurrent_isSet;
    bool m_recurrent_isValid;

    QString m_reminder_datetime;
    bool m_reminder_datetime_isSet;
    bool m_reminder_datetime_isValid;

    bool m_reminder_set;
    bool m_reminder_set_isSet;
    bool m_reminder_set_isValid;

    QString m_show_as;
    bool m_show_as_isSet;
    bool m_show_as_isValid;

    QString m_solution_id;
    bool m_solution_id_isSet;
    bool m_solution_id_isValid;

    QString m_start_datetime;
    bool m_start_datetime_isSet;
    bool m_start_datetime_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    QString m_updated_by;
    bool m_updated_by_isSet;
    bool m_updated_by_isValid;

    QString m_user_id;
    bool m_user_id_isSet;
    bool m_user_id_isValid;

    QString m_video_conference_id;
    bool m_video_conference_id_isSet;
    bool m_video_conference_id_isValid;

    QString m_video_conference_url;
    bool m_video_conference_url_isSet;
    bool m_video_conference_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIActivity)

#endif // OAIActivity_H
