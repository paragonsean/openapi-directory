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
 * OAIAggregateOffer.h
 *
 * Defines a list of offers from merchants that are related to the image.
 */

#ifndef OAIAggregateOffer_H
#define OAIAggregateOffer_H

#include <QJsonObject>

#include "OAIAggregateRating.h"
#include "OAIImageObject.h"
#include "OAIOffer.h"
#include "OAIOrganization.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOffer;
class OAIAggregateRating;
class OAIOrganization;
class OAIImageObject;

class OAIAggregateOffer : public OAIObject {
public:
    OAIAggregateOffer();
    OAIAggregateOffer(QString json);
    ~OAIAggregateOffer() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIOffer> getOffers() const;
    void setOffers(const QList<OAIOffer> &offers);
    bool is_offers_Set() const;
    bool is_offers_Valid() const;

    OAIAggregateRating getAggregateRating() const;
    void setAggregateRating(const OAIAggregateRating &aggregate_rating);
    bool is_aggregate_rating_Set() const;
    bool is_aggregate_rating_Valid() const;

    QString getAvailability() const;
    void setAvailability(const QString &availability);
    bool is_availability_Set() const;
    bool is_availability_Valid() const;

    QString getLastUpdated() const;
    void setLastUpdated(const QString &last_updated);
    bool is_last_updated_Set() const;
    bool is_last_updated_Valid() const;

    float getPrice() const;
    void setPrice(const float &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QString getPriceCurrency() const;
    void setPriceCurrency(const QString &price_currency);
    bool is_price_currency_Set() const;
    bool is_price_currency_Valid() const;

    OAIOrganization getSeller() const;
    void setSeller(const OAIOrganization &seller);
    bool is_seller_Set() const;
    bool is_seller_Valid() const;

    QString getAlternateName() const;
    void setAlternateName(const QString &alternate_name);
    bool is_alternate_name_Set() const;
    bool is_alternate_name_Valid() const;

    QString getBingId() const;
    void setBingId(const QString &bing_id);
    bool is_bing_id_Set() const;
    bool is_bing_id_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    OAIImageObject getImage() const;
    void setImage(const OAIImageObject &image);
    bool is_image_Set() const;
    bool is_image_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    QString getReadLink() const;
    void setReadLink(const QString &read_link);
    bool is_read_link_Set() const;
    bool is_read_link_Valid() const;

    QString getWebSearchUrl() const;
    void setWebSearchUrl(const QString &web_search_url);
    bool is_web_search_url_Set() const;
    bool is_web_search_url_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getType() const;
    void setType(const QString &_type);
    bool is__type_Set() const;
    bool is__type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIOffer> m_offers;
    bool m_offers_isSet;
    bool m_offers_isValid;

    OAIAggregateRating m_aggregate_rating;
    bool m_aggregate_rating_isSet;
    bool m_aggregate_rating_isValid;

    QString m_availability;
    bool m_availability_isSet;
    bool m_availability_isValid;

    QString m_last_updated;
    bool m_last_updated_isSet;
    bool m_last_updated_isValid;

    float m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QString m_price_currency;
    bool m_price_currency_isSet;
    bool m_price_currency_isValid;

    OAIOrganization m_seller;
    bool m_seller_isSet;
    bool m_seller_isValid;

    QString m_alternate_name;
    bool m_alternate_name_isSet;
    bool m_alternate_name_isValid;

    QString m_bing_id;
    bool m_bing_id_isSet;
    bool m_bing_id_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    OAIImageObject m_image;
    bool m_image_isSet;
    bool m_image_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;

    QString m_read_link;
    bool m_read_link_isSet;
    bool m_read_link_isValid;

    QString m_web_search_url;
    bool m_web_search_url_isSet;
    bool m_web_search_url_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m__type;
    bool m__type_isSet;
    bool m__type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAggregateOffer)

#endif // OAIAggregateOffer_H
