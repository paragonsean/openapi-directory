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
 * OAIStyle.h
 *
 * 
 */

#ifndef OAIStyle_H
#define OAIStyle_H

#include <QJsonObject>

#include "OAIBackgroundStyle.h"
#include "OAIInnerEyeStyle.h"
#include "OAIModuleStyle.h"
#include "OAIOuterEyeStyle.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBackgroundStyle;
class OAIInnerEyeStyle;
class OAIModuleStyle;
class OAIOuterEyeStyle;

class OAIStyle : public OAIObject {
public:
    OAIStyle();
    OAIStyle(QString json);
    ~OAIStyle() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIBackgroundStyle getBackground() const;
    void setBackground(const OAIBackgroundStyle &background);
    bool is_background_Set() const;
    bool is_background_Valid() const;

    OAIInnerEyeStyle getInnerEye() const;
    void setInnerEye(const OAIInnerEyeStyle &inner_eye);
    bool is_inner_eye_Set() const;
    bool is_inner_eye_Valid() const;

    OAIModuleStyle getModule() const;
    void setModule(const OAIModuleStyle &module);
    bool is_module_Set() const;
    bool is_module_Valid() const;

    OAIOuterEyeStyle getOuterEye() const;
    void setOuterEye(const OAIOuterEyeStyle &outer_eye);
    bool is_outer_eye_Set() const;
    bool is_outer_eye_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIBackgroundStyle m_background;
    bool m_background_isSet;
    bool m_background_isValid;

    OAIInnerEyeStyle m_inner_eye;
    bool m_inner_eye_isSet;
    bool m_inner_eye_isValid;

    OAIModuleStyle m_module;
    bool m_module_isSet;
    bool m_module_isValid;

    OAIOuterEyeStyle m_outer_eye;
    bool m_outer_eye_isSet;
    bool m_outer_eye_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStyle)

#endif // OAIStyle_H
