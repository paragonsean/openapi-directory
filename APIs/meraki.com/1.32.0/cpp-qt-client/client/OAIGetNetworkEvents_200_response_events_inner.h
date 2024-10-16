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
 * OAIGetNetworkEvents_200_response_events_inner.h
 *
 * 
 */

#ifndef OAIGetNetworkEvents_200_response_events_inner_H
#define OAIGetNetworkEvents_200_response_events_inner_H

#include <QJsonObject>

#include "OAIGetNetworkEvents_200_response_events_inner_eventData.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetNetworkEvents_200_response_events_inner_eventData;

class OAIGetNetworkEvents_200_response_events_inner : public OAIObject {
public:
    OAIGetNetworkEvents_200_response_events_inner();
    OAIGetNetworkEvents_200_response_events_inner(QString json);
    ~OAIGetNetworkEvents_200_response_events_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCategory() const;
    void setCategory(const QString &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    QString getClientDescription() const;
    void setClientDescription(const QString &client_description);
    bool is_client_description_Set() const;
    bool is_client_description_Valid() const;

    QString getClientId() const;
    void setClientId(const QString &client_id);
    bool is_client_id_Set() const;
    bool is_client_id_Valid() const;

    QString getClientMac() const;
    void setClientMac(const QString &client_mac);
    bool is_client_mac_Set() const;
    bool is_client_mac_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QString getDeviceName() const;
    void setDeviceName(const QString &device_name);
    bool is_device_name_Set() const;
    bool is_device_name_Valid() const;

    QString getDeviceSerial() const;
    void setDeviceSerial(const QString &device_serial);
    bool is_device_serial_Set() const;
    bool is_device_serial_Valid() const;

    OAIGetNetworkEvents_200_response_events_inner_eventData getEventData() const;
    void setEventData(const OAIGetNetworkEvents_200_response_events_inner_eventData &event_data);
    bool is_event_data_Set() const;
    bool is_event_data_Valid() const;

    QString getNetworkId() const;
    void setNetworkId(const QString &network_id);
    bool is_network_id_Set() const;
    bool is_network_id_Valid() const;

    QString getOccurredAt() const;
    void setOccurredAt(const QString &occurred_at);
    bool is_occurred_at_Set() const;
    bool is_occurred_at_Valid() const;

    qint32 getSsidNumber() const;
    void setSsidNumber(const qint32 &ssid_number);
    bool is_ssid_number_Set() const;
    bool is_ssid_number_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    QString m_client_description;
    bool m_client_description_isSet;
    bool m_client_description_isValid;

    QString m_client_id;
    bool m_client_id_isSet;
    bool m_client_id_isValid;

    QString m_client_mac;
    bool m_client_mac_isSet;
    bool m_client_mac_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QString m_device_name;
    bool m_device_name_isSet;
    bool m_device_name_isValid;

    QString m_device_serial;
    bool m_device_serial_isSet;
    bool m_device_serial_isValid;

    OAIGetNetworkEvents_200_response_events_inner_eventData m_event_data;
    bool m_event_data_isSet;
    bool m_event_data_isValid;

    QString m_network_id;
    bool m_network_id_isSet;
    bool m_network_id_isValid;

    QString m_occurred_at;
    bool m_occurred_at_isSet;
    bool m_occurred_at_isValid;

    qint32 m_ssid_number;
    bool m_ssid_number_isSet;
    bool m_ssid_number_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetNetworkEvents_200_response_events_inner)

#endif // OAIGetNetworkEvents_200_response_events_inner_H
