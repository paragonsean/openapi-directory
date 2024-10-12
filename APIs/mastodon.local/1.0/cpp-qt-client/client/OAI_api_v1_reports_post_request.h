/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_api_v1_reports_post_request.h
 *
 * 
 */

#ifndef OAI_api_v1_reports_post_request_H
#define OAI_api_v1_reports_post_request_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_api_v1_reports_post_request : public OAIObject {
public:
    OAI_api_v1_reports_post_request();
    OAI_api_v1_reports_post_request(QString json);
    ~OAI_api_v1_reports_post_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAccountId() const;
    void setAccountId(const QString &account_id);
    bool is_account_id_Set() const;
    bool is_account_id_Valid() const;

    QString getComment() const;
    void setComment(const QString &comment);
    bool is_comment_Set() const;
    bool is_comment_Valid() const;

    bool isForward() const;
    void setForward(const bool &forward);
    bool is_forward_Set() const;
    bool is_forward_Valid() const;

    QList<QString> getStatusIds() const;
    void setStatusIds(const QList<QString> &status_ids);
    bool is_status_ids_Set() const;
    bool is_status_ids_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_account_id;
    bool m_account_id_isSet;
    bool m_account_id_isValid;

    QString m_comment;
    bool m_comment_isSet;
    bool m_comment_isValid;

    bool m_forward;
    bool m_forward_isSet;
    bool m_forward_isValid;

    QList<QString> m_status_ids;
    bool m_status_ids_isSet;
    bool m_status_ids_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_api_v1_reports_post_request)

#endif // OAI_api_v1_reports_post_request_H
