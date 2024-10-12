/**
 * AutomationManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2015-10-31
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDscNodeConfiguration_ListByAutomationAccount_default_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDscNodeConfiguration_ListByAutomationAccount_default_response::OAIDscNodeConfiguration_ListByAutomationAccount_default_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDscNodeConfiguration_ListByAutomationAccount_default_response::OAIDscNodeConfiguration_ListByAutomationAccount_default_response() {
    this->initializeModel();
}

OAIDscNodeConfiguration_ListByAutomationAccount_default_response::~OAIDscNodeConfiguration_ListByAutomationAccount_default_response() {}

void OAIDscNodeConfiguration_ListByAutomationAccount_default_response::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAIDscNodeConfiguration_ListByAutomationAccount_default_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDscNodeConfiguration_ListByAutomationAccount_default_response::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAIDscNodeConfiguration_ListByAutomationAccount_default_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDscNodeConfiguration_ListByAutomationAccount_default_response::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

QString OAIDscNodeConfiguration_ListByAutomationAccount_default_response::getCode() const {
    return m_code;
}
void OAIDscNodeConfiguration_ListByAutomationAccount_default_response::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIDscNodeConfiguration_ListByAutomationAccount_default_response::is_code_Set() const{
    return m_code_isSet;
}

bool OAIDscNodeConfiguration_ListByAutomationAccount_default_response::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIDscNodeConfiguration_ListByAutomationAccount_default_response::getMessage() const {
    return m_message;
}
void OAIDscNodeConfiguration_ListByAutomationAccount_default_response::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIDscNodeConfiguration_ListByAutomationAccount_default_response::is_message_Set() const{
    return m_message_isSet;
}

bool OAIDscNodeConfiguration_ListByAutomationAccount_default_response::is_message_Valid() const{
    return m_message_isValid;
}

bool OAIDscNodeConfiguration_ListByAutomationAccount_default_response::isSet() const {
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

bool OAIDscNodeConfiguration_ListByAutomationAccount_default_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
