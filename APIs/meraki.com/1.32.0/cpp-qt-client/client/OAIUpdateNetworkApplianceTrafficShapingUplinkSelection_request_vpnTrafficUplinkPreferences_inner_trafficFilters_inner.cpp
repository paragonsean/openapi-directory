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

#include "OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner() {
    this->initializeModel();
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::~OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner() {}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::initializeModel() {

    m_type_isSet = false;
    m_type_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::fromJsonObject(QJsonObject json) {

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_value.isSet()) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::getType() const {
    return m_type;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::is_type_Valid() const{
    return m_type_isValid;
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::getValue() const {
    return m_value;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::setValue(const OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_type_isValid && m_value_isValid && true;
}

} // namespace OpenAPI
