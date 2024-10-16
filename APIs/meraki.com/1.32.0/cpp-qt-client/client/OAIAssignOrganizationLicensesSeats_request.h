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
 * OAIAssignOrganizationLicensesSeats_request.h
 *
 * 
 */

#ifndef OAIAssignOrganizationLicensesSeats_request_H
#define OAIAssignOrganizationLicensesSeats_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAssignOrganizationLicensesSeats_request : public OAIObject {
public:
    OAIAssignOrganizationLicensesSeats_request();
    OAIAssignOrganizationLicensesSeats_request(QString json);
    ~OAIAssignOrganizationLicensesSeats_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getLicenseId() const;
    void setLicenseId(const QString &license_id);
    bool is_license_id_Set() const;
    bool is_license_id_Valid() const;

    QString getNetworkId() const;
    void setNetworkId(const QString &network_id);
    bool is_network_id_Set() const;
    bool is_network_id_Valid() const;

    qint32 getSeatCount() const;
    void setSeatCount(const qint32 &seat_count);
    bool is_seat_count_Set() const;
    bool is_seat_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_license_id;
    bool m_license_id_isSet;
    bool m_license_id_isValid;

    QString m_network_id;
    bool m_network_id_isSet;
    bool m_network_id_isValid;

    qint32 m_seat_count;
    bool m_seat_count_isSet;
    bool m_seat_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAssignOrganizationLicensesSeats_request)

#endif // OAIAssignOrganizationLicensesSeats_request_H
