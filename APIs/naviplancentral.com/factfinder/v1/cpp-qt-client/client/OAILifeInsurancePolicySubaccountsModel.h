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
 * OAILifeInsurancePolicySubaccountsModel.h
 *
 * 
 */

#ifndef OAILifeInsurancePolicySubaccountsModel_H
#define OAILifeInsurancePolicySubaccountsModel_H

#include <QJsonObject>

#include "OAILifeInsurancePolicySubaccountWithIdModel.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILifeInsurancePolicySubaccountWithIdModel;

class OAILifeInsurancePolicySubaccountsModel : public OAIObject {
public:
    OAILifeInsurancePolicySubaccountsModel();
    OAILifeInsurancePolicySubaccountsModel(QString json);
    ~OAILifeInsurancePolicySubaccountsModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAILifeInsurancePolicySubaccountWithIdModel> getLifeInsurancePolicySubaccounts() const;
    void setLifeInsurancePolicySubaccounts(const QList<OAILifeInsurancePolicySubaccountWithIdModel> &life_insurance_policy_subaccounts);
    bool is_life_insurance_policy_subaccounts_Set() const;
    bool is_life_insurance_policy_subaccounts_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAILifeInsurancePolicySubaccountWithIdModel> m_life_insurance_policy_subaccounts;
    bool m_life_insurance_policy_subaccounts_isSet;
    bool m_life_insurance_policy_subaccounts_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILifeInsurancePolicySubaccountsModel)

#endif // OAILifeInsurancePolicySubaccountsModel_H
