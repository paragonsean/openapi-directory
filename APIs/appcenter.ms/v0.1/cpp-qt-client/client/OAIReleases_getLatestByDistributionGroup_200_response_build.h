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
 * OAIReleases_getLatestByDistributionGroup_200_response_build.h
 *
 * Contains metadata about the build that produced the release being uploaded
 */

#ifndef OAIReleases_getLatestByDistributionGroup_200_response_build_H
#define OAIReleases_getLatestByDistributionGroup_200_response_build_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIReleases_getLatestByDistributionGroup_200_response_build : public OAIObject {
public:
    OAIReleases_getLatestByDistributionGroup_200_response_build();
    OAIReleases_getLatestByDistributionGroup_200_response_build(QString json);
    ~OAIReleases_getLatestByDistributionGroup_200_response_build() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBranchName() const;
    void setBranchName(const QString &branch_name);
    bool is_branch_name_Set() const;
    bool is_branch_name_Valid() const;

    QString getCommitHash() const;
    void setCommitHash(const QString &commit_hash);
    bool is_commit_hash_Set() const;
    bool is_commit_hash_Valid() const;

    QString getCommitMessage() const;
    void setCommitMessage(const QString &commit_message);
    bool is_commit_message_Set() const;
    bool is_commit_message_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_branch_name;
    bool m_branch_name_isSet;
    bool m_branch_name_isValid;

    QString m_commit_hash;
    bool m_commit_hash_isSet;
    bool m_commit_hash_isValid;

    QString m_commit_message;
    bool m_commit_message_isSet;
    bool m_commit_message_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIReleases_getLatestByDistributionGroup_200_response_build)

#endif // OAIReleases_getLatestByDistributionGroup_200_response_build_H
