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
 * OAICuration.h
 *
 * 
 */

#ifndef OAICuration_H
#define OAICuration_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICuration : public OAIObject {
public:
    OAICuration();
    OAICuration(QString json);
    ~OAICuration() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint64 getAccountId() const;
    void setAccountId(const qint64 &account_id);
    bool is_account_id_Set() const;
    bool is_account_id_Valid() const;

    qint64 getArticleId() const;
    void setArticleId(const qint64 &article_id);
    bool is_article_id_Set() const;
    bool is_article_id_Valid() const;

    qint64 getAssignedTo() const;
    void setAssignedTo(const qint64 &assigned_to);
    bool is_assigned_to_Set() const;
    bool is_assigned_to_Valid() const;

    qint64 getCommentsCount() const;
    void setCommentsCount(const qint64 &comments_count);
    bool is_comments_count_Set() const;
    bool is_comments_count_Valid() const;

    QString getCreatedDate() const;
    void setCreatedDate(const QString &created_date);
    bool is_created_date_Set() const;
    bool is_created_date_Valid() const;

    qint64 getGroupId() const;
    void setGroupId(const qint64 &group_id);
    bool is_group_id_Set() const;
    bool is_group_id_Valid() const;

    qint64 getId() const;
    void setId(const qint64 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getModifiedDate() const;
    void setModifiedDate(const QString &modified_date);
    bool is_modified_date_Set() const;
    bool is_modified_date_Valid() const;

    QString getReviewDate() const;
    void setReviewDate(const QString &review_date);
    bool is_review_date_Set() const;
    bool is_review_date_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    qint64 getVersion() const;
    void setVersion(const qint64 &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint64 m_account_id;
    bool m_account_id_isSet;
    bool m_account_id_isValid;

    qint64 m_article_id;
    bool m_article_id_isSet;
    bool m_article_id_isValid;

    qint64 m_assigned_to;
    bool m_assigned_to_isSet;
    bool m_assigned_to_isValid;

    qint64 m_comments_count;
    bool m_comments_count_isSet;
    bool m_comments_count_isValid;

    QString m_created_date;
    bool m_created_date_isSet;
    bool m_created_date_isValid;

    qint64 m_group_id;
    bool m_group_id_isSet;
    bool m_group_id_isValid;

    qint64 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_modified_date;
    bool m_modified_date_isSet;
    bool m_modified_date_isValid;

    QString m_review_date;
    bool m_review_date_isSet;
    bool m_review_date_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    qint64 m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICuration)

#endif // OAICuration_H
