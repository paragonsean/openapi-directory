/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISessionRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISessionRequest::OAISessionRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISessionRequest::OAISessionRequest() {
    this->initializeModel();
}

OAISessionRequest::~OAISessionRequest() {}

void OAISessionRequest::initializeModel() {

    m_client_id_isSet = false;
    m_client_id_isValid = false;

    m_client_secret_isSet = false;
    m_client_secret_isValid = false;

    m_grant_type_isSet = false;
    m_grant_type_isValid = false;

    m_refresh_token_isSet = false;
    m_refresh_token_isValid = false;
}

void OAISessionRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISessionRequest::fromJsonObject(QJsonObject json) {

    m_client_id_isValid = ::OpenAPI::fromJsonValue(m_client_id, json[QString("clientId")]);
    m_client_id_isSet = !json[QString("clientId")].isNull() && m_client_id_isValid;

    m_client_secret_isValid = ::OpenAPI::fromJsonValue(m_client_secret, json[QString("clientSecret")]);
    m_client_secret_isSet = !json[QString("clientSecret")].isNull() && m_client_secret_isValid;

    m_grant_type_isValid = ::OpenAPI::fromJsonValue(m_grant_type, json[QString("grantType")]);
    m_grant_type_isSet = !json[QString("grantType")].isNull() && m_grant_type_isValid;

    m_refresh_token_isValid = ::OpenAPI::fromJsonValue(m_refresh_token, json[QString("refreshToken")]);
    m_refresh_token_isSet = !json[QString("refreshToken")].isNull() && m_refresh_token_isValid;
}

QString OAISessionRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISessionRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_client_id_isSet) {
        obj.insert(QString("clientId"), ::OpenAPI::toJsonValue(m_client_id));
    }
    if (m_client_secret_isSet) {
        obj.insert(QString("clientSecret"), ::OpenAPI::toJsonValue(m_client_secret));
    }
    if (m_grant_type_isSet) {
        obj.insert(QString("grantType"), ::OpenAPI::toJsonValue(m_grant_type));
    }
    if (m_refresh_token_isSet) {
        obj.insert(QString("refreshToken"), ::OpenAPI::toJsonValue(m_refresh_token));
    }
    return obj;
}

QString OAISessionRequest::getClientId() const {
    return m_client_id;
}
void OAISessionRequest::setClientId(const QString &client_id) {
    m_client_id = client_id;
    m_client_id_isSet = true;
}

bool OAISessionRequest::is_client_id_Set() const{
    return m_client_id_isSet;
}

bool OAISessionRequest::is_client_id_Valid() const{
    return m_client_id_isValid;
}

QString OAISessionRequest::getClientSecret() const {
    return m_client_secret;
}
void OAISessionRequest::setClientSecret(const QString &client_secret) {
    m_client_secret = client_secret;
    m_client_secret_isSet = true;
}

bool OAISessionRequest::is_client_secret_Set() const{
    return m_client_secret_isSet;
}

bool OAISessionRequest::is_client_secret_Valid() const{
    return m_client_secret_isValid;
}

QString OAISessionRequest::getGrantType() const {
    return m_grant_type;
}
void OAISessionRequest::setGrantType(const QString &grant_type) {
    m_grant_type = grant_type;
    m_grant_type_isSet = true;
}

bool OAISessionRequest::is_grant_type_Set() const{
    return m_grant_type_isSet;
}

bool OAISessionRequest::is_grant_type_Valid() const{
    return m_grant_type_isValid;
}

QString OAISessionRequest::getRefreshToken() const {
    return m_refresh_token;
}
void OAISessionRequest::setRefreshToken(const QString &refresh_token) {
    m_refresh_token = refresh_token;
    m_refresh_token_isSet = true;
}

bool OAISessionRequest::is_refresh_token_Set() const{
    return m_refresh_token_isSet;
}

bool OAISessionRequest::is_refresh_token_Valid() const{
    return m_refresh_token_isValid;
}

bool OAISessionRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_secret_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_grant_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_refresh_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISessionRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_client_id_isValid && m_client_secret_isValid && m_grant_type_isValid && true;
}

} // namespace OpenAPI
