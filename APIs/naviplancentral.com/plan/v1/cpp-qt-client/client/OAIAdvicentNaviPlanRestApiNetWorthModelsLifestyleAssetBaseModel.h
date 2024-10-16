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
 * OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel.h
 *
 * 
 */

#ifndef OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel_H
#define OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel_H

#include <QJsonObject>

#include "OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetModel.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetModel;

class OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel : public OAIObject {
public:
    OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel();
    OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel(QString json);
    ~OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetModel> getLifestyleAssets() const;
    void setLifestyleAssets(const QList<OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetModel> &lifestyle_assets);
    bool is_lifestyle_assets_Set() const;
    bool is_lifestyle_assets_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetModel> m_lifestyle_assets;
    bool m_lifestyle_assets_isSet;
    bool m_lifestyle_assets_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel)

#endif // OAIAdvicentNaviPlanRestApiNetWorthModelsLifestyleAssetBaseModel_H
