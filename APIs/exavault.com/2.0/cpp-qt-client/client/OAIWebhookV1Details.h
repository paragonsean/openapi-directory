/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIWebhookV1Details.h
 *
 * 
 */

#ifndef OAIWebhookV1Details_H
#define OAIWebhookV1Details_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIWebhookV1Details : public OAIObject {
public:
    OAIWebhookV1Details();
    OAIWebhookV1Details(QString json);
    ~OAIWebhookV1Details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccountName() const;
    void setAccountName(const QString &account_name);
    bool is_account_name_Set() const;
    bool is_account_name_Valid() const;

    qint32 getAttempt() const;
    void setAttempt(const qint32 &attempt);
    bool is_attempt_Set() const;
    bool is_attempt_Valid() const;

    QString getAttemptId() const;
    void setAttemptId(const QString &attempt_id);
    bool is_attempt_id_Set() const;
    bool is_attempt_id_Valid() const;

    QString getEvent() const;
    void setEvent(const QString &event);
    bool is_event_Set() const;
    bool is_event_Valid() const;

    QString getProtocol() const;
    void setProtocol(const QString &protocol);
    bool is_protocol_Set() const;
    bool is_protocol_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_account_name;
    bool m_account_name_isSet;
    bool m_account_name_isValid;

    qint32 m_attempt;
    bool m_attempt_isSet;
    bool m_attempt_isValid;

    QString m_attempt_id;
    bool m_attempt_id_isSet;
    bool m_attempt_id_isValid;

    QString m_event;
    bool m_event_isSet;
    bool m_event_isValid;

    QString m_protocol;
    bool m_protocol_isSet;
    bool m_protocol_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebhookV1Details)

#endif // OAIWebhookV1Details_H
