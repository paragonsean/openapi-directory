/**
 * Azure SQL Database
 * Provides create, read, update and delete functionality for Azure SQL Database resources including recommendations and operations.
 *
 * The version of the OpenAPI document: 2014-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITransparentDataEncryption.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITransparentDataEncryption::OAITransparentDataEncryption(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITransparentDataEncryption::OAITransparentDataEncryption() {
    this->initializeModel();
}

OAITransparentDataEncryption::~OAITransparentDataEncryption() {}

void OAITransparentDataEncryption::initializeModel() {

    m_location_isSet = false;
    m_location_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAITransparentDataEncryption::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITransparentDataEncryption::fromJsonObject(QJsonObject json) {

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAITransparentDataEncryption::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITransparentDataEncryption::asJsonObject() const {
    QJsonObject obj;
    if (m_location_isSet) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAITransparentDataEncryption::getLocation() const {
    return m_location;
}
void OAITransparentDataEncryption::setLocation(const QString &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAITransparentDataEncryption::is_location_Set() const{
    return m_location_isSet;
}

bool OAITransparentDataEncryption::is_location_Valid() const{
    return m_location_isValid;
}

OAITransparentDataEncryptionProperties OAITransparentDataEncryption::getProperties() const {
    return m_properties;
}
void OAITransparentDataEncryption::setProperties(const OAITransparentDataEncryptionProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAITransparentDataEncryption::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAITransparentDataEncryption::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAITransparentDataEncryption::getId() const {
    return m_id;
}
void OAITransparentDataEncryption::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITransparentDataEncryption::is_id_Set() const{
    return m_id_isSet;
}

bool OAITransparentDataEncryption::is_id_Valid() const{
    return m_id_isValid;
}

QString OAITransparentDataEncryption::getName() const {
    return m_name;
}
void OAITransparentDataEncryption::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITransparentDataEncryption::is_name_Set() const{
    return m_name_isSet;
}

bool OAITransparentDataEncryption::is_name_Valid() const{
    return m_name_isValid;
}

QString OAITransparentDataEncryption::getType() const {
    return m_type;
}
void OAITransparentDataEncryption::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAITransparentDataEncryption::is_type_Set() const{
    return m_type_isSet;
}

bool OAITransparentDataEncryption::is_type_Valid() const{
    return m_type_isValid;
}

bool OAITransparentDataEncryption::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
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

bool OAITransparentDataEncryption::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
