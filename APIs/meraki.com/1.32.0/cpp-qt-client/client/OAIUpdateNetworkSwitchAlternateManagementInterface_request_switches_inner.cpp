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

#include "OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner() {
    this->initializeModel();
}

OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::~OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner() {}

void OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::initializeModel() {

    m_alternate_management_ip_isSet = false;
    m_alternate_management_ip_isValid = false;

    m_gateway_isSet = false;
    m_gateway_isValid = false;

    m_serial_isSet = false;
    m_serial_isValid = false;

    m_subnet_mask_isSet = false;
    m_subnet_mask_isValid = false;
}

void OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::fromJsonObject(QJsonObject json) {

    m_alternate_management_ip_isValid = ::OpenAPI::fromJsonValue(m_alternate_management_ip, json[QString("alternateManagementIp")]);
    m_alternate_management_ip_isSet = !json[QString("alternateManagementIp")].isNull() && m_alternate_management_ip_isValid;

    m_gateway_isValid = ::OpenAPI::fromJsonValue(m_gateway, json[QString("gateway")]);
    m_gateway_isSet = !json[QString("gateway")].isNull() && m_gateway_isValid;

    m_serial_isValid = ::OpenAPI::fromJsonValue(m_serial, json[QString("serial")]);
    m_serial_isSet = !json[QString("serial")].isNull() && m_serial_isValid;

    m_subnet_mask_isValid = ::OpenAPI::fromJsonValue(m_subnet_mask, json[QString("subnetMask")]);
    m_subnet_mask_isSet = !json[QString("subnetMask")].isNull() && m_subnet_mask_isValid;
}

QString OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_alternate_management_ip_isSet) {
        obj.insert(QString("alternateManagementIp"), ::OpenAPI::toJsonValue(m_alternate_management_ip));
    }
    if (m_gateway_isSet) {
        obj.insert(QString("gateway"), ::OpenAPI::toJsonValue(m_gateway));
    }
    if (m_serial_isSet) {
        obj.insert(QString("serial"), ::OpenAPI::toJsonValue(m_serial));
    }
    if (m_subnet_mask_isSet) {
        obj.insert(QString("subnetMask"), ::OpenAPI::toJsonValue(m_subnet_mask));
    }
    return obj;
}

QString OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::getAlternateManagementIp() const {
    return m_alternate_management_ip;
}
void OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::setAlternateManagementIp(const QString &alternate_management_ip) {
    m_alternate_management_ip = alternate_management_ip;
    m_alternate_management_ip_isSet = true;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::is_alternate_management_ip_Set() const{
    return m_alternate_management_ip_isSet;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::is_alternate_management_ip_Valid() const{
    return m_alternate_management_ip_isValid;
}

QString OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::getGateway() const {
    return m_gateway;
}
void OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::setGateway(const QString &gateway) {
    m_gateway = gateway;
    m_gateway_isSet = true;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::is_gateway_Set() const{
    return m_gateway_isSet;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::is_gateway_Valid() const{
    return m_gateway_isValid;
}

QString OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::getSerial() const {
    return m_serial;
}
void OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::setSerial(const QString &serial) {
    m_serial = serial;
    m_serial_isSet = true;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::is_serial_Set() const{
    return m_serial_isSet;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::is_serial_Valid() const{
    return m_serial_isValid;
}

QString OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::getSubnetMask() const {
    return m_subnet_mask;
}
void OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::setSubnetMask(const QString &subnet_mask) {
    m_subnet_mask = subnet_mask;
    m_subnet_mask_isSet = true;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::is_subnet_mask_Set() const{
    return m_subnet_mask_isSet;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::is_subnet_mask_Valid() const{
    return m_subnet_mask_isValid;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_alternate_management_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gateway_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_serial_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subnet_mask_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkSwitchAlternateManagementInterface_request_switches_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_alternate_management_ip_isValid && m_serial_isValid && true;
}

} // namespace OpenAPI
