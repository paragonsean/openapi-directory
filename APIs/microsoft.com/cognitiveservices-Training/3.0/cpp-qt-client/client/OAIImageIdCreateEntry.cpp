/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImageIdCreateEntry.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageIdCreateEntry::OAIImageIdCreateEntry(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageIdCreateEntry::OAIImageIdCreateEntry() {
    this->initializeModel();
}

OAIImageIdCreateEntry::~OAIImageIdCreateEntry() {}

void OAIImageIdCreateEntry::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_regions_isSet = false;
    m_regions_isValid = false;

    m_tag_ids_isSet = false;
    m_tag_ids_isValid = false;
}

void OAIImageIdCreateEntry::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImageIdCreateEntry::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_regions_isValid = ::OpenAPI::fromJsonValue(m_regions, json[QString("regions")]);
    m_regions_isSet = !json[QString("regions")].isNull() && m_regions_isValid;

    m_tag_ids_isValid = ::OpenAPI::fromJsonValue(m_tag_ids, json[QString("tagIds")]);
    m_tag_ids_isSet = !json[QString("tagIds")].isNull() && m_tag_ids_isValid;
}

QString OAIImageIdCreateEntry::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImageIdCreateEntry::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_regions.size() > 0) {
        obj.insert(QString("regions"), ::OpenAPI::toJsonValue(m_regions));
    }
    if (m_tag_ids.size() > 0) {
        obj.insert(QString("tagIds"), ::OpenAPI::toJsonValue(m_tag_ids));
    }
    return obj;
}

QString OAIImageIdCreateEntry::getId() const {
    return m_id;
}
void OAIImageIdCreateEntry::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIImageIdCreateEntry::is_id_Set() const{
    return m_id_isSet;
}

bool OAIImageIdCreateEntry::is_id_Valid() const{
    return m_id_isValid;
}

QList<OAIRegion> OAIImageIdCreateEntry::getRegions() const {
    return m_regions;
}
void OAIImageIdCreateEntry::setRegions(const QList<OAIRegion> &regions) {
    m_regions = regions;
    m_regions_isSet = true;
}

bool OAIImageIdCreateEntry::is_regions_Set() const{
    return m_regions_isSet;
}

bool OAIImageIdCreateEntry::is_regions_Valid() const{
    return m_regions_isValid;
}

QList<QString> OAIImageIdCreateEntry::getTagIds() const {
    return m_tag_ids;
}
void OAIImageIdCreateEntry::setTagIds(const QList<QString> &tag_ids) {
    m_tag_ids = tag_ids;
    m_tag_ids_isSet = true;
}

bool OAIImageIdCreateEntry::is_tag_ids_Set() const{
    return m_tag_ids_isSet;
}

bool OAIImageIdCreateEntry::is_tag_ids_Valid() const{
    return m_tag_ids_isValid;
}

bool OAIImageIdCreateEntry::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_regions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImageIdCreateEntry::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
