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

#include "OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner() {
    this->initializeModel();
}

OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::~OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner() {}

void OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::initializeModel() {

    m_access_isSet = false;
    m_access_isValid = false;

    m_allowed_ips_isSet = false;
    m_allowed_ips_isValid = false;

    m_lan_ip_isSet = false;
    m_lan_ip_isValid = false;

    m_local_port_isSet = false;
    m_local_port_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_protocol_isSet = false;
    m_protocol_isValid = false;

    m_public_port_isSet = false;
    m_public_port_isValid = false;
}

void OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::fromJsonObject(QJsonObject json) {

    m_access_isValid = ::OpenAPI::fromJsonValue(m_access, json[QString("access")]);
    m_access_isSet = !json[QString("access")].isNull() && m_access_isValid;

    m_allowed_ips_isValid = ::OpenAPI::fromJsonValue(m_allowed_ips, json[QString("allowedIps")]);
    m_allowed_ips_isSet = !json[QString("allowedIps")].isNull() && m_allowed_ips_isValid;

    m_lan_ip_isValid = ::OpenAPI::fromJsonValue(m_lan_ip, json[QString("lanIp")]);
    m_lan_ip_isSet = !json[QString("lanIp")].isNull() && m_lan_ip_isValid;

    m_local_port_isValid = ::OpenAPI::fromJsonValue(m_local_port, json[QString("localPort")]);
    m_local_port_isSet = !json[QString("localPort")].isNull() && m_local_port_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_protocol_isValid = ::OpenAPI::fromJsonValue(m_protocol, json[QString("protocol")]);
    m_protocol_isSet = !json[QString("protocol")].isNull() && m_protocol_isValid;

    m_public_port_isValid = ::OpenAPI::fromJsonValue(m_public_port, json[QString("publicPort")]);
    m_public_port_isSet = !json[QString("publicPort")].isNull() && m_public_port_isValid;
}

QString OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_access_isSet) {
        obj.insert(QString("access"), ::OpenAPI::toJsonValue(m_access));
    }
    if (m_allowed_ips.size() > 0) {
        obj.insert(QString("allowedIps"), ::OpenAPI::toJsonValue(m_allowed_ips));
    }
    if (m_lan_ip_isSet) {
        obj.insert(QString("lanIp"), ::OpenAPI::toJsonValue(m_lan_ip));
    }
    if (m_local_port_isSet) {
        obj.insert(QString("localPort"), ::OpenAPI::toJsonValue(m_local_port));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_protocol_isSet) {
        obj.insert(QString("protocol"), ::OpenAPI::toJsonValue(m_protocol));
    }
    if (m_public_port_isSet) {
        obj.insert(QString("publicPort"), ::OpenAPI::toJsonValue(m_public_port));
    }
    return obj;
}

QString OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::getAccess() const {
    return m_access;
}
void OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::setAccess(const QString &access) {
    m_access = access;
    m_access_isSet = true;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_access_Set() const{
    return m_access_isSet;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_access_Valid() const{
    return m_access_isValid;
}

QList<QString> OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::getAllowedIps() const {
    return m_allowed_ips;
}
void OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::setAllowedIps(const QList<QString> &allowed_ips) {
    m_allowed_ips = allowed_ips;
    m_allowed_ips_isSet = true;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_allowed_ips_Set() const{
    return m_allowed_ips_isSet;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_allowed_ips_Valid() const{
    return m_allowed_ips_isValid;
}

QString OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::getLanIp() const {
    return m_lan_ip;
}
void OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::setLanIp(const QString &lan_ip) {
    m_lan_ip = lan_ip;
    m_lan_ip_isSet = true;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_lan_ip_Set() const{
    return m_lan_ip_isSet;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_lan_ip_Valid() const{
    return m_lan_ip_isValid;
}

QString OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::getLocalPort() const {
    return m_local_port;
}
void OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::setLocalPort(const QString &local_port) {
    m_local_port = local_port;
    m_local_port_isSet = true;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_local_port_Set() const{
    return m_local_port_isSet;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_local_port_Valid() const{
    return m_local_port_isValid;
}

QString OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::getName() const {
    return m_name;
}
void OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::getProtocol() const {
    return m_protocol;
}
void OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::setProtocol(const QString &protocol) {
    m_protocol = protocol;
    m_protocol_isSet = true;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_protocol_Set() const{
    return m_protocol_isSet;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_protocol_Valid() const{
    return m_protocol_isValid;
}

QString OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::getPublicPort() const {
    return m_public_port;
}
void OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::setPublicPort(const QString &public_port) {
    m_public_port = public_port;
    m_public_port_isSet = true;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_public_port_Set() const{
    return m_public_port_isSet;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::is_public_port_Valid() const{
    return m_public_port_isValid;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_access_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_allowed_ips.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_lan_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_local_port_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_protocol_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_public_port_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateDeviceCellularGatewayPortForwardingRules_request_rules_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_access_isValid && m_lan_ip_isValid && m_local_port_isValid && m_protocol_isValid && m_public_port_isValid && true;
}

} // namespace OpenAPI
