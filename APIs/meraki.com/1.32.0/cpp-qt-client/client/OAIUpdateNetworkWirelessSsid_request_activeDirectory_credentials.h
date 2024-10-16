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
 * OAIUpdateNetworkWirelessSsid_request_activeDirectory_credentials.h
 *
 * (Optional) The credentials of the user account to be used by the AP to bind to your Active Directory server. The Active Directory account should have permissions on all your Active Directory servers. Only valid if the splashPage is &#39;Password-protected with Active Directory&#39;.
 */

#ifndef OAIUpdateNetworkWirelessSsid_request_activeDirectory_credentials_H
#define OAIUpdateNetworkWirelessSsid_request_activeDirectory_credentials_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateNetworkWirelessSsid_request_activeDirectory_credentials : public OAIObject {
public:
    OAIUpdateNetworkWirelessSsid_request_activeDirectory_credentials();
    OAIUpdateNetworkWirelessSsid_request_activeDirectory_credentials(QString json);
    ~OAIUpdateNetworkWirelessSsid_request_activeDirectory_credentials() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getLogonName() const;
    void setLogonName(const QString &logon_name);
    bool is_logon_name_Set() const;
    bool is_logon_name_Valid() const;

    QString getPassword() const;
    void setPassword(const QString &password);
    bool is_password_Set() const;
    bool is_password_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_logon_name;
    bool m_logon_name_isSet;
    bool m_logon_name_isValid;

    QString m_password;
    bool m_password_isSet;
    bool m_password_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkWirelessSsid_request_activeDirectory_credentials)

#endif // OAIUpdateNetworkWirelessSsid_request_activeDirectory_credentials_H
