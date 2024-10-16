/**
 * GOV.UK Pay API
 * GOV.UK Pay API (This version is no longer maintained. See openapi/publicapi_spec.json for latest API specification)
 *
 * The version of the OpenAPI document: 1.0.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRefundDetailForSearch.h
 *
 * 
 */

#ifndef OAIRefundDetailForSearch_H
#define OAIRefundDetailForSearch_H

#include <QJsonObject>

#include "OAIRefundLinksForSearch.h"
#include "OAIRefundSettlementSummary.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIRefundLinksForSearch;
class OAIRefundSettlementSummary;

class OAIRefundDetailForSearch : public OAIObject {
public:
    OAIRefundDetailForSearch();
    OAIRefundDetailForSearch(QString json);
    ~OAIRefundDetailForSearch() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIRefundLinksForSearch getLinks() const;
    void setLinks(const OAIRefundLinksForSearch &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    qint64 getAmount() const;
    void setAmount(const qint64 &amount);
    bool is_amount_Set() const;
    bool is_amount_Valid() const;

    QString getCreatedDate() const;
    void setCreatedDate(const QString &created_date);
    bool is_created_date_Set() const;
    bool is_created_date_Valid() const;

    QString getRefundId() const;
    void setRefundId(const QString &refund_id);
    bool is_refund_id_Set() const;
    bool is_refund_id_Valid() const;

    OAIRefundSettlementSummary getSettlementSummary() const;
    void setSettlementSummary(const OAIRefundSettlementSummary &settlement_summary);
    bool is_settlement_summary_Set() const;
    bool is_settlement_summary_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIRefundLinksForSearch m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    qint64 m_amount;
    bool m_amount_isSet;
    bool m_amount_isValid;

    QString m_created_date;
    bool m_created_date_isSet;
    bool m_created_date_isValid;

    QString m_refund_id;
    bool m_refund_id_isSet;
    bool m_refund_id_isValid;

    OAIRefundSettlementSummary m_settlement_summary;
    bool m_settlement_summary_isSet;
    bool m_settlement_summary_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRefundDetailForSearch)

#endif // OAIRefundDetailForSearch_H
