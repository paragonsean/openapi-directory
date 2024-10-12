/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIValidateTokenRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIValidateTokenRequest::OAIValidateTokenRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIValidateTokenRequest::OAIValidateTokenRequest() {
    this->initializeModel();
}

OAIValidateTokenRequest::~OAIValidateTokenRequest() {}

void OAIValidateTokenRequest::initializeModel() {

    m_auth_token_isSet = false;
    m_auth_token_isValid = false;
}

void OAIValidateTokenRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIValidateTokenRequest::fromJsonObject(QJsonObject json) {

    m_auth_token_isValid = ::OpenAPI::fromJsonValue(m_auth_token, json[QString("authToken")]);
    m_auth_token_isSet = !json[QString("authToken")].isNull() && m_auth_token_isValid;
}

QString OAIValidateTokenRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIValidateTokenRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_auth_token_isSet) {
        obj.insert(QString("authToken"), ::OpenAPI::toJsonValue(m_auth_token));
    }
    return obj;
}

QString OAIValidateTokenRequest::getAuthToken() const {
    return m_auth_token;
}
void OAIValidateTokenRequest::setAuthToken(const QString &auth_token) {
    m_auth_token = auth_token;
    m_auth_token_isSet = true;
}

bool OAIValidateTokenRequest::is_auth_token_Set() const{
    return m_auth_token_isSet;
}

bool OAIValidateTokenRequest::is_auth_token_Valid() const{
    return m_auth_token_isValid;
}

bool OAIValidateTokenRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_auth_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIValidateTokenRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
