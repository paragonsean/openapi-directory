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

#include "OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner() {
    this->initializeModel();
}

OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::~OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner() {}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::initializeModel() {

    m_preferred_uplink_isSet = false;
    m_preferred_uplink_isValid = false;

    m_traffic_filters_isSet = false;
    m_traffic_filters_isValid = false;
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::fromJsonObject(QJsonObject json) {

    m_preferred_uplink_isValid = ::OpenAPI::fromJsonValue(m_preferred_uplink, json[QString("preferredUplink")]);
    m_preferred_uplink_isSet = !json[QString("preferredUplink")].isNull() && m_preferred_uplink_isValid;

    m_traffic_filters_isValid = ::OpenAPI::fromJsonValue(m_traffic_filters, json[QString("trafficFilters")]);
    m_traffic_filters_isSet = !json[QString("trafficFilters")].isNull() && m_traffic_filters_isValid;
}

QString OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_preferred_uplink_isSet) {
        obj.insert(QString("preferredUplink"), ::OpenAPI::toJsonValue(m_preferred_uplink));
    }
    if (m_traffic_filters.size() > 0) {
        obj.insert(QString("trafficFilters"), ::OpenAPI::toJsonValue(m_traffic_filters));
    }
    return obj;
}

QString OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::getPreferredUplink() const {
    return m_preferred_uplink;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::setPreferredUplink(const QString &preferred_uplink) {
    m_preferred_uplink = preferred_uplink;
    m_preferred_uplink_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::is_preferred_uplink_Set() const{
    return m_preferred_uplink_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::is_preferred_uplink_Valid() const{
    return m_preferred_uplink_isValid;
}

QList<OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner> OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::getTrafficFilters() const {
    return m_traffic_filters;
}
void OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::setTrafficFilters(const QList<OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner_trafficFilters_inner> &traffic_filters) {
    m_traffic_filters = traffic_filters;
    m_traffic_filters_isSet = true;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::is_traffic_filters_Set() const{
    return m_traffic_filters_isSet;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::is_traffic_filters_Valid() const{
    return m_traffic_filters_isValid;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_preferred_uplink_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_traffic_filters.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_wanTrafficUplinkPreferences_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_preferred_uplink_isValid && m_traffic_filters_isValid && true;
}

} // namespace OpenAPI
