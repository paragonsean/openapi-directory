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
 * OAIWebhookEventResource_relationships.h
 *
 * 
 */

#ifndef OAIWebhookEventResource_relationships_H
#define OAIWebhookEventResource_relationships_H

#include <QJsonObject>

#include "OAIWebhookEventResource_relationships_transaction.h"
#include "OAIWebhookEventResource_relationships_webhook.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWebhookEventResource_relationships_transaction;
class OAIWebhookEventResource_relationships_webhook;

class OAIWebhookEventResource_relationships : public OAIObject {
public:
    OAIWebhookEventResource_relationships();
    OAIWebhookEventResource_relationships(QString json);
    ~OAIWebhookEventResource_relationships() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIWebhookEventResource_relationships_transaction getTransaction() const;
    void setTransaction(const OAIWebhookEventResource_relationships_transaction &transaction);
    bool is_transaction_Set() const;
    bool is_transaction_Valid() const;

    OAIWebhookEventResource_relationships_webhook getWebhook() const;
    void setWebhook(const OAIWebhookEventResource_relationships_webhook &webhook);
    bool is_webhook_Set() const;
    bool is_webhook_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIWebhookEventResource_relationships_transaction m_transaction;
    bool m_transaction_isSet;
    bool m_transaction_isValid;

    OAIWebhookEventResource_relationships_webhook m_webhook;
    bool m_webhook_isSet;
    bool m_webhook_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebhookEventResource_relationships)

#endif // OAIWebhookEventResource_relationships_H
