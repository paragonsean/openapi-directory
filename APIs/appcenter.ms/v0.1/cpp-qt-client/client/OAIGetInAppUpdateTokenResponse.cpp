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

#include "OAIGetInAppUpdateTokenResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetInAppUpdateTokenResponse::OAIGetInAppUpdateTokenResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetInAppUpdateTokenResponse::OAIGetInAppUpdateTokenResponse() {
    this->initializeModel();
}

OAIGetInAppUpdateTokenResponse::~OAIGetInAppUpdateTokenResponse() {}

void OAIGetInAppUpdateTokenResponse::initializeModel() {

    m_token_isSet = false;
    m_token_isValid = false;
}

void OAIGetInAppUpdateTokenResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetInAppUpdateTokenResponse::fromJsonObject(QJsonObject json) {

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;
}

QString OAIGetInAppUpdateTokenResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetInAppUpdateTokenResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    return obj;
}

QString OAIGetInAppUpdateTokenResponse::getToken() const {
    return m_token;
}
void OAIGetInAppUpdateTokenResponse::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIGetInAppUpdateTokenResponse::is_token_Set() const{
    return m_token_isSet;
}

bool OAIGetInAppUpdateTokenResponse::is_token_Valid() const{
    return m_token_isValid;
}

bool OAIGetInAppUpdateTokenResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetInAppUpdateTokenResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_token_isValid && true;
}

} // namespace OpenAPI
