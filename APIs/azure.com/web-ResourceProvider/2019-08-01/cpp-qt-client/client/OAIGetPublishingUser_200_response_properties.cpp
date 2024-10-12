/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetPublishingUser_200_response_properties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetPublishingUser_200_response_properties::OAIGetPublishingUser_200_response_properties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetPublishingUser_200_response_properties::OAIGetPublishingUser_200_response_properties() {
    this->initializeModel();
}

OAIGetPublishingUser_200_response_properties::~OAIGetPublishingUser_200_response_properties() {}

void OAIGetPublishingUser_200_response_properties::initializeModel() {

    m_publishing_password_isSet = false;
    m_publishing_password_isValid = false;

    m_publishing_password_hash_isSet = false;
    m_publishing_password_hash_isValid = false;

    m_publishing_password_hash_salt_isSet = false;
    m_publishing_password_hash_salt_isValid = false;

    m_publishing_user_name_isSet = false;
    m_publishing_user_name_isValid = false;

    m_scm_uri_isSet = false;
    m_scm_uri_isValid = false;
}

void OAIGetPublishingUser_200_response_properties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetPublishingUser_200_response_properties::fromJsonObject(QJsonObject json) {

    m_publishing_password_isValid = ::OpenAPI::fromJsonValue(m_publishing_password, json[QString("publishingPassword")]);
    m_publishing_password_isSet = !json[QString("publishingPassword")].isNull() && m_publishing_password_isValid;

    m_publishing_password_hash_isValid = ::OpenAPI::fromJsonValue(m_publishing_password_hash, json[QString("publishingPasswordHash")]);
    m_publishing_password_hash_isSet = !json[QString("publishingPasswordHash")].isNull() && m_publishing_password_hash_isValid;

    m_publishing_password_hash_salt_isValid = ::OpenAPI::fromJsonValue(m_publishing_password_hash_salt, json[QString("publishingPasswordHashSalt")]);
    m_publishing_password_hash_salt_isSet = !json[QString("publishingPasswordHashSalt")].isNull() && m_publishing_password_hash_salt_isValid;

    m_publishing_user_name_isValid = ::OpenAPI::fromJsonValue(m_publishing_user_name, json[QString("publishingUserName")]);
    m_publishing_user_name_isSet = !json[QString("publishingUserName")].isNull() && m_publishing_user_name_isValid;

    m_scm_uri_isValid = ::OpenAPI::fromJsonValue(m_scm_uri, json[QString("scmUri")]);
    m_scm_uri_isSet = !json[QString("scmUri")].isNull() && m_scm_uri_isValid;
}

QString OAIGetPublishingUser_200_response_properties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetPublishingUser_200_response_properties::asJsonObject() const {
    QJsonObject obj;
    if (m_publishing_password_isSet) {
        obj.insert(QString("publishingPassword"), ::OpenAPI::toJsonValue(m_publishing_password));
    }
    if (m_publishing_password_hash_isSet) {
        obj.insert(QString("publishingPasswordHash"), ::OpenAPI::toJsonValue(m_publishing_password_hash));
    }
    if (m_publishing_password_hash_salt_isSet) {
        obj.insert(QString("publishingPasswordHashSalt"), ::OpenAPI::toJsonValue(m_publishing_password_hash_salt));
    }
    if (m_publishing_user_name_isSet) {
        obj.insert(QString("publishingUserName"), ::OpenAPI::toJsonValue(m_publishing_user_name));
    }
    if (m_scm_uri_isSet) {
        obj.insert(QString("scmUri"), ::OpenAPI::toJsonValue(m_scm_uri));
    }
    return obj;
}

QString OAIGetPublishingUser_200_response_properties::getPublishingPassword() const {
    return m_publishing_password;
}
void OAIGetPublishingUser_200_response_properties::setPublishingPassword(const QString &publishing_password) {
    m_publishing_password = publishing_password;
    m_publishing_password_isSet = true;
}

bool OAIGetPublishingUser_200_response_properties::is_publishing_password_Set() const{
    return m_publishing_password_isSet;
}

bool OAIGetPublishingUser_200_response_properties::is_publishing_password_Valid() const{
    return m_publishing_password_isValid;
}

QString OAIGetPublishingUser_200_response_properties::getPublishingPasswordHash() const {
    return m_publishing_password_hash;
}
void OAIGetPublishingUser_200_response_properties::setPublishingPasswordHash(const QString &publishing_password_hash) {
    m_publishing_password_hash = publishing_password_hash;
    m_publishing_password_hash_isSet = true;
}

bool OAIGetPublishingUser_200_response_properties::is_publishing_password_hash_Set() const{
    return m_publishing_password_hash_isSet;
}

bool OAIGetPublishingUser_200_response_properties::is_publishing_password_hash_Valid() const{
    return m_publishing_password_hash_isValid;
}

QString OAIGetPublishingUser_200_response_properties::getPublishingPasswordHashSalt() const {
    return m_publishing_password_hash_salt;
}
void OAIGetPublishingUser_200_response_properties::setPublishingPasswordHashSalt(const QString &publishing_password_hash_salt) {
    m_publishing_password_hash_salt = publishing_password_hash_salt;
    m_publishing_password_hash_salt_isSet = true;
}

bool OAIGetPublishingUser_200_response_properties::is_publishing_password_hash_salt_Set() const{
    return m_publishing_password_hash_salt_isSet;
}

bool OAIGetPublishingUser_200_response_properties::is_publishing_password_hash_salt_Valid() const{
    return m_publishing_password_hash_salt_isValid;
}

QString OAIGetPublishingUser_200_response_properties::getPublishingUserName() const {
    return m_publishing_user_name;
}
void OAIGetPublishingUser_200_response_properties::setPublishingUserName(const QString &publishing_user_name) {
    m_publishing_user_name = publishing_user_name;
    m_publishing_user_name_isSet = true;
}

bool OAIGetPublishingUser_200_response_properties::is_publishing_user_name_Set() const{
    return m_publishing_user_name_isSet;
}

bool OAIGetPublishingUser_200_response_properties::is_publishing_user_name_Valid() const{
    return m_publishing_user_name_isValid;
}

QString OAIGetPublishingUser_200_response_properties::getScmUri() const {
    return m_scm_uri;
}
void OAIGetPublishingUser_200_response_properties::setScmUri(const QString &scm_uri) {
    m_scm_uri = scm_uri;
    m_scm_uri_isSet = true;
}

bool OAIGetPublishingUser_200_response_properties::is_scm_uri_Set() const{
    return m_scm_uri_isSet;
}

bool OAIGetPublishingUser_200_response_properties::is_scm_uri_Valid() const{
    return m_scm_uri_isValid;
}

bool OAIGetPublishingUser_200_response_properties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_publishing_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publishing_password_hash_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publishing_password_hash_salt_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publishing_user_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scm_uri_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetPublishingUser_200_response_properties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_publishing_user_name_isValid && true;
}

} // namespace OpenAPI
