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

#include "OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image() {
    this->initializeModel();
}

OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::~OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image() {}

void OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::initializeModel() {

    m_preview_isSet = false;
    m_preview_isValid = false;
}

void OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::fromJsonObject(QJsonObject json) {

    m_preview_isValid = ::OpenAPI::fromJsonValue(m_preview, json[QString("preview")]);
    m_preview_isSet = !json[QString("preview")].isNull() && m_preview_isValid;
}

QString OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::asJsonObject() const {
    QJsonObject obj;
    if (m_preview.isSet()) {
        obj.insert(QString("preview"), ::OpenAPI::toJsonValue(m_preview));
    }
    return obj;
}

OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image_preview OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::getPreview() const {
    return m_preview;
}
void OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::setPreview(const OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image_preview &preview) {
    m_preview = preview;
    m_preview_isSet = true;
}

bool OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::is_preview_Set() const{
    return m_preview_isSet;
}

bool OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::is_preview_Valid() const{
    return m_preview_isValid;
}

bool OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_preview.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetOrganizationBrandingPolicies_200_response_inner_customLogo_image::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
