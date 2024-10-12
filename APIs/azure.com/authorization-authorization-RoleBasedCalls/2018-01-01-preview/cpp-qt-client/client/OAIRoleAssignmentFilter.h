/**
 * AuthorizationManagementClient
 * Role based access control provides you a way to apply granular level policy administration down to individual resources or resource groups. These operations enable you to manage role definitions and role assignments. A role definition describes the set of actions that can be performed on resources. A role assignment grants access to Azure Active Directory users.
 *
 * The version of the OpenAPI document: 2018-01-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRoleAssignmentFilter.h
 *
 * Role Assignments filter
 */

#ifndef OAIRoleAssignmentFilter_H
#define OAIRoleAssignmentFilter_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIRoleAssignmentFilter : public OAIObject {
public:
    OAIRoleAssignmentFilter();
    OAIRoleAssignmentFilter(QString json);
    ~OAIRoleAssignmentFilter() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isCanDelegate() const;
    void setCanDelegate(const bool &can_delegate);
    bool is_can_delegate_Set() const;
    bool is_can_delegate_Valid() const;

    QString getPrincipalId() const;
    void setPrincipalId(const QString &principal_id);
    bool is_principal_id_Set() const;
    bool is_principal_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_can_delegate;
    bool m_can_delegate_isSet;
    bool m_can_delegate_isValid;

    QString m_principal_id;
    bool m_principal_id_isSet;
    bool m_principal_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRoleAssignmentFilter)

#endif // OAIRoleAssignmentFilter_H
