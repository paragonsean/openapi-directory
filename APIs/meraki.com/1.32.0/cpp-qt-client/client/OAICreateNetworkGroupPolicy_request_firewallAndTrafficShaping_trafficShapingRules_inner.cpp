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

#include "OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner() {
    this->initializeModel();
}

OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::~OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner() {}

void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::initializeModel() {

    m_definitions_isSet = false;
    m_definitions_isValid = false;

    m_dscp_tag_value_isSet = false;
    m_dscp_tag_value_isValid = false;

    m_pcp_tag_value_isSet = false;
    m_pcp_tag_value_isValid = false;

    m_per_client_bandwidth_limits_isSet = false;
    m_per_client_bandwidth_limits_isValid = false;

    m_priority_isSet = false;
    m_priority_isValid = false;
}

void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::fromJsonObject(QJsonObject json) {

    m_definitions_isValid = ::OpenAPI::fromJsonValue(m_definitions, json[QString("definitions")]);
    m_definitions_isSet = !json[QString("definitions")].isNull() && m_definitions_isValid;

    m_dscp_tag_value_isValid = ::OpenAPI::fromJsonValue(m_dscp_tag_value, json[QString("dscpTagValue")]);
    m_dscp_tag_value_isSet = !json[QString("dscpTagValue")].isNull() && m_dscp_tag_value_isValid;

    m_pcp_tag_value_isValid = ::OpenAPI::fromJsonValue(m_pcp_tag_value, json[QString("pcpTagValue")]);
    m_pcp_tag_value_isSet = !json[QString("pcpTagValue")].isNull() && m_pcp_tag_value_isValid;

    m_per_client_bandwidth_limits_isValid = ::OpenAPI::fromJsonValue(m_per_client_bandwidth_limits, json[QString("perClientBandwidthLimits")]);
    m_per_client_bandwidth_limits_isSet = !json[QString("perClientBandwidthLimits")].isNull() && m_per_client_bandwidth_limits_isValid;

    m_priority_isValid = ::OpenAPI::fromJsonValue(m_priority, json[QString("priority")]);
    m_priority_isSet = !json[QString("priority")].isNull() && m_priority_isValid;
}

QString OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_definitions.size() > 0) {
        obj.insert(QString("definitions"), ::OpenAPI::toJsonValue(m_definitions));
    }
    if (m_dscp_tag_value_isSet) {
        obj.insert(QString("dscpTagValue"), ::OpenAPI::toJsonValue(m_dscp_tag_value));
    }
    if (m_pcp_tag_value_isSet) {
        obj.insert(QString("pcpTagValue"), ::OpenAPI::toJsonValue(m_pcp_tag_value));
    }
    if (m_per_client_bandwidth_limits.isSet()) {
        obj.insert(QString("perClientBandwidthLimits"), ::OpenAPI::toJsonValue(m_per_client_bandwidth_limits));
    }
    if (m_priority_isSet) {
        obj.insert(QString("priority"), ::OpenAPI::toJsonValue(m_priority));
    }
    return obj;
}

QList<OAIUpdateNetworkApplianceTrafficShapingRules_request_rules_inner_definitions_inner> OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::getDefinitions() const {
    return m_definitions;
}
void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::setDefinitions(const QList<OAIUpdateNetworkApplianceTrafficShapingRules_request_rules_inner_definitions_inner> &definitions) {
    m_definitions = definitions;
    m_definitions_isSet = true;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::is_definitions_Set() const{
    return m_definitions_isSet;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::is_definitions_Valid() const{
    return m_definitions_isValid;
}

qint32 OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::getDscpTagValue() const {
    return m_dscp_tag_value;
}
void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::setDscpTagValue(const qint32 &dscp_tag_value) {
    m_dscp_tag_value = dscp_tag_value;
    m_dscp_tag_value_isSet = true;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::is_dscp_tag_value_Set() const{
    return m_dscp_tag_value_isSet;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::is_dscp_tag_value_Valid() const{
    return m_dscp_tag_value_isValid;
}

qint32 OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::getPcpTagValue() const {
    return m_pcp_tag_value;
}
void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::setPcpTagValue(const qint32 &pcp_tag_value) {
    m_pcp_tag_value = pcp_tag_value;
    m_pcp_tag_value_isSet = true;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::is_pcp_tag_value_Set() const{
    return m_pcp_tag_value_isSet;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::is_pcp_tag_value_Valid() const{
    return m_pcp_tag_value_isValid;
}

OAIUpdateNetworkApplianceTrafficShapingRules_request_rules_inner_perClientBandwidthLimits OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::getPerClientBandwidthLimits() const {
    return m_per_client_bandwidth_limits;
}
void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::setPerClientBandwidthLimits(const OAIUpdateNetworkApplianceTrafficShapingRules_request_rules_inner_perClientBandwidthLimits &per_client_bandwidth_limits) {
    m_per_client_bandwidth_limits = per_client_bandwidth_limits;
    m_per_client_bandwidth_limits_isSet = true;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::is_per_client_bandwidth_limits_Set() const{
    return m_per_client_bandwidth_limits_isSet;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::is_per_client_bandwidth_limits_Valid() const{
    return m_per_client_bandwidth_limits_isValid;
}

QString OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::getPriority() const {
    return m_priority;
}
void OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::setPriority(const QString &priority) {
    m_priority = priority;
    m_priority_isSet = true;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::is_priority_Set() const{
    return m_priority_isSet;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::is_priority_Valid() const{
    return m_priority_isValid;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_definitions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_dscp_tag_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pcp_tag_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_per_client_bandwidth_limits.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_priority_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateNetworkGroupPolicy_request_firewallAndTrafficShaping_trafficShapingRules_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_definitions_isValid && true;
}

} // namespace OpenAPI
