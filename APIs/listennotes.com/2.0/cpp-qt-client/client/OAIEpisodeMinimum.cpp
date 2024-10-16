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

#include "OAIEpisodeMinimum.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEpisodeMinimum::OAIEpisodeMinimum(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEpisodeMinimum::OAIEpisodeMinimum() {
    this->initializeModel();
}

OAIEpisodeMinimum::~OAIEpisodeMinimum() {}

void OAIEpisodeMinimum::initializeModel() {

    m_audio_isSet = false;
    m_audio_isValid = false;

    m_audio_length_sec_isSet = false;
    m_audio_length_sec_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_explicit_content_isSet = false;
    m_explicit_content_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_link_isSet = false;
    m_link_isValid = false;

    m_listennotes_edit_url_isSet = false;
    m_listennotes_edit_url_isValid = false;

    m_listennotes_url_isSet = false;
    m_listennotes_url_isValid = false;

    m_maybe_audio_invalid_isSet = false;
    m_maybe_audio_invalid_isValid = false;

    m_pub_date_ms_isSet = false;
    m_pub_date_ms_isValid = false;

    m_thumbnail_isSet = false;
    m_thumbnail_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAIEpisodeMinimum::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEpisodeMinimum::fromJsonObject(QJsonObject json) {

    m_audio_isValid = ::OpenAPI::fromJsonValue(m_audio, json[QString("audio")]);
    m_audio_isSet = !json[QString("audio")].isNull() && m_audio_isValid;

    m_audio_length_sec_isValid = ::OpenAPI::fromJsonValue(m_audio_length_sec, json[QString("audio_length_sec")]);
    m_audio_length_sec_isSet = !json[QString("audio_length_sec")].isNull() && m_audio_length_sec_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_explicit_content_isValid = ::OpenAPI::fromJsonValue(m_explicit_content, json[QString("explicit_content")]);
    m_explicit_content_isSet = !json[QString("explicit_content")].isNull() && m_explicit_content_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_link_isValid = ::OpenAPI::fromJsonValue(m_link, json[QString("link")]);
    m_link_isSet = !json[QString("link")].isNull() && m_link_isValid;

    m_listennotes_edit_url_isValid = ::OpenAPI::fromJsonValue(m_listennotes_edit_url, json[QString("listennotes_edit_url")]);
    m_listennotes_edit_url_isSet = !json[QString("listennotes_edit_url")].isNull() && m_listennotes_edit_url_isValid;

    m_listennotes_url_isValid = ::OpenAPI::fromJsonValue(m_listennotes_url, json[QString("listennotes_url")]);
    m_listennotes_url_isSet = !json[QString("listennotes_url")].isNull() && m_listennotes_url_isValid;

    m_maybe_audio_invalid_isValid = ::OpenAPI::fromJsonValue(m_maybe_audio_invalid, json[QString("maybe_audio_invalid")]);
    m_maybe_audio_invalid_isSet = !json[QString("maybe_audio_invalid")].isNull() && m_maybe_audio_invalid_isValid;

    m_pub_date_ms_isValid = ::OpenAPI::fromJsonValue(m_pub_date_ms, json[QString("pub_date_ms")]);
    m_pub_date_ms_isSet = !json[QString("pub_date_ms")].isNull() && m_pub_date_ms_isValid;

    m_thumbnail_isValid = ::OpenAPI::fromJsonValue(m_thumbnail, json[QString("thumbnail")]);
    m_thumbnail_isSet = !json[QString("thumbnail")].isNull() && m_thumbnail_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAIEpisodeMinimum::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEpisodeMinimum::asJsonObject() const {
    QJsonObject obj;
    if (m_audio_isSet) {
        obj.insert(QString("audio"), ::OpenAPI::toJsonValue(m_audio));
    }
    if (m_audio_length_sec_isSet) {
        obj.insert(QString("audio_length_sec"), ::OpenAPI::toJsonValue(m_audio_length_sec));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_explicit_content_isSet) {
        obj.insert(QString("explicit_content"), ::OpenAPI::toJsonValue(m_explicit_content));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
    }
    if (m_link_isSet) {
        obj.insert(QString("link"), ::OpenAPI::toJsonValue(m_link));
    }
    if (m_listennotes_edit_url_isSet) {
        obj.insert(QString("listennotes_edit_url"), ::OpenAPI::toJsonValue(m_listennotes_edit_url));
    }
    if (m_listennotes_url_isSet) {
        obj.insert(QString("listennotes_url"), ::OpenAPI::toJsonValue(m_listennotes_url));
    }
    if (m_maybe_audio_invalid_isSet) {
        obj.insert(QString("maybe_audio_invalid"), ::OpenAPI::toJsonValue(m_maybe_audio_invalid));
    }
    if (m_pub_date_ms_isSet) {
        obj.insert(QString("pub_date_ms"), ::OpenAPI::toJsonValue(m_pub_date_ms));
    }
    if (m_thumbnail_isSet) {
        obj.insert(QString("thumbnail"), ::OpenAPI::toJsonValue(m_thumbnail));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

QString OAIEpisodeMinimum::getAudio() const {
    return m_audio;
}
void OAIEpisodeMinimum::setAudio(const QString &audio) {
    m_audio = audio;
    m_audio_isSet = true;
}

bool OAIEpisodeMinimum::is_audio_Set() const{
    return m_audio_isSet;
}

bool OAIEpisodeMinimum::is_audio_Valid() const{
    return m_audio_isValid;
}

qint32 OAIEpisodeMinimum::getAudioLengthSec() const {
    return m_audio_length_sec;
}
void OAIEpisodeMinimum::setAudioLengthSec(const qint32 &audio_length_sec) {
    m_audio_length_sec = audio_length_sec;
    m_audio_length_sec_isSet = true;
}

bool OAIEpisodeMinimum::is_audio_length_sec_Set() const{
    return m_audio_length_sec_isSet;
}

bool OAIEpisodeMinimum::is_audio_length_sec_Valid() const{
    return m_audio_length_sec_isValid;
}

QString OAIEpisodeMinimum::getDescription() const {
    return m_description;
}
void OAIEpisodeMinimum::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIEpisodeMinimum::is_description_Set() const{
    return m_description_isSet;
}

bool OAIEpisodeMinimum::is_description_Valid() const{
    return m_description_isValid;
}

bool OAIEpisodeMinimum::isExplicitContent() const {
    return m_explicit_content;
}
void OAIEpisodeMinimum::setExplicitContent(const bool &explicit_content) {
    m_explicit_content = explicit_content;
    m_explicit_content_isSet = true;
}

bool OAIEpisodeMinimum::is_explicit_content_Set() const{
    return m_explicit_content_isSet;
}

bool OAIEpisodeMinimum::is_explicit_content_Valid() const{
    return m_explicit_content_isValid;
}

QString OAIEpisodeMinimum::getId() const {
    return m_id;
}
void OAIEpisodeMinimum::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIEpisodeMinimum::is_id_Set() const{
    return m_id_isSet;
}

bool OAIEpisodeMinimum::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIEpisodeMinimum::getImage() const {
    return m_image;
}
void OAIEpisodeMinimum::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAIEpisodeMinimum::is_image_Set() const{
    return m_image_isSet;
}

bool OAIEpisodeMinimum::is_image_Valid() const{
    return m_image_isValid;
}

QString OAIEpisodeMinimum::getLink() const {
    return m_link;
}
void OAIEpisodeMinimum::setLink(const QString &link) {
    m_link = link;
    m_link_isSet = true;
}

bool OAIEpisodeMinimum::is_link_Set() const{
    return m_link_isSet;
}

bool OAIEpisodeMinimum::is_link_Valid() const{
    return m_link_isValid;
}

QString OAIEpisodeMinimum::getListennotesEditUrl() const {
    return m_listennotes_edit_url;
}
void OAIEpisodeMinimum::setListennotesEditUrl(const QString &listennotes_edit_url) {
    m_listennotes_edit_url = listennotes_edit_url;
    m_listennotes_edit_url_isSet = true;
}

bool OAIEpisodeMinimum::is_listennotes_edit_url_Set() const{
    return m_listennotes_edit_url_isSet;
}

bool OAIEpisodeMinimum::is_listennotes_edit_url_Valid() const{
    return m_listennotes_edit_url_isValid;
}

QString OAIEpisodeMinimum::getListennotesUrl() const {
    return m_listennotes_url;
}
void OAIEpisodeMinimum::setListennotesUrl(const QString &listennotes_url) {
    m_listennotes_url = listennotes_url;
    m_listennotes_url_isSet = true;
}

bool OAIEpisodeMinimum::is_listennotes_url_Set() const{
    return m_listennotes_url_isSet;
}

bool OAIEpisodeMinimum::is_listennotes_url_Valid() const{
    return m_listennotes_url_isValid;
}

bool OAIEpisodeMinimum::isMaybeAudioInvalid() const {
    return m_maybe_audio_invalid;
}
void OAIEpisodeMinimum::setMaybeAudioInvalid(const bool &maybe_audio_invalid) {
    m_maybe_audio_invalid = maybe_audio_invalid;
    m_maybe_audio_invalid_isSet = true;
}

bool OAIEpisodeMinimum::is_maybe_audio_invalid_Set() const{
    return m_maybe_audio_invalid_isSet;
}

bool OAIEpisodeMinimum::is_maybe_audio_invalid_Valid() const{
    return m_maybe_audio_invalid_isValid;
}

qint32 OAIEpisodeMinimum::getPubDateMs() const {
    return m_pub_date_ms;
}
void OAIEpisodeMinimum::setPubDateMs(const qint32 &pub_date_ms) {
    m_pub_date_ms = pub_date_ms;
    m_pub_date_ms_isSet = true;
}

bool OAIEpisodeMinimum::is_pub_date_ms_Set() const{
    return m_pub_date_ms_isSet;
}

bool OAIEpisodeMinimum::is_pub_date_ms_Valid() const{
    return m_pub_date_ms_isValid;
}

QString OAIEpisodeMinimum::getThumbnail() const {
    return m_thumbnail;
}
void OAIEpisodeMinimum::setThumbnail(const QString &thumbnail) {
    m_thumbnail = thumbnail;
    m_thumbnail_isSet = true;
}

bool OAIEpisodeMinimum::is_thumbnail_Set() const{
    return m_thumbnail_isSet;
}

bool OAIEpisodeMinimum::is_thumbnail_Valid() const{
    return m_thumbnail_isValid;
}

QString OAIEpisodeMinimum::getTitle() const {
    return m_title;
}
void OAIEpisodeMinimum::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIEpisodeMinimum::is_title_Set() const{
    return m_title_isSet;
}

bool OAIEpisodeMinimum::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIEpisodeMinimum::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_audio_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_audio_length_sec_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

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

        if (m_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_listennotes_edit_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_listennotes_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_maybe_audio_invalid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pub_date_ms_isSet) {
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

bool OAIEpisodeMinimum::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
