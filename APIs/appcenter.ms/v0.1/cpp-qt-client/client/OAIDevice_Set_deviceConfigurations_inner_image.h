/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDevice_Set_deviceConfigurations_inner_image.h
 *
 * 
 */

#ifndef OAIDevice_Set_deviceConfigurations_inner_image_H
#define OAIDevice_Set_deviceConfigurations_inner_image_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIDevice_Set_deviceConfigurations_inner_image : public OAIObject {
public:
    OAIDevice_Set_deviceConfigurations_inner_image();
    OAIDevice_Set_deviceConfigurations_inner_image(QString json);
    ~OAIDevice_Set_deviceConfigurations_inner_image() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getThumb() const;
    void setThumb(const QString &thumb);
    bool is_thumb_Set() const;
    bool is_thumb_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_thumb;
    bool m_thumb_isSet;
    bool m_thumb_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDevice_Set_deviceConfigurations_inner_image)

#endif // OAIDevice_Set_deviceConfigurations_inner_image_H
