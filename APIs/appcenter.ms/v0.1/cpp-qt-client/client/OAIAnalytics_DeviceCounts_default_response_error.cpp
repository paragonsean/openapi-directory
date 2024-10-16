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

#include "OAIAnalytics_DeviceCounts_default_response_error.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAnalytics_DeviceCounts_default_response_error::OAIAnalytics_DeviceCounts_default_response_error(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAnalytics_DeviceCounts_default_response_error::OAIAnalytics_DeviceCounts_default_response_error() {
    this->initializeModel();
}

OAIAnalytics_DeviceCounts_default_response_error::~OAIAnalytics_DeviceCounts_default_response_error() {}

void OAIAnalytics_DeviceCounts_default_response_error::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAIAnalytics_DeviceCounts_default_response_error::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAnalytics_DeviceCounts_default_response_error::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAIAnalytics_DeviceCounts_default_response_error::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAnalytics_DeviceCounts_default_response_error::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

qint32 OAIAnalytics_DeviceCounts_default_response_error::getCode() const {
    return m_code;
}
void OAIAnalytics_DeviceCounts_default_response_error::setCode(const qint32 &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIAnalytics_DeviceCounts_default_response_error::is_code_Set() const{
    return m_code_isSet;
}

bool OAIAnalytics_DeviceCounts_default_response_error::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIAnalytics_DeviceCounts_default_response_error::getMessage() const {
    return m_message;
}
void OAIAnalytics_DeviceCounts_default_response_error::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIAnalytics_DeviceCounts_default_response_error::is_message_Set() const{
    return m_message_isSet;
}

bool OAIAnalytics_DeviceCounts_default_response_error::is_message_Valid() const{
    return m_message_isValid;
}

bool OAIAnalytics_DeviceCounts_default_response_error::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
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

bool OAIAnalytics_DeviceCounts_default_response_error::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
