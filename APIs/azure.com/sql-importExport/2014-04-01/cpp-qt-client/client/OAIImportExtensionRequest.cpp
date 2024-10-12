/**
 * Azure SQL Database Import/Export spec
 * Provides create and read functionality for Import/Export operations on Azure SQL databases.
 *
 * The version of the OpenAPI document: 2014-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImportExtensionRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImportExtensionRequest::OAIImportExtensionRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImportExtensionRequest::OAIImportExtensionRequest() {
    this->initializeModel();
}

OAIImportExtensionRequest::~OAIImportExtensionRequest() {}

void OAIImportExtensionRequest::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIImportExtensionRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImportExtensionRequest::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIImportExtensionRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImportExtensionRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIImportExtensionRequest::getName() const {
    return m_name;
}
void OAIImportExtensionRequest::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIImportExtensionRequest::is_name_Set() const{
    return m_name_isSet;
}

bool OAIImportExtensionRequest::is_name_Valid() const{
    return m_name_isValid;
}

OAIImportExtensionProperties OAIImportExtensionRequest::getProperties() const {
    return m_properties;
}
void OAIImportExtensionRequest::setProperties(const OAIImportExtensionProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIImportExtensionRequest::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIImportExtensionRequest::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIImportExtensionRequest::getType() const {
    return m_type;
}
void OAIImportExtensionRequest::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIImportExtensionRequest::is_type_Set() const{
    return m_type_isSet;
}

bool OAIImportExtensionRequest::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIImportExtensionRequest::isSet() const {
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

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImportExtensionRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
