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

/*
 * OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value.h
 *
 * Value object of this traffic filter
 */

#ifndef OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_H
#define OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_H

#include <QJsonObject>

#include "OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination.h"
#include "OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_source.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination;
class OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_source;

class OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value : public OAIObject {
public:
    OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value();
    OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value(QString json);
    ~OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination getDestination() const;
    void setDestination(const OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination &destination);
    bool is_destination_Set() const;
    bool is_destination_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getProtocol() const;
    void setProtocol(const QString &protocol);
    bool is_protocol_Set() const;
    bool is_protocol_Valid() const;

    OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_source getSource() const;
    void setSource(const OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_source &source);
    bool is_source_Set() const;
    bool is_source_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_destination m_destination;
    bool m_destination_isSet;
    bool m_destination_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_protocol;
    bool m_protocol_isSet;
    bool m_protocol_isValid;

    OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_source m_source;
    bool m_source_isSet;
    bool m_source_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value)

#endif // OAIUpdateNetworkApplianceTrafficShapingUplinkSelection_request_vpnTrafficUplinkPreferences_inner_trafficFilters_inner_value_H
