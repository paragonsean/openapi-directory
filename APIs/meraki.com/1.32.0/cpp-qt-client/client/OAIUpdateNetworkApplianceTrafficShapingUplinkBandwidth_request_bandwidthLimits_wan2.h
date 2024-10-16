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
 * OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan2.h
 *
 * The bandwidth settings for the &#39;wan2&#39; uplink
 */

#ifndef OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan2_H
#define OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan2_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan2 : public OAIObject {
public:
    OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan2();
    OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan2(QString json);
    ~OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan2() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getLimitDown() const;
    void setLimitDown(const qint32 &limit_down);
    bool is_limit_down_Set() const;
    bool is_limit_down_Valid() const;

    qint32 getLimitUp() const;
    void setLimitUp(const qint32 &limit_up);
    bool is_limit_up_Set() const;
    bool is_limit_up_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_limit_down;
    bool m_limit_down_isSet;
    bool m_limit_down_isValid;

    qint32 m_limit_up;
    bool m_limit_up_isSet;
    bool m_limit_up_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan2)

#endif // OAIUpdateNetworkApplianceTrafficShapingUplinkBandwidth_request_bandwidthLimits_wan2_H
