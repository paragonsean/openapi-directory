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
 * OAIUpdateNetworkApplianceSingleLan_request_ipv6.h
 *
 * IPv6 configuration on the VLAN
 */

#ifndef OAIUpdateNetworkApplianceSingleLan_request_ipv6_H
#define OAIUpdateNetworkApplianceSingleLan_request_ipv6_H

#include <QJsonObject>

#include "OAIUpdateNetworkApplianceSingleLan_request_ipv6_prefixAssignments_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateNetworkApplianceSingleLan_request_ipv6_prefixAssignments_inner;

class OAIUpdateNetworkApplianceSingleLan_request_ipv6 : public OAIObject {
public:
    OAIUpdateNetworkApplianceSingleLan_request_ipv6();
    OAIUpdateNetworkApplianceSingleLan_request_ipv6(QString json);
    ~OAIUpdateNetworkApplianceSingleLan_request_ipv6() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    QList<OAIUpdateNetworkApplianceSingleLan_request_ipv6_prefixAssignments_inner> getPrefixAssignments() const;
    void setPrefixAssignments(const QList<OAIUpdateNetworkApplianceSingleLan_request_ipv6_prefixAssignments_inner> &prefix_assignments);
    bool is_prefix_assignments_Set() const;
    bool is_prefix_assignments_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    QList<OAIUpdateNetworkApplianceSingleLan_request_ipv6_prefixAssignments_inner> m_prefix_assignments;
    bool m_prefix_assignments_isSet;
    bool m_prefix_assignments_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkApplianceSingleLan_request_ipv6)

#endif // OAIUpdateNetworkApplianceSingleLan_request_ipv6_H
