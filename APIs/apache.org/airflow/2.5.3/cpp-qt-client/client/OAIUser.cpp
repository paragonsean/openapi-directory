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

#include "OAIUser.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUser::OAIUser(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUser::OAIUser() {
    this->initializeModel();
}

OAIUser::~OAIUser() {}

void OAIUser::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_changed_on_isSet = false;
    m_changed_on_isValid = false;

    m_created_on_isSet = false;
    m_created_on_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_failed_login_count_isSet = false;
    m_failed_login_count_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_last_login_isSet = false;
    m_last_login_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_login_count_isSet = false;
    m_login_count_isValid = false;

    m_roles_isSet = false;
    m_roles_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;
}

void OAIUser::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUser::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("active")]);
    m_active_isSet = !json[QString("active")].isNull() && m_active_isValid;

    m_changed_on_isValid = ::OpenAPI::fromJsonValue(m_changed_on, json[QString("changed_on")]);
    m_changed_on_isSet = !json[QString("changed_on")].isNull() && m_changed_on_isValid;

    m_created_on_isValid = ::OpenAPI::fromJsonValue(m_created_on, json[QString("created_on")]);
    m_created_on_isSet = !json[QString("created_on")].isNull() && m_created_on_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_failed_login_count_isValid = ::OpenAPI::fromJsonValue(m_failed_login_count, json[QString("failed_login_count")]);
    m_failed_login_count_isSet = !json[QString("failed_login_count")].isNull() && m_failed_login_count_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_last_login_isValid = ::OpenAPI::fromJsonValue(m_last_login, json[QString("last_login")]);
    m_last_login_isSet = !json[QString("last_login")].isNull() && m_last_login_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_login_count_isValid = ::OpenAPI::fromJsonValue(m_login_count, json[QString("login_count")]);
    m_login_count_isSet = !json[QString("login_count")].isNull() && m_login_count_isValid;

    m_roles_isValid = ::OpenAPI::fromJsonValue(m_roles, json[QString("roles")]);
    m_roles_isSet = !json[QString("roles")].isNull() && m_roles_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;
}

QString OAIUser::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUser::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_changed_on_isSet) {
        obj.insert(QString("changed_on"), ::OpenAPI::toJsonValue(m_changed_on));
    }
    if (m_created_on_isSet) {
        obj.insert(QString("created_on"), ::OpenAPI::toJsonValue(m_created_on));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_failed_login_count_isSet) {
        obj.insert(QString("failed_login_count"), ::OpenAPI::toJsonValue(m_failed_login_count));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_last_login_isSet) {
        obj.insert(QString("last_login"), ::OpenAPI::toJsonValue(m_last_login));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_login_count_isSet) {
        obj.insert(QString("login_count"), ::OpenAPI::toJsonValue(m_login_count));
    }
    if (m_roles.size() > 0) {
        obj.insert(QString("roles"), ::OpenAPI::toJsonValue(m_roles));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    return obj;
}

bool OAIUser::isActive() const {
    return m_active;
}
void OAIUser::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAIUser::is_active_Set() const{
    return m_active_isSet;
}

bool OAIUser::is_active_Valid() const{
    return m_active_isValid;
}

QString OAIUser::getChangedOn() const {
    return m_changed_on;
}
void OAIUser::setChangedOn(const QString &changed_on) {
    m_changed_on = changed_on;
    m_changed_on_isSet = true;
}

bool OAIUser::is_changed_on_Set() const{
    return m_changed_on_isSet;
}

bool OAIUser::is_changed_on_Valid() const{
    return m_changed_on_isValid;
}

QString OAIUser::getCreatedOn() const {
    return m_created_on;
}
void OAIUser::setCreatedOn(const QString &created_on) {
    m_created_on = created_on;
    m_created_on_isSet = true;
}

bool OAIUser::is_created_on_Set() const{
    return m_created_on_isSet;
}

bool OAIUser::is_created_on_Valid() const{
    return m_created_on_isValid;
}

QString OAIUser::getEmail() const {
    return m_email;
}
void OAIUser::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIUser::is_email_Set() const{
    return m_email_isSet;
}

bool OAIUser::is_email_Valid() const{
    return m_email_isValid;
}

qint32 OAIUser::getFailedLoginCount() const {
    return m_failed_login_count;
}
void OAIUser::setFailedLoginCount(const qint32 &failed_login_count) {
    m_failed_login_count = failed_login_count;
    m_failed_login_count_isSet = true;
}

bool OAIUser::is_failed_login_count_Set() const{
    return m_failed_login_count_isSet;
}

bool OAIUser::is_failed_login_count_Valid() const{
    return m_failed_login_count_isValid;
}

QString OAIUser::getFirstName() const {
    return m_first_name;
}
void OAIUser::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIUser::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIUser::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIUser::getLastLogin() const {
    return m_last_login;
}
void OAIUser::setLastLogin(const QString &last_login) {
    m_last_login = last_login;
    m_last_login_isSet = true;
}

bool OAIUser::is_last_login_Set() const{
    return m_last_login_isSet;
}

bool OAIUser::is_last_login_Valid() const{
    return m_last_login_isValid;
}

QString OAIUser::getLastName() const {
    return m_last_name;
}
void OAIUser::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIUser::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIUser::is_last_name_Valid() const{
    return m_last_name_isValid;
}

qint32 OAIUser::getLoginCount() const {
    return m_login_count;
}
void OAIUser::setLoginCount(const qint32 &login_count) {
    m_login_count = login_count;
    m_login_count_isSet = true;
}

bool OAIUser::is_login_count_Set() const{
    return m_login_count_isSet;
}

bool OAIUser::is_login_count_Valid() const{
    return m_login_count_isValid;
}

QList<OAIUserCollectionItem_roles_inner> OAIUser::getRoles() const {
    return m_roles;
}
void OAIUser::setRoles(const QList<OAIUserCollectionItem_roles_inner> &roles) {
    m_roles = roles;
    m_roles_isSet = true;
}

bool OAIUser::is_roles_Set() const{
    return m_roles_isSet;
}

bool OAIUser::is_roles_Valid() const{
    return m_roles_isValid;
}

QString OAIUser::getUsername() const {
    return m_username;
}
void OAIUser::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIUser::is_username_Set() const{
    return m_username_isSet;
}

bool OAIUser::is_username_Valid() const{
    return m_username_isValid;
}

QString OAIUser::getPassword() const {
    return m_password;
}
void OAIUser::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIUser::is_password_Set() const{
    return m_password_isSet;
}

bool OAIUser::is_password_Valid() const{
    return m_password_isValid;
}

bool OAIUser::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_changed_on_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_on_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_failed_login_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_login_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_login_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_roles.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUser::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
