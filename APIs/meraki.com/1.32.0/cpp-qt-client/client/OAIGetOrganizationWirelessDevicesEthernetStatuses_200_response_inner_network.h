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
 * OAIGetOrganizationWirelessDevicesEthernetStatuses_200_response_inner_network.h
 *
 * Network details object
 */

#ifndef OAIGetOrganizationWirelessDevicesEthernetStatuses_200_response_inner_network_H
#define OAIGetOrganizationWirelessDevicesEthernetStatuses_200_response_inner_network_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetOrganizationWirelessDevicesEthernetStatuses_200_response_inner_network : public OAIObject {
public:
    OAIGetOrganizationWirelessDevicesEthernetStatuses_200_response_inner_network();
    OAIGetOrganizationWirelessDevicesEthernetStatuses_200_response_inner_network(QString json);
    ~OAIGetOrganizationWirelessDevicesEthernetStatuses_200_response_inner_network() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationWirelessDevicesEthernetStatuses_200_response_inner_network)

#endif // OAIGetOrganizationWirelessDevicesEthernetStatuses_200_response_inner_network_H
