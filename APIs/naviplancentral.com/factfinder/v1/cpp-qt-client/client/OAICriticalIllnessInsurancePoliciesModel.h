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
 * OAICriticalIllnessInsurancePoliciesModel.h
 *
 * 
 */

#ifndef OAICriticalIllnessInsurancePoliciesModel_H
#define OAICriticalIllnessInsurancePoliciesModel_H

#include <QJsonObject>

#include "OAICriticalIllnessInsurancePolicyWithIdModel.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICriticalIllnessInsurancePolicyWithIdModel;

class OAICriticalIllnessInsurancePoliciesModel : public OAIObject {
public:
    OAICriticalIllnessInsurancePoliciesModel();
    OAICriticalIllnessInsurancePoliciesModel(QString json);
    ~OAICriticalIllnessInsurancePoliciesModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAICriticalIllnessInsurancePolicyWithIdModel> getCriticalIllnessInsurancePolicies() const;
    void setCriticalIllnessInsurancePolicies(const QList<OAICriticalIllnessInsurancePolicyWithIdModel> &critical_illness_insurance_policies);
    bool is_critical_illness_insurance_policies_Set() const;
    bool is_critical_illness_insurance_policies_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAICriticalIllnessInsurancePolicyWithIdModel> m_critical_illness_insurance_policies;
    bool m_critical_illness_insurance_policies_isSet;
    bool m_critical_illness_insurance_policies_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICriticalIllnessInsurancePoliciesModel)

#endif // OAICriticalIllnessInsurancePoliciesModel_H
