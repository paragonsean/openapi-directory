/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDockerBuildStepUpdateParameters.h
 *
 * The properties for updating a docker build step.
 */

#ifndef OAIDockerBuildStepUpdateParameters_H
#define OAIDockerBuildStepUpdateParameters_H

#include <QJsonObject>

#include "OAIBuildArgument.h"
#include "OAIBuildStepPropertiesUpdateParameters.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBuildArgument;

class OAIDockerBuildStepUpdateParameters : public OAIObject {
public:
    OAIDockerBuildStepUpdateParameters();
    OAIDockerBuildStepUpdateParameters(QString json);
    ~OAIDockerBuildStepUpdateParameters() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBaseImageTrigger() const;
    void setBaseImageTrigger(const QString &base_image_trigger);
    bool is_base_image_trigger_Set() const;
    bool is_base_image_trigger_Valid() const;

    QString getBranch() const;
    void setBranch(const QString &branch);
    bool is_branch_Set() const;
    bool is_branch_Valid() const;

    QList<OAIBuildArgument> getBuildArguments() const;
    void setBuildArguments(const QList<OAIBuildArgument> &build_arguments);
    bool is_build_arguments_Set() const;
    bool is_build_arguments_Valid() const;

    QString getContextPath() const;
    void setContextPath(const QString &context_path);
    bool is_context_path_Set() const;
    bool is_context_path_Valid() const;

    QString getDockerFilePath() const;
    void setDockerFilePath(const QString &docker_file_path);
    bool is_docker_file_path_Set() const;
    bool is_docker_file_path_Valid() const;

    QList<QString> getImageNames() const;
    void setImageNames(const QList<QString> &image_names);
    bool is_image_names_Set() const;
    bool is_image_names_Valid() const;

    bool isIsPushEnabled() const;
    void setIsPushEnabled(const bool &is_push_enabled);
    bool is_is_push_enabled_Set() const;
    bool is_is_push_enabled_Valid() const;

    bool isNoCache() const;
    void setNoCache(const bool &no_cache);
    bool is_no_cache_Set() const;
    bool is_no_cache_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_base_image_trigger;
    bool m_base_image_trigger_isSet;
    bool m_base_image_trigger_isValid;

    QString m_branch;
    bool m_branch_isSet;
    bool m_branch_isValid;

    QList<OAIBuildArgument> m_build_arguments;
    bool m_build_arguments_isSet;
    bool m_build_arguments_isValid;

    QString m_context_path;
    bool m_context_path_isSet;
    bool m_context_path_isValid;

    QString m_docker_file_path;
    bool m_docker_file_path_isSet;
    bool m_docker_file_path_isValid;

    QList<QString> m_image_names;
    bool m_image_names_isSet;
    bool m_image_names_isValid;

    bool m_is_push_enabled;
    bool m_is_push_enabled_isSet;
    bool m_is_push_enabled_isValid;

    bool m_no_cache;
    bool m_no_cache_isSet;
    bool m_no_cache_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDockerBuildStepUpdateParameters)

#endif // OAIDockerBuildStepUpdateParameters_H
