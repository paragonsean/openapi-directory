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
 * OAINotificationConfig.h
 *
 * Notification configuration information
 */

#ifndef OAINotificationConfig_H
#define OAINotificationConfig_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAINotificationConfig : public OAIObject {
public:
    OAINotificationConfig();
    OAINotificationConfig(QString json);
    ~OAINotificationConfig() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<qint32> getChannelIds() const;
    void setChannelIds(const QList<qint32> &channel_ids);
    bool is_channel_ids_Set() const;
    bool is_channel_ids_Valid() const;

    QString getEventTypeName() const;
    void setEventTypeName(const QString &event_type_name);
    bool is_event_type_name_Set() const;
    bool is_event_type_name_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint32 getScopeId() const;
    void setScopeId(const qint32 &scope_id);
    bool is_scope_id_Set() const;
    bool is_scope_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<qint32> m_channel_ids;
    bool m_channel_ids_isSet;
    bool m_channel_ids_isValid;

    QString m_event_type_name;
    bool m_event_type_name_isSet;
    bool m_event_type_name_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint32 m_scope_id;
    bool m_scope_id_isSet;
    bool m_scope_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINotificationConfig)

#endif // OAINotificationConfig_H
