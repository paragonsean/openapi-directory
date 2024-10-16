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

#include "OAIUpdateNetworkSwitchAlternateManagementInterface_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkSwitchAlternateManagementInterface_request::OAIUpdateNetworkSwitchAlternateManagementInterface_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkSwitchAlternateManagementInterface_request::OAIUpdateNetworkSwitchAlternateManagementInterface_request() {
    this->initializeModel();
}

OAIUpdateNetworkSwitchAlternateManagementInterface_request::~OAIUpdateNetworkSwitchAlternateManagementInterface_request() {}

void OAIUpdateNetworkSwitchAlternateManagementInterface_request::initializeModel() {

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_protocols_isSet = false;
    m_protocols_isValid = false;

    m_switches_isSet = false;
    m_switches_isValid = false;

    m_vlan_id_isSet = false;
    m_vlan_id_isValid = false;
}

void OAIUpdateNetworkSwitchAlternateManagementInterface_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkSwitchAlternateManagementInterface_request::fromJsonObject(QJsonObject json) {

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_protocols_isValid = ::OpenAPI::fromJsonValue(m_protocols, json[QString("protocols")]);
    m_protocols_isSet = !json[QString("protocols")].isNull() && m_protocols_isValid;

    m_switches_isValid = ::OpenAPI::fromJsonValue(m_switches, json[QString("switches")]);
    m_switches_isSet = !json[QString("switches")].isNull() && m_switches_isValid;

    m_vlan_id_isValid = ::OpenAPI::fromJsonValue(m_vlan_id, json[QString("vlanId")]);
    m_vlan_id_isSet = !json[QString("vlanId")].isNull() && m_vlan_id_isValid;
}

QString OAIUpdateNetworkSwitchAlternateManagementInterface_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkSwitchAlternateManagementInterface_request::asJsonObject() const {
    QJsonObject obj;
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_protocols.size() > 0) {
        obj.insert(QString("protocols"), ::OpenAPI::toJsonValue(m_protocols));
    }
    if (m_switches.size() > 0) {
        obj.insert(QString("switches"), ::OpenAPI::toJsonValue(m_switches));
    }
    if (m_vlan_id_isSet) {
        obj.insert(QString("vlanId"), ::OpenAPI::toJsonValue(m_vlan_id));
    }
    return obj;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request::isEnabled() const {
    return m_enabled;
}
void OAIUpdateNetworkSwitchAlternateManagementInterface_request::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request::is_enabled_Valid() const{
    return m_enabled_isValid;
}

QList<QString> OAIUpdateNetworkSwitchAlternateManagementInterface_request::getProtocols() const {
    return m_protocols;
}
void OAIUpdateNetworkSwitchAlternateManagementInterface_request::setProtocols(const QList<QString> &protocols) {
    m_protocols = protocols;
    m_protocols_isSet = true;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request::is_protocols_Set() const{
    return m_protocols_isSet;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request::is_protocols_Valid() const{
    return m_protocols_isValid;
}

QList<OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner> OAIUpdateNetworkSwitchAlternateManagementInterface_request::getSwitches() const {
    return m_switches;
}
void OAIUpdateNetworkSwitchAlternateManagementInterface_request::setSwitches(const QList<OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner> &switches) {
    m_switches = switches;
    m_switches_isSet = true;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request::is_switches_Set() const{
    return m_switches_isSet;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request::is_switches_Valid() const{
    return m_switches_isValid;
}

qint32 OAIUpdateNetworkSwitchAlternateManagementInterface_request::getVlanId() const {
    return m_vlan_id;
}
void OAIUpdateNetworkSwitchAlternateManagementInterface_request::setVlanId(const qint32 &vlan_id) {
    m_vlan_id = vlan_id;
    m_vlan_id_isSet = true;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request::is_vlan_id_Set() const{
    return m_vlan_id_isSet;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request::is_vlan_id_Valid() const{
    return m_vlan_id_isValid;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_protocols.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_switches.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_vlan_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
