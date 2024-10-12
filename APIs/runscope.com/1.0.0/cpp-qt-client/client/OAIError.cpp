/**
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIError.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIError::OAIError(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIError::OAIError() {
    this->initializeModel();
}

OAIError::~OAIError() {}

void OAIError::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_fields_isSet = false;
    m_fields_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAIError::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIError::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_fields_isValid = ::OpenAPI::fromJsonValue(m_fields, json[QString("fields")]);
    m_fields_isSet = !json[QString("fields")].isNull() && m_fields_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAIError::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIError::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_fields_isSet) {
        obj.insert(QString("fields"), ::OpenAPI::toJsonValue(m_fields));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

qint32 OAIError::getCode() const {
    return m_code;
}
void OAIError::setCode(const qint32 &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIError::is_code_Set() const{
    return m_code_isSet;
}

bool OAIError::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIError::getFields() const {
    return m_fields;
}
void OAIError::setFields(const QString &fields) {
    m_fields = fields;
    m_fields_isSet = true;
}

bool OAIError::is_fields_Set() const{
    return m_fields_isSet;
}

bool OAIError::is_fields_Valid() const{
    return m_fields_isValid;
}

QString OAIError::getMessage() const {
    return m_message;
}
void OAIError::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIError::is_message_Set() const{
    return m_message_isSet;
}

bool OAIError::is_message_Valid() const{
    return m_message_isValid;
}

bool OAIError::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fields_isSet) {
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

bool OAIError::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
