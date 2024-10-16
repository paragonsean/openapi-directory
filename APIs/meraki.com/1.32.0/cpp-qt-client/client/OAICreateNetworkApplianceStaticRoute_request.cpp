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

#include "OAICreateNetworkApplianceStaticRoute_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateNetworkApplianceStaticRoute_request::OAICreateNetworkApplianceStaticRoute_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateNetworkApplianceStaticRoute_request::OAICreateNetworkApplianceStaticRoute_request() {
    this->initializeModel();
}

OAICreateNetworkApplianceStaticRoute_request::~OAICreateNetworkApplianceStaticRoute_request() {}

void OAICreateNetworkApplianceStaticRoute_request::initializeModel() {

    m_gateway_ip_isSet = false;
    m_gateway_ip_isValid = false;

    m_gateway_vlan_id_isSet = false;
    m_gateway_vlan_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_subnet_isSet = false;
    m_subnet_isValid = false;
}

void OAICreateNetworkApplianceStaticRoute_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateNetworkApplianceStaticRoute_request::fromJsonObject(QJsonObject json) {

    m_gateway_ip_isValid = ::OpenAPI::fromJsonValue(m_gateway_ip, json[QString("gatewayIp")]);
    m_gateway_ip_isSet = !json[QString("gatewayIp")].isNull() && m_gateway_ip_isValid;

    m_gateway_vlan_id_isValid = ::OpenAPI::fromJsonValue(m_gateway_vlan_id, json[QString("gatewayVlanId")]);
    m_gateway_vlan_id_isSet = !json[QString("gatewayVlanId")].isNull() && m_gateway_vlan_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_subnet_isValid = ::OpenAPI::fromJsonValue(m_subnet, json[QString("subnet")]);
    m_subnet_isSet = !json[QString("subnet")].isNull() && m_subnet_isValid;
}

QString OAICreateNetworkApplianceStaticRoute_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateNetworkApplianceStaticRoute_request::asJsonObject() const {
    QJsonObject obj;
    if (m_gateway_ip_isSet) {
        obj.insert(QString("gatewayIp"), ::OpenAPI::toJsonValue(m_gateway_ip));
    }
    if (m_gateway_vlan_id_isSet) {
        obj.insert(QString("gatewayVlanId"), ::OpenAPI::toJsonValue(m_gateway_vlan_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_subnet_isSet) {
        obj.insert(QString("subnet"), ::OpenAPI::toJsonValue(m_subnet));
    }
    return obj;
}

QString OAICreateNetworkApplianceStaticRoute_request::getGatewayIp() const {
    return m_gateway_ip;
}
void OAICreateNetworkApplianceStaticRoute_request::setGatewayIp(const QString &gateway_ip) {
    m_gateway_ip = gateway_ip;
    m_gateway_ip_isSet = true;
}

bool OAICreateNetworkApplianceStaticRoute_request::is_gateway_ip_Set() const{
    return m_gateway_ip_isSet;
}

bool OAICreateNetworkApplianceStaticRoute_request::is_gateway_ip_Valid() const{
    return m_gateway_ip_isValid;
}

QString OAICreateNetworkApplianceStaticRoute_request::getGatewayVlanId() const {
    return m_gateway_vlan_id;
}
void OAICreateNetworkApplianceStaticRoute_request::setGatewayVlanId(const QString &gateway_vlan_id) {
    m_gateway_vlan_id = gateway_vlan_id;
    m_gateway_vlan_id_isSet = true;
}

bool OAICreateNetworkApplianceStaticRoute_request::is_gateway_vlan_id_Set() const{
    return m_gateway_vlan_id_isSet;
}

bool OAICreateNetworkApplianceStaticRoute_request::is_gateway_vlan_id_Valid() const{
    return m_gateway_vlan_id_isValid;
}

QString OAICreateNetworkApplianceStaticRoute_request::getName() const {
    return m_name;
}
void OAICreateNetworkApplianceStaticRoute_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICreateNetworkApplianceStaticRoute_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAICreateNetworkApplianceStaticRoute_request::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICreateNetworkApplianceStaticRoute_request::getSubnet() const {
    return m_subnet;
}
void OAICreateNetworkApplianceStaticRoute_request::setSubnet(const QString &subnet) {
    m_subnet = subnet;
    m_subnet_isSet = true;
}

bool OAICreateNetworkApplianceStaticRoute_request::is_subnet_Set() const{
    return m_subnet_isSet;
}

bool OAICreateNetworkApplianceStaticRoute_request::is_subnet_Valid() const{
    return m_subnet_isValid;
}

bool OAICreateNetworkApplianceStaticRoute_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_gateway_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gateway_vlan_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
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

bool OAICreateNetworkApplianceStaticRoute_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_gateway_ip_isValid && m_name_isValid && m_subnet_isValid && true;
}

} // namespace OpenAPI
