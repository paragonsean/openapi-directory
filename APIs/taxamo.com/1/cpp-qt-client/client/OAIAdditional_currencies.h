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
 * OAIAdditional_currencies.h
 *
 * 
 */

#ifndef OAIAdditional_currencies_H
#define OAIAdditional_currencies_H

#include <QJsonObject>

#include "OAIAdditional_currency.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAdditional_currency;

class OAIAdditional_currencies : public OAIObject {
public:
    OAIAdditional_currencies();
    OAIAdditional_currencies(QString json);
    ~OAIAdditional_currencies() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAdditional_currency getInvoice() const;
    void setInvoice(const OAIAdditional_currency &invoice);
    bool is_invoice_Set() const;
    bool is_invoice_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAdditional_currency m_invoice;
    bool m_invoice_isSet;
    bool m_invoice_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAdditional_currencies)

#endif // OAIAdditional_currencies_H
