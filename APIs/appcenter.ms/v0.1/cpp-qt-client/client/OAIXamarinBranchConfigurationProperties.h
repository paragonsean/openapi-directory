/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIXamarinBranchConfigurationProperties.h
 *
 * Build configuration for Xamarin projects
 */

#ifndef OAIXamarinBranchConfigurationProperties_H
#define OAIXamarinBranchConfigurationProperties_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIXamarinBranchConfigurationProperties : public OAIObject {
public:
    OAIXamarinBranchConfigurationProperties();
    OAIXamarinBranchConfigurationProperties(QString json);
    ~OAIXamarinBranchConfigurationProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getArgs() const;
    void setArgs(const QString &args);
    bool is_args_Set() const;
    bool is_args_Valid() const;

    QString getConfiguration() const;
    void setConfiguration(const QString &configuration);
    bool is_configuration_Set() const;
    bool is_configuration_Valid() const;

    bool isIsSimBuild() const;
    void setIsSimBuild(const bool &is_sim_build);
    bool is_is_sim_build_Set() const;
    bool is_is_sim_build_Valid() const;

    QString getMonoVersion() const;
    void setMonoVersion(const QString &mono_version);
    bool is_mono_version_Set() const;
    bool is_mono_version_Valid() const;

    QString getP12File() const;
    void setP12File(const QString &p12_file);
    bool is_p12_file_Set() const;
    bool is_p12_file_Valid() const;

    QString getP12Pwd() const;
    void setP12Pwd(const QString &p12_pwd);
    bool is_p12_pwd_Set() const;
    bool is_p12_pwd_Valid() const;

    QString getProvProfile() const;
    void setProvProfile(const QString &prov_profile);
    bool is_prov_profile_Set() const;
    bool is_prov_profile_Valid() const;

    QString getSdkBundle() const;
    void setSdkBundle(const QString &sdk_bundle);
    bool is_sdk_bundle_Set() const;
    bool is_sdk_bundle_Valid() const;

    QString getSlnPath() const;
    void setSlnPath(const QString &sln_path);
    bool is_sln_path_Set() const;
    bool is_sln_path_Valid() const;

    QString getSymlink() const;
    void setSymlink(const QString &symlink);
    bool is_symlink_Set() const;
    bool is_symlink_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_args;
    bool m_args_isSet;
    bool m_args_isValid;

    QString m_configuration;
    bool m_configuration_isSet;
    bool m_configuration_isValid;

    bool m_is_sim_build;
    bool m_is_sim_build_isSet;
    bool m_is_sim_build_isValid;

    QString m_mono_version;
    bool m_mono_version_isSet;
    bool m_mono_version_isValid;

    QString m_p12_file;
    bool m_p12_file_isSet;
    bool m_p12_file_isValid;

    QString m_p12_pwd;
    bool m_p12_pwd_isSet;
    bool m_p12_pwd_isValid;

    QString m_prov_profile;
    bool m_prov_profile_isSet;
    bool m_prov_profile_isValid;

    QString m_sdk_bundle;
    bool m_sdk_bundle_isSet;
    bool m_sdk_bundle_isValid;

    QString m_sln_path;
    bool m_sln_path_isSet;
    bool m_sln_path_isValid;

    QString m_symlink;
    bool m_symlink_isSet;
    bool m_symlink_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIXamarinBranchConfigurationProperties)

#endif // OAIXamarinBranchConfigurationProperties_H
