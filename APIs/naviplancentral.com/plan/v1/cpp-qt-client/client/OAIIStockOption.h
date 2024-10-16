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
 * OAIIStockOption.h
 *
 * 
 */

#ifndef OAIIStockOption_H
#define OAIIStockOption_H

#include <QJsonObject>

#include "OAICurrency.h"
#include "OAIDate.h"
#include "OAIFormattedDateRange.h"
#include "OAIIVestingData.h"
#include "OAIPercent.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICurrency;
class OAIFormattedDateRange;
class OAIDate;
class OAIPercent;
class OAIIVestingData;

class OAIIStockOption : public OAIObject {
public:
    OAIIStockOption();
    OAIIStockOption(QString json);
    ~OAIIStockOption() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICurrency getAnnualDividendPerUnit() const;
    void setAnnualDividendPerUnit(const OAICurrency &annual_dividend_per_unit);
    bool is_annual_dividend_per_unit_Set() const;
    bool is_annual_dividend_per_unit_Valid() const;

    OAIFormattedDateRange getApplicableRangeRetirementLiquidatedAssets() const;
    void setApplicableRangeRetirementLiquidatedAssets(const OAIFormattedDateRange &applicable_range_retirement_liquidated_assets);
    bool is_applicable_range_retirement_liquidated_assets_Set() const;
    bool is_applicable_range_retirement_liquidated_assets_Valid() const;

    QString getCompany() const;
    void setCompany(const QString &company);
    bool is_company_Set() const;
    bool is_company_Valid() const;

    OAICurrency getCurrentUnitPrice() const;
    void setCurrentUnitPrice(const OAICurrency &current_unit_price);
    bool is_current_unit_price_Set() const;
    bool is_current_unit_price_Valid() const;

    OAIDate getCurrentUnitPriceDate() const;
    void setCurrentUnitPriceDate(const OAIDate &current_unit_price_date);
    bool is_current_unit_price_date_Set() const;
    bool is_current_unit_price_date_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    OAICurrency getEndOfPlanYearExercisableGrossValue() const;
    void setEndOfPlanYearExercisableGrossValue(const OAICurrency &end_of_plan_year_exercisable_gross_value);
    bool is_end_of_plan_year_exercisable_gross_value_Set() const;
    bool is_end_of_plan_year_exercisable_gross_value_Valid() const;

    OAICurrency getExerciseCost() const;
    void setExerciseCost(const OAICurrency &exercise_cost);
    bool is_exercise_cost_Set() const;
    bool is_exercise_cost_Valid() const;

    OAIDate getExpirationDate() const;
    void setExpirationDate(const OAIDate &expiration_date);
    bool is_expiration_date_Set() const;
    bool is_expiration_date_Valid() const;

    OAIDate getGrantDate() const;
    void setGrantDate(const OAIDate &grant_date);
    bool is_grant_date_Set() const;
    bool is_grant_date_Valid() const;

    qint32 getGrantedOptions() const;
    void setGrantedOptions(const qint32 &granted_options);
    bool is_granted_options_Set() const;
    bool is_granted_options_Valid() const;

    OAIPercent getGrowthRate() const;
    void setGrowthRate(const OAIPercent &growth_rate);
    bool is_growth_rate_Set() const;
    bool is_growth_rate_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint32 getOptionsExercisable() const;
    void setOptionsExercisable(const qint32 &options_exercisable);
    bool is_options_exercisable_Set() const;
    bool is_options_exercisable_Valid() const;

    qint32 getOptionsExercised() const;
    void setOptionsExercised(const qint32 &options_exercised);
    bool is_options_exercised_Set() const;
    bool is_options_exercised_Valid() const;

    qint32 getOptionsVested() const;
    void setOptionsVested(const qint32 &options_vested);
    bool is_options_vested_Set() const;
    bool is_options_vested_Valid() const;

    QString getOwner() const;
    void setOwner(const QString &owner);
    bool is_owner_Set() const;
    bool is_owner_Valid() const;

    OAICurrency getPreTaxProfit() const;
    void setPreTaxProfit(const OAICurrency &pre_tax_profit);
    bool is_pre_tax_profit_Set() const;
    bool is_pre_tax_profit_Valid() const;

    OAICurrency getStartOfYearAmtBasis() const;
    void setStartOfYearAmtBasis(const OAICurrency &start_of_year_amt_basis);
    bool is_start_of_year_amt_basis_Set() const;
    bool is_start_of_year_amt_basis_Valid() const;

    OAICurrency getStartOfYearCostBasis() const;
    void setStartOfYearCostBasis(const OAICurrency &start_of_year_cost_basis);
    bool is_start_of_year_cost_basis_Set() const;
    bool is_start_of_year_cost_basis_Valid() const;

    OAICurrency getStartOfYearUnitPrice() const;
    void setStartOfYearUnitPrice(const OAICurrency &start_of_year_unit_price);
    bool is_start_of_year_unit_price_Set() const;
    bool is_start_of_year_unit_price_Valid() const;

    OAICurrency getStrikePrice() const;
    void setStrikePrice(const OAICurrency &strike_price);
    bool is_strike_price_Set() const;
    bool is_strike_price_Valid() const;

    QString getSymbol() const;
    void setSymbol(const QString &symbol);
    bool is_symbol_Set() const;
    bool is_symbol_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getTypeFormatted() const;
    void setTypeFormatted(const QString &type_formatted);
    bool is_type_formatted_Set() const;
    bool is_type_formatted_Valid() const;

    QList<OAIIVestingData> getVestingSchedule() const;
    void setVestingSchedule(const QList<OAIIVestingData> &vesting_schedule);
    bool is_vesting_schedule_Set() const;
    bool is_vesting_schedule_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICurrency m_annual_dividend_per_unit;
    bool m_annual_dividend_per_unit_isSet;
    bool m_annual_dividend_per_unit_isValid;

    OAIFormattedDateRange m_applicable_range_retirement_liquidated_assets;
    bool m_applicable_range_retirement_liquidated_assets_isSet;
    bool m_applicable_range_retirement_liquidated_assets_isValid;

    QString m_company;
    bool m_company_isSet;
    bool m_company_isValid;

    OAICurrency m_current_unit_price;
    bool m_current_unit_price_isSet;
    bool m_current_unit_price_isValid;

    OAIDate m_current_unit_price_date;
    bool m_current_unit_price_date_isSet;
    bool m_current_unit_price_date_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAICurrency m_end_of_plan_year_exercisable_gross_value;
    bool m_end_of_plan_year_exercisable_gross_value_isSet;
    bool m_end_of_plan_year_exercisable_gross_value_isValid;

    OAICurrency m_exercise_cost;
    bool m_exercise_cost_isSet;
    bool m_exercise_cost_isValid;

    OAIDate m_expiration_date;
    bool m_expiration_date_isSet;
    bool m_expiration_date_isValid;

    OAIDate m_grant_date;
    bool m_grant_date_isSet;
    bool m_grant_date_isValid;

    qint32 m_granted_options;
    bool m_granted_options_isSet;
    bool m_granted_options_isValid;

    OAIPercent m_growth_rate;
    bool m_growth_rate_isSet;
    bool m_growth_rate_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint32 m_options_exercisable;
    bool m_options_exercisable_isSet;
    bool m_options_exercisable_isValid;

    qint32 m_options_exercised;
    bool m_options_exercised_isSet;
    bool m_options_exercised_isValid;

    qint32 m_options_vested;
    bool m_options_vested_isSet;
    bool m_options_vested_isValid;

    QString m_owner;
    bool m_owner_isSet;
    bool m_owner_isValid;

    OAICurrency m_pre_tax_profit;
    bool m_pre_tax_profit_isSet;
    bool m_pre_tax_profit_isValid;

    OAICurrency m_start_of_year_amt_basis;
    bool m_start_of_year_amt_basis_isSet;
    bool m_start_of_year_amt_basis_isValid;

    OAICurrency m_start_of_year_cost_basis;
    bool m_start_of_year_cost_basis_isSet;
    bool m_start_of_year_cost_basis_isValid;

    OAICurrency m_start_of_year_unit_price;
    bool m_start_of_year_unit_price_isSet;
    bool m_start_of_year_unit_price_isValid;

    OAICurrency m_strike_price;
    bool m_strike_price_isSet;
    bool m_strike_price_isValid;

    QString m_symbol;
    bool m_symbol_isSet;
    bool m_symbol_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_type_formatted;
    bool m_type_formatted_isSet;
    bool m_type_formatted_isValid;

    QList<OAIIVestingData> m_vesting_schedule;
    bool m_vesting_schedule_isSet;
    bool m_vesting_schedule_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIStockOption)

#endif // OAIIStockOption_H
