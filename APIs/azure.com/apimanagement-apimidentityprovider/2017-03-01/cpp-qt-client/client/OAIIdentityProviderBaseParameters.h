/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2017-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIdentityProviderBaseParameters.h
 *
 * Identity Provider Base Parameter Properties.
 */

#ifndef OAIIdentityProviderBaseParameters_H
#define OAIIdentityProviderBaseParameters_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIIdentityProviderBaseParameters : public OAIObject {
public:
    OAIIdentityProviderBaseParameters();
    OAIIdentityProviderBaseParameters(QString json);
    ~OAIIdentityProviderBaseParameters() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getAllowedTenants() const;
    void setAllowedTenants(const QList<QString> &allowed_tenants);
    bool is_allowed_tenants_Set() const;
    bool is_allowed_tenants_Valid() const;

    QString getPasswordResetPolicyName() const;
    void setPasswordResetPolicyName(const QString &password_reset_policy_name);
    bool is_password_reset_policy_name_Set() const;
    bool is_password_reset_policy_name_Valid() const;

    QString getProfileEditingPolicyName() const;
    void setProfileEditingPolicyName(const QString &profile_editing_policy_name);
    bool is_profile_editing_policy_name_Set() const;
    bool is_profile_editing_policy_name_Valid() const;

    QString getSigninPolicyName() const;
    void setSigninPolicyName(const QString &signin_policy_name);
    bool is_signin_policy_name_Set() const;
    bool is_signin_policy_name_Valid() const;

    QString getSignupPolicyName() const;
    void setSignupPolicyName(const QString &signup_policy_name);
    bool is_signup_policy_name_Set() const;
    bool is_signup_policy_name_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_allowed_tenants;
    bool m_allowed_tenants_isSet;
    bool m_allowed_tenants_isValid;

    QString m_password_reset_policy_name;
    bool m_password_reset_policy_name_isSet;
    bool m_password_reset_policy_name_isValid;

    QString m_profile_editing_policy_name;
    bool m_profile_editing_policy_name_isSet;
    bool m_profile_editing_policy_name_isValid;

    QString m_signin_policy_name;
    bool m_signin_policy_name_isSet;
    bool m_signin_policy_name_isValid;

    QString m_signup_policy_name;
    bool m_signup_policy_name_isSet;
    bool m_signup_policy_name_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIdentityProviderBaseParameters)

#endif // OAIIdentityProviderBaseParameters_H
