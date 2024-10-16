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
 * OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner.h
 *
 * 
 */

#ifndef OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner_H
#define OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner_H

#include <QJsonObject>

#include "OAIGetOrganizationApplianceVpnThirdPartyVPNPeers_200_response_peers_inner_ipsecPolicies.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetOrganizationApplianceVpnThirdPartyVPNPeers_200_response_peers_inner_ipsecPolicies;

class OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner : public OAIObject {
public:
    OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner();
    OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner(QString json);
    ~OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getIkeVersion() const;
    void setIkeVersion(const QString &ike_version);
    bool is_ike_version_Set() const;
    bool is_ike_version_Valid() const;

    OAIGetOrganizationApplianceVpnThirdPartyVPNPeers_200_response_peers_inner_ipsecPolicies getIpsecPolicies() const;
    void setIpsecPolicies(const OAIGetOrganizationApplianceVpnThirdPartyVPNPeers_200_response_peers_inner_ipsecPolicies &ipsec_policies);
    bool is_ipsec_policies_Set() const;
    bool is_ipsec_policies_Valid() const;

    QString getIpsecPoliciesPreset() const;
    void setIpsecPoliciesPreset(const QString &ipsec_policies_preset);
    bool is_ipsec_policies_preset_Set() const;
    bool is_ipsec_policies_preset_Valid() const;

    QString getLocalId() const;
    void setLocalId(const QString &local_id);
    bool is_local_id_Set() const;
    bool is_local_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<QString> getNetworkTags() const;
    void setNetworkTags(const QList<QString> &network_tags);
    bool is_network_tags_Set() const;
    bool is_network_tags_Valid() const;

    QList<QString> getPrivateSubnets() const;
    void setPrivateSubnets(const QList<QString> &private_subnets);
    bool is_private_subnets_Set() const;
    bool is_private_subnets_Valid() const;

    QString getPublicIp() const;
    void setPublicIp(const QString &public_ip);
    bool is_public_ip_Set() const;
    bool is_public_ip_Valid() const;

    QString getRemoteId() const;
    void setRemoteId(const QString &remote_id);
    bool is_remote_id_Set() const;
    bool is_remote_id_Valid() const;

    QString getSecret() const;
    void setSecret(const QString &secret);
    bool is_secret_Set() const;
    bool is_secret_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_ike_version;
    bool m_ike_version_isSet;
    bool m_ike_version_isValid;

    OAIGetOrganizationApplianceVpnThirdPartyVPNPeers_200_response_peers_inner_ipsecPolicies m_ipsec_policies;
    bool m_ipsec_policies_isSet;
    bool m_ipsec_policies_isValid;

    QString m_ipsec_policies_preset;
    bool m_ipsec_policies_preset_isSet;
    bool m_ipsec_policies_preset_isValid;

    QString m_local_id;
    bool m_local_id_isSet;
    bool m_local_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<QString> m_network_tags;
    bool m_network_tags_isSet;
    bool m_network_tags_isValid;

    QList<QString> m_private_subnets;
    bool m_private_subnets_isSet;
    bool m_private_subnets_isValid;

    QString m_public_ip;
    bool m_public_ip_isSet;
    bool m_public_ip_isValid;

    QString m_remote_id;
    bool m_remote_id_isSet;
    bool m_remote_id_isValid;

    QString m_secret;
    bool m_secret_isSet;
    bool m_secret_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner)

#endif // OAIUpdateOrganizationApplianceVpnThirdPartyVPNPeers_request_peers_inner_H
