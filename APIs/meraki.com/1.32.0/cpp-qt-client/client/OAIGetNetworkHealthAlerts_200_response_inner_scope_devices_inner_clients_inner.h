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
 * OAIGetNetworkHealthAlerts_200_response_inner_scope_devices_inner_clients_inner.h
 *
 * 
 */

#ifndef OAIGetNetworkHealthAlerts_200_response_inner_scope_devices_inner_clients_inner_H
#define OAIGetNetworkHealthAlerts_200_response_inner_scope_devices_inner_clients_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetNetworkHealthAlerts_200_response_inner_scope_devices_inner_clients_inner : public OAIObject {
public:
    OAIGetNetworkHealthAlerts_200_response_inner_scope_devices_inner_clients_inner();
    OAIGetNetworkHealthAlerts_200_response_inner_scope_devices_inner_clients_inner(QString json);
    ~OAIGetNetworkHealthAlerts_200_response_inner_scope_devices_inner_clients_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getMac() const;
    void setMac(const QString &mac);
    bool is_mac_Set() const;
    bool is_mac_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_mac;
    bool m_mac_isSet;
    bool m_mac_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkHealthAlerts_200_response_inner_scope_devices_inner_clients_inner)

#endif // OAIGetNetworkHealthAlerts_200_response_inner_scope_devices_inner_clients_inner_H
