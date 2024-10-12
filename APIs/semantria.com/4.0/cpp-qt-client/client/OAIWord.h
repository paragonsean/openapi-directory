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
 * OAIWord.h
 *
 * 
 */

#ifndef OAIWord_H
#define OAIWord_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIWord : public OAIObject {
public:
    OAIWord();
    OAIWord(QString json);
    ~OAIWord() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isIsNegated() const;
    void setIsNegated(const bool &is_negated);
    bool is_is_negated_Set() const;
    bool is_is_negated_Valid() const;

    double getSentimentScore() const;
    void setSentimentScore(const double &sentiment_score);
    bool is_sentiment_score_Set() const;
    bool is_sentiment_score_Valid() const;

    QString getStemmed() const;
    void setStemmed(const QString &stemmed);
    bool is_stemmed_Set() const;
    bool is_stemmed_Valid() const;

    QString getTag() const;
    void setTag(const QString &tag);
    bool is_tag_Set() const;
    bool is_tag_Valid() const;

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

    bool m_is_negated;
    bool m_is_negated_isSet;
    bool m_is_negated_isValid;

    double m_sentiment_score;
    bool m_sentiment_score_isSet;
    bool m_sentiment_score_isValid;

    QString m_stemmed;
    bool m_stemmed_isSet;
    bool m_stemmed_isValid;

    QString m_tag;
    bool m_tag_isSet;
    bool m_tag_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIWord)

#endif // OAIWord_H
