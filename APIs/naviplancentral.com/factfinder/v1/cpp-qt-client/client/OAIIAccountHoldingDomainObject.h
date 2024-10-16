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
 * OAIIAccountHoldingDomainObject.h
 *
 * 
 */

#ifndef OAIIAccountHoldingDomainObject_H
#define OAIIAccountHoldingDomainObject_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIIAccountHoldingDomainObject : public OAIObject {
public:
    OAIIAccountHoldingDomainObject();
    OAIIAccountHoldingDomainObject(QString json);
    ~OAIIAccountHoldingDomainObject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAccountHoldingId() const;
    void setAccountHoldingId(const qint32 &account_holding_id);
    bool is_account_holding_id_Set() const;
    bool is_account_holding_id_Valid() const;

    qint32 getAccountId() const;
    void setAccountId(const qint32 &account_id);
    bool is_account_id_Set() const;
    bool is_account_id_Valid() const;

    double getCostBasis() const;
    void setCostBasis(const double &cost_basis);
    bool is_cost_basis_Set() const;
    bool is_cost_basis_Valid() const;

    QString getCusip() const;
    void setCusip(const QString &cusip);
    bool is_cusip_Set() const;
    bool is_cusip_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getExternalDestinationId() const;
    void setExternalDestinationId(const QString &external_destination_id);
    bool is_external_destination_id_Set() const;
    bool is_external_destination_id_Valid() const;

    bool isHeldAway() const;
    void setHeldAway(const bool &held_away);
    bool is_held_away_Set() const;
    bool is_held_away_Valid() const;

    double getMarketValue() const;
    void setMarketValue(const double &market_value);
    bool is_market_value_Set() const;
    bool is_market_value_Valid() const;

    QString getSymbol() const;
    void setSymbol(const QString &symbol);
    bool is_symbol_Set() const;
    bool is_symbol_Valid() const;

    QDateTime getValuationDate() const;
    void setValuationDate(const QDateTime &valuation_date);
    bool is_valuation_date_Set() const;
    bool is_valuation_date_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_account_holding_id;
    bool m_account_holding_id_isSet;
    bool m_account_holding_id_isValid;

    qint32 m_account_id;
    bool m_account_id_isSet;
    bool m_account_id_isValid;

    double m_cost_basis;
    bool m_cost_basis_isSet;
    bool m_cost_basis_isValid;

    QString m_cusip;
    bool m_cusip_isSet;
    bool m_cusip_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_external_destination_id;
    bool m_external_destination_id_isSet;
    bool m_external_destination_id_isValid;

    bool m_held_away;
    bool m_held_away_isSet;
    bool m_held_away_isValid;

    double m_market_value;
    bool m_market_value_isSet;
    bool m_market_value_isValid;

    QString m_symbol;
    bool m_symbol_isSet;
    bool m_symbol_isValid;

    QDateTime m_valuation_date;
    bool m_valuation_date_isSet;
    bool m_valuation_date_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIAccountHoldingDomainObject)

#endif // OAIIAccountHoldingDomainObject_H
