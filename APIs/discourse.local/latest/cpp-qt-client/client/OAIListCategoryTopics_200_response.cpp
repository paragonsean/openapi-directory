/**
 * Discourse API Documentation
 * This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 
 *
 * The version of the OpenAPI document: latest
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIListCategoryTopics_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListCategoryTopics_200_response::OAIListCategoryTopics_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListCategoryTopics_200_response::OAIListCategoryTopics_200_response() {
    this->initializeModel();
}

OAIListCategoryTopics_200_response::~OAIListCategoryTopics_200_response() {}

void OAIListCategoryTopics_200_response::initializeModel() {

    m_primary_groups_isSet = false;
    m_primary_groups_isValid = false;

    m_topic_list_isSet = false;
    m_topic_list_isValid = false;

    m_users_isSet = false;
    m_users_isValid = false;
}

void OAIListCategoryTopics_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListCategoryTopics_200_response::fromJsonObject(QJsonObject json) {

    m_primary_groups_isValid = ::OpenAPI::fromJsonValue(m_primary_groups, json[QString("primary_groups")]);
    m_primary_groups_isSet = !json[QString("primary_groups")].isNull() && m_primary_groups_isValid;

    m_topic_list_isValid = ::OpenAPI::fromJsonValue(m_topic_list, json[QString("topic_list")]);
    m_topic_list_isSet = !json[QString("topic_list")].isNull() && m_topic_list_isValid;

    m_users_isValid = ::OpenAPI::fromJsonValue(m_users, json[QString("users")]);
    m_users_isSet = !json[QString("users")].isNull() && m_users_isValid;
}

QString OAIListCategoryTopics_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListCategoryTopics_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_primary_groups.size() > 0) {
        obj.insert(QString("primary_groups"), ::OpenAPI::toJsonValue(m_primary_groups));
    }
    if (m_topic_list.isSet()) {
        obj.insert(QString("topic_list"), ::OpenAPI::toJsonValue(m_topic_list));
    }
    if (m_users.size() > 0) {
        obj.insert(QString("users"), ::OpenAPI::toJsonValue(m_users));
    }
    return obj;
}

QList<QJsonValue> OAIListCategoryTopics_200_response::getPrimaryGroups() const {
    return m_primary_groups;
}
void OAIListCategoryTopics_200_response::setPrimaryGroups(const QList<QJsonValue> &primary_groups) {
    m_primary_groups = primary_groups;
    m_primary_groups_isSet = true;
}

bool OAIListCategoryTopics_200_response::is_primary_groups_Set() const{
    return m_primary_groups_isSet;
}

bool OAIListCategoryTopics_200_response::is_primary_groups_Valid() const{
    return m_primary_groups_isValid;
}

OAIListCategoryTopics_200_response_topic_list OAIListCategoryTopics_200_response::getTopicList() const {
    return m_topic_list;
}
void OAIListCategoryTopics_200_response::setTopicList(const OAIListCategoryTopics_200_response_topic_list &topic_list) {
    m_topic_list = topic_list;
    m_topic_list_isSet = true;
}

bool OAIListCategoryTopics_200_response::is_topic_list_Set() const{
    return m_topic_list_isSet;
}

bool OAIListCategoryTopics_200_response::is_topic_list_Valid() const{
    return m_topic_list_isValid;
}

QList<OAIAdminGetUser_200_response_approved_by> OAIListCategoryTopics_200_response::getUsers() const {
    return m_users;
}
void OAIListCategoryTopics_200_response::setUsers(const QList<OAIAdminGetUser_200_response_approved_by> &users) {
    m_users = users;
    m_users_isSet = true;
}

bool OAIListCategoryTopics_200_response::is_users_Set() const{
    return m_users_isSet;
}

bool OAIListCategoryTopics_200_response::is_users_Valid() const{
    return m_users_isValid;
}

bool OAIListCategoryTopics_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_primary_groups.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_topic_list.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_users.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListCategoryTopics_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_topic_list_isValid && true;
}

} // namespace OpenAPI
