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

#include "OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4() {
    this->initializeModel();
}

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::~OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4() {}

void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_gateway_isSet = false;
    m_gateway_isValid = false;

    m_subnet_isSet = false;
    m_subnet_isValid = false;
}

void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_gateway_isValid = ::OpenAPI::fromJsonValue(m_gateway, json[QString("gateway")]);
    m_gateway_isSet = !json[QString("gateway")].isNull() && m_gateway_isValid;

    m_subnet_isValid = ::OpenAPI::fromJsonValue(m_subnet, json[QString("subnet")]);
    m_subnet_isSet = !json[QString("subnet")].isNull() && m_subnet_isValid;
}

QString OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::asJsonObject() const {
    QJsonObject obj;
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_gateway_isSet) {
        obj.insert(QString("gateway"), ::OpenAPI::toJsonValue(m_gateway));
    }
    if (m_subnet_isSet) {
        obj.insert(QString("subnet"), ::OpenAPI::toJsonValue(m_subnet));
    }
    return obj;
}

QString OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::getAddress() const {
    return m_address;
}
void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::is_address_Set() const{
    return m_address_isSet;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::is_address_Valid() const{
    return m_address_isValid;
}

QString OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::getGateway() const {
    return m_gateway;
}
void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::setGateway(const QString &gateway) {
    m_gateway = gateway;
    m_gateway_isSet = true;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::is_gateway_Set() const{
    return m_gateway_isSet;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::is_gateway_Valid() const{
    return m_gateway_isValid;
}

QString OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::getSubnet() const {
    return m_subnet;
}
void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::setSubnet(const QString &subnet) {
    m_subnet = subnet;
    m_subnet_isSet = true;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::is_subnet_Set() const{
    return m_subnet_isSet;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::is_subnet_Valid() const{
    return m_subnet_isValid;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gateway_isSet) {
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

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_ipv4::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
