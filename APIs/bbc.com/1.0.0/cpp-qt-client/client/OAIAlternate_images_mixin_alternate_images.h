/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAlternate_images_mixin_alternate_images.h
 *
 * 
 */

#ifndef OAIAlternate_images_mixin_alternate_images_H
#define OAIAlternate_images_mixin_alternate_images_H

#include <QJsonObject>

#include "OAIAlternate_images_mixin_alternate_images_alternate_image_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAlternate_images_mixin_alternate_images_alternate_image_inner;

class OAIAlternate_images_mixin_alternate_images : public OAIObject {
public:
    OAIAlternate_images_mixin_alternate_images();
    OAIAlternate_images_mixin_alternate_images(QString json);
    ~OAIAlternate_images_mixin_alternate_images() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIAlternate_images_mixin_alternate_images_alternate_image_inner> getAlternateImage() const;
    void setAlternateImage(const QList<OAIAlternate_images_mixin_alternate_images_alternate_image_inner> &alternate_image);
    bool is_alternate_image_Set() const;
    bool is_alternate_image_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIAlternate_images_mixin_alternate_images_alternate_image_inner> m_alternate_image;
    bool m_alternate_image_isSet;
    bool m_alternate_image_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAlternate_images_mixin_alternate_images)

#endif // OAIAlternate_images_mixin_alternate_images_H
