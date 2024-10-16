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
 * OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner.h
 *
 * 
 */

#ifndef OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner_H
#define OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner_H

#include <QJsonObject>

#include "OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner_upgrade.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner_upgrade;

class OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner : public OAIObject {
public:
    OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner();
    OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner(QString json);
    ~OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDeviceStatus() const;
    void setDeviceStatus(const QString &device_status);
    bool is_device_status_Set() const;
    bool is_device_status_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getSerial() const;
    void setSerial(const QString &serial);
    bool is_serial_Set() const;
    bool is_serial_Valid() const;

    OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner_upgrade getUpgrade() const;
    void setUpgrade(const OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner_upgrade &upgrade);
    bool is_upgrade_Set() const;
    bool is_upgrade_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_device_status;
    bool m_device_status_isSet;
    bool m_device_status_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_serial;
    bool m_serial_isSet;
    bool m_serial_isValid;

    OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner_upgrade m_upgrade;
    bool m_upgrade_isSet;
    bool m_upgrade_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner)

#endif // OAIGetOrganizationFirmwareUpgradesByDevice_200_response_inner_H
