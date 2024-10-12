/**
 * Semantria
 * Semantria applies Text and Sentiment Analysis to tweets, facebook posts, surveys, reviews or enterprise content.
 *
 * The version of the OpenAPI document: 4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPhrase.h
 *
 * 
 */

#ifndef OAIPhrase_H
#define OAIPhrase_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIPhrase : public OAIObject {
public:
    OAIPhrase();
    OAIPhrase(QString json);
    ~OAIPhrase() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getIntensifyingPhrase() const;
    void setIntensifyingPhrase(const QString &intensifying_phrase);
    bool is_intensifying_phrase_Set() const;
    bool is_intensifying_phrase_Valid() const;

    bool isIsIntensified() const;
    void setIsIntensified(const bool &is_intensified);
    bool is_is_intensified_Set() const;
    bool is_is_intensified_Valid() const;

    bool isIsNegated() const;
    void setIsNegated(const bool &is_negated);
    bool is_is_negated_Set() const;
    bool is_is_negated_Valid() const;

    QString getNegatingPhrase() const;
    void setNegatingPhrase(const QString &negating_phrase);
    bool is_negating_phrase_Set() const;
    bool is_negating_phrase_Valid() const;

    QString getSentimentPolarity() const;
    void setSentimentPolarity(const QString &sentiment_polarity);
    bool is_sentiment_polarity_Set() const;
    bool is_sentiment_polarity_Valid() const;

    double getSentimentScore() const;
    void setSentimentScore(const double &sentiment_score);
    bool is_sentiment_score_Set() const;
    bool is_sentiment_score_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_intensifying_phrase;
    bool m_intensifying_phrase_isSet;
    bool m_intensifying_phrase_isValid;

    bool m_is_intensified;
    bool m_is_intensified_isSet;
    bool m_is_intensified_isValid;

    bool m_is_negated;
    bool m_is_negated_isSet;
    bool m_is_negated_isValid;

    QString m_negating_phrase;
    bool m_negating_phrase_isSet;
    bool m_negating_phrase_isValid;

    QString m_sentiment_polarity;
    bool m_sentiment_polarity_isSet;
    bool m_sentiment_polarity_isValid;

    double m_sentiment_score;
    bool m_sentiment_score_isSet;
    bool m_sentiment_score_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPhrase)

#endif // OAIPhrase_H
