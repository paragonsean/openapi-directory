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

#include "OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket() {
    this->initializeModel();
}

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::~OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket() {}

void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::initializeModel() {

    m_destination_isSet = false;
    m_destination_isValid = false;

    m_ethernet_isSet = false;
    m_ethernet_isValid = false;

    m_fields_isSet = false;
    m_fields_isValid = false;

    m_ip_isSet = false;
    m_ip_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_udp_isSet = false;
    m_udp_isValid = false;
}

void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::fromJsonObject(QJsonObject json) {

    m_destination_isValid = ::OpenAPI::fromJsonValue(m_destination, json[QString("destination")]);
    m_destination_isSet = !json[QString("destination")].isNull() && m_destination_isValid;

    m_ethernet_isValid = ::OpenAPI::fromJsonValue(m_ethernet, json[QString("ethernet")]);
    m_ethernet_isSet = !json[QString("ethernet")].isNull() && m_ethernet_isValid;

    m_fields_isValid = ::OpenAPI::fromJsonValue(m_fields, json[QString("fields")]);
    m_fields_isSet = !json[QString("fields")].isNull() && m_fields_isValid;

    m_ip_isValid = ::OpenAPI::fromJsonValue(m_ip, json[QString("ip")]);
    m_ip_isSet = !json[QString("ip")].isNull() && m_ip_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_udp_isValid = ::OpenAPI::fromJsonValue(m_udp, json[QString("udp")]);
    m_udp_isSet = !json[QString("udp")].isNull() && m_udp_isValid;
}

QString OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::asJsonObject() const {
    QJsonObject obj;
    if (m_destination.isSet()) {
        obj.insert(QString("destination"), ::OpenAPI::toJsonValue(m_destination));
    }
    if (m_ethernet.isSet()) {
        obj.insert(QString("ethernet"), ::OpenAPI::toJsonValue(m_ethernet));
    }
    if (m_fields.isSet()) {
        obj.insert(QString("fields"), ::OpenAPI::toJsonValue(m_fields));
    }
    if (m_ip.isSet()) {
        obj.insert(QString("ip"), ::OpenAPI::toJsonValue(m_ip));
    }
    if (m_source.isSet()) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_udp.isSet()) {
        obj.insert(QString("udp"), ::OpenAPI::toJsonValue(m_udp));
    }
    return obj;
}

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_destination OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::getDestination() const {
    return m_destination;
}
void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::setDestination(const OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_destination &destination) {
    m_destination = destination;
    m_destination_isSet = true;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_destination_Set() const{
    return m_destination_isSet;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_destination_Valid() const{
    return m_destination_isValid;
}

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_ethernet OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::getEthernet() const {
    return m_ethernet;
}
void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::setEthernet(const OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_ethernet &ethernet) {
    m_ethernet = ethernet;
    m_ethernet_isSet = true;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_ethernet_Set() const{
    return m_ethernet_isSet;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_ethernet_Valid() const{
    return m_ethernet_isValid;
}

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_fields OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::getFields() const {
    return m_fields;
}
void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::setFields(const OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_fields &fields) {
    m_fields = fields;
    m_fields_isSet = true;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_fields_Set() const{
    return m_fields_isSet;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_fields_Valid() const{
    return m_fields_isValid;
}

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_ip OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::getIp() const {
    return m_ip;
}
void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::setIp(const OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_ip &ip) {
    m_ip = ip;
    m_ip_isSet = true;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_ip_Set() const{
    return m_ip_isSet;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_ip_Valid() const{
    return m_ip_isValid;
}

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_source OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::getSource() const {
    return m_source;
}
void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::setSource(const OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_source &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_source_Set() const{
    return m_source_isSet;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::getType() const {
    return m_type;
}
void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_type_Set() const{
    return m_type_isSet;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_type_Valid() const{
    return m_type_isValid;
}

OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_udp OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::getUdp() const {
    return m_udp;
}
void OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::setUdp(const OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket_udp &udp) {
    m_udp = udp;
    m_udp_isSet = true;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_udp_Set() const{
    return m_udp_isSet;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::is_udp_Valid() const{
    return m_udp_isValid;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_destination.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ethernet.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_fields.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ip.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_source.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_udp.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetNetworkSwitchDhcpV4ServersSeen_200_response_inner_lastPacket::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
