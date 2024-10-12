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

#include "OAICreateTagGroup_200_response_tag_group.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateTagGroup_200_response_tag_group::OAICreateTagGroup_200_response_tag_group(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateTagGroup_200_response_tag_group::OAICreateTagGroup_200_response_tag_group() {
    this->initializeModel();
}

OAICreateTagGroup_200_response_tag_group::~OAICreateTagGroup_200_response_tag_group() {}

void OAICreateTagGroup_200_response_tag_group::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_one_per_topic_isSet = false;
    m_one_per_topic_isValid = false;

    m_parent_tag_name_isSet = false;
    m_parent_tag_name_isValid = false;

    m_permissions_isSet = false;
    m_permissions_isValid = false;

    m_tag_names_isSet = false;
    m_tag_names_isValid = false;
}

void OAICreateTagGroup_200_response_tag_group::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateTagGroup_200_response_tag_group::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_one_per_topic_isValid = ::OpenAPI::fromJsonValue(m_one_per_topic, json[QString("one_per_topic")]);
    m_one_per_topic_isSet = !json[QString("one_per_topic")].isNull() && m_one_per_topic_isValid;

    m_parent_tag_name_isValid = ::OpenAPI::fromJsonValue(m_parent_tag_name, json[QString("parent_tag_name")]);
    m_parent_tag_name_isSet = !json[QString("parent_tag_name")].isNull() && m_parent_tag_name_isValid;

    m_permissions_isValid = ::OpenAPI::fromJsonValue(m_permissions, json[QString("permissions")]);
    m_permissions_isSet = !json[QString("permissions")].isNull() && m_permissions_isValid;

    m_tag_names_isValid = ::OpenAPI::fromJsonValue(m_tag_names, json[QString("tag_names")]);
    m_tag_names_isSet = !json[QString("tag_names")].isNull() && m_tag_names_isValid;
}

QString OAICreateTagGroup_200_response_tag_group::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateTagGroup_200_response_tag_group::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_one_per_topic_isSet) {
        obj.insert(QString("one_per_topic"), ::OpenAPI::toJsonValue(m_one_per_topic));
    }
    if (m_parent_tag_name.size() > 0) {
        obj.insert(QString("parent_tag_name"), ::OpenAPI::toJsonValue(m_parent_tag_name));
    }
    if (m_permissions_isSet) {
        obj.insert(QString("permissions"), ::OpenAPI::toJsonValue(m_permissions));
    }
    if (m_tag_names.size() > 0) {
        obj.insert(QString("tag_names"), ::OpenAPI::toJsonValue(m_tag_names));
    }
    return obj;
}

qint32 OAICreateTagGroup_200_response_tag_group::getId() const {
    return m_id;
}
void OAICreateTagGroup_200_response_tag_group::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICreateTagGroup_200_response_tag_group::is_id_Set() const{
    return m_id_isSet;
}

bool OAICreateTagGroup_200_response_tag_group::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICreateTagGroup_200_response_tag_group::getName() const {
    return m_name;
}
void OAICreateTagGroup_200_response_tag_group::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateTagGroup_200_response_tag_group::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateTagGroup_200_response_tag_group::is_name_Valid() const{
    return m_name_isValid;
}

bool OAICreateTagGroup_200_response_tag_group::isOnePerTopic() const {
    return m_one_per_topic;
}
void OAICreateTagGroup_200_response_tag_group::setOnePerTopic(const bool &one_per_topic) {
    m_one_per_topic = one_per_topic;
    m_one_per_topic_isSet = true;
}

bool OAICreateTagGroup_200_response_tag_group::is_one_per_topic_Set() const{
    return m_one_per_topic_isSet;
}

bool OAICreateTagGroup_200_response_tag_group::is_one_per_topic_Valid() const{
    return m_one_per_topic_isValid;
}

QList<QJsonValue> OAICreateTagGroup_200_response_tag_group::getParentTagName() const {
    return m_parent_tag_name;
}
void OAICreateTagGroup_200_response_tag_group::setParentTagName(const QList<QJsonValue> &parent_tag_name) {
    m_parent_tag_name = parent_tag_name;
    m_parent_tag_name_isSet = true;
}

bool OAICreateTagGroup_200_response_tag_group::is_parent_tag_name_Set() const{
    return m_parent_tag_name_isSet;
}

bool OAICreateTagGroup_200_response_tag_group::is_parent_tag_name_Valid() const{
    return m_parent_tag_name_isValid;
}

OAIObject OAICreateTagGroup_200_response_tag_group::getPermissions() const {
    return m_permissions;
}
void OAICreateTagGroup_200_response_tag_group::setPermissions(const OAIObject &permissions) {
    m_permissions = permissions;
    m_permissions_isSet = true;
}

bool OAICreateTagGroup_200_response_tag_group::is_permissions_Set() const{
    return m_permissions_isSet;
}

bool OAICreateTagGroup_200_response_tag_group::is_permissions_Valid() const{
    return m_permissions_isValid;
}

QList<QJsonValue> OAICreateTagGroup_200_response_tag_group::getTagNames() const {
    return m_tag_names;
}
void OAICreateTagGroup_200_response_tag_group::setTagNames(const QList<QJsonValue> &tag_names) {
    m_tag_names = tag_names;
    m_tag_names_isSet = true;
}

bool OAICreateTagGroup_200_response_tag_group::is_tag_names_Set() const{
    return m_tag_names_isSet;
}

bool OAICreateTagGroup_200_response_tag_group::is_tag_names_Valid() const{
    return m_tag_names_isValid;
}

bool OAICreateTagGroup_200_response_tag_group::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_one_per_topic_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_tag_name.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_permissions_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_names.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateTagGroup_200_response_tag_group::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_name_isValid && m_one_per_topic_isValid && m_parent_tag_name_isValid && m_permissions_isValid && m_tag_names_isValid && true;
}

} // namespace OpenAPI
