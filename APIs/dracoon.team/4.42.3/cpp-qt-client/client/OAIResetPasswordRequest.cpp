/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResetPasswordRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResetPasswordRequest::OAIResetPasswordRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResetPasswordRequest::OAIResetPasswordRequest() {
    this->initializeModel();
}

OAIResetPasswordRequest::~OAIResetPasswordRequest() {}

void OAIResetPasswordRequest::initializeModel() {

    m_creator_language_isSet = false;
    m_creator_language_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_login_isSet = false;
    m_login_isValid = false;

    m_user_name_isSet = false;
    m_user_name_isValid = false;
}

void OAIResetPasswordRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResetPasswordRequest::fromJsonObject(QJsonObject json) {

    m_creator_language_isValid = ::OpenAPI::fromJsonValue(m_creator_language, json[QString("creatorLanguage")]);
    m_creator_language_isSet = !json[QString("creatorLanguage")].isNull() && m_creator_language_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_login_isValid = ::OpenAPI::fromJsonValue(m_login, json[QString("login")]);
    m_login_isSet = !json[QString("login")].isNull() && m_login_isValid;

    m_user_name_isValid = ::OpenAPI::fromJsonValue(m_user_name, json[QString("userName")]);
    m_user_name_isSet = !json[QString("userName")].isNull() && m_user_name_isValid;
}

QString OAIResetPasswordRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResetPasswordRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_creator_language_isSet) {
        obj.insert(QString("creatorLanguage"), ::OpenAPI::toJsonValue(m_creator_language));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_login_isSet) {
        obj.insert(QString("login"), ::OpenAPI::toJsonValue(m_login));
    }
    if (m_user_name_isSet) {
        obj.insert(QString("userName"), ::OpenAPI::toJsonValue(m_user_name));
    }
    return obj;
}

QString OAIResetPasswordRequest::getCreatorLanguage() const {
    return m_creator_language;
}
void OAIResetPasswordRequest::setCreatorLanguage(const QString &creator_language) {
    m_creator_language = creator_language;
    m_creator_language_isSet = true;
}

bool OAIResetPasswordRequest::is_creator_language_Set() const{
    return m_creator_language_isSet;
}

bool OAIResetPasswordRequest::is_creator_language_Valid() const{
    return m_creator_language_isValid;
}

QString OAIResetPasswordRequest::getLanguage() const {
    return m_language;
}
void OAIResetPasswordRequest::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIResetPasswordRequest::is_language_Set() const{
    return m_language_isSet;
}

bool OAIResetPasswordRequest::is_language_Valid() const{
    return m_language_isValid;
}

QString OAIResetPasswordRequest::getLogin() const {
    return m_login;
}
void OAIResetPasswordRequest::setLogin(const QString &login) {
    m_login = login;
    m_login_isSet = true;
}

bool OAIResetPasswordRequest::is_login_Set() const{
    return m_login_isSet;
}

bool OAIResetPasswordRequest::is_login_Valid() const{
    return m_login_isValid;
}

QString OAIResetPasswordRequest::getUserName() const {
    return m_user_name;
}
void OAIResetPasswordRequest::setUserName(const QString &user_name) {
    m_user_name = user_name;
    m_user_name_isSet = true;
}

bool OAIResetPasswordRequest::is_user_name_Set() const{
    return m_user_name_isSet;
}

bool OAIResetPasswordRequest::is_user_name_Valid() const{
    return m_user_name_isValid;
}

bool OAIResetPasswordRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_creator_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_login_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResetPasswordRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
