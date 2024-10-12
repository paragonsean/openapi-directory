/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAmenity_Media.h
 *
 * Media is a digital content like image, video with associated text and description, several scales and some metadata can be provided also.
 */

#ifndef OAIAmenity_Media_H
#define OAIAmenity_Media_H

#include <QJsonObject>

#include "OAIQualifiedFreeText.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIQualifiedFreeText;

class OAIAmenity_Media : public OAIObject {
public:
    OAIAmenity_Media();
    OAIAmenity_Media(QString json);
    ~OAIAmenity_Media() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIQualifiedFreeText getDescription() const;
    void setDescription(const OAIQualifiedFreeText &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getHref() const;
    void setHref(const QString &href);
    bool is_href_Set() const;
    bool is_href_Valid() const;

    QString getMediaType() const;
    void setMediaType(const QString &media_type);
    bool is_media_type_Set() const;
    bool is_media_type_Valid() const;

    QString getTitle() const;
    void setTitle(const QString &title);
    bool is_title_Set() const;
    bool is_title_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIQualifiedFreeText m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_href;
    bool m_href_isSet;
    bool m_href_isValid;

    QString m_media_type;
    bool m_media_type_isSet;
    bool m_media_type_isValid;

    QString m_title;
    bool m_title_isSet;
    bool m_title_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAmenity_Media)

#endif // OAIAmenity_Media_H
