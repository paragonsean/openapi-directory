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

#include "OAIBuildSystem_Shared_DTO_Parameter.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBuildSystem_Shared_DTO_Parameter::OAIBuildSystem_Shared_DTO_Parameter(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBuildSystem_Shared_DTO_Parameter::OAIBuildSystem_Shared_DTO_Parameter() {
    this->initializeModel();
}

OAIBuildSystem_Shared_DTO_Parameter::~OAIBuildSystem_Shared_DTO_Parameter() {}

void OAIBuildSystem_Shared_DTO_Parameter::initializeModel() {

    m_direction_isSet = false;
    m_direction_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIBuildSystem_Shared_DTO_Parameter::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBuildSystem_Shared_DTO_Parameter::fromJsonObject(QJsonObject json) {

    m_direction_isValid = ::OpenAPI::fromJsonValue(m_direction, json[QString("Direction")]);
    m_direction_isSet = !json[QString("Direction")].isNull() && m_direction_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("Type")]);
    m_type_isSet = !json[QString("Type")].isNull() && m_type_isValid;
}

QString OAIBuildSystem_Shared_DTO_Parameter::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBuildSystem_Shared_DTO_Parameter::asJsonObject() const {
    QJsonObject obj;
    if (m_direction_isSet) {
        obj.insert(QString("Direction"), ::OpenAPI::toJsonValue(m_direction));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("Type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIBuildSystem_Shared_DTO_Parameter::getDirection() const {
    return m_direction;
}
void OAIBuildSystem_Shared_DTO_Parameter::setDirection(const QString &direction) {
    m_direction = direction;
    m_direction_isSet = true;
}

bool OAIBuildSystem_Shared_DTO_Parameter::is_direction_Set() const{
    return m_direction_isSet;
}

bool OAIBuildSystem_Shared_DTO_Parameter::is_direction_Valid() const{
    return m_direction_isValid;
}

QString OAIBuildSystem_Shared_DTO_Parameter::getName() const {
    return m_name;
}
void OAIBuildSystem_Shared_DTO_Parameter::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBuildSystem_Shared_DTO_Parameter::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBuildSystem_Shared_DTO_Parameter::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIBuildSystem_Shared_DTO_Parameter::getType() const {
    return m_type;
}
void OAIBuildSystem_Shared_DTO_Parameter::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIBuildSystem_Shared_DTO_Parameter::is_type_Set() const{
    return m_type_isSet;
}

bool OAIBuildSystem_Shared_DTO_Parameter::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIBuildSystem_Shared_DTO_Parameter::isSet() const {
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

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBuildSystem_Shared_DTO_Parameter::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
