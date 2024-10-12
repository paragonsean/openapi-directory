/**
 * import.io
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAPIError.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAPIError::OAIAPIError(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAPIError::OAIAPIError() {
    this->initializeModel();
}

OAIAPIError::~OAIAPIError() {}

void OAIAPIError::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAIAPIError::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAPIError::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAIAPIError::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAPIError::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_error_isSet) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

qint32 OAIAPIError::getCode() const {
    return m_code;
}
void OAIAPIError::setCode(const qint32 &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIAPIError::is_code_Set() const{
    return m_code_isSet;
}

bool OAIAPIError::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIAPIError::getError() const {
    return m_error;
}
void OAIAPIError::setError(const QString &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIAPIError::is_error_Set() const{
    return m_error_isSet;
}

bool OAIAPIError::is_error_Valid() const{
    return m_error_isValid;
}

QString OAIAPIError::getMessage() const {
    return m_message;
}
void OAIAPIError::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIAPIError::is_message_Set() const{
    return m_message_isSet;
}

bool OAIAPIError::is_message_Valid() const{
    return m_message_isValid;
}

bool OAIAPIError::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_isSet) {
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

bool OAIAPIError::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
