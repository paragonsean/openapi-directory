/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISourceTriggerDescriptor.h
 *
 * The source trigger that caused a run.
 */

#ifndef OAISourceTriggerDescriptor_H
#define OAISourceTriggerDescriptor_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAISourceTriggerDescriptor : public OAIObject {
public:
    OAISourceTriggerDescriptor();
    OAISourceTriggerDescriptor(QString json);
    ~OAISourceTriggerDescriptor() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBranchName() const;
    void setBranchName(const QString &branch_name);
    bool is_branch_name_Set() const;
    bool is_branch_name_Valid() const;

    QString getCommitId() const;
    void setCommitId(const QString &commit_id);
    bool is_commit_id_Set() const;
    bool is_commit_id_Valid() const;

    QString getEventType() const;
    void setEventType(const QString &event_type);
    bool is_event_type_Set() const;
    bool is_event_type_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getProviderType() const;
    void setProviderType(const QString &provider_type);
    bool is_provider_type_Set() const;
    bool is_provider_type_Valid() const;

    QString getPullRequestId() const;
    void setPullRequestId(const QString &pull_request_id);
    bool is_pull_request_id_Set() const;
    bool is_pull_request_id_Valid() const;

    QString getRepositoryUrl() const;
    void setRepositoryUrl(const QString &repository_url);
    bool is_repository_url_Set() const;
    bool is_repository_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_branch_name;
    bool m_branch_name_isSet;
    bool m_branch_name_isValid;

    QString m_commit_id;
    bool m_commit_id_isSet;
    bool m_commit_id_isValid;

    QString m_event_type;
    bool m_event_type_isSet;
    bool m_event_type_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_provider_type;
    bool m_provider_type_isSet;
    bool m_provider_type_isValid;

    QString m_pull_request_id;
    bool m_pull_request_id_isSet;
    bool m_pull_request_id_isValid;

    QString m_repository_url;
    bool m_repository_url_isSet;
    bool m_repository_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISourceTriggerDescriptor)

#endif // OAISourceTriggerDescriptor_H
