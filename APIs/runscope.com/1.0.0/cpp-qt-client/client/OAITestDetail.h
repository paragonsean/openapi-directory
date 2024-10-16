/**
 * Runscope API
 * Manage Runscope programmatically.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITestDetail.h
 *
 * 
 */

#ifndef OAITestDetail_H
#define OAITestDetail_H

#include <QJsonObject>

#include "OAIEnvironment.h"
#include "OAIObject.h"
#include "OAISchedule.h"
#include "OAITest_created_by.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAITest_created_by;
class OAIEnvironment;
class OAISchedule;

class OAITestDetail : public OAIObject {
public:
    OAITestDetail();
    OAITestDetail(QString json);
    ~OAITestDetail() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getCreatedAt() const;
    void setCreatedAt(const qint32 &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    OAITest_created_by getCreatedBy() const;
    void setCreatedBy(const OAITest_created_by &created_by);
    bool is_created_by_Set() const;
    bool is_created_by_Valid() const;

    QString getDefaultEnvironmentId() const;
    void setDefaultEnvironmentId(const QString &default_environment_id);
    bool is_default_environment_id_Set() const;
    bool is_default_environment_id_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIObject getLastRun() const;
    void setLastRun(const OAIObject &last_run);
    bool is_last_run_Set() const;
    bool is_last_run_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getTriggerUrl() const;
    void setTriggerUrl(const QString &trigger_url);
    bool is_trigger_url_Set() const;
    bool is_trigger_url_Valid() const;

    OAIEnvironment getEnvironments() const;
    void setEnvironments(const OAIEnvironment &environments);
    bool is_environments_Set() const;
    bool is_environments_Valid() const;

    qint32 getExportedAt() const;
    void setExportedAt(const qint32 &exported_at);
    bool is_exported_at_Set() const;
    bool is_exported_at_Valid() const;

    QList<OAISchedule> getSchedules() const;
    void setSchedules(const QList<OAISchedule> &schedules);
    bool is_schedules_Set() const;
    bool is_schedules_Valid() const;

    QList<OAIObject> getSteps() const;
    void setSteps(const QList<OAIObject> &steps);
    bool is_steps_Set() const;
    bool is_steps_Valid() const;

    QString getVersion() const;
    void setVersion(const QString &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    OAITest_created_by m_created_by;
    bool m_created_by_isSet;
    bool m_created_by_isValid;

    QString m_default_environment_id;
    bool m_default_environment_id_isSet;
    bool m_default_environment_id_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIObject m_last_run;
    bool m_last_run_isSet;
    bool m_last_run_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_trigger_url;
    bool m_trigger_url_isSet;
    bool m_trigger_url_isValid;

    OAIEnvironment m_environments;
    bool m_environments_isSet;
    bool m_environments_isValid;

    qint32 m_exported_at;
    bool m_exported_at_isSet;
    bool m_exported_at_isValid;

    QList<OAISchedule> m_schedules;
    bool m_schedules_isSet;
    bool m_schedules_isValid;

    QList<OAIObject> m_steps;
    bool m_steps_isSet;
    bool m_steps_isValid;

    QString m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITestDetail)

#endif // OAITestDetail_H
