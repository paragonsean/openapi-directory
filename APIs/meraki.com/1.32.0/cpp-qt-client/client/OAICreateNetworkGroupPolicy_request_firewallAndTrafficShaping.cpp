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

#include "OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping() {
    this->initializeModel();
}

OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::~OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping() {}

void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::initializeModel() {

    m_l3_firewall_rules_isSet = false;
    m_l3_firewall_rules_isValid = false;

    m_l7_firewall_rules_isSet = false;
    m_l7_firewall_rules_isValid = false;

    m_settings_isSet = false;
    m_settings_isValid = false;

    m_traffic_shaping_rules_isSet = false;
    m_traffic_shaping_rules_isValid = false;
}

void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::fromJsonObject(QJsonObject json) {

    m_l3_firewall_rules_isValid = ::OpenAPI::fromJsonValue(m_l3_firewall_rules, json[QString("l3FirewallRules")]);
    m_l3_firewall_rules_isSet = !json[QString("l3FirewallRules")].isNull() && m_l3_firewall_rules_isValid;

    m_l7_firewall_rules_isValid = ::OpenAPI::fromJsonValue(m_l7_firewall_rules, json[QString("l7FirewallRules")]);
    m_l7_firewall_rules_isSet = !json[QString("l7FirewallRules")].isNull() && m_l7_firewall_rules_isValid;

    m_settings_isValid = ::OpenAPI::fromJsonValue(m_settings, json[QString("settings")]);
    m_settings_isSet = !json[QString("settings")].isNull() && m_settings_isValid;

    m_traffic_shaping_rules_isValid = ::OpenAPI::fromJsonValue(m_traffic_shaping_rules, json[QString("trafficShapingRules")]);
    m_traffic_shaping_rules_isSet = !json[QString("trafficShapingRules")].isNull() && m_traffic_shaping_rules_isValid;
}

QString OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::asJsonObject() const {
    QJsonObject obj;
    if (m_l3_firewall_rules.size() > 0) {
        obj.insert(QString("l3FirewallRules"), ::OpenAPI::toJsonValue(m_l3_firewall_rules));
    }
    if (m_l7_firewall_rules.size() > 0) {
        obj.insert(QString("l7FirewallRules"), ::OpenAPI::toJsonValue(m_l7_firewall_rules));
    }
    if (m_settings_isSet) {
        obj.insert(QString("settings"), ::OpenAPI::toJsonValue(m_settings));
    }
    if (m_traffic_shaping_rules.size() > 0) {
        obj.insert(QString("trafficShapingRules"), ::OpenAPI::toJsonValue(m_traffic_shaping_rules));
    }
    return obj;
}

QList<OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_l3FirewallRules_inner> OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::getL3FirewallRules() const {
    return m_l3_firewall_rules;
}
void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::setL3FirewallRules(const QList<OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_l3FirewallRules_inner> &l3_firewall_rules) {
    m_l3_firewall_rules = l3_firewall_rules;
    m_l3_firewall_rules_isSet = true;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::is_l3_firewall_rules_Set() const{
    return m_l3_firewall_rules_isSet;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::is_l3_firewall_rules_Valid() const{
    return m_l3_firewall_rules_isValid;
}

QList<OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_l7FirewallRules_inner> OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::getL7FirewallRules() const {
    return m_l7_firewall_rules;
}
void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::setL7FirewallRules(const QList<OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_l7FirewallRules_inner> &l7_firewall_rules) {
    m_l7_firewall_rules = l7_firewall_rules;
    m_l7_firewall_rules_isSet = true;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::is_l7_firewall_rules_Set() const{
    return m_l7_firewall_rules_isSet;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::is_l7_firewall_rules_Valid() const{
    return m_l7_firewall_rules_isValid;
}

QString OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::getSettings() const {
    return m_settings;
}
void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::setSettings(const QString &settings) {
    m_settings = settings;
    m_settings_isSet = true;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::is_settings_Set() const{
    return m_settings_isSet;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::is_settings_Valid() const{
    return m_settings_isValid;
}

QList<OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner> OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::getTrafficShapingRules() const {
    return m_traffic_shaping_rules;
}
void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::setTrafficShapingRules(const QList<OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner> &traffic_shaping_rules) {
    m_traffic_shaping_rules = traffic_shaping_rules;
    m_traffic_shaping_rules_isSet = true;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::is_traffic_shaping_rules_Set() const{
    return m_traffic_shaping_rules_isSet;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::is_traffic_shaping_rules_Valid() const{
    return m_traffic_shaping_rules_isValid;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_l3_firewall_rules.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_l7_firewall_rules.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_settings_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_traffic_shaping_rules.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
