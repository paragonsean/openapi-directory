/**
 * Authentication
 * Personio Authentication API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAuthenticationTokenResponse_allOf_data.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuthenticationTokenResponse_allOf_data::OAIAuthenticationTokenResponse_allOf_data(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuthenticationTokenResponse_allOf_data::OAIAuthenticationTokenResponse_allOf_data() {
    this->initializeModel();
}

OAIAuthenticationTokenResponse_allOf_data::~OAIAuthenticationTokenResponse_allOf_data() {}

void OAIAuthenticationTokenResponse_allOf_data::initializeModel() {

    m_token_isSet = false;
    m_token_isValid = false;
}

void OAIAuthenticationTokenResponse_allOf_data::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAuthenticationTokenResponse_allOf_data::fromJsonObject(QJsonObject json) {

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;
}

QString OAIAuthenticationTokenResponse_allOf_data::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAuthenticationTokenResponse_allOf_data::asJsonObject() const {
    QJsonObject obj;
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    return obj;
}

QString OAIAuthenticationTokenResponse_allOf_data::getToken() const {
    return m_token;
}
void OAIAuthenticationTokenResponse_allOf_data::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIAuthenticationTokenResponse_allOf_data::is_token_Set() const{
    return m_token_isSet;
}

bool OAIAuthenticationTokenResponse_allOf_data::is_token_Valid() const{
    return m_token_isValid;
}

bool OAIAuthenticationTokenResponse_allOf_data::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAuthenticationTokenResponse_allOf_data::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_token_isValid && true;
}

} // namespace OpenAPI
