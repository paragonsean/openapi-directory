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

#include "OAICreateDeviceSwitchRoutingStaticRoute_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateDeviceSwitchRoutingStaticRoute_request::OAICreateDeviceSwitchRoutingStaticRoute_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateDeviceSwitchRoutingStaticRoute_request::OAICreateDeviceSwitchRoutingStaticRoute_request() {
    this->initializeModel();
}

OAICreateDeviceSwitchRoutingStaticRoute_request::~OAICreateDeviceSwitchRoutingStaticRoute_request() {}

void OAICreateDeviceSwitchRoutingStaticRoute_request::initializeModel() {

    m_advertise_via_ospf_enabled_isSet = false;
    m_advertise_via_ospf_enabled_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_next_hop_ip_isSet = false;
    m_next_hop_ip_isValid = false;

    m_prefer_over_ospf_routes_enabled_isSet = false;
    m_prefer_over_ospf_routes_enabled_isValid = false;

    m_subnet_isSet = false;
    m_subnet_isValid = false;
}

void OAICreateDeviceSwitchRoutingStaticRoute_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateDeviceSwitchRoutingStaticRoute_request::fromJsonObject(QJsonObject json) {

    m_advertise_via_ospf_enabled_isValid = ::OpenAPI::fromJsonValue(m_advertise_via_ospf_enabled, json[QString("advertiseViaOspfEnabled")]);
    m_advertise_via_ospf_enabled_isSet = !json[QString("advertiseViaOspfEnabled")].isNull() && m_advertise_via_ospf_enabled_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_next_hop_ip_isValid = ::OpenAPI::fromJsonValue(m_next_hop_ip, json[QString("nextHopIp")]);
    m_next_hop_ip_isSet = !json[QString("nextHopIp")].isNull() && m_next_hop_ip_isValid;

    m_prefer_over_ospf_routes_enabled_isValid = ::OpenAPI::fromJsonValue(m_prefer_over_ospf_routes_enabled, json[QString("preferOverOspfRoutesEnabled")]);
    m_prefer_over_ospf_routes_enabled_isSet = !json[QString("preferOverOspfRoutesEnabled")].isNull() && m_prefer_over_ospf_routes_enabled_isValid;

    m_subnet_isValid = ::OpenAPI::fromJsonValue(m_subnet, json[QString("subnet")]);
    m_subnet_isSet = !json[QString("subnet")].isNull() && m_subnet_isValid;
}

QString OAICreateDeviceSwitchRoutingStaticRoute_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateDeviceSwitchRoutingStaticRoute_request::asJsonObject() const {
    QJsonObject obj;
    if (m_advertise_via_ospf_enabled_isSet) {
        obj.insert(QString("advertiseViaOspfEnabled"), ::OpenAPI::toJsonValue(m_advertise_via_ospf_enabled));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_next_hop_ip_isSet) {
        obj.insert(QString("nextHopIp"), ::OpenAPI::toJsonValue(m_next_hop_ip));
    }
    if (m_prefer_over_ospf_routes_enabled_isSet) {
        obj.insert(QString("preferOverOspfRoutesEnabled"), ::OpenAPI::toJsonValue(m_prefer_over_ospf_routes_enabled));
    }
    if (m_subnet_isSet) {
        obj.insert(QString("subnet"), ::OpenAPI::toJsonValue(m_subnet));
    }
    return obj;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::isAdvertiseViaOspfEnabled() const {
    return m_advertise_via_ospf_enabled;
}
void OAICreateDeviceSwitchRoutingStaticRoute_request::setAdvertiseViaOspfEnabled(const bool &advertise_via_ospf_enabled) {
    m_advertise_via_ospf_enabled = advertise_via_ospf_enabled;
    m_advertise_via_ospf_enabled_isSet = true;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::is_advertise_via_ospf_enabled_Set() const{
    return m_advertise_via_ospf_enabled_isSet;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::is_advertise_via_ospf_enabled_Valid() const{
    return m_advertise_via_ospf_enabled_isValid;
}

QString OAICreateDeviceSwitchRoutingStaticRoute_request::getName() const {
    return m_name;
}
void OAICreateDeviceSwitchRoutingStaticRoute_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICreateDeviceSwitchRoutingStaticRoute_request::getNextHopIp() const {
    return m_next_hop_ip;
}
void OAICreateDeviceSwitchRoutingStaticRoute_request::setNextHopIp(const QString &next_hop_ip) {
    m_next_hop_ip = next_hop_ip;
    m_next_hop_ip_isSet = true;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::is_next_hop_ip_Set() const{
    return m_next_hop_ip_isSet;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::is_next_hop_ip_Valid() const{
    return m_next_hop_ip_isValid;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::isPreferOverOspfRoutesEnabled() const {
    return m_prefer_over_ospf_routes_enabled;
}
void OAICreateDeviceSwitchRoutingStaticRoute_request::setPreferOverOspfRoutesEnabled(const bool &prefer_over_ospf_routes_enabled) {
    m_prefer_over_ospf_routes_enabled = prefer_over_ospf_routes_enabled;
    m_prefer_over_ospf_routes_enabled_isSet = true;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::is_prefer_over_ospf_routes_enabled_Set() const{
    return m_prefer_over_ospf_routes_enabled_isSet;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::is_prefer_over_ospf_routes_enabled_Valid() const{
    return m_prefer_over_ospf_routes_enabled_isValid;
}

QString OAICreateDeviceSwitchRoutingStaticRoute_request::getSubnet() const {
    return m_subnet;
}
void OAICreateDeviceSwitchRoutingStaticRoute_request::setSubnet(const QString &subnet) {
    m_subnet = subnet;
    m_subnet_isSet = true;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::is_subnet_Set() const{
    return m_subnet_isSet;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::is_subnet_Valid() const{
    return m_subnet_isValid;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_advertise_via_ospf_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_hop_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_prefer_over_ospf_routes_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subnet_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateDeviceSwitchRoutingStaticRoute_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_next_hop_ip_isValid && m_subnet_isValid && true;
}

} // namespace OpenAPI
