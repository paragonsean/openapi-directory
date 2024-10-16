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
 * OAIAdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments.h
 *
 * 
 */

#ifndef OAIAdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments_H
#define OAIAdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments_H

#include <QJsonObject>

#include "OAIAdvicentNaviPlanRestApiGoalAdjustmentsCoverageProjections.h"
#include "OAIAdvicentNaviPlanRestApiGoalAdjustmentsGoalAdjustmentsResultAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAdvicentNaviPlanRestApiGoalAdjustmentsGoalAdjustmentsResultAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments;
class OAIAdvicentNaviPlanRestApiGoalAdjustmentsCoverageProjections;

class OAIAdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments : public OAIObject {
public:
    OAIAdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments();
    OAIAdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments(QString json);
    ~OAIAdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAdvicentNaviPlanRestApiGoalAdjustmentsGoalAdjustmentsResultAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments getGoalAdjustments() const;
    void setGoalAdjustments(const OAIAdvicentNaviPlanRestApiGoalAdjustmentsGoalAdjustmentsResultAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments &goal_adjustments);
    bool is_goal_adjustments_Set() const;
    bool is_goal_adjustments_Valid() const;

    OAIAdvicentNaviPlanRestApiGoalAdjustmentsCoverageProjections getProjectedResults() const;
    void setProjectedResults(const OAIAdvicentNaviPlanRestApiGoalAdjustmentsCoverageProjections &projected_results);
    bool is_projected_results_Set() const;
    bool is_projected_results_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAdvicentNaviPlanRestApiGoalAdjustmentsGoalAdjustmentsResultAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments m_goal_adjustments;
    bool m_goal_adjustments_isSet;
    bool m_goal_adjustments_isValid;

    OAIAdvicentNaviPlanRestApiGoalAdjustmentsCoverageProjections m_projected_results;
    bool m_projected_results_isSet;
    bool m_projected_results_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments)

#endif // OAIAdvicentNaviPlanRestApiGoalAdjustmentsModelsCoverageProjectionsResultModelAdvicentDomainLogicGoalWhatIfEducationGoalAdjustments_H
