/**
 * FabricAdminClient
 * Volume operation endpoints and objects.
 *
 * The version of the OpenAPI document: 2018-10-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVolume.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVolume::OAIVolume(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVolume::OAIVolume() {
    this->initializeModel();
}

OAIVolume::~OAIVolume() {}

void OAIVolume::initializeModel() {

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIVolume::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVolume::fromJsonObject(QJsonObject json) {

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIVolume::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVolume::asJsonObject() const {
    QJsonObject obj;
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_location_isSet) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAIVolumeModel OAIVolume::getProperties() const {
    return m_properties;
}
void OAIVolume::setProperties(const OAIVolumeModel &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIVolume::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIVolume::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIVolume::getId() const {
    return m_id;
}
void OAIVolume::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIVolume::is_id_Set() const{
    return m_id_isSet;
}

bool OAIVolume::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIVolume::getLocation() const {
    return m_location;
}
void OAIVolume::setLocation(const QString &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAIVolume::is_location_Set() const{
    return m_location_isSet;
}

bool OAIVolume::is_location_Valid() const{
    return m_location_isValid;
}

QString OAIVolume::getName() const {
    return m_name;
}
void OAIVolume::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIVolume::is_name_Set() const{
    return m_name_isSet;
}

bool OAIVolume::is_name_Valid() const{
    return m_name_isValid;
}

QMap<QString, QString> OAIVolume::getTags() const {
    return m_tags;
}
void OAIVolume::setTags(const QMap<QString, QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIVolume::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIVolume::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIVolume::getType() const {
    return m_type;
}
void OAIVolume::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIVolume::is_type_Set() const{
    return m_type_isSet;
}

bool OAIVolume::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIVolume::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
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

bool OAIVolume::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
