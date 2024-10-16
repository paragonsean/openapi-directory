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
 * OAIGetDailySettlementStatsOut.h
 *
 * 
 */

#ifndef OAIGetDailySettlementStatsOut_H
#define OAIGetDailySettlementStatsOut_H

#include <QJsonObject>

#include "OAISettlement_daily_stats_schema.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISettlement_daily_stats_schema;

class OAIGetDailySettlementStatsOut : public OAIObject {
public:
    OAIGetDailySettlementStatsOut();
    OAIGetDailySettlementStatsOut(QString json);
    ~OAIGetDailySettlementStatsOut() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAISettlement_daily_stats_schema> getSettlementDaily() const;
    void setSettlementDaily(const QList<OAISettlement_daily_stats_schema> &settlement_daily);
    bool is_settlement_daily_Set() const;
    bool is_settlement_daily_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAISettlement_daily_stats_schema> m_settlement_daily;
    bool m_settlement_daily_isSet;
    bool m_settlement_daily_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetDailySettlementStatsOut)

#endif // OAIGetDailySettlementStatsOut_H
