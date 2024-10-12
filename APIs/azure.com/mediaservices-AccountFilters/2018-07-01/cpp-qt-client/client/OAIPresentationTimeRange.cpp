/**
 * Azure Media Services
 * This Swagger was generated by the API Framework.
 *
 * The version of the OpenAPI document: 2018-07-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPresentationTimeRange.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPresentationTimeRange::OAIPresentationTimeRange(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPresentationTimeRange::OAIPresentationTimeRange() {
    this->initializeModel();
}

OAIPresentationTimeRange::~OAIPresentationTimeRange() {}

void OAIPresentationTimeRange::initializeModel() {

    m_end_timestamp_isSet = false;
    m_end_timestamp_isValid = false;

    m_force_end_timestamp_isSet = false;
    m_force_end_timestamp_isValid = false;

    m_live_backoff_duration_isSet = false;
    m_live_backoff_duration_isValid = false;

    m_presentation_window_duration_isSet = false;
    m_presentation_window_duration_isValid = false;

    m_start_timestamp_isSet = false;
    m_start_timestamp_isValid = false;

    m_timescale_isSet = false;
    m_timescale_isValid = false;
}

void OAIPresentationTimeRange::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPresentationTimeRange::fromJsonObject(QJsonObject json) {

    m_end_timestamp_isValid = ::OpenAPI::fromJsonValue(m_end_timestamp, json[QString("endTimestamp")]);
    m_end_timestamp_isSet = !json[QString("endTimestamp")].isNull() && m_end_timestamp_isValid;

    m_force_end_timestamp_isValid = ::OpenAPI::fromJsonValue(m_force_end_timestamp, json[QString("forceEndTimestamp")]);
    m_force_end_timestamp_isSet = !json[QString("forceEndTimestamp")].isNull() && m_force_end_timestamp_isValid;

    m_live_backoff_duration_isValid = ::OpenAPI::fromJsonValue(m_live_backoff_duration, json[QString("liveBackoffDuration")]);
    m_live_backoff_duration_isSet = !json[QString("liveBackoffDuration")].isNull() && m_live_backoff_duration_isValid;

    m_presentation_window_duration_isValid = ::OpenAPI::fromJsonValue(m_presentation_window_duration, json[QString("presentationWindowDuration")]);
    m_presentation_window_duration_isSet = !json[QString("presentationWindowDuration")].isNull() && m_presentation_window_duration_isValid;

    m_start_timestamp_isValid = ::OpenAPI::fromJsonValue(m_start_timestamp, json[QString("startTimestamp")]);
    m_start_timestamp_isSet = !json[QString("startTimestamp")].isNull() && m_start_timestamp_isValid;

    m_timescale_isValid = ::OpenAPI::fromJsonValue(m_timescale, json[QString("timescale")]);
    m_timescale_isSet = !json[QString("timescale")].isNull() && m_timescale_isValid;
}

QString OAIPresentationTimeRange::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPresentationTimeRange::asJsonObject() const {
    QJsonObject obj;
    if (m_end_timestamp_isSet) {
        obj.insert(QString("endTimestamp"), ::OpenAPI::toJsonValue(m_end_timestamp));
    }
    if (m_force_end_timestamp_isSet) {
        obj.insert(QString("forceEndTimestamp"), ::OpenAPI::toJsonValue(m_force_end_timestamp));
    }
    if (m_live_backoff_duration_isSet) {
        obj.insert(QString("liveBackoffDuration"), ::OpenAPI::toJsonValue(m_live_backoff_duration));
    }
    if (m_presentation_window_duration_isSet) {
        obj.insert(QString("presentationWindowDuration"), ::OpenAPI::toJsonValue(m_presentation_window_duration));
    }
    if (m_start_timestamp_isSet) {
        obj.insert(QString("startTimestamp"), ::OpenAPI::toJsonValue(m_start_timestamp));
    }
    if (m_timescale_isSet) {
        obj.insert(QString("timescale"), ::OpenAPI::toJsonValue(m_timescale));
    }
    return obj;
}

qint64 OAIPresentationTimeRange::getEndTimestamp() const {
    return m_end_timestamp;
}
void OAIPresentationTimeRange::setEndTimestamp(const qint64 &end_timestamp) {
    m_end_timestamp = end_timestamp;
    m_end_timestamp_isSet = true;
}

bool OAIPresentationTimeRange::is_end_timestamp_Set() const{
    return m_end_timestamp_isSet;
}

bool OAIPresentationTimeRange::is_end_timestamp_Valid() const{
    return m_end_timestamp_isValid;
}

bool OAIPresentationTimeRange::isForceEndTimestamp() const {
    return m_force_end_timestamp;
}
void OAIPresentationTimeRange::setForceEndTimestamp(const bool &force_end_timestamp) {
    m_force_end_timestamp = force_end_timestamp;
    m_force_end_timestamp_isSet = true;
}

bool OAIPresentationTimeRange::is_force_end_timestamp_Set() const{
    return m_force_end_timestamp_isSet;
}

bool OAIPresentationTimeRange::is_force_end_timestamp_Valid() const{
    return m_force_end_timestamp_isValid;
}

qint64 OAIPresentationTimeRange::getLiveBackoffDuration() const {
    return m_live_backoff_duration;
}
void OAIPresentationTimeRange::setLiveBackoffDuration(const qint64 &live_backoff_duration) {
    m_live_backoff_duration = live_backoff_duration;
    m_live_backoff_duration_isSet = true;
}

bool OAIPresentationTimeRange::is_live_backoff_duration_Set() const{
    return m_live_backoff_duration_isSet;
}

bool OAIPresentationTimeRange::is_live_backoff_duration_Valid() const{
    return m_live_backoff_duration_isValid;
}

qint64 OAIPresentationTimeRange::getPresentationWindowDuration() const {
    return m_presentation_window_duration;
}
void OAIPresentationTimeRange::setPresentationWindowDuration(const qint64 &presentation_window_duration) {
    m_presentation_window_duration = presentation_window_duration;
    m_presentation_window_duration_isSet = true;
}

bool OAIPresentationTimeRange::is_presentation_window_duration_Set() const{
    return m_presentation_window_duration_isSet;
}

bool OAIPresentationTimeRange::is_presentation_window_duration_Valid() const{
    return m_presentation_window_duration_isValid;
}

qint64 OAIPresentationTimeRange::getStartTimestamp() const {
    return m_start_timestamp;
}
void OAIPresentationTimeRange::setStartTimestamp(const qint64 &start_timestamp) {
    m_start_timestamp = start_timestamp;
    m_start_timestamp_isSet = true;
}

bool OAIPresentationTimeRange::is_start_timestamp_Set() const{
    return m_start_timestamp_isSet;
}

bool OAIPresentationTimeRange::is_start_timestamp_Valid() const{
    return m_start_timestamp_isValid;
}

qint64 OAIPresentationTimeRange::getTimescale() const {
    return m_timescale;
}
void OAIPresentationTimeRange::setTimescale(const qint64 &timescale) {
    m_timescale = timescale;
    m_timescale_isSet = true;
}

bool OAIPresentationTimeRange::is_timescale_Set() const{
    return m_timescale_isSet;
}

bool OAIPresentationTimeRange::is_timescale_Valid() const{
    return m_timescale_isValid;
}

bool OAIPresentationTimeRange::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_end_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_force_end_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_live_backoff_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_presentation_window_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timescale_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPresentationTimeRange::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
