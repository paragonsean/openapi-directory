/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAppServicePlans_ListWebApps_200_response_value_inner_identity.h
 *
 * Managed service identity.
 */

#ifndef OAIAppServicePlans_ListWebApps_200_response_value_inner_identity_H
#define OAIAppServicePlans_ListWebApps_200_response_value_inner_identity_H

#include <QJsonObject>

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_identity_userAssignedIdentities_value.h"
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAppServicePlans_ListWebApps_200_response_value_inner_identity_userAssignedIdentities_value;

class OAIAppServicePlans_ListWebApps_200_response_value_inner_identity : public OAIObject {
public:
    OAIAppServicePlans_ListWebApps_200_response_value_inner_identity();
    OAIAppServicePlans_ListWebApps_200_response_value_inner_identity(QString json);
    ~OAIAppServicePlans_ListWebApps_200_response_value_inner_identity() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getPrincipalId() const;
    void setPrincipalId(const QString &principal_id);
    bool is_principal_id_Set() const;
    bool is_principal_id_Valid() const;

    QString getTenantId() const;
    void setTenantId(const QString &tenant_id);
    bool is_tenant_id_Set() const;
    bool is_tenant_id_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QMap<QString, OAIAppServicePlans_ListWebApps_200_response_value_inner_identity_userAssignedIdentities_value> getUserAssignedIdentities() const;
    void setUserAssignedIdentities(const QMap<QString, OAIAppServicePlans_ListWebApps_200_response_value_inner_identity_userAssignedIdentities_value> &user_assigned_identities);
    bool is_user_assigned_identities_Set() const;
    bool is_user_assigned_identities_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_principal_id;
    bool m_principal_id_isSet;
    bool m_principal_id_isValid;

    QString m_tenant_id;
    bool m_tenant_id_isSet;
    bool m_tenant_id_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QMap<QString, OAIAppServicePlans_ListWebApps_200_response_value_inner_identity_userAssignedIdentities_value> m_user_assigned_identities;
    bool m_user_assigned_identities_isSet;
    bool m_user_assigned_identities_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_ListWebApps_200_response_value_inner_identity)

#endif // OAIAppServicePlans_ListWebApps_200_response_value_inner_identity_H
