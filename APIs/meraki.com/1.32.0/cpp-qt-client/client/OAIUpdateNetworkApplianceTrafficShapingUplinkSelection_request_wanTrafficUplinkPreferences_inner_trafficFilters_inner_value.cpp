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

#include "OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value() {
    this->initializeModel();
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::~OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value() {}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::initializeModel() {

    m_destination_isSet = false;
    m_destination_isValid = false;

    m_protocol_isSet = false;
    m_protocol_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::fromJsonObject(QJsonObject json) {

    m_destination_isValid = ::OpenAPI::fromJsonValue(m_destination, json[QString("destination")]);
    m_destination_isSet = !json[QString("destination")].isNull() && m_destination_isValid;

    m_protocol_isValid = ::OpenAPI::fromJsonValue(m_protocol, json[QString("protocol")]);
    m_protocol_isSet = !json[QString("protocol")].isNull() && m_protocol_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;
}

QString OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::asJsonObject() const {
    QJsonObject obj;
    if (m_destination.isSet()) {
        obj.insert(QString("destination"), ::OpenAPI::toJsonValue(m_destination));
    }
    if (m_protocol_isSet) {
        obj.insert(QString("protocol"), ::OpenAPI::toJsonValue(m_protocol));
    }
    if (m_source.isSet()) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    return obj;
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::getDestination() const {
    return m_destination;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::setDestination(const OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination &destination) {
    m_destination = destination;
    m_destination_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::is_destination_Set() const{
    return m_destination_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::is_destination_Valid() const{
    return m_destination_isValid;
}

QString OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::getProtocol() const {
    return m_protocol;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::setProtocol(const QString &protocol) {
    m_protocol = protocol;
    m_protocol_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::is_protocol_Set() const{
    return m_protocol_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::is_protocol_Valid() const{
    return m_protocol_isValid;
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value_source OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::getSource() const {
    return m_source;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::setSource(const OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value_source &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::is_source_Set() const{
    return m_source_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::is_source_Valid() const{
    return m_source_isValid;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_destination.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_protocol_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner_value::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_destination_isValid && m_source_isValid && true;
}

} // namespace OpenAPI
