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
 * OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade.h
 *
 * Details of the next firmware upgrade on the device
 */

#ifndef OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade_H
#define OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade_H

#include <QJsonObject>

#include "OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade_toVersion.h"
#include <QDateTime>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade_toVersion;

class OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade : public OAIObject {
public:
    OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade();
    OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade(QString json);
    ~OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getTime() const;
    void setTime(const QDateTime &time);
    bool is_time_Set() const;
    bool is_time_Valid() const;

    OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade_toVersion getToVersion() const;
    void setToVersion(const OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade_toVersion &to_version);
    bool is_to_version_Set() const;
    bool is_to_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_time;
    bool m_time_isSet;
    bool m_time_isValid;

    OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade_toVersion m_to_version;
    bool m_to_version_isSet;
    bool m_to_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade)

#endif // OAIGetNetworkFirmwareUpgrades_200_response_products_appliance_nextUpgrade_H
