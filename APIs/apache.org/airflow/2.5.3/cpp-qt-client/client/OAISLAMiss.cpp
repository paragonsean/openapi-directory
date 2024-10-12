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

#include "OAISLAMiss.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISLAMiss::OAISLAMiss(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISLAMiss::OAISLAMiss() {
    this->initializeModel();
}

OAISLAMiss::~OAISLAMiss() {}

void OAISLAMiss::initializeModel() {

    m_dag_id_isSet = false;
    m_dag_id_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_email_sent_isSet = false;
    m_email_sent_isValid = false;

    m_execution_date_isSet = false;
    m_execution_date_isValid = false;

    m_notification_sent_isSet = false;
    m_notification_sent_isValid = false;

    m_task_id_isSet = false;
    m_task_id_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAISLAMiss::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISLAMiss::fromJsonObject(QJsonObject json) {

    m_dag_id_isValid = ::OpenAPI::fromJsonValue(m_dag_id, json[QString("dag_id")]);
    m_dag_id_isSet = !json[QString("dag_id")].isNull() && m_dag_id_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_email_sent_isValid = ::OpenAPI::fromJsonValue(m_email_sent, json[QString("email_sent")]);
    m_email_sent_isSet = !json[QString("email_sent")].isNull() && m_email_sent_isValid;

    m_execution_date_isValid = ::OpenAPI::fromJsonValue(m_execution_date, json[QString("execution_date")]);
    m_execution_date_isSet = !json[QString("execution_date")].isNull() && m_execution_date_isValid;

    m_notification_sent_isValid = ::OpenAPI::fromJsonValue(m_notification_sent, json[QString("notification_sent")]);
    m_notification_sent_isSet = !json[QString("notification_sent")].isNull() && m_notification_sent_isValid;

    m_task_id_isValid = ::OpenAPI::fromJsonValue(m_task_id, json[QString("task_id")]);
    m_task_id_isSet = !json[QString("task_id")].isNull() && m_task_id_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;
}

QString OAISLAMiss::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISLAMiss::asJsonObject() const {
    QJsonObject obj;
    if (m_dag_id_isSet) {
        obj.insert(QString("dag_id"), ::OpenAPI::toJsonValue(m_dag_id));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_email_sent_isSet) {
        obj.insert(QString("email_sent"), ::OpenAPI::toJsonValue(m_email_sent));
    }
    if (m_execution_date_isSet) {
        obj.insert(QString("execution_date"), ::OpenAPI::toJsonValue(m_execution_date));
    }
    if (m_notification_sent_isSet) {
        obj.insert(QString("notification_sent"), ::OpenAPI::toJsonValue(m_notification_sent));
    }
    if (m_task_id_isSet) {
        obj.insert(QString("task_id"), ::OpenAPI::toJsonValue(m_task_id));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    return obj;
}

QString OAISLAMiss::getDagId() const {
    return m_dag_id;
}
void OAISLAMiss::setDagId(const QString &dag_id) {
    m_dag_id = dag_id;
    m_dag_id_isSet = true;
}

bool OAISLAMiss::is_dag_id_Set() const{
    return m_dag_id_isSet;
}

bool OAISLAMiss::is_dag_id_Valid() const{
    return m_dag_id_isValid;
}

QString OAISLAMiss::getDescription() const {
    return m_description;
}
void OAISLAMiss::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAISLAMiss::is_description_Set() const{
    return m_description_isSet;
}

bool OAISLAMiss::is_description_Valid() const{
    return m_description_isValid;
}

bool OAISLAMiss::isEmailSent() const {
    return m_email_sent;
}
void OAISLAMiss::setEmailSent(const bool &email_sent) {
    m_email_sent = email_sent;
    m_email_sent_isSet = true;
}

bool OAISLAMiss::is_email_sent_Set() const{
    return m_email_sent_isSet;
}

bool OAISLAMiss::is_email_sent_Valid() const{
    return m_email_sent_isValid;
}

QString OAISLAMiss::getExecutionDate() const {
    return m_execution_date;
}
void OAISLAMiss::setExecutionDate(const QString &execution_date) {
    m_execution_date = execution_date;
    m_execution_date_isSet = true;
}

bool OAISLAMiss::is_execution_date_Set() const{
    return m_execution_date_isSet;
}

bool OAISLAMiss::is_execution_date_Valid() const{
    return m_execution_date_isValid;
}

bool OAISLAMiss::isNotificationSent() const {
    return m_notification_sent;
}
void OAISLAMiss::setNotificationSent(const bool &notification_sent) {
    m_notification_sent = notification_sent;
    m_notification_sent_isSet = true;
}

bool OAISLAMiss::is_notification_sent_Set() const{
    return m_notification_sent_isSet;
}

bool OAISLAMiss::is_notification_sent_Valid() const{
    return m_notification_sent_isValid;
}

QString OAISLAMiss::getTaskId() const {
    return m_task_id;
}
void OAISLAMiss::setTaskId(const QString &task_id) {
    m_task_id = task_id;
    m_task_id_isSet = true;
}

bool OAISLAMiss::is_task_id_Set() const{
    return m_task_id_isSet;
}

bool OAISLAMiss::is_task_id_Valid() const{
    return m_task_id_isValid;
}

QString OAISLAMiss::getTimestamp() const {
    return m_timestamp;
}
void OAISLAMiss::setTimestamp(const QString &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAISLAMiss::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAISLAMiss::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAISLAMiss::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_dag_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_sent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_execution_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notification_sent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_task_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISLAMiss::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
