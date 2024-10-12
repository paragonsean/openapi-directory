/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIImageRegionCreateResult.h
 *
 * 
 */

#ifndef OAIImageRegionCreateResult_H
#define OAIImageRegionCreateResult_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIImageRegionCreateResult : public OAIObject {
public:
    OAIImageRegionCreateResult();
    OAIImageRegionCreateResult(QString json);
    ~OAIImageRegionCreateResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getCreated() const;
    void setCreated(const QDateTime &created);
    bool is_created_Set() const;
    bool is_created_Valid() const;

    float getHeight() const;
    void setHeight(const float &height);
    bool is_height_Set() const;
    bool is_height_Valid() const;

    QString getImageId() const;
    void setImageId(const QString &image_id);
    bool is_image_id_Set() const;
    bool is_image_id_Valid() const;

    float getLeft() const;
    void setLeft(const float &left);
    bool is_left_Set() const;
    bool is_left_Valid() const;

    QString getRegionId() const;
    void setRegionId(const QString &region_id);
    bool is_region_id_Set() const;
    bool is_region_id_Valid() const;

    QString getTagId() const;
    void setTagId(const QString &tag_id);
    bool is_tag_id_Set() const;
    bool is_tag_id_Valid() const;

    QString getTagName() const;
    void setTagName(const QString &tag_name);
    bool is_tag_name_Set() const;
    bool is_tag_name_Valid() const;

    float getTop() const;
    void setTop(const float &top);
    bool is_top_Set() const;
    bool is_top_Valid() const;

    float getWidth() const;
    void setWidth(const float &width);
    bool is_width_Set() const;
    bool is_width_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_created;
    bool m_created_isSet;
    bool m_created_isValid;

    float m_height;
    bool m_height_isSet;
    bool m_height_isValid;

    QString m_image_id;
    bool m_image_id_isSet;
    bool m_image_id_isValid;

    float m_left;
    bool m_left_isSet;
    bool m_left_isValid;

    QString m_region_id;
    bool m_region_id_isSet;
    bool m_region_id_isValid;

    QString m_tag_id;
    bool m_tag_id_isSet;
    bool m_tag_id_isValid;

    QString m_tag_name;
    bool m_tag_name_isSet;
    bool m_tag_name_isValid;

    float m_top;
    bool m_top_isSet;
    bool m_top_isValid;

    float m_width;
    bool m_width_isSet;
    bool m_width_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageRegionCreateResult)

#endif // OAIImageRegionCreateResult_H
