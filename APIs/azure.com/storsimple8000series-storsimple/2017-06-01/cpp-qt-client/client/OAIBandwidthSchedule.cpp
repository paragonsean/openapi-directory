/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBandwidthSchedule.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBandwidthSchedule::OAIBandwidthSchedule(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBandwidthSchedule::OAIBandwidthSchedule() {
    this->initializeModel();
}

OAIBandwidthSchedule::~OAIBandwidthSchedule() {}

void OAIBandwidthSchedule::initializeModel() {

    m_days_isSet = false;
    m_days_isValid = false;

    m_rate_in_mbps_isSet = false;
    m_rate_in_mbps_isValid = false;

    m_start_isSet = false;
    m_start_isValid = false;

    m_stop_isSet = false;
    m_stop_isValid = false;
}

void OAIBandwidthSchedule::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBandwidthSchedule::fromJsonObject(QJsonObject json) {

    m_days_isValid = ::OpenAPI::fromJsonValue(m_days, json[QString("days")]);
    m_days_isSet = !json[QString("days")].isNull() && m_days_isValid;

    m_rate_in_mbps_isValid = ::OpenAPI::fromJsonValue(m_rate_in_mbps, json[QString("rateInMbps")]);
    m_rate_in_mbps_isSet = !json[QString("rateInMbps")].isNull() && m_rate_in_mbps_isValid;

    m_start_isValid = ::OpenAPI::fromJsonValue(m_start, json[QString("start")]);
    m_start_isSet = !json[QString("start")].isNull() && m_start_isValid;

    m_stop_isValid = ::OpenAPI::fromJsonValue(m_stop, json[QString("stop")]);
    m_stop_isSet = !json[QString("stop")].isNull() && m_stop_isValid;
}

QString OAIBandwidthSchedule::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBandwidthSchedule::asJsonObject() const {
    QJsonObject obj;
    if (m_days.size() > 0) {
        obj.insert(QString("days"), ::OpenAPI::toJsonValue(m_days));
    }
    if (m_rate_in_mbps_isSet) {
        obj.insert(QString("rateInMbps"), ::OpenAPI::toJsonValue(m_rate_in_mbps));
    }
    if (m_start.isSet()) {
        obj.insert(QString("start"), ::OpenAPI::toJsonValue(m_start));
    }
    if (m_stop.isSet()) {
        obj.insert(QString("stop"), ::OpenAPI::toJsonValue(m_stop));
    }
    return obj;
}

QList<QString> OAIBandwidthSchedule::getDays() const {
    return m_days;
}
void OAIBandwidthSchedule::setDays(const QList<QString> &days) {
    m_days = days;
    m_days_isSet = true;
}

bool OAIBandwidthSchedule::is_days_Set() const{
    return m_days_isSet;
}

bool OAIBandwidthSchedule::is_days_Valid() const{
    return m_days_isValid;
}

qint32 OAIBandwidthSchedule::getRateInMbps() const {
    return m_rate_in_mbps;
}
void OAIBandwidthSchedule::setRateInMbps(const qint32 &rate_in_mbps) {
    m_rate_in_mbps = rate_in_mbps;
    m_rate_in_mbps_isSet = true;
}

bool OAIBandwidthSchedule::is_rate_in_mbps_Set() const{
    return m_rate_in_mbps_isSet;
}

bool OAIBandwidthSchedule::is_rate_in_mbps_Valid() const{
    return m_rate_in_mbps_isValid;
}

OAITime OAIBandwidthSchedule::getStart() const {
    return m_start;
}
void OAIBandwidthSchedule::setStart(const OAITime &start) {
    m_start = start;
    m_start_isSet = true;
}

bool OAIBandwidthSchedule::is_start_Set() const{
    return m_start_isSet;
}

bool OAIBandwidthSchedule::is_start_Valid() const{
    return m_start_isValid;
}

OAITime OAIBandwidthSchedule::getStop() const {
    return m_stop;
}
void OAIBandwidthSchedule::setStop(const OAITime &stop) {
    m_stop = stop;
    m_stop_isSet = true;
}

bool OAIBandwidthSchedule::is_stop_Set() const{
    return m_stop_isSet;
}

bool OAIBandwidthSchedule::is_stop_Valid() const{
    return m_stop_isValid;
}

bool OAIBandwidthSchedule::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_days.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_rate_in_mbps_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_stop.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBandwidthSchedule::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_days_isValid && m_rate_in_mbps_isValid && m_start_isValid && m_stop_isValid && true;
}

} // namespace OpenAPI
