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

#include "OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess() {
    this->initializeModel();
}

OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::~OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess() {}

void OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::initializeModel() {

    m_duration_in_minutes_isSet = false;
    m_duration_in_minutes_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;
}

void OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::fromJsonObject(QJsonObject json) {

    m_duration_in_minutes_isValid = ::OpenAPI::fromJsonValue(m_duration_in_minutes, json[QString("durationInMinutes")]);
    m_duration_in_minutes_isSet = !json[QString("durationInMinutes")].isNull() && m_duration_in_minutes_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;
}

QString OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::asJsonObject() const {
    QJsonObject obj;
    if (m_duration_in_minutes_isSet) {
        obj.insert(QString("durationInMinutes"), ::OpenAPI::toJsonValue(m_duration_in_minutes));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    return obj;
}

qint32 OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::getDurationInMinutes() const {
    return m_duration_in_minutes;
}
void OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::setDurationInMinutes(const qint32 &duration_in_minutes) {
    m_duration_in_minutes = duration_in_minutes;
    m_duration_in_minutes_isSet = true;
}

bool OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::is_duration_in_minutes_Set() const{
    return m_duration_in_minutes_isSet;
}

bool OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::is_duration_in_minutes_Valid() const{
    return m_duration_in_minutes_isValid;
}

bool OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::isEnabled() const {
    return m_enabled;
}
void OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::is_enabled_Valid() const{
    return m_enabled_isValid;
}

bool OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_duration_in_minutes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkWirelessSsidSplashSettings_request_billing_freeAccess::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
