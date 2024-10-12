/**
 * Flight Choice Prediction
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 2.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPrice.h
 *
 * 
 */

#ifndef OAIPrice_H
#define OAIPrice_H

#include <QJsonObject>

#include "OAIFee.h"
#include "OAITax.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIFee;
class OAITax;

class OAIPrice : public OAIObject {
public:
    OAIPrice();
    OAIPrice(QString json);
    ~OAIPrice() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBase() const;
    void setBase(const QString &base);
    bool is_base_Set() const;
    bool is_base_Valid() const;

    QString getCurrency() const;
    void setCurrency(const QString &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    QList<OAIFee> getFees() const;
    void setFees(const QList<OAIFee> &fees);
    bool is_fees_Set() const;
    bool is_fees_Valid() const;

    QList<OAITax> getTaxes() const;
    void setTaxes(const QList<OAITax> &taxes);
    bool is_taxes_Set() const;
    bool is_taxes_Valid() const;

    QString getTotal() const;
    void setTotal(const QString &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_base;
    bool m_base_isSet;
    bool m_base_isValid;

    QString m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    QList<OAIFee> m_fees;
    bool m_fees_isSet;
    bool m_fees_isValid;

    QList<OAITax> m_taxes;
    bool m_taxes_isSet;
    bool m_taxes_isValid;

    QString m_total;
    bool m_total_isSet;
    bool m_total_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPrice)

#endif // OAIPrice_H
