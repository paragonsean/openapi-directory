/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI_oauth_token_post_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_oauth_token_post_200_response::OAI_oauth_token_post_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_oauth_token_post_200_response::OAI_oauth_token_post_200_response() {
    this->initializeModel();
}

OAI_oauth_token_post_200_response::~OAI_oauth_token_post_200_response() {}

void OAI_oauth_token_post_200_response::initializeModel() {

    m_access_token_isSet = false;
    m_access_token_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_scope_isSet = false;
    m_scope_isValid = false;

    m_token_type_isSet = false;
    m_token_type_isValid = false;
}

void OAI_oauth_token_post_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_oauth_token_post_200_response::fromJsonObject(QJsonObject json) {

    m_access_token_isValid = ::OpenAPI::fromJsonValue(m_access_token, json[QString("access_token")]);
    m_access_token_isSet = !json[QString("access_token")].isNull() && m_access_token_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_scope_isValid = ::OpenAPI::fromJsonValue(m_scope, json[QString("scope")]);
    m_scope_isSet = !json[QString("scope")].isNull() && m_scope_isValid;

    m_token_type_isValid = ::OpenAPI::fromJsonValue(m_token_type, json[QString("token_type")]);
    m_token_type_isSet = !json[QString("token_type")].isNull() && m_token_type_isValid;
}

QString OAI_oauth_token_post_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_oauth_token_post_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_access_token_isSet) {
        obj.insert(QString("access_token"), ::OpenAPI::toJsonValue(m_access_token));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_scope_isSet) {
        obj.insert(QString("scope"), ::OpenAPI::toJsonValue(m_scope));
    }
    if (m_token_type_isSet) {
        obj.insert(QString("token_type"), ::OpenAPI::toJsonValue(m_token_type));
    }
    return obj;
}

QString OAI_oauth_token_post_200_response::getAccessToken() const {
    return m_access_token;
}
void OAI_oauth_token_post_200_response::setAccessToken(const QString &access_token) {
    m_access_token = access_token;
    m_access_token_isSet = true;
}

bool OAI_oauth_token_post_200_response::is_access_token_Set() const{
    return m_access_token_isSet;
}

bool OAI_oauth_token_post_200_response::is_access_token_Valid() const{
    return m_access_token_isValid;
}

qint32 OAI_oauth_token_post_200_response::getCreatedAt() const {
    return m_created_at;
}
void OAI_oauth_token_post_200_response::setCreatedAt(const qint32 &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAI_oauth_token_post_200_response::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAI_oauth_token_post_200_response::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAI_oauth_token_post_200_response::getScope() const {
    return m_scope;
}
void OAI_oauth_token_post_200_response::setScope(const QString &scope) {
    m_scope = scope;
    m_scope_isSet = true;
}

bool OAI_oauth_token_post_200_response::is_scope_Set() const{
    return m_scope_isSet;
}

bool OAI_oauth_token_post_200_response::is_scope_Valid() const{
    return m_scope_isValid;
}

QString OAI_oauth_token_post_200_response::getTokenType() const {
    return m_token_type;
}
void OAI_oauth_token_post_200_response::setTokenType(const QString &token_type) {
    m_token_type = token_type;
    m_token_type_isSet = true;
}

bool OAI_oauth_token_post_200_response::is_token_type_Set() const{
    return m_token_type_isSet;
}

bool OAI_oauth_token_post_200_response::is_token_type_Valid() const{
    return m_token_type_isValid;
}

bool OAI_oauth_token_post_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_access_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scope_isSet) {
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

bool OAI_oauth_token_post_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
