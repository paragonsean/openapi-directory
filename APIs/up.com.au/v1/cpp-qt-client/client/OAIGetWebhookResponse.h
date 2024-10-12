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
 * OAIGetWebhookResponse.h
 *
 * Successful response to get a single webhook. 
 */

#ifndef OAIGetWebhookResponse_H
#define OAIGetWebhookResponse_H

#include <QJsonObject>

#include "OAIWebhookResource.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWebhookResource;

class OAIGetWebhookResponse : public OAIObject {
public:
    OAIGetWebhookResponse();
    OAIGetWebhookResponse(QString json);
    ~OAIGetWebhookResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIWebhookResource getData() const;
    void setData(const OAIWebhookResource &data);
    bool is_data_Set() const;
    bool is_data_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIWebhookResource m_data;
    bool m_data_isSet;
    bool m_data_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetWebhookResponse)

#endif // OAIGetWebhookResponse_H
