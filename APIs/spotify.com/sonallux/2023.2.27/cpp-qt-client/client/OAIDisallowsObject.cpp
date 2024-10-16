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

#include "OAIDisallowsObject.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDisallowsObject::OAIDisallowsObject(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDisallowsObject::OAIDisallowsObject() {
    this->initializeModel();
}

OAIDisallowsObject::~OAIDisallowsObject() {}

void OAIDisallowsObject::initializeModel() {

    m_interrupting_playback_isSet = false;
    m_interrupting_playback_isValid = false;

    m_pausing_isSet = false;
    m_pausing_isValid = false;

    m_resuming_isSet = false;
    m_resuming_isValid = false;

    m_seeking_isSet = false;
    m_seeking_isValid = false;

    m_skipping_next_isSet = false;
    m_skipping_next_isValid = false;

    m_skipping_prev_isSet = false;
    m_skipping_prev_isValid = false;

    m_toggling_repeat_context_isSet = false;
    m_toggling_repeat_context_isValid = false;

    m_toggling_repeat_track_isSet = false;
    m_toggling_repeat_track_isValid = false;

    m_toggling_shuffle_isSet = false;
    m_toggling_shuffle_isValid = false;

    m_transferring_playback_isSet = false;
    m_transferring_playback_isValid = false;
}

void OAIDisallowsObject::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDisallowsObject::fromJsonObject(QJsonObject json) {

    m_interrupting_playback_isValid = ::OpenAPI::fromJsonValue(m_interrupting_playback, json[QString("interrupting_playback")]);
    m_interrupting_playback_isSet = !json[QString("interrupting_playback")].isNull() && m_interrupting_playback_isValid;

    m_pausing_isValid = ::OpenAPI::fromJsonValue(m_pausing, json[QString("pausing")]);
    m_pausing_isSet = !json[QString("pausing")].isNull() && m_pausing_isValid;

    m_resuming_isValid = ::OpenAPI::fromJsonValue(m_resuming, json[QString("resuming")]);
    m_resuming_isSet = !json[QString("resuming")].isNull() && m_resuming_isValid;

    m_seeking_isValid = ::OpenAPI::fromJsonValue(m_seeking, json[QString("seeking")]);
    m_seeking_isSet = !json[QString("seeking")].isNull() && m_seeking_isValid;

    m_skipping_next_isValid = ::OpenAPI::fromJsonValue(m_skipping_next, json[QString("skipping_next")]);
    m_skipping_next_isSet = !json[QString("skipping_next")].isNull() && m_skipping_next_isValid;

    m_skipping_prev_isValid = ::OpenAPI::fromJsonValue(m_skipping_prev, json[QString("skipping_prev")]);
    m_skipping_prev_isSet = !json[QString("skipping_prev")].isNull() && m_skipping_prev_isValid;

    m_toggling_repeat_context_isValid = ::OpenAPI::fromJsonValue(m_toggling_repeat_context, json[QString("toggling_repeat_context")]);
    m_toggling_repeat_context_isSet = !json[QString("toggling_repeat_context")].isNull() && m_toggling_repeat_context_isValid;

    m_toggling_repeat_track_isValid = ::OpenAPI::fromJsonValue(m_toggling_repeat_track, json[QString("toggling_repeat_track")]);
    m_toggling_repeat_track_isSet = !json[QString("toggling_repeat_track")].isNull() && m_toggling_repeat_track_isValid;

    m_toggling_shuffle_isValid = ::OpenAPI::fromJsonValue(m_toggling_shuffle, json[QString("toggling_shuffle")]);
    m_toggling_shuffle_isSet = !json[QString("toggling_shuffle")].isNull() && m_toggling_shuffle_isValid;

    m_transferring_playback_isValid = ::OpenAPI::fromJsonValue(m_transferring_playback, json[QString("transferring_playback")]);
    m_transferring_playback_isSet = !json[QString("transferring_playback")].isNull() && m_transferring_playback_isValid;
}

QString OAIDisallowsObject::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDisallowsObject::asJsonObject() const {
    QJsonObject obj;
    if (m_interrupting_playback_isSet) {
        obj.insert(QString("interrupting_playback"), ::OpenAPI::toJsonValue(m_interrupting_playback));
    }
    if (m_pausing_isSet) {
        obj.insert(QString("pausing"), ::OpenAPI::toJsonValue(m_pausing));
    }
    if (m_resuming_isSet) {
        obj.insert(QString("resuming"), ::OpenAPI::toJsonValue(m_resuming));
    }
    if (m_seeking_isSet) {
        obj.insert(QString("seeking"), ::OpenAPI::toJsonValue(m_seeking));
    }
    if (m_skipping_next_isSet) {
        obj.insert(QString("skipping_next"), ::OpenAPI::toJsonValue(m_skipping_next));
    }
    if (m_skipping_prev_isSet) {
        obj.insert(QString("skipping_prev"), ::OpenAPI::toJsonValue(m_skipping_prev));
    }
    if (m_toggling_repeat_context_isSet) {
        obj.insert(QString("toggling_repeat_context"), ::OpenAPI::toJsonValue(m_toggling_repeat_context));
    }
    if (m_toggling_repeat_track_isSet) {
        obj.insert(QString("toggling_repeat_track"), ::OpenAPI::toJsonValue(m_toggling_repeat_track));
    }
    if (m_toggling_shuffle_isSet) {
        obj.insert(QString("toggling_shuffle"), ::OpenAPI::toJsonValue(m_toggling_shuffle));
    }
    if (m_transferring_playback_isSet) {
        obj.insert(QString("transferring_playback"), ::OpenAPI::toJsonValue(m_transferring_playback));
    }
    return obj;
}

bool OAIDisallowsObject::isInterruptingPlayback() const {
    return m_interrupting_playback;
}
void OAIDisallowsObject::setInterruptingPlayback(const bool &interrupting_playback) {
    m_interrupting_playback = interrupting_playback;
    m_interrupting_playback_isSet = true;
}

bool OAIDisallowsObject::is_interrupting_playback_Set() const{
    return m_interrupting_playback_isSet;
}

bool OAIDisallowsObject::is_interrupting_playback_Valid() const{
    return m_interrupting_playback_isValid;
}

bool OAIDisallowsObject::isPausing() const {
    return m_pausing;
}
void OAIDisallowsObject::setPausing(const bool &pausing) {
    m_pausing = pausing;
    m_pausing_isSet = true;
}

bool OAIDisallowsObject::is_pausing_Set() const{
    return m_pausing_isSet;
}

bool OAIDisallowsObject::is_pausing_Valid() const{
    return m_pausing_isValid;
}

bool OAIDisallowsObject::isResuming() const {
    return m_resuming;
}
void OAIDisallowsObject::setResuming(const bool &resuming) {
    m_resuming = resuming;
    m_resuming_isSet = true;
}

bool OAIDisallowsObject::is_resuming_Set() const{
    return m_resuming_isSet;
}

bool OAIDisallowsObject::is_resuming_Valid() const{
    return m_resuming_isValid;
}

bool OAIDisallowsObject::isSeeking() const {
    return m_seeking;
}
void OAIDisallowsObject::setSeeking(const bool &seeking) {
    m_seeking = seeking;
    m_seeking_isSet = true;
}

bool OAIDisallowsObject::is_seeking_Set() const{
    return m_seeking_isSet;
}

bool OAIDisallowsObject::is_seeking_Valid() const{
    return m_seeking_isValid;
}

bool OAIDisallowsObject::isSkippingNext() const {
    return m_skipping_next;
}
void OAIDisallowsObject::setSkippingNext(const bool &skipping_next) {
    m_skipping_next = skipping_next;
    m_skipping_next_isSet = true;
}

bool OAIDisallowsObject::is_skipping_next_Set() const{
    return m_skipping_next_isSet;
}

bool OAIDisallowsObject::is_skipping_next_Valid() const{
    return m_skipping_next_isValid;
}

bool OAIDisallowsObject::isSkippingPrev() const {
    return m_skipping_prev;
}
void OAIDisallowsObject::setSkippingPrev(const bool &skipping_prev) {
    m_skipping_prev = skipping_prev;
    m_skipping_prev_isSet = true;
}

bool OAIDisallowsObject::is_skipping_prev_Set() const{
    return m_skipping_prev_isSet;
}

bool OAIDisallowsObject::is_skipping_prev_Valid() const{
    return m_skipping_prev_isValid;
}

bool OAIDisallowsObject::isTogglingRepeatContext() const {
    return m_toggling_repeat_context;
}
void OAIDisallowsObject::setTogglingRepeatContext(const bool &toggling_repeat_context) {
    m_toggling_repeat_context = toggling_repeat_context;
    m_toggling_repeat_context_isSet = true;
}

bool OAIDisallowsObject::is_toggling_repeat_context_Set() const{
    return m_toggling_repeat_context_isSet;
}

bool OAIDisallowsObject::is_toggling_repeat_context_Valid() const{
    return m_toggling_repeat_context_isValid;
}

bool OAIDisallowsObject::isTogglingRepeatTrack() const {
    return m_toggling_repeat_track;
}
void OAIDisallowsObject::setTogglingRepeatTrack(const bool &toggling_repeat_track) {
    m_toggling_repeat_track = toggling_repeat_track;
    m_toggling_repeat_track_isSet = true;
}

bool OAIDisallowsObject::is_toggling_repeat_track_Set() const{
    return m_toggling_repeat_track_isSet;
}

bool OAIDisallowsObject::is_toggling_repeat_track_Valid() const{
    return m_toggling_repeat_track_isValid;
}

bool OAIDisallowsObject::isTogglingShuffle() const {
    return m_toggling_shuffle;
}
void OAIDisallowsObject::setTogglingShuffle(const bool &toggling_shuffle) {
    m_toggling_shuffle = toggling_shuffle;
    m_toggling_shuffle_isSet = true;
}

bool OAIDisallowsObject::is_toggling_shuffle_Set() const{
    return m_toggling_shuffle_isSet;
}

bool OAIDisallowsObject::is_toggling_shuffle_Valid() const{
    return m_toggling_shuffle_isValid;
}

bool OAIDisallowsObject::isTransferringPlayback() const {
    return m_transferring_playback;
}
void OAIDisallowsObject::setTransferringPlayback(const bool &transferring_playback) {
    m_transferring_playback = transferring_playback;
    m_transferring_playback_isSet = true;
}

bool OAIDisallowsObject::is_transferring_playback_Set() const{
    return m_transferring_playback_isSet;
}

bool OAIDisallowsObject::is_transferring_playback_Valid() const{
    return m_transferring_playback_isValid;
}

bool OAIDisallowsObject::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_interrupting_playback_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pausing_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_resuming_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seeking_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_skipping_next_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_skipping_prev_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_toggling_repeat_context_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_toggling_repeat_track_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_toggling_shuffle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transferring_playback_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDisallowsObject::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
