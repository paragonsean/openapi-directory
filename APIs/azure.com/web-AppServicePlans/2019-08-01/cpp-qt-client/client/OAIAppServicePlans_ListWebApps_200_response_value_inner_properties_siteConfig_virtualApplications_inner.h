/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner.h
 *
 * Virtual application in an app.
 */

#ifndef OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner_H
#define OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner_H

#include <QJsonObject>

#include "OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner_virtualDirectories_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner_virtualDirectories_inner;

class OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner : public OAIObject {
public:
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner();
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner(QString json);
    ~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getPhysicalPath() const;
    void setPhysicalPath(const QString &physical_path);
    bool is_physical_path_Set() const;
    bool is_physical_path_Valid() const;

    bool isPreloadEnabled() const;
    void setPreloadEnabled(const bool &preload_enabled);
    bool is_preload_enabled_Set() const;
    bool is_preload_enabled_Valid() const;

    QList<OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner_virtualDirectories_inner> getVirtualDirectories() const;
    void setVirtualDirectories(const QList<OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner_virtualDirectories_inner> &virtual_directories);
    bool is_virtual_directories_Set() const;
    bool is_virtual_directories_Valid() const;

    QString getVirtualPath() const;
    void setVirtualPath(const QString &virtual_path);
    bool is_virtual_path_Set() const;
    bool is_virtual_path_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_physical_path;
    bool m_physical_path_isSet;
    bool m_physical_path_isValid;

    bool m_preload_enabled;
    bool m_preload_enabled_isSet;
    bool m_preload_enabled_isValid;

    QList<OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner_virtualDirectories_inner> m_virtual_directories;
    bool m_virtual_directories_isSet;
    bool m_virtual_directories_isValid;

    QString m_virtual_path;
    bool m_virtual_path_isSet;
    bool m_virtual_path_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner)

#endif // OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_virtualApplications_inner_H
