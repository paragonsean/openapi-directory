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
 * OAIProvisionNetworkClients_request_policiesBySsid_0.h
 *
 * The number for the SSID
 */

#ifndef OAIProvisionNetworkClients_request_policiesBySsid_0_H
#define OAIProvisionNetworkClients_request_policiesBySsid_0_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIProvisionNetworkClients_request_policiesBySsid_0 : public OAIObject {
public:
    OAIProvisionNetworkClients_request_policiesBySsid_0();
    OAIProvisionNetworkClients_request_policiesBySsid_0(QString json);
    ~OAIProvisionNetworkClients_request_policiesBySsid_0() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDevicePolicy() const;
    void setDevicePolicy(const QString &device_policy);
    bool is_device_policy_Set() const;
    bool is_device_policy_Valid() const;

    QString getGroupPolicyId() const;
    void setGroupPolicyId(const QString &group_policy_id);
    bool is_group_policy_id_Set() const;
    bool is_group_policy_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_device_policy;
    bool m_device_policy_isSet;
    bool m_device_policy_isValid;

    QString m_group_policy_id;
    bool m_group_policy_id_isSet;
    bool m_group_policy_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProvisionNetworkClients_request_policiesBySsid_0)

#endif // OAIProvisionNetworkClients_request_policiesBySsid_0_H
