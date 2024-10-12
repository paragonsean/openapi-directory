/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImageFileCreateEntry.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageFileCreateEntry::OAIImageFileCreateEntry(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageFileCreateEntry::OAIImageFileCreateEntry() {
    this->initializeModel();
}

OAIImageFileCreateEntry::~OAIImageFileCreateEntry() {}

void OAIImageFileCreateEntry::initializeModel() {

    m_contents_isSet = false;
    m_contents_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_regions_isSet = false;
    m_regions_isValid = false;

    m_tag_ids_isSet = false;
    m_tag_ids_isValid = false;
}

void OAIImageFileCreateEntry::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImageFileCreateEntry::fromJsonObject(QJsonObject json) {

    m_contents_isValid = ::OpenAPI::fromJsonValue(m_contents, json[QString("contents")]);
    m_contents_isSet = !json[QString("contents")].isNull() && m_contents_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_regions_isValid = ::OpenAPI::fromJsonValue(m_regions, json[QString("regions")]);
    m_regions_isSet = !json[QString("regions")].isNull() && m_regions_isValid;

    m_tag_ids_isValid = ::OpenAPI::fromJsonValue(m_tag_ids, json[QString("tagIds")]);
    m_tag_ids_isSet = !json[QString("tagIds")].isNull() && m_tag_ids_isValid;
}

QString OAIImageFileCreateEntry::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImageFileCreateEntry::asJsonObject() const {
    QJsonObject obj;
    if (m_contents_isSet) {
        obj.insert(QString("contents"), ::OpenAPI::toJsonValue(m_contents));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_regions.size() > 0) {
        obj.insert(QString("regions"), ::OpenAPI::toJsonValue(m_regions));
    }
    if (m_tag_ids.size() > 0) {
        obj.insert(QString("tagIds"), ::OpenAPI::toJsonValue(m_tag_ids));
    }
    return obj;
}

QByteArray OAIImageFileCreateEntry::getContents() const {
    return m_contents;
}
void OAIImageFileCreateEntry::setContents(const QByteArray &contents) {
    m_contents = contents;
    m_contents_isSet = true;
}

bool OAIImageFileCreateEntry::is_contents_Set() const{
    return m_contents_isSet;
}

bool OAIImageFileCreateEntry::is_contents_Valid() const{
    return m_contents_isValid;
}

QString OAIImageFileCreateEntry::getName() const {
    return m_name;
}
void OAIImageFileCreateEntry::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIImageFileCreateEntry::is_name_Set() const{
    return m_name_isSet;
}

bool OAIImageFileCreateEntry::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIRegion> OAIImageFileCreateEntry::getRegions() const {
    return m_regions;
}
void OAIImageFileCreateEntry::setRegions(const QList<OAIRegion> &regions) {
    m_regions = regions;
    m_regions_isSet = true;
}

bool OAIImageFileCreateEntry::is_regions_Set() const{
    return m_regions_isSet;
}

bool OAIImageFileCreateEntry::is_regions_Valid() const{
    return m_regions_isValid;
}

QList<QString> OAIImageFileCreateEntry::getTagIds() const {
    return m_tag_ids;
}
void OAIImageFileCreateEntry::setTagIds(const QList<QString> &tag_ids) {
    m_tag_ids = tag_ids;
    m_tag_ids_isSet = true;
}

bool OAIImageFileCreateEntry::is_tag_ids_Set() const{
    return m_tag_ids_isSet;
}

bool OAIImageFileCreateEntry::is_tag_ids_Valid() const{
    return m_tag_ids_isValid;
}

bool OAIImageFileCreateEntry::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_contents_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

bool OAIImageFileCreateEntry::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
