/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBackupPolicyProperties.h
 *
 * The properties of the backup policy.
 */

#ifndef OAIBackupPolicyProperties_H
#define OAIBackupPolicyProperties_H

#include <QJsonObject>

#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBackupPolicyProperties : public OAIObject {
public:
    OAIBackupPolicyProperties();
    OAIBackupPolicyProperties(QString json);
    ~OAIBackupPolicyProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBackupPolicyCreationType() const;
    void setBackupPolicyCreationType(const QString &backup_policy_creation_type);
    bool is_backup_policy_creation_type_Set() const;
    bool is_backup_policy_creation_type_Valid() const;

    QDateTime getLastBackupTime() const;
    void setLastBackupTime(const QDateTime &last_backup_time);
    bool is_last_backup_time_Set() const;
    bool is_last_backup_time_Valid() const;

    QDateTime getNextBackupTime() const;
    void setNextBackupTime(const QDateTime &next_backup_time);
    bool is_next_backup_time_Set() const;
    bool is_next_backup_time_Valid() const;

    QString getScheduledBackupStatus() const;
    void setScheduledBackupStatus(const QString &scheduled_backup_status);
    bool is_scheduled_backup_status_Set() const;
    bool is_scheduled_backup_status_Valid() const;

    qint64 getSchedulesCount() const;
    void setSchedulesCount(const qint64 &schedules_count);
    bool is_schedules_count_Set() const;
    bool is_schedules_count_Valid() const;

    QString getSsmHostName() const;
    void setSsmHostName(const QString &ssm_host_name);
    bool is_ssm_host_name_Set() const;
    bool is_ssm_host_name_Valid() const;

    QList<QString> getVolumeIds() const;
    void setVolumeIds(const QList<QString> &volume_ids);
    bool is_volume_ids_Set() const;
    bool is_volume_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_backup_policy_creation_type;
    bool m_backup_policy_creation_type_isSet;
    bool m_backup_policy_creation_type_isValid;

    QDateTime m_last_backup_time;
    bool m_last_backup_time_isSet;
    bool m_last_backup_time_isValid;

    QDateTime m_next_backup_time;
    bool m_next_backup_time_isSet;
    bool m_next_backup_time_isValid;

    QString m_scheduled_backup_status;
    bool m_scheduled_backup_status_isSet;
    bool m_scheduled_backup_status_isValid;

    qint64 m_schedules_count;
    bool m_schedules_count_isSet;
    bool m_schedules_count_isValid;

    QString m_ssm_host_name;
    bool m_ssm_host_name_isSet;
    bool m_ssm_host_name_isValid;

    QList<QString> m_volume_ids;
    bool m_volume_ids_isSet;
    bool m_volume_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBackupPolicyProperties)

#endif // OAIBackupPolicyProperties_H
