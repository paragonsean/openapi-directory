/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetSettlementSummaryIn.h
 *
 * 
 */

#ifndef OAIGetSettlementSummaryIn_H
#define OAIGetSettlementSummaryIn_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetSettlementSummaryIn : public OAIObject {
public:
    OAIGetSettlementSummaryIn();
    OAIGetSettlementSummaryIn(QString json);
    ~OAIGetSettlementSummaryIn() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEndMonth() const;
    void setEndMonth(const QString &end_month);
    bool is_end_month_Set() const;
    bool is_end_month_Valid() const;

    QString getMossCountryCode() const;
    void setMossCountryCode(const QString &moss_country_code);
    bool is_moss_country_code_Set() const;
    bool is_moss_country_code_Valid() const;

    QString getStartMonth() const;
    void setStartMonth(const QString &start_month);
    bool is_start_month_Set() const;
    bool is_start_month_Valid() const;

    QString getTaxRegion() const;
    void setTaxRegion(const QString &tax_region);
    bool is_tax_region_Set() const;
    bool is_tax_region_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_end_month;
    bool m_end_month_isSet;
    bool m_end_month_isValid;

    QString m_moss_country_code;
    bool m_moss_country_code_isSet;
    bool m_moss_country_code_isValid;

    QString m_start_month;
    bool m_start_month_isSet;
    bool m_start_month_isValid;

    QString m_tax_region;
    bool m_tax_region_isSet;
    bool m_tax_region_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetSettlementSummaryIn)

#endif // OAIGetSettlementSummaryIn_H
