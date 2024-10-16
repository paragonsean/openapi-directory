/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPlugin.h
 *
 * Plugin A plugin for the Engine API
 */

#ifndef OAIPlugin_H
#define OAIPlugin_H

#include <QJsonObject>

#include "OAIPluginConfig.h"
#include "OAIPluginSettings.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPluginConfig;
class OAIPluginSettings;

class OAIPlugin : public OAIObject {
public:
    OAIPlugin();
    OAIPlugin(QString json);
    ~OAIPlugin() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPluginConfig getConfig() const;
    void setConfig(const OAIPluginConfig &config);
    bool is_config_Set() const;
    bool is_config_Valid() const;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPluginReference() const;
    void setPluginReference(const QString &plugin_reference);
    bool is_plugin_reference_Set() const;
    bool is_plugin_reference_Valid() const;

    OAIPluginSettings getSettings() const;
    void setSettings(const OAIPluginSettings &settings);
    bool is_settings_Set() const;
    bool is_settings_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPluginConfig m_config;
    bool m_config_isSet;
    bool m_config_isValid;

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_plugin_reference;
    bool m_plugin_reference_isSet;
    bool m_plugin_reference_isValid;

    OAIPluginSettings m_settings;
    bool m_settings_isSet;
    bool m_settings_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlugin)

#endif // OAIPlugin_H
