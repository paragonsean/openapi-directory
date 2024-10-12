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
 * OAINetworkAdapters.h
 *
 * Represents the network adapter on device.
 */

#ifndef OAINetworkAdapters_H
#define OAINetworkAdapters_H

#include <QJsonObject>

#include "OAINicIPv4.h"
#include "OAINicIPv6.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAINicIPv4;
class OAINicIPv6;

class OAINetworkAdapters : public OAIObject {
public:
    OAINetworkAdapters();
    OAINetworkAdapters(QString json);
    ~OAINetworkAdapters() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getInterfaceId() const;
    void setInterfaceId(const QString &interface_id);
    bool is_interface_id_Set() const;
    bool is_interface_id_Valid() const;

    bool isIsDefault() const;
    void setIsDefault(const bool &is_default);
    bool is_is_default_Set() const;
    bool is_is_default_Valid() const;

    QString getIscsiAndCloudStatus() const;
    void setIscsiAndCloudStatus(const QString &iscsi_and_cloud_status);
    bool is_iscsi_and_cloud_status_Set() const;
    bool is_iscsi_and_cloud_status_Valid() const;

    QString getMode() const;
    void setMode(const QString &mode);
    bool is_mode_Set() const;
    bool is_mode_Valid() const;

    QString getNetInterfaceStatus() const;
    void setNetInterfaceStatus(const QString &net_interface_status);
    bool is_net_interface_status_Set() const;
    bool is_net_interface_status_Valid() const;

    OAINicIPv4 getNicIpv4Settings() const;
    void setNicIpv4Settings(const OAINicIPv4 &nic_ipv4_settings);
    bool is_nic_ipv4_settings_Set() const;
    bool is_nic_ipv4_settings_Valid() const;

    OAINicIPv6 getNicIpv6Settings() const;
    void setNicIpv6Settings(const OAINicIPv6 &nic_ipv6_settings);
    bool is_nic_ipv6_settings_Set() const;
    bool is_nic_ipv6_settings_Valid() const;

    qint64 getSpeed() const;
    void setSpeed(const qint64 &speed);
    bool is_speed_Set() const;
    bool is_speed_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_interface_id;
    bool m_interface_id_isSet;
    bool m_interface_id_isValid;

    bool m_is_default;
    bool m_is_default_isSet;
    bool m_is_default_isValid;

    QString m_iscsi_and_cloud_status;
    bool m_iscsi_and_cloud_status_isSet;
    bool m_iscsi_and_cloud_status_isValid;

    QString m_mode;
    bool m_mode_isSet;
    bool m_mode_isValid;

    QString m_net_interface_status;
    bool m_net_interface_status_isSet;
    bool m_net_interface_status_isValid;

    OAINicIPv4 m_nic_ipv4_settings;
    bool m_nic_ipv4_settings_isSet;
    bool m_nic_ipv4_settings_isValid;

    OAINicIPv6 m_nic_ipv6_settings;
    bool m_nic_ipv6_settings_isSet;
    bool m_nic_ipv6_settings_isValid;

    qint64 m_speed;
    bool m_speed_isSet;
    bool m_speed_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAINetworkAdapters)

#endif // OAINetworkAdapters_H
