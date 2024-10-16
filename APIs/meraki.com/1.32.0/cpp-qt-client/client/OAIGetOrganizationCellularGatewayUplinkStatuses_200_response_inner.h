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
 * OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner.h
 *
 * 
 */

#ifndef OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner_H
#define OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner_H

#include <QJsonObject>

#include "OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner_uplinks_inner.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner_uplinks_inner;

class OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner : public OAIObject {
public:
    OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner();
    OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner(QString json);
    ~OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getLastReportedAt() const;
    void setLastReportedAt(const QDateTime &last_reported_at);
    bool is_last_reported_at_Set() const;
    bool is_last_reported_at_Valid() const;

    QString getModel() const;
    void setModel(const QString &model);
    bool is_model_Set() const;
    bool is_model_Valid() const;

    QString getNetworkId() const;
    void setNetworkId(const QString &network_id);
    bool is_network_id_Set() const;
    bool is_network_id_Valid() const;

    QString getSerial() const;
    void setSerial(const QString &serial);
    bool is_serial_Set() const;
    bool is_serial_Valid() const;

    QList<OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner_uplinks_inner> getUplinks() const;
    void setUplinks(const QList<OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner_uplinks_inner> &uplinks);
    bool is_uplinks_Set() const;
    bool is_uplinks_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_last_reported_at;
    bool m_last_reported_at_isSet;
    bool m_last_reported_at_isValid;

    QString m_model;
    bool m_model_isSet;
    bool m_model_isValid;

    QString m_network_id;
    bool m_network_id_isSet;
    bool m_network_id_isValid;

    QString m_serial;
    bool m_serial_isSet;
    bool m_serial_isValid;

    QList<OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner_uplinks_inner> m_uplinks;
    bool m_uplinks_isSet;
    bool m_uplinks_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner)

#endif // OAIGetOrganizationCellularGatewayUplinkStatuses_200_response_inner_H
