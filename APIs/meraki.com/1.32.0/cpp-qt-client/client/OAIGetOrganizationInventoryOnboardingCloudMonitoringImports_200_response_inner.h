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
 * OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner.h
 *
 * 
 */

#ifndef OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner_H
#define OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner_H

#include <QJsonObject>

#include "OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner_device.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner_device;

class OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner : public OAIObject {
public:
    OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner();
    OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner(QString json);
    ~OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner_device getDevice() const;
    void setDevice(const OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner_device &device);
    bool is_device_Set() const;
    bool is_device_Valid() const;

    QString getImportId() const;
    void setImportId(const QString &import_id);
    bool is_import_id_Set() const;
    bool is_import_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner_device m_device;
    bool m_device_isSet;
    bool m_device_isValid;

    QString m_import_id;
    bool m_import_id_isSet;
    bool m_import_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner)

#endif // OAIGetOrganizationInventoryOnboardingCloudMonitoringImports_200_response_inner_H
