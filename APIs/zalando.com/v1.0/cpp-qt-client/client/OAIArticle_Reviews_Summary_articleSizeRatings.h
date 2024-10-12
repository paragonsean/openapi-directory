/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIArticle_Reviews_Summary_articleSizeRatings.h
 *
 * size rating of the article
 */

#ifndef OAIArticle_Reviews_Summary_articleSizeRatings_H
#define OAIArticle_Reviews_Summary_articleSizeRatings_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIArticle_Reviews_Summary_articleSizeRatings : public OAIObject {
public:
    OAIArticle_Reviews_Summary_articleSizeRatings();
    OAIArticle_Reviews_Summary_articleSizeRatings(QString json);
    ~OAIArticle_Reviews_Summary_articleSizeRatings() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    double getBootlegWidth() const;
    void setBootlegWidth(const double &bootleg_width);
    bool is_bootleg_width_Set() const;
    bool is_bootleg_width_Valid() const;

    double getChest() const;
    void setChest(const double &chest);
    bool is_chest_Set() const;
    bool is_chest_Valid() const;

    double getChestGirth() const;
    void setChestGirth(const double &chest_girth);
    bool is_chest_girth_Set() const;
    bool is_chest_girth_Valid() const;

    double getCollarSize() const;
    void setCollarSize(const double &collar_size);
    bool is_collar_size_Set() const;
    bool is_collar_size_Valid() const;

    double getCupSize() const;
    void setCupSize(const double &cup_size);
    bool is_cup_size_Set() const;
    bool is_cup_size_Valid() const;

    double getHipsOrRear() const;
    void setHipsOrRear(const double &hips_or_rear);
    bool is_hips_or_rear_Set() const;
    bool is_hips_or_rear_Valid() const;

    double getLegFit() const;
    void setLegFit(const double &leg_fit);
    bool is_leg_fit_Set() const;
    bool is_leg_fit_Valid() const;

    double getLength() const;
    void setLength(const double &length);
    bool is_length_Set() const;
    bool is_length_Valid() const;

    double getOverall() const;
    void setOverall(const double &overall);
    bool is_overall_Set() const;
    bool is_overall_Valid() const;

    double getShoeWidth() const;
    void setShoeWidth(const double &shoe_width);
    bool is_shoe_width_Set() const;
    bool is_shoe_width_Valid() const;

    double getShoulders() const;
    void setShoulders(const double &shoulders);
    bool is_shoulders_Set() const;
    bool is_shoulders_Valid() const;

    double getSleeves() const;
    void setSleeves(const double &sleeves);
    bool is_sleeves_Set() const;
    bool is_sleeves_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    double m_bootleg_width;
    bool m_bootleg_width_isSet;
    bool m_bootleg_width_isValid;

    double m_chest;
    bool m_chest_isSet;
    bool m_chest_isValid;

    double m_chest_girth;
    bool m_chest_girth_isSet;
    bool m_chest_girth_isValid;

    double m_collar_size;
    bool m_collar_size_isSet;
    bool m_collar_size_isValid;

    double m_cup_size;
    bool m_cup_size_isSet;
    bool m_cup_size_isValid;

    double m_hips_or_rear;
    bool m_hips_or_rear_isSet;
    bool m_hips_or_rear_isValid;

    double m_leg_fit;
    bool m_leg_fit_isSet;
    bool m_leg_fit_isValid;

    double m_length;
    bool m_length_isSet;
    bool m_length_isValid;

    double m_overall;
    bool m_overall_isSet;
    bool m_overall_isValid;

    double m_shoe_width;
    bool m_shoe_width_isSet;
    bool m_shoe_width_isValid;

    double m_shoulders;
    bool m_shoulders_isSet;
    bool m_shoulders_isValid;

    double m_sleeves;
    bool m_sleeves_isSet;
    bool m_sleeves_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArticle_Reviews_Summary_articleSizeRatings)

#endif // OAIArticle_Reviews_Summary_articleSizeRatings_H
