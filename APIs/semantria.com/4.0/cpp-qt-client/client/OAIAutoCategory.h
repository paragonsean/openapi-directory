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
 * OAIAutoCategory.h
 *
 * 
 */

#ifndef OAIAutoCategory_H
#define OAIAutoCategory_H

#include <QJsonObject>

#include "OAISubCategory.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISubCategory;

class OAIAutoCategory : public OAIObject {
public:
    OAIAutoCategory();
    OAIAutoCategory(QString json);
    ~OAIAutoCategory() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAISubCategory> getCategories() const;
    void setCategories(const QList<OAISubCategory> &categories);
    bool is_categories_Set() const;
    bool is_categories_Valid() const;

    QString getSentimentPolarity() const;
    void setSentimentPolarity(const QString &sentiment_polarity);
    bool is_sentiment_polarity_Set() const;
    bool is_sentiment_polarity_Valid() const;

    double getSentimentScore() const;
    void setSentimentScore(const double &sentiment_score);
    bool is_sentiment_score_Set() const;
    bool is_sentiment_score_Valid() const;

    double getStrengthScore() const;
    void setStrengthScore(const double &strength_score);
    bool is_strength_score_Set() const;
    bool is_strength_score_Valid() const;

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

    QList<OAISubCategory> m_categories;
    bool m_categories_isSet;
    bool m_categories_isValid;

    QString m_sentiment_polarity;
    bool m_sentiment_polarity_isSet;
    bool m_sentiment_polarity_isValid;

    double m_sentiment_score;
    bool m_sentiment_score_isSet;
    bool m_sentiment_score_isValid;

    double m_strength_score;
    bool m_strength_score_isSet;
    bool m_strength_score_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAutoCategory)

#endif // OAIAutoCategory_H
