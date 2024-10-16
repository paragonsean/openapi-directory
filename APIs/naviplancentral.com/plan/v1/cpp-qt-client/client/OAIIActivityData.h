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
 * OAIIActivityData.h
 *
 * 
 */

#ifndef OAIIActivityData_H
#define OAIIActivityData_H

#include <QJsonObject>

#include "OAICurrencyWithGrowth.h"
#include "OAIFormattedDateRange.h"
#include "OAIIFormattedFrequency.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICurrencyWithGrowth;
class OAIFormattedDateRange;
class OAIIFormattedFrequency;

class OAIIActivityData : public OAIObject {
public:
    OAIIActivityData();
    OAIIActivityData(QString json);
    ~OAIIActivityData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAICurrencyWithGrowth getAmountWithGrowth() const;
    void setAmountWithGrowth(const OAICurrencyWithGrowth &amount_with_growth);
    bool is_amount_with_growth_Set() const;
    bool is_amount_with_growth_Valid() const;

    OAIFormattedDateRange getApplicableDateRange() const;
    void setApplicableDateRange(const OAIFormattedDateRange &applicable_date_range);
    bool is_applicable_date_range_Set() const;
    bool is_applicable_date_range_Valid() const;

    QString getDirectTo() const;
    void setDirectTo(const QString &direct_to);
    bool is_direct_to_Set() const;
    bool is_direct_to_Valid() const;

    OAIIFormattedFrequency getFrequency() const;
    void setFrequency(const OAIIFormattedFrequency &frequency);
    bool is_frequency_Set() const;
    bool is_frequency_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAICurrencyWithGrowth m_amount_with_growth;
    bool m_amount_with_growth_isSet;
    bool m_amount_with_growth_isValid;

    OAIFormattedDateRange m_applicable_date_range;
    bool m_applicable_date_range_isSet;
    bool m_applicable_date_range_isValid;

    QString m_direct_to;
    bool m_direct_to_isSet;
    bool m_direct_to_isValid;

    OAIIFormattedFrequency m_frequency;
    bool m_frequency_isSet;
    bool m_frequency_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIActivityData)

#endif // OAIIActivityData_H
