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

#include "OAIClear_dag_run_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIClear_dag_run_200_response::OAIClear_dag_run_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIClear_dag_run_200_response::OAIClear_dag_run_200_response() {
    this->initializeModel();
}

OAIClear_dag_run_200_response::~OAIClear_dag_run_200_response() {}

void OAIClear_dag_run_200_response::initializeModel() {

    m_conf_isSet = false;
    m_conf_isValid = false;

    m_dag_id_isSet = false;
    m_dag_id_isValid = false;

    m_dag_run_id_isSet = false;
    m_dag_run_id_isValid = false;

    m_data_interval_end_isSet = false;
    m_data_interval_end_isValid = false;

    m_data_interval_start_isSet = false;
    m_data_interval_start_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_execution_date_isSet = false;
    m_execution_date_isValid = false;

    m_external_trigger_isSet = false;
    m_external_trigger_isValid = false;

    m_last_scheduling_decision_isSet = false;
    m_last_scheduling_decision_isValid = false;

    m_logical_date_isSet = false;
    m_logical_date_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_run_type_isSet = false;
    m_run_type_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_task_instances_isSet = false;
    m_task_instances_isValid = false;

    m_total_entries_isSet = false;
    m_total_entries_isValid = false;
}

void OAIClear_dag_run_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIClear_dag_run_200_response::fromJsonObject(QJsonObject json) {

    m_conf_isValid = ::OpenAPI::fromJsonValue(m_conf, json[QString("conf")]);
    m_conf_isSet = !json[QString("conf")].isNull() && m_conf_isValid;

    m_dag_id_isValid = ::OpenAPI::fromJsonValue(m_dag_id, json[QString("dag_id")]);
    m_dag_id_isSet = !json[QString("dag_id")].isNull() && m_dag_id_isValid;

    m_dag_run_id_isValid = ::OpenAPI::fromJsonValue(m_dag_run_id, json[QString("dag_run_id")]);
    m_dag_run_id_isSet = !json[QString("dag_run_id")].isNull() && m_dag_run_id_isValid;

    m_data_interval_end_isValid = ::OpenAPI::fromJsonValue(m_data_interval_end, json[QString("data_interval_end")]);
    m_data_interval_end_isSet = !json[QString("data_interval_end")].isNull() && m_data_interval_end_isValid;

    m_data_interval_start_isValid = ::OpenAPI::fromJsonValue(m_data_interval_start, json[QString("data_interval_start")]);
    m_data_interval_start_isSet = !json[QString("data_interval_start")].isNull() && m_data_interval_start_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("end_date")]);
    m_end_date_isSet = !json[QString("end_date")].isNull() && m_end_date_isValid;

    m_execution_date_isValid = ::OpenAPI::fromJsonValue(m_execution_date, json[QString("execution_date")]);
    m_execution_date_isSet = !json[QString("execution_date")].isNull() && m_execution_date_isValid;

    m_external_trigger_isValid = ::OpenAPI::fromJsonValue(m_external_trigger, json[QString("external_trigger")]);
    m_external_trigger_isSet = !json[QString("external_trigger")].isNull() && m_external_trigger_isValid;

    m_last_scheduling_decision_isValid = ::OpenAPI::fromJsonValue(m_last_scheduling_decision, json[QString("last_scheduling_decision")]);
    m_last_scheduling_decision_isSet = !json[QString("last_scheduling_decision")].isNull() && m_last_scheduling_decision_isValid;

    m_logical_date_isValid = ::OpenAPI::fromJsonValue(m_logical_date, json[QString("logical_date")]);
    m_logical_date_isSet = !json[QString("logical_date")].isNull() && m_logical_date_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_run_type_isValid = ::OpenAPI::fromJsonValue(m_run_type, json[QString("run_type")]);
    m_run_type_isSet = !json[QString("run_type")].isNull() && m_run_type_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("start_date")]);
    m_start_date_isSet = !json[QString("start_date")].isNull() && m_start_date_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_task_instances_isValid = ::OpenAPI::fromJsonValue(m_task_instances, json[QString("task_instances")]);
    m_task_instances_isSet = !json[QString("task_instances")].isNull() && m_task_instances_isValid;

    m_total_entries_isValid = ::OpenAPI::fromJsonValue(m_total_entries, json[QString("total_entries")]);
    m_total_entries_isSet = !json[QString("total_entries")].isNull() && m_total_entries_isValid;
}

QString OAIClear_dag_run_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIClear_dag_run_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_conf_isSet) {
        obj.insert(QString("conf"), ::OpenAPI::toJsonValue(m_conf));
    }
    if (m_dag_id_isSet) {
        obj.insert(QString("dag_id"), ::OpenAPI::toJsonValue(m_dag_id));
    }
    if (m_dag_run_id_isSet) {
        obj.insert(QString("dag_run_id"), ::OpenAPI::toJsonValue(m_dag_run_id));
    }
    if (m_data_interval_end_isSet) {
        obj.insert(QString("data_interval_end"), ::OpenAPI::toJsonValue(m_data_interval_end));
    }
    if (m_data_interval_start_isSet) {
        obj.insert(QString("data_interval_start"), ::OpenAPI::toJsonValue(m_data_interval_start));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("end_date"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_execution_date_isSet) {
        obj.insert(QString("execution_date"), ::OpenAPI::toJsonValue(m_execution_date));
    }
    if (m_external_trigger_isSet) {
        obj.insert(QString("external_trigger"), ::OpenAPI::toJsonValue(m_external_trigger));
    }
    if (m_last_scheduling_decision_isSet) {
        obj.insert(QString("last_scheduling_decision"), ::OpenAPI::toJsonValue(m_last_scheduling_decision));
    }
    if (m_logical_date_isSet) {
        obj.insert(QString("logical_date"), ::OpenAPI::toJsonValue(m_logical_date));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_run_type_isSet) {
        obj.insert(QString("run_type"), ::OpenAPI::toJsonValue(m_run_type));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("start_date"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_state.isSet()) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_task_instances.size() > 0) {
        obj.insert(QString("task_instances"), ::OpenAPI::toJsonValue(m_task_instances));
    }
    if (m_total_entries_isSet) {
        obj.insert(QString("total_entries"), ::OpenAPI::toJsonValue(m_total_entries));
    }
    return obj;
}

OAIObject OAIClear_dag_run_200_response::getConf() const {
    return m_conf;
}
void OAIClear_dag_run_200_response::setConf(const OAIObject &conf) {
    m_conf = conf;
    m_conf_isSet = true;
}

bool OAIClear_dag_run_200_response::is_conf_Set() const{
    return m_conf_isSet;
}

bool OAIClear_dag_run_200_response::is_conf_Valid() const{
    return m_conf_isValid;
}

QString OAIClear_dag_run_200_response::getDagId() const {
    return m_dag_id;
}
void OAIClear_dag_run_200_response::setDagId(const QString &dag_id) {
    m_dag_id = dag_id;
    m_dag_id_isSet = true;
}

bool OAIClear_dag_run_200_response::is_dag_id_Set() const{
    return m_dag_id_isSet;
}

bool OAIClear_dag_run_200_response::is_dag_id_Valid() const{
    return m_dag_id_isValid;
}

QString OAIClear_dag_run_200_response::getDagRunId() const {
    return m_dag_run_id;
}
void OAIClear_dag_run_200_response::setDagRunId(const QString &dag_run_id) {
    m_dag_run_id = dag_run_id;
    m_dag_run_id_isSet = true;
}

bool OAIClear_dag_run_200_response::is_dag_run_id_Set() const{
    return m_dag_run_id_isSet;
}

bool OAIClear_dag_run_200_response::is_dag_run_id_Valid() const{
    return m_dag_run_id_isValid;
}

QDateTime OAIClear_dag_run_200_response::getDataIntervalEnd() const {
    return m_data_interval_end;
}
void OAIClear_dag_run_200_response::setDataIntervalEnd(const QDateTime &data_interval_end) {
    m_data_interval_end = data_interval_end;
    m_data_interval_end_isSet = true;
}

bool OAIClear_dag_run_200_response::is_data_interval_end_Set() const{
    return m_data_interval_end_isSet;
}

bool OAIClear_dag_run_200_response::is_data_interval_end_Valid() const{
    return m_data_interval_end_isValid;
}

QDateTime OAIClear_dag_run_200_response::getDataIntervalStart() const {
    return m_data_interval_start;
}
void OAIClear_dag_run_200_response::setDataIntervalStart(const QDateTime &data_interval_start) {
    m_data_interval_start = data_interval_start;
    m_data_interval_start_isSet = true;
}

bool OAIClear_dag_run_200_response::is_data_interval_start_Set() const{
    return m_data_interval_start_isSet;
}

bool OAIClear_dag_run_200_response::is_data_interval_start_Valid() const{
    return m_data_interval_start_isValid;
}

QDateTime OAIClear_dag_run_200_response::getEndDate() const {
    return m_end_date;
}
void OAIClear_dag_run_200_response::setEndDate(const QDateTime &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIClear_dag_run_200_response::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIClear_dag_run_200_response::is_end_date_Valid() const{
    return m_end_date_isValid;
}

QDateTime OAIClear_dag_run_200_response::getExecutionDate() const {
    return m_execution_date;
}
void OAIClear_dag_run_200_response::setExecutionDate(const QDateTime &execution_date) {
    m_execution_date = execution_date;
    m_execution_date_isSet = true;
}

bool OAIClear_dag_run_200_response::is_execution_date_Set() const{
    return m_execution_date_isSet;
}

bool OAIClear_dag_run_200_response::is_execution_date_Valid() const{
    return m_execution_date_isValid;
}

bool OAIClear_dag_run_200_response::isExternalTrigger() const {
    return m_external_trigger;
}
void OAIClear_dag_run_200_response::setExternalTrigger(const bool &external_trigger) {
    m_external_trigger = external_trigger;
    m_external_trigger_isSet = true;
}

bool OAIClear_dag_run_200_response::is_external_trigger_Set() const{
    return m_external_trigger_isSet;
}

bool OAIClear_dag_run_200_response::is_external_trigger_Valid() const{
    return m_external_trigger_isValid;
}

QDateTime OAIClear_dag_run_200_response::getLastSchedulingDecision() const {
    return m_last_scheduling_decision;
}
void OAIClear_dag_run_200_response::setLastSchedulingDecision(const QDateTime &last_scheduling_decision) {
    m_last_scheduling_decision = last_scheduling_decision;
    m_last_scheduling_decision_isSet = true;
}

bool OAIClear_dag_run_200_response::is_last_scheduling_decision_Set() const{
    return m_last_scheduling_decision_isSet;
}

bool OAIClear_dag_run_200_response::is_last_scheduling_decision_Valid() const{
    return m_last_scheduling_decision_isValid;
}

QDateTime OAIClear_dag_run_200_response::getLogicalDate() const {
    return m_logical_date;
}
void OAIClear_dag_run_200_response::setLogicalDate(const QDateTime &logical_date) {
    m_logical_date = logical_date;
    m_logical_date_isSet = true;
}

bool OAIClear_dag_run_200_response::is_logical_date_Set() const{
    return m_logical_date_isSet;
}

bool OAIClear_dag_run_200_response::is_logical_date_Valid() const{
    return m_logical_date_isValid;
}

QString OAIClear_dag_run_200_response::getNote() const {
    return m_note;
}
void OAIClear_dag_run_200_response::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAIClear_dag_run_200_response::is_note_Set() const{
    return m_note_isSet;
}

bool OAIClear_dag_run_200_response::is_note_Valid() const{
    return m_note_isValid;
}

QString OAIClear_dag_run_200_response::getRunType() const {
    return m_run_type;
}
void OAIClear_dag_run_200_response::setRunType(const QString &run_type) {
    m_run_type = run_type;
    m_run_type_isSet = true;
}

bool OAIClear_dag_run_200_response::is_run_type_Set() const{
    return m_run_type_isSet;
}

bool OAIClear_dag_run_200_response::is_run_type_Valid() const{
    return m_run_type_isValid;
}

QDateTime OAIClear_dag_run_200_response::getStartDate() const {
    return m_start_date;
}
void OAIClear_dag_run_200_response::setStartDate(const QDateTime &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIClear_dag_run_200_response::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIClear_dag_run_200_response::is_start_date_Valid() const{
    return m_start_date_isValid;
}

OAIDagState OAIClear_dag_run_200_response::getState() const {
    return m_state;
}
void OAIClear_dag_run_200_response::setState(const OAIDagState &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIClear_dag_run_200_response::is_state_Set() const{
    return m_state_isSet;
}

bool OAIClear_dag_run_200_response::is_state_Valid() const{
    return m_state_isValid;
}

QList<OAITaskInstance> OAIClear_dag_run_200_response::getTaskInstances() const {
    return m_task_instances;
}
void OAIClear_dag_run_200_response::setTaskInstances(const QList<OAITaskInstance> &task_instances) {
    m_task_instances = task_instances;
    m_task_instances_isSet = true;
}

bool OAIClear_dag_run_200_response::is_task_instances_Set() const{
    return m_task_instances_isSet;
}

bool OAIClear_dag_run_200_response::is_task_instances_Valid() const{
    return m_task_instances_isValid;
}

qint32 OAIClear_dag_run_200_response::getTotalEntries() const {
    return m_total_entries;
}
void OAIClear_dag_run_200_response::setTotalEntries(const qint32 &total_entries) {
    m_total_entries = total_entries;
    m_total_entries_isSet = true;
}

bool OAIClear_dag_run_200_response::is_total_entries_Set() const{
    return m_total_entries_isSet;
}

bool OAIClear_dag_run_200_response::is_total_entries_Valid() const{
    return m_total_entries_isValid;
}

bool OAIClear_dag_run_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_conf_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dag_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dag_run_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_interval_end_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_data_interval_start_isSet) {
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

        if (m_external_trigger_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_scheduling_decision_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_logical_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_run_type_isSet) {
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

        if (m_task_instances.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_entries_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIClear_dag_run_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
