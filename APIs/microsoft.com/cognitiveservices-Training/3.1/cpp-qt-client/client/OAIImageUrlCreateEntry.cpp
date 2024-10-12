/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIImageUrlCreateEntry.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIImageUrlCreateEntry::OAIImageUrlCreateEntry(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIImageUrlCreateEntry::OAIImageUrlCreateEntry() {
    this->initializeModel();
}

OAIImageUrlCreateEntry::~OAIImageUrlCreateEntry() {}

void OAIImageUrlCreateEntry::initializeModel() {

    m_regions_isSet = false;
    m_regions_isValid = false;

    m_tag_ids_isSet = false;
    m_tag_ids_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;
}

void OAIImageUrlCreateEntry::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIImageUrlCreateEntry::fromJsonObject(QJsonObject json) {

    m_regions_isValid = ::OpenAPI::fromJsonValue(m_regions, json[QString("regions")]);
    m_regions_isSet = !json[QString("regions")].isNull() && m_regions_isValid;

    m_tag_ids_isValid = ::OpenAPI::fromJsonValue(m_tag_ids, json[QString("tagIds")]);
    m_tag_ids_isSet = !json[QString("tagIds")].isNull() && m_tag_ids_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;
}

QString OAIImageUrlCreateEntry::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIImageUrlCreateEntry::asJsonObject() const {
    QJsonObject obj;
    if (m_regions.size() > 0) {
        obj.insert(QString("regions"), ::OpenAPI::toJsonValue(m_regions));
    }
    if (m_tag_ids.size() > 0) {
        obj.insert(QString("tagIds"), ::OpenAPI::toJsonValue(m_tag_ids));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    return obj;
}

QList<OAIRegion> OAIImageUrlCreateEntry::getRegions() const {
    return m_regions;
}
void OAIImageUrlCreateEntry::setRegions(const QList<OAIRegion> &regions) {
    m_regions = regions;
    m_regions_isSet = true;
}

bool OAIImageUrlCreateEntry::is_regions_Set() const{
    return m_regions_isSet;
}

bool OAIImageUrlCreateEntry::is_regions_Valid() const{
    return m_regions_isValid;
}

QList<QString> OAIImageUrlCreateEntry::getTagIds() const {
    return m_tag_ids;
}
void OAIImageUrlCreateEntry::setTagIds(const QList<QString> &tag_ids) {
    m_tag_ids = tag_ids;
    m_tag_ids_isSet = true;
}

bool OAIImageUrlCreateEntry::is_tag_ids_Set() const{
    return m_tag_ids_isSet;
}

bool OAIImageUrlCreateEntry::is_tag_ids_Valid() const{
    return m_tag_ids_isValid;
}

QString OAIImageUrlCreateEntry::getUrl() const {
    return m_url;
}
void OAIImageUrlCreateEntry::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIImageUrlCreateEntry::is_url_Set() const{
    return m_url_isSet;
}

bool OAIImageUrlCreateEntry::is_url_Valid() const{
    return m_url_isValid;
}

bool OAIImageUrlCreateEntry::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_regions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tag_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIImageUrlCreateEntry::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_url_isValid && true;
}

} // namespace OpenAPI
