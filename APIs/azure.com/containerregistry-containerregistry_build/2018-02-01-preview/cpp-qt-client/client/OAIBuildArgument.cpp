/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBuildArgument.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBuildArgument::OAIBuildArgument(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBuildArgument::OAIBuildArgument() {
    this->initializeModel();
}

OAIBuildArgument::~OAIBuildArgument() {}

void OAIBuildArgument::initializeModel() {

    m_is_secret_isSet = false;
    m_is_secret_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIBuildArgument::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBuildArgument::fromJsonObject(QJsonObject json) {

    m_is_secret_isValid = ::OpenAPI::fromJsonValue(m_is_secret, json[QString("isSecret")]);
    m_is_secret_isSet = !json[QString("isSecret")].isNull() && m_is_secret_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIBuildArgument::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBuildArgument::asJsonObject() const {
    QJsonObject obj;
    if (m_is_secret_isSet) {
        obj.insert(QString("isSecret"), ::OpenAPI::toJsonValue(m_is_secret));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

bool OAIBuildArgument::isIsSecret() const {
    return m_is_secret;
}
void OAIBuildArgument::setIsSecret(const bool &is_secret) {
    m_is_secret = is_secret;
    m_is_secret_isSet = true;
}

bool OAIBuildArgument::is_is_secret_Set() const{
    return m_is_secret_isSet;
}

bool OAIBuildArgument::is_is_secret_Valid() const{
    return m_is_secret_isValid;
}

QString OAIBuildArgument::getName() const {
    return m_name;
}
void OAIBuildArgument::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBuildArgument::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBuildArgument::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIBuildArgument::getType() const {
    return m_type;
}
void OAIBuildArgument::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIBuildArgument::is_type_Set() const{
    return m_type_isSet;
}

bool OAIBuildArgument::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIBuildArgument::getValue() const {
    return m_value;
}
void OAIBuildArgument::setValue(const QString &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIBuildArgument::is_value_Set() const{
    return m_value_isSet;
}

bool OAIBuildArgument::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIBuildArgument::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_secret_isSet) {
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

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBuildArgument::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && m_type_isValid && m_value_isValid && true;
}

} // namespace OpenAPI
