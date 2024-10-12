/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICreateLabProperties.h
 *
 * Properties for creating a managed lab and a default environment setting
 */

#ifndef OAICreateLabProperties_H
#define OAICreateLabProperties_H

#include <QJsonObject>

#include "OAIEnvironmentSettingCreationParameters.h"
#include "OAILabCreationParameters.h"
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIEnvironmentSettingCreationParameters;
class OAILabCreationParameters;

class OAICreateLabProperties : public OAIObject {
public:
    OAICreateLabProperties();
    OAICreateLabProperties(QString json);
    ~OAICreateLabProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIEnvironmentSettingCreationParameters getEnvironmentSettingCreationParameters() const;
    void setEnvironmentSettingCreationParameters(const OAIEnvironmentSettingCreationParameters &environment_setting_creation_parameters);
    bool is_environment_setting_creation_parameters_Set() const;
    bool is_environment_setting_creation_parameters_Valid() const;

    OAILabCreationParameters getLabCreationParameters() const;
    void setLabCreationParameters(const OAILabCreationParameters &lab_creation_parameters);
    bool is_lab_creation_parameters_Set() const;
    bool is_lab_creation_parameters_Valid() const;

    QString getLocation() const;
    void setLocation(const QString &location);
    bool is_location_Set() const;
    bool is_location_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QMap<QString, QString> getTags() const;
    void setTags(const QMap<QString, QString> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIEnvironmentSettingCreationParameters m_environment_setting_creation_parameters;
    bool m_environment_setting_creation_parameters_isSet;
    bool m_environment_setting_creation_parameters_isValid;

    OAILabCreationParameters m_lab_creation_parameters;
    bool m_lab_creation_parameters_isSet;
    bool m_lab_creation_parameters_isValid;

    QString m_location;
    bool m_location_isSet;
    bool m_location_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QMap<QString, QString> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateLabProperties)

#endif // OAICreateLabProperties_H
