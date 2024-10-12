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

#include "OAITaskInstance.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITaskInstance::OAITaskInstance(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITaskInstance::OAITaskInstance() {
    this->initializeModel();
}

OAITaskInstance::~OAITaskInstance() {}

void OAITaskInstance::initializeModel() {

    m_dag_id_isSet = false;
    m_dag_id_isValid = false;

    m_dag_run_id_isSet = false;
    m_dag_run_id_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_execution_date_isSet = false;
    m_execution_date_isValid = false;

    m_executor_config_isSet = false;
    m_executor_config_isValid = false;

    m_hostname_isSet = false;
    m_hostname_isValid = false;

    m_map_index_isSet = false;
    m_map_index_isValid = false;

    m_max_tries_isSet = false;
    m_max_tries_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_r_operator_isSet = false;
    m_r_operator_isValid = false;

    m_pid_isSet = false;
    m_pid_isValid = false;

    m_pool_isSet = false;
    m_pool_isValid = false;

    m_pool_slots_isSet = false;
    m_pool_slots_isValid = false;

    m_priority_weight_isSet = false;
    m_priority_weight_isValid = false;

    m_queue_isSet = false;
    m_queue_isValid = false;

    m_queued_when_isSet = false;
    m_queued_when_isValid = false;

    m_rendered_fields_isSet = false;
    m_rendered_fields_isValid = false;

    m_sla_miss_isSet = false;
    m_sla_miss_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_task_id_isSet = false;
    m_task_id_isValid = false;

    m_trigger_isSet = false;
    m_trigger_isValid = false;

    m_triggerer_job_isSet = false;
    m_triggerer_job_isValid = false;

    m_try_number_isSet = false;
    m_try_number_isValid = false;

    m_unixname_isSet = false;
    m_unixname_isValid = false;
}

void OAITaskInstance::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITaskInstance::fromJsonObject(QJsonObject json) {

    m_dag_id_isValid = ::OpenAPI::fromJsonValue(m_dag_id, json[QString("dag_id")]);
    m_dag_id_isSet = !json[QString("dag_id")].isNull() && m_dag_id_isValid;

    m_dag_run_id_isValid = ::OpenAPI::fromJsonValue(m_dag_run_id, json[QString("dag_run_id")]);
    m_dag_run_id_isSet = !json[QString("dag_run_id")].isNull() && m_dag_run_id_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("end_date")]);
    m_end_date_isSet = !json[QString("end_date")].isNull() && m_end_date_isValid;

    m_execution_date_isValid = ::OpenAPI::fromJsonValue(m_execution_date, json[QString("execution_date")]);
    m_execution_date_isSet = !json[QString("execution_date")].isNull() && m_execution_date_isValid;

    m_executor_config_isValid = ::OpenAPI::fromJsonValue(m_executor_config, json[QString("executor_config")]);
    m_executor_config_isSet = !json[QString("executor_config")].isNull() && m_executor_config_isValid;

    m_hostname_isValid = ::OpenAPI::fromJsonValue(m_hostname, json[QString("hostname")]);
    m_hostname_isSet = !json[QString("hostname")].isNull() && m_hostname_isValid;

    m_map_index_isValid = ::OpenAPI::fromJsonValue(m_map_index, json[QString("map_index")]);
    m_map_index_isSet = !json[QString("map_index")].isNull() && m_map_index_isValid;

    m_max_tries_isValid = ::OpenAPI::fromJsonValue(m_max_tries, json[QString("max_tries")]);
    m_max_tries_isSet = !json[QString("max_tries")].isNull() && m_max_tries_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_r_operator_isValid = ::OpenAPI::fromJsonValue(m_r_operator, json[QString("operator")]);
    m_r_operator_isSet = !json[QString("operator")].isNull() && m_r_operator_isValid;

    m_pid_isValid = ::OpenAPI::fromJsonValue(m_pid, json[QString("pid")]);
    m_pid_isSet = !json[QString("pid")].isNull() && m_pid_isValid;

    m_pool_isValid = ::OpenAPI::fromJsonValue(m_pool, json[QString("pool")]);
    m_pool_isSet = !json[QString("pool")].isNull() && m_pool_isValid;

    m_pool_slots_isValid = ::OpenAPI::fromJsonValue(m_pool_slots, json[QString("pool_slots")]);
    m_pool_slots_isSet = !json[QString("pool_slots")].isNull() && m_pool_slots_isValid;

    m_priority_weight_isValid = ::OpenAPI::fromJsonValue(m_priority_weight, json[QString("priority_weight")]);
    m_priority_weight_isSet = !json[QString("priority_weight")].isNull() && m_priority_weight_isValid;

    m_queue_isValid = ::OpenAPI::fromJsonValue(m_queue, json[QString("queue")]);
    m_queue_isSet = !json[QString("queue")].isNull() && m_queue_isValid;

    m_queued_when_isValid = ::OpenAPI::fromJsonValue(m_queued_when, json[QString("queued_when")]);
    m_queued_when_isSet = !json[QString("queued_when")].isNull() && m_queued_when_isValid;

    m_rendered_fields_isValid = ::OpenAPI::fromJsonValue(m_rendered_fields, json[QString("rendered_fields")]);
    m_rendered_fields_isSet = !json[QString("rendered_fields")].isNull() && m_rendered_fields_isValid;

    m_sla_miss_isValid = ::OpenAPI::fromJsonValue(m_sla_miss, json[QString("sla_miss")]);
    m_sla_miss_isSet = !json[QString("sla_miss")].isNull() && m_sla_miss_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("start_date")]);
    m_start_date_isSet = !json[QString("start_date")].isNull() && m_start_date_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_task_id_isValid = ::OpenAPI::fromJsonValue(m_task_id, json[QString("task_id")]);
    m_task_id_isSet = !json[QString("task_id")].isNull() && m_task_id_isValid;

    m_trigger_isValid = ::OpenAPI::fromJsonValue(m_trigger, json[QString("trigger")]);
    m_trigger_isSet = !json[QString("trigger")].isNull() && m_trigger_isValid;

    m_triggerer_job_isValid = ::OpenAPI::fromJsonValue(m_triggerer_job, json[QString("triggerer_job")]);
    m_triggerer_job_isSet = !json[QString("triggerer_job")].isNull() && m_triggerer_job_isValid;

    m_try_number_isValid = ::OpenAPI::fromJsonValue(m_try_number, json[QString("try_number")]);
    m_try_number_isSet = !json[QString("try_number")].isNull() && m_try_number_isValid;

    m_unixname_isValid = ::OpenAPI::fromJsonValue(m_unixname, json[QString("unixname")]);
    m_unixname_isSet = !json[QString("unixname")].isNull() && m_unixname_isValid;
}

QString OAITaskInstance::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITaskInstance::asJsonObject() const {
    QJsonObject obj;
    if (m_dag_id_isSet) {
        obj.insert(QString("dag_id"), ::OpenAPI::toJsonValue(m_dag_id));
    }
    if (m_dag_run_id_isSet) {
        obj.insert(QString("dag_run_id"), ::OpenAPI::toJsonValue(m_dag_run_id));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("end_date"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_execution_date_isSet) {
        obj.insert(QString("execution_date"), ::OpenAPI::toJsonValue(m_execution_date));
    }
    if (m_executor_config_isSet) {
        obj.insert(QString("executor_config"), ::OpenAPI::toJsonValue(m_executor_config));
    }
    if (m_hostname_isSet) {
        obj.insert(QString("hostname"), ::OpenAPI::toJsonValue(m_hostname));
    }
    if (m_map_index_isSet) {
        obj.insert(QString("map_index"), ::OpenAPI::toJsonValue(m_map_index));
    }
    if (m_max_tries_isSet) {
        obj.insert(QString("max_tries"), ::OpenAPI::toJsonValue(m_max_tries));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_r_operator_isSet) {
        obj.insert(QString("operator"), ::OpenAPI::toJsonValue(m_r_operator));
    }
    if (m_pid_isSet) {
        obj.insert(QString("pid"), ::OpenAPI::toJsonValue(m_pid));
    }
    if (m_pool_isSet) {
        obj.insert(QString("pool"), ::OpenAPI::toJsonValue(m_pool));
    }
    if (m_pool_slots_isSet) {
        obj.insert(QString("pool_slots"), ::OpenAPI::toJsonValue(m_pool_slots));
    }
    if (m_priority_weight_isSet) {
        obj.insert(QString("priority_weight"), ::OpenAPI::toJsonValue(m_priority_weight));
    }
    if (m_queue_isSet) {
        obj.insert(QString("queue"), ::OpenAPI::toJsonValue(m_queue));
    }
    if (m_queued_when_isSet) {
        obj.insert(QString("queued_when"), ::OpenAPI::toJsonValue(m_queued_when));
    }
    if (m_rendered_fields_isSet) {
        obj.insert(QString("rendered_fields"), ::OpenAPI::toJsonValue(m_rendered_fields));
    }
    if (m_sla_miss.isSet()) {
        obj.insert(QString("sla_miss"), ::OpenAPI::toJsonValue(m_sla_miss));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("start_date"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_state.isSet()) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_task_id_isSet) {
        obj.insert(QString("task_id"), ::OpenAPI::toJsonValue(m_task_id));
    }
    if (m_trigger.isSet()) {
        obj.insert(QString("trigger"), ::OpenAPI::toJsonValue(m_trigger));
    }
    if (m_triggerer_job.isSet()) {
        obj.insert(QString("triggerer_job"), ::OpenAPI::toJsonValue(m_triggerer_job));
    }
    if (m_try_number_isSet) {
        obj.insert(QString("try_number"), ::OpenAPI::toJsonValue(m_try_number));
    }
    if (m_unixname_isSet) {
        obj.insert(QString("unixname"), ::OpenAPI::toJsonValue(m_unixname));
    }
    return obj;
}

QString OAITaskInstance::getDagId() const {
    return m_dag_id;
}
void OAITaskInstance::setDagId(const QString &dag_id) {
    m_dag_id = dag_id;
    m_dag_id_isSet = true;
}

bool OAITaskInstance::is_dag_id_Set() const{
    return m_dag_id_isSet;
}

bool OAITaskInstance::is_dag_id_Valid() const{
    return m_dag_id_isValid;
}

QString OAITaskInstance::getDagRunId() const {
    return m_dag_run_id;
}
void OAITaskInstance::setDagRunId(const QString &dag_run_id) {
    m_dag_run_id = dag_run_id;
    m_dag_run_id_isSet = true;
}

bool OAITaskInstance::is_dag_run_id_Set() const{
    return m_dag_run_id_isSet;
}

bool OAITaskInstance::is_dag_run_id_Valid() const{
    return m_dag_run_id_isValid;
}

double OAITaskInstance::getDuration() const {
    return m_duration;
}
void OAITaskInstance::setDuration(const double &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAITaskInstance::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAITaskInstance::is_duration_Valid() const{
    return m_duration_isValid;
}

QString OAITaskInstance::getEndDate() const {
    return m_end_date;
}
void OAITaskInstance::setEndDate(const QString &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAITaskInstance::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAITaskInstance::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QString OAITaskInstance::getExecutionDate() const {
    return m_execution_date;
}
void OAITaskInstance::setExecutionDate(const QString &execution_date) {
    m_execution_date = execution_date;
    m_execution_date_isSet = true;
}

bool OAITaskInstance::is_execution_date_Set() const{
    return m_execution_date_isSet;
}

bool OAITaskInstance::is_execution_date_Valid() const{
    return m_execution_date_isValid;
}

QString OAITaskInstance::getExecutorConfig() const {
    return m_executor_config;
}
void OAITaskInstance::setExecutorConfig(const QString &executor_config) {
    m_executor_config = executor_config;
    m_executor_config_isSet = true;
}

bool OAITaskInstance::is_executor_config_Set() const{
    return m_executor_config_isSet;
}

bool OAITaskInstance::is_executor_config_Valid() const{
    return m_executor_config_isValid;
}

QString OAITaskInstance::getHostname() const {
    return m_hostname;
}
void OAITaskInstance::setHostname(const QString &hostname) {
    m_hostname = hostname;
    m_hostname_isSet = true;
}

bool OAITaskInstance::is_hostname_Set() const{
    return m_hostname_isSet;
}

bool OAITaskInstance::is_hostname_Valid() const{
    return m_hostname_isValid;
}

qint32 OAITaskInstance::getMapIndex() const {
    return m_map_index;
}
void OAITaskInstance::setMapIndex(const qint32 &map_index) {
    m_map_index = map_index;
    m_map_index_isSet = true;
}

bool OAITaskInstance::is_map_index_Set() const{
    return m_map_index_isSet;
}

bool OAITaskInstance::is_map_index_Valid() const{
    return m_map_index_isValid;
}

qint32 OAITaskInstance::getMaxTries() const {
    return m_max_tries;
}
void OAITaskInstance::setMaxTries(const qint32 &max_tries) {
    m_max_tries = max_tries;
    m_max_tries_isSet = true;
}

bool OAITaskInstance::is_max_tries_Set() const{
    return m_max_tries_isSet;
}

bool OAITaskInstance::is_max_tries_Valid() const{
    return m_max_tries_isValid;
}

QString OAITaskInstance::getNote() const {
    return m_note;
}
void OAITaskInstance::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAITaskInstance::is_note_Set() const{
    return m_note_isSet;
}

bool OAITaskInstance::is_note_Valid() const{
    return m_note_isValid;
}

QString OAITaskInstance::getROperator() const {
    return m_r_operator;
}
void OAITaskInstance::setROperator(const QString &r_operator) {
    m_r_operator = r_operator;
    m_r_operator_isSet = true;
}

bool OAITaskInstance::is_r_operator_Set() const{
    return m_r_operator_isSet;
}

bool OAITaskInstance::is_r_operator_Valid() const{
    return m_r_operator_isValid;
}

qint32 OAITaskInstance::getPid() const {
    return m_pid;
}
void OAITaskInstance::setPid(const qint32 &pid) {
    m_pid = pid;
    m_pid_isSet = true;
}

bool OAITaskInstance::is_pid_Set() const{
    return m_pid_isSet;
}

bool OAITaskInstance::is_pid_Valid() const{
    return m_pid_isValid;
}

QString OAITaskInstance::getPool() const {
    return m_pool;
}
void OAITaskInstance::setPool(const QString &pool) {
    m_pool = pool;
    m_pool_isSet = true;
}

bool OAITaskInstance::is_pool_Set() const{
    return m_pool_isSet;
}

bool OAITaskInstance::is_pool_Valid() const{
    return m_pool_isValid;
}

qint32 OAITaskInstance::getPoolSlots() const {
    return m_pool_slots;
}
void OAITaskInstance::setPoolSlots(const qint32 &pool_slots) {
    m_pool_slots = pool_slots;
    m_pool_slots_isSet = true;
}

bool OAITaskInstance::is_pool_slots_Set() const{
    return m_pool_slots_isSet;
}

bool OAITaskInstance::is_pool_slots_Valid() const{
    return m_pool_slots_isValid;
}

qint32 OAITaskInstance::getPriorityWeight() const {
    return m_priority_weight;
}
void OAITaskInstance::setPriorityWeight(const qint32 &priority_weight) {
    m_priority_weight = priority_weight;
    m_priority_weight_isSet = true;
}

bool OAITaskInstance::is_priority_weight_Set() const{
    return m_priority_weight_isSet;
}

bool OAITaskInstance::is_priority_weight_Valid() const{
    return m_priority_weight_isValid;
}

QString OAITaskInstance::getQueue() const {
    return m_queue;
}
void OAITaskInstance::setQueue(const QString &queue) {
    m_queue = queue;
    m_queue_isSet = true;
}

bool OAITaskInstance::is_queue_Set() const{
    return m_queue_isSet;
}

bool OAITaskInstance::is_queue_Valid() const{
    return m_queue_isValid;
}

QString OAITaskInstance::getQueuedWhen() const {
    return m_queued_when;
}
void OAITaskInstance::setQueuedWhen(const QString &queued_when) {
    m_queued_when = queued_when;
    m_queued_when_isSet = true;
}

bool OAITaskInstance::is_queued_when_Set() const{
    return m_queued_when_isSet;
}

bool OAITaskInstance::is_queued_when_Valid() const{
    return m_queued_when_isValid;
}

OAIObject OAITaskInstance::getRenderedFields() const {
    return m_rendered_fields;
}
void OAITaskInstance::setRenderedFields(const OAIObject &rendered_fields) {
    m_rendered_fields = rendered_fields;
    m_rendered_fields_isSet = true;
}

bool OAITaskInstance::is_rendered_fields_Set() const{
    return m_rendered_fields_isSet;
}

bool OAITaskInstance::is_rendered_fields_Valid() const{
    return m_rendered_fields_isValid;
}

OAISLAMiss OAITaskInstance::getSlaMiss() const {
    return m_sla_miss;
}
void OAITaskInstance::setSlaMiss(const OAISLAMiss &sla_miss) {
    m_sla_miss = sla_miss;
    m_sla_miss_isSet = true;
}

bool OAITaskInstance::is_sla_miss_Set() const{
    return m_sla_miss_isSet;
}

bool OAITaskInstance::is_sla_miss_Valid() const{
    return m_sla_miss_isValid;
}

QString OAITaskInstance::getStartDate() const {
    return m_start_date;
}
void OAITaskInstance::setStartDate(const QString &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAITaskInstance::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAITaskInstance::is_start_date_Valid() const{
    return m_start_date_isValid;
}

OAITaskState OAITaskInstance::getState() const {
    return m_state;
}
void OAITaskInstance::setState(const OAITaskState &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAITaskInstance::is_state_Set() const{
    return m_state_isSet;
}

bool OAITaskInstance::is_state_Valid() const{
    return m_state_isValid;
}

QString OAITaskInstance::getTaskId() const {
    return m_task_id;
}
void OAITaskInstance::setTaskId(const QString &task_id) {
    m_task_id = task_id;
    m_task_id_isSet = true;
}

bool OAITaskInstance::is_task_id_Set() const{
    return m_task_id_isSet;
}

bool OAITaskInstance::is_task_id_Valid() const{
    return m_task_id_isValid;
}

OAITrigger OAITaskInstance::getTrigger() const {
    return m_trigger;
}
void OAITaskInstance::setTrigger(const OAITrigger &trigger) {
    m_trigger = trigger;
    m_trigger_isSet = true;
}

bool OAITaskInstance::is_trigger_Set() const{
    return m_trigger_isSet;
}

bool OAITaskInstance::is_trigger_Valid() const{
    return m_trigger_isValid;
}

OAIJob OAITaskInstance::getTriggererJob() const {
    return m_triggerer_job;
}
void OAITaskInstance::setTriggererJob(const OAIJob &triggerer_job) {
    m_triggerer_job = triggerer_job;
    m_triggerer_job_isSet = true;
}

bool OAITaskInstance::is_triggerer_job_Set() const{
    return m_triggerer_job_isSet;
}

bool OAITaskInstance::is_triggerer_job_Valid() const{
    return m_triggerer_job_isValid;
}

qint32 OAITaskInstance::getTryNumber() const {
    return m_try_number;
}
void OAITaskInstance::setTryNumber(const qint32 &try_number) {
    m_try_number = try_number;
    m_try_number_isSet = true;
}

bool OAITaskInstance::is_try_number_Set() const{
    return m_try_number_isSet;
}

bool OAITaskInstance::is_try_number_Valid() const{
    return m_try_number_isValid;
}

QString OAITaskInstance::getUnixname() const {
    return m_unixname;
}
void OAITaskInstance::setUnixname(const QString &unixname) {
    m_unixname = unixname;
    m_unixname_isSet = true;
}

bool OAITaskInstance::is_unixname_Set() const{
    return m_unixname_isSet;
}

bool OAITaskInstance::is_unixname_Valid() const{
    return m_unixname_isValid;
}

bool OAITaskInstance::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dag_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dag_run_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_execution_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_executor_config_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hostname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_map_index_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_tries_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_operator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pool_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pool_slots_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_priority_weight_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_queue_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_queued_when_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rendered_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sla_miss.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_task_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trigger.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_triggerer_job.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_try_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unixname_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITaskInstance::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
