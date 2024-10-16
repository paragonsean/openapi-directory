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
 * OAIICashFlow.h
 *
 * 
 */

#ifndef OAIICashFlow_H
#define OAIICashFlow_H

#include <QJsonObject>

#include "OAICurrency.h"
#include "OAIICashFlowIncomes.h"
#include "OAIICashFlowOutflows.h"
#include "OAIITaxes.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIICashFlowIncomes;
class OAIICashFlowOutflows;
class OAICurrency;
class OAIITaxes;

class OAIICashFlow : public OAIObject {
public:
    OAIICashFlow();
    OAIICashFlow(QString json);
    ~OAIICashFlow() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIICashFlowIncomes getIncomes() const;
    void setIncomes(const OAIICashFlowIncomes &incomes);
    bool is_incomes_Set() const;
    bool is_incomes_Valid() const;

    OAIICashFlowOutflows getOutflows() const;
    void setOutflows(const OAIICashFlowOutflows &outflows);
    bool is_outflows_Set() const;
    bool is_outflows_Valid() const;

    OAICurrency getSurplusDeficit() const;
    void setSurplusDeficit(const OAICurrency &surplus_deficit);
    bool is_surplus_deficit_Set() const;
    bool is_surplus_deficit_Valid() const;

    OAIITaxes getTaxes() const;
    void setTaxes(const OAIITaxes &taxes);
    bool is_taxes_Set() const;
    bool is_taxes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIICashFlowIncomes m_incomes;
    bool m_incomes_isSet;
    bool m_incomes_isValid;

    OAIICashFlowOutflows m_outflows;
    bool m_outflows_isSet;
    bool m_outflows_isValid;

    OAICurrency m_surplus_deficit;
    bool m_surplus_deficit_isSet;
    bool m_surplus_deficit_isValid;

    OAIITaxes m_taxes;
    bool m_taxes_isSet;
    bool m_taxes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIICashFlow)

#endif // OAIICashFlow_H
