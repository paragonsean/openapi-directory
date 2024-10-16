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
 * OAIISEPPRedemptionStrategy.h
 *
 * 
 */

#ifndef OAIISEPPRedemptionStrategy_H
#define OAIISEPPRedemptionStrategy_H

#include <QJsonObject>

#include "OAIFormattedDateRange.h"
#include "OAIFormattedEnumType_Frequency.h"
#include "OAIFormattedEnumType_SEPPDistributionMethod.h"
#include "OAIFormattedEnumType_SEPPLifeExpectancyTable.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFormattedDateRange;
class OAIFormattedEnumType_SEPPDistributionMethod;
class OAIFormattedEnumType_SEPPLifeExpectancyTable;
class OAIFormattedEnumType_Frequency;

class OAIISEPPRedemptionStrategy : public OAIObject {
public:
    OAIISEPPRedemptionStrategy();
    OAIISEPPRedemptionStrategy(QString json);
    ~OAIISEPPRedemptionStrategy() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIFormattedDateRange getApplicableDateRange() const;
    void setApplicableDateRange(const OAIFormattedDateRange &applicable_date_range);
    bool is_applicable_date_range_Set() const;
    bool is_applicable_date_range_Valid() const;

    OAIFormattedEnumType_SEPPDistributionMethod getDistributionMethod() const;
    void setDistributionMethod(const OAIFormattedEnumType_SEPPDistributionMethod &distribution_method);
    bool is_distribution_method_Set() const;
    bool is_distribution_method_Valid() const;

    OAIFormattedEnumType_SEPPLifeExpectancyTable getLifeExpectancyTable() const;
    void setLifeExpectancyTable(const OAIFormattedEnumType_SEPPLifeExpectancyTable &life_expectancy_table);
    bool is_life_expectancy_table_Set() const;
    bool is_life_expectancy_table_Valid() const;

    OAIFormattedEnumType_Frequency getRedemptionFrequency() const;
    void setRedemptionFrequency(const OAIFormattedEnumType_Frequency &redemption_frequency);
    bool is_redemption_frequency_Set() const;
    bool is_redemption_frequency_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIFormattedDateRange m_applicable_date_range;
    bool m_applicable_date_range_isSet;
    bool m_applicable_date_range_isValid;

    OAIFormattedEnumType_SEPPDistributionMethod m_distribution_method;
    bool m_distribution_method_isSet;
    bool m_distribution_method_isValid;

    OAIFormattedEnumType_SEPPLifeExpectancyTable m_life_expectancy_table;
    bool m_life_expectancy_table_isSet;
    bool m_life_expectancy_table_isValid;

    OAIFormattedEnumType_Frequency m_redemption_frequency;
    bool m_redemption_frequency_isSet;
    bool m_redemption_frequency_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIISEPPRedemptionStrategy)

#endif // OAIISEPPRedemptionStrategy_H
