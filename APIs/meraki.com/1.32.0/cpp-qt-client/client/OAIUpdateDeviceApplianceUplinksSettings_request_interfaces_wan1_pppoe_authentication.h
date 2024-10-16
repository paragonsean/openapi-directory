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
 * OAIUpdateDeviceApplianceUplinksSettings_request_interfaces_wan1_pppoe_authentication.h
 *
 * Settings for PPPoE Authentication.
 */

#ifndef OAIUpdateDeviceApplianceUplinksSettings_request_interfaces_wan1_pppoe_authentication_H
#define OAIUpdateDeviceApplianceUplinksSettings_request_interfaces_wan1_pppoe_authentication_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateDeviceApplianceUplinksSettings_request_interfaces_wan1_pppoe_authentication : public OAIObject {
public:
    OAIUpdateDeviceApplianceUplinksSettings_request_interfaces_wan1_pppoe_authentication();
    OAIUpdateDeviceApplianceUplinksSettings_request_interfaces_wan1_pppoe_authentication(QString json);
    ~OAIUpdateDeviceApplianceUplinksSettings_request_interfaces_wan1_pppoe_authentication() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    QString getUsername() const;
    void setUsername(const QString &username);
    bool is_username_Set() const;
    bool is_username_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;

    QString m_username;
    bool m_username_isSet;
    bool m_username_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateDeviceApplianceUplinksSettings_request_interfaces_wan1_pppoe_authentication)

#endif // OAIUpdateDeviceApplianceUplinksSettings_request_interfaces_wan1_pppoe_authentication_H
