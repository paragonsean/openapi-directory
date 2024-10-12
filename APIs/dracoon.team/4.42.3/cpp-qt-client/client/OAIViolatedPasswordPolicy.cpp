/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIViolatedPasswordPolicy.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIViolatedPasswordPolicy::OAIViolatedPasswordPolicy(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIViolatedPasswordPolicy::OAIViolatedPasswordPolicy() {
    this->initializeModel();
}

OAIViolatedPasswordPolicy::~OAIViolatedPasswordPolicy() {}

void OAIViolatedPasswordPolicy::initializeModel() {

    m_message_isSet = false;
    m_message_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIViolatedPasswordPolicy::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIViolatedPasswordPolicy::fromJsonObject(QJsonObject json) {

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIViolatedPasswordPolicy::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIViolatedPasswordPolicy::asJsonObject() const {
    QJsonObject obj;
    if (m_message_isSet) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIViolatedPasswordPolicy::getMessage() const {
    return m_message;
}
void OAIViolatedPasswordPolicy::setMessage(const QString &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIViolatedPasswordPolicy::is_message_Set() const{
    return m_message_isSet;
}

bool OAIViolatedPasswordPolicy::is_message_Valid() const{
    return m_message_isValid;
}

QString OAIViolatedPasswordPolicy::getName() const {
    return m_name;
}
void OAIViolatedPasswordPolicy::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIViolatedPasswordPolicy::is_name_Set() const{
    return m_name_isSet;
}

bool OAIViolatedPasswordPolicy::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIViolatedPasswordPolicy::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIViolatedPasswordPolicy::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
