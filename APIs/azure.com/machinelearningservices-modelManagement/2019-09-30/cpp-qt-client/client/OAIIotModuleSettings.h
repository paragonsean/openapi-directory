/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIIotModuleSettings.h
 *
 * 
 */

#ifndef OAIIotModuleSettings_H
#define OAIIotModuleSettings_H

#include <QJsonObject>

#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIIotModuleSettings : public OAIObject {
public:
    OAIIotModuleSettings();
    OAIIotModuleSettings(QString json);
    ~OAIIotModuleSettings() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCreateOptions() const;
    void setCreateOptions(const QString &create_options);
    bool is_create_options_Set() const;
    bool is_create_options_Valid() const;

    QMap<QString, QString> getEnvironmentVariables() const;
    void setEnvironmentVariables(const QMap<QString, QString> &environment_variables);
    bool is_environment_variables_Set() const;
    bool is_environment_variables_Valid() const;

    QString getImageLocation() const;
    void setImageLocation(const QString &image_location);
    bool is_image_location_Set() const;
    bool is_image_location_Valid() const;

    QString getModuleName() const;
    void setModuleName(const QString &module_name);
    bool is_module_name_Set() const;
    bool is_module_name_Valid() const;

    QMap<QString, QString> getPropertiesDesired() const;
    void setPropertiesDesired(const QMap<QString, QString> &properties_desired);
    bool is_properties_desired_Set() const;
    bool is_properties_desired_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_create_options;
    bool m_create_options_isSet;
    bool m_create_options_isValid;

    QMap<QString, QString> m_environment_variables;
    bool m_environment_variables_isSet;
    bool m_environment_variables_isValid;

    QString m_image_location;
    bool m_image_location_isSet;
    bool m_image_location_isValid;

    QString m_module_name;
    bool m_module_name_isSet;
    bool m_module_name_isValid;

    QMap<QString, QString> m_properties_desired;
    bool m_properties_desired_isSet;
    bool m_properties_desired_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIIotModuleSettings)

#endif // OAIIotModuleSettings_H
