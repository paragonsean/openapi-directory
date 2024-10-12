/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_apiDefinition.h
 *
 * Information about the formal API definition for the app.
 */

#ifndef OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_apiDefinition_H
#define OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_apiDefinition_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_apiDefinition : public OAIObject {
public:
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_apiDefinition();
    OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_apiDefinition(QString json);
    ~OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_apiDefinition() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getUrl() const;
    void setUrl(const QString &url);
    bool is_url_Set() const;
    bool is_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_url;
    bool m_url_isSet;
    bool m_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_apiDefinition)

#endif // OAIAppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_apiDefinition_H
