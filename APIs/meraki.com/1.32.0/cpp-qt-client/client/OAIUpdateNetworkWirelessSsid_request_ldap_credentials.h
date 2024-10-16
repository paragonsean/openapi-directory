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
 * OAIUpdateNetworkWirelessSsid_request_ldap_credentials.h
 *
 * (Optional) The credentials of the user account to be used by the AP to bind to your LDAP server. The LDAP account should have permissions on all your LDAP servers.
 */

#ifndef OAIUpdateNetworkWirelessSsid_request_ldap_credentials_H
#define OAIUpdateNetworkWirelessSsid_request_ldap_credentials_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateNetworkWirelessSsid_request_ldap_credentials : public OAIObject {
public:
    OAIUpdateNetworkWirelessSsid_request_ldap_credentials();
    OAIUpdateNetworkWirelessSsid_request_ldap_credentials(QString json);
    ~OAIUpdateNetworkWirelessSsid_request_ldap_credentials() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDistinguishedName() const;
    void setDistinguishedName(const QString &distinguished_name);
    bool is_distinguished_name_Set() const;
    bool is_distinguished_name_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_distinguished_name;
    bool m_distinguished_name_isSet;
    bool m_distinguished_name_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkWirelessSsid_request_ldap_credentials)

#endif // OAIUpdateNetworkWirelessSsid_request_ldap_credentials_H
