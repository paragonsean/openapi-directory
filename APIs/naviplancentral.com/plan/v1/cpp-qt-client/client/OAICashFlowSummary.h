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
 * OAICashFlowSummary.h
 *
 * 
 */

#ifndef OAICashFlowSummary_H
#define OAICashFlowSummary_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICashFlowSummary : public OAIObject {
public:
    OAICashFlowSummary();
    OAICashFlowSummary(QString json);
    ~OAICashFlowSummary() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getSurplusDeficit() const;
    void setSurplusDeficit(const double &surplus_deficit);
    bool is_surplus_deficit_Set() const;
    bool is_surplus_deficit_Valid() const;

    double getTotalIncome() const;
    void setTotalIncome(const double &total_income);
    bool is_total_income_Set() const;
    bool is_total_income_Valid() const;

    double getTotalOutflowsWithTaxes() const;
    void setTotalOutflowsWithTaxes(const double &total_outflows_with_taxes);
    bool is_total_outflows_with_taxes_Set() const;
    bool is_total_outflows_with_taxes_Valid() const;

    double getTotalOutflowsWithoutTaxes() const;
    void setTotalOutflowsWithoutTaxes(const double &total_outflows_without_taxes);
    bool is_total_outflows_without_taxes_Set() const;
    bool is_total_outflows_without_taxes_Valid() const;

    double getTotalTaxes() const;
    void setTotalTaxes(const double &total_taxes);
    bool is_total_taxes_Set() const;
    bool is_total_taxes_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_surplus_deficit;
    bool m_surplus_deficit_isSet;
    bool m_surplus_deficit_isValid;

    double m_total_income;
    bool m_total_income_isSet;
    bool m_total_income_isValid;

    double m_total_outflows_with_taxes;
    bool m_total_outflows_with_taxes_isSet;
    bool m_total_outflows_with_taxes_isValid;

    double m_total_outflows_without_taxes;
    bool m_total_outflows_without_taxes_isSet;
    bool m_total_outflows_without_taxes_isValid;

    double m_total_taxes;
    bool m_total_taxes_isSet;
    bool m_total_taxes_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICashFlowSummary)

#endif // OAICashFlowSummary_H
