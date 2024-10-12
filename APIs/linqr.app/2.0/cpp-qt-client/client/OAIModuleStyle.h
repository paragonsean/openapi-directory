/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIModuleStyle.h
 *
 * 
 */

#ifndef OAIModuleStyle_H
#define OAIModuleStyle_H

#include <QJsonObject>

#include "OAIColor.h"
#include "OAIModuleShapes.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIColor;

class OAIModuleStyle : public OAIObject {
public:
    OAIModuleStyle();
    OAIModuleStyle(QString json);
    ~OAIModuleStyle() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIColor getColor() const;
    void setColor(const OAIColor &color);
    bool is_color_Set() const;
    bool is_color_Valid() const;

    OAIModuleShapes getShape() const;
    void setShape(const OAIModuleShapes &shape);
    bool is_shape_Set() const;
    bool is_shape_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIColor m_color;
    bool m_color_isSet;
    bool m_color_isValid;

    OAIModuleShapes m_shape;
    bool m_shape_isSet;
    bool m_shape_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIModuleStyle)

#endif // OAIModuleStyle_H
