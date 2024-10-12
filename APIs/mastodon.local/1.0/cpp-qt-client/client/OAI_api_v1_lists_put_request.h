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
 * OAI_api_v1_lists_put_request.h
 *
 * 
 */

#ifndef OAI_api_v1_lists_put_request_H
#define OAI_api_v1_lists_put_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_api_v1_lists_put_request : public OAIObject {
public:
    OAI_api_v1_lists_put_request();
    OAI_api_v1_lists_put_request(QString json);
    ~OAI_api_v1_lists_put_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getRepliesPolicy() const;
    void setRepliesPolicy(const QString &replies_policy);
    bool is_replies_policy_Set() const;
    bool is_replies_policy_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_replies_policy;
    bool m_replies_policy_isSet;
    bool m_replies_policy_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_api_v1_lists_put_request)

#endif // OAI_api_v1_lists_put_request_H
