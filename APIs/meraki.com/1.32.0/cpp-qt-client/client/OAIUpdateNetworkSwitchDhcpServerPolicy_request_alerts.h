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
 * OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts.h
 *
 * Alert settings for DHCP servers
 */

#ifndef OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts_H
#define OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts_H

#include <QJsonObject>

#include "OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts_email.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts_email;

class OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts : public OAIObject {
public:
    OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts();
    OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts(QString json);
    ~OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts_email getEmail() const;
    void setEmail(const OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts_email &email);
    bool is_email_Set() const;
    bool is_email_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts_email m_email;
    bool m_email_isSet;
    bool m_email_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts)

#endif // OAIUpdateNetworkSwitchDhcpServerPolicy_request_alerts_H
