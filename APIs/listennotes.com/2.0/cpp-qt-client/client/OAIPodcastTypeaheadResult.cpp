/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPodcastTypeaheadResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPodcastTypeaheadResult::OAIPodcastTypeaheadResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPodcastTypeaheadResult::OAIPodcastTypeaheadResult() {
    this->initializeModel();
}

OAIPodcastTypeaheadResult::~OAIPodcastTypeaheadResult() {}

void OAIPodcastTypeaheadResult::initializeModel() {

    m_explicit_content_isSet = false;
    m_explicit_content_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_publisher_highlighted_isSet = false;
    m_publisher_highlighted_isValid = false;

    m_publisher_original_isSet = false;
    m_publisher_original_isValid = false;

    m_thumbnail_isSet = false;
    m_thumbnail_isValid = false;

    m_title_highlighted_isSet = false;
    m_title_highlighted_isValid = false;

    m_title_original_isSet = false;
    m_title_original_isValid = false;
}

void OAIPodcastTypeaheadResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPodcastTypeaheadResult::fromJsonObject(QJsonObject json) {

    m_explicit_content_isValid = ::OpenAPI::fromJsonValue(m_explicit_content, json[QString("explicit_content")]);
    m_explicit_content_isSet = !json[QString("explicit_content")].isNull() && m_explicit_content_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_publisher_highlighted_isValid = ::OpenAPI::fromJsonValue(m_publisher_highlighted, json[QString("publisher_highlighted")]);
    m_publisher_highlighted_isSet = !json[QString("publisher_highlighted")].isNull() && m_publisher_highlighted_isValid;

    m_publisher_original_isValid = ::OpenAPI::fromJsonValue(m_publisher_original, json[QString("publisher_original")]);
    m_publisher_original_isSet = !json[QString("publisher_original")].isNull() && m_publisher_original_isValid;

    m_thumbnail_isValid = ::OpenAPI::fromJsonValue(m_thumbnail, json[QString("thumbnail")]);
    m_thumbnail_isSet = !json[QString("thumbnail")].isNull() && m_thumbnail_isValid;

    m_title_highlighted_isValid = ::OpenAPI::fromJsonValue(m_title_highlighted, json[QString("title_highlighted")]);
    m_title_highlighted_isSet = !json[QString("title_highlighted")].isNull() && m_title_highlighted_isValid;

    m_title_original_isValid = ::OpenAPI::fromJsonValue(m_title_original, json[QString("title_original")]);
    m_title_original_isSet = !json[QString("title_original")].isNull() && m_title_original_isValid;
}

QString OAIPodcastTypeaheadResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPodcastTypeaheadResult::asJsonObject() const {
    QJsonObject obj;
    if (m_explicit_content_isSet) {
        obj.insert(QString("explicit_content"), ::OpenAPI::toJsonValue(m_explicit_content));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_publisher_highlighted_isSet) {
        obj.insert(QString("publisher_highlighted"), ::OpenAPI::toJsonValue(m_publisher_highlighted));
    }
    if (m_publisher_original_isSet) {
        obj.insert(QString("publisher_original"), ::OpenAPI::toJsonValue(m_publisher_original));
    }
    if (m_thumbnail_isSet) {
        obj.insert(QString("thumbnail"), ::OpenAPI::toJsonValue(m_thumbnail));
    }
    if (m_title_highlighted_isSet) {
        obj.insert(QString("title_highlighted"), ::OpenAPI::toJsonValue(m_title_highlighted));
    }
    if (m_title_original_isSet) {
        obj.insert(QString("title_original"), ::OpenAPI::toJsonValue(m_title_original));
    }
    return obj;
}

bool OAIPodcastTypeaheadResult::isExplicitContent() const {
    return m_explicit_content;
}
void OAIPodcastTypeaheadResult::setExplicitContent(const bool &explicit_content) {
    m_explicit_content = explicit_content;
    m_explicit_content_isSet = true;
}

bool OAIPodcastTypeaheadResult::is_explicit_content_Set() const{
    return m_explicit_content_isSet;
}

bool OAIPodcastTypeaheadResult::is_explicit_content_Valid() const{
    return m_explicit_content_isValid;
}

QString OAIPodcastTypeaheadResult::getId() const {
    return m_id;
}
void OAIPodcastTypeaheadResult::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPodcastTypeaheadResult::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPodcastTypeaheadResult::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPodcastTypeaheadResult::getImage() const {
    return m_image;
}
void OAIPodcastTypeaheadResult::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIPodcastTypeaheadResult::is_image_Set() const{
    return m_image_isSet;
}

bool OAIPodcastTypeaheadResult::is_image_Valid() const{
    return m_image_isValid;
}

QString OAIPodcastTypeaheadResult::getPublisherHighlighted() const {
    return m_publisher_highlighted;
}
void OAIPodcastTypeaheadResult::setPublisherHighlighted(const QString &publisher_highlighted) {
    m_publisher_highlighted = publisher_highlighted;
    m_publisher_highlighted_isSet = true;
}

bool OAIPodcastTypeaheadResult::is_publisher_highlighted_Set() const{
    return m_publisher_highlighted_isSet;
}

bool OAIPodcastTypeaheadResult::is_publisher_highlighted_Valid() const{
    return m_publisher_highlighted_isValid;
}

QString OAIPodcastTypeaheadResult::getPublisherOriginal() const {
    return m_publisher_original;
}
void OAIPodcastTypeaheadResult::setPublisherOriginal(const QString &publisher_original) {
    m_publisher_original = publisher_original;
    m_publisher_original_isSet = true;
}

bool OAIPodcastTypeaheadResult::is_publisher_original_Set() const{
    return m_publisher_original_isSet;
}

bool OAIPodcastTypeaheadResult::is_publisher_original_Valid() const{
    return m_publisher_original_isValid;
}

QString OAIPodcastTypeaheadResult::getThumbnail() const {
    return m_thumbnail;
}
void OAIPodcastTypeaheadResult::setThumbnail(const QString &thumbnail) {
    m_thumbnail = thumbnail;
    m_thumbnail_isSet = true;
}

bool OAIPodcastTypeaheadResult::is_thumbnail_Set() const{
    return m_thumbnail_isSet;
}

bool OAIPodcastTypeaheadResult::is_thumbnail_Valid() const{
    return m_thumbnail_isValid;
}

QString OAIPodcastTypeaheadResult::getTitleHighlighted() const {
    return m_title_highlighted;
}
void OAIPodcastTypeaheadResult::setTitleHighlighted(const QString &title_highlighted) {
    m_title_highlighted = title_highlighted;
    m_title_highlighted_isSet = true;
}

bool OAIPodcastTypeaheadResult::is_title_highlighted_Set() const{
    return m_title_highlighted_isSet;
}

bool OAIPodcastTypeaheadResult::is_title_highlighted_Valid() const{
    return m_title_highlighted_isValid;
}

QString OAIPodcastTypeaheadResult::getTitleOriginal() const {
    return m_title_original;
}
void OAIPodcastTypeaheadResult::setTitleOriginal(const QString &title_original) {
    m_title_original = title_original;
    m_title_original_isSet = true;
}

bool OAIPodcastTypeaheadResult::is_title_original_Set() const{
    return m_title_original_isSet;
}

bool OAIPodcastTypeaheadResult::is_title_original_Valid() const{
    return m_title_original_isValid;
}

bool OAIPodcastTypeaheadResult::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_explicit_content_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publisher_highlighted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publisher_original_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbnail_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_highlighted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_original_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPodcastTypeaheadResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
