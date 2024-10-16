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
 * OAIIGeneralSetups.h
 *
 * 
 */

#ifndef OAIIGeneralSetups_H
#define OAIIGeneralSetups_H

#include <QJsonObject>

#include "OAICurrency.h"
#include "OAIPercent.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICurrency;
class OAIPercent;

class OAIIGeneralSetups : public OAIObject {
public:
    OAIIGeneralSetups();
    OAIIGeneralSetups(QString json);
    ~OAIIGeneralSetups() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICurrency getAppliedBusinessLimit() const;
    void setAppliedBusinessLimit(const OAICurrency &applied_business_limit);
    bool is_applied_business_limit_Set() const;
    bool is_applied_business_limit_Valid() const;

    OAICurrency getGoodWillFutureSalesMarketValue() const;
    void setGoodWillFutureSalesMarketValue(const OAICurrency &good_will_future_sales_market_value);
    bool is_good_will_future_sales_market_value_Set() const;
    bool is_good_will_future_sales_market_value_Valid() const;

    OAIPercent getPercentageOfLimitToUse() const;
    void setPercentageOfLimitToUse(const OAIPercent &percentage_of_limit_to_use);
    bool is_percentage_of_limit_to_use_Set() const;
    bool is_percentage_of_limit_to_use_Valid() const;

    OAICurrency getPreviousYearAdjustedAggregateInvestmentIncome() const;
    void setPreviousYearAdjustedAggregateInvestmentIncome(const OAICurrency &previous_year_adjusted_aggregate_investment_income);
    bool is_previous_year_adjusted_aggregate_investment_income_Set() const;
    bool is_previous_year_adjusted_aggregate_investment_income_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICurrency m_applied_business_limit;
    bool m_applied_business_limit_isSet;
    bool m_applied_business_limit_isValid;

    OAICurrency m_good_will_future_sales_market_value;
    bool m_good_will_future_sales_market_value_isSet;
    bool m_good_will_future_sales_market_value_isValid;

    OAIPercent m_percentage_of_limit_to_use;
    bool m_percentage_of_limit_to_use_isSet;
    bool m_percentage_of_limit_to_use_isValid;

    OAICurrency m_previous_year_adjusted_aggregate_investment_income;
    bool m_previous_year_adjusted_aggregate_investment_income_isSet;
    bool m_previous_year_adjusted_aggregate_investment_income_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIGeneralSetups)

#endif // OAIIGeneralSetups_H
