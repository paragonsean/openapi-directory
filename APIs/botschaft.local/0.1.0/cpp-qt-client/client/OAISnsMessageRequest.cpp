/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISnsMessageRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISnsMessageRequest::OAISnsMessageRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISnsMessageRequest::OAISnsMessageRequest() {
    this->initializeModel();
}

OAISnsMessageRequest::~OAISnsMessageRequest() {}

void OAISnsMessageRequest::initializeModel() {

    m_base64_message_isSet = false;
    m_base64_message_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAISnsMessageRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISnsMessageRequest::fromJsonObject(QJsonObject json) {

    m_base64_message_isValid = ::OpenAPI::fromJsonValue(m_base64_message, json[QString("base64_message")]);
    m_base64_message_isSet = !json[QString("base64_message")].isNull() && m_base64_message_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAISnsMessageRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISnsMessageRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_base64_message_isSet) {
        obj.insert(QString("base64_message"), ::OpenAPI::toJsonValue(m_base64_message));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

QString OAISnsMessageRequest::getBase64Message() const {
    return m_base64_message;
}
void OAISnsMessageRequest::setBase64Message(const QString &base64_message) {
    m_base64_message = base64_message;
    m_base64_message_isSet = true;
}

bool OAISnsMessageRequest::is_base64_message_Set() const{
    return m_base64_message_isSet;
}

bool OAISnsMessageRequest::is_base64_message_Valid() const{
    return m_base64_message_isValid;
}

QString OAISnsMessageRequest::getMessage() const {
    return m_message;
}
void OAISnsMessageRequest::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAISnsMessageRequest::is_message_Set() const{
    return m_message_isSet;
}

bool OAISnsMessageRequest::is_message_Valid() const{
    return m_message_isValid;
}

bool OAISnsMessageRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_base64_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISnsMessageRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
