/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResetPasswordUsingTokenRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResetPasswordUsingTokenRequest::OAIResetPasswordUsingTokenRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResetPasswordUsingTokenRequest::OAIResetPasswordUsingTokenRequest() {
    this->initializeModel();
}

OAIResetPasswordUsingTokenRequest::~OAIResetPasswordUsingTokenRequest() {}

void OAIResetPasswordUsingTokenRequest::initializeModel() {

    m_new_password_isSet = false;
    m_new_password_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;
}

void OAIResetPasswordUsingTokenRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResetPasswordUsingTokenRequest::fromJsonObject(QJsonObject json) {

    m_new_password_isValid = ::OpenAPI::fromJsonValue(m_new_password, json[QString("new_password")]);
    m_new_password_isSet = !json[QString("new_password")].isNull() && m_new_password_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;
}

QString OAIResetPasswordUsingTokenRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResetPasswordUsingTokenRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_new_password_isSet) {
        obj.insert(QString("new_password"), ::OpenAPI::toJsonValue(m_new_password));
    }
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    return obj;
}

QString OAIResetPasswordUsingTokenRequest::getNewPassword() const {
    return m_new_password;
}
void OAIResetPasswordUsingTokenRequest::setNewPassword(const QString &new_password) {
    m_new_password = new_password;
    m_new_password_isSet = true;
}

bool OAIResetPasswordUsingTokenRequest::is_new_password_Set() const{
    return m_new_password_isSet;
}

bool OAIResetPasswordUsingTokenRequest::is_new_password_Valid() const{
    return m_new_password_isValid;
}

QString OAIResetPasswordUsingTokenRequest::getToken() const {
    return m_token;
}
void OAIResetPasswordUsingTokenRequest::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIResetPasswordUsingTokenRequest::is_token_Set() const{
    return m_token_isSet;
}

bool OAIResetPasswordUsingTokenRequest::is_token_Valid() const{
    return m_token_isValid;
}

bool OAIResetPasswordUsingTokenRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_new_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResetPasswordUsingTokenRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_new_password_isValid && m_token_isValid && true;
}

} // namespace OpenAPI
