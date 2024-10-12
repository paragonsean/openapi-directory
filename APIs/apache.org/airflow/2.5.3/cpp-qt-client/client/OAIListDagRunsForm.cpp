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

#include "OAIListDagRunsForm.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListDagRunsForm::OAIListDagRunsForm(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListDagRunsForm::OAIListDagRunsForm() {
    this->initializeModel();
}

OAIListDagRunsForm::~OAIListDagRunsForm() {}

void OAIListDagRunsForm::initializeModel() {

    m_dag_ids_isSet = false;
    m_dag_ids_isValid = false;

    m_end_date_gte_isSet = false;
    m_end_date_gte_isValid = false;

    m_end_date_lte_isSet = false;
    m_end_date_lte_isValid = false;

    m_execution_date_gte_isSet = false;
    m_execution_date_gte_isValid = false;

    m_execution_date_lte_isSet = false;
    m_execution_date_lte_isValid = false;

    m_order_by_isSet = false;
    m_order_by_isValid = false;

    m_page_limit_isSet = false;
    m_page_limit_isValid = false;

    m_page_offset_isSet = false;
    m_page_offset_isValid = false;

    m_start_date_gte_isSet = false;
    m_start_date_gte_isValid = false;

    m_start_date_lte_isSet = false;
    m_start_date_lte_isValid = false;

    m_states_isSet = false;
    m_states_isValid = false;
}

void OAIListDagRunsForm::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListDagRunsForm::fromJsonObject(QJsonObject json) {

    m_dag_ids_isValid = ::OpenAPI::fromJsonValue(m_dag_ids, json[QString("dag_ids")]);
    m_dag_ids_isSet = !json[QString("dag_ids")].isNull() && m_dag_ids_isValid;

    m_end_date_gte_isValid = ::OpenAPI::fromJsonValue(m_end_date_gte, json[QString("end_date_gte")]);
    m_end_date_gte_isSet = !json[QString("end_date_gte")].isNull() && m_end_date_gte_isValid;

    m_end_date_lte_isValid = ::OpenAPI::fromJsonValue(m_end_date_lte, json[QString("end_date_lte")]);
    m_end_date_lte_isSet = !json[QString("end_date_lte")].isNull() && m_end_date_lte_isValid;

    m_execution_date_gte_isValid = ::OpenAPI::fromJsonValue(m_execution_date_gte, json[QString("execution_date_gte")]);
    m_execution_date_gte_isSet = !json[QString("execution_date_gte")].isNull() && m_execution_date_gte_isValid;

    m_execution_date_lte_isValid = ::OpenAPI::fromJsonValue(m_execution_date_lte, json[QString("execution_date_lte")]);
    m_execution_date_lte_isSet = !json[QString("execution_date_lte")].isNull() && m_execution_date_lte_isValid;

    m_order_by_isValid = ::OpenAPI::fromJsonValue(m_order_by, json[QString("order_by")]);
    m_order_by_isSet = !json[QString("order_by")].isNull() && m_order_by_isValid;

    m_page_limit_isValid = ::OpenAPI::fromJsonValue(m_page_limit, json[QString("page_limit")]);
    m_page_limit_isSet = !json[QString("page_limit")].isNull() && m_page_limit_isValid;

    m_page_offset_isValid = ::OpenAPI::fromJsonValue(m_page_offset, json[QString("page_offset")]);
    m_page_offset_isSet = !json[QString("page_offset")].isNull() && m_page_offset_isValid;

    m_start_date_gte_isValid = ::OpenAPI::fromJsonValue(m_start_date_gte, json[QString("start_date_gte")]);
    m_start_date_gte_isSet = !json[QString("start_date_gte")].isNull() && m_start_date_gte_isValid;

    m_start_date_lte_isValid = ::OpenAPI::fromJsonValue(m_start_date_lte, json[QString("start_date_lte")]);
    m_start_date_lte_isSet = !json[QString("start_date_lte")].isNull() && m_start_date_lte_isValid;

    m_states_isValid = ::OpenAPI::fromJsonValue(m_states, json[QString("states")]);
    m_states_isSet = !json[QString("states")].isNull() && m_states_isValid;
}

QString OAIListDagRunsForm::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListDagRunsForm::asJsonObject() const {
    QJsonObject obj;
    if (m_dag_ids.size() > 0) {
        obj.insert(QString("dag_ids"), ::OpenAPI::toJsonValue(m_dag_ids));
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
    if (m_order_by_isSet) {
        obj.insert(QString("order_by"), ::OpenAPI::toJsonValue(m_order_by));
    }
    if (m_page_limit_isSet) {
        obj.insert(QString("page_limit"), ::OpenAPI::toJsonValue(m_page_limit));
    }
    if (m_page_offset_isSet) {
        obj.insert(QString("page_offset"), ::OpenAPI::toJsonValue(m_page_offset));
    }
    if (m_start_date_gte_isSet) {
        obj.insert(QString("start_date_gte"), ::OpenAPI::toJsonValue(m_start_date_gte));
    }
    if (m_start_date_lte_isSet) {
        obj.insert(QString("start_date_lte"), ::OpenAPI::toJsonValue(m_start_date_lte));
    }
    if (m_states.size() > 0) {
        obj.insert(QString("states"), ::OpenAPI::toJsonValue(m_states));
    }
    return obj;
}

QList<QString> OAIListDagRunsForm::getDagIds() const {
    return m_dag_ids;
}
void OAIListDagRunsForm::setDagIds(const QList<QString> &dag_ids) {
    m_dag_ids = dag_ids;
    m_dag_ids_isSet = true;
}

bool OAIListDagRunsForm::is_dag_ids_Set() const{
    return m_dag_ids_isSet;
}

bool OAIListDagRunsForm::is_dag_ids_Valid() const{
    return m_dag_ids_isValid;
}

QDateTime OAIListDagRunsForm::getEndDateGte() const {
    return m_end_date_gte;
}
void OAIListDagRunsForm::setEndDateGte(const QDateTime &end_date_gte) {
    m_end_date_gte = end_date_gte;
    m_end_date_gte_isSet = true;
}

bool OAIListDagRunsForm::is_end_date_gte_Set() const{
    return m_end_date_gte_isSet;
}

bool OAIListDagRunsForm::is_end_date_gte_Valid() const{
    return m_end_date_gte_isValid;
}

QDateTime OAIListDagRunsForm::getEndDateLte() const {
    return m_end_date_lte;
}
void OAIListDagRunsForm::setEndDateLte(const QDateTime &end_date_lte) {
    m_end_date_lte = end_date_lte;
    m_end_date_lte_isSet = true;
}

bool OAIListDagRunsForm::is_end_date_lte_Set() const{
    return m_end_date_lte_isSet;
}

bool OAIListDagRunsForm::is_end_date_lte_Valid() const{
    return m_end_date_lte_isValid;
}

QDateTime OAIListDagRunsForm::getExecutionDateGte() const {
    return m_execution_date_gte;
}
void OAIListDagRunsForm::setExecutionDateGte(const QDateTime &execution_date_gte) {
    m_execution_date_gte = execution_date_gte;
    m_execution_date_gte_isSet = true;
}

bool OAIListDagRunsForm::is_execution_date_gte_Set() const{
    return m_execution_date_gte_isSet;
}

bool OAIListDagRunsForm::is_execution_date_gte_Valid() const{
    return m_execution_date_gte_isValid;
}

QDateTime OAIListDagRunsForm::getExecutionDateLte() const {
    return m_execution_date_lte;
}
void OAIListDagRunsForm::setExecutionDateLte(const QDateTime &execution_date_lte) {
    m_execution_date_lte = execution_date_lte;
    m_execution_date_lte_isSet = true;
}

bool OAIListDagRunsForm::is_execution_date_lte_Set() const{
    return m_execution_date_lte_isSet;
}

bool OAIListDagRunsForm::is_execution_date_lte_Valid() const{
    return m_execution_date_lte_isValid;
}

QString OAIListDagRunsForm::getOrderBy() const {
    return m_order_by;
}
void OAIListDagRunsForm::setOrderBy(const QString &order_by) {
    m_order_by = order_by;
    m_order_by_isSet = true;
}

bool OAIListDagRunsForm::is_order_by_Set() const{
    return m_order_by_isSet;
}

bool OAIListDagRunsForm::is_order_by_Valid() const{
    return m_order_by_isValid;
}

qint32 OAIListDagRunsForm::getPageLimit() const {
    return m_page_limit;
}
void OAIListDagRunsForm::setPageLimit(const qint32 &page_limit) {
    m_page_limit = page_limit;
    m_page_limit_isSet = true;
}

bool OAIListDagRunsForm::is_page_limit_Set() const{
    return m_page_limit_isSet;
}

bool OAIListDagRunsForm::is_page_limit_Valid() const{
    return m_page_limit_isValid;
}

qint32 OAIListDagRunsForm::getPageOffset() const {
    return m_page_offset;
}
void OAIListDagRunsForm::setPageOffset(const qint32 &page_offset) {
    m_page_offset = page_offset;
    m_page_offset_isSet = true;
}

bool OAIListDagRunsForm::is_page_offset_Set() const{
    return m_page_offset_isSet;
}

bool OAIListDagRunsForm::is_page_offset_Valid() const{
    return m_page_offset_isValid;
}

QDateTime OAIListDagRunsForm::getStartDateGte() const {
    return m_start_date_gte;
}
void OAIListDagRunsForm::setStartDateGte(const QDateTime &start_date_gte) {
    m_start_date_gte = start_date_gte;
    m_start_date_gte_isSet = true;
}

bool OAIListDagRunsForm::is_start_date_gte_Set() const{
    return m_start_date_gte_isSet;
}

bool OAIListDagRunsForm::is_start_date_gte_Valid() const{
    return m_start_date_gte_isValid;
}

QDateTime OAIListDagRunsForm::getStartDateLte() const {
    return m_start_date_lte;
}
void OAIListDagRunsForm::setStartDateLte(const QDateTime &start_date_lte) {
    m_start_date_lte = start_date_lte;
    m_start_date_lte_isSet = true;
}

bool OAIListDagRunsForm::is_start_date_lte_Set() const{
    return m_start_date_lte_isSet;
}

bool OAIListDagRunsForm::is_start_date_lte_Valid() const{
    return m_start_date_lte_isValid;
}

QList<QString> OAIListDagRunsForm::getStates() const {
    return m_states;
}
void OAIListDagRunsForm::setStates(const QList<QString> &states) {
    m_states = states;
    m_states_isSet = true;
}

bool OAIListDagRunsForm::is_states_Set() const{
    return m_states_isSet;
}

bool OAIListDagRunsForm::is_states_Valid() const{
    return m_states_isValid;
}

bool OAIListDagRunsForm::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dag_ids.size() > 0) {
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

        if (m_order_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_limit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_offset_isSet) {
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

        if (m_states.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListDagRunsForm::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
