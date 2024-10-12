/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAuthInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuthInfo::OAIAuthInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuthInfo::OAIAuthInfo() {
    this->initializeModel();
}

OAIAuthInfo::~OAIAuthInfo() {}

void OAIAuthInfo::initializeModel() {

    m_expires_in_isSet = false;
    m_expires_in_isValid = false;

    m_refresh_token_isSet = false;
    m_refresh_token_isValid = false;

    m_scope_isSet = false;
    m_scope_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;

    m_token_type_isSet = false;
    m_token_type_isValid = false;
}

void OAIAuthInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAuthInfo::fromJsonObject(QJsonObject json) {

    m_expires_in_isValid = ::OpenAPI::fromJsonValue(m_expires_in, json[QString("expiresIn")]);
    m_expires_in_isSet = !json[QString("expiresIn")].isNull() && m_expires_in_isValid;

    m_refresh_token_isValid = ::OpenAPI::fromJsonValue(m_refresh_token, json[QString("refreshToken")]);
    m_refresh_token_isSet = !json[QString("refreshToken")].isNull() && m_refresh_token_isValid;

    m_scope_isValid = ::OpenAPI::fromJsonValue(m_scope, json[QString("scope")]);
    m_scope_isSet = !json[QString("scope")].isNull() && m_scope_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;

    m_token_type_isValid = ::OpenAPI::fromJsonValue(m_token_type, json[QString("tokenType")]);
    m_token_type_isSet = !json[QString("tokenType")].isNull() && m_token_type_isValid;
}

QString OAIAuthInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAuthInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_expires_in_isSet) {
        obj.insert(QString("expiresIn"), ::OpenAPI::toJsonValue(m_expires_in));
    }
    if (m_refresh_token_isSet) {
        obj.insert(QString("refreshToken"), ::OpenAPI::toJsonValue(m_refresh_token));
    }
    if (m_scope_isSet) {
        obj.insert(QString("scope"), ::OpenAPI::toJsonValue(m_scope));
    }
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    if (m_token_type_isSet) {
        obj.insert(QString("tokenType"), ::OpenAPI::toJsonValue(m_token_type));
    }
    return obj;
}

qint32 OAIAuthInfo::getExpiresIn() const {
    return m_expires_in;
}
void OAIAuthInfo::setExpiresIn(const qint32 &expires_in) {
    m_expires_in = expires_in;
    m_expires_in_isSet = true;
}

bool OAIAuthInfo::is_expires_in_Set() const{
    return m_expires_in_isSet;
}

bool OAIAuthInfo::is_expires_in_Valid() const{
    return m_expires_in_isValid;
}

QString OAIAuthInfo::getRefreshToken() const {
    return m_refresh_token;
}
void OAIAuthInfo::setRefreshToken(const QString &refresh_token) {
    m_refresh_token = refresh_token;
    m_refresh_token_isSet = true;
}

bool OAIAuthInfo::is_refresh_token_Set() const{
    return m_refresh_token_isSet;
}

bool OAIAuthInfo::is_refresh_token_Valid() const{
    return m_refresh_token_isValid;
}

QString OAIAuthInfo::getScope() const {
    return m_scope;
}
void OAIAuthInfo::setScope(const QString &scope) {
    m_scope = scope;
    m_scope_isSet = true;
}

bool OAIAuthInfo::is_scope_Set() const{
    return m_scope_isSet;
}

bool OAIAuthInfo::is_scope_Valid() const{
    return m_scope_isValid;
}

QString OAIAuthInfo::getToken() const {
    return m_token;
}
void OAIAuthInfo::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIAuthInfo::is_token_Set() const{
    return m_token_isSet;
}

bool OAIAuthInfo::is_token_Valid() const{
    return m_token_isValid;
}

QString OAIAuthInfo::getTokenType() const {
    return m_token_type;
}
void OAIAuthInfo::setTokenType(const QString &token_type) {
    m_token_type = token_type;
    m_token_type_isSet = true;
}

bool OAIAuthInfo::is_token_type_Set() const{
    return m_token_type_isSet;
}

bool OAIAuthInfo::is_token_type_Valid() const{
    return m_token_type_isValid;
}

bool OAIAuthInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_expires_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_refresh_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scope_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAuthInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_token_isValid && m_token_type_isValid && true;
}

} // namespace OpenAPI
