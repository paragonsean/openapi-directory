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
 * OAIAssetsFundingGoalModel.h
 *
 * 
 */

#ifndef OAIAssetsFundingGoalModel_H
#define OAIAssetsFundingGoalModel_H

#include <QJsonObject>

#include "OAIObjectLink.h"
#include "OAIProjectedGoalsSummary_AssetsFundingGoalSummary.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIObjectLink;
class OAIProjectedGoalsSummary_AssetsFundingGoalSummary;

class OAIAssetsFundingGoalModel : public OAIObject {
public:
    OAIAssetsFundingGoalModel();
    OAIAssetsFundingGoalModel(QString json);
    ~OAIAssetsFundingGoalModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIObjectLink> getLinks() const;
    void setLinks(const QList<OAIObjectLink> &links);
    bool is_links_Set() const;
    bool is_links_Valid() const;

    QList<OAIProjectedGoalsSummary_AssetsFundingGoalSummary> getProjections() const;
    void setProjections(const QList<OAIProjectedGoalsSummary_AssetsFundingGoalSummary> &projections);
    bool is_projections_Set() const;
    bool is_projections_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIObjectLink> m_links;
    bool m_links_isSet;
    bool m_links_isValid;

    QList<OAIProjectedGoalsSummary_AssetsFundingGoalSummary> m_projections;
    bool m_projections_isSet;
    bool m_projections_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAssetsFundingGoalModel)

#endif // OAIAssetsFundingGoalModel_H
