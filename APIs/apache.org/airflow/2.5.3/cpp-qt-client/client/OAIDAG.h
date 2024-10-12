/**
 * Airflow API (Stable)
 * # Overview  To facilitate management, Apache Airflow supports a range of REST API endpoints across its objects. This section provides an overview of the API design, methods, and supported use cases.  Most of the endpoints accept `JSON` as input and return `JSON` responses. This means that you must usually add the following headers to your request: ``` Content-type: application/json Accept: application/json ```  ## Resources  The term `resource` refers to a single type of object in the Airflow metadata. An API is broken up by its endpoint's corresponding resource. The name of a resource is typically plural and expressed in camelCase. Example: `dagRuns`.  Resource names are used as part of endpoint URLs, as well as in API parameters and responses.  ## CRUD Operations  The platform supports **C**reate, **R**ead, **U**pdate, and **D**elete operations on most resources. You can review the standards for these operations and their standard parameters below.  Some endpoints have special behavior as exceptions.  ### Create  To create a resource, you typically submit an HTTP `POST` request with the resource's required metadata in the request body. The response returns a `201 Created` response code upon success with the resource's metadata, including its internal `id`, in the response body.  ### Read  The HTTP `GET` request can be used to read a resource or to list a number of resources.  A resource's `id` can be submitted in the request parameters to read a specific resource. The response usually returns a `200 OK` response code upon success, with the resource's metadata in the response body.  If a `GET` request does not include a specific resource `id`, it is treated as a list request. The response usually returns a `200 OK` response code upon success, with an object containing a list of resources' metadata in the response body.  When reading resources, some common query parameters are usually available. e.g.: ``` v1/connections?limit=25&offset=25 ```  |Query Parameter|Type|Description| |---------------|----|-----------| |limit|integer|Maximum number of objects to fetch. Usually 25 by default| |offset|integer|Offset after which to start returning objects. For use with limit query parameter.|  ### Update  Updating a resource requires the resource `id`, and is typically done using an HTTP `PATCH` request, with the fields to modify in the request body. The response usually returns a `200 OK` response code upon success, with information about the modified resource in the response body.  ### Delete  Deleting a resource requires the resource `id` and is typically executing via an HTTP `DELETE` request. The response usually returns a `204 No Content` response code upon success.  ## Conventions  - Resource names are plural and expressed in camelCase. - Names are consistent between URL parameter name and field name.  - Field names are in snake_case. ```json {     \"name\": \"string\",     \"slots\": 0,     \"occupied_slots\": 0,     \"used_slots\": 0,     \"queued_slots\": 0,     \"open_slots\": 0 } ```  ### Update Mask  Update mask is available as a query parameter in patch endpoints. It is used to notify the API which fields you want to update. Using `update_mask` makes it easier to update objects by helping the server know which fields to update in an object instead of updating all fields. The update request ignores any fields that aren't specified in the field mask, leaving them with their current values.  Example: ```   resource = request.get('/resource/my-id').json()   resource['my_field'] = 'new-value'   request.patch('/resource/my-id?update_mask=my_field', data=json.dumps(resource)) ```  ## Versioning and Endpoint Lifecycle  - API versioning is not synchronized to specific releases of the Apache Airflow. - APIs are designed to be backward compatible. - Any changes to the API will first go through a deprecation phase.  # Trying the API  You can use a third party client, such as [curl](https://curl.haxx.se/), [HTTPie](https://httpie.org/), [Postman](https://www.postman.com/) or [the Insomnia rest client](https://insomnia.rest/) to test the Apache Airflow API.  Note that you will need to pass credentials data.  For e.g., here is how to pause a DAG with [curl](https://curl.haxx.se/), when basic authorization is used: ```bash curl -X PATCH 'https://example.com/api/v1/dags/{dag_id}?update_mask=is_paused' \\ -H 'Content-Type: application/json' \\ --user \"username:password\" \\ -d '{     \"is_paused\": true }' ```  Using a graphical tool such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/), it is possible to import the API specifications directly:  1. Download the API specification by clicking the **Download** button at top of this document 2. Import the JSON specification in the graphical tool of your choice.   - In *Postman*, you can click the **import** button at the top   - With *Insomnia*, you can just drag-and-drop the file on the UI  Note that with *Postman*, you can also generate code snippets by selecting a request and clicking on the **Code** button.  ## Enabling CORS  [Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is a browser security feature that restricts HTTP requests that are initiated from scripts running in the browser.  For details on enabling/configuring CORS, see [Enabling CORS](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Authentication  To be able to meet the requirements of many organizations, Airflow supports many authentication methods, and it is even possible to add your own method.  If you want to check which auth backend is currently set, you can use `airflow config get-value api auth_backends` command as in the example below. ```bash $ airflow config get-value api auth_backends airflow.api.auth.backend.basic_auth ``` The default is to deny all requests.  For details on configuring the authentication, see [API Authorization](https://airflow.apache.org/docs/apache-airflow/stable/security/api.html).  # Errors  We follow the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs. As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Unauthenticated  This indicates that the request has not been applied because it lacks valid authentication credentials for the target resource. Please check that you have valid credentials.  ## PermissionDenied  This response means that the server understood the request but refuses to authorize it because it lacks sufficient rights to the resource. It happens when you do not have the necessary permission to execute the action you performed. You need to get the appropriate permissions in other to resolve this error.  ## BadRequest  This response means that the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). To resolve this, please ensure that your syntax is correct.  ## NotFound  This client error response indicates that the server cannot find the requested resource.  ## MethodNotAllowed  Indicates that the request method is known by the server but is not supported by the target resource.  ## NotAcceptable  The target resource does not have a current representation that would be acceptable to the user agent, according to the proactive negotiation header fields received in the request, and the server is unwilling to supply a default representation.  ## AlreadyExists  The request could not be completed due to a conflict with the current state of the target resource, e.g. the resource it tries to create already exists.  ## Unknown  This means that the server encountered an unexpected condition that prevented it from fulfilling the request. 
 *
 * The version of the OpenAPI document: 2.5.3
 * Contact: dev@airflow.apache.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDAG.h
 *
 * DAG
 */

#ifndef OAIDAG_H
#define OAIDAG_H

#include <QJsonObject>

#include "OAIScheduleInterval.h"
#include "OAITag.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIScheduleInterval;
class OAITag;

class OAIDAG : public OAIObject {
public:
    OAIDAG();
    OAIDAG(QString json);
    ~OAIDAG() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDagId() const;
    void setDagId(const QString &dag_id);
    bool is_dag_id_Set() const;
    bool is_dag_id_Valid() const;

    QString getDefaultView() const;
    void setDefaultView(const QString &default_view);
    bool is_default_view_Set() const;
    bool is_default_view_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getFileToken() const;
    void setFileToken(const QString &file_token);
    bool is_file_token_Set() const;
    bool is_file_token_Valid() const;

    QString getFileloc() const;
    void setFileloc(const QString &fileloc);
    bool is_fileloc_Set() const;
    bool is_fileloc_Valid() const;

    bool isHasImportErrors() const;
    void setHasImportErrors(const bool &has_import_errors);
    bool is_has_import_errors_Set() const;
    bool is_has_import_errors_Valid() const;

    bool isHasTaskConcurrencyLimits() const;
    void setHasTaskConcurrencyLimits(const bool &has_task_concurrency_limits);
    bool is_has_task_concurrency_limits_Set() const;
    bool is_has_task_concurrency_limits_Valid() const;

    bool isIsActive() const;
    void setIsActive(const bool &is_active);
    bool is_is_active_Set() const;
    bool is_is_active_Valid() const;

    bool isIsPaused() const;
    void setIsPaused(const bool &is_paused);
    bool is_is_paused_Set() const;
    bool is_is_paused_Valid() const;

    bool isIsSubdag() const;
    void setIsSubdag(const bool &is_subdag);
    bool is_is_subdag_Set() const;
    bool is_is_subdag_Valid() const;

    QDateTime getLastExpired() const;
    void setLastExpired(const QDateTime &last_expired);
    bool is_last_expired_Set() const;
    bool is_last_expired_Valid() const;

    QDateTime getLastParsedTime() const;
    void setLastParsedTime(const QDateTime &last_parsed_time);
    bool is_last_parsed_time_Set() const;
    bool is_last_parsed_time_Valid() const;

    QDateTime getLastPickled() const;
    void setLastPickled(const QDateTime &last_pickled);
    bool is_last_pickled_Set() const;
    bool is_last_pickled_Valid() const;

    qint32 getMaxActiveRuns() const;
    void setMaxActiveRuns(const qint32 &max_active_runs);
    bool is_max_active_runs_Set() const;
    bool is_max_active_runs_Valid() const;

    qint32 getMaxActiveTasks() const;
    void setMaxActiveTasks(const qint32 &max_active_tasks);
    bool is_max_active_tasks_Set() const;
    bool is_max_active_tasks_Valid() const;

    QDateTime getNextDagrun() const;
    void setNextDagrun(const QDateTime &next_dagrun);
    bool is_next_dagrun_Set() const;
    bool is_next_dagrun_Valid() const;

    QDateTime getNextDagrunCreateAfter() const;
    void setNextDagrunCreateAfter(const QDateTime &next_dagrun_create_after);
    bool is_next_dagrun_create_after_Set() const;
    bool is_next_dagrun_create_after_Valid() const;

    QDateTime getNextDagrunDataIntervalEnd() const;
    void setNextDagrunDataIntervalEnd(const QDateTime &next_dagrun_data_interval_end);
    bool is_next_dagrun_data_interval_end_Set() const;
    bool is_next_dagrun_data_interval_end_Valid() const;

    QDateTime getNextDagrunDataIntervalStart() const;
    void setNextDagrunDataIntervalStart(const QDateTime &next_dagrun_data_interval_start);
    bool is_next_dagrun_data_interval_start_Set() const;
    bool is_next_dagrun_data_interval_start_Valid() const;

    QList<QString> getOwners() const;
    void setOwners(const QList<QString> &owners);
    bool is_owners_Set() const;
    bool is_owners_Valid() const;

    QString getPickleId() const;
    void setPickleId(const QString &pickle_id);
    bool is_pickle_id_Set() const;
    bool is_pickle_id_Valid() const;

    QString getRootDagId() const;
    void setRootDagId(const QString &root_dag_id);
    bool is_root_dag_id_Set() const;
    bool is_root_dag_id_Valid() const;

    OAIScheduleInterval getScheduleInterval() const;
    void setScheduleInterval(const OAIScheduleInterval &schedule_interval);
    bool is_schedule_interval_Set() const;
    bool is_schedule_interval_Valid() const;

    bool isSchedulerLock() const;
    void setSchedulerLock(const bool &scheduler_lock);
    bool is_scheduler_lock_Set() const;
    bool is_scheduler_lock_Valid() const;

    QList<OAITag> getTags() const;
    void setTags(const QList<OAITag> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    QString getTimetableDescription() const;
    void setTimetableDescription(const QString &timetable_description);
    bool is_timetable_description_Set() const;
    bool is_timetable_description_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_dag_id;
    bool m_dag_id_isSet;
    bool m_dag_id_isValid;

    QString m_default_view;
    bool m_default_view_isSet;
    bool m_default_view_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_file_token;
    bool m_file_token_isSet;
    bool m_file_token_isValid;

    QString m_fileloc;
    bool m_fileloc_isSet;
    bool m_fileloc_isValid;

    bool m_has_import_errors;
    bool m_has_import_errors_isSet;
    bool m_has_import_errors_isValid;

    bool m_has_task_concurrency_limits;
    bool m_has_task_concurrency_limits_isSet;
    bool m_has_task_concurrency_limits_isValid;

    bool m_is_active;
    bool m_is_active_isSet;
    bool m_is_active_isValid;

    bool m_is_paused;
    bool m_is_paused_isSet;
    bool m_is_paused_isValid;

    bool m_is_subdag;
    bool m_is_subdag_isSet;
    bool m_is_subdag_isValid;

    QDateTime m_last_expired;
    bool m_last_expired_isSet;
    bool m_last_expired_isValid;

    QDateTime m_last_parsed_time;
    bool m_last_parsed_time_isSet;
    bool m_last_parsed_time_isValid;

    QDateTime m_last_pickled;
    bool m_last_pickled_isSet;
    bool m_last_pickled_isValid;

    qint32 m_max_active_runs;
    bool m_max_active_runs_isSet;
    bool m_max_active_runs_isValid;

    qint32 m_max_active_tasks;
    bool m_max_active_tasks_isSet;
    bool m_max_active_tasks_isValid;

    QDateTime m_next_dagrun;
    bool m_next_dagrun_isSet;
    bool m_next_dagrun_isValid;

    QDateTime m_next_dagrun_create_after;
    bool m_next_dagrun_create_after_isSet;
    bool m_next_dagrun_create_after_isValid;

    QDateTime m_next_dagrun_data_interval_end;
    bool m_next_dagrun_data_interval_end_isSet;
    bool m_next_dagrun_data_interval_end_isValid;

    QDateTime m_next_dagrun_data_interval_start;
    bool m_next_dagrun_data_interval_start_isSet;
    bool m_next_dagrun_data_interval_start_isValid;

    QList<QString> m_owners;
    bool m_owners_isSet;
    bool m_owners_isValid;

    QString m_pickle_id;
    bool m_pickle_id_isSet;
    bool m_pickle_id_isValid;

    QString m_root_dag_id;
    bool m_root_dag_id_isSet;
    bool m_root_dag_id_isValid;

    OAIScheduleInterval m_schedule_interval;
    bool m_schedule_interval_isSet;
    bool m_schedule_interval_isValid;

    bool m_scheduler_lock;
    bool m_scheduler_lock_isSet;
    bool m_scheduler_lock_isValid;

    QList<OAITag> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;

    QString m_timetable_description;
    bool m_timetable_description_isSet;
    bool m_timetable_description_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDAG)

#endif // OAIDAG_H
