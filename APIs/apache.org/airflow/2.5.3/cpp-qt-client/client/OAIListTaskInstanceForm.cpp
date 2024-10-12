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

#include "OAIListTaskInstanceForm.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListTaskInstanceForm::OAIListTaskInstanceForm(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListTaskInstanceForm::OAIListTaskInstanceForm() {
    this->initializeModel();
}

OAIListTaskInstanceForm::~OAIListTaskInstanceForm() {}

void OAIListTaskInstanceForm::initializeModel() {

    m_dag_ids_isSet = false;
    m_dag_ids_isValid = false;

    m_duration_gte_isSet = false;
    m_duration_gte_isValid = false;

    m_duration_lte_isSet = false;
    m_duration_lte_isValid = false;

    m_end_date_gte_isSet = false;
    m_end_date_gte_isValid = false;

    m_end_date_lte_isSet = false;
    m_end_date_lte_isValid = false;

    m_execution_date_gte_isSet = false;
    m_execution_date_gte_isValid = false;

    m_execution_date_lte_isSet = false;
    m_execution_date_lte_isValid = false;

    m_pool_isSet = false;
    m_pool_isValid = false;

    m_queue_isSet = false;
    m_queue_isValid = false;

    m_start_date_gte_isSet = false;
    m_start_date_gte_isValid = false;

    m_start_date_lte_isSet = false;
    m_start_date_lte_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;
}

void OAIListTaskInstanceForm::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListTaskInstanceForm::fromJsonObject(QJsonObject json) {

    m_dag_ids_isValid = ::OpenAPI::fromJsonValue(m_dag_ids, json[QString("dag_ids")]);
    m_dag_ids_isSet = !json[QString("dag_ids")].isNull() && m_dag_ids_isValid;

    m_duration_gte_isValid = ::OpenAPI::fromJsonValue(m_duration_gte, json[QString("duration_gte")]);
    m_duration_gte_isSet = !json[QString("duration_gte")].isNull() && m_duration_gte_isValid;

    m_duration_lte_isValid = ::OpenAPI::fromJsonValue(m_duration_lte, json[QString("duration_lte")]);
    m_duration_lte_isSet = !json[QString("duration_lte")].isNull() && m_duration_lte_isValid;

    m_end_date_gte_isValid = ::OpenAPI::fromJsonValue(m_end_date_gte, json[QString("end_date_gte")]);
    m_end_date_gte_isSet = !json[QString("end_date_gte")].isNull() && m_end_date_gte_isValid;

    m_end_date_lte_isValid = ::OpenAPI::fromJsonValue(m_end_date_lte, json[QString("end_date_lte")]);
    m_end_date_lte_isSet = !json[QString("end_date_lte")].isNull() && m_end_date_lte_isValid;

    m_execution_date_gte_isValid = ::OpenAPI::fromJsonValue(m_execution_date_gte, json[QString("execution_date_gte")]);
    m_execution_date_gte_isSet = !json[QString("execution_date_gte")].isNull() && m_execution_date_gte_isValid;

    m_execution_date_lte_isValid = ::OpenAPI::fromJsonValue(m_execution_date_lte, json[QString("execution_date_lte")]);
    m_execution_date_lte_isSet = !json[QString("execution_date_lte")].isNull() && m_execution_date_lte_isValid;

    m_pool_isValid = ::OpenAPI::fromJsonValue(m_pool, json[QString("pool")]);
    m_pool_isSet = !json[QString("pool")].isNull() && m_pool_isValid;

    m_queue_isValid = ::OpenAPI::fromJsonValue(m_queue, json[QString("queue")]);
    m_queue_isSet = !json[QString("queue")].isNull() && m_queue_isValid;

    m_start_date_gte_isValid = ::OpenAPI::fromJsonValue(m_start_date_gte, json[QString("start_date_gte")]);
    m_start_date_gte_isSet = !json[QString("start_date_gte")].isNull() && m_start_date_gte_isValid;

    m_start_date_lte_isValid = ::OpenAPI::fromJsonValue(m_start_date_lte, json[QString("start_date_lte")]);
    m_start_date_lte_isSet = !json[QString("start_date_lte")].isNull() && m_start_date_lte_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;
}

QString OAIListTaskInstanceForm::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListTaskInstanceForm::asJsonObject() const {
    QJsonObject obj;
    if (m_dag_ids.size() > 0) {
        obj.insert(QString("dag_ids"), ::OpenAPI::toJsonValue(m_dag_ids));
    }
    if (m_duration_gte_isSet) {
        obj.insert(QString("duration_gte"), ::OpenAPI::toJsonValue(m_duration_gte));
    }
    if (m_duration_lte_isSet) {
        obj.insert(QString("duration_lte"), ::OpenAPI::toJsonValue(m_duration_lte));
    }
    if (m_end_date_gte_isSet) {
        obj.insert(QString("end_date_gte"), ::OpenAPI::toJsonValue(m_end_date_gte));
    }
    if (m_end_date_lte_isSet) {
        obj.insert(QString("end_date_lte"), ::OpenAPI::toJsonValue(m_end_date_lte));
    }
    if (m_execution_date_gte_isSet) {
        obj.insert(QString("execution_date_gte"), ::OpenAPI::toJsonValue(m_execution_date_gte));
    }
    if (m_execution_date_lte_isSet) {
        obj.insert(QString("execution_date_lte"), ::OpenAPI::toJsonValue(m_execution_date_lte));
    }
    if (m_pool.size() > 0) {
        obj.insert(QString("pool"), ::OpenAPI::toJsonValue(m_pool));
    }
    if (m_queue.size() > 0) {
        obj.insert(QString("queue"), ::OpenAPI::toJsonValue(m_queue));
    }
    if (m_start_date_gte_isSet) {
        obj.insert(QString("start_date_gte"), ::OpenAPI::toJsonValue(m_start_date_gte));
    }
    if (m_start_date_lte_isSet) {
        obj.insert(QString("start_date_lte"), ::OpenAPI::toJsonValue(m_start_date_lte));
    }
    if (m_state.size() > 0) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    return obj;
}

QList<QString> OAIListTaskInstanceForm::getDagIds() const {
    return m_dag_ids;
}
void OAIListTaskInstanceForm::setDagIds(const QList<QString> &dag_ids) {
    m_dag_ids = dag_ids;
    m_dag_ids_isSet = true;
}

bool OAIListTaskInstanceForm::is_dag_ids_Set() const{
    return m_dag_ids_isSet;
}

bool OAIListTaskInstanceForm::is_dag_ids_Valid() const{
    return m_dag_ids_isValid;
}

double OAIListTaskInstanceForm::getDurationGte() const {
    return m_duration_gte;
}
void OAIListTaskInstanceForm::setDurationGte(const double &duration_gte) {
    m_duration_gte = duration_gte;
    m_duration_gte_isSet = true;
}

bool OAIListTaskInstanceForm::is_duration_gte_Set() const{
    return m_duration_gte_isSet;
}

bool OAIListTaskInstanceForm::is_duration_gte_Valid() const{
    return m_duration_gte_isValid;
}

double OAIListTaskInstanceForm::getDurationLte() const {
    return m_duration_lte;
}
void OAIListTaskInstanceForm::setDurationLte(const double &duration_lte) {
    m_duration_lte = duration_lte;
    m_duration_lte_isSet = true;
}

bool OAIListTaskInstanceForm::is_duration_lte_Set() const{
    return m_duration_lte_isSet;
}

bool OAIListTaskInstanceForm::is_duration_lte_Valid() const{
    return m_duration_lte_isValid;
}

QDateTime OAIListTaskInstanceForm::getEndDateGte() const {
    return m_end_date_gte;
}
void OAIListTaskInstanceForm::setEndDateGte(const QDateTime &end_date_gte) {
    m_end_date_gte = end_date_gte;
    m_end_date_gte_isSet = true;
}

bool OAIListTaskInstanceForm::is_end_date_gte_Set() const{
    return m_end_date_gte_isSet;
}

bool OAIListTaskInstanceForm::is_end_date_gte_Valid() const{
    return m_end_date_gte_isValid;
}

QDateTime OAIListTaskInstanceForm::getEndDateLte() const {
    return m_end_date_lte;
}
void OAIListTaskInstanceForm::setEndDateLte(const QDateTime &end_date_lte) {
    m_end_date_lte = end_date_lte;
    m_end_date_lte_isSet = true;
}

bool OAIListTaskInstanceForm::is_end_date_lte_Set() const{
    return m_end_date_lte_isSet;
}

bool OAIListTaskInstanceForm::is_end_date_lte_Valid() const{
    return m_end_date_lte_isValid;
}

QDateTime OAIListTaskInstanceForm::getExecutionDateGte() const {
    return m_execution_date_gte;
}
void OAIListTaskInstanceForm::setExecutionDateGte(const QDateTime &execution_date_gte) {
    m_execution_date_gte = execution_date_gte;
    m_execution_date_gte_isSet = true;
}

bool OAIListTaskInstanceForm::is_execution_date_gte_Set() const{
    return m_execution_date_gte_isSet;
}

bool OAIListTaskInstanceForm::is_execution_date_gte_Valid() const{
    return m_execution_date_gte_isValid;
}

QDateTime OAIListTaskInstanceForm::getExecutionDateLte() const {
    return m_execution_date_lte;
}
void OAIListTaskInstanceForm::setExecutionDateLte(const QDateTime &execution_date_lte) {
    m_execution_date_lte = execution_date_lte;
    m_execution_date_lte_isSet = true;
}

bool OAIListTaskInstanceForm::is_execution_date_lte_Set() const{
    return m_execution_date_lte_isSet;
}

bool OAIListTaskInstanceForm::is_execution_date_lte_Valid() const{
    return m_execution_date_lte_isValid;
}

QList<QString> OAIListTaskInstanceForm::getPool() const {
    return m_pool;
}
void OAIListTaskInstanceForm::setPool(const QList<QString> &pool) {
    m_pool = pool;
    m_pool_isSet = true;
}

bool OAIListTaskInstanceForm::is_pool_Set() const{
    return m_pool_isSet;
}

bool OAIListTaskInstanceForm::is_pool_Valid() const{
    return m_pool_isValid;
}

QList<QString> OAIListTaskInstanceForm::getQueue() const {
    return m_queue;
}
void OAIListTaskInstanceForm::setQueue(const QList<QString> &queue) {
    m_queue = queue;
    m_queue_isSet = true;
}

bool OAIListTaskInstanceForm::is_queue_Set() const{
    return m_queue_isSet;
}

bool OAIListTaskInstanceForm::is_queue_Valid() const{
    return m_queue_isValid;
}

QDateTime OAIListTaskInstanceForm::getStartDateGte() const {
    return m_start_date_gte;
}
void OAIListTaskInstanceForm::setStartDateGte(const QDateTime &start_date_gte) {
    m_start_date_gte = start_date_gte;
    m_start_date_gte_isSet = true;
}

bool OAIListTaskInstanceForm::is_start_date_gte_Set() const{
    return m_start_date_gte_isSet;
}

bool OAIListTaskInstanceForm::is_start_date_gte_Valid() const{
    return m_start_date_gte_isValid;
}

QDateTime OAIListTaskInstanceForm::getStartDateLte() const {
    return m_start_date_lte;
}
void OAIListTaskInstanceForm::setStartDateLte(const QDateTime &start_date_lte) {
    m_start_date_lte = start_date_lte;
    m_start_date_lte_isSet = true;
}

bool OAIListTaskInstanceForm::is_start_date_lte_Set() const{
    return m_start_date_lte_isSet;
}

bool OAIListTaskInstanceForm::is_start_date_lte_Valid() const{
    return m_start_date_lte_isValid;
}

QList<OAITaskState> OAIListTaskInstanceForm::getState() const {
    return m_state;
}
void OAIListTaskInstanceForm::setState(const QList<OAITaskState> &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIListTaskInstanceForm::is_state_Set() const{
    return m_state_isSet;
}

bool OAIListTaskInstanceForm::is_state_Valid() const{
    return m_state_isValid;
}

bool OAIListTaskInstanceForm::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dag_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_gte_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_lte_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_gte_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_date_lte_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_execution_date_gte_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_execution_date_lte_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pool.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_queue.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_gte_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_date_lte_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListTaskInstanceForm::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
