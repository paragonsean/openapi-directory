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

#include "OAIPodcastMinimumRss.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPodcastMinimumRss::OAIPodcastMinimumRss(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPodcastMinimumRss::OAIPodcastMinimumRss() {
    this->initializeModel();
}

OAIPodcastMinimumRss::~OAIPodcastMinimumRss() {}

void OAIPodcastMinimumRss::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_listennotes_url_isSet = false;
    m_listennotes_url_isValid = false;

    m_publisher_isSet = false;
    m_publisher_isValid = false;

    m_rss_isSet = false;
    m_rss_isValid = false;

    m_thumbnail_isSet = false;
    m_thumbnail_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAIPodcastMinimumRss::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPodcastMinimumRss::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_listennotes_url_isValid = ::OpenAPI::fromJsonValue(m_listennotes_url, json[QString("listennotes_url")]);
    m_listennotes_url_isSet = !json[QString("listennotes_url")].isNull() && m_listennotes_url_isValid;

    m_publisher_isValid = ::OpenAPI::fromJsonValue(m_publisher, json[QString("publisher")]);
    m_publisher_isSet = !json[QString("publisher")].isNull() && m_publisher_isValid;

    m_rss_isValid = ::OpenAPI::fromJsonValue(m_rss, json[QString("rss")]);
    m_rss_isSet = !json[QString("rss")].isNull() && m_rss_isValid;

    m_thumbnail_isValid = ::OpenAPI::fromJsonValue(m_thumbnail, json[QString("thumbnail")]);
    m_thumbnail_isSet = !json[QString("thumbnail")].isNull() && m_thumbnail_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAIPodcastMinimumRss::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPodcastMinimumRss::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_listennotes_url_isSet) {
        obj.insert(QString("listennotes_url"), ::OpenAPI::toJsonValue(m_listennotes_url));
    }
    if (m_publisher_isSet) {
        obj.insert(QString("publisher"), ::OpenAPI::toJsonValue(m_publisher));
    }
    if (m_rss_isSet) {
        obj.insert(QString("rss"), ::OpenAPI::toJsonValue(m_rss));
    }
    if (m_thumbnail_isSet) {
        obj.insert(QString("thumbnail"), ::OpenAPI::toJsonValue(m_thumbnail));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

QString OAIPodcastMinimumRss::getId() const {
    return m_id;
}
void OAIPodcastMinimumRss::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPodcastMinimumRss::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPodcastMinimumRss::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPodcastMinimumRss::getImage() const {
    return m_image;
}
void OAIPodcastMinimumRss::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIPodcastMinimumRss::is_image_Set() const{
    return m_image_isSet;
}

bool OAIPodcastMinimumRss::is_image_Valid() const{
    return m_image_isValid;
}

QString OAIPodcastMinimumRss::getListennotesUrl() const {
    return m_listennotes_url;
}
void OAIPodcastMinimumRss::setListennotesUrl(const QString &listennotes_url) {
    m_listennotes_url = listennotes_url;
    m_listennotes_url_isSet = true;
}

bool OAIPodcastMinimumRss::is_listennotes_url_Set() const{
    return m_listennotes_url_isSet;
}

bool OAIPodcastMinimumRss::is_listennotes_url_Valid() const{
    return m_listennotes_url_isValid;
}

QString OAIPodcastMinimumRss::getPublisher() const {
    return m_publisher;
}
void OAIPodcastMinimumRss::setPublisher(const QString &publisher) {
    m_publisher = publisher;
    m_publisher_isSet = true;
}

bool OAIPodcastMinimumRss::is_publisher_Set() const{
    return m_publisher_isSet;
}

bool OAIPodcastMinimumRss::is_publisher_Valid() const{
    return m_publisher_isValid;
}

QString OAIPodcastMinimumRss::getRss() const {
    return m_rss;
}
void OAIPodcastMinimumRss::setRss(const QString &rss) {
    m_rss = rss;
    m_rss_isSet = true;
}

bool OAIPodcastMinimumRss::is_rss_Set() const{
    return m_rss_isSet;
}

bool OAIPodcastMinimumRss::is_rss_Valid() const{
    return m_rss_isValid;
}

QString OAIPodcastMinimumRss::getThumbnail() const {
    return m_thumbnail;
}
void OAIPodcastMinimumRss::setThumbnail(const QString &thumbnail) {
    m_thumbnail = thumbnail;
    m_thumbnail_isSet = true;
}

bool OAIPodcastMinimumRss::is_thumbnail_Set() const{
    return m_thumbnail_isSet;
}

bool OAIPodcastMinimumRss::is_thumbnail_Valid() const{
    return m_thumbnail_isValid;
}

QString OAIPodcastMinimumRss::getTitle() const {
    return m_title;
}
void OAIPodcastMinimumRss::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIPodcastMinimumRss::is_title_Set() const{
    return m_title_isSet;
}

bool OAIPodcastMinimumRss::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIPodcastMinimumRss::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_listennotes_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publisher_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rss_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_thumbnail_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPodcastMinimumRss::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
