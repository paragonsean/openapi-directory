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

#include "OAIDAG.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDAG::OAIDAG(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDAG::OAIDAG() {
    this->initializeModel();
}

OAIDAG::~OAIDAG() {}

void OAIDAG::initializeModel() {

    m_dag_id_isSet = false;
    m_dag_id_isValid = false;

    m_default_view_isSet = false;
    m_default_view_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_file_token_isSet = false;
    m_file_token_isValid = false;

    m_fileloc_isSet = false;
    m_fileloc_isValid = false;

    m_has_import_errors_isSet = false;
    m_has_import_errors_isValid = false;

    m_has_task_concurrency_limits_isSet = false;
    m_has_task_concurrency_limits_isValid = false;

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_is_paused_isSet = false;
    m_is_paused_isValid = false;

    m_is_subdag_isSet = false;
    m_is_subdag_isValid = false;

    m_last_expired_isSet = false;
    m_last_expired_isValid = false;

    m_last_parsed_time_isSet = false;
    m_last_parsed_time_isValid = false;

    m_last_pickled_isSet = false;
    m_last_pickled_isValid = false;

    m_max_active_runs_isSet = false;
    m_max_active_runs_isValid = false;

    m_max_active_tasks_isSet = false;
    m_max_active_tasks_isValid = false;

    m_next_dagrun_isSet = false;
    m_next_dagrun_isValid = false;

    m_next_dagrun_create_after_isSet = false;
    m_next_dagrun_create_after_isValid = false;

    m_next_dagrun_data_interval_end_isSet = false;
    m_next_dagrun_data_interval_end_isValid = false;

    m_next_dagrun_data_interval_start_isSet = false;
    m_next_dagrun_data_interval_start_isValid = false;

    m_owners_isSet = false;
    m_owners_isValid = false;

    m_pickle_id_isSet = false;
    m_pickle_id_isValid = false;

    m_root_dag_id_isSet = false;
    m_root_dag_id_isValid = false;

    m_schedule_interval_isSet = false;
    m_schedule_interval_isValid = false;

    m_scheduler_lock_isSet = false;
    m_scheduler_lock_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_timetable_description_isSet = false;
    m_timetable_description_isValid = false;
}

void OAIDAG::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDAG::fromJsonObject(QJsonObject json) {

    m_dag_id_isValid = ::OpenAPI::fromJsonValue(m_dag_id, json[QString("dag_id")]);
    m_dag_id_isSet = !json[QString("dag_id")].isNull() && m_dag_id_isValid;

    m_default_view_isValid = ::OpenAPI::fromJsonValue(m_default_view, json[QString("default_view")]);
    m_default_view_isSet = !json[QString("default_view")].isNull() && m_default_view_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_file_token_isValid = ::OpenAPI::fromJsonValue(m_file_token, json[QString("file_token")]);
    m_file_token_isSet = !json[QString("file_token")].isNull() && m_file_token_isValid;

    m_fileloc_isValid = ::OpenAPI::fromJsonValue(m_fileloc, json[QString("fileloc")]);
    m_fileloc_isSet = !json[QString("fileloc")].isNull() && m_fileloc_isValid;

    m_has_import_errors_isValid = ::OpenAPI::fromJsonValue(m_has_import_errors, json[QString("has_import_errors")]);
    m_has_import_errors_isSet = !json[QString("has_import_errors")].isNull() && m_has_import_errors_isValid;

    m_has_task_concurrency_limits_isValid = ::OpenAPI::fromJsonValue(m_has_task_concurrency_limits, json[QString("has_task_concurrency_limits")]);
    m_has_task_concurrency_limits_isSet = !json[QString("has_task_concurrency_limits")].isNull() && m_has_task_concurrency_limits_isValid;

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("is_active")]);
    m_is_active_isSet = !json[QString("is_active")].isNull() && m_is_active_isValid;

    m_is_paused_isValid = ::OpenAPI::fromJsonValue(m_is_paused, json[QString("is_paused")]);
    m_is_paused_isSet = !json[QString("is_paused")].isNull() && m_is_paused_isValid;

    m_is_subdag_isValid = ::OpenAPI::fromJsonValue(m_is_subdag, json[QString("is_subdag")]);
    m_is_subdag_isSet = !json[QString("is_subdag")].isNull() && m_is_subdag_isValid;

    m_last_expired_isValid = ::OpenAPI::fromJsonValue(m_last_expired, json[QString("last_expired")]);
    m_last_expired_isSet = !json[QString("last_expired")].isNull() && m_last_expired_isValid;

    m_last_parsed_time_isValid = ::OpenAPI::fromJsonValue(m_last_parsed_time, json[QString("last_parsed_time")]);
    m_last_parsed_time_isSet = !json[QString("last_parsed_time")].isNull() && m_last_parsed_time_isValid;

    m_last_pickled_isValid = ::OpenAPI::fromJsonValue(m_last_pickled, json[QString("last_pickled")]);
    m_last_pickled_isSet = !json[QString("last_pickled")].isNull() && m_last_pickled_isValid;

    m_max_active_runs_isValid = ::OpenAPI::fromJsonValue(m_max_active_runs, json[QString("max_active_runs")]);
    m_max_active_runs_isSet = !json[QString("max_active_runs")].isNull() && m_max_active_runs_isValid;

    m_max_active_tasks_isValid = ::OpenAPI::fromJsonValue(m_max_active_tasks, json[QString("max_active_tasks")]);
    m_max_active_tasks_isSet = !json[QString("max_active_tasks")].isNull() && m_max_active_tasks_isValid;

    m_next_dagrun_isValid = ::OpenAPI::fromJsonValue(m_next_dagrun, json[QString("next_dagrun")]);
    m_next_dagrun_isSet = !json[QString("next_dagrun")].isNull() && m_next_dagrun_isValid;

    m_next_dagrun_create_after_isValid = ::OpenAPI::fromJsonValue(m_next_dagrun_create_after, json[QString("next_dagrun_create_after")]);
    m_next_dagrun_create_after_isSet = !json[QString("next_dagrun_create_after")].isNull() && m_next_dagrun_create_after_isValid;

    m_next_dagrun_data_interval_end_isValid = ::OpenAPI::fromJsonValue(m_next_dagrun_data_interval_end, json[QString("next_dagrun_data_interval_end")]);
    m_next_dagrun_data_interval_end_isSet = !json[QString("next_dagrun_data_interval_end")].isNull() && m_next_dagrun_data_interval_end_isValid;

    m_next_dagrun_data_interval_start_isValid = ::OpenAPI::fromJsonValue(m_next_dagrun_data_interval_start, json[QString("next_dagrun_data_interval_start")]);
    m_next_dagrun_data_interval_start_isSet = !json[QString("next_dagrun_data_interval_start")].isNull() && m_next_dagrun_data_interval_start_isValid;

    m_owners_isValid = ::OpenAPI::fromJsonValue(m_owners, json[QString("owners")]);
    m_owners_isSet = !json[QString("owners")].isNull() && m_owners_isValid;

    m_pickle_id_isValid = ::OpenAPI::fromJsonValue(m_pickle_id, json[QString("pickle_id")]);
    m_pickle_id_isSet = !json[QString("pickle_id")].isNull() && m_pickle_id_isValid;

    m_root_dag_id_isValid = ::OpenAPI::fromJsonValue(m_root_dag_id, json[QString("root_dag_id")]);
    m_root_dag_id_isSet = !json[QString("root_dag_id")].isNull() && m_root_dag_id_isValid;

    m_schedule_interval_isValid = ::OpenAPI::fromJsonValue(m_schedule_interval, json[QString("schedule_interval")]);
    m_schedule_interval_isSet = !json[QString("schedule_interval")].isNull() && m_schedule_interval_isValid;

    m_scheduler_lock_isValid = ::OpenAPI::fromJsonValue(m_scheduler_lock, json[QString("scheduler_lock")]);
    m_scheduler_lock_isSet = !json[QString("scheduler_lock")].isNull() && m_scheduler_lock_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_timetable_description_isValid = ::OpenAPI::fromJsonValue(m_timetable_description, json[QString("timetable_description")]);
    m_timetable_description_isSet = !json[QString("timetable_description")].isNull() && m_timetable_description_isValid;
}

QString OAIDAG::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDAG::asJsonObject() const {
    QJsonObject obj;
    if (m_dag_id_isSet) {
        obj.insert(QString("dag_id"), ::OpenAPI::toJsonValue(m_dag_id));
    }
    if (m_default_view_isSet) {
        obj.insert(QString("default_view"), ::OpenAPI::toJsonValue(m_default_view));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_file_token_isSet) {
        obj.insert(QString("file_token"), ::OpenAPI::toJsonValue(m_file_token));
    }
    if (m_fileloc_isSet) {
        obj.insert(QString("fileloc"), ::OpenAPI::toJsonValue(m_fileloc));
    }
    if (m_has_import_errors_isSet) {
        obj.insert(QString("has_import_errors"), ::OpenAPI::toJsonValue(m_has_import_errors));
    }
    if (m_has_task_concurrency_limits_isSet) {
        obj.insert(QString("has_task_concurrency_limits"), ::OpenAPI::toJsonValue(m_has_task_concurrency_limits));
    }
    if (m_is_active_isSet) {
        obj.insert(QString("is_active"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_is_paused_isSet) {
        obj.insert(QString("is_paused"), ::OpenAPI::toJsonValue(m_is_paused));
    }
    if (m_is_subdag_isSet) {
        obj.insert(QString("is_subdag"), ::OpenAPI::toJsonValue(m_is_subdag));
    }
    if (m_last_expired_isSet) {
        obj.insert(QString("last_expired"), ::OpenAPI::toJsonValue(m_last_expired));
    }
    if (m_last_parsed_time_isSet) {
        obj.insert(QString("last_parsed_time"), ::OpenAPI::toJsonValue(m_last_parsed_time));
    }
    if (m_last_pickled_isSet) {
        obj.insert(QString("last_pickled"), ::OpenAPI::toJsonValue(m_last_pickled));
    }
    if (m_max_active_runs_isSet) {
        obj.insert(QString("max_active_runs"), ::OpenAPI::toJsonValue(m_max_active_runs));
    }
    if (m_max_active_tasks_isSet) {
        obj.insert(QString("max_active_tasks"), ::OpenAPI::toJsonValue(m_max_active_tasks));
    }
    if (m_next_dagrun_isSet) {
        obj.insert(QString("next_dagrun"), ::OpenAPI::toJsonValue(m_next_dagrun));
    }
    if (m_next_dagrun_create_after_isSet) {
        obj.insert(QString("next_dagrun_create_after"), ::OpenAPI::toJsonValue(m_next_dagrun_create_after));
    }
    if (m_next_dagrun_data_interval_end_isSet) {
        obj.insert(QString("next_dagrun_data_interval_end"), ::OpenAPI::toJsonValue(m_next_dagrun_data_interval_end));
    }
    if (m_next_dagrun_data_interval_start_isSet) {
        obj.insert(QString("next_dagrun_data_interval_start"), ::OpenAPI::toJsonValue(m_next_dagrun_data_interval_start));
    }
    if (m_owners.size() > 0) {
        obj.insert(QString("owners"), ::OpenAPI::toJsonValue(m_owners));
    }
    if (m_pickle_id_isSet) {
        obj.insert(QString("pickle_id"), ::OpenAPI::toJsonValue(m_pickle_id));
    }
    if (m_root_dag_id_isSet) {
        obj.insert(QString("root_dag_id"), ::OpenAPI::toJsonValue(m_root_dag_id));
    }
    if (m_schedule_interval.isSet()) {
        obj.insert(QString("schedule_interval"), ::OpenAPI::toJsonValue(m_schedule_interval));
    }
    if (m_scheduler_lock_isSet) {
        obj.insert(QString("scheduler_lock"), ::OpenAPI::toJsonValue(m_scheduler_lock));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_timetable_description_isSet) {
        obj.insert(QString("timetable_description"), ::OpenAPI::toJsonValue(m_timetable_description));
    }
    return obj;
}

QString OAIDAG::getDagId() const {
    return m_dag_id;
}
void OAIDAG::setDagId(const QString &dag_id) {
    m_dag_id = dag_id;
    m_dag_id_isSet = true;
}

bool OAIDAG::is_dag_id_Set() const{
    return m_dag_id_isSet;
}

bool OAIDAG::is_dag_id_Valid() const{
    return m_dag_id_isValid;
}

QString OAIDAG::getDefaultView() const {
    return m_default_view;
}
void OAIDAG::setDefaultView(const QString &default_view) {
    m_default_view = default_view;
    m_default_view_isSet = true;
}

bool OAIDAG::is_default_view_Set() const{
    return m_default_view_isSet;
}

bool OAIDAG::is_default_view_Valid() const{
    return m_default_view_isValid;
}

QString OAIDAG::getDescription() const {
    return m_description;
}
void OAIDAG::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIDAG::is_description_Set() const{
    return m_description_isSet;
}

bool OAIDAG::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIDAG::getFileToken() const {
    return m_file_token;
}
void OAIDAG::setFileToken(const QString &file_token) {
    m_file_token = file_token;
    m_file_token_isSet = true;
}

bool OAIDAG::is_file_token_Set() const{
    return m_file_token_isSet;
}

bool OAIDAG::is_file_token_Valid() const{
    return m_file_token_isValid;
}

QString OAIDAG::getFileloc() const {
    return m_fileloc;
}
void OAIDAG::setFileloc(const QString &fileloc) {
    m_fileloc = fileloc;
    m_fileloc_isSet = true;
}

bool OAIDAG::is_fileloc_Set() const{
    return m_fileloc_isSet;
}

bool OAIDAG::is_fileloc_Valid() const{
    return m_fileloc_isValid;
}

bool OAIDAG::isHasImportErrors() const {
    return m_has_import_errors;
}
void OAIDAG::setHasImportErrors(const bool &has_import_errors) {
    m_has_import_errors = has_import_errors;
    m_has_import_errors_isSet = true;
}

bool OAIDAG::is_has_import_errors_Set() const{
    return m_has_import_errors_isSet;
}

bool OAIDAG::is_has_import_errors_Valid() const{
    return m_has_import_errors_isValid;
}

bool OAIDAG::isHasTaskConcurrencyLimits() const {
    return m_has_task_concurrency_limits;
}
void OAIDAG::setHasTaskConcurrencyLimits(const bool &has_task_concurrency_limits) {
    m_has_task_concurrency_limits = has_task_concurrency_limits;
    m_has_task_concurrency_limits_isSet = true;
}

bool OAIDAG::is_has_task_concurrency_limits_Set() const{
    return m_has_task_concurrency_limits_isSet;
}

bool OAIDAG::is_has_task_concurrency_limits_Valid() const{
    return m_has_task_concurrency_limits_isValid;
}

bool OAIDAG::isIsActive() const {
    return m_is_active;
}
void OAIDAG::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAIDAG::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAIDAG::is_is_active_Valid() const{
    return m_is_active_isValid;
}

bool OAIDAG::isIsPaused() const {
    return m_is_paused;
}
void OAIDAG::setIsPaused(const bool &is_paused) {
    m_is_paused = is_paused;
    m_is_paused_isSet = true;
}

bool OAIDAG::is_is_paused_Set() const{
    return m_is_paused_isSet;
}

bool OAIDAG::is_is_paused_Valid() const{
    return m_is_paused_isValid;
}

bool OAIDAG::isIsSubdag() const {
    return m_is_subdag;
}
void OAIDAG::setIsSubdag(const bool &is_subdag) {
    m_is_subdag = is_subdag;
    m_is_subdag_isSet = true;
}

bool OAIDAG::is_is_subdag_Set() const{
    return m_is_subdag_isSet;
}

bool OAIDAG::is_is_subdag_Valid() const{
    return m_is_subdag_isValid;
}

QDateTime OAIDAG::getLastExpired() const {
    return m_last_expired;
}
void OAIDAG::setLastExpired(const QDateTime &last_expired) {
    m_last_expired = last_expired;
    m_last_expired_isSet = true;
}

bool OAIDAG::is_last_expired_Set() const{
    return m_last_expired_isSet;
}

bool OAIDAG::is_last_expired_Valid() const{
    return m_last_expired_isValid;
}

QDateTime OAIDAG::getLastParsedTime() const {
    return m_last_parsed_time;
}
void OAIDAG::setLastParsedTime(const QDateTime &last_parsed_time) {
    m_last_parsed_time = last_parsed_time;
    m_last_parsed_time_isSet = true;
}

bool OAIDAG::is_last_parsed_time_Set() const{
    return m_last_parsed_time_isSet;
}

bool OAIDAG::is_last_parsed_time_Valid() const{
    return m_last_parsed_time_isValid;
}

QDateTime OAIDAG::getLastPickled() const {
    return m_last_pickled;
}
void OAIDAG::setLastPickled(const QDateTime &last_pickled) {
    m_last_pickled = last_pickled;
    m_last_pickled_isSet = true;
}

bool OAIDAG::is_last_pickled_Set() const{
    return m_last_pickled_isSet;
}

bool OAIDAG::is_last_pickled_Valid() const{
    return m_last_pickled_isValid;
}

qint32 OAIDAG::getMaxActiveRuns() const {
    return m_max_active_runs;
}
void OAIDAG::setMaxActiveRuns(const qint32 &max_active_runs) {
    m_max_active_runs = max_active_runs;
    m_max_active_runs_isSet = true;
}

bool OAIDAG::is_max_active_runs_Set() const{
    return m_max_active_runs_isSet;
}

bool OAIDAG::is_max_active_runs_Valid() const{
    return m_max_active_runs_isValid;
}

qint32 OAIDAG::getMaxActiveTasks() const {
    return m_max_active_tasks;
}
void OAIDAG::setMaxActiveTasks(const qint32 &max_active_tasks) {
    m_max_active_tasks = max_active_tasks;
    m_max_active_tasks_isSet = true;
}

bool OAIDAG::is_max_active_tasks_Set() const{
    return m_max_active_tasks_isSet;
}

bool OAIDAG::is_max_active_tasks_Valid() const{
    return m_max_active_tasks_isValid;
}

QDateTime OAIDAG::getNextDagrun() const {
    return m_next_dagrun;
}
void OAIDAG::setNextDagrun(const QDateTime &next_dagrun) {
    m_next_dagrun = next_dagrun;
    m_next_dagrun_isSet = true;
}

bool OAIDAG::is_next_dagrun_Set() const{
    return m_next_dagrun_isSet;
}

bool OAIDAG::is_next_dagrun_Valid() const{
    return m_next_dagrun_isValid;
}

QDateTime OAIDAG::getNextDagrunCreateAfter() const {
    return m_next_dagrun_create_after;
}
void OAIDAG::setNextDagrunCreateAfter(const QDateTime &next_dagrun_create_after) {
    m_next_dagrun_create_after = next_dagrun_create_after;
    m_next_dagrun_create_after_isSet = true;
}

bool OAIDAG::is_next_dagrun_create_after_Set() const{
    return m_next_dagrun_create_after_isSet;
}

bool OAIDAG::is_next_dagrun_create_after_Valid() const{
    return m_next_dagrun_create_after_isValid;
}

QDateTime OAIDAG::getNextDagrunDataIntervalEnd() const {
    return m_next_dagrun_data_interval_end;
}
void OAIDAG::setNextDagrunDataIntervalEnd(const QDateTime &next_dagrun_data_interval_end) {
    m_next_dagrun_data_interval_end = next_dagrun_data_interval_end;
    m_next_dagrun_data_interval_end_isSet = true;
}

bool OAIDAG::is_next_dagrun_data_interval_end_Set() const{
    return m_next_dagrun_data_interval_end_isSet;
}

bool OAIDAG::is_next_dagrun_data_interval_end_Valid() const{
    return m_next_dagrun_data_interval_end_isValid;
}

QDateTime OAIDAG::getNextDagrunDataIntervalStart() const {
    return m_next_dagrun_data_interval_start;
}
void OAIDAG::setNextDagrunDataIntervalStart(const QDateTime &next_dagrun_data_interval_start) {
    m_next_dagrun_data_interval_start = next_dagrun_data_interval_start;
    m_next_dagrun_data_interval_start_isSet = true;
}

bool OAIDAG::is_next_dagrun_data_interval_start_Set() const{
    return m_next_dagrun_data_interval_start_isSet;
}

bool OAIDAG::is_next_dagrun_data_interval_start_Valid() const{
    return m_next_dagrun_data_interval_start_isValid;
}

QList<QString> OAIDAG::getOwners() const {
    return m_owners;
}
void OAIDAG::setOwners(const QList<QString> &owners) {
    m_owners = owners;
    m_owners_isSet = true;
}

bool OAIDAG::is_owners_Set() const{
    return m_owners_isSet;
}

bool OAIDAG::is_owners_Valid() const{
    return m_owners_isValid;
}

QString OAIDAG::getPickleId() const {
    return m_pickle_id;
}
void OAIDAG::setPickleId(const QString &pickle_id) {
    m_pickle_id = pickle_id;
    m_pickle_id_isSet = true;
}

bool OAIDAG::is_pickle_id_Set() const{
    return m_pickle_id_isSet;
}

bool OAIDAG::is_pickle_id_Valid() const{
    return m_pickle_id_isValid;
}

QString OAIDAG::getRootDagId() const {
    return m_root_dag_id;
}
void OAIDAG::setRootDagId(const QString &root_dag_id) {
    m_root_dag_id = root_dag_id;
    m_root_dag_id_isSet = true;
}

bool OAIDAG::is_root_dag_id_Set() const{
    return m_root_dag_id_isSet;
}

bool OAIDAG::is_root_dag_id_Valid() const{
    return m_root_dag_id_isValid;
}

OAIScheduleInterval OAIDAG::getScheduleInterval() const {
    return m_schedule_interval;
}
void OAIDAG::setScheduleInterval(const OAIScheduleInterval &schedule_interval) {
    m_schedule_interval = schedule_interval;
    m_schedule_interval_isSet = true;
}

bool OAIDAG::is_schedule_interval_Set() const{
    return m_schedule_interval_isSet;
}

bool OAIDAG::is_schedule_interval_Valid() const{
    return m_schedule_interval_isValid;
}

bool OAIDAG::isSchedulerLock() const {
    return m_scheduler_lock;
}
void OAIDAG::setSchedulerLock(const bool &scheduler_lock) {
    m_scheduler_lock = scheduler_lock;
    m_scheduler_lock_isSet = true;
}

bool OAIDAG::is_scheduler_lock_Set() const{
    return m_scheduler_lock_isSet;
}

bool OAIDAG::is_scheduler_lock_Valid() const{
    return m_scheduler_lock_isValid;
}

QList<OAITag> OAIDAG::getTags() const {
    return m_tags;
}
void OAIDAG::setTags(const QList<OAITag> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIDAG::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIDAG::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIDAG::getTimetableDescription() const {
    return m_timetable_description;
}
void OAIDAG::setTimetableDescription(const QString &timetable_description) {
    m_timetable_description = timetable_description;
    m_timetable_description_isSet = true;
}

bool OAIDAG::is_timetable_description_Set() const{
    return m_timetable_description_isSet;
}

bool OAIDAG::is_timetable_description_Valid() const{
    return m_timetable_description_isValid;
}

bool OAIDAG::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dag_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_default_view_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fileloc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_import_errors_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_task_concurrency_limits_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_paused_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_subdag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_expired_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_parsed_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_pickled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_active_runs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_active_tasks_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_dagrun_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_dagrun_create_after_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_dagrun_data_interval_end_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_dagrun_data_interval_start_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owners.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_pickle_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_root_dag_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedule_interval.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_scheduler_lock_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_timetable_description_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDAG::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
