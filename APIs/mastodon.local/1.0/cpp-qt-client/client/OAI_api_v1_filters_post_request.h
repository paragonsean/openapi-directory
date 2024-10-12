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
 * OAI_api_v1_filters_post_request.h
 *
 * 
 */

#ifndef OAI_api_v1_filters_post_request_H
#define OAI_api_v1_filters_post_request_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAI_api_v1_filters_post_request : public OAIObject {
public:
    OAI_api_v1_filters_post_request();
    OAI_api_v1_filters_post_request(QString json);
    ~OAI_api_v1_filters_post_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getContext() const;
    void setContext(const QList<QString> &context);
    bool is_context_Set() const;
    bool is_context_Valid() const;

    qint32 getExpiresIn() const;
    void setExpiresIn(const qint32 &expires_in);
    bool is_expires_in_Set() const;
    bool is_expires_in_Valid() const;

    bool isIrreversible() const;
    void setIrreversible(const bool &irreversible);
    bool is_irreversible_Set() const;
    bool is_irreversible_Valid() const;

    QString getPhrase() const;
    void setPhrase(const QString &phrase);
    bool is_phrase_Set() const;
    bool is_phrase_Valid() const;

    bool isWholeWord() const;
    void setWholeWord(const bool &whole_word);
    bool is_whole_word_Set() const;
    bool is_whole_word_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_context;
    bool m_context_isSet;
    bool m_context_isValid;

    qint32 m_expires_in;
    bool m_expires_in_isSet;
    bool m_expires_in_isValid;

    bool m_irreversible;
    bool m_irreversible_isSet;
    bool m_irreversible_isValid;

    QString m_phrase;
    bool m_phrase_isSet;
    bool m_phrase_isValid;

    bool m_whole_word;
    bool m_whole_word_isSet;
    bool m_whole_word_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_api_v1_filters_post_request)

#endif // OAI_api_v1_filters_post_request_H
