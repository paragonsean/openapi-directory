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
 * OAIGetOrganizationDevices_200_response_inner.h
 *
 * 
 */

#ifndef OAIGetOrganizationDevices_200_response_inner_H
#define OAIGetOrganizationDevices_200_response_inner_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIGetOrganizationDevices_200_response_inner : public OAIObject {
public:
    OAIGetOrganizationDevices_200_response_inner();
    OAIGetOrganizationDevices_200_response_inner(QString json);
    ~OAIGetOrganizationDevices_200_response_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAddress() const;
    void setAddress(const QString &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    QString getFirmware() const;
    void setFirmware(const QString &firmware);
    bool is_firmware_Set() const;
    bool is_firmware_Valid() const;

    QString getLanIp() const;
    void setLanIp(const QString &lan_ip);
    bool is_lan_ip_Set() const;
    bool is_lan_ip_Valid() const;

    float getLat() const;
    void setLat(const float &lat);
    bool is_lat_Set() const;
    bool is_lat_Valid() const;

    float getLng() const;
    void setLng(const float &lng);
    bool is_lng_Set() const;
    bool is_lng_Valid() const;

    QString getMac() const;
    void setMac(const QString &mac);
    bool is_mac_Set() const;
    bool is_mac_Valid() const;

    QString getModel() const;
    void setModel(const QString &model);
    bool is_model_Set() const;
    bool is_model_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getNetworkId() const;
    void setNetworkId(const QString &network_id);
    bool is_network_id_Set() const;
    bool is_network_id_Valid() const;

    QString getNotes() const;
    void setNotes(const QString &notes);
    bool is_notes_Set() const;
    bool is_notes_Valid() const;

    QString getProductType() const;
    void setProductType(const QString &product_type);
    bool is_product_type_Set() const;
    bool is_product_type_Valid() const;

    QString getSerial() const;
    void setSerial(const QString &serial);
    bool is_serial_Set() const;
    bool is_serial_Valid() const;

    QList<QString> getTags() const;
    void setTags(const QList<QString> &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    QString m_firmware;
    bool m_firmware_isSet;
    bool m_firmware_isValid;

    QString m_lan_ip;
    bool m_lan_ip_isSet;
    bool m_lan_ip_isValid;

    float m_lat;
    bool m_lat_isSet;
    bool m_lat_isValid;

    float m_lng;
    bool m_lng_isSet;
    bool m_lng_isValid;

    QString m_mac;
    bool m_mac_isSet;
    bool m_mac_isValid;

    QString m_model;
    bool m_model_isSet;
    bool m_model_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_network_id;
    bool m_network_id_isSet;
    bool m_network_id_isValid;

    QString m_notes;
    bool m_notes_isSet;
    bool m_notes_isValid;

    QString m_product_type;
    bool m_product_type_isSet;
    bool m_product_type_isValid;

    QString m_serial;
    bool m_serial_isSet;
    bool m_serial_isValid;

    QList<QString> m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetOrganizationDevices_200_response_inner)

#endif // OAIGetOrganizationDevices_200_response_inner_H
