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
 * OAIAlternate_images_mixin.h
 *
 * 
 */

#ifndef OAIAlternate_images_mixin_H
#define OAIAlternate_images_mixin_H

#include <QJsonObject>

#include "OAIAlternate_images_mixin_alternate_images.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAlternate_images_mixin_alternate_images;

class OAIAlternate_images_mixin : public OAIObject {
public:
    OAIAlternate_images_mixin();
    OAIAlternate_images_mixin(QString json);
    ~OAIAlternate_images_mixin() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAlternate_images_mixin_alternate_images getAlternateImages() const;
    void setAlternateImages(const OAIAlternate_images_mixin_alternate_images &alternate_images);
    bool is_alternate_images_Set() const;
    bool is_alternate_images_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAlternate_images_mixin_alternate_images m_alternate_images;
    bool m_alternate_images_isSet;
    bool m_alternate_images_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAlternate_images_mixin)

#endif // OAIAlternate_images_mixin_H
