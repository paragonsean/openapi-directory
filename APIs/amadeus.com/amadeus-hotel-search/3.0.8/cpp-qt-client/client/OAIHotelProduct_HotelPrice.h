/**
 * Hotel Search API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 3.0.8
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIHotelProduct_HotelPrice.h
 *
 * price information
 */

#ifndef OAIHotelProduct_HotelPrice_H
#define OAIHotelProduct_HotelPrice_H

#include <QJsonObject>

#include "OAIHotelProduct_PriceVariations.h"
#include "OAIMarkup.h"
#include "OAITax.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMarkup;
class OAITax;
class OAIHotelProduct_PriceVariations;

class OAIHotelProduct_HotelPrice : public OAIObject {
public:
    OAIHotelProduct_HotelPrice();
    OAIHotelProduct_HotelPrice(QString json);
    ~OAIHotelProduct_HotelPrice() override;

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

    QList<OAIMarkup> getMarkups() const;
    void setMarkups(const QList<OAIMarkup> &markups);
    bool is_markups_Set() const;
    bool is_markups_Valid() const;

    QString getSellingTotal() const;
    void setSellingTotal(const QString &selling_total);
    bool is_selling_total_Set() const;
    bool is_selling_total_Valid() const;

    QList<OAITax> getTaxes() const;
    void setTaxes(const QList<OAITax> &taxes);
    bool is_taxes_Set() const;
    bool is_taxes_Valid() const;

    QString getTotal() const;
    void setTotal(const QString &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    OAIHotelProduct_PriceVariations getVariations() const;
    void setVariations(const OAIHotelProduct_PriceVariations &variations);
    bool is_variations_Set() const;
    bool is_variations_Valid() const;

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

    QList<OAIMarkup> m_markups;
    bool m_markups_isSet;
    bool m_markups_isValid;

    QString m_selling_total;
    bool m_selling_total_isSet;
    bool m_selling_total_isValid;

    QList<OAITax> m_taxes;
    bool m_taxes_isSet;
    bool m_taxes_isValid;

    QString m_total;
    bool m_total_isSet;
    bool m_total_isValid;

    OAIHotelProduct_PriceVariations m_variations;
    bool m_variations_isSet;
    bool m_variations_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHotelProduct_HotelPrice)

#endif // OAIHotelProduct_HotelPrice_H
