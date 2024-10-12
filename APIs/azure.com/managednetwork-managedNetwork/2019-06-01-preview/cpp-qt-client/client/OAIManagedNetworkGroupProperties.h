/**
 * ManagedNetworkManagementClient
 * The Microsoft Azure Managed Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to programmatically view, control, change, and monitor your entire Azure network centrally and with ease.
 *
 * The version of the OpenAPI document: 2019-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIManagedNetworkGroupProperties.h
 *
 * Properties of a Managed Network Group
 */

#ifndef OAIManagedNetworkGroupProperties_H
#define OAIManagedNetworkGroupProperties_H

#include <QJsonObject>

#include "OAIResourceId.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIResourceId;

class OAIManagedNetworkGroupProperties : public OAIObject {
public:
    OAIManagedNetworkGroupProperties();
    OAIManagedNetworkGroupProperties(QString json);
    ~OAIManagedNetworkGroupProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIResourceId> getManagementGroups() const;
    void setManagementGroups(const QList<OAIResourceId> &management_groups);
    bool is_management_groups_Set() const;
    bool is_management_groups_Valid() const;

    QList<OAIResourceId> getSubnets() const;
    void setSubnets(const QList<OAIResourceId> &subnets);
    bool is_subnets_Set() const;
    bool is_subnets_Valid() const;

    QList<OAIResourceId> getSubscriptions() const;
    void setSubscriptions(const QList<OAIResourceId> &subscriptions);
    bool is_subscriptions_Set() const;
    bool is_subscriptions_Valid() const;

    QList<OAIResourceId> getVirtualNetworks() const;
    void setVirtualNetworks(const QList<OAIResourceId> &virtual_networks);
    bool is_virtual_networks_Set() const;
    bool is_virtual_networks_Valid() const;

    QString getEtag() const;
    void setEtag(const QString &etag);
    bool is_etag_Set() const;
    bool is_etag_Valid() const;

    QString getProvisioningState() const;
    void setProvisioningState(const QString &provisioning_state);
    bool is_provisioning_state_Set() const;
    bool is_provisioning_state_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIResourceId> m_management_groups;
    bool m_management_groups_isSet;
    bool m_management_groups_isValid;

    QList<OAIResourceId> m_subnets;
    bool m_subnets_isSet;
    bool m_subnets_isValid;

    QList<OAIResourceId> m_subscriptions;
    bool m_subscriptions_isSet;
    bool m_subscriptions_isValid;

    QList<OAIResourceId> m_virtual_networks;
    bool m_virtual_networks_isSet;
    bool m_virtual_networks_isValid;

    QString m_etag;
    bool m_etag_isSet;
    bool m_etag_isValid;

    QString m_provisioning_state;
    bool m_provisioning_state_isSet;
    bool m_provisioning_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIManagedNetworkGroupProperties)

#endif // OAIManagedNetworkGroupProperties_H
