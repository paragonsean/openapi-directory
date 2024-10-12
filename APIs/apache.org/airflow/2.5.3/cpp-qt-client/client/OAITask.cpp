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

#include "OAITask.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITask::OAITask(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITask::OAITask() {
    this->initializeModel();
}

OAITask::~OAITask() {}

void OAITask::initializeModel() {

    m_class_ref_isSet = false;
    m_class_ref_isValid = false;

    m_depends_on_past_isSet = false;
    m_depends_on_past_isValid = false;

    m_downstream_task_ids_isSet = false;
    m_downstream_task_ids_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_execution_timeout_isSet = false;
    m_execution_timeout_isValid = false;

    m_extra_links_isSet = false;
    m_extra_links_isValid = false;

    m_is_mapped_isSet = false;
    m_is_mapped_isValid = false;

    m_owner_isSet = false;
    m_owner_isValid = false;

    m_pool_isSet = false;
    m_pool_isValid = false;

    m_pool_slots_isSet = false;
    m_pool_slots_isValid = false;

    m_priority_weight_isSet = false;
    m_priority_weight_isValid = false;

    m_queue_isSet = false;
    m_queue_isValid = false;

    m_retries_isSet = false;
    m_retries_isValid = false;

    m_retry_delay_isSet = false;
    m_retry_delay_isValid = false;

    m_retry_exponential_backoff_isSet = false;
    m_retry_exponential_backoff_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_sub_dag_isSet = false;
    m_sub_dag_isValid = false;

    m_task_id_isSet = false;
    m_task_id_isValid = false;

    m_template_fields_isSet = false;
    m_template_fields_isValid = false;

    m_trigger_rule_isSet = false;
    m_trigger_rule_isValid = false;

    m_ui_color_isSet = false;
    m_ui_color_isValid = false;

    m_ui_fgcolor_isSet = false;
    m_ui_fgcolor_isValid = false;

    m_wait_for_downstream_isSet = false;
    m_wait_for_downstream_isValid = false;

    m_weight_rule_isSet = false;
    m_weight_rule_isValid = false;
}

void OAITask::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITask::fromJsonObject(QJsonObject json) {

    m_class_ref_isValid = ::OpenAPI::fromJsonValue(m_class_ref, json[QString("class_ref")]);
    m_class_ref_isSet = !json[QString("class_ref")].isNull() && m_class_ref_isValid;

    m_depends_on_past_isValid = ::OpenAPI::fromJsonValue(m_depends_on_past, json[QString("depends_on_past")]);
    m_depends_on_past_isSet = !json[QString("depends_on_past")].isNull() && m_depends_on_past_isValid;

    m_downstream_task_ids_isValid = ::OpenAPI::fromJsonValue(m_downstream_task_ids, json[QString("downstream_task_ids")]);
    m_downstream_task_ids_isSet = !json[QString("downstream_task_ids")].isNull() && m_downstream_task_ids_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("end_date")]);
    m_end_date_isSet = !json[QString("end_date")].isNull() && m_end_date_isValid;

    m_execution_timeout_isValid = ::OpenAPI::fromJsonValue(m_execution_timeout, json[QString("execution_timeout")]);
    m_execution_timeout_isSet = !json[QString("execution_timeout")].isNull() && m_execution_timeout_isValid;

    m_extra_links_isValid = ::OpenAPI::fromJsonValue(m_extra_links, json[QString("extra_links")]);
    m_extra_links_isSet = !json[QString("extra_links")].isNull() && m_extra_links_isValid;

    m_is_mapped_isValid = ::OpenAPI::fromJsonValue(m_is_mapped, json[QString("is_mapped")]);
    m_is_mapped_isSet = !json[QString("is_mapped")].isNull() && m_is_mapped_isValid;

    m_owner_isValid = ::OpenAPI::fromJsonValue(m_owner, json[QString("owner")]);
    m_owner_isSet = !json[QString("owner")].isNull() && m_owner_isValid;

    m_pool_isValid = ::OpenAPI::fromJsonValue(m_pool, json[QString("pool")]);
    m_pool_isSet = !json[QString("pool")].isNull() && m_pool_isValid;

    m_pool_slots_isValid = ::OpenAPI::fromJsonValue(m_pool_slots, json[QString("pool_slots")]);
    m_pool_slots_isSet = !json[QString("pool_slots")].isNull() && m_pool_slots_isValid;

    m_priority_weight_isValid = ::OpenAPI::fromJsonValue(m_priority_weight, json[QString("priority_weight")]);
    m_priority_weight_isSet = !json[QString("priority_weight")].isNull() && m_priority_weight_isValid;

    m_queue_isValid = ::OpenAPI::fromJsonValue(m_queue, json[QString("queue")]);
    m_queue_isSet = !json[QString("queue")].isNull() && m_queue_isValid;

    m_retries_isValid = ::OpenAPI::fromJsonValue(m_retries, json[QString("retries")]);
    m_retries_isSet = !json[QString("retries")].isNull() && m_retries_isValid;

    m_retry_delay_isValid = ::OpenAPI::fromJsonValue(m_retry_delay, json[QString("retry_delay")]);
    m_retry_delay_isSet = !json[QString("retry_delay")].isNull() && m_retry_delay_isValid;

    m_retry_exponential_backoff_isValid = ::OpenAPI::fromJsonValue(m_retry_exponential_backoff, json[QString("retry_exponential_backoff")]);
    m_retry_exponential_backoff_isSet = !json[QString("retry_exponential_backoff")].isNull() && m_retry_exponential_backoff_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("start_date")]);
    m_start_date_isSet = !json[QString("start_date")].isNull() && m_start_date_isValid;

    m_sub_dag_isValid = ::OpenAPI::fromJsonValue(m_sub_dag, json[QString("sub_dag")]);
    m_sub_dag_isSet = !json[QString("sub_dag")].isNull() && m_sub_dag_isValid;

    m_task_id_isValid = ::OpenAPI::fromJsonValue(m_task_id, json[QString("task_id")]);
    m_task_id_isSet = !json[QString("task_id")].isNull() && m_task_id_isValid;

    m_template_fields_isValid = ::OpenAPI::fromJsonValue(m_template_fields, json[QString("template_fields")]);
    m_template_fields_isSet = !json[QString("template_fields")].isNull() && m_template_fields_isValid;

    m_trigger_rule_isValid = ::OpenAPI::fromJsonValue(m_trigger_rule, json[QString("trigger_rule")]);
    m_trigger_rule_isSet = !json[QString("trigger_rule")].isNull() && m_trigger_rule_isValid;

    m_ui_color_isValid = ::OpenAPI::fromJsonValue(m_ui_color, json[QString("ui_color")]);
    m_ui_color_isSet = !json[QString("ui_color")].isNull() && m_ui_color_isValid;

    m_ui_fgcolor_isValid = ::OpenAPI::fromJsonValue(m_ui_fgcolor, json[QString("ui_fgcolor")]);
    m_ui_fgcolor_isSet = !json[QString("ui_fgcolor")].isNull() && m_ui_fgcolor_isValid;

    m_wait_for_downstream_isValid = ::OpenAPI::fromJsonValue(m_wait_for_downstream, json[QString("wait_for_downstream")]);
    m_wait_for_downstream_isSet = !json[QString("wait_for_downstream")].isNull() && m_wait_for_downstream_isValid;

    m_weight_rule_isValid = ::OpenAPI::fromJsonValue(m_weight_rule, json[QString("weight_rule")]);
    m_weight_rule_isSet = !json[QString("weight_rule")].isNull() && m_weight_rule_isValid;
}

QString OAITask::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITask::asJsonObject() const {
    QJsonObject obj;
    if (m_class_ref.isSet()) {
        obj.insert(QString("class_ref"), ::OpenAPI::toJsonValue(m_class_ref));
    }
    if (m_depends_on_past_isSet) {
        obj.insert(QString("depends_on_past"), ::OpenAPI::toJsonValue(m_depends_on_past));
    }
    if (m_downstream_task_ids.size() > 0) {
        obj.insert(QString("downstream_task_ids"), ::OpenAPI::toJsonValue(m_downstream_task_ids));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("end_date"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_execution_timeout.isSet()) {
        obj.insert(QString("execution_timeout"), ::OpenAPI::toJsonValue(m_execution_timeout));
    }
    if (m_extra_links.size() > 0) {
        obj.insert(QString("extra_links"), ::OpenAPI::toJsonValue(m_extra_links));
    }
    if (m_is_mapped_isSet) {
        obj.insert(QString("is_mapped"), ::OpenAPI::toJsonValue(m_is_mapped));
    }
    if (m_owner_isSet) {
        obj.insert(QString("owner"), ::OpenAPI::toJsonValue(m_owner));
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
    if (m_retries_isSet) {
        obj.insert(QString("retries"), ::OpenAPI::toJsonValue(m_retries));
    }
    if (m_retry_delay.isSet()) {
        obj.insert(QString("retry_delay"), ::OpenAPI::toJsonValue(m_retry_delay));
    }
    if (m_retry_exponential_backoff_isSet) {
        obj.insert(QString("retry_exponential_backoff"), ::OpenAPI::toJsonValue(m_retry_exponential_backoff));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("start_date"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_sub_dag.isSet()) {
        obj.insert(QString("sub_dag"), ::OpenAPI::toJsonValue(m_sub_dag));
    }
    if (m_task_id_isSet) {
        obj.insert(QString("task_id"), ::OpenAPI::toJsonValue(m_task_id));
    }
    if (m_template_fields.size() > 0) {
        obj.insert(QString("template_fields"), ::OpenAPI::toJsonValue(m_template_fields));
    }
    if (m_trigger_rule.isSet()) {
        obj.insert(QString("trigger_rule"), ::OpenAPI::toJsonValue(m_trigger_rule));
    }
    if (m_ui_color_isSet) {
        obj.insert(QString("ui_color"), ::OpenAPI::toJsonValue(m_ui_color));
    }
    if (m_ui_fgcolor_isSet) {
        obj.insert(QString("ui_fgcolor"), ::OpenAPI::toJsonValue(m_ui_fgcolor));
    }
    if (m_wait_for_downstream_isSet) {
        obj.insert(QString("wait_for_downstream"), ::OpenAPI::toJsonValue(m_wait_for_downstream));
    }
    if (m_weight_rule.isSet()) {
        obj.insert(QString("weight_rule"), ::OpenAPI::toJsonValue(m_weight_rule));
    }
    return obj;
}

OAIClassReference OAITask::getClassRef() const {
    return m_class_ref;
}
void OAITask::setClassRef(const OAIClassReference &class_ref) {
    m_class_ref = class_ref;
    m_class_ref_isSet = true;
}

bool OAITask::is_class_ref_Set() const{
    return m_class_ref_isSet;
}

bool OAITask::is_class_ref_Valid() const{
    return m_class_ref_isValid;
}

bool OAITask::isDependsOnPast() const {
    return m_depends_on_past;
}
void OAITask::setDependsOnPast(const bool &depends_on_past) {
    m_depends_on_past = depends_on_past;
    m_depends_on_past_isSet = true;
}

bool OAITask::is_depends_on_past_Set() const{
    return m_depends_on_past_isSet;
}

bool OAITask::is_depends_on_past_Valid() const{
    return m_depends_on_past_isValid;
}

QList<QString> OAITask::getDownstreamTaskIds() const {
    return m_downstream_task_ids;
}
void OAITask::setDownstreamTaskIds(const QList<QString> &downstream_task_ids) {
    m_downstream_task_ids = downstream_task_ids;
    m_downstream_task_ids_isSet = true;
}

bool OAITask::is_downstream_task_ids_Set() const{
    return m_downstream_task_ids_isSet;
}

bool OAITask::is_downstream_task_ids_Valid() const{
    return m_downstream_task_ids_isValid;
}

QDateTime OAITask::getEndDate() const {
    return m_end_date;
}
void OAITask::setEndDate(const QDateTime &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAITask::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAITask::is_end_date_Valid() const{
    return m_end_date_isValid;
}

OAITimeDelta OAITask::getExecutionTimeout() const {
    return m_execution_timeout;
}
void OAITask::setExecutionTimeout(const OAITimeDelta &execution_timeout) {
    m_execution_timeout = execution_timeout;
    m_execution_timeout_isSet = true;
}

bool OAITask::is_execution_timeout_Set() const{
    return m_execution_timeout_isSet;
}

bool OAITask::is_execution_timeout_Valid() const{
    return m_execution_timeout_isValid;
}

QList<OAITask_extra_links_inner> OAITask::getExtraLinks() const {
    return m_extra_links;
}
void OAITask::setExtraLinks(const QList<OAITask_extra_links_inner> &extra_links) {
    m_extra_links = extra_links;
    m_extra_links_isSet = true;
}

bool OAITask::is_extra_links_Set() const{
    return m_extra_links_isSet;
}

bool OAITask::is_extra_links_Valid() const{
    return m_extra_links_isValid;
}

bool OAITask::isIsMapped() const {
    return m_is_mapped;
}
void OAITask::setIsMapped(const bool &is_mapped) {
    m_is_mapped = is_mapped;
    m_is_mapped_isSet = true;
}

bool OAITask::is_is_mapped_Set() const{
    return m_is_mapped_isSet;
}

bool OAITask::is_is_mapped_Valid() const{
    return m_is_mapped_isValid;
}

QString OAITask::getOwner() const {
    return m_owner;
}
void OAITask::setOwner(const QString &owner) {
    m_owner = owner;
    m_owner_isSet = true;
}

bool OAITask::is_owner_Set() const{
    return m_owner_isSet;
}

bool OAITask::is_owner_Valid() const{
    return m_owner_isValid;
}

QString OAITask::getPool() const {
    return m_pool;
}
void OAITask::setPool(const QString &pool) {
    m_pool = pool;
    m_pool_isSet = true;
}

bool OAITask::is_pool_Set() const{
    return m_pool_isSet;
}

bool OAITask::is_pool_Valid() const{
    return m_pool_isValid;
}

double OAITask::getPoolSlots() const {
    return m_pool_slots;
}
void OAITask::setPoolSlots(const double &pool_slots) {
    m_pool_slots = pool_slots;
    m_pool_slots_isSet = true;
}

bool OAITask::is_pool_slots_Set() const{
    return m_pool_slots_isSet;
}

bool OAITask::is_pool_slots_Valid() const{
    return m_pool_slots_isValid;
}

double OAITask::getPriorityWeight() const {
    return m_priority_weight;
}
void OAITask::setPriorityWeight(const double &priority_weight) {
    m_priority_weight = priority_weight;
    m_priority_weight_isSet = true;
}

bool OAITask::is_priority_weight_Set() const{
    return m_priority_weight_isSet;
}

bool OAITask::is_priority_weight_Valid() const{
    return m_priority_weight_isValid;
}

QString OAITask::getQueue() const {
    return m_queue;
}
void OAITask::setQueue(const QString &queue) {
    m_queue = queue;
    m_queue_isSet = true;
}

bool OAITask::is_queue_Set() const{
    return m_queue_isSet;
}

bool OAITask::is_queue_Valid() const{
    return m_queue_isValid;
}

double OAITask::getRetries() const {
    return m_retries;
}
void OAITask::setRetries(const double &retries) {
    m_retries = retries;
    m_retries_isSet = true;
}

bool OAITask::is_retries_Set() const{
    return m_retries_isSet;
}

bool OAITask::is_retries_Valid() const{
    return m_retries_isValid;
}

OAITimeDelta OAITask::getRetryDelay() const {
    return m_retry_delay;
}
void OAITask::setRetryDelay(const OAITimeDelta &retry_delay) {
    m_retry_delay = retry_delay;
    m_retry_delay_isSet = true;
}

bool OAITask::is_retry_delay_Set() const{
    return m_retry_delay_isSet;
}

bool OAITask::is_retry_delay_Valid() const{
    return m_retry_delay_isValid;
}

bool OAITask::isRetryExponentialBackoff() const {
    return m_retry_exponential_backoff;
}
void OAITask::setRetryExponentialBackoff(const bool &retry_exponential_backoff) {
    m_retry_exponential_backoff = retry_exponential_backoff;
    m_retry_exponential_backoff_isSet = true;
}

bool OAITask::is_retry_exponential_backoff_Set() const{
    return m_retry_exponential_backoff_isSet;
}

bool OAITask::is_retry_exponential_backoff_Valid() const{
    return m_retry_exponential_backoff_isValid;
}

QDateTime OAITask::getStartDate() const {
    return m_start_date;
}
void OAITask::setStartDate(const QDateTime &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAITask::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAITask::is_start_date_Valid() const{
    return m_start_date_isValid;
}

OAIDAG OAITask::getSubDag() const {
    return m_sub_dag;
}
void OAITask::setSubDag(const OAIDAG &sub_dag) {
    m_sub_dag = sub_dag;
    m_sub_dag_isSet = true;
}

bool OAITask::is_sub_dag_Set() const{
    return m_sub_dag_isSet;
}

bool OAITask::is_sub_dag_Valid() const{
    return m_sub_dag_isValid;
}

QString OAITask::getTaskId() const {
    return m_task_id;
}
void OAITask::setTaskId(const QString &task_id) {
    m_task_id = task_id;
    m_task_id_isSet = true;
}

bool OAITask::is_task_id_Set() const{
    return m_task_id_isSet;
}

bool OAITask::is_task_id_Valid() const{
    return m_task_id_isValid;
}

QList<QString> OAITask::getTemplateFields() const {
    return m_template_fields;
}
void OAITask::setTemplateFields(const QList<QString> &template_fields) {
    m_template_fields = template_fields;
    m_template_fields_isSet = true;
}

bool OAITask::is_template_fields_Set() const{
    return m_template_fields_isSet;
}

bool OAITask::is_template_fields_Valid() const{
    return m_template_fields_isValid;
}

OAITriggerRule OAITask::getTriggerRule() const {
    return m_trigger_rule;
}
void OAITask::setTriggerRule(const OAITriggerRule &trigger_rule) {
    m_trigger_rule = trigger_rule;
    m_trigger_rule_isSet = true;
}

bool OAITask::is_trigger_rule_Set() const{
    return m_trigger_rule_isSet;
}

bool OAITask::is_trigger_rule_Valid() const{
    return m_trigger_rule_isValid;
}

QString OAITask::getUiColor() const {
    return m_ui_color;
}
void OAITask::setUiColor(const QString &ui_color) {
    m_ui_color = ui_color;
    m_ui_color_isSet = true;
}

bool OAITask::is_ui_color_Set() const{
    return m_ui_color_isSet;
}

bool OAITask::is_ui_color_Valid() const{
    return m_ui_color_isValid;
}

QString OAITask::getUiFgcolor() const {
    return m_ui_fgcolor;
}
void OAITask::setUiFgcolor(const QString &ui_fgcolor) {
    m_ui_fgcolor = ui_fgcolor;
    m_ui_fgcolor_isSet = true;
}

bool OAITask::is_ui_fgcolor_Set() const{
    return m_ui_fgcolor_isSet;
}

bool OAITask::is_ui_fgcolor_Valid() const{
    return m_ui_fgcolor_isValid;
}

bool OAITask::isWaitForDownstream() const {
    return m_wait_for_downstream;
}
void OAITask::setWaitForDownstream(const bool &wait_for_downstream) {
    m_wait_for_downstream = wait_for_downstream;
    m_wait_for_downstream_isSet = true;
}

bool OAITask::is_wait_for_downstream_Set() const{
    return m_wait_for_downstream_isSet;
}

bool OAITask::is_wait_for_downstream_Valid() const{
    return m_wait_for_downstream_isValid;
}

OAIWeightRule OAITask::getWeightRule() const {
    return m_weight_rule;
}
void OAITask::setWeightRule(const OAIWeightRule &weight_rule) {
    m_weight_rule = weight_rule;
    m_weight_rule_isSet = true;
}

bool OAITask::is_weight_rule_Set() const{
    return m_weight_rule_isSet;
}

bool OAITask::is_weight_rule_Valid() const{
    return m_weight_rule_isValid;
}

bool OAITask::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_class_ref.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_depends_on_past_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_downstream_task_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_execution_timeout.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_extra_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_mapped_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_isSet) {
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

        if (m_retries_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_retry_delay.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_retry_exponential_backoff_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sub_dag.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_task_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_template_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_trigger_rule.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ui_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ui_fgcolor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wait_for_downstream_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weight_rule.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITask::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
