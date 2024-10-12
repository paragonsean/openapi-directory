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

#include "OAIPluginCollectionItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPluginCollectionItem::OAIPluginCollectionItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPluginCollectionItem::OAIPluginCollectionItem() {
    this->initializeModel();
}

OAIPluginCollectionItem::~OAIPluginCollectionItem() {}

void OAIPluginCollectionItem::initializeModel() {

    m_appbuilder_menu_items_isSet = false;
    m_appbuilder_menu_items_isValid = false;

    m_appbuilder_views_isSet = false;
    m_appbuilder_views_isValid = false;

    m_executors_isSet = false;
    m_executors_isValid = false;

    m_flask_blueprints_isSet = false;
    m_flask_blueprints_isValid = false;

    m_global_operator_extra_links_isSet = false;
    m_global_operator_extra_links_isValid = false;

    m_hooks_isSet = false;
    m_hooks_isValid = false;

    m_macros_isSet = false;
    m_macros_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_operator_extra_links_isSet = false;
    m_operator_extra_links_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;
}

void OAIPluginCollectionItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPluginCollectionItem::fromJsonObject(QJsonObject json) {

    m_appbuilder_menu_items_isValid = ::OpenAPI::fromJsonValue(m_appbuilder_menu_items, json[QString("appbuilder_menu_items")]);
    m_appbuilder_menu_items_isSet = !json[QString("appbuilder_menu_items")].isNull() && m_appbuilder_menu_items_isValid;

    m_appbuilder_views_isValid = ::OpenAPI::fromJsonValue(m_appbuilder_views, json[QString("appbuilder_views")]);
    m_appbuilder_views_isSet = !json[QString("appbuilder_views")].isNull() && m_appbuilder_views_isValid;

    m_executors_isValid = ::OpenAPI::fromJsonValue(m_executors, json[QString("executors")]);
    m_executors_isSet = !json[QString("executors")].isNull() && m_executors_isValid;

    m_flask_blueprints_isValid = ::OpenAPI::fromJsonValue(m_flask_blueprints, json[QString("flask_blueprints")]);
    m_flask_blueprints_isSet = !json[QString("flask_blueprints")].isNull() && m_flask_blueprints_isValid;

    m_global_operator_extra_links_isValid = ::OpenAPI::fromJsonValue(m_global_operator_extra_links, json[QString("global_operator_extra_links")]);
    m_global_operator_extra_links_isSet = !json[QString("global_operator_extra_links")].isNull() && m_global_operator_extra_links_isValid;

    m_hooks_isValid = ::OpenAPI::fromJsonValue(m_hooks, json[QString("hooks")]);
    m_hooks_isSet = !json[QString("hooks")].isNull() && m_hooks_isValid;

    m_macros_isValid = ::OpenAPI::fromJsonValue(m_macros, json[QString("macros")]);
    m_macros_isSet = !json[QString("macros")].isNull() && m_macros_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_operator_extra_links_isValid = ::OpenAPI::fromJsonValue(m_operator_extra_links, json[QString("operator_extra_links")]);
    m_operator_extra_links_isSet = !json[QString("operator_extra_links")].isNull() && m_operator_extra_links_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;
}

QString OAIPluginCollectionItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPluginCollectionItem::asJsonObject() const {
    QJsonObject obj;
    if (m_appbuilder_menu_items.size() > 0) {
        obj.insert(QString("appbuilder_menu_items"), ::OpenAPI::toJsonValue(m_appbuilder_menu_items));
    }
    if (m_appbuilder_views.size() > 0) {
        obj.insert(QString("appbuilder_views"), ::OpenAPI::toJsonValue(m_appbuilder_views));
    }
    if (m_executors.size() > 0) {
        obj.insert(QString("executors"), ::OpenAPI::toJsonValue(m_executors));
    }
    if (m_flask_blueprints.size() > 0) {
        obj.insert(QString("flask_blueprints"), ::OpenAPI::toJsonValue(m_flask_blueprints));
    }
    if (m_global_operator_extra_links.size() > 0) {
        obj.insert(QString("global_operator_extra_links"), ::OpenAPI::toJsonValue(m_global_operator_extra_links));
    }
    if (m_hooks.size() > 0) {
        obj.insert(QString("hooks"), ::OpenAPI::toJsonValue(m_hooks));
    }
    if (m_macros.size() > 0) {
        obj.insert(QString("macros"), ::OpenAPI::toJsonValue(m_macros));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_operator_extra_links.size() > 0) {
        obj.insert(QString("operator_extra_links"), ::OpenAPI::toJsonValue(m_operator_extra_links));
    }
    if (m_source_isSet) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    return obj;
}

QList<OAIObject> OAIPluginCollectionItem::getAppbuilderMenuItems() const {
    return m_appbuilder_menu_items;
}
void OAIPluginCollectionItem::setAppbuilderMenuItems(const QList<OAIObject> &appbuilder_menu_items) {
    m_appbuilder_menu_items = appbuilder_menu_items;
    m_appbuilder_menu_items_isSet = true;
}

bool OAIPluginCollectionItem::is_appbuilder_menu_items_Set() const{
    return m_appbuilder_menu_items_isSet;
}

bool OAIPluginCollectionItem::is_appbuilder_menu_items_Valid() const{
    return m_appbuilder_menu_items_isValid;
}

QList<OAIObject> OAIPluginCollectionItem::getAppbuilderViews() const {
    return m_appbuilder_views;
}
void OAIPluginCollectionItem::setAppbuilderViews(const QList<OAIObject> &appbuilder_views) {
    m_appbuilder_views = appbuilder_views;
    m_appbuilder_views_isSet = true;
}

bool OAIPluginCollectionItem::is_appbuilder_views_Set() const{
    return m_appbuilder_views_isSet;
}

bool OAIPluginCollectionItem::is_appbuilder_views_Valid() const{
    return m_appbuilder_views_isValid;
}

QList<QString> OAIPluginCollectionItem::getExecutors() const {
    return m_executors;
}
void OAIPluginCollectionItem::setExecutors(const QList<QString> &executors) {
    m_executors = executors;
    m_executors_isSet = true;
}

bool OAIPluginCollectionItem::is_executors_Set() const{
    return m_executors_isSet;
}

bool OAIPluginCollectionItem::is_executors_Valid() const{
    return m_executors_isValid;
}

QList<OAIObject> OAIPluginCollectionItem::getFlaskBlueprints() const {
    return m_flask_blueprints;
}
void OAIPluginCollectionItem::setFlaskBlueprints(const QList<OAIObject> &flask_blueprints) {
    m_flask_blueprints = flask_blueprints;
    m_flask_blueprints_isSet = true;
}

bool OAIPluginCollectionItem::is_flask_blueprints_Set() const{
    return m_flask_blueprints_isSet;
}

bool OAIPluginCollectionItem::is_flask_blueprints_Valid() const{
    return m_flask_blueprints_isValid;
}

QList<OAIObject> OAIPluginCollectionItem::getGlobalOperatorExtraLinks() const {
    return m_global_operator_extra_links;
}
void OAIPluginCollectionItem::setGlobalOperatorExtraLinks(const QList<OAIObject> &global_operator_extra_links) {
    m_global_operator_extra_links = global_operator_extra_links;
    m_global_operator_extra_links_isSet = true;
}

bool OAIPluginCollectionItem::is_global_operator_extra_links_Set() const{
    return m_global_operator_extra_links_isSet;
}

bool OAIPluginCollectionItem::is_global_operator_extra_links_Valid() const{
    return m_global_operator_extra_links_isValid;
}

QList<QString> OAIPluginCollectionItem::getHooks() const {
    return m_hooks;
}
void OAIPluginCollectionItem::setHooks(const QList<QString> &hooks) {
    m_hooks = hooks;
    m_hooks_isSet = true;
}

bool OAIPluginCollectionItem::is_hooks_Set() const{
    return m_hooks_isSet;
}

bool OAIPluginCollectionItem::is_hooks_Valid() const{
    return m_hooks_isValid;
}

QList<OAIObject> OAIPluginCollectionItem::getMacros() const {
    return m_macros;
}
void OAIPluginCollectionItem::setMacros(const QList<OAIObject> &macros) {
    m_macros = macros;
    m_macros_isSet = true;
}

bool OAIPluginCollectionItem::is_macros_Set() const{
    return m_macros_isSet;
}

bool OAIPluginCollectionItem::is_macros_Valid() const{
    return m_macros_isValid;
}

QString OAIPluginCollectionItem::getName() const {
    return m_name;
}
void OAIPluginCollectionItem::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPluginCollectionItem::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPluginCollectionItem::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIObject> OAIPluginCollectionItem::getOperatorExtraLinks() const {
    return m_operator_extra_links;
}
void OAIPluginCollectionItem::setOperatorExtraLinks(const QList<OAIObject> &operator_extra_links) {
    m_operator_extra_links = operator_extra_links;
    m_operator_extra_links_isSet = true;
}

bool OAIPluginCollectionItem::is_operator_extra_links_Set() const{
    return m_operator_extra_links_isSet;
}

bool OAIPluginCollectionItem::is_operator_extra_links_Valid() const{
    return m_operator_extra_links_isValid;
}

QString OAIPluginCollectionItem::getSource() const {
    return m_source;
}
void OAIPluginCollectionItem::setSource(const QString &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIPluginCollectionItem::is_source_Set() const{
    return m_source_isSet;
}

bool OAIPluginCollectionItem::is_source_Valid() const{
    return m_source_isValid;
}

bool OAIPluginCollectionItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_appbuilder_menu_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_appbuilder_views.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_executors.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_flask_blueprints.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_global_operator_extra_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_hooks.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_macros.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_operator_extra_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPluginCollectionItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
