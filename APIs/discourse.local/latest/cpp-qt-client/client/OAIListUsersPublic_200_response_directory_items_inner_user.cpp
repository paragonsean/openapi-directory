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

#include "OAIListUsersPublic_200_response_directory_items_inner_user.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListUsersPublic_200_response_directory_items_inner_user::OAIListUsersPublic_200_response_directory_items_inner_user(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListUsersPublic_200_response_directory_items_inner_user::OAIListUsersPublic_200_response_directory_items_inner_user() {
    this->initializeModel();
}

OAIListUsersPublic_200_response_directory_items_inner_user::~OAIListUsersPublic_200_response_directory_items_inner_user() {}

void OAIListUsersPublic_200_response_directory_items_inner_user::initializeModel() {

    m_avatar_template_isSet = false;
    m_avatar_template_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAIListUsersPublic_200_response_directory_items_inner_user::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListUsersPublic_200_response_directory_items_inner_user::fromJsonObject(QJsonObject json) {

    m_avatar_template_isValid = ::OpenAPI::fromJsonValue(m_avatar_template, json[QString("avatar_template")]);
    m_avatar_template_isSet = !json[QString("avatar_template")].isNull() && m_avatar_template_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAIListUsersPublic_200_response_directory_items_inner_user::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListUsersPublic_200_response_directory_items_inner_user::asJsonObject() const {
    QJsonObject obj;
    if (m_avatar_template_isSet) {
        obj.insert(QString("avatar_template"), ::OpenAPI::toJsonValue(m_avatar_template));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAIListUsersPublic_200_response_directory_items_inner_user::getAvatarTemplate() const {
    return m_avatar_template;
}
void OAIListUsersPublic_200_response_directory_items_inner_user::setAvatarTemplate(const QString &avatar_template) {
    m_avatar_template = avatar_template;
    m_avatar_template_isSet = true;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::is_avatar_template_Set() const{
    return m_avatar_template_isSet;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::is_avatar_template_Valid() const{
    return m_avatar_template_isValid;
}

qint32 OAIListUsersPublic_200_response_directory_items_inner_user::getId() const {
    return m_id;
}
void OAIListUsersPublic_200_response_directory_items_inner_user::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::is_id_Set() const{
    return m_id_isSet;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIListUsersPublic_200_response_directory_items_inner_user::getName() const {
    return m_name;
}
void OAIListUsersPublic_200_response_directory_items_inner_user::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::is_name_Set() const{
    return m_name_isSet;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIListUsersPublic_200_response_directory_items_inner_user::getTitle() const {
    return m_title;
}
void OAIListUsersPublic_200_response_directory_items_inner_user::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::is_title_Set() const{
    return m_title_isSet;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIListUsersPublic_200_response_directory_items_inner_user::getUsername() const {
    return m_username;
}
void OAIListUsersPublic_200_response_directory_items_inner_user::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::is_username_Set() const{
    return m_username_isSet;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_avatar_template_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_username_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListUsersPublic_200_response_directory_items_inner_user::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_avatar_template_isValid && m_id_isValid && m_name_isValid && m_title_isValid && m_username_isValid && true;
}

} // namespace OpenAPI
