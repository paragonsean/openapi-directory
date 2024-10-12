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

#include "OAIChangeUserPasswordRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIChangeUserPasswordRequest::OAIChangeUserPasswordRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIChangeUserPasswordRequest::OAIChangeUserPasswordRequest() {
    this->initializeModel();
}

OAIChangeUserPasswordRequest::~OAIChangeUserPasswordRequest() {}

void OAIChangeUserPasswordRequest::initializeModel() {

    m_new_password_isSet = false;
    m_new_password_isValid = false;

    m_old_password_isSet = false;
    m_old_password_isValid = false;
}

void OAIChangeUserPasswordRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIChangeUserPasswordRequest::fromJsonObject(QJsonObject json) {

    m_new_password_isValid = ::OpenAPI::fromJsonValue(m_new_password, json[QString("newPassword")]);
    m_new_password_isSet = !json[QString("newPassword")].isNull() && m_new_password_isValid;

    m_old_password_isValid = ::OpenAPI::fromJsonValue(m_old_password, json[QString("oldPassword")]);
    m_old_password_isSet = !json[QString("oldPassword")].isNull() && m_old_password_isValid;
}

QString OAIChangeUserPasswordRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIChangeUserPasswordRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_new_password_isSet) {
        obj.insert(QString("newPassword"), ::OpenAPI::toJsonValue(m_new_password));
    }
    if (m_old_password_isSet) {
        obj.insert(QString("oldPassword"), ::OpenAPI::toJsonValue(m_old_password));
    }
    return obj;
}

QString OAIChangeUserPasswordRequest::getNewPassword() const {
    return m_new_password;
}
void OAIChangeUserPasswordRequest::setNewPassword(const QString &new_password) {
    m_new_password = new_password;
    m_new_password_isSet = true;
}

bool OAIChangeUserPasswordRequest::is_new_password_Set() const{
    return m_new_password_isSet;
}

bool OAIChangeUserPasswordRequest::is_new_password_Valid() const{
    return m_new_password_isValid;
}

QString OAIChangeUserPasswordRequest::getOldPassword() const {
    return m_old_password;
}
void OAIChangeUserPasswordRequest::setOldPassword(const QString &old_password) {
    m_old_password = old_password;
    m_old_password_isSet = true;
}

bool OAIChangeUserPasswordRequest::is_old_password_Set() const{
    return m_old_password_isSet;
}

bool OAIChangeUserPasswordRequest::is_old_password_Valid() const{
    return m_old_password_isValid;
}

bool OAIChangeUserPasswordRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_new_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_old_password_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIChangeUserPasswordRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_new_password_isValid && m_old_password_isValid && true;
}

} // namespace OpenAPI
