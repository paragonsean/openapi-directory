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
 * OAICalculateSimpleTaxIn.h
 *
 * 
 */

#ifndef OAICalculateSimpleTaxIn_H
#define OAICalculateSimpleTaxIn_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICalculateSimpleTaxIn : public OAIObject {
public:
    OAICalculateSimpleTaxIn();
    OAICalculateSimpleTaxIn(QString json);
    ~OAICalculateSimpleTaxIn() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getAmount() const;
    void setAmount(const double &amount);
    bool is_amount_Set() const;
    bool is_amount_Valid() const;

    QString getBillingCountryCode() const;
    void setBillingCountryCode(const QString &billing_country_code);
    bool is_billing_country_code_Set() const;
    bool is_billing_country_code_Valid() const;

    QString getBuyerCreditCardPrefix() const;
    void setBuyerCreditCardPrefix(const QString &buyer_credit_card_prefix);
    bool is_buyer_credit_card_prefix_Set() const;
    bool is_buyer_credit_card_prefix_Valid() const;

    QString getBuyerTaxNumber() const;
    void setBuyerTaxNumber(const QString &buyer_tax_number);
    bool is_buyer_tax_number_Set() const;
    bool is_buyer_tax_number_Valid() const;

    QString getCurrencyCode() const;
    void setCurrencyCode(const QString &currency_code);
    bool is_currency_code_Set() const;
    bool is_currency_code_Valid() const;

    QString getForceCountryCode() const;
    void setForceCountryCode(const QString &force_country_code);
    bool is_force_country_code_Set() const;
    bool is_force_country_code_Valid() const;

    QString getInvoiceAddressCity() const;
    void setInvoiceAddressCity(const QString &invoice_address_city);
    bool is_invoice_address_city_Set() const;
    bool is_invoice_address_city_Valid() const;

    QString getInvoiceAddressPostalCode() const;
    void setInvoiceAddressPostalCode(const QString &invoice_address_postal_code);
    bool is_invoice_address_postal_code_Set() const;
    bool is_invoice_address_postal_code_Valid() const;

    QString getInvoiceAddressRegion() const;
    void setInvoiceAddressRegion(const QString &invoice_address_region);
    bool is_invoice_address_region_Set() const;
    bool is_invoice_address_region_Valid() const;

    QString getOrderDate() const;
    void setOrderDate(const QString &order_date);
    bool is_order_date_Set() const;
    bool is_order_date_Valid() const;

    QString getProductType() const;
    void setProductType(const QString &product_type);
    bool is_product_type_Set() const;
    bool is_product_type_Valid() const;

    double getQuantity() const;
    void setQuantity(const double &quantity);
    bool is_quantity_Set() const;
    bool is_quantity_Valid() const;

    bool isTaxDeducted() const;
    void setTaxDeducted(const bool &tax_deducted);
    bool is_tax_deducted_Set() const;
    bool is_tax_deducted_Valid() const;

    double getTotalAmount() const;
    void setTotalAmount(const double &total_amount);
    bool is_total_amount_Set() const;
    bool is_total_amount_Valid() const;

    double getUnitPrice() const;
    void setUnitPrice(const double &unit_price);
    bool is_unit_price_Set() const;
    bool is_unit_price_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_amount;
    bool m_amount_isSet;
    bool m_amount_isValid;

    QString m_billing_country_code;
    bool m_billing_country_code_isSet;
    bool m_billing_country_code_isValid;

    QString m_buyer_credit_card_prefix;
    bool m_buyer_credit_card_prefix_isSet;
    bool m_buyer_credit_card_prefix_isValid;

    QString m_buyer_tax_number;
    bool m_buyer_tax_number_isSet;
    bool m_buyer_tax_number_isValid;

    QString m_currency_code;
    bool m_currency_code_isSet;
    bool m_currency_code_isValid;

    QString m_force_country_code;
    bool m_force_country_code_isSet;
    bool m_force_country_code_isValid;

    QString m_invoice_address_city;
    bool m_invoice_address_city_isSet;
    bool m_invoice_address_city_isValid;

    QString m_invoice_address_postal_code;
    bool m_invoice_address_postal_code_isSet;
    bool m_invoice_address_postal_code_isValid;

    QString m_invoice_address_region;
    bool m_invoice_address_region_isSet;
    bool m_invoice_address_region_isValid;

    QString m_order_date;
    bool m_order_date_isSet;
    bool m_order_date_isValid;

    QString m_product_type;
    bool m_product_type_isSet;
    bool m_product_type_isValid;

    double m_quantity;
    bool m_quantity_isSet;
    bool m_quantity_isValid;

    bool m_tax_deducted;
    bool m_tax_deducted_isSet;
    bool m_tax_deducted_isValid;

    double m_total_amount;
    bool m_total_amount_isSet;
    bool m_total_amount_isValid;

    double m_unit_price;
    bool m_unit_price_isSet;
    bool m_unit_price_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICalculateSimpleTaxIn)

#endif // OAICalculateSimpleTaxIn_H
