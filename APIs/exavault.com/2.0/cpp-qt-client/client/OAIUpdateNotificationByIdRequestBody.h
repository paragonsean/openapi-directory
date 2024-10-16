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
 * OAIUpdateNotificationByIdRequestBody.h
 *
 * 
 */

#ifndef OAIUpdateNotificationByIdRequestBody_H
#define OAIUpdateNotificationByIdRequestBody_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateNotificationByIdRequestBody : public OAIObject {
public:
    OAIUpdateNotificationByIdRequestBody();
    OAIUpdateNotificationByIdRequestBody(QString json);
    ~OAIUpdateNotificationByIdRequestBody() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAction() const;
    void setAction(const QString &action);
    bool is_action_Set() const;
    bool is_action_Valid() const;

    QString getMessage() const;
    void setMessage(const QString &message);
    bool is_message_Set() const;
    bool is_message_Valid() const;

    QList<QString> getRecipients() const;
    void setRecipients(const QList<QString> &recipients);
    bool is_recipients_Set() const;
    bool is_recipients_Valid() const;

    bool isSendEmail() const;
    void setSendEmail(const bool &send_email);
    bool is_send_email_Set() const;
    bool is_send_email_Valid() const;

    QList<QString> getUsernames() const;
    void setUsernames(const QList<QString> &usernames);
    bool is_usernames_Set() const;
    bool is_usernames_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_action;
    bool m_action_isSet;
    bool m_action_isValid;

    QString m_message;
    bool m_message_isSet;
    bool m_message_isValid;

    QList<QString> m_recipients;
    bool m_recipients_isSet;
    bool m_recipients_isValid;

    bool m_send_email;
    bool m_send_email_isSet;
    bool m_send_email_isValid;

    QList<QString> m_usernames;
    bool m_usernames_isSet;
    bool m_usernames_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNotificationByIdRequestBody)

#endif // OAIUpdateNotificationByIdRequestBody_H
