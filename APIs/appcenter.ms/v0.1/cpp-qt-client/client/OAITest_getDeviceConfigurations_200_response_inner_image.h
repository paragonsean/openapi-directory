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
 * OAITest_getDeviceConfigurations_200_response_inner_image.h
 *
 * 
 */

#ifndef OAITest_getDeviceConfigurations_200_response_inner_image_H
#define OAITest_getDeviceConfigurations_200_response_inner_image_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAITest_getDeviceConfigurations_200_response_inner_image : public OAIObject {
public:
    OAITest_getDeviceConfigurations_200_response_inner_image();
    OAITest_getDeviceConfigurations_200_response_inner_image(QString json);
    ~OAITest_getDeviceConfigurations_200_response_inner_image() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFull() const;
    void setFull(const QString &full);
    bool is_full_Set() const;
    bool is_full_Valid() const;

    QString getThumb() const;
    void setThumb(const QString &thumb);
    bool is_thumb_Set() const;
    bool is_thumb_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_full;
    bool m_full_isSet;
    bool m_full_isValid;

    QString m_thumb;
    bool m_thumb_isSet;
    bool m_thumb_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITest_getDeviceConfigurations_200_response_inner_image)

#endif // OAITest_getDeviceConfigurations_200_response_inner_image_H
