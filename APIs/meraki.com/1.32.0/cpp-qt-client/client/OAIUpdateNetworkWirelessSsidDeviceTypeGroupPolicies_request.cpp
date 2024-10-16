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

#include "OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request() {
    this->initializeModel();
}

OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::~OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request() {}

void OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::initializeModel() {

    m_device_type_policies_isSet = false;
    m_device_type_policies_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;
}

void OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::fromJsonObject(QJsonObject json) {

    m_device_type_policies_isValid = ::OpenAPI::fromJsonValue(m_device_type_policies, json[QString("deviceTypePolicies")]);
    m_device_type_policies_isSet = !json[QString("deviceTypePolicies")].isNull() && m_device_type_policies_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;
}

QString OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::asJsonObject() const {
    QJsonObject obj;
    if (m_device_type_policies.size() > 0) {
        obj.insert(QString("deviceTypePolicies"), ::OpenAPI::toJsonValue(m_device_type_policies));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    return obj;
}

QList<OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request_deviceTypePolicies_inner> OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::getDeviceTypePolicies() const {
    return m_device_type_policies;
}
void OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::setDeviceTypePolicies(const QList<OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request_deviceTypePolicies_inner> &device_type_policies) {
    m_device_type_policies = device_type_policies;
    m_device_type_policies_isSet = true;
}

bool OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::is_device_type_policies_Set() const{
    return m_device_type_policies_isSet;
}

bool OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::is_device_type_policies_Valid() const{
    return m_device_type_policies_isValid;
}

bool OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::isEnabled() const {
    return m_enabled;
}
void OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::is_enabled_Valid() const{
    return m_enabled_isValid;
}

bool OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_device_type_policies.size() > 0) {
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

bool OAIUpdateNetworkWirelessSsidDeviceTypeGroupPolicies_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
