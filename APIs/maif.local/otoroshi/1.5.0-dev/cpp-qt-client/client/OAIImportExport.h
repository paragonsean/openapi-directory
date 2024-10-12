/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImportExport.h
 *
 * The structure that can be imported to or exported from Otoroshi. It represent the memory state of Otoroshi
 */

#ifndef OAIImportExport_H
#define OAIImportExport_H

#include <QJsonObject>

#include "OAIGlobalConfig.h"
#include "OAIImportExportStats.h"
#include "OAIImportExport_admins_inner.h"
#include "OAIImportExport_apiKeys_inner.h"
#include "OAIImportExport_errorTemplates_inner.h"
#include "OAIImportExport_serviceDescriptors_inner.h"
#include "OAIImportExport_serviceGroups_inner.h"
#include "OAIImportExport_simpleAdmins_inner.h"
#include <QDateTime>
#include <QList>
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIImportExport_admins_inner;
class OAIImportExport_apiKeys_inner;
class OAIGlobalConfig;
class OAIImportExport_errorTemplates_inner;
class OAIImportExport_serviceDescriptors_inner;
class OAIImportExport_serviceGroups_inner;
class OAIImportExport_simpleAdmins_inner;
class OAIImportExportStats;

class OAIImportExport : public OAIObject {
public:
    OAIImportExport();
    OAIImportExport(QString json);
    ~OAIImportExport() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIImportExport_admins_inner> getAdmins() const;
    void setAdmins(const QList<OAIImportExport_admins_inner> &admins);
    bool is_admins_Set() const;
    bool is_admins_Valid() const;

    QList<OAIImportExport_apiKeys_inner> getApiKeys() const;
    void setApiKeys(const QList<OAIImportExport_apiKeys_inner> &api_keys);
    bool is_api_keys_Set() const;
    bool is_api_keys_Valid() const;

    QMap<QString, QString> getAppConfig() const;
    void setAppConfig(const QMap<QString, QString> &app_config);
    bool is_app_config_Set() const;
    bool is_app_config_Valid() const;

    OAIGlobalConfig getConfig() const;
    void setConfig(const OAIGlobalConfig &config);
    bool is_config_Set() const;
    bool is_config_Valid() const;

    QDateTime getDate() const;
    void setDate(const QDateTime &date);
    bool is_date_Set() const;
    bool is_date_Valid() const;

    qint64 getDateRaw() const;
    void setDateRaw(const qint64 &date_raw);
    bool is_date_raw_Set() const;
    bool is_date_raw_Valid() const;

    QList<OAIImportExport_errorTemplates_inner> getErrorTemplates() const;
    void setErrorTemplates(const QList<OAIImportExport_errorTemplates_inner> &error_templates);
    bool is_error_templates_Set() const;
    bool is_error_templates_Valid() const;

    QString getLabel() const;
    void setLabel(const QString &label);
    bool is_label_Set() const;
    bool is_label_Valid() const;

    QList<OAIImportExport_serviceDescriptors_inner> getServiceDescriptors() const;
    void setServiceDescriptors(const QList<OAIImportExport_serviceDescriptors_inner> &service_descriptors);
    bool is_service_descriptors_Set() const;
    bool is_service_descriptors_Valid() const;

    QList<OAIImportExport_serviceGroups_inner> getServiceGroups() const;
    void setServiceGroups(const QList<OAIImportExport_serviceGroups_inner> &service_groups);
    bool is_service_groups_Set() const;
    bool is_service_groups_Valid() const;

    QList<OAIImportExport_simpleAdmins_inner> getSimpleAdmins() const;
    void setSimpleAdmins(const QList<OAIImportExport_simpleAdmins_inner> &simple_admins);
    bool is_simple_admins_Set() const;
    bool is_simple_admins_Valid() const;

    OAIImportExportStats getStats() const;
    void setStats(const OAIImportExportStats &stats);
    bool is_stats_Set() const;
    bool is_stats_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIImportExport_admins_inner> m_admins;
    bool m_admins_isSet;
    bool m_admins_isValid;

    QList<OAIImportExport_apiKeys_inner> m_api_keys;
    bool m_api_keys_isSet;
    bool m_api_keys_isValid;

    QMap<QString, QString> m_app_config;
    bool m_app_config_isSet;
    bool m_app_config_isValid;

    OAIGlobalConfig m_config;
    bool m_config_isSet;
    bool m_config_isValid;

    QDateTime m_date;
    bool m_date_isSet;
    bool m_date_isValid;

    qint64 m_date_raw;
    bool m_date_raw_isSet;
    bool m_date_raw_isValid;

    QList<OAIImportExport_errorTemplates_inner> m_error_templates;
    bool m_error_templates_isSet;
    bool m_error_templates_isValid;

    QString m_label;
    bool m_label_isSet;
    bool m_label_isValid;

    QList<OAIImportExport_serviceDescriptors_inner> m_service_descriptors;
    bool m_service_descriptors_isSet;
    bool m_service_descriptors_isValid;

    QList<OAIImportExport_serviceGroups_inner> m_service_groups;
    bool m_service_groups_isSet;
    bool m_service_groups_isValid;

    QList<OAIImportExport_simpleAdmins_inner> m_simple_admins;
    bool m_simple_admins_isSet;
    bool m_simple_admins_isValid;

    OAIImportExportStats m_stats;
    bool m_stats_isSet;
    bool m_stats_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImportExport)

#endif // OAIImportExport_H
