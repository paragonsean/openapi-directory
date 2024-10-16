/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIFactFinderSnapshotDomainObject.h
 *
 * 
 */

#ifndef OAIIFactFinderSnapshotDomainObject_H
#define OAIIFactFinderSnapshotDomainObject_H

#include <QJsonObject>

#include "OAIIAccountWithSubEntitiesDomainObject.h"
#include "OAIICriticalIllnessInsurancePolicyDomainObject.h"
#include "OAIIDemographicsWithDependentsDomainObject.h"
#include "OAIIDisabilityInsurancePolicyDomainObject.h"
#include "OAIIEducationGoalWithExpensesDomainObject.h"
#include "OAIIExpenseDomainObject.h"
#include "OAIIFactFinderDefinedBenefitPensionDomainObject.h"
#include "OAIIFactFinderLiabilityDomainObject.h"
#include "OAIIFactFinderLifestyleAssetDomainObject.h"
#include "OAIIIncomeDomainObject.h"
#include "OAIILifeInsurancePolicyDomainObject.h"
#include "OAIILongTermCareInsurancePolicyDomainObject.h"
#include "OAIIMajorPurchaseGoalDomainObject.h"
#include "OAIIRealEstateAssetDomainObject.h"
#include "OAIIRetirementGoalWithExpensesDomainObject.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIAccountWithSubEntitiesDomainObject;
class OAIICriticalIllnessInsurancePolicyDomainObject;
class OAIIFactFinderDefinedBenefitPensionDomainObject;
class OAIIDemographicsWithDependentsDomainObject;
class OAIIDisabilityInsurancePolicyDomainObject;
class OAIIEducationGoalWithExpensesDomainObject;
class OAIIExpenseDomainObject;
class OAIIIncomeDomainObject;
class OAIIFactFinderLiabilityDomainObject;
class OAIILifeInsurancePolicyDomainObject;
class OAIIFactFinderLifestyleAssetDomainObject;
class OAIILongTermCareInsurancePolicyDomainObject;
class OAIIMajorPurchaseGoalDomainObject;
class OAIIRealEstateAssetDomainObject;
class OAIIRetirementGoalWithExpensesDomainObject;

class OAIIFactFinderSnapshotDomainObject : public OAIObject {
public:
    OAIIFactFinderSnapshotDomainObject();
    OAIIFactFinderSnapshotDomainObject(QString json);
    ~OAIIFactFinderSnapshotDomainObject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIIAccountWithSubEntitiesDomainObject> getAccounts() const;
    void setAccounts(const QList<OAIIAccountWithSubEntitiesDomainObject> &accounts);
    bool is_accounts_Set() const;
    bool is_accounts_Valid() const;

    QList<OAIICriticalIllnessInsurancePolicyDomainObject> getCriticalIllnessInsurancePolicies() const;
    void setCriticalIllnessInsurancePolicies(const QList<OAIICriticalIllnessInsurancePolicyDomainObject> &critical_illness_insurance_policies);
    bool is_critical_illness_insurance_policies_Set() const;
    bool is_critical_illness_insurance_policies_Valid() const;

    QList<OAIIFactFinderDefinedBenefitPensionDomainObject> getDefinedBenefitPensions() const;
    void setDefinedBenefitPensions(const QList<OAIIFactFinderDefinedBenefitPensionDomainObject> &defined_benefit_pensions);
    bool is_defined_benefit_pensions_Set() const;
    bool is_defined_benefit_pensions_Valid() const;

    OAIIDemographicsWithDependentsDomainObject getDemographics() const;
    void setDemographics(const OAIIDemographicsWithDependentsDomainObject &demographics);
    bool is_demographics_Set() const;
    bool is_demographics_Valid() const;

    QList<OAIIDisabilityInsurancePolicyDomainObject> getDisabilityInsurancePolicies() const;
    void setDisabilityInsurancePolicies(const QList<OAIIDisabilityInsurancePolicyDomainObject> &disability_insurance_policies);
    bool is_disability_insurance_policies_Set() const;
    bool is_disability_insurance_policies_Valid() const;

    QList<OAIIEducationGoalWithExpensesDomainObject> getEducationGoals() const;
    void setEducationGoals(const QList<OAIIEducationGoalWithExpensesDomainObject> &education_goals);
    bool is_education_goals_Set() const;
    bool is_education_goals_Valid() const;

    QList<OAIIExpenseDomainObject> getExpenses() const;
    void setExpenses(const QList<OAIIExpenseDomainObject> &expenses);
    bool is_expenses_Set() const;
    bool is_expenses_Valid() const;

    QList<OAIIIncomeDomainObject> getIncomes() const;
    void setIncomes(const QList<OAIIIncomeDomainObject> &incomes);
    bool is_incomes_Set() const;
    bool is_incomes_Valid() const;

    QList<OAIIFactFinderLiabilityDomainObject> getLiabilities() const;
    void setLiabilities(const QList<OAIIFactFinderLiabilityDomainObject> &liabilities);
    bool is_liabilities_Set() const;
    bool is_liabilities_Valid() const;

    QList<OAIILifeInsurancePolicyDomainObject> getLifeInsurancePolicies() const;
    void setLifeInsurancePolicies(const QList<OAIILifeInsurancePolicyDomainObject> &life_insurance_policies);
    bool is_life_insurance_policies_Set() const;
    bool is_life_insurance_policies_Valid() const;

    QList<OAIIFactFinderLifestyleAssetDomainObject> getLifestyleAssets() const;
    void setLifestyleAssets(const QList<OAIIFactFinderLifestyleAssetDomainObject> &lifestyle_assets);
    bool is_lifestyle_assets_Set() const;
    bool is_lifestyle_assets_Valid() const;

    QList<OAIILongTermCareInsurancePolicyDomainObject> getLongTermCareInsurancePolicies() const;
    void setLongTermCareInsurancePolicies(const QList<OAIILongTermCareInsurancePolicyDomainObject> &long_term_care_insurance_policies);
    bool is_long_term_care_insurance_policies_Set() const;
    bool is_long_term_care_insurance_policies_Valid() const;

    QList<OAIIMajorPurchaseGoalDomainObject> getMajorPurchaseGoals() const;
    void setMajorPurchaseGoals(const QList<OAIIMajorPurchaseGoalDomainObject> &major_purchase_goals);
    bool is_major_purchase_goals_Set() const;
    bool is_major_purchase_goals_Valid() const;

    qint32 getPlanYear() const;
    void setPlanYear(const qint32 &plan_year);
    bool is_plan_year_Set() const;
    bool is_plan_year_Valid() const;

    QList<OAIIRealEstateAssetDomainObject> getRealEstateAssets() const;
    void setRealEstateAssets(const QList<OAIIRealEstateAssetDomainObject> &real_estate_assets);
    bool is_real_estate_assets_Set() const;
    bool is_real_estate_assets_Valid() const;

    OAIIRetirementGoalWithExpensesDomainObject getRetirementGoal() const;
    void setRetirementGoal(const OAIIRetirementGoalWithExpensesDomainObject &retirement_goal);
    bool is_retirement_goal_Set() const;
    bool is_retirement_goal_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIIAccountWithSubEntitiesDomainObject> m_accounts;
    bool m_accounts_isSet;
    bool m_accounts_isValid;

    QList<OAIICriticalIllnessInsurancePolicyDomainObject> m_critical_illness_insurance_policies;
    bool m_critical_illness_insurance_policies_isSet;
    bool m_critical_illness_insurance_policies_isValid;

    QList<OAIIFactFinderDefinedBenefitPensionDomainObject> m_defined_benefit_pensions;
    bool m_defined_benefit_pensions_isSet;
    bool m_defined_benefit_pensions_isValid;

    OAIIDemographicsWithDependentsDomainObject m_demographics;
    bool m_demographics_isSet;
    bool m_demographics_isValid;

    QList<OAIIDisabilityInsurancePolicyDomainObject> m_disability_insurance_policies;
    bool m_disability_insurance_policies_isSet;
    bool m_disability_insurance_policies_isValid;

    QList<OAIIEducationGoalWithExpensesDomainObject> m_education_goals;
    bool m_education_goals_isSet;
    bool m_education_goals_isValid;

    QList<OAIIExpenseDomainObject> m_expenses;
    bool m_expenses_isSet;
    bool m_expenses_isValid;

    QList<OAIIIncomeDomainObject> m_incomes;
    bool m_incomes_isSet;
    bool m_incomes_isValid;

    QList<OAIIFactFinderLiabilityDomainObject> m_liabilities;
    bool m_liabilities_isSet;
    bool m_liabilities_isValid;

    QList<OAIILifeInsurancePolicyDomainObject> m_life_insurance_policies;
    bool m_life_insurance_policies_isSet;
    bool m_life_insurance_policies_isValid;

    QList<OAIIFactFinderLifestyleAssetDomainObject> m_lifestyle_assets;
    bool m_lifestyle_assets_isSet;
    bool m_lifestyle_assets_isValid;

    QList<OAIILongTermCareInsurancePolicyDomainObject> m_long_term_care_insurance_policies;
    bool m_long_term_care_insurance_policies_isSet;
    bool m_long_term_care_insurance_policies_isValid;

    QList<OAIIMajorPurchaseGoalDomainObject> m_major_purchase_goals;
    bool m_major_purchase_goals_isSet;
    bool m_major_purchase_goals_isValid;

    qint32 m_plan_year;
    bool m_plan_year_isSet;
    bool m_plan_year_isValid;

    QList<OAIIRealEstateAssetDomainObject> m_real_estate_assets;
    bool m_real_estate_assets_isSet;
    bool m_real_estate_assets_isValid;

    OAIIRetirementGoalWithExpensesDomainObject m_retirement_goal;
    bool m_retirement_goal_isSet;
    bool m_retirement_goal_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIFactFinderSnapshotDomainObject)

#endif // OAIIFactFinderSnapshotDomainObject_H
