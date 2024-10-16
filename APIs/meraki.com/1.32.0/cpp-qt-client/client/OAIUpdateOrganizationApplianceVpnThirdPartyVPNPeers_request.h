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
 * OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request.h
 *
 * 
 */

#ifndef OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_H
#define OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_H

#include <QJsonObject>

#include "OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner;

class OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request : public OAIObject {
public:
    OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request();
    OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request(QString json);
    ~OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner> getPeers() const;
    void setPeers(const QList<OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner> &peers);
    bool is_peers_Set() const;
    bool is_peers_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner> m_peers;
    bool m_peers_isSet;
    bool m_peers_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request)

#endif // OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_H
