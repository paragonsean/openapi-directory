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
 * OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits.h
 *
 * A hash uplink keys and their configured settings for the Appliance
 */

#ifndef OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_H
#define OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_H

#include <QJsonObject>

#include "OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_cellular.h"
#include "OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_wan1.h"
#include "OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_wan2.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_cellular;
class OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_wan1;
class OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_wan2;

class OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits : public OAIObject {
public:
    OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits();
    OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits(QString json);
    ~OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_cellular getCellular() const;
    void setCellular(const OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_cellular &cellular);
    bool is_cellular_Set() const;
    bool is_cellular_Valid() const;

    OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_wan1 getWan1() const;
    void setWan1(const OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_wan1 &wan1);
    bool is_wan1_Set() const;
    bool is_wan1_Valid() const;

    OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_wan2 getWan2() const;
    void setWan2(const OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_wan2 &wan2);
    bool is_wan2_Set() const;
    bool is_wan2_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_cellular m_cellular;
    bool m_cellular_isSet;
    bool m_cellular_isValid;

    OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_wan1 m_wan1;
    bool m_wan1_isSet;
    bool m_wan1_isValid;

    OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_wan2 m_wan2;
    bool m_wan2_isSet;
    bool m_wan2_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits)

#endif // OAIGetNetworkApplianceTrafficShapingUplinkBandwidth_200_response_bandwidthLimits_H
