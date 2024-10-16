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
 * OAIILifestyleAsset.h
 *
 * 
 */

#ifndef OAIILifestyleAsset_H
#define OAIILifestyleAsset_H

#include <QJsonObject>

#include "OAICurrency.h"
#include "OAICurrencyWithDate.h"
#include "OAIDate.h"
#include "OAIFormattedLifestyleType.h"
#include "OAIPercent.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICurrency;
class OAICurrencyWithDate;
class OAIPercent;
class OAIDate;
class OAIFormattedLifestyleType;

class OAIILifestyleAsset : public OAIObject {
public:
    OAIILifestyleAsset();
    OAIILifestyleAsset(QString json);
    ~OAIILifestyleAsset() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAfterTaxProceedsAccountName() const;
    void setAfterTaxProceedsAccountName(const QString &after_tax_proceeds_account_name);
    bool is_after_tax_proceeds_account_name_Set() const;
    bool is_after_tax_proceeds_account_name_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    OAICurrency getFutureValueProjectedGrossSaleValue() const;
    void setFutureValueProjectedGrossSaleValue(const OAICurrency &future_value_projected_gross_sale_value);
    bool is_future_value_projected_gross_sale_value_Set() const;
    bool is_future_value_projected_gross_sale_value_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsMajorPurchaseGoal() const;
    void setIsMajorPurchaseGoal(const bool &is_major_purchase_goal);
    bool is_is_major_purchase_goal_Set() const;
    bool is_is_major_purchase_goal_Valid() const;

    OAICurrencyWithDate getMarketValueAsOf() const;
    void setMarketValueAsOf(const OAICurrencyWithDate &market_value_as_of);
    bool is_market_value_as_of_Set() const;
    bool is_market_value_as_of_Valid() const;

    QString getOwner() const;
    void setOwner(const QString &owner);
    bool is_owner_Set() const;
    bool is_owner_Valid() const;

    OAIPercent getPreTaxGrowthRate() const;
    void setPreTaxGrowthRate(const OAIPercent &pre_tax_growth_rate);
    bool is_pre_tax_growth_rate_Set() const;
    bool is_pre_tax_growth_rate_Valid() const;

    OAICurrency getPresentValueProjectedGrossSaleValue() const;
    void setPresentValueProjectedGrossSaleValue(const OAICurrency &present_value_projected_gross_sale_value);
    bool is_present_value_projected_gross_sale_value_Set() const;
    bool is_present_value_projected_gross_sale_value_Valid() const;

    OAIDate getProjectedSaleDate() const;
    void setProjectedSaleDate(const OAIDate &projected_sale_date);
    bool is_projected_sale_date_Set() const;
    bool is_projected_sale_date_Valid() const;

    OAICurrency getPurchaseAmount() const;
    void setPurchaseAmount(const OAICurrency &purchase_amount);
    bool is_purchase_amount_Set() const;
    bool is_purchase_amount_Valid() const;

    OAIDate getPurchaseDate() const;
    void setPurchaseDate(const OAIDate &purchase_date);
    bool is_purchase_date_Set() const;
    bool is_purchase_date_Valid() const;

    OAIPercent getSellingCostPercent() const;
    void setSellingCostPercent(const OAIPercent &selling_cost_percent);
    bool is_selling_cost_percent_Set() const;
    bool is_selling_cost_percent_Valid() const;

    OAIPercent getStandardDeviation() const;
    void setStandardDeviation(const OAIPercent &standard_deviation);
    bool is_standard_deviation_Set() const;
    bool is_standard_deviation_Valid() const;

    OAIFormattedLifestyleType getType() const;
    void setType(const OAIFormattedLifestyleType &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_after_tax_proceeds_account_name;
    bool m_after_tax_proceeds_account_name_isSet;
    bool m_after_tax_proceeds_account_name_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAICurrency m_future_value_projected_gross_sale_value;
    bool m_future_value_projected_gross_sale_value_isSet;
    bool m_future_value_projected_gross_sale_value_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_major_purchase_goal;
    bool m_is_major_purchase_goal_isSet;
    bool m_is_major_purchase_goal_isValid;

    OAICurrencyWithDate m_market_value_as_of;
    bool m_market_value_as_of_isSet;
    bool m_market_value_as_of_isValid;

    QString m_owner;
    bool m_owner_isSet;
    bool m_owner_isValid;

    OAIPercent m_pre_tax_growth_rate;
    bool m_pre_tax_growth_rate_isSet;
    bool m_pre_tax_growth_rate_isValid;

    OAICurrency m_present_value_projected_gross_sale_value;
    bool m_present_value_projected_gross_sale_value_isSet;
    bool m_present_value_projected_gross_sale_value_isValid;

    OAIDate m_projected_sale_date;
    bool m_projected_sale_date_isSet;
    bool m_projected_sale_date_isValid;

    OAICurrency m_purchase_amount;
    bool m_purchase_amount_isSet;
    bool m_purchase_amount_isValid;

    OAIDate m_purchase_date;
    bool m_purchase_date_isSet;
    bool m_purchase_date_isValid;

    OAIPercent m_selling_cost_percent;
    bool m_selling_cost_percent_isSet;
    bool m_selling_cost_percent_isValid;

    OAIPercent m_standard_deviation;
    bool m_standard_deviation_isSet;
    bool m_standard_deviation_isValid;

    OAIFormattedLifestyleType m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIILifestyleAsset)

#endif // OAIILifestyleAsset_H
