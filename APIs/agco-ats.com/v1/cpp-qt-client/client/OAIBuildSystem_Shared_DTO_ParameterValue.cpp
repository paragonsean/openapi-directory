/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBuildSystem_Shared_DTO_ParameterValue.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBuildSystem_Shared_DTO_ParameterValue::OAIBuildSystem_Shared_DTO_ParameterValue(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBuildSystem_Shared_DTO_ParameterValue::OAIBuildSystem_Shared_DTO_ParameterValue() {
    this->initializeModel();
}

OAIBuildSystem_Shared_DTO_ParameterValue::~OAIBuildSystem_Shared_DTO_ParameterValue() {}

void OAIBuildSystem_Shared_DTO_ParameterValue::initializeModel() {

    m_direction_isSet = false;
    m_direction_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIBuildSystem_Shared_DTO_ParameterValue::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBuildSystem_Shared_DTO_ParameterValue::fromJsonObject(QJsonObject json) {

    m_direction_isValid = ::OpenAPI::fromJsonValue(m_direction, json[QString("Direction")]);
    m_direction_isSet = !json[QString("Direction")].isNull() && m_direction_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("Value")]);
    m_value_isSet = !json[QString("Value")].isNull() && m_value_isValid;
}

QString OAIBuildSystem_Shared_DTO_ParameterValue::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBuildSystem_Shared_DTO_ParameterValue::asJsonObject() const {
    QJsonObject obj;
    if (m_direction_isSet) {
        obj.insert(QString("Direction"), ::OpenAPI::toJsonValue(m_direction));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_value_isSet) {
        obj.insert(QString("Value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIBuildSystem_Shared_DTO_ParameterValue::getDirection() const {
    return m_direction;
}
void OAIBuildSystem_Shared_DTO_ParameterValue::setDirection(const QString &direction) {
    m_direction = direction;
    m_direction_isSet = true;
}

bool OAIBuildSystem_Shared_DTO_ParameterValue::is_direction_Set() const{
    return m_direction_isSet;
}

bool OAIBuildSystem_Shared_DTO_ParameterValue::is_direction_Valid() const{
    return m_direction_isValid;
}

QString OAIBuildSystem_Shared_DTO_ParameterValue::getName() const {
    return m_name;
}
void OAIBuildSystem_Shared_DTO_ParameterValue::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBuildSystem_Shared_DTO_ParameterValue::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBuildSystem_Shared_DTO_ParameterValue::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIBuildSystem_Shared_DTO_ParameterValue::getValue() const {
    return m_value;
}
void OAIBuildSystem_Shared_DTO_ParameterValue::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIBuildSystem_Shared_DTO_ParameterValue::is_value_Set() const{
    return m_value_isSet;
}

bool OAIBuildSystem_Shared_DTO_ParameterValue::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIBuildSystem_Shared_DTO_ParameterValue::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_direction_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

bool OAIBuildSystem_Shared_DTO_ParameterValue::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
