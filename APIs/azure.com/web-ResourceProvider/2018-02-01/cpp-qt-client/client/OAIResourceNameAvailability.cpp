/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResourceNameAvailability.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResourceNameAvailability::OAIResourceNameAvailability(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResourceNameAvailability::OAIResourceNameAvailability() {
    this->initializeModel();
}

OAIResourceNameAvailability::~OAIResourceNameAvailability() {}

void OAIResourceNameAvailability::initializeModel() {

    m_message_isSet = false;
    m_message_isValid = false;

    m_name_available_isSet = false;
    m_name_available_isValid = false;

    m_reason_isSet = false;
    m_reason_isValid = false;
}

void OAIResourceNameAvailability::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResourceNameAvailability::fromJsonObject(QJsonObject json) {

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_name_available_isValid = ::OpenAPI::fromJsonValue(m_name_available, json[QString("nameAvailable")]);
    m_name_available_isSet = !json[QString("nameAvailable")].isNull() && m_name_available_isValid;

    m_reason_isValid = ::OpenAPI::fromJsonValue(m_reason, json[QString("reason")]);
    m_reason_isSet = !json[QString("reason")].isNull() && m_reason_isValid;
}

QString OAIResourceNameAvailability::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResourceNameAvailability::asJsonObject() const {
    QJsonObject obj;
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_name_available_isSet) {
        obj.insert(QString("nameAvailable"), ::OpenAPI::toJsonValue(m_name_available));
    }
    if (m_reason_isSet) {
        obj.insert(QString("reason"), ::OpenAPI::toJsonValue(m_reason));
    }
    return obj;
}

QString OAIResourceNameAvailability::getMessage() const {
    return m_message;
}
void OAIResourceNameAvailability::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIResourceNameAvailability::is_message_Set() const{
    return m_message_isSet;
}

bool OAIResourceNameAvailability::is_message_Valid() const{
    return m_message_isValid;
}

bool OAIResourceNameAvailability::isNameAvailable() const {
    return m_name_available;
}
void OAIResourceNameAvailability::setNameAvailable(const bool &name_available) {
    m_name_available = name_available;
    m_name_available_isSet = true;
}

bool OAIResourceNameAvailability::is_name_available_Set() const{
    return m_name_available_isSet;
}

bool OAIResourceNameAvailability::is_name_available_Valid() const{
    return m_name_available_isValid;
}

QString OAIResourceNameAvailability::getReason() const {
    return m_reason;
}
void OAIResourceNameAvailability::setReason(const QString &reason) {
    m_reason = reason;
    m_reason_isSet = true;
}

bool OAIResourceNameAvailability::is_reason_Set() const{
    return m_reason_isSet;
}

bool OAIResourceNameAvailability::is_reason_Valid() const{
    return m_reason_isValid;
}

bool OAIResourceNameAvailability::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reason_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResourceNameAvailability::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
