/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEventDeviceCount.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEventDeviceCount::OAIEventDeviceCount(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEventDeviceCount::OAIEventDeviceCount() {
    this->initializeModel();
}

OAIEventDeviceCount::~OAIEventDeviceCount() {}

void OAIEventDeviceCount::initializeModel() {

    m_devices_count_isSet = false;
    m_devices_count_isValid = false;

    m_previous_total_devices_with_event_isSet = false;
    m_previous_total_devices_with_event_isValid = false;

    m_total_devices_isSet = false;
    m_total_devices_isValid = false;

    m_total_devices_with_event_isSet = false;
    m_total_devices_with_event_isValid = false;
}

void OAIEventDeviceCount::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEventDeviceCount::fromJsonObject(QJsonObject json) {

    m_devices_count_isValid = ::OpenAPI::fromJsonValue(m_devices_count, json[QString("devices_count")]);
    m_devices_count_isSet = !json[QString("devices_count")].isNull() && m_devices_count_isValid;

    m_previous_total_devices_with_event_isValid = ::OpenAPI::fromJsonValue(m_previous_total_devices_with_event, json[QString("previous_total_devices_with_event")]);
    m_previous_total_devices_with_event_isSet = !json[QString("previous_total_devices_with_event")].isNull() && m_previous_total_devices_with_event_isValid;

    m_total_devices_isValid = ::OpenAPI::fromJsonValue(m_total_devices, json[QString("total_devices")]);
    m_total_devices_isSet = !json[QString("total_devices")].isNull() && m_total_devices_isValid;

    m_total_devices_with_event_isValid = ::OpenAPI::fromJsonValue(m_total_devices_with_event, json[QString("total_devices_with_event")]);
    m_total_devices_with_event_isSet = !json[QString("total_devices_with_event")].isNull() && m_total_devices_with_event_isValid;
}

QString OAIEventDeviceCount::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEventDeviceCount::asJsonObject() const {
    QJsonObject obj;
    if (m_devices_count.size() > 0) {
        obj.insert(QString("devices_count"), ::OpenAPI::toJsonValue(m_devices_count));
    }
    if (m_previous_total_devices_with_event_isSet) {
        obj.insert(QString("previous_total_devices_with_event"), ::OpenAPI::toJsonValue(m_previous_total_devices_with_event));
    }
    if (m_total_devices_isSet) {
        obj.insert(QString("total_devices"), ::OpenAPI::toJsonValue(m_total_devices));
    }
    if (m_total_devices_with_event_isSet) {
        obj.insert(QString("total_devices_with_event"), ::OpenAPI::toJsonValue(m_total_devices_with_event));
    }
    return obj;
}

QList<OAIAnalytics_DeviceCounts_200_response_daily_inner> OAIEventDeviceCount::getDevicesCount() const {
    return m_devices_count;
}
void OAIEventDeviceCount::setDevicesCount(const QList<OAIAnalytics_DeviceCounts_200_response_daily_inner> &devices_count) {
    m_devices_count = devices_count;
    m_devices_count_isSet = true;
}

bool OAIEventDeviceCount::is_devices_count_Set() const{
    return m_devices_count_isSet;
}

bool OAIEventDeviceCount::is_devices_count_Valid() const{
    return m_devices_count_isValid;
}

qint64 OAIEventDeviceCount::getPreviousTotalDevicesWithEvent() const {
    return m_previous_total_devices_with_event;
}
void OAIEventDeviceCount::setPreviousTotalDevicesWithEvent(const qint64 &previous_total_devices_with_event) {
    m_previous_total_devices_with_event = previous_total_devices_with_event;
    m_previous_total_devices_with_event_isSet = true;
}

bool OAIEventDeviceCount::is_previous_total_devices_with_event_Set() const{
    return m_previous_total_devices_with_event_isSet;
}

bool OAIEventDeviceCount::is_previous_total_devices_with_event_Valid() const{
    return m_previous_total_devices_with_event_isValid;
}

qint64 OAIEventDeviceCount::getTotalDevices() const {
    return m_total_devices;
}
void OAIEventDeviceCount::setTotalDevices(const qint64 &total_devices) {
    m_total_devices = total_devices;
    m_total_devices_isSet = true;
}

bool OAIEventDeviceCount::is_total_devices_Set() const{
    return m_total_devices_isSet;
}

bool OAIEventDeviceCount::is_total_devices_Valid() const{
    return m_total_devices_isValid;
}

qint64 OAIEventDeviceCount::getTotalDevicesWithEvent() const {
    return m_total_devices_with_event;
}
void OAIEventDeviceCount::setTotalDevicesWithEvent(const qint64 &total_devices_with_event) {
    m_total_devices_with_event = total_devices_with_event;
    m_total_devices_with_event_isSet = true;
}

bool OAIEventDeviceCount::is_total_devices_with_event_Set() const{
    return m_total_devices_with_event_isSet;
}

bool OAIEventDeviceCount::is_total_devices_with_event_Valid() const{
    return m_total_devices_with_event_isValid;
}

bool OAIEventDeviceCount::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_devices_count.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_previous_total_devices_with_event_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_devices_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_devices_with_event_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEventDeviceCount::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
