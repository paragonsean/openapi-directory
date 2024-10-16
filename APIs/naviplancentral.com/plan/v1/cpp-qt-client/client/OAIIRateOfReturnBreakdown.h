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
 * OAIIRateOfReturnBreakdown.h
 *
 * 
 */

#ifndef OAIIRateOfReturnBreakdown_H
#define OAIIRateOfReturnBreakdown_H

#include <QJsonObject>

#include "OAIPercent.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPercent;

class OAIIRateOfReturnBreakdown : public OAIObject {
public:
    OAIIRateOfReturnBreakdown();
    OAIIRateOfReturnBreakdown(QString json);
    ~OAIIRateOfReturnBreakdown() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPercent getCapitalGain() const;
    void setCapitalGain(const OAIPercent &capital_gain);
    bool is_capital_gain_Set() const;
    bool is_capital_gain_Valid() const;

    OAIPercent getDeferredGrowth() const;
    void setDeferredGrowth(const OAIPercent &deferred_growth);
    bool is_deferred_growth_Set() const;
    bool is_deferred_growth_Valid() const;

    OAIPercent getDividend() const;
    void setDividend(const OAIPercent &dividend);
    bool is_dividend_Set() const;
    bool is_dividend_Valid() const;

    OAIPercent getInterest() const;
    void setInterest(const OAIPercent &interest);
    bool is_interest_Set() const;
    bool is_interest_Valid() const;

    OAIPercent getTaxFree() const;
    void setTaxFree(const OAIPercent &tax_free);
    bool is_tax_free_Set() const;
    bool is_tax_free_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPercent m_capital_gain;
    bool m_capital_gain_isSet;
    bool m_capital_gain_isValid;

    OAIPercent m_deferred_growth;
    bool m_deferred_growth_isSet;
    bool m_deferred_growth_isValid;

    OAIPercent m_dividend;
    bool m_dividend_isSet;
    bool m_dividend_isValid;

    OAIPercent m_interest;
    bool m_interest_isSet;
    bool m_interest_isValid;

    OAIPercent m_tax_free;
    bool m_tax_free_isSet;
    bool m_tax_free_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIRateOfReturnBreakdown)

#endif // OAIIRateOfReturnBreakdown_H
