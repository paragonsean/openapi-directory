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
 * OAIContributions_mixin_contribution.h
 *
 * 
 */

#ifndef OAIContributions_mixin_contribution_H
#define OAIContributions_mixin_contribution_H

#include <QJsonObject>

#include "OAIContributions_mixin_contribution_contribution.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIContributions_mixin_contribution_contribution;

class OAIContributions_mixin_contribution : public OAIObject {
public:
    OAIContributions_mixin_contribution();
    OAIContributions_mixin_contribution(QString json);
    ~OAIContributions_mixin_contribution() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIContributions_mixin_contribution_contribution getContribution() const;
    void setContribution(const OAIContributions_mixin_contribution_contribution &contribution);
    bool is_contribution_Set() const;
    bool is_contribution_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIContributions_mixin_contribution_contribution m_contribution;
    bool m_contribution_isSet;
    bool m_contribution_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIContributions_mixin_contribution)

#endif // OAIContributions_mixin_contribution_H
