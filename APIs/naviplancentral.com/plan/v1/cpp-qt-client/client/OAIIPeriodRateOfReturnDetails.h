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
 * OAIIPeriodRateOfReturnDetails.h
 *
 * 
 */

#ifndef OAIIPeriodRateOfReturnDetails_H
#define OAIIPeriodRateOfReturnDetails_H

#include <QJsonObject>

#include "OAIIRateOfReturnBreakdown.h"
#include "OAIPercent.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIIRateOfReturnBreakdown;
class OAIPercent;

class OAIIPeriodRateOfReturnDetails : public OAIObject {
public:
    OAIIPeriodRateOfReturnDetails();
    OAIIPeriodRateOfReturnDetails(QString json);
    ~OAIIPeriodRateOfReturnDetails() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIIRateOfReturnBreakdown getBreakdown() const;
    void setBreakdown(const OAIIRateOfReturnBreakdown &breakdown);
    bool is_breakdown_Set() const;
    bool is_breakdown_Valid() const;

    OAIPercent getStandardDeviation() const;
    void setStandardDeviation(const OAIPercent &standard_deviation);
    bool is_standard_deviation_Set() const;
    bool is_standard_deviation_Valid() const;

    OAIPercent getTotal() const;
    void setTotal(const OAIPercent &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIIRateOfReturnBreakdown m_breakdown;
    bool m_breakdown_isSet;
    bool m_breakdown_isValid;

    OAIPercent m_standard_deviation;
    bool m_standard_deviation_isSet;
    bool m_standard_deviation_isValid;

    OAIPercent m_total;
    bool m_total_isSet;
    bool m_total_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIPeriodRateOfReturnDetails)

#endif // OAIIPeriodRateOfReturnDetails_H
