/**
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRecognizedEntityRegion.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRecognizedEntityRegion::OAIRecognizedEntityRegion(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRecognizedEntityRegion::OAIRecognizedEntityRegion() {
    this->initializeModel();
}

OAIRecognizedEntityRegion::~OAIRecognizedEntityRegion() {}

void OAIRecognizedEntityRegion::initializeModel() {

    m_matching_entities_isSet = false;
    m_matching_entities_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_read_link_isSet = false;
    m_read_link_isValid = false;

    m_web_search_url_isSet = false;
    m_web_search_url_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m__type_isSet = false;
    m__type_isValid = false;
}

void OAIRecognizedEntityRegion::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRecognizedEntityRegion::fromJsonObject(QJsonObject json) {

    m_matching_entities_isValid = ::OpenAPI::fromJsonValue(m_matching_entities, json[QString("matchingEntities")]);
    m_matching_entities_isSet = !json[QString("matchingEntities")].isNull() && m_matching_entities_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_read_link_isValid = ::OpenAPI::fromJsonValue(m_read_link, json[QString("readLink")]);
    m_read_link_isSet = !json[QString("readLink")].isNull() && m_read_link_isValid;

    m_web_search_url_isValid = ::OpenAPI::fromJsonValue(m_web_search_url, json[QString("webSearchUrl")]);
    m_web_search_url_isSet = !json[QString("webSearchUrl")].isNull() && m_web_search_url_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m__type_isValid = ::OpenAPI::fromJsonValue(m__type, json[QString("_type")]);
    m__type_isSet = !json[QString("_type")].isNull() && m__type_isValid;
}

QString OAIRecognizedEntityRegion::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRecognizedEntityRegion::asJsonObject() const {
    QJsonObject obj;
    if (m_matching_entities.size() > 0) {
        obj.insert(QString("matchingEntities"), ::OpenAPI::toJsonValue(m_matching_entities));
    }
    if (m_region.isSet()) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_read_link_isSet) {
        obj.insert(QString("readLink"), ::OpenAPI::toJsonValue(m_read_link));
    }
    if (m_web_search_url_isSet) {
        obj.insert(QString("webSearchUrl"), ::OpenAPI::toJsonValue(m_web_search_url));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m__type_isSet) {
        obj.insert(QString("_type"), ::OpenAPI::toJsonValue(m__type));
    }
    return obj;
}

QList<OAIRecognizedEntity> OAIRecognizedEntityRegion::getMatchingEntities() const {
    return m_matching_entities;
}
void OAIRecognizedEntityRegion::setMatchingEntities(const QList<OAIRecognizedEntity> &matching_entities) {
    m_matching_entities = matching_entities;
    m_matching_entities_isSet = true;
}

bool OAIRecognizedEntityRegion::is_matching_entities_Set() const{
    return m_matching_entities_isSet;
}

bool OAIRecognizedEntityRegion::is_matching_entities_Valid() const{
    return m_matching_entities_isValid;
}

OAINormalizedRectangle OAIRecognizedEntityRegion::getRegion() const {
    return m_region;
}
void OAIRecognizedEntityRegion::setRegion(const OAINormalizedRectangle &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAIRecognizedEntityRegion::is_region_Set() const{
    return m_region_isSet;
}

bool OAIRecognizedEntityRegion::is_region_Valid() const{
    return m_region_isValid;
}

QString OAIRecognizedEntityRegion::getReadLink() const {
    return m_read_link;
}
void OAIRecognizedEntityRegion::setReadLink(const QString &read_link) {
    m_read_link = read_link;
    m_read_link_isSet = true;
}

bool OAIRecognizedEntityRegion::is_read_link_Set() const{
    return m_read_link_isSet;
}

bool OAIRecognizedEntityRegion::is_read_link_Valid() const{
    return m_read_link_isValid;
}

QString OAIRecognizedEntityRegion::getWebSearchUrl() const {
    return m_web_search_url;
}
void OAIRecognizedEntityRegion::setWebSearchUrl(const QString &web_search_url) {
    m_web_search_url = web_search_url;
    m_web_search_url_isSet = true;
}

bool OAIRecognizedEntityRegion::is_web_search_url_Set() const{
    return m_web_search_url_isSet;
}

bool OAIRecognizedEntityRegion::is_web_search_url_Valid() const{
    return m_web_search_url_isValid;
}

QString OAIRecognizedEntityRegion::getId() const {
    return m_id;
}
void OAIRecognizedEntityRegion::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIRecognizedEntityRegion::is_id_Set() const{
    return m_id_isSet;
}

bool OAIRecognizedEntityRegion::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIRecognizedEntityRegion::getType() const {
    return m__type;
}
void OAIRecognizedEntityRegion::setType(const QString &_type) {
    m__type = _type;
    m__type_isSet = true;
}

bool OAIRecognizedEntityRegion::is__type_Set() const{
    return m__type_isSet;
}

bool OAIRecognizedEntityRegion::is__type_Valid() const{
    return m__type_isValid;
}

bool OAIRecognizedEntityRegion::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_matching_entities.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_region.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_read_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_web_search_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m__type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRecognizedEntityRegion::isValid() const {
    // only required properties are required for the object to be considered valid
    return m__type_isValid && true;
}

} // namespace OpenAPI
