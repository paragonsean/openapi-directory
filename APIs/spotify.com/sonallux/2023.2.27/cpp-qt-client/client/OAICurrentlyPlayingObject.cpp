/**
 * Spotify Web API with fixes and improvements from sonallux
 * You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 
 *
 * The version of the OpenAPI document: 2023.2.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICurrentlyPlayingObject.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICurrentlyPlayingObject::OAICurrentlyPlayingObject(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICurrentlyPlayingObject::OAICurrentlyPlayingObject() {
    this->initializeModel();
}

OAICurrentlyPlayingObject::~OAICurrentlyPlayingObject() {}

void OAICurrentlyPlayingObject::initializeModel() {

    m_context_isSet = false;
    m_context_isValid = false;

    m_currently_playing_type_isSet = false;
    m_currently_playing_type_isValid = false;

    m_is_playing_isSet = false;
    m_is_playing_isValid = false;

    m_item_isSet = false;
    m_item_isValid = false;

    m_progress_ms_isSet = false;
    m_progress_ms_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;
}

void OAICurrentlyPlayingObject::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICurrentlyPlayingObject::fromJsonObject(QJsonObject json) {

    m_context_isValid = ::OpenAPI::fromJsonValue(m_context, json[QString("context")]);
    m_context_isSet = !json[QString("context")].isNull() && m_context_isValid;

    m_currently_playing_type_isValid = ::OpenAPI::fromJsonValue(m_currently_playing_type, json[QString("currently_playing_type")]);
    m_currently_playing_type_isSet = !json[QString("currently_playing_type")].isNull() && m_currently_playing_type_isValid;

    m_is_playing_isValid = ::OpenAPI::fromJsonValue(m_is_playing, json[QString("is_playing")]);
    m_is_playing_isSet = !json[QString("is_playing")].isNull() && m_is_playing_isValid;

    m_item_isValid = ::OpenAPI::fromJsonValue(m_item, json[QString("item")]);
    m_item_isSet = !json[QString("item")].isNull() && m_item_isValid;

    m_progress_ms_isValid = ::OpenAPI::fromJsonValue(m_progress_ms, json[QString("progress_ms")]);
    m_progress_ms_isSet = !json[QString("progress_ms")].isNull() && m_progress_ms_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;
}

QString OAICurrentlyPlayingObject::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICurrentlyPlayingObject::asJsonObject() const {
    QJsonObject obj;
    if (m_context.isSet()) {
        obj.insert(QString("context"), ::OpenAPI::toJsonValue(m_context));
    }
    if (m_currently_playing_type_isSet) {
        obj.insert(QString("currently_playing_type"), ::OpenAPI::toJsonValue(m_currently_playing_type));
    }
    if (m_is_playing_isSet) {
        obj.insert(QString("is_playing"), ::OpenAPI::toJsonValue(m_is_playing));
    }
    if (m_item.isSet()) {
        obj.insert(QString("item"), ::OpenAPI::toJsonValue(m_item));
    }
    if (m_progress_ms_isSet) {
        obj.insert(QString("progress_ms"), ::OpenAPI::toJsonValue(m_progress_ms));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    return obj;
}

OAIContextObject OAICurrentlyPlayingObject::getContext() const {
    return m_context;
}
void OAICurrentlyPlayingObject::setContext(const OAIContextObject &context) {
    m_context = context;
    m_context_isSet = true;
}

bool OAICurrentlyPlayingObject::is_context_Set() const{
    return m_context_isSet;
}

bool OAICurrentlyPlayingObject::is_context_Valid() const{
    return m_context_isValid;
}

QString OAICurrentlyPlayingObject::getCurrentlyPlayingType() const {
    return m_currently_playing_type;
}
void OAICurrentlyPlayingObject::setCurrentlyPlayingType(const QString &currently_playing_type) {
    m_currently_playing_type = currently_playing_type;
    m_currently_playing_type_isSet = true;
}

bool OAICurrentlyPlayingObject::is_currently_playing_type_Set() const{
    return m_currently_playing_type_isSet;
}

bool OAICurrentlyPlayingObject::is_currently_playing_type_Valid() const{
    return m_currently_playing_type_isValid;
}

bool OAICurrentlyPlayingObject::isIsPlaying() const {
    return m_is_playing;
}
void OAICurrentlyPlayingObject::setIsPlaying(const bool &is_playing) {
    m_is_playing = is_playing;
    m_is_playing_isSet = true;
}

bool OAICurrentlyPlayingObject::is_is_playing_Set() const{
    return m_is_playing_isSet;
}

bool OAICurrentlyPlayingObject::is_is_playing_Valid() const{
    return m_is_playing_isValid;
}

OAICurrentlyPlayingContextObject_item OAICurrentlyPlayingObject::getItem() const {
    return m_item;
}
void OAICurrentlyPlayingObject::setItem(const OAICurrentlyPlayingContextObject_item &item) {
    m_item = item;
    m_item_isSet = true;
}

bool OAICurrentlyPlayingObject::is_item_Set() const{
    return m_item_isSet;
}

bool OAICurrentlyPlayingObject::is_item_Valid() const{
    return m_item_isValid;
}

qint32 OAICurrentlyPlayingObject::getProgressMs() const {
    return m_progress_ms;
}
void OAICurrentlyPlayingObject::setProgressMs(const qint32 &progress_ms) {
    m_progress_ms = progress_ms;
    m_progress_ms_isSet = true;
}

bool OAICurrentlyPlayingObject::is_progress_ms_Set() const{
    return m_progress_ms_isSet;
}

bool OAICurrentlyPlayingObject::is_progress_ms_Valid() const{
    return m_progress_ms_isValid;
}

qint32 OAICurrentlyPlayingObject::getTimestamp() const {
    return m_timestamp;
}
void OAICurrentlyPlayingObject::setTimestamp(const qint32 &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAICurrentlyPlayingObject::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAICurrentlyPlayingObject::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

bool OAICurrentlyPlayingObject::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_context.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_currently_playing_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_playing_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_item.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_progress_ms_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICurrentlyPlayingObject::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
