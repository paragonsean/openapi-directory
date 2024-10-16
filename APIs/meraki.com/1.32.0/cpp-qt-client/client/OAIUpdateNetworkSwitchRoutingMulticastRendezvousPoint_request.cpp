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

#include "OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request() {
    this->initializeModel();
}

OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::~OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request() {}

void OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::initializeModel() {

    m_interface_ip_isSet = false;
    m_interface_ip_isValid = false;

    m_multicast_group_isSet = false;
    m_multicast_group_isValid = false;
}

void OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::fromJsonObject(QJsonObject json) {

    m_interface_ip_isValid = ::OpenAPI::fromJsonValue(m_interface_ip, json[QString("interfaceIp")]);
    m_interface_ip_isSet = !json[QString("interfaceIp")].isNull() && m_interface_ip_isValid;

    m_multicast_group_isValid = ::OpenAPI::fromJsonValue(m_multicast_group, json[QString("multicastGroup")]);
    m_multicast_group_isSet = !json[QString("multicastGroup")].isNull() && m_multicast_group_isValid;
}

QString OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::asJsonObject() const {
    QJsonObject obj;
    if (m_interface_ip_isSet) {
        obj.insert(QString("interfaceIp"), ::OpenAPI::toJsonValue(m_interface_ip));
    }
    if (m_multicast_group_isSet) {
        obj.insert(QString("multicastGroup"), ::OpenAPI::toJsonValue(m_multicast_group));
    }
    return obj;
}

QString OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::getInterfaceIp() const {
    return m_interface_ip;
}
void OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::setInterfaceIp(const QString &interface_ip) {
    m_interface_ip = interface_ip;
    m_interface_ip_isSet = true;
}

bool OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::is_interface_ip_Set() const{
    return m_interface_ip_isSet;
}

bool OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::is_interface_ip_Valid() const{
    return m_interface_ip_isValid;
}

QString OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::getMulticastGroup() const {
    return m_multicast_group;
}
void OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::setMulticastGroup(const QString &multicast_group) {
    m_multicast_group = multicast_group;
    m_multicast_group_isSet = true;
}

bool OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::is_multicast_group_Set() const{
    return m_multicast_group_isSet;
}

bool OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::is_multicast_group_Valid() const{
    return m_multicast_group_isValid;
}

bool OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_interface_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_multicast_group_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkSwitchRoutingMulticastRendezvousPoint_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_interface_ip_isValid && m_multicast_group_isValid && true;
}

} // namespace OpenAPI
