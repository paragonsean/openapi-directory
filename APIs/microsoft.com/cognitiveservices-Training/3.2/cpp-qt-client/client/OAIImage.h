/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImage.h
 *
 * Image model to be sent as JSON.
 */

#ifndef OAIImage_H
#define OAIImage_H

#include <QJsonObject>

#include "OAIImageRegion.h"
#include "OAIImageTag.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIImageRegion;
class OAIImageTag;

class OAIImage : public OAIObject {
public:
    OAIImage();
    OAIImage(QString json);
    ~OAIImage() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getCreated() const;
    void setCreated(const QDateTime &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    qint32 getHeight() const;
    void setHeight(const qint32 &height);
    bool is_height_Set() const;
    bool is_height_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getOriginalImageUri() const;
    void setOriginalImageUri(const QString &original_image_uri);
    bool is_original_image_uri_Set() const;
    bool is_original_image_uri_Valid() const;

    QList<OAIImageRegion> getRegions() const;
    void setRegions(const QList<OAIImageRegion> &regions);
    bool is_regions_Set() const;
    bool is_regions_Valid() const;

    QString getResizedImageUri() const;
    void setResizedImageUri(const QString &resized_image_uri);
    bool is_resized_image_uri_Set() const;
    bool is_resized_image_uri_Valid() const;

    QList<OAIImageTag> getTags() const;
    void setTags(const QList<OAIImageTag> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    QString getThumbnailUri() const;
    void setThumbnailUri(const QString &thumbnail_uri);
    bool is_thumbnail_uri_Set() const;
    bool is_thumbnail_uri_Valid() const;

    qint32 getWidth() const;
    void setWidth(const qint32 &width);
    bool is_width_Set() const;
    bool is_width_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    qint32 m_height;
    bool m_height_isSet;
    bool m_height_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_original_image_uri;
    bool m_original_image_uri_isSet;
    bool m_original_image_uri_isValid;

    QList<OAIImageRegion> m_regions;
    bool m_regions_isSet;
    bool m_regions_isValid;

    QString m_resized_image_uri;
    bool m_resized_image_uri_isSet;
    bool m_resized_image_uri_isValid;

    QList<OAIImageTag> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;

    QString m_thumbnail_uri;
    bool m_thumbnail_uri_isSet;
    bool m_thumbnail_uri_isValid;

    qint32 m_width;
    bool m_width_isSet;
    bool m_width_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImage)

#endif // OAIImage_H
