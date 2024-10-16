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

#include "OAIAppleMultifactorLoginResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppleMultifactorLoginResponse::OAIAppleMultifactorLoginResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppleMultifactorLoginResponse::OAIAppleMultifactorLoginResponse() {
    this->initializeModel();
}

OAIAppleMultifactorLoginResponse::~OAIAppleMultifactorLoginResponse() {}

void OAIAppleMultifactorLoginResponse::initializeModel() {

    m_cookie_isSet = false;
    m_cookie_isValid = false;

    m_expires_isSet = false;
    m_expires_isValid = false;

    m_username_isSet = false;
    m_username_isValid = false;
}

void OAIAppleMultifactorLoginResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppleMultifactorLoginResponse::fromJsonObject(QJsonObject json) {

    m_cookie_isValid = ::OpenAPI::fromJsonValue(m_cookie, json[QString("cookie")]);
    m_cookie_isSet = !json[QString("cookie")].isNull() && m_cookie_isValid;

    m_expires_isValid = ::OpenAPI::fromJsonValue(m_expires, json[QString("expires")]);
    m_expires_isSet = !json[QString("expires")].isNull() && m_expires_isValid;

    m_username_isValid = ::OpenAPI::fromJsonValue(m_username, json[QString("username")]);
    m_username_isSet = !json[QString("username")].isNull() && m_username_isValid;
}

QString OAIAppleMultifactorLoginResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppleMultifactorLoginResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_cookie_isSet) {
        obj.insert(QString("cookie"), ::OpenAPI::toJsonValue(m_cookie));
    }
    if (m_expires_isSet) {
        obj.insert(QString("expires"), ::OpenAPI::toJsonValue(m_expires));
    }
    if (m_username_isSet) {
        obj.insert(QString("username"), ::OpenAPI::toJsonValue(m_username));
    }
    return obj;
}

QString OAIAppleMultifactorLoginResponse::getCookie() const {
    return m_cookie;
}
void OAIAppleMultifactorLoginResponse::setCookie(const QString &cookie) {
    m_cookie = cookie;
    m_cookie_isSet = true;
}

bool OAIAppleMultifactorLoginResponse::is_cookie_Set() const{
    return m_cookie_isSet;
}

bool OAIAppleMultifactorLoginResponse::is_cookie_Valid() const{
    return m_cookie_isValid;
}

QString OAIAppleMultifactorLoginResponse::getExpires() const {
    return m_expires;
}
void OAIAppleMultifactorLoginResponse::setExpires(const QString &expires) {
    m_expires = expires;
    m_expires_isSet = true;
}

bool OAIAppleMultifactorLoginResponse::is_expires_Set() const{
    return m_expires_isSet;
}

bool OAIAppleMultifactorLoginResponse::is_expires_Valid() const{
    return m_expires_isValid;
}

QString OAIAppleMultifactorLoginResponse::getUsername() const {
    return m_username;
}
void OAIAppleMultifactorLoginResponse::setUsername(const QString &username) {
    m_username = username;
    m_username_isSet = true;
}

bool OAIAppleMultifactorLoginResponse::is_username_Set() const{
    return m_username_isSet;
}

bool OAIAppleMultifactorLoginResponse::is_username_Valid() const{
    return m_username_isValid;
}

bool OAIAppleMultifactorLoginResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_cookie_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expires_isSet) {
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

bool OAIAppleMultifactorLoginResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
