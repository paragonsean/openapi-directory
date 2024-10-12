/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIProjectCompletePrivate.h
 *
 * 
 */

#ifndef OAIProjectCompletePrivate_H
#define OAIProjectCompletePrivate_H

#include <QJsonObject>

#include "OAICollaborator.h"
#include "OAICustomArticleField.h"
#include "OAIFundingInformation.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICollaborator;
class OAICustomArticleField;
class OAIFundingInformation;

class OAIProjectCompletePrivate : public OAIObject {
public:
    OAIProjectCompletePrivate();
    OAIProjectCompletePrivate(QString json);
    ~OAIProjectCompletePrivate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getAccountId() const;
    void setAccountId(const qint64 &account_id);
    bool is_account_id_Set() const;
    bool is_account_id_Valid() const;

    QList<OAICollaborator> getCollaborators() const;
    void setCollaborators(const QList<OAICollaborator> &collaborators);
    bool is_collaborators_Set() const;
    bool is_collaborators_Valid() const;

    QString getCreatedDate() const;
    void setCreatedDate(const QString &created_date);
    bool is_created_date_Set() const;
    bool is_created_date_Valid() const;

    QList<OAICustomArticleField> getCustomFields() const;
    void setCustomFields(const QList<OAICustomArticleField> &custom_fields);
    bool is_custom_fields_Set() const;
    bool is_custom_fields_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getFigshareUrl() const;
    void setFigshareUrl(const QString &figshare_url);
    bool is_figshare_url_Set() const;
    bool is_figshare_url_Valid() const;

    QString getFunding() const;
    void setFunding(const QString &funding);
    bool is_funding_Set() const;
    bool is_funding_Valid() const;

    QList<OAIFundingInformation> getFundingList() const;
    void setFundingList(const QList<OAIFundingInformation> &funding_list);
    bool is_funding_list_Set() const;
    bool is_funding_list_Valid() const;

    qint64 getGroupId() const;
    void setGroupId(const qint64 &group_id);
    bool is_group_id_Set() const;
    bool is_group_id_Valid() const;

    QString getModifiedDate() const;
    void setModifiedDate(const QString &modified_date);
    bool is_modified_date_Set() const;
    bool is_modified_date_Valid() const;

    qint64 getQuota() const;
    void setQuota(const qint64 &quota);
    bool is_quota_Set() const;
    bool is_quota_Valid() const;

    qint64 getUsedQuota() const;
    void setUsedQuota(const qint64 &used_quota);
    bool is_used_quota_Set() const;
    bool is_used_quota_Valid() const;

    qint64 getUsedQuotaPrivate() const;
    void setUsedQuotaPrivate(const qint64 &used_quota_private);
    bool is_used_quota_private_Set() const;
    bool is_used_quota_private_Valid() const;

    qint64 getUsedQuotaPublic() const;
    void setUsedQuotaPublic(const qint64 &used_quota_public);
    bool is_used_quota_public_Set() const;
    bool is_used_quota_public_Valid() const;

    QString getRole() const;
    void setRole(const QString &role);
    bool is_role_Set() const;
    bool is_role_Valid() const;

    QString getStorage() const;
    void setStorage(const QString &storage);
    bool is_storage_Set() const;
    bool is_storage_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getPublishedDate() const;
    void setPublishedDate(const QString &published_date);
    bool is_published_date_Set() const;
    bool is_published_date_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_account_id;
    bool m_account_id_isSet;
    bool m_account_id_isValid;

    QList<OAICollaborator> m_collaborators;
    bool m_collaborators_isSet;
    bool m_collaborators_isValid;

    QString m_created_date;
    bool m_created_date_isSet;
    bool m_created_date_isValid;

    QList<OAICustomArticleField> m_custom_fields;
    bool m_custom_fields_isSet;
    bool m_custom_fields_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_figshare_url;
    bool m_figshare_url_isSet;
    bool m_figshare_url_isValid;

    QString m_funding;
    bool m_funding_isSet;
    bool m_funding_isValid;

    QList<OAIFundingInformation> m_funding_list;
    bool m_funding_list_isSet;
    bool m_funding_list_isValid;

    qint64 m_group_id;
    bool m_group_id_isSet;
    bool m_group_id_isValid;

    QString m_modified_date;
    bool m_modified_date_isSet;
    bool m_modified_date_isValid;

    qint64 m_quota;
    bool m_quota_isSet;
    bool m_quota_isValid;

    qint64 m_used_quota;
    bool m_used_quota_isSet;
    bool m_used_quota_isValid;

    qint64 m_used_quota_private;
    bool m_used_quota_private_isSet;
    bool m_used_quota_private_isValid;

    qint64 m_used_quota_public;
    bool m_used_quota_public_isSet;
    bool m_used_quota_public_isValid;

    QString m_role;
    bool m_role_isSet;
    bool m_role_isValid;

    QString m_storage;
    bool m_storage_isSet;
    bool m_storage_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_published_date;
    bool m_published_date_isSet;
    bool m_published_date_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProjectCompletePrivate)

#endif // OAIProjectCompletePrivate_H
