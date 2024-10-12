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
 * OAIWebhookDeliveryLogResource_relationships.h
 *
 * 
 */

#ifndef OAIWebhookDeliveryLogResource_relationships_H
#define OAIWebhookDeliveryLogResource_relationships_H

#include <QJsonObject>

#include "OAIWebhookDeliveryLogResource_relationships_webhookEvent.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWebhookDeliveryLogResource_relationships_webhookEvent;

class OAIWebhookDeliveryLogResource_relationships : public OAIObject {
public:
    OAIWebhookDeliveryLogResource_relationships();
    OAIWebhookDeliveryLogResource_relationships(QString json);
    ~OAIWebhookDeliveryLogResource_relationships() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIWebhookDeliveryLogResource_relationships_webhookEvent getWebhookEvent() const;
    void setWebhookEvent(const OAIWebhookDeliveryLogResource_relationships_webhookEvent &webhook_event);
    bool is_webhook_event_Set() const;
    bool is_webhook_event_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIWebhookDeliveryLogResource_relationships_webhookEvent m_webhook_event;
    bool m_webhook_event_isSet;
    bool m_webhook_event_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebhookDeliveryLogResource_relationships)

#endif // OAIWebhookDeliveryLogResource_relationships_H
