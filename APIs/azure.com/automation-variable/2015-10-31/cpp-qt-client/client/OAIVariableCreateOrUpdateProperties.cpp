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

#include "OAIVariableCreateOrUpdateProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVariableCreateOrUpdateProperties::OAIVariableCreateOrUpdateProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVariableCreateOrUpdateProperties::OAIVariableCreateOrUpdateProperties() {
    this->initializeModel();
}

OAIVariableCreateOrUpdateProperties::~OAIVariableCreateOrUpdateProperties() {}

void OAIVariableCreateOrUpdateProperties::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_is_encrypted_isSet = false;
    m_is_encrypted_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIVariableCreateOrUpdateProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVariableCreateOrUpdateProperties::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_is_encrypted_isValid = ::OpenAPI::fromJsonValue(m_is_encrypted, json[QString("isEncrypted")]);
    m_is_encrypted_isSet = !json[QString("isEncrypted")].isNull() && m_is_encrypted_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIVariableCreateOrUpdateProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVariableCreateOrUpdateProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_is_encrypted_isSet) {
        obj.insert(QString("isEncrypted"), ::OpenAPI::toJsonValue(m_is_encrypted));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIVariableCreateOrUpdateProperties::getDescription() const {
    return m_description;
}
void OAIVariableCreateOrUpdateProperties::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIVariableCreateOrUpdateProperties::is_description_Set() const{
    return m_description_isSet;
}

bool OAIVariableCreateOrUpdateProperties::is_description_Valid() const{
    return m_description_isValid;
}

bool OAIVariableCreateOrUpdateProperties::isIsEncrypted() const {
    return m_is_encrypted;
}
void OAIVariableCreateOrUpdateProperties::setIsEncrypted(const bool &is_encrypted) {
    m_is_encrypted = is_encrypted;
    m_is_encrypted_isSet = true;
}

bool OAIVariableCreateOrUpdateProperties::is_is_encrypted_Set() const{
    return m_is_encrypted_isSet;
}

bool OAIVariableCreateOrUpdateProperties::is_is_encrypted_Valid() const{
    return m_is_encrypted_isValid;
}

QString OAIVariableCreateOrUpdateProperties::getValue() const {
    return m_value;
}
void OAIVariableCreateOrUpdateProperties::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIVariableCreateOrUpdateProperties::is_value_Set() const{
    return m_value_isSet;
}

bool OAIVariableCreateOrUpdateProperties::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIVariableCreateOrUpdateProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_encrypted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVariableCreateOrUpdateProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
