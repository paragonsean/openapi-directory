/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image.h
 *
 * Properties of the image.
 */

#ifndef OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image_H
#define OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image_H

#include <QJsonObject>

#include "OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image_preview.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image_preview;

class OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image : public OAIObject {
public:
    OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image();
    OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image(QString json);
    ~OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image_preview getPreview() const;
    void setPreview(const OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image_preview &preview);
    bool is_preview_Set() const;
    bool is_preview_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image_preview m_preview;
    bool m_preview_isSet;
    bool m_preview_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image)

#endif // OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image_H
