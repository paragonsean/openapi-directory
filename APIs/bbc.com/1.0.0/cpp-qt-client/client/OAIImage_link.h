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
 * OAIImage_link.h
 *
 * 
 */

#ifndef OAIImage_link_H
#define OAIImage_link_H

#include <QJsonObject>

#include "OAIImage_link_image.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIImage_link_image;

class OAIImage_link : public OAIObject {
public:
    OAIImage_link();
    OAIImage_link(QString json);
    ~OAIImage_link() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIImage_link_image getImage() const;
    void setImage(const OAIImage_link_image &image);
    bool is_image_Set() const;
    bool is_image_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIImage_link_image m_image;
    bool m_image_isSet;
    bool m_image_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIImage_link)

#endif // OAIImage_link_H
