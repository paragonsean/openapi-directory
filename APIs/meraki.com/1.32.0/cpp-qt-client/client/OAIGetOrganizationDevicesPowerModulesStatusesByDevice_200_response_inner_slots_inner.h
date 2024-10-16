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
 * OAIGetOrganizationDevicesPowerModulesStatusesByDevice_200_response_inner_slots_inner.h
 *
 * 
 */

#ifndef OAIGetOrganizationDevicesPowerModulesStatusesByDevice_200_response_inner_slots_inner_H
#define OAIGetOrganizationDevicesPowerModulesStatusesByDevice_200_response_inner_slots_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetOrganizationDevicesPowerModulesStatusesByDevice_200_response_inner_slots_inner : public OAIObject {
public:
    OAIGetOrganizationDevicesPowerModulesStatusesByDevice_200_response_inner_slots_inner();
    OAIGetOrganizationDevicesPowerModulesStatusesByDevice_200_response_inner_slots_inner(QString json);
    ~OAIGetOrganizationDevicesPowerModulesStatusesByDevice_200_response_inner_slots_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getModel() const;
    void setModel(const QString &model);
    bool is_model_Set() const;
    bool is_model_Valid() const;

    qint32 getNumber() const;
    void setNumber(const qint32 &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    QString getSerial() const;
    void setSerial(const QString &serial);
    bool is_serial_Set() const;
    bool is_serial_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_model;
    bool m_model_isSet;
    bool m_model_isValid;

    qint32 m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    QString m_serial;
    bool m_serial_isSet;
    bool m_serial_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationDevicesPowerModulesStatusesByDevice_200_response_inner_slots_inner)

#endif // OAIGetOrganizationDevicesPowerModulesStatusesByDevice_200_response_inner_slots_inner_H
