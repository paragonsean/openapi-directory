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
 * OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_tunnel_rootCertificate.h
 *
 * Root certificate information
 */

#ifndef OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_tunnel_rootCertificate_H
#define OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_tunnel_rootCertificate_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_tunnel_rootCertificate : public OAIObject {
public:
    OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_tunnel_rootCertificate();
    OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_tunnel_rootCertificate(QString json);
    ~OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_tunnel_rootCertificate() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getContent() const;
    void setContent(const QString &content);
    bool is_content_Set() const;
    bool is_content_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_content;
    bool m_content_isSet;
    bool m_content_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_tunnel_rootCertificate)

#endif // OAICreateOrganizationInventoryOnboardingCloudMonitoringPrepare_201_response_inner_configParams_tunnel_rootCertificate_H
