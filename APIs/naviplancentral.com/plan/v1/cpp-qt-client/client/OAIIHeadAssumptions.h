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
 * OAIIHeadAssumptions.h
 *
 * 
 */

#ifndef OAIIHeadAssumptions_H
#define OAIIHeadAssumptions_H

#include <QJsonObject>

#include "OAIDate.h"
#include "OAIFormattedMaritalOrTaxFilingStatus.h"
#include "OAIIGovernmentPensions.h"
#include "OAIIIncomeTaxes.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDate;
class OAIIIncomeTaxes;
class OAIIGovernmentPensions;
class OAIFormattedMaritalOrTaxFilingStatus;

class OAIIHeadAssumptions : public OAIObject {
public:
    OAIIHeadAssumptions();
    OAIIHeadAssumptions(QString json);
    ~OAIIHeadAssumptions() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAlreadyRetired() const;
    void setAlreadyRetired(const bool &already_retired);
    bool is_already_retired_Set() const;
    bool is_already_retired_Valid() const;

    qint32 getDeceasedAge() const;
    void setDeceasedAge(const qint32 &deceased_age);
    bool is_deceased_age_Set() const;
    bool is_deceased_age_Valid() const;

    OAIDate getDeceasedDate() const;
    void setDeceasedDate(const OAIDate &deceased_date);
    bool is_deceased_date_Set() const;
    bool is_deceased_date_Valid() const;

    OAIIIncomeTaxes getEstateIncomeTaxes() const;
    void setEstateIncomeTaxes(const OAIIIncomeTaxes &estate_income_taxes);
    bool is_estate_income_taxes_Set() const;
    bool is_estate_income_taxes_Valid() const;

    OAIIGovernmentPensions getGovernmentPensions() const;
    void setGovernmentPensions(const OAIIGovernmentPensions &government_pensions);
    bool is_government_pensions_Set() const;
    bool is_government_pensions_Valid() const;

    OAIFormattedMaritalOrTaxFilingStatus getMaritalOrTaxFilingStatus() const;
    void setMaritalOrTaxFilingStatus(const OAIFormattedMaritalOrTaxFilingStatus &marital_or_tax_filing_status);
    bool is_marital_or_tax_filing_status_Set() const;
    bool is_marital_or_tax_filing_status_Valid() const;

    OAIIIncomeTaxes getPreRetirementIncomeTaxes() const;
    void setPreRetirementIncomeTaxes(const OAIIIncomeTaxes &pre_retirement_income_taxes);
    bool is_pre_retirement_income_taxes_Set() const;
    bool is_pre_retirement_income_taxes_Valid() const;

    qint32 getRetirementAge() const;
    void setRetirementAge(const qint32 &retirement_age);
    bool is_retirement_age_Set() const;
    bool is_retirement_age_Valid() const;

    OAIDate getRetirementDate() const;
    void setRetirementDate(const OAIDate &retirement_date);
    bool is_retirement_date_Set() const;
    bool is_retirement_date_Valid() const;

    OAIIIncomeTaxes getRetirementIncomeTaxes() const;
    void setRetirementIncomeTaxes(const OAIIIncomeTaxes &retirement_income_taxes);
    bool is_retirement_income_taxes_Set() const;
    bool is_retirement_income_taxes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_already_retired;
    bool m_already_retired_isSet;
    bool m_already_retired_isValid;

    qint32 m_deceased_age;
    bool m_deceased_age_isSet;
    bool m_deceased_age_isValid;

    OAIDate m_deceased_date;
    bool m_deceased_date_isSet;
    bool m_deceased_date_isValid;

    OAIIIncomeTaxes m_estate_income_taxes;
    bool m_estate_income_taxes_isSet;
    bool m_estate_income_taxes_isValid;

    OAIIGovernmentPensions m_government_pensions;
    bool m_government_pensions_isSet;
    bool m_government_pensions_isValid;

    OAIFormattedMaritalOrTaxFilingStatus m_marital_or_tax_filing_status;
    bool m_marital_or_tax_filing_status_isSet;
    bool m_marital_or_tax_filing_status_isValid;

    OAIIIncomeTaxes m_pre_retirement_income_taxes;
    bool m_pre_retirement_income_taxes_isSet;
    bool m_pre_retirement_income_taxes_isValid;

    qint32 m_retirement_age;
    bool m_retirement_age_isSet;
    bool m_retirement_age_isValid;

    OAIDate m_retirement_date;
    bool m_retirement_date_isSet;
    bool m_retirement_date_isValid;

    OAIIIncomeTaxes m_retirement_income_taxes;
    bool m_retirement_income_taxes_isSet;
    bool m_retirement_income_taxes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIHeadAssumptions)

#endif // OAIIHeadAssumptions_H
