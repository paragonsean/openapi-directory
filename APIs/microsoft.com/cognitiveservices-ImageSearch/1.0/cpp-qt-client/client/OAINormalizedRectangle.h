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
 * OAINormalizedRectangle.h
 *
 * Defines a region of an image. The region is defined by the coordinates of the top, left corner and bottom, right corner of the region. The coordinates are fractional values of the original image&#39;s width and height in the range 0.0 through 1.0.
 */

#ifndef OAINormalizedRectangle_H
#define OAINormalizedRectangle_H

#include <QJsonObject>

#include "OAIImageObject.h"
#include "OAIStructuredValue.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIImageObject;

class OAINormalizedRectangle : public OAIObject {
public:
    OAINormalizedRectangle();
    OAINormalizedRectangle(QString json);
    ~OAINormalizedRectangle() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    float getBottom() const;
    void setBottom(const float &bottom);
    bool is_bottom_Set() const;
    bool is_bottom_Valid() const;

    float getLeft() const;
    void setLeft(const float &left);
    bool is_left_Set() const;
    bool is_left_Valid() const;

    float getRight() const;
    void setRight(const float &right);
    bool is_right_Set() const;
    bool is_right_Valid() const;

    float getTop() const;
    void setTop(const float &top);
    bool is_top_Set() const;
    bool is_top_Valid() const;

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

    float m_bottom;
    bool m_bottom_isSet;
    bool m_bottom_isValid;

    float m_left;
    bool m_left_isSet;
    bool m_left_isValid;

    float m_right;
    bool m_right_isSet;
    bool m_right_isValid;

    float m_top;
    bool m_top_isSet;
    bool m_top_isValid;

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

Q_DECLARE_METATYPE(OpenAPI::OAINormalizedRectangle)

#endif // OAINormalizedRectangle_H
