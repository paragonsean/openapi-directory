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

#include "OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort() {
    this->initializeModel();
}

OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::~OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort() {}

void OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_authentication_status_isSet = false;
    m_authentication_status_isValid = false;

    m_config_overrides_isSet = false;
    m_config_overrides_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;
}

void OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("active")]);
    m_active_isSet = !json[QString("active")].isNull() && m_active_isValid;

    m_authentication_status_isValid = ::OpenAPI::fromJsonValue(m_authentication_status, json[QString("authenticationStatus")]);
    m_authentication_status_isSet = !json[QString("authenticationStatus")].isNull() && m_authentication_status_isValid;

    m_config_overrides_isValid = ::OpenAPI::fromJsonValue(m_config_overrides, json[QString("configOverrides")]);
    m_config_overrides_isSet = !json[QString("configOverrides")].isNull() && m_config_overrides_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;
}

QString OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_authentication_status_isSet) {
        obj.insert(QString("authenticationStatus"), ::OpenAPI::toJsonValue(m_authentication_status));
    }
    if (m_config_overrides.isSet()) {
        obj.insert(QString("configOverrides"), ::OpenAPI::toJsonValue(m_config_overrides));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    return obj;
}

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::isActive() const {
    return m_active;
}
void OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::is_active_Set() const{
    return m_active_isSet;
}

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::is_active_Valid() const{
    return m_active_isValid;
}

QString OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::getAuthenticationStatus() const {
    return m_authentication_status;
}
void OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::setAuthenticationStatus(const QString &authentication_status) {
    m_authentication_status = authentication_status;
    m_authentication_status_isSet = true;
}

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::is_authentication_status_Set() const{
    return m_authentication_status_isSet;
}

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::is_authentication_status_Valid() const{
    return m_authentication_status_isValid;
}

OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort_configOverrides OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::getConfigOverrides() const {
    return m_config_overrides;
}
void OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::setConfigOverrides(const OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort_configOverrides &config_overrides) {
    m_config_overrides = config_overrides;
    m_config_overrides_isSet = true;
}

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::is_config_overrides_Set() const{
    return m_config_overrides_isSet;
}

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::is_config_overrides_Valid() const{
    return m_config_overrides_isValid;
}

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::isEnabled() const {
    return m_enabled;
}
void OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::is_enabled_Valid() const{
    return m_enabled_isValid;
}

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_authentication_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_config_overrides.isSet()) {
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

bool OAIGetDeviceSwitchPortsStatuses_200_response_inner_securePort::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
