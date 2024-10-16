/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIResourceServerRepresentation.h
 *
 * 
 */

#ifndef OAIResourceServerRepresentation_H
#define OAIResourceServerRepresentation_H

#include <QJsonObject>

#include "OAIPolicyRepresentation.h"
#include "OAIResourceRepresentation.h"
#include "OAIScopeRepresentation.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPolicyRepresentation;
class OAIResourceRepresentation;
class OAIScopeRepresentation;

class OAIResourceServerRepresentation : public OAIObject {
public:
    OAIResourceServerRepresentation();
    OAIResourceServerRepresentation(QString json);
    ~OAIResourceServerRepresentation() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllowRemoteResourceManagement() const;
    void setAllowRemoteResourceManagement(const bool &allow_remote_resource_management);
    bool is_allow_remote_resource_management_Set() const;
    bool is_allow_remote_resource_management_Valid() const;

    QString getClientId() const;
    void setClientId(const QString &client_id);
    bool is_client_id_Set() const;
    bool is_client_id_Valid() const;

    QString getDecisionStrategy() const;
    void setDecisionStrategy(const QString &decision_strategy);
    bool is_decision_strategy_Set() const;
    bool is_decision_strategy_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAIPolicyRepresentation> getPolicies() const;
    void setPolicies(const QList<OAIPolicyRepresentation> &policies);
    bool is_policies_Set() const;
    bool is_policies_Valid() const;

    QString getPolicyEnforcementMode() const;
    void setPolicyEnforcementMode(const QString &policy_enforcement_mode);
    bool is_policy_enforcement_mode_Set() const;
    bool is_policy_enforcement_mode_Valid() const;

    QList<OAIResourceRepresentation> getResources() const;
    void setResources(const QList<OAIResourceRepresentation> &resources);
    bool is_resources_Set() const;
    bool is_resources_Valid() const;

    QList<OAIScopeRepresentation> getScopes() const;
    void setScopes(const QList<OAIScopeRepresentation> &scopes);
    bool is_scopes_Set() const;
    bool is_scopes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_allow_remote_resource_management;
    bool m_allow_remote_resource_management_isSet;
    bool m_allow_remote_resource_management_isValid;

    QString m_client_id;
    bool m_client_id_isSet;
    bool m_client_id_isValid;

    QString m_decision_strategy;
    bool m_decision_strategy_isSet;
    bool m_decision_strategy_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAIPolicyRepresentation> m_policies;
    bool m_policies_isSet;
    bool m_policies_isValid;

    QString m_policy_enforcement_mode;
    bool m_policy_enforcement_mode_isSet;
    bool m_policy_enforcement_mode_isValid;

    QList<OAIResourceRepresentation> m_resources;
    bool m_resources_isSet;
    bool m_resources_isValid;

    QList<OAIScopeRepresentation> m_scopes;
    bool m_scopes_isSet;
    bool m_scopes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIResourceServerRepresentation)

#endif // OAIResourceServerRepresentation_H
