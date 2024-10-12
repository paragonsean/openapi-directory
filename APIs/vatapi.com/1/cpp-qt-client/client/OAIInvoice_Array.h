/**
 * VAT API
 * A developer friendly API to help your business achieve VAT compliance
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIInvoice_Array.h
 *
 * 
 */

#ifndef OAIInvoice_Array_H
#define OAIInvoice_Array_H

#include <QJsonObject>

#include "OAIInvoice_Items.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIInvoice_Items;

class OAIInvoice_Array : public OAIObject {
public:
    OAIInvoice_Array();
    OAIInvoice_Array(QString json);
    ~OAIInvoice_Array() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBusinessAddress() const;
    void setBusinessAddress(const QString &business_address);
    bool is_business_address_Set() const;
    bool is_business_address_Valid() const;

    QString getBusinessName() const;
    void setBusinessName(const QString &business_name);
    bool is_business_name_Set() const;
    bool is_business_name_Valid() const;

    qint32 getConversionRate() const;
    void setConversionRate(const qint32 &conversion_rate);
    bool is_conversion_rate_Set() const;
    bool is_conversion_rate_Valid() const;

    QString getCurrencyCode() const;
    void setCurrencyCode(const QString &currency_code);
    bool is_currency_code_Set() const;
    bool is_currency_code_Valid() const;

    QString getCurrencyCodeConversion() const;
    void setCurrencyCodeConversion(const QString &currency_code_conversion);
    bool is_currency_code_conversion_Set() const;
    bool is_currency_code_conversion_Valid() const;

    QString getCustomerAddress() const;
    void setCustomerAddress(const QString &customer_address);
    bool is_customer_address_Set() const;
    bool is_customer_address_Valid() const;

    QString getCustomerName() const;
    void setCustomerName(const QString &customer_name);
    bool is_customer_name_Set() const;
    bool is_customer_name_Valid() const;

    QString getCustomerVatNumber() const;
    void setCustomerVatNumber(const QString &customer_vat_number);
    bool is_customer_vat_number_Set() const;
    bool is_customer_vat_number_Valid() const;

    QString getDate() const;
    void setDate(const QString &date);
    bool is_date_Set() const;
    bool is_date_Valid() const;

    qint32 getDiscountRate() const;
    void setDiscountRate(const qint32 &discount_rate);
    bool is_discount_rate_Set() const;
    bool is_discount_rate_Valid() const;

    qint32 getDiscountTotal() const;
    void setDiscountTotal(const qint32 &discount_total);
    bool is_discount_total_Set() const;
    bool is_discount_total_Valid() const;

    qint32 getInvoiceNumber() const;
    void setInvoiceNumber(const qint32 &invoice_number);
    bool is_invoice_number_Set() const;
    bool is_invoice_number_Valid() const;

    QString getInvoiceUrl() const;
    void setInvoiceUrl(const QString &invoice_url);
    bool is_invoice_url_Set() const;
    bool is_invoice_url_Valid() const;

    QList<OAIInvoice_Items> getItems() const;
    void setItems(const QList<OAIInvoice_Items> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    QString getLogoUrl() const;
    void setLogoUrl(const QString &logo_url);
    bool is_logo_url_Set() const;
    bool is_logo_url_Valid() const;

    QString getNotes() const;
    void setNotes(const QString &notes);
    bool is_notes_Set() const;
    bool is_notes_Valid() const;

    qint32 getSubtotal() const;
    void setSubtotal(const qint32 &subtotal);
    bool is_subtotal_Set() const;
    bool is_subtotal_Valid() const;

    QString getTaxPoint() const;
    void setTaxPoint(const QString &tax_point);
    bool is_tax_point_Set() const;
    bool is_tax_point_Valid() const;

    qint32 getTotal() const;
    void setTotal(const qint32 &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getVatNumber() const;
    void setVatNumber(const QString &vat_number);
    bool is_vat_number_Set() const;
    bool is_vat_number_Valid() const;

    qint32 getVatTotal() const;
    void setVatTotal(const qint32 &vat_total);
    bool is_vat_total_Set() const;
    bool is_vat_total_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_business_address;
    bool m_business_address_isSet;
    bool m_business_address_isValid;

    QString m_business_name;
    bool m_business_name_isSet;
    bool m_business_name_isValid;

    qint32 m_conversion_rate;
    bool m_conversion_rate_isSet;
    bool m_conversion_rate_isValid;

    QString m_currency_code;
    bool m_currency_code_isSet;
    bool m_currency_code_isValid;

    QString m_currency_code_conversion;
    bool m_currency_code_conversion_isSet;
    bool m_currency_code_conversion_isValid;

    QString m_customer_address;
    bool m_customer_address_isSet;
    bool m_customer_address_isValid;

    QString m_customer_name;
    bool m_customer_name_isSet;
    bool m_customer_name_isValid;

    QString m_customer_vat_number;
    bool m_customer_vat_number_isSet;
    bool m_customer_vat_number_isValid;

    QString m_date;
    bool m_date_isSet;
    bool m_date_isValid;

    qint32 m_discount_rate;
    bool m_discount_rate_isSet;
    bool m_discount_rate_isValid;

    qint32 m_discount_total;
    bool m_discount_total_isSet;
    bool m_discount_total_isValid;

    qint32 m_invoice_number;
    bool m_invoice_number_isSet;
    bool m_invoice_number_isValid;

    QString m_invoice_url;
    bool m_invoice_url_isSet;
    bool m_invoice_url_isValid;

    QList<OAIInvoice_Items> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    QString m_logo_url;
    bool m_logo_url_isSet;
    bool m_logo_url_isValid;

    QString m_notes;
    bool m_notes_isSet;
    bool m_notes_isValid;

    qint32 m_subtotal;
    bool m_subtotal_isSet;
    bool m_subtotal_isValid;

    QString m_tax_point;
    bool m_tax_point_isSet;
    bool m_tax_point_isValid;

    qint32 m_total;
    bool m_total_isSet;
    bool m_total_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_vat_number;
    bool m_vat_number_isSet;
    bool m_vat_number_isValid;

    qint32 m_vat_total;
    bool m_vat_total_isSet;
    bool m_vat_total_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInvoice_Array)

#endif // OAIInvoice_Array_H
