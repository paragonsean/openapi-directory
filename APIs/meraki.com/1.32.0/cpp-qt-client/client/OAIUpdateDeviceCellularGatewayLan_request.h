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
 * OAIUpdateDeviceCellularGatewayLan_request.h
 *
 * 
 */

#ifndef OAIUpdateDeviceCellularGatewayLan_request_H
#define OAIUpdateDeviceCellularGatewayLan_request_H

#include <QJsonObject>

#include "OAIUpdateDeviceCellularGatewayLan_request_fixedIpAssignments_inner.h"
#include "OAIUpdateDeviceCellularGatewayLan_request_reservedIpRanges_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIUpdateDeviceCellularGatewayLan_request_fixedIpAssignments_inner;
class OAIUpdateDeviceCellularGatewayLan_request_reservedIpRanges_inner;

class OAIUpdateDeviceCellularGatewayLan_request : public OAIObject {
public:
    OAIUpdateDeviceCellularGatewayLan_request();
    OAIUpdateDeviceCellularGatewayLan_request(QString json);
    ~OAIUpdateDeviceCellularGatewayLan_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIUpdateDeviceCellularGatewayLan_request_fixedIpAssignments_inner> getFixedIpAssignments() const;
    void setFixedIpAssignments(const QList<OAIUpdateDeviceCellularGatewayLan_request_fixedIpAssignments_inner> &fixed_ip_assignments);
    bool is_fixed_ip_assignments_Set() const;
    bool is_fixed_ip_assignments_Valid() const;

    QList<OAIUpdateDeviceCellularGatewayLan_request_reservedIpRanges_inner> getReservedIpRanges() const;
    void setReservedIpRanges(const QList<OAIUpdateDeviceCellularGatewayLan_request_reservedIpRanges_inner> &reserved_ip_ranges);
    bool is_reserved_ip_ranges_Set() const;
    bool is_reserved_ip_ranges_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIUpdateDeviceCellularGatewayLan_request_fixedIpAssignments_inner> m_fixed_ip_assignments;
    bool m_fixed_ip_assignments_isSet;
    bool m_fixed_ip_assignments_isValid;

    QList<OAIUpdateDeviceCellularGatewayLan_request_reservedIpRanges_inner> m_reserved_ip_ranges;
    bool m_reserved_ip_ranges_isSet;
    bool m_reserved_ip_ranges_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateDeviceCellularGatewayLan_request)

#endif // OAIUpdateDeviceCellularGatewayLan_request_H
