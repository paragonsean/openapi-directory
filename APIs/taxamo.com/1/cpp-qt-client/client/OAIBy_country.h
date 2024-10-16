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
 * OAIBy_country.h
 *
 * 
 */

#ifndef OAIBy_country_H
#define OAIBy_country_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBy_country : public OAIObject {
public:
    OAIBy_country();
    OAIBy_country(QString json);
    ~OAIBy_country() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCurrencyCode() const;
    void setCurrencyCode(const QString &currency_code);
    bool is_currency_code_Set() const;
    bool is_currency_code_Valid() const;

    QString getTaxCountryCode() const;
    void setTaxCountryCode(const QString &tax_country_code);
    bool is_tax_country_code_Set() const;
    bool is_tax_country_code_Valid() const;

    QString getTaxCountryName() const;
    void setTaxCountryName(const QString &tax_country_name);
    bool is_tax_country_name_Set() const;
    bool is_tax_country_name_Valid() const;

    double getValue() const;
    void setValue(const double &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_currency_code;
    bool m_currency_code_isSet;
    bool m_currency_code_isValid;

    QString m_tax_country_code;
    bool m_tax_country_code_isSet;
    bool m_tax_country_code_isValid;

    QString m_tax_country_name;
    bool m_tax_country_name_isSet;
    bool m_tax_country_name_isValid;

    double m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBy_country)

#endif // OAIBy_country_H
