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

#include "OAICustomAudio.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomAudio::OAICustomAudio(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomAudio::OAICustomAudio() {
    this->initializeModel();
}

OAICustomAudio::~OAICustomAudio() {}

void OAICustomAudio::initializeModel() {

    m_audio_isSet = false;
    m_audio_isValid = false;

    m_audio_length_sec_isSet = false;
    m_audio_length_sec_isValid = false;

    m_image_isSet = false;
    m_image_isValid = false;

    m_pub_date_ms_isSet = false;
    m_pub_date_ms_isValid = false;

    m_thumbnail_isSet = false;
    m_thumbnail_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAICustomAudio::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomAudio::fromJsonObject(QJsonObject json) {

    m_audio_isValid = ::OpenAPI::fromJsonValue(m_audio, json[QString("audio")]);
    m_audio_isSet = !json[QString("audio")].isNull() && m_audio_isValid;

    m_audio_length_sec_isValid = ::OpenAPI::fromJsonValue(m_audio_length_sec, json[QString("audio_length_sec")]);
    m_audio_length_sec_isSet = !json[QString("audio_length_sec")].isNull() && m_audio_length_sec_isValid;

    m_image_isValid = ::OpenAPI::fromJsonValue(m_image, json[QString("image")]);
    m_image_isSet = !json[QString("image")].isNull() && m_image_isValid;

    m_pub_date_ms_isValid = ::OpenAPI::fromJsonValue(m_pub_date_ms, json[QString("pub_date_ms")]);
    m_pub_date_ms_isSet = !json[QString("pub_date_ms")].isNull() && m_pub_date_ms_isValid;

    m_thumbnail_isValid = ::OpenAPI::fromJsonValue(m_thumbnail, json[QString("thumbnail")]);
    m_thumbnail_isSet = !json[QString("thumbnail")].isNull() && m_thumbnail_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAICustomAudio::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomAudio::asJsonObject() const {
    QJsonObject obj;
    if (m_audio_isSet) {
        obj.insert(QString("audio"), ::OpenAPI::toJsonValue(m_audio));
    }
    if (m_audio_length_sec_isSet) {
        obj.insert(QString("audio_length_sec"), ::OpenAPI::toJsonValue(m_audio_length_sec));
    }
    if (m_image_isSet) {
        obj.insert(QString("image"), ::OpenAPI::toJsonValue(m_image));
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

QString OAICustomAudio::getAudio() const {
    return m_audio;
}
void OAICustomAudio::setAudio(const QString &audio) {
    m_audio = audio;
    m_audio_isSet = true;
}

bool OAICustomAudio::is_audio_Set() const{
    return m_audio_isSet;
}

bool OAICustomAudio::is_audio_Valid() const{
    return m_audio_isValid;
}

qint32 OAICustomAudio::getAudioLengthSec() const {
    return m_audio_length_sec;
}
void OAICustomAudio::setAudioLengthSec(const qint32 &audio_length_sec) {
    m_audio_length_sec = audio_length_sec;
    m_audio_length_sec_isSet = true;
}

bool OAICustomAudio::is_audio_length_sec_Set() const{
    return m_audio_length_sec_isSet;
}

bool OAICustomAudio::is_audio_length_sec_Valid() const{
    return m_audio_length_sec_isValid;
}

QString OAICustomAudio::getImage() const {
    return m_image;
}
void OAICustomAudio::setImage(const QString &image) {
    m_image = image;
    m_image_isSet = true;
}

bool OAICustomAudio::is_image_Set() const{
    return m_image_isSet;
}

bool OAICustomAudio::is_image_Valid() const{
    return m_image_isValid;
}

qint32 OAICustomAudio::getPubDateMs() const {
    return m_pub_date_ms;
}
void OAICustomAudio::setPubDateMs(const qint32 &pub_date_ms) {
    m_pub_date_ms = pub_date_ms;
    m_pub_date_ms_isSet = true;
}

bool OAICustomAudio::is_pub_date_ms_Set() const{
    return m_pub_date_ms_isSet;
}

bool OAICustomAudio::is_pub_date_ms_Valid() const{
    return m_pub_date_ms_isValid;
}

QString OAICustomAudio::getThumbnail() const {
    return m_thumbnail;
}
void OAICustomAudio::setThumbnail(const QString &thumbnail) {
    m_thumbnail = thumbnail;
    m_thumbnail_isSet = true;
}

bool OAICustomAudio::is_thumbnail_Set() const{
    return m_thumbnail_isSet;
}

bool OAICustomAudio::is_thumbnail_Valid() const{
    return m_thumbnail_isValid;
}

QString OAICustomAudio::getTitle() const {
    return m_title;
}
void OAICustomAudio::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAICustomAudio::is_title_Set() const{
    return m_title_isSet;
}

bool OAICustomAudio::is_title_Valid() const{
    return m_title_isValid;
}

bool OAICustomAudio::isSet() const {
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

        if (m_image_isSet) {
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

bool OAICustomAudio::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
