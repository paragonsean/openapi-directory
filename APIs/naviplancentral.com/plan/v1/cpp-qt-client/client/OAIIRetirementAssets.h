/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIRetirementAssets.h
 *
 * 
 */

#ifndef OAIIRetirementAssets_H
#define OAIIRetirementAssets_H

#include <QJsonObject>

#include "OAIIRetirementAssetCategories.h"
#include "OAIPercent.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIRetirementAssetCategories;
class OAIPercent;

class OAIIRetirementAssets : public OAIObject {
public:
    OAIIRetirementAssets();
    OAIIRetirementAssets(QString json);
    ~OAIIRetirementAssets() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIIRetirementAssetCategories getAllAssets() const;
    void setAllAssets(const OAIIRetirementAssetCategories &all_assets);
    bool is_all_assets_Set() const;
    bool is_all_assets_Valid() const;

    OAIIRetirementAssetCategories getClientAssets() const;
    void setClientAssets(const OAIIRetirementAssetCategories &client_assets);
    bool is_client_assets_Set() const;
    bool is_client_assets_Valid() const;

    OAIIRetirementAssetCategories getCoClientAssets() const;
    void setCoClientAssets(const OAIIRetirementAssetCategories &co_client_assets);
    bool is_co_client_assets_Set() const;
    bool is_co_client_assets_Valid() const;

    OAIIRetirementAssetCategories getCommunityPropertyAssets() const;
    void setCommunityPropertyAssets(const OAIIRetirementAssetCategories &community_property_assets);
    bool is_community_property_assets_Set() const;
    bool is_community_property_assets_Valid() const;

    OAIIRetirementAssetCategories getJointAssets() const;
    void setJointAssets(const OAIIRetirementAssetCategories &joint_assets);
    bool is_joint_assets_Set() const;
    bool is_joint_assets_Valid() const;

    OAIPercent getWithdrawalRate() const;
    void setWithdrawalRate(const OAIPercent &withdrawal_rate);
    bool is_withdrawal_rate_Set() const;
    bool is_withdrawal_rate_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIIRetirementAssetCategories m_all_assets;
    bool m_all_assets_isSet;
    bool m_all_assets_isValid;

    OAIIRetirementAssetCategories m_client_assets;
    bool m_client_assets_isSet;
    bool m_client_assets_isValid;

    OAIIRetirementAssetCategories m_co_client_assets;
    bool m_co_client_assets_isSet;
    bool m_co_client_assets_isValid;

    OAIIRetirementAssetCategories m_community_property_assets;
    bool m_community_property_assets_isSet;
    bool m_community_property_assets_isValid;

    OAIIRetirementAssetCategories m_joint_assets;
    bool m_joint_assets_isSet;
    bool m_joint_assets_isValid;

    OAIPercent m_withdrawal_rate;
    bool m_withdrawal_rate_isSet;
    bool m_withdrawal_rate_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIRetirementAssets)

#endif // OAIIRetirementAssets_H
