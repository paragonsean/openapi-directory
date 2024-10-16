/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGitHubMarketplacePurchase_plan.h
 *
 * GitHub Marketplace plan
 */

#ifndef OAIGitHubMarketplacePurchase_plan_H
#define OAIGitHubMarketplacePurchase_plan_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGitHubMarketplacePurchase_plan : public OAIObject {
public:
    OAIGitHubMarketplacePurchase_plan();
    OAIGitHubMarketplacePurchase_plan(QString json);
    ~OAIGitHubMarketplacePurchase_plan() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGitHubMarketplacePurchase_plan)

#endif // OAIGitHubMarketplacePurchase_plan_H
