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

#include "OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner() {
    this->initializeModel();
}

OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::~OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner() {}

void OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::initializeModel() {

    m_port_rules_isSet = false;
    m_port_rules_isValid = false;

    m_public_ip_isSet = false;
    m_public_ip_isValid = false;

    m_uplink_isSet = false;
    m_uplink_isValid = false;
}

void OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::fromJsonObject(QJsonObject json) {

    m_port_rules_isValid = ::OpenAPI::fromJsonValue(m_port_rules, json[QString("portRules")]);
    m_port_rules_isSet = !json[QString("portRules")].isNull() && m_port_rules_isValid;

    m_public_ip_isValid = ::OpenAPI::fromJsonValue(m_public_ip, json[QString("publicIp")]);
    m_public_ip_isSet = !json[QString("publicIp")].isNull() && m_public_ip_isValid;

    m_uplink_isValid = ::OpenAPI::fromJsonValue(m_uplink, json[QString("uplink")]);
    m_uplink_isSet = !json[QString("uplink")].isNull() && m_uplink_isValid;
}

QString OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_port_rules.size() > 0) {
        obj.insert(QString("portRules"), ::OpenAPI::toJsonValue(m_port_rules));
    }
    if (m_public_ip_isSet) {
        obj.insert(QString("publicIp"), ::OpenAPI::toJsonValue(m_public_ip));
    }
    if (m_uplink_isSet) {
        obj.insert(QString("uplink"), ::OpenAPI::toJsonValue(m_uplink));
    }
    return obj;
}

QList<OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner_portRules_inner> OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::getPortRules() const {
    return m_port_rules;
}
void OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::setPortRules(const QList<OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner_portRules_inner> &port_rules) {
    m_port_rules = port_rules;
    m_port_rules_isSet = true;
}

bool OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::is_port_rules_Set() const{
    return m_port_rules_isSet;
}

bool OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::is_port_rules_Valid() const{
    return m_port_rules_isValid;
}

QString OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::getPublicIp() const {
    return m_public_ip;
}
void OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::setPublicIp(const QString &public_ip) {
    m_public_ip = public_ip;
    m_public_ip_isSet = true;
}

bool OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::is_public_ip_Set() const{
    return m_public_ip_isSet;
}

bool OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::is_public_ip_Valid() const{
    return m_public_ip_isValid;
}

QString OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::getUplink() const {
    return m_uplink;
}
void OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::setUplink(const QString &uplink) {
    m_uplink = uplink;
    m_uplink_isSet = true;
}

bool OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::is_uplink_Set() const{
    return m_uplink_isSet;
}

bool OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::is_uplink_Valid() const{
    return m_uplink_isValid;
}

bool OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_port_rules.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_public_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uplink_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkApplianceFirewallOneToManyNatRules_request_rules_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_port_rules_isValid && m_public_ip_isValid && m_uplink_isValid && true;
}

} // namespace OpenAPI
