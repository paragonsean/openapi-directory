/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIContributions_mixin_contribution_contribution.h
 *
 * 
 */

#ifndef OAIContributions_mixin_contribution_contribution_H
#define OAIContributions_mixin_contribution_contribution_H

#include <QJsonObject>

#include "OAIContributions_mixin_contribution_contribution_contribution.h"
#include "OAIContributions_mixin_contribution_contribution_contribution_credit_role.h"
#include "OAIContributions_mixin_contributor.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIContributions_mixin_contribution_contribution_contribution;
class OAIContributions_mixin_contributor;
class OAIContributions_mixin_contribution_contribution_contribution_credit_role;

class OAIContributions_mixin_contribution_contribution : public OAIObject {
public:
    OAIContributions_mixin_contribution_contribution();
    OAIContributions_mixin_contribution_contribution(QString json);
    ~OAIContributions_mixin_contribution_contribution() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCharacterName() const;
    void setCharacterName(const QString &character_name);
    bool is_character_name_Set() const;
    bool is_character_name_Valid() const;

    OAIContributions_mixin_contribution_contribution_contribution getContribution() const;
    void setContribution(const OAIContributions_mixin_contribution_contribution_contribution &contribution);
    bool is_contribution_Set() const;
    bool is_contribution_Valid() const;

    OAIContributions_mixin_contributor getContributionsMixinContributor() const;
    void setContributionsMixinContributor(const OAIContributions_mixin_contributor &contributions_mixin_contributor);
    bool is_contributions_mixin_contributor_Set() const;
    bool is_contributions_mixin_contributor_Valid() const;

    OAIContributions_mixin_contribution_contribution_contribution_credit_role getCreditRole() const;
    void setCreditRole(const OAIContributions_mixin_contribution_contribution_contribution_credit_role &credit_role);
    bool is_credit_role_Set() const;
    bool is_credit_role_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_character_name;
    bool m_character_name_isSet;
    bool m_character_name_isValid;

    OAIContributions_mixin_contribution_contribution_contribution m_contribution;
    bool m_contribution_isSet;
    bool m_contribution_isValid;

    OAIContributions_mixin_contributor m_contributions_mixin_contributor;
    bool m_contributions_mixin_contributor_isSet;
    bool m_contributions_mixin_contributor_isValid;

    OAIContributions_mixin_contribution_contribution_contribution_credit_role m_credit_role;
    bool m_credit_role_isSet;
    bool m_credit_role_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIContributions_mixin_contribution_contribution)

#endif // OAIContributions_mixin_contribution_contribution_H
