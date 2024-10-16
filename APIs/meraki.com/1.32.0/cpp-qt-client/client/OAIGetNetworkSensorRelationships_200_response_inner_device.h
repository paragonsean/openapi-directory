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
 * OAIGetNetworkSensorRelationships_200_response_inner_device.h
 *
 * A sensor or gateway device in the network
 */

#ifndef OAIGetNetworkSensorRelationships_200_response_inner_device_H
#define OAIGetNetworkSensorRelationships_200_response_inner_device_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetNetworkSensorRelationships_200_response_inner_device : public OAIObject {
public:
    OAIGetNetworkSensorRelationships_200_response_inner_device();
    OAIGetNetworkSensorRelationships_200_response_inner_device(QString json);
    ~OAIGetNetworkSensorRelationships_200_response_inner_device() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getProductType() const;
    void setProductType(const QString &product_type);
    bool is_product_type_Set() const;
    bool is_product_type_Valid() const;

    QString getSerial() const;
    void setSerial(const QString &serial);
    bool is_serial_Set() const;
    bool is_serial_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_product_type;
    bool m_product_type_isSet;
    bool m_product_type_isValid;

    QString m_serial;
    bool m_serial_isSet;
    bool m_serial_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkSensorRelationships_200_response_inner_device)

#endif // OAIGetNetworkSensorRelationships_200_response_inner_device_H
