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

#include "OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6() {
    this->initializeModel();
}

OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::~OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6() {}

void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_assignment_mode_isSet = false;
    m_assignment_mode_isValid = false;

    m_gateway_isSet = false;
    m_gateway_isValid = false;

    m_nameservers_isSet = false;
    m_nameservers_isValid = false;
}

void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_assignment_mode_isValid = ::OpenAPI::fromJsonValue(m_assignment_mode, json[QString("assignmentMode")]);
    m_assignment_mode_isSet = !json[QString("assignmentMode")].isNull() && m_assignment_mode_isValid;

    m_gateway_isValid = ::OpenAPI::fromJsonValue(m_gateway, json[QString("gateway")]);
    m_gateway_isSet = !json[QString("gateway")].isNull() && m_gateway_isValid;

    m_nameservers_isValid = ::OpenAPI::fromJsonValue(m_nameservers, json[QString("nameservers")]);
    m_nameservers_isSet = !json[QString("nameservers")].isNull() && m_nameservers_isValid;
}

QString OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::asJsonObject() const {
    QJsonObject obj;
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_assignment_mode_isSet) {
        obj.insert(QString("assignmentMode"), ::OpenAPI::toJsonValue(m_assignment_mode));
    }
    if (m_gateway_isSet) {
        obj.insert(QString("gateway"), ::OpenAPI::toJsonValue(m_gateway));
    }
    if (m_nameservers.isSet()) {
        obj.insert(QString("nameservers"), ::OpenAPI::toJsonValue(m_nameservers));
    }
    return obj;
}

QString OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::getAddress() const {
    return m_address;
}
void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::is_address_Set() const{
    return m_address_isSet;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::is_address_Valid() const{
    return m_address_isValid;
}

QString OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::getAssignmentMode() const {
    return m_assignment_mode;
}
void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::setAssignmentMode(const QString &assignment_mode) {
    m_assignment_mode = assignment_mode;
    m_assignment_mode_isSet = true;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::is_assignment_mode_Set() const{
    return m_assignment_mode_isSet;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::is_assignment_mode_Valid() const{
    return m_assignment_mode_isValid;
}

QString OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::getGateway() const {
    return m_gateway;
}
void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::setGateway(const QString &gateway) {
    m_gateway = gateway;
    m_gateway_isSet = true;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::is_gateway_Set() const{
    return m_gateway_isSet;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::is_gateway_Valid() const{
    return m_gateway_isValid;
}

OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4_nameservers OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::getNameservers() const {
    return m_nameservers;
}
void OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::setNameservers(const OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv4_nameservers &nameservers) {
    m_nameservers = nameservers;
    m_nameservers_isSet = true;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::is_nameservers_Set() const{
    return m_nameservers_isSet;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::is_nameservers_Valid() const{
    return m_nameservers_isValid;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_assignment_mode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gateway_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nameservers.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetDeviceApplianceUplinksSettings_200_response_interfaces_wan1_svis_ipv6::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
