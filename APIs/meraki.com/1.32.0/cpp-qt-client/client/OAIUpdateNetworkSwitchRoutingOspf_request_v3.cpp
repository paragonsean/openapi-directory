/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateNetworkSwitchRoutingOspf_request_v3.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkSwitchRoutingOspf_request_v3::OAIUpdateNetworkSwitchRoutingOspf_request_v3(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkSwitchRoutingOspf_request_v3::OAIUpdateNetworkSwitchRoutingOspf_request_v3() {
    this->initializeModel();
}

OAIUpdateNetworkSwitchRoutingOspf_request_v3::~OAIUpdateNetworkSwitchRoutingOspf_request_v3() {}

void OAIUpdateNetworkSwitchRoutingOspf_request_v3::initializeModel() {

    m_areas_isSet = false;
    m_areas_isValid = false;

    m_dead_timer_in_seconds_isSet = false;
    m_dead_timer_in_seconds_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_hello_timer_in_seconds_isSet = false;
    m_hello_timer_in_seconds_isValid = false;
}

void OAIUpdateNetworkSwitchRoutingOspf_request_v3::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkSwitchRoutingOspf_request_v3::fromJsonObject(QJsonObject json) {

    m_areas_isValid = ::OpenAPI::fromJsonValue(m_areas, json[QString("areas")]);
    m_areas_isSet = !json[QString("areas")].isNull() && m_areas_isValid;

    m_dead_timer_in_seconds_isValid = ::OpenAPI::fromJsonValue(m_dead_timer_in_seconds, json[QString("deadTimerInSeconds")]);
    m_dead_timer_in_seconds_isSet = !json[QString("deadTimerInSeconds")].isNull() && m_dead_timer_in_seconds_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_hello_timer_in_seconds_isValid = ::OpenAPI::fromJsonValue(m_hello_timer_in_seconds, json[QString("helloTimerInSeconds")]);
    m_hello_timer_in_seconds_isSet = !json[QString("helloTimerInSeconds")].isNull() && m_hello_timer_in_seconds_isValid;
}

QString OAIUpdateNetworkSwitchRoutingOspf_request_v3::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkSwitchRoutingOspf_request_v3::asJsonObject() const {
    QJsonObject obj;
    if (m_areas.size() > 0) {
        obj.insert(QString("areas"), ::OpenAPI::toJsonValue(m_areas));
    }
    if (m_dead_timer_in_seconds_isSet) {
        obj.insert(QString("deadTimerInSeconds"), ::OpenAPI::toJsonValue(m_dead_timer_in_seconds));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_hello_timer_in_seconds_isSet) {
        obj.insert(QString("helloTimerInSeconds"), ::OpenAPI::toJsonValue(m_hello_timer_in_seconds));
    }
    return obj;
}

QList<OAIUpdateNetworkSwitchRoutingOspf_request_areas_inner> OAIUpdateNetworkSwitchRoutingOspf_request_v3::getAreas() const {
    return m_areas;
}
void OAIUpdateNetworkSwitchRoutingOspf_request_v3::setAreas(const QList<OAIUpdateNetworkSwitchRoutingOspf_request_areas_inner> &areas) {
    m_areas = areas;
    m_areas_isSet = true;
}

bool OAIUpdateNetworkSwitchRoutingOspf_request_v3::is_areas_Set() const{
    return m_areas_isSet;
}

bool OAIUpdateNetworkSwitchRoutingOspf_request_v3::is_areas_Valid() const{
    return m_areas_isValid;
}

qint32 OAIUpdateNetworkSwitchRoutingOspf_request_v3::getDeadTimerInSeconds() const {
    return m_dead_timer_in_seconds;
}
void OAIUpdateNetworkSwitchRoutingOspf_request_v3::setDeadTimerInSeconds(const qint32 &dead_timer_in_seconds) {
    m_dead_timer_in_seconds = dead_timer_in_seconds;
    m_dead_timer_in_seconds_isSet = true;
}

bool OAIUpdateNetworkSwitchRoutingOspf_request_v3::is_dead_timer_in_seconds_Set() const{
    return m_dead_timer_in_seconds_isSet;
}

bool OAIUpdateNetworkSwitchRoutingOspf_request_v3::is_dead_timer_in_seconds_Valid() const{
    return m_dead_timer_in_seconds_isValid;
}

bool OAIUpdateNetworkSwitchRoutingOspf_request_v3::isEnabled() const {
    return m_enabled;
}
void OAIUpdateNetworkSwitchRoutingOspf_request_v3::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIUpdateNetworkSwitchRoutingOspf_request_v3::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIUpdateNetworkSwitchRoutingOspf_request_v3::is_enabled_Valid() const{
    return m_enabled_isValid;
}

qint32 OAIUpdateNetworkSwitchRoutingOspf_request_v3::getHelloTimerInSeconds() const {
    return m_hello_timer_in_seconds;
}
void OAIUpdateNetworkSwitchRoutingOspf_request_v3::setHelloTimerInSeconds(const qint32 &hello_timer_in_seconds) {
    m_hello_timer_in_seconds = hello_timer_in_seconds;
    m_hello_timer_in_seconds_isSet = true;
}

bool OAIUpdateNetworkSwitchRoutingOspf_request_v3::is_hello_timer_in_seconds_Set() const{
    return m_hello_timer_in_seconds_isSet;
}

bool OAIUpdateNetworkSwitchRoutingOspf_request_v3::is_hello_timer_in_seconds_Valid() const{
    return m_hello_timer_in_seconds_isValid;
}

bool OAIUpdateNetworkSwitchRoutingOspf_request_v3::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_areas.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_dead_timer_in_seconds_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hello_timer_in_seconds_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkSwitchRoutingOspf_request_v3::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
