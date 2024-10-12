/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIConfigureDeviceRequestProperties.h
 *
 * The properties of the configure device request.
 */

#ifndef OAIConfigureDeviceRequestProperties_H
#define OAIConfigureDeviceRequestProperties_H

#include <QJsonObject>

#include "OAINetworkInterfaceData0Settings.h"
#include "OAISecondaryDNSSettings.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAISecondaryDNSSettings;
class OAINetworkInterfaceData0Settings;

class OAIConfigureDeviceRequestProperties : public OAIObject {
public:
    OAIConfigureDeviceRequestProperties();
    OAIConfigureDeviceRequestProperties(QString json);
    ~OAIConfigureDeviceRequestProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCurrentDeviceName() const;
    void setCurrentDeviceName(const QString &current_device_name);
    bool is_current_device_name_Set() const;
    bool is_current_device_name_Valid() const;

    OAISecondaryDNSSettings getDnsSettings() const;
    void setDnsSettings(const OAISecondaryDNSSettings &dns_settings);
    bool is_dns_settings_Set() const;
    bool is_dns_settings_Valid() const;

    QString getFriendlyName() const;
    void setFriendlyName(const QString &friendly_name);
    bool is_friendly_name_Set() const;
    bool is_friendly_name_Valid() const;

    OAINetworkInterfaceData0Settings getNetworkInterfaceData0Settings() const;
    void setNetworkInterfaceData0Settings(const OAINetworkInterfaceData0Settings &network_interface_data0_settings);
    bool is_network_interface_data0_settings_Set() const;
    bool is_network_interface_data0_settings_Valid() const;

    QString getTimeZone() const;
    void setTimeZone(const QString &time_zone);
    bool is_time_zone_Set() const;
    bool is_time_zone_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_current_device_name;
    bool m_current_device_name_isSet;
    bool m_current_device_name_isValid;

    OAISecondaryDNSSettings m_dns_settings;
    bool m_dns_settings_isSet;
    bool m_dns_settings_isValid;

    QString m_friendly_name;
    bool m_friendly_name_isSet;
    bool m_friendly_name_isValid;

    OAINetworkInterfaceData0Settings m_network_interface_data0_settings;
    bool m_network_interface_data0_settings_isSet;
    bool m_network_interface_data0_settings_isValid;

    QString m_time_zone;
    bool m_time_zone_isSet;
    bool m_time_zone_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIConfigureDeviceRequestProperties)

#endif // OAIConfigureDeviceRequestProperties_H
