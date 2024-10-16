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

#include "OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication() {
    this->initializeModel();
}

OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::~OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication() {}

void OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::initializeModel() {

    m_enabled_isSet = false;
    m_enabled_isValid = false;
}

void OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::fromJsonObject(QJsonObject json) {

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;
}

QString OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::asJsonObject() const {
    QJsonObject obj;
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    return obj;
}

bool OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::isEnabled() const {
    return m_enabled;
}
void OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::is_enabled_Valid() const{
    return m_enabled_isValid;
}

bool OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkApplianceSsid_request_dhcpEnforcedDeauthentication::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
