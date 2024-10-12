/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOrderProperties.h
 *
 * Order properties.
 */

#ifndef OAIOrderProperties_H
#define OAIOrderProperties_H

#include <QJsonObject>

#include "OAIAddress.h"
#include "OAIContactDetails.h"
#include "OAIOrderStatus.h"
#include "OAITrackingInfo.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIContactDetails;
class OAIOrderStatus;
class OAITrackingInfo;
class OAIAddress;

class OAIOrderProperties : public OAIObject {
public:
    OAIOrderProperties();
    OAIOrderProperties(QString json);
    ~OAIOrderProperties() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIContactDetails getContactInformation() const;
    void setContactInformation(const OAIContactDetails &contact_information);
    bool is_contact_information_Set() const;
    bool is_contact_information_Valid() const;

    OAIOrderStatus getCurrentStatus() const;
    void setCurrentStatus(const OAIOrderStatus &current_status);
    bool is_current_status_Set() const;
    bool is_current_status_Valid() const;

    QList<OAITrackingInfo> getDeliveryTrackingInfo() const;
    void setDeliveryTrackingInfo(const QList<OAITrackingInfo> &delivery_tracking_info);
    bool is_delivery_tracking_info_Set() const;
    bool is_delivery_tracking_info_Valid() const;

    QList<OAIOrderStatus> getOrderHistory() const;
    void setOrderHistory(const QList<OAIOrderStatus> &order_history);
    bool is_order_history_Set() const;
    bool is_order_history_Valid() const;

    QList<OAITrackingInfo> getReturnTrackingInfo() const;
    void setReturnTrackingInfo(const QList<OAITrackingInfo> &return_tracking_info);
    bool is_return_tracking_info_Set() const;
    bool is_return_tracking_info_Valid() const;

    QString getSerialNumber() const;
    void setSerialNumber(const QString &serial_number);
    bool is_serial_number_Set() const;
    bool is_serial_number_Valid() const;

    OAIAddress getShippingAddress() const;
    void setShippingAddress(const OAIAddress &shipping_address);
    bool is_shipping_address_Set() const;
    bool is_shipping_address_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIContactDetails m_contact_information;
    bool m_contact_information_isSet;
    bool m_contact_information_isValid;

    OAIOrderStatus m_current_status;
    bool m_current_status_isSet;
    bool m_current_status_isValid;

    QList<OAITrackingInfo> m_delivery_tracking_info;
    bool m_delivery_tracking_info_isSet;
    bool m_delivery_tracking_info_isValid;

    QList<OAIOrderStatus> m_order_history;
    bool m_order_history_isSet;
    bool m_order_history_isValid;

    QList<OAITrackingInfo> m_return_tracking_info;
    bool m_return_tracking_info_isSet;
    bool m_return_tracking_info_isValid;

    QString m_serial_number;
    bool m_serial_number_isSet;
    bool m_serial_number_isValid;

    OAIAddress m_shipping_address;
    bool m_shipping_address_isSet;
    bool m_shipping_address_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOrderProperties)

#endif // OAIOrderProperties_H
