/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRoomWebhook.h
 *
 * Webhook information
 */

#ifndef OAIRoomWebhook_H
#define OAIRoomWebhook_H

#include <QJsonObject>

#include "OAIWebhook.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIWebhook;

class OAIRoomWebhook : public OAIObject {
public:
    OAIRoomWebhook();
    OAIRoomWebhook(QString json);
    ~OAIRoomWebhook() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isIsAssigned() const;
    void setIsAssigned(const bool &is_assigned);
    bool is_is_assigned_Set() const;
    bool is_is_assigned_Valid() const;

    OAIWebhook getWebhook() const;
    void setWebhook(const OAIWebhook &webhook);
    bool is_webhook_Set() const;
    bool is_webhook_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_is_assigned;
    bool m_is_assigned_isSet;
    bool m_is_assigned_isValid;

    OAIWebhook m_webhook;
    bool m_webhook_isSet;
    bool m_webhook_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRoomWebhook)

#endif // OAIRoomWebhook_H
