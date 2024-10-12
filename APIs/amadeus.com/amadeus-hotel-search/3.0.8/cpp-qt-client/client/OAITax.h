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
 * OAITax.h
 *
 * IATA Tax definition: An impost for raising revenue for the general treasury and which will be used for general public purposes.
 */

#ifndef OAITax_H
#define OAITax_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITax : public OAIObject {
public:
    OAITax();
    OAITax(QString json);
    ~OAITax() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAmount() const;
    void setAmount(const QString &amount);
    bool is_amount_Set() const;
    bool is_amount_Valid() const;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    QString getCurrency() const;
    void setCurrency(const QString &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    bool isIncluded() const;
    void setIncluded(const bool &included);
    bool is_included_Set() const;
    bool is_included_Valid() const;

    QString getPercentage() const;
    void setPercentage(const QString &percentage);
    bool is_percentage_Set() const;
    bool is_percentage_Valid() const;

    QString getPricingFrequency() const;
    void setPricingFrequency(const QString &pricing_frequency);
    bool is_pricing_frequency_Set() const;
    bool is_pricing_frequency_Valid() const;

    QString getPricingMode() const;
    void setPricingMode(const QString &pricing_mode);
    bool is_pricing_mode_Set() const;
    bool is_pricing_mode_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_amount;
    bool m_amount_isSet;
    bool m_amount_isValid;

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    QString m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    bool m_included;
    bool m_included_isSet;
    bool m_included_isValid;

    QString m_percentage;
    bool m_percentage_isSet;
    bool m_percentage_isValid;

    QString m_pricing_frequency;
    bool m_pricing_frequency_isSet;
    bool m_pricing_frequency_isValid;

    QString m_pricing_mode;
    bool m_pricing_mode_isSet;
    bool m_pricing_mode_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITax)

#endif // OAITax_H
