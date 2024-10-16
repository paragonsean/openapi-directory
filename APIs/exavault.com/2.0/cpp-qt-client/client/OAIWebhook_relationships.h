/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWebhook_relationships.h
 *
 * 
 */

#ifndef OAIWebhook_relationships_H
#define OAIWebhook_relationships_H

#include <QJsonObject>

#include "OAIWebhook_relationships_ownerAccount.h"
#include "OAIWebhook_relationships_resource.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWebhook_relationships_ownerAccount;
class OAIWebhook_relationships_resource;

class OAIWebhook_relationships : public OAIObject {
public:
    OAIWebhook_relationships();
    OAIWebhook_relationships(QString json);
    ~OAIWebhook_relationships() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIWebhook_relationships_ownerAccount getOwnerAccount() const;
    void setOwnerAccount(const OAIWebhook_relationships_ownerAccount &owner_account);
    bool is_owner_account_Set() const;
    bool is_owner_account_Valid() const;

    OAIWebhook_relationships_resource getResource() const;
    void setResource(const OAIWebhook_relationships_resource &resource);
    bool is_resource_Set() const;
    bool is_resource_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIWebhook_relationships_ownerAccount m_owner_account;
    bool m_owner_account_isSet;
    bool m_owner_account_isValid;

    OAIWebhook_relationships_resource m_resource;
    bool m_resource_isSet;
    bool m_resource_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebhook_relationships)

#endif // OAIWebhook_relationships_H
