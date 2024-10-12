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
 * OAIRoundUpObject.h
 *
 * Provides information about how a Round Up was applied, such as whether or not a boost was included in the Round Up. 
 */

#ifndef OAIRoundUpObject_H
#define OAIRoundUpObject_H

#include <QJsonObject>

#include "OAIMoneyObject.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIMoneyObject;

class OAIRoundUpObject : public OAIObject {
public:
    OAIRoundUpObject();
    OAIRoundUpObject(QString json);
    ~OAIRoundUpObject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIMoneyObject getAmount() const;
    void setAmount(const OAIMoneyObject &amount);
    bool is_amount_Set() const;
    bool is_amount_Valid() const;

    OAIMoneyObject getBoostPortion() const;
    void setBoostPortion(const OAIMoneyObject &boost_portion);
    bool is_boost_portion_Set() const;
    bool is_boost_portion_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIMoneyObject m_amount;
    bool m_amount_isSet;
    bool m_amount_isValid;

    OAIMoneyObject m_boost_portion;
    bool m_boost_portion_isSet;
    bool m_boost_portion_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRoundUpObject)

#endif // OAIRoundUpObject_H
