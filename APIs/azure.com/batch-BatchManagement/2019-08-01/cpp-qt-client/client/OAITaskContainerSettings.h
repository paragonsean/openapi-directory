/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITaskContainerSettings.h
 *
 * 
 */

#ifndef OAITaskContainerSettings_H
#define OAITaskContainerSettings_H

#include <QJsonObject>

#include "OAIContainerRegistry.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIContainerRegistry;

class OAITaskContainerSettings : public OAIObject {
public:
    OAITaskContainerSettings();
    OAITaskContainerSettings(QString json);
    ~OAITaskContainerSettings() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getContainerRunOptions() const;
    void setContainerRunOptions(const QString &container_run_options);
    bool is_container_run_options_Set() const;
    bool is_container_run_options_Valid() const;

    QString getImageName() const;
    void setImageName(const QString &image_name);
    bool is_image_name_Set() const;
    bool is_image_name_Valid() const;

    OAIContainerRegistry getRegistry() const;
    void setRegistry(const OAIContainerRegistry &registry);
    bool is_registry_Set() const;
    bool is_registry_Valid() const;

    QString getWorkingDirectory() const;
    void setWorkingDirectory(const QString &working_directory);
    bool is_working_directory_Set() const;
    bool is_working_directory_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_container_run_options;
    bool m_container_run_options_isSet;
    bool m_container_run_options_isValid;

    QString m_image_name;
    bool m_image_name_isSet;
    bool m_image_name_isValid;

    OAIContainerRegistry m_registry;
    bool m_registry_isSet;
    bool m_registry_isValid;

    QString m_working_directory;
    bool m_working_directory_isSet;
    bool m_working_directory_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITaskContainerSettings)

#endif // OAITaskContainerSettings_H
