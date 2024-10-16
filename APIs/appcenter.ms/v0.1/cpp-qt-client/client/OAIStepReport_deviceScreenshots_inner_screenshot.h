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
 * OAIStepReport_deviceScreenshots_inner_screenshot.h
 *
 * 
 */

#ifndef OAIStepReport_deviceScreenshots_inner_screenshot_H
#define OAIStepReport_deviceScreenshots_inner_screenshot_H

#include <QJsonObject>

#include "OAIStepReport_deviceScreenshots_inner_screenshot_urls.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIStepReport_deviceScreenshots_inner_screenshot_urls;

class OAIStepReport_deviceScreenshots_inner_screenshot : public OAIObject {
public:
    OAIStepReport_deviceScreenshots_inner_screenshot();
    OAIStepReport_deviceScreenshots_inner_screenshot(QString json);
    ~OAIStepReport_deviceScreenshots_inner_screenshot() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isLandscape() const;
    void setLandscape(const bool &landscape);
    bool is_landscape_Set() const;
    bool is_landscape_Valid() const;

    double getRotation() const;
    void setRotation(const double &rotation);
    bool is_rotation_Set() const;
    bool is_rotation_Valid() const;

    OAIStepReport_deviceScreenshots_inner_screenshot_urls getUrls() const;
    void setUrls(const OAIStepReport_deviceScreenshots_inner_screenshot_urls &urls);
    bool is_urls_Set() const;
    bool is_urls_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_landscape;
    bool m_landscape_isSet;
    bool m_landscape_isValid;

    double m_rotation;
    bool m_rotation_isSet;
    bool m_rotation_isValid;

    OAIStepReport_deviceScreenshots_inner_screenshot_urls m_urls;
    bool m_urls_isSet;
    bool m_urls_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStepReport_deviceScreenshots_inner_screenshot)

#endif // OAIStepReport_deviceScreenshots_inner_screenshot_H
