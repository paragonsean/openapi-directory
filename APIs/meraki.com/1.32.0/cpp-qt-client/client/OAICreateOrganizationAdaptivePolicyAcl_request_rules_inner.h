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
 * OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner.h
 *
 * 
 */

#ifndef OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner_H
#define OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner : public OAIObject {
public:
    OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner();
    OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner(QString json);
    ~OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDstPort() const;
    void setDstPort(const QString &dst_port);
    bool is_dst_port_Set() const;
    bool is_dst_port_Valid() const;

    QString getPolicy() const;
    void setPolicy(const QString &policy);
    bool is_policy_Set() const;
    bool is_policy_Valid() const;

    QString getProtocol() const;
    void setProtocol(const QString &protocol);
    bool is_protocol_Set() const;
    bool is_protocol_Valid() const;

    QString getSrcPort() const;
    void setSrcPort(const QString &src_port);
    bool is_src_port_Set() const;
    bool is_src_port_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_dst_port;
    bool m_dst_port_isSet;
    bool m_dst_port_isValid;

    QString m_policy;
    bool m_policy_isSet;
    bool m_policy_isValid;

    QString m_protocol;
    bool m_protocol_isSet;
    bool m_protocol_isValid;

    QString m_src_port;
    bool m_src_port_isSet;
    bool m_src_port_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner)

#endif // OAICreateOrganizationAdaptivePolicyAcl_request_rules_inner_H
