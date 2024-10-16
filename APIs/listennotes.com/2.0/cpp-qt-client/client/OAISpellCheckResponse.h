/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAISpellCheckResponse.h
 *
 * 
 */

#ifndef OAISpellCheckResponse_H
#define OAISpellCheckResponse_H

#include <QJsonObject>

#include "OAISpellCheckResponse_tokens_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISpellCheckResponse_tokens_inner;

class OAISpellCheckResponse : public OAIObject {
public:
    OAISpellCheckResponse();
    OAISpellCheckResponse(QString json);
    ~OAISpellCheckResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCorrectedTextHtml() const;
    void setCorrectedTextHtml(const QString &corrected_text_html);
    bool is_corrected_text_html_Set() const;
    bool is_corrected_text_html_Valid() const;

    QList<OAISpellCheckResponse_tokens_inner> getTokens() const;
    void setTokens(const QList<OAISpellCheckResponse_tokens_inner> &tokens);
    bool is_tokens_Set() const;
    bool is_tokens_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_corrected_text_html;
    bool m_corrected_text_html_isSet;
    bool m_corrected_text_html_isValid;

    QList<OAISpellCheckResponse_tokens_inner> m_tokens;
    bool m_tokens_isSet;
    bool m_tokens_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAISpellCheckResponse)

#endif // OAISpellCheckResponse_H
