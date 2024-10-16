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
 * OAIIAssumptions.h
 *
 * 
 */

#ifndef OAIIAssumptions_H
#define OAIIAssumptions_H

#include <QJsonObject>

#include "OAIDate.h"
#include "OAIIBucketing.h"
#include "OAIIHeadAssumptions.h"
#include "OAIPercent.h"
#include "OAIYear.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIBucketing;
class OAIIHeadAssumptions;
class OAIDate;
class OAIPercent;
class OAIYear;

class OAIIAssumptions : public OAIObject {
public:
    OAIIAssumptions();
    OAIIAssumptions(QString json);
    ~OAIIAssumptions() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAnyHeadAlreadyRetired() const;
    void setAnyHeadAlreadyRetired(const bool &any_head_already_retired);
    bool is_any_head_already_retired_Set() const;
    bool is_any_head_already_retired_Valid() const;

    bool isBothRetired() const;
    void setBothRetired(const bool &both_retired);
    bool is_both_retired_Set() const;
    bool is_both_retired_Valid() const;

    OAIIBucketing getBucketing() const;
    void setBucketing(const OAIIBucketing &bucketing);
    bool is_bucketing_Set() const;
    bool is_bucketing_Valid() const;

    OAIIHeadAssumptions getClient() const;
    void setClient(const OAIIHeadAssumptions &client);
    bool is_client_Set() const;
    bool is_client_Valid() const;

    OAIIHeadAssumptions getCoClient() const;
    void setCoClient(const OAIIHeadAssumptions &co_client);
    bool is_co_client_Set() const;
    bool is_co_client_Valid() const;

    OAIDate getFirstToDieDate() const;
    void setFirstToDieDate(const OAIDate &first_to_die_date);
    bool is_first_to_die_date_Set() const;
    bool is_first_to_die_date_Valid() const;

    QString getFirstToDieMember() const;
    void setFirstToDieMember(const QString &first_to_die_member);
    bool is_first_to_die_member_Set() const;
    bool is_first_to_die_member_Valid() const;

    OAIDate getFirstToRetireDate() const;
    void setFirstToRetireDate(const OAIDate &first_to_retire_date);
    bool is_first_to_retire_date_Set() const;
    bool is_first_to_retire_date_Valid() const;

    OAIPercent getInflationRate() const;
    void setInflationRate(const OAIPercent &inflation_rate);
    bool is_inflation_rate_Set() const;
    bool is_inflation_rate_Valid() const;

    OAIDate getLastToDieDate() const;
    void setLastToDieDate(const OAIDate &last_to_die_date);
    bool is_last_to_die_date_Set() const;
    bool is_last_to_die_date_Valid() const;

    QString getLastToDieMember() const;
    void setLastToDieMember(const QString &last_to_die_member);
    bool is_last_to_die_member_Set() const;
    bool is_last_to_die_member_Valid() const;

    OAIDate getLastToRetireDate() const;
    void setLastToRetireDate(const OAIDate &last_to_retire_date);
    bool is_last_to_retire_date_Set() const;
    bool is_last_to_retire_date_Valid() const;

    OAIYear getRetirementYearAdjustedIfAlreadyRetired() const;
    void setRetirementYearAdjustedIfAlreadyRetired(const OAIYear &retirement_year_adjusted_if_already_retired);
    bool is_retirement_year_adjusted_if_already_retired_Set() const;
    bool is_retirement_year_adjusted_if_already_retired_Valid() const;

    bool isSplitSurplusSavingsStrategiesEnabled() const;
    void setSplitSurplusSavingsStrategiesEnabled(const bool &split_surplus_savings_strategies_enabled);
    bool is_split_surplus_savings_strategies_enabled_Set() const;
    bool is_split_surplus_savings_strategies_enabled_Valid() const;

    QString getTaxMethod() const;
    void setTaxMethod(const QString &tax_method);
    bool is_tax_method_Set() const;
    bool is_tax_method_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_any_head_already_retired;
    bool m_any_head_already_retired_isSet;
    bool m_any_head_already_retired_isValid;

    bool m_both_retired;
    bool m_both_retired_isSet;
    bool m_both_retired_isValid;

    OAIIBucketing m_bucketing;
    bool m_bucketing_isSet;
    bool m_bucketing_isValid;

    OAIIHeadAssumptions m_client;
    bool m_client_isSet;
    bool m_client_isValid;

    OAIIHeadAssumptions m_co_client;
    bool m_co_client_isSet;
    bool m_co_client_isValid;

    OAIDate m_first_to_die_date;
    bool m_first_to_die_date_isSet;
    bool m_first_to_die_date_isValid;

    QString m_first_to_die_member;
    bool m_first_to_die_member_isSet;
    bool m_first_to_die_member_isValid;

    OAIDate m_first_to_retire_date;
    bool m_first_to_retire_date_isSet;
    bool m_first_to_retire_date_isValid;

    OAIPercent m_inflation_rate;
    bool m_inflation_rate_isSet;
    bool m_inflation_rate_isValid;

    OAIDate m_last_to_die_date;
    bool m_last_to_die_date_isSet;
    bool m_last_to_die_date_isValid;

    QString m_last_to_die_member;
    bool m_last_to_die_member_isSet;
    bool m_last_to_die_member_isValid;

    OAIDate m_last_to_retire_date;
    bool m_last_to_retire_date_isSet;
    bool m_last_to_retire_date_isValid;

    OAIYear m_retirement_year_adjusted_if_already_retired;
    bool m_retirement_year_adjusted_if_already_retired_isSet;
    bool m_retirement_year_adjusted_if_already_retired_isValid;

    bool m_split_surplus_savings_strategies_enabled;
    bool m_split_surplus_savings_strategies_enabled_isSet;
    bool m_split_surplus_savings_strategies_enabled_isValid;

    QString m_tax_method;
    bool m_tax_method_isSet;
    bool m_tax_method_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIAssumptions)

#endif // OAIIAssumptions_H
