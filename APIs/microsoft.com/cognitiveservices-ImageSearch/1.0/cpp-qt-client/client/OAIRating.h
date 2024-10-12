/**
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIRating.h
 *
 * Defines a rating.
 */

#ifndef OAIRating_H
#define OAIRating_H

#include <QJsonObject>

#include "OAIPropertiesItem.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIRating : public OAIObject {
public:
    OAIRating();
    OAIRating(QString json);
    ~OAIRating() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    float getBestRating() const;
    void setBestRating(const float &best_rating);
    bool is_best_rating_Set() const;
    bool is_best_rating_Valid() const;

    float getRatingValue() const;
    void setRatingValue(const float &rating_value);
    bool is_rating_value_Set() const;
    bool is_rating_value_Valid() const;

    QString getType() const;
    void setType(const QString &_type);
    bool is__type_Set() const;
    bool is__type_Valid() const;

    QString getText() const;
    void setText(const QString &text);
    bool is_text_Set() const;
    bool is_text_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    float m_best_rating;
    bool m_best_rating_isSet;
    bool m_best_rating_isValid;

    float m_rating_value;
    bool m_rating_value_isSet;
    bool m_rating_value_isValid;

    QString m__type;
    bool m__type_isSet;
    bool m__type_isValid;

    QString m_text;
    bool m_text_isSet;
    bool m_text_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRating)

#endif // OAIRating_H
