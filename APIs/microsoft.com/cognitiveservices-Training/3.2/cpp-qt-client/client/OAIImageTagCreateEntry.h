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
 * OAIImageTagCreateEntry.h
 *
 * Entry associating a tag to an image.
 */

#ifndef OAIImageTagCreateEntry_H
#define OAIImageTagCreateEntry_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIImageTagCreateEntry : public OAIObject {
public:
    OAIImageTagCreateEntry();
    OAIImageTagCreateEntry(QString json);
    ~OAIImageTagCreateEntry() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getImageId() const;
    void setImageId(const QString &image_id);
    bool is_image_id_Set() const;
    bool is_image_id_Valid() const;

    QString getTagId() const;
    void setTagId(const QString &tag_id);
    bool is_tag_id_Set() const;
    bool is_tag_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_image_id;
    bool m_image_id_isSet;
    bool m_image_id_isValid;

    QString m_tag_id;
    bool m_tag_id_isSet;
    bool m_tag_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImageTagCreateEntry)

#endif // OAIImageTagCreateEntry_H
