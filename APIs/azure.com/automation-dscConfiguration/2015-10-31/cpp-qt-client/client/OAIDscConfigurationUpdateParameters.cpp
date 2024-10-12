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

#include "OAIDscConfigurationUpdateParameters.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDscConfigurationUpdateParameters::OAIDscConfigurationUpdateParameters(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDscConfigurationUpdateParameters::OAIDscConfigurationUpdateParameters() {
    this->initializeModel();
}

OAIDscConfigurationUpdateParameters::~OAIDscConfigurationUpdateParameters() {}

void OAIDscConfigurationUpdateParameters::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;
}

void OAIDscConfigurationUpdateParameters::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDscConfigurationUpdateParameters::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;
}

QString OAIDscConfigurationUpdateParameters::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDscConfigurationUpdateParameters::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    return obj;
}

QString OAIDscConfigurationUpdateParameters::getName() const {
    return m_name;
}
void OAIDscConfigurationUpdateParameters::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIDscConfigurationUpdateParameters::is_name_Set() const{
    return m_name_isSet;
}

bool OAIDscConfigurationUpdateParameters::is_name_Valid() const{
    return m_name_isValid;
}

OAIDscConfigurationCreateOrUpdateProperties OAIDscConfigurationUpdateParameters::getProperties() const {
    return m_properties;
}
void OAIDscConfigurationUpdateParameters::setProperties(const OAIDscConfigurationCreateOrUpdateProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIDscConfigurationUpdateParameters::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIDscConfigurationUpdateParameters::is_properties_Valid() const{
    return m_properties_isValid;
}

QMap<QString, QString> OAIDscConfigurationUpdateParameters::getTags() const {
    return m_tags;
}
void OAIDscConfigurationUpdateParameters::setTags(const QMap<QString, QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIDscConfigurationUpdateParameters::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIDscConfigurationUpdateParameters::is_tags_Valid() const{
    return m_tags_isValid;
}

bool OAIDscConfigurationUpdateParameters::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDscConfigurationUpdateParameters::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
