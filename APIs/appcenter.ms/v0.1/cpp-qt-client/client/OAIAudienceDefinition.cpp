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

#include "OAIAudienceDefinition.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAudienceDefinition::OAIAudienceDefinition(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAudienceDefinition::OAIAudienceDefinition() {
    this->initializeModel();
}

OAIAudienceDefinition::~OAIAudienceDefinition() {}

void OAIAudienceDefinition::initializeModel() {

    m_custom_properties_isSet = false;
    m_custom_properties_isValid = false;

    m_definition_isSet = false;
    m_definition_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;
}

void OAIAudienceDefinition::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAudienceDefinition::fromJsonObject(QJsonObject json) {

    m_custom_properties_isValid = ::OpenAPI::fromJsonValue(m_custom_properties, json[QString("custom_properties")]);
    m_custom_properties_isSet = !json[QString("custom_properties")].isNull() && m_custom_properties_isValid;

    m_definition_isValid = ::OpenAPI::fromJsonValue(m_definition, json[QString("definition")]);
    m_definition_isSet = !json[QString("definition")].isNull() && m_definition_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;
}

QString OAIAudienceDefinition::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAudienceDefinition::asJsonObject() const {
    QJsonObject obj;
    if (m_custom_properties.size() > 0) {
        obj.insert(QString("custom_properties"), ::OpenAPI::toJsonValue(m_custom_properties));
    }
    if (m_definition_isSet) {
        obj.insert(QString("definition"), ::OpenAPI::toJsonValue(m_definition));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    return obj;
}

QMap<QString, QString> OAIAudienceDefinition::getCustomProperties() const {
    return m_custom_properties;
}
void OAIAudienceDefinition::setCustomProperties(const QMap<QString, QString> &custom_properties) {
    m_custom_properties = custom_properties;
    m_custom_properties_isSet = true;
}

bool OAIAudienceDefinition::is_custom_properties_Set() const{
    return m_custom_properties_isSet;
}

bool OAIAudienceDefinition::is_custom_properties_Valid() const{
    return m_custom_properties_isValid;
}

QString OAIAudienceDefinition::getDefinition() const {
    return m_definition;
}
void OAIAudienceDefinition::setDefinition(const QString &definition) {
    m_definition = definition;
    m_definition_isSet = true;
}

bool OAIAudienceDefinition::is_definition_Set() const{
    return m_definition_isSet;
}

bool OAIAudienceDefinition::is_definition_Valid() const{
    return m_definition_isValid;
}

QString OAIAudienceDefinition::getDescription() const {
    return m_description;
}
void OAIAudienceDefinition::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIAudienceDefinition::is_description_Set() const{
    return m_description_isSet;
}

bool OAIAudienceDefinition::is_description_Valid() const{
    return m_description_isValid;
}

bool OAIAudienceDefinition::isEnabled() const {
    return m_enabled;
}
void OAIAudienceDefinition::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIAudienceDefinition::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIAudienceDefinition::is_enabled_Valid() const{
    return m_enabled_isValid;
}

bool OAIAudienceDefinition::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_custom_properties.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_definition_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAudienceDefinition::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_definition_isValid && true;
}

} // namespace OpenAPI
