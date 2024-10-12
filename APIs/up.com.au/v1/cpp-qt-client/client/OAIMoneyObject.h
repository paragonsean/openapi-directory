/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIMoneyObject.h
 *
 * Provides information about a value of money. 
 */

#ifndef OAIMoneyObject_H
#define OAIMoneyObject_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIMoneyObject : public OAIObject {
public:
    OAIMoneyObject();
    OAIMoneyObject(QString json);
    ~OAIMoneyObject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCurrencyCode() const;
    void setCurrencyCode(const QString &currency_code);
    bool is_currency_code_Set() const;
    bool is_currency_code_Valid() const;

    QString getValue() const;
    void setValue(const QString &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    qint32 getValueInBaseUnits() const;
    void setValueInBaseUnits(const qint32 &value_in_base_units);
    bool is_value_in_base_units_Set() const;
    bool is_value_in_base_units_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_currency_code;
    bool m_currency_code_isSet;
    bool m_currency_code_isValid;

    QString m_value;
    bool m_value_isSet;
    bool m_value_isValid;

    qint32 m_value_in_base_units;
    bool m_value_in_base_units_isSet;
    bool m_value_in_base_units_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIMoneyObject)

#endif // OAIMoneyObject_H
