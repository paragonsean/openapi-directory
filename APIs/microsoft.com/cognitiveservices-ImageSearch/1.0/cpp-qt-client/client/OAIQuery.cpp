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

#include "OAIQuery.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQuery::OAIQuery(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQuery::OAIQuery() {
    this->initializeModel();
}

OAIQuery::~OAIQuery() {}

void OAIQuery::initializeModel() {

    m_display_text_isSet = false;
    m_display_text_isValid = false;

    m_search_link_isSet = false;
    m_search_link_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;

    m_thumbnail_isSet = false;
    m_thumbnail_isValid = false;

    m_web_search_url_isSet = false;
    m_web_search_url_isValid = false;
}

void OAIQuery::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQuery::fromJsonObject(QJsonObject json) {

    m_display_text_isValid = ::OpenAPI::fromJsonValue(m_display_text, json[QString("displayText")]);
    m_display_text_isSet = !json[QString("displayText")].isNull() && m_display_text_isValid;

    m_search_link_isValid = ::OpenAPI::fromJsonValue(m_search_link, json[QString("searchLink")]);
    m_search_link_isSet = !json[QString("searchLink")].isNull() && m_search_link_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;

    m_thumbnail_isValid = ::OpenAPI::fromJsonValue(m_thumbnail, json[QString("thumbnail")]);
    m_thumbnail_isSet = !json[QString("thumbnail")].isNull() && m_thumbnail_isValid;

    m_web_search_url_isValid = ::OpenAPI::fromJsonValue(m_web_search_url, json[QString("webSearchUrl")]);
    m_web_search_url_isSet = !json[QString("webSearchUrl")].isNull() && m_web_search_url_isValid;
}

QString OAIQuery::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQuery::asJsonObject() const {
    QJsonObject obj;
    if (m_display_text_isSet) {
        obj.insert(QString("displayText"), ::OpenAPI::toJsonValue(m_display_text));
    }
    if (m_search_link_isSet) {
        obj.insert(QString("searchLink"), ::OpenAPI::toJsonValue(m_search_link));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    if (m_thumbnail.isSet()) {
        obj.insert(QString("thumbnail"), ::OpenAPI::toJsonValue(m_thumbnail));
    }
    if (m_web_search_url_isSet) {
        obj.insert(QString("webSearchUrl"), ::OpenAPI::toJsonValue(m_web_search_url));
    }
    return obj;
}

QString OAIQuery::getDisplayText() const {
    return m_display_text;
}
void OAIQuery::setDisplayText(const QString &display_text) {
    m_display_text = display_text;
    m_display_text_isSet = true;
}

bool OAIQuery::is_display_text_Set() const{
    return m_display_text_isSet;
}

bool OAIQuery::is_display_text_Valid() const{
    return m_display_text_isValid;
}

QString OAIQuery::getSearchLink() const {
    return m_search_link;
}
void OAIQuery::setSearchLink(const QString &search_link) {
    m_search_link = search_link;
    m_search_link_isSet = true;
}

bool OAIQuery::is_search_link_Set() const{
    return m_search_link_isSet;
}

bool OAIQuery::is_search_link_Valid() const{
    return m_search_link_isValid;
}

QString OAIQuery::getText() const {
    return m_text;
}
void OAIQuery::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIQuery::is_text_Set() const{
    return m_text_isSet;
}

bool OAIQuery::is_text_Valid() const{
    return m_text_isValid;
}

OAIImageObject OAIQuery::getThumbnail() const {
    return m_thumbnail;
}
void OAIQuery::setThumbnail(const OAIImageObject &thumbnail) {
    m_thumbnail = thumbnail;
    m_thumbnail_isSet = true;
}

bool OAIQuery::is_thumbnail_Set() const{
    return m_thumbnail_isSet;
}

bool OAIQuery::is_thumbnail_Valid() const{
    return m_thumbnail_isValid;
}

QString OAIQuery::getWebSearchUrl() const {
    return m_web_search_url;
}
void OAIQuery::setWebSearchUrl(const QString &web_search_url) {
    m_web_search_url = web_search_url;
    m_web_search_url_isSet = true;
}

bool OAIQuery::is_web_search_url_Set() const{
    return m_web_search_url_isSet;
}

bool OAIQuery::is_web_search_url_Valid() const{
    return m_web_search_url_isValid;
}

bool OAIQuery::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_display_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_search_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbnail.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_web_search_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQuery::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_text_isValid && true;
}

} // namespace OpenAPI
