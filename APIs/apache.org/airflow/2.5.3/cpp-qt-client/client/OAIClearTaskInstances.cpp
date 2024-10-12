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

#include "OAIClearTaskInstances.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIClearTaskInstances::OAIClearTaskInstances(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIClearTaskInstances::OAIClearTaskInstances() {
    this->initializeModel();
}

OAIClearTaskInstances::~OAIClearTaskInstances() {}

void OAIClearTaskInstances::initializeModel() {

    m_dag_run_id_isSet = false;
    m_dag_run_id_isValid = false;

    m_dry_run_isSet = false;
    m_dry_run_isValid = false;

    m_end_date_isSet = false;
    m_end_date_isValid = false;

    m_include_downstream_isSet = false;
    m_include_downstream_isValid = false;

    m_include_future_isSet = false;
    m_include_future_isValid = false;

    m_include_parentdag_isSet = false;
    m_include_parentdag_isValid = false;

    m_include_past_isSet = false;
    m_include_past_isValid = false;

    m_include_subdags_isSet = false;
    m_include_subdags_isValid = false;

    m_include_upstream_isSet = false;
    m_include_upstream_isValid = false;

    m_only_failed_isSet = false;
    m_only_failed_isValid = false;

    m_only_running_isSet = false;
    m_only_running_isValid = false;

    m_reset_dag_runs_isSet = false;
    m_reset_dag_runs_isValid = false;

    m_start_date_isSet = false;
    m_start_date_isValid = false;

    m_task_ids_isSet = false;
    m_task_ids_isValid = false;
}

void OAIClearTaskInstances::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIClearTaskInstances::fromJsonObject(QJsonObject json) {

    m_dag_run_id_isValid = ::OpenAPI::fromJsonValue(m_dag_run_id, json[QString("dag_run_id")]);
    m_dag_run_id_isSet = !json[QString("dag_run_id")].isNull() && m_dag_run_id_isValid;

    m_dry_run_isValid = ::OpenAPI::fromJsonValue(m_dry_run, json[QString("dry_run")]);
    m_dry_run_isSet = !json[QString("dry_run")].isNull() && m_dry_run_isValid;

    m_end_date_isValid = ::OpenAPI::fromJsonValue(m_end_date, json[QString("end_date")]);
    m_end_date_isSet = !json[QString("end_date")].isNull() && m_end_date_isValid;

    m_include_downstream_isValid = ::OpenAPI::fromJsonValue(m_include_downstream, json[QString("include_downstream")]);
    m_include_downstream_isSet = !json[QString("include_downstream")].isNull() && m_include_downstream_isValid;

    m_include_future_isValid = ::OpenAPI::fromJsonValue(m_include_future, json[QString("include_future")]);
    m_include_future_isSet = !json[QString("include_future")].isNull() && m_include_future_isValid;

    m_include_parentdag_isValid = ::OpenAPI::fromJsonValue(m_include_parentdag, json[QString("include_parentdag")]);
    m_include_parentdag_isSet = !json[QString("include_parentdag")].isNull() && m_include_parentdag_isValid;

    m_include_past_isValid = ::OpenAPI::fromJsonValue(m_include_past, json[QString("include_past")]);
    m_include_past_isSet = !json[QString("include_past")].isNull() && m_include_past_isValid;

    m_include_subdags_isValid = ::OpenAPI::fromJsonValue(m_include_subdags, json[QString("include_subdags")]);
    m_include_subdags_isSet = !json[QString("include_subdags")].isNull() && m_include_subdags_isValid;

    m_include_upstream_isValid = ::OpenAPI::fromJsonValue(m_include_upstream, json[QString("include_upstream")]);
    m_include_upstream_isSet = !json[QString("include_upstream")].isNull() && m_include_upstream_isValid;

    m_only_failed_isValid = ::OpenAPI::fromJsonValue(m_only_failed, json[QString("only_failed")]);
    m_only_failed_isSet = !json[QString("only_failed")].isNull() && m_only_failed_isValid;

    m_only_running_isValid = ::OpenAPI::fromJsonValue(m_only_running, json[QString("only_running")]);
    m_only_running_isSet = !json[QString("only_running")].isNull() && m_only_running_isValid;

    m_reset_dag_runs_isValid = ::OpenAPI::fromJsonValue(m_reset_dag_runs, json[QString("reset_dag_runs")]);
    m_reset_dag_runs_isSet = !json[QString("reset_dag_runs")].isNull() && m_reset_dag_runs_isValid;

    m_start_date_isValid = ::OpenAPI::fromJsonValue(m_start_date, json[QString("start_date")]);
    m_start_date_isSet = !json[QString("start_date")].isNull() && m_start_date_isValid;

    m_task_ids_isValid = ::OpenAPI::fromJsonValue(m_task_ids, json[QString("task_ids")]);
    m_task_ids_isSet = !json[QString("task_ids")].isNull() && m_task_ids_isValid;
}

QString OAIClearTaskInstances::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIClearTaskInstances::asJsonObject() const {
    QJsonObject obj;
    if (m_dag_run_id_isSet) {
        obj.insert(QString("dag_run_id"), ::OpenAPI::toJsonValue(m_dag_run_id));
    }
    if (m_dry_run_isSet) {
        obj.insert(QString("dry_run"), ::OpenAPI::toJsonValue(m_dry_run));
    }
    if (m_end_date_isSet) {
        obj.insert(QString("end_date"), ::OpenAPI::toJsonValue(m_end_date));
    }
    if (m_include_downstream_isSet) {
        obj.insert(QString("include_downstream"), ::OpenAPI::toJsonValue(m_include_downstream));
    }
    if (m_include_future_isSet) {
        obj.insert(QString("include_future"), ::OpenAPI::toJsonValue(m_include_future));
    }
    if (m_include_parentdag_isSet) {
        obj.insert(QString("include_parentdag"), ::OpenAPI::toJsonValue(m_include_parentdag));
    }
    if (m_include_past_isSet) {
        obj.insert(QString("include_past"), ::OpenAPI::toJsonValue(m_include_past));
    }
    if (m_include_subdags_isSet) {
        obj.insert(QString("include_subdags"), ::OpenAPI::toJsonValue(m_include_subdags));
    }
    if (m_include_upstream_isSet) {
        obj.insert(QString("include_upstream"), ::OpenAPI::toJsonValue(m_include_upstream));
    }
    if (m_only_failed_isSet) {
        obj.insert(QString("only_failed"), ::OpenAPI::toJsonValue(m_only_failed));
    }
    if (m_only_running_isSet) {
        obj.insert(QString("only_running"), ::OpenAPI::toJsonValue(m_only_running));
    }
    if (m_reset_dag_runs_isSet) {
        obj.insert(QString("reset_dag_runs"), ::OpenAPI::toJsonValue(m_reset_dag_runs));
    }
    if (m_start_date_isSet) {
        obj.insert(QString("start_date"), ::OpenAPI::toJsonValue(m_start_date));
    }
    if (m_task_ids.size() > 0) {
        obj.insert(QString("task_ids"), ::OpenAPI::toJsonValue(m_task_ids));
    }
    return obj;
}

QString OAIClearTaskInstances::getDagRunId() const {
    return m_dag_run_id;
}
void OAIClearTaskInstances::setDagRunId(const QString &dag_run_id) {
    m_dag_run_id = dag_run_id;
    m_dag_run_id_isSet = true;
}

bool OAIClearTaskInstances::is_dag_run_id_Set() const{
    return m_dag_run_id_isSet;
}

bool OAIClearTaskInstances::is_dag_run_id_Valid() const{
    return m_dag_run_id_isValid;
}

bool OAIClearTaskInstances::isDryRun() const {
    return m_dry_run;
}
void OAIClearTaskInstances::setDryRun(const bool &dry_run) {
    m_dry_run = dry_run;
    m_dry_run_isSet = true;
}

bool OAIClearTaskInstances::is_dry_run_Set() const{
    return m_dry_run_isSet;
}

bool OAIClearTaskInstances::is_dry_run_Valid() const{
    return m_dry_run_isValid;
}

QString OAIClearTaskInstances::getEndDate() const {
    return m_end_date;
}
void OAIClearTaskInstances::setEndDate(const QString &end_date) {
    m_end_date = end_date;
    m_end_date_isSet = true;
}

bool OAIClearTaskInstances::is_end_date_Set() const{
    return m_end_date_isSet;
}

bool OAIClearTaskInstances::is_end_date_Valid() const{
    return m_end_date_isValid;
}

bool OAIClearTaskInstances::isIncludeDownstream() const {
    return m_include_downstream;
}
void OAIClearTaskInstances::setIncludeDownstream(const bool &include_downstream) {
    m_include_downstream = include_downstream;
    m_include_downstream_isSet = true;
}

bool OAIClearTaskInstances::is_include_downstream_Set() const{
    return m_include_downstream_isSet;
}

bool OAIClearTaskInstances::is_include_downstream_Valid() const{
    return m_include_downstream_isValid;
}

bool OAIClearTaskInstances::isIncludeFuture() const {
    return m_include_future;
}
void OAIClearTaskInstances::setIncludeFuture(const bool &include_future) {
    m_include_future = include_future;
    m_include_future_isSet = true;
}

bool OAIClearTaskInstances::is_include_future_Set() const{
    return m_include_future_isSet;
}

bool OAIClearTaskInstances::is_include_future_Valid() const{
    return m_include_future_isValid;
}

bool OAIClearTaskInstances::isIncludeParentdag() const {
    return m_include_parentdag;
}
void OAIClearTaskInstances::setIncludeParentdag(const bool &include_parentdag) {
    m_include_parentdag = include_parentdag;
    m_include_parentdag_isSet = true;
}

bool OAIClearTaskInstances::is_include_parentdag_Set() const{
    return m_include_parentdag_isSet;
}

bool OAIClearTaskInstances::is_include_parentdag_Valid() const{
    return m_include_parentdag_isValid;
}

bool OAIClearTaskInstances::isIncludePast() const {
    return m_include_past;
}
void OAIClearTaskInstances::setIncludePast(const bool &include_past) {
    m_include_past = include_past;
    m_include_past_isSet = true;
}

bool OAIClearTaskInstances::is_include_past_Set() const{
    return m_include_past_isSet;
}

bool OAIClearTaskInstances::is_include_past_Valid() const{
    return m_include_past_isValid;
}

bool OAIClearTaskInstances::isIncludeSubdags() const {
    return m_include_subdags;
}
void OAIClearTaskInstances::setIncludeSubdags(const bool &include_subdags) {
    m_include_subdags = include_subdags;
    m_include_subdags_isSet = true;
}

bool OAIClearTaskInstances::is_include_subdags_Set() const{
    return m_include_subdags_isSet;
}

bool OAIClearTaskInstances::is_include_subdags_Valid() const{
    return m_include_subdags_isValid;
}

bool OAIClearTaskInstances::isIncludeUpstream() const {
    return m_include_upstream;
}
void OAIClearTaskInstances::setIncludeUpstream(const bool &include_upstream) {
    m_include_upstream = include_upstream;
    m_include_upstream_isSet = true;
}

bool OAIClearTaskInstances::is_include_upstream_Set() const{
    return m_include_upstream_isSet;
}

bool OAIClearTaskInstances::is_include_upstream_Valid() const{
    return m_include_upstream_isValid;
}

bool OAIClearTaskInstances::isOnlyFailed() const {
    return m_only_failed;
}
void OAIClearTaskInstances::setOnlyFailed(const bool &only_failed) {
    m_only_failed = only_failed;
    m_only_failed_isSet = true;
}

bool OAIClearTaskInstances::is_only_failed_Set() const{
    return m_only_failed_isSet;
}

bool OAIClearTaskInstances::is_only_failed_Valid() const{
    return m_only_failed_isValid;
}

bool OAIClearTaskInstances::isOnlyRunning() const {
    return m_only_running;
}
void OAIClearTaskInstances::setOnlyRunning(const bool &only_running) {
    m_only_running = only_running;
    m_only_running_isSet = true;
}

bool OAIClearTaskInstances::is_only_running_Set() const{
    return m_only_running_isSet;
}

bool OAIClearTaskInstances::is_only_running_Valid() const{
    return m_only_running_isValid;
}

bool OAIClearTaskInstances::isResetDagRuns() const {
    return m_reset_dag_runs;
}
void OAIClearTaskInstances::setResetDagRuns(const bool &reset_dag_runs) {
    m_reset_dag_runs = reset_dag_runs;
    m_reset_dag_runs_isSet = true;
}

bool OAIClearTaskInstances::is_reset_dag_runs_Set() const{
    return m_reset_dag_runs_isSet;
}

bool OAIClearTaskInstances::is_reset_dag_runs_Valid() const{
    return m_reset_dag_runs_isValid;
}

QString OAIClearTaskInstances::getStartDate() const {
    return m_start_date;
}
void OAIClearTaskInstances::setStartDate(const QString &start_date) {
    m_start_date = start_date;
    m_start_date_isSet = true;
}

bool OAIClearTaskInstances::is_start_date_Set() const{
    return m_start_date_isSet;
}

bool OAIClearTaskInstances::is_start_date_Valid() const{
    return m_start_date_isValid;
}

QList<QString> OAIClearTaskInstances::getTaskIds() const {
    return m_task_ids;
}
void OAIClearTaskInstances::setTaskIds(const QList<QString> &task_ids) {
    m_task_ids = task_ids;
    m_task_ids_isSet = true;
}

bool OAIClearTaskInstances::is_task_ids_Set() const{
    return m_task_ids_isSet;
}

bool OAIClearTaskInstances::is_task_ids_Valid() const{
    return m_task_ids_isValid;
}

bool OAIClearTaskInstances::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dag_run_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dry_run_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_include_downstream_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_include_future_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_include_parentdag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_include_past_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_include_subdags_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_include_upstream_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_only_failed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_only_running_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reset_dag_runs_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_task_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIClearTaskInstances::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
