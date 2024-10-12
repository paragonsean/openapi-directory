/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAzureFirewallFqdnTagPropertiesFormat.h
 *
 * Azure Firewall FQDN Tag Properties
 */

#ifndef OAIAzureFirewallFqdnTagPropertiesFormat_H
#define OAIAzureFirewallFqdnTagPropertiesFormat_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAzureFirewallFqdnTagPropertiesFormat : public OAIObject {
public:
    OAIAzureFirewallFqdnTagPropertiesFormat();
    OAIAzureFirewallFqdnTagPropertiesFormat(QString json);
    ~OAIAzureFirewallFqdnTagPropertiesFormat() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFqdnTagName() const;
    void setFqdnTagName(const QString &fqdn_tag_name);
    bool is_fqdn_tag_name_Set() const;
    bool is_fqdn_tag_name_Valid() const;

    QString getProvisioningState() const;
    void setProvisioningState(const QString &provisioning_state);
    bool is_provisioning_state_Set() const;
    bool is_provisioning_state_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_fqdn_tag_name;
    bool m_fqdn_tag_name_isSet;
    bool m_fqdn_tag_name_isValid;

    QString m_provisioning_state;
    bool m_provisioning_state_isSet;
    bool m_provisioning_state_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAzureFirewallFqdnTagPropertiesFormat)

#endif // OAIAzureFirewallFqdnTagPropertiesFormat_H
