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
 * OAIWebhook.h
 *
 * Webhook information
 */

#ifndef OAIWebhook_H
#define OAIWebhook_H

#include <QJsonObject>

#include "OAIUserInfo.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUserInfo;

class OAIWebhook : public OAIObject {
public:
    OAIWebhook();
    OAIWebhook(QString json);
    ~OAIWebhook() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    OAIUserInfo getCreatedBy() const;
    void setCreatedBy(const OAIUserInfo &created_by);
    bool is_created_by_Set() const;
    bool is_created_by_Valid() const;

    QList<QString> getEventTypeNames() const;
    void setEventTypeNames(const QList<QString> &event_type_names);
    bool is_event_type_names_Set() const;
    bool is_event_type_names_Valid() const;

    QDateTime getExpireAt() const;
    void setExpireAt(const QDateTime &expire_at);
    bool is_expire_at_Set() const;
    bool is_expire_at_Valid() const;

    qint32 getFailStatus() const;
    void setFailStatus(const qint32 &fail_status);
    bool is_fail_status_Set() const;
    bool is_fail_status_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsEnabled() const;
    void setIsEnabled(const bool &is_enabled);
    bool is_is_enabled_Set() const;
    bool is_is_enabled_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getSecret() const;
    void setSecret(const QString &secret);
    bool is_secret_Set() const;
    bool is_secret_Valid() const;

    QDateTime getUpdatedAt() const;
    void setUpdatedAt(const QDateTime &updated_at);
    bool is_updated_at_Set() const;
    bool is_updated_at_Valid() const;

    OAIUserInfo getUpdatedBy() const;
    void setUpdatedBy(const OAIUserInfo &updated_by);
    bool is_updated_by_Set() const;
    bool is_updated_by_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    OAIUserInfo m_created_by;
    bool m_created_by_isSet;
    bool m_created_by_isValid;

    QList<QString> m_event_type_names;
    bool m_event_type_names_isSet;
    bool m_event_type_names_isValid;

    QDateTime m_expire_at;
    bool m_expire_at_isSet;
    bool m_expire_at_isValid;

    qint32 m_fail_status;
    bool m_fail_status_isSet;
    bool m_fail_status_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_enabled;
    bool m_is_enabled_isSet;
    bool m_is_enabled_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_secret;
    bool m_secret_isSet;
    bool m_secret_isValid;

    QDateTime m_updated_at;
    bool m_updated_at_isSet;
    bool m_updated_at_isValid;

    OAIUserInfo m_updated_by;
    bool m_updated_by_isSet;
    bool m_updated_by_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWebhook)

#endif // OAIWebhook_H
