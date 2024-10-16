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

#include "OAIUpdateNetworkApplianceVlan_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkApplianceVlan_request::OAIUpdateNetworkApplianceVlan_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkApplianceVlan_request::OAIUpdateNetworkApplianceVlan_request() {
    this->initializeModel();
}

OAIUpdateNetworkApplianceVlan_request::~OAIUpdateNetworkApplianceVlan_request() {}

void OAIUpdateNetworkApplianceVlan_request::initializeModel() {

    m_appliance_ip_isSet = false;
    m_appliance_ip_isValid = false;

    m_cidr_isSet = false;
    m_cidr_isValid = false;

    m_dhcp_boot_filename_isSet = false;
    m_dhcp_boot_filename_isValid = false;

    m_dhcp_boot_next_server_isSet = false;
    m_dhcp_boot_next_server_isValid = false;

    m_dhcp_boot_options_enabled_isSet = false;
    m_dhcp_boot_options_enabled_isValid = false;

    m_dhcp_handling_isSet = false;
    m_dhcp_handling_isValid = false;

    m_dhcp_lease_time_isSet = false;
    m_dhcp_lease_time_isValid = false;

    m_dhcp_options_isSet = false;
    m_dhcp_options_isValid = false;

    m_dhcp_relay_server_ips_isSet = false;
    m_dhcp_relay_server_ips_isValid = false;

    m_dns_nameservers_isSet = false;
    m_dns_nameservers_isValid = false;

    m_fixed_ip_assignments_isSet = false;
    m_fixed_ip_assignments_isValid = false;

    m_group_policy_id_isSet = false;
    m_group_policy_id_isValid = false;

    m_ipv6_isSet = false;
    m_ipv6_isValid = false;

    m_mandatory_dhcp_isSet = false;
    m_mandatory_dhcp_isValid = false;

    m_mask_isSet = false;
    m_mask_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_reserved_ip_ranges_isSet = false;
    m_reserved_ip_ranges_isValid = false;

    m_subnet_isSet = false;
    m_subnet_isValid = false;

    m_template_vlan_type_isSet = false;
    m_template_vlan_type_isValid = false;

    m_vpn_nat_subnet_isSet = false;
    m_vpn_nat_subnet_isValid = false;
}

void OAIUpdateNetworkApplianceVlan_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkApplianceVlan_request::fromJsonObject(QJsonObject json) {

    m_appliance_ip_isValid = ::OpenAPI::fromJsonValue(m_appliance_ip, json[QString("applianceIp")]);
    m_appliance_ip_isSet = !json[QString("applianceIp")].isNull() && m_appliance_ip_isValid;

    m_cidr_isValid = ::OpenAPI::fromJsonValue(m_cidr, json[QString("cidr")]);
    m_cidr_isSet = !json[QString("cidr")].isNull() && m_cidr_isValid;

    m_dhcp_boot_filename_isValid = ::OpenAPI::fromJsonValue(m_dhcp_boot_filename, json[QString("dhcpBootFilename")]);
    m_dhcp_boot_filename_isSet = !json[QString("dhcpBootFilename")].isNull() && m_dhcp_boot_filename_isValid;

    m_dhcp_boot_next_server_isValid = ::OpenAPI::fromJsonValue(m_dhcp_boot_next_server, json[QString("dhcpBootNextServer")]);
    m_dhcp_boot_next_server_isSet = !json[QString("dhcpBootNextServer")].isNull() && m_dhcp_boot_next_server_isValid;

    m_dhcp_boot_options_enabled_isValid = ::OpenAPI::fromJsonValue(m_dhcp_boot_options_enabled, json[QString("dhcpBootOptionsEnabled")]);
    m_dhcp_boot_options_enabled_isSet = !json[QString("dhcpBootOptionsEnabled")].isNull() && m_dhcp_boot_options_enabled_isValid;

    m_dhcp_handling_isValid = ::OpenAPI::fromJsonValue(m_dhcp_handling, json[QString("dhcpHandling")]);
    m_dhcp_handling_isSet = !json[QString("dhcpHandling")].isNull() && m_dhcp_handling_isValid;

    m_dhcp_lease_time_isValid = ::OpenAPI::fromJsonValue(m_dhcp_lease_time, json[QString("dhcpLeaseTime")]);
    m_dhcp_lease_time_isSet = !json[QString("dhcpLeaseTime")].isNull() && m_dhcp_lease_time_isValid;

    m_dhcp_options_isValid = ::OpenAPI::fromJsonValue(m_dhcp_options, json[QString("dhcpOptions")]);
    m_dhcp_options_isSet = !json[QString("dhcpOptions")].isNull() && m_dhcp_options_isValid;

    m_dhcp_relay_server_ips_isValid = ::OpenAPI::fromJsonValue(m_dhcp_relay_server_ips, json[QString("dhcpRelayServerIps")]);
    m_dhcp_relay_server_ips_isSet = !json[QString("dhcpRelayServerIps")].isNull() && m_dhcp_relay_server_ips_isValid;

    m_dns_nameservers_isValid = ::OpenAPI::fromJsonValue(m_dns_nameservers, json[QString("dnsNameservers")]);
    m_dns_nameservers_isSet = !json[QString("dnsNameservers")].isNull() && m_dns_nameservers_isValid;

    m_fixed_ip_assignments_isValid = ::OpenAPI::fromJsonValue(m_fixed_ip_assignments, json[QString("fixedIpAssignments")]);
    m_fixed_ip_assignments_isSet = !json[QString("fixedIpAssignments")].isNull() && m_fixed_ip_assignments_isValid;

    m_group_policy_id_isValid = ::OpenAPI::fromJsonValue(m_group_policy_id, json[QString("groupPolicyId")]);
    m_group_policy_id_isSet = !json[QString("groupPolicyId")].isNull() && m_group_policy_id_isValid;

    m_ipv6_isValid = ::OpenAPI::fromJsonValue(m_ipv6, json[QString("ipv6")]);
    m_ipv6_isSet = !json[QString("ipv6")].isNull() && m_ipv6_isValid;

    m_mandatory_dhcp_isValid = ::OpenAPI::fromJsonValue(m_mandatory_dhcp, json[QString("mandatoryDhcp")]);
    m_mandatory_dhcp_isSet = !json[QString("mandatoryDhcp")].isNull() && m_mandatory_dhcp_isValid;

    m_mask_isValid = ::OpenAPI::fromJsonValue(m_mask, json[QString("mask")]);
    m_mask_isSet = !json[QString("mask")].isNull() && m_mask_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_reserved_ip_ranges_isValid = ::OpenAPI::fromJsonValue(m_reserved_ip_ranges, json[QString("reservedIpRanges")]);
    m_reserved_ip_ranges_isSet = !json[QString("reservedIpRanges")].isNull() && m_reserved_ip_ranges_isValid;

    m_subnet_isValid = ::OpenAPI::fromJsonValue(m_subnet, json[QString("subnet")]);
    m_subnet_isSet = !json[QString("subnet")].isNull() && m_subnet_isValid;

    m_template_vlan_type_isValid = ::OpenAPI::fromJsonValue(m_template_vlan_type, json[QString("templateVlanType")]);
    m_template_vlan_type_isSet = !json[QString("templateVlanType")].isNull() && m_template_vlan_type_isValid;

    m_vpn_nat_subnet_isValid = ::OpenAPI::fromJsonValue(m_vpn_nat_subnet, json[QString("vpnNatSubnet")]);
    m_vpn_nat_subnet_isSet = !json[QString("vpnNatSubnet")].isNull() && m_vpn_nat_subnet_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkApplianceVlan_request::asJsonObject() const {
    QJsonObject obj;
    if (m_appliance_ip_isSet) {
        obj.insert(QString("applianceIp"), ::OpenAPI::toJsonValue(m_appliance_ip));
    }
    if (m_cidr_isSet) {
        obj.insert(QString("cidr"), ::OpenAPI::toJsonValue(m_cidr));
    }
    if (m_dhcp_boot_filename_isSet) {
        obj.insert(QString("dhcpBootFilename"), ::OpenAPI::toJsonValue(m_dhcp_boot_filename));
    }
    if (m_dhcp_boot_next_server_isSet) {
        obj.insert(QString("dhcpBootNextServer"), ::OpenAPI::toJsonValue(m_dhcp_boot_next_server));
    }
    if (m_dhcp_boot_options_enabled_isSet) {
        obj.insert(QString("dhcpBootOptionsEnabled"), ::OpenAPI::toJsonValue(m_dhcp_boot_options_enabled));
    }
    if (m_dhcp_handling_isSet) {
        obj.insert(QString("dhcpHandling"), ::OpenAPI::toJsonValue(m_dhcp_handling));
    }
    if (m_dhcp_lease_time_isSet) {
        obj.insert(QString("dhcpLeaseTime"), ::OpenAPI::toJsonValue(m_dhcp_lease_time));
    }
    if (m_dhcp_options.size() > 0) {
        obj.insert(QString("dhcpOptions"), ::OpenAPI::toJsonValue(m_dhcp_options));
    }
    if (m_dhcp_relay_server_ips.size() > 0) {
        obj.insert(QString("dhcpRelayServerIps"), ::OpenAPI::toJsonValue(m_dhcp_relay_server_ips));
    }
    if (m_dns_nameservers_isSet) {
        obj.insert(QString("dnsNameservers"), ::OpenAPI::toJsonValue(m_dns_nameservers));
    }
    if (m_fixed_ip_assignments_isSet) {
        obj.insert(QString("fixedIpAssignments"), ::OpenAPI::toJsonValue(m_fixed_ip_assignments));
    }
    if (m_group_policy_id_isSet) {
        obj.insert(QString("groupPolicyId"), ::OpenAPI::toJsonValue(m_group_policy_id));
    }
    if (m_ipv6.isSet()) {
        obj.insert(QString("ipv6"), ::OpenAPI::toJsonValue(m_ipv6));
    }
    if (m_mandatory_dhcp.isSet()) {
        obj.insert(QString("mandatoryDhcp"), ::OpenAPI::toJsonValue(m_mandatory_dhcp));
    }
    if (m_mask_isSet) {
        obj.insert(QString("mask"), ::OpenAPI::toJsonValue(m_mask));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_reserved_ip_ranges.size() > 0) {
        obj.insert(QString("reservedIpRanges"), ::OpenAPI::toJsonValue(m_reserved_ip_ranges));
    }
    if (m_subnet_isSet) {
        obj.insert(QString("subnet"), ::OpenAPI::toJsonValue(m_subnet));
    }
    if (m_template_vlan_type_isSet) {
        obj.insert(QString("templateVlanType"), ::OpenAPI::toJsonValue(m_template_vlan_type));
    }
    if (m_vpn_nat_subnet_isSet) {
        obj.insert(QString("vpnNatSubnet"), ::OpenAPI::toJsonValue(m_vpn_nat_subnet));
    }
    return obj;
}

QString OAIUpdateNetworkApplianceVlan_request::getApplianceIp() const {
    return m_appliance_ip;
}
void OAIUpdateNetworkApplianceVlan_request::setApplianceIp(const QString &appliance_ip) {
    m_appliance_ip = appliance_ip;
    m_appliance_ip_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_appliance_ip_Set() const{
    return m_appliance_ip_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_appliance_ip_Valid() const{
    return m_appliance_ip_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::getCidr() const {
    return m_cidr;
}
void OAIUpdateNetworkApplianceVlan_request::setCidr(const QString &cidr) {
    m_cidr = cidr;
    m_cidr_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_cidr_Set() const{
    return m_cidr_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_cidr_Valid() const{
    return m_cidr_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::getDhcpBootFilename() const {
    return m_dhcp_boot_filename;
}
void OAIUpdateNetworkApplianceVlan_request::setDhcpBootFilename(const QString &dhcp_boot_filename) {
    m_dhcp_boot_filename = dhcp_boot_filename;
    m_dhcp_boot_filename_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_boot_filename_Set() const{
    return m_dhcp_boot_filename_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_boot_filename_Valid() const{
    return m_dhcp_boot_filename_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::getDhcpBootNextServer() const {
    return m_dhcp_boot_next_server;
}
void OAIUpdateNetworkApplianceVlan_request::setDhcpBootNextServer(const QString &dhcp_boot_next_server) {
    m_dhcp_boot_next_server = dhcp_boot_next_server;
    m_dhcp_boot_next_server_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_boot_next_server_Set() const{
    return m_dhcp_boot_next_server_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_boot_next_server_Valid() const{
    return m_dhcp_boot_next_server_isValid;
}

bool OAIUpdateNetworkApplianceVlan_request::isDhcpBootOptionsEnabled() const {
    return m_dhcp_boot_options_enabled;
}
void OAIUpdateNetworkApplianceVlan_request::setDhcpBootOptionsEnabled(const bool &dhcp_boot_options_enabled) {
    m_dhcp_boot_options_enabled = dhcp_boot_options_enabled;
    m_dhcp_boot_options_enabled_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_boot_options_enabled_Set() const{
    return m_dhcp_boot_options_enabled_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_boot_options_enabled_Valid() const{
    return m_dhcp_boot_options_enabled_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::getDhcpHandling() const {
    return m_dhcp_handling;
}
void OAIUpdateNetworkApplianceVlan_request::setDhcpHandling(const QString &dhcp_handling) {
    m_dhcp_handling = dhcp_handling;
    m_dhcp_handling_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_handling_Set() const{
    return m_dhcp_handling_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_handling_Valid() const{
    return m_dhcp_handling_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::getDhcpLeaseTime() const {
    return m_dhcp_lease_time;
}
void OAIUpdateNetworkApplianceVlan_request::setDhcpLeaseTime(const QString &dhcp_lease_time) {
    m_dhcp_lease_time = dhcp_lease_time;
    m_dhcp_lease_time_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_lease_time_Set() const{
    return m_dhcp_lease_time_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_lease_time_Valid() const{
    return m_dhcp_lease_time_isValid;
}

QList<OAIGetNetworkApplianceVlans_200_response_inner_dhcpOptions_inner> OAIUpdateNetworkApplianceVlan_request::getDhcpOptions() const {
    return m_dhcp_options;
}
void OAIUpdateNetworkApplianceVlan_request::setDhcpOptions(const QList<OAIGetNetworkApplianceVlans_200_response_inner_dhcpOptions_inner> &dhcp_options) {
    m_dhcp_options = dhcp_options;
    m_dhcp_options_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_options_Set() const{
    return m_dhcp_options_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_options_Valid() const{
    return m_dhcp_options_isValid;
}

QList<QString> OAIUpdateNetworkApplianceVlan_request::getDhcpRelayServerIps() const {
    return m_dhcp_relay_server_ips;
}
void OAIUpdateNetworkApplianceVlan_request::setDhcpRelayServerIps(const QList<QString> &dhcp_relay_server_ips) {
    m_dhcp_relay_server_ips = dhcp_relay_server_ips;
    m_dhcp_relay_server_ips_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_relay_server_ips_Set() const{
    return m_dhcp_relay_server_ips_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dhcp_relay_server_ips_Valid() const{
    return m_dhcp_relay_server_ips_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::getDnsNameservers() const {
    return m_dns_nameservers;
}
void OAIUpdateNetworkApplianceVlan_request::setDnsNameservers(const QString &dns_nameservers) {
    m_dns_nameservers = dns_nameservers;
    m_dns_nameservers_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dns_nameservers_Set() const{
    return m_dns_nameservers_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_dns_nameservers_Valid() const{
    return m_dns_nameservers_isValid;
}

OAIObject OAIUpdateNetworkApplianceVlan_request::getFixedIpAssignments() const {
    return m_fixed_ip_assignments;
}
void OAIUpdateNetworkApplianceVlan_request::setFixedIpAssignments(const OAIObject &fixed_ip_assignments) {
    m_fixed_ip_assignments = fixed_ip_assignments;
    m_fixed_ip_assignments_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_fixed_ip_assignments_Set() const{
    return m_fixed_ip_assignments_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_fixed_ip_assignments_Valid() const{
    return m_fixed_ip_assignments_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::getGroupPolicyId() const {
    return m_group_policy_id;
}
void OAIUpdateNetworkApplianceVlan_request::setGroupPolicyId(const QString &group_policy_id) {
    m_group_policy_id = group_policy_id;
    m_group_policy_id_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_group_policy_id_Set() const{
    return m_group_policy_id_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_group_policy_id_Valid() const{
    return m_group_policy_id_isValid;
}

OAIUpdateNetworkApplianceSingleLan_request_ipv6 OAIUpdateNetworkApplianceVlan_request::getIpv6() const {
    return m_ipv6;
}
void OAIUpdateNetworkApplianceVlan_request::setIpv6(const OAIUpdateNetworkApplianceSingleLan_request_ipv6 &ipv6) {
    m_ipv6 = ipv6;
    m_ipv6_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_ipv6_Set() const{
    return m_ipv6_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_ipv6_Valid() const{
    return m_ipv6_isValid;
}

OAIGetNetworkApplianceVlans_200_response_inner_mandatoryDhcp OAIUpdateNetworkApplianceVlan_request::getMandatoryDhcp() const {
    return m_mandatory_dhcp;
}
void OAIUpdateNetworkApplianceVlan_request::setMandatoryDhcp(const OAIGetNetworkApplianceVlans_200_response_inner_mandatoryDhcp &mandatory_dhcp) {
    m_mandatory_dhcp = mandatory_dhcp;
    m_mandatory_dhcp_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_mandatory_dhcp_Set() const{
    return m_mandatory_dhcp_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_mandatory_dhcp_Valid() const{
    return m_mandatory_dhcp_isValid;
}

qint32 OAIUpdateNetworkApplianceVlan_request::getMask() const {
    return m_mask;
}
void OAIUpdateNetworkApplianceVlan_request::setMask(const qint32 &mask) {
    m_mask = mask;
    m_mask_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_mask_Set() const{
    return m_mask_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_mask_Valid() const{
    return m_mask_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::getName() const {
    return m_name;
}
void OAIUpdateNetworkApplianceVlan_request::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIUpdateNetworkApplianceStaticRoute_request_reservedIpRanges_inner> OAIUpdateNetworkApplianceVlan_request::getReservedIpRanges() const {
    return m_reserved_ip_ranges;
}
void OAIUpdateNetworkApplianceVlan_request::setReservedIpRanges(const QList<OAIUpdateNetworkApplianceStaticRoute_request_reservedIpRanges_inner> &reserved_ip_ranges) {
    m_reserved_ip_ranges = reserved_ip_ranges;
    m_reserved_ip_ranges_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_reserved_ip_ranges_Set() const{
    return m_reserved_ip_ranges_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_reserved_ip_ranges_Valid() const{
    return m_reserved_ip_ranges_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::getSubnet() const {
    return m_subnet;
}
void OAIUpdateNetworkApplianceVlan_request::setSubnet(const QString &subnet) {
    m_subnet = subnet;
    m_subnet_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_subnet_Set() const{
    return m_subnet_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_subnet_Valid() const{
    return m_subnet_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::getTemplateVlanType() const {
    return m_template_vlan_type;
}
void OAIUpdateNetworkApplianceVlan_request::setTemplateVlanType(const QString &template_vlan_type) {
    m_template_vlan_type = template_vlan_type;
    m_template_vlan_type_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_template_vlan_type_Set() const{
    return m_template_vlan_type_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_template_vlan_type_Valid() const{
    return m_template_vlan_type_isValid;
}

QString OAIUpdateNetworkApplianceVlan_request::getVpnNatSubnet() const {
    return m_vpn_nat_subnet;
}
void OAIUpdateNetworkApplianceVlan_request::setVpnNatSubnet(const QString &vpn_nat_subnet) {
    m_vpn_nat_subnet = vpn_nat_subnet;
    m_vpn_nat_subnet_isSet = true;
}

bool OAIUpdateNetworkApplianceVlan_request::is_vpn_nat_subnet_Set() const{
    return m_vpn_nat_subnet_isSet;
}

bool OAIUpdateNetworkApplianceVlan_request::is_vpn_nat_subnet_Valid() const{
    return m_vpn_nat_subnet_isValid;
}

bool OAIUpdateNetworkApplianceVlan_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_appliance_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cidr_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dhcp_boot_filename_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dhcp_boot_next_server_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dhcp_boot_options_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dhcp_handling_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dhcp_lease_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dhcp_options.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_dhcp_relay_server_ips.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_dns_nameservers_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fixed_ip_assignments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_policy_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ipv6.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_mandatory_dhcp.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_mask_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reserved_ip_ranges.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_subnet_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_template_vlan_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vpn_nat_subnet_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkApplianceVlan_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
