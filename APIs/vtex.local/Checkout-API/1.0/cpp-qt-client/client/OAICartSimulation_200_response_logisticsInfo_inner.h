/**
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAICartSimulation_200_response_logisticsInfo_inner.h
 *
 * 
 */

#ifndef OAICartSimulation_200_response_logisticsInfo_inner_H
#define OAICartSimulation_200_response_logisticsInfo_inner_H

#include <QJsonObject>

#include "OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_deliveryChannels_inner.h"
#include "OAICartSimulation_200_response_logisticsInfo_inner_itemMetadata.h"
#include "OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions.h"
#include "OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner.h"
#include "OAICartSimulation_200_response_logisticsInfo_inner_totals_inner.h"
#include "OAIObject.h"
#include <QJsonValue>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_deliveryChannels_inner;
class OAICartSimulation_200_response_logisticsInfo_inner_itemMetadata;
class OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions;
class OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner;
class OAICartSimulation_200_response_logisticsInfo_inner_totals_inner;

class OAICartSimulation_200_response_logisticsInfo_inner : public OAIObject {
public:
    OAICartSimulation_200_response_logisticsInfo_inner();
    OAICartSimulation_200_response_logisticsInfo_inner(QString json);
    ~OAICartSimulation_200_response_logisticsInfo_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAddressId() const;
    void setAddressId(const QString &address_id);
    bool is_address_id_Set() const;
    bool is_address_id_Valid() const;

    QList<OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_deliveryChannels_inner> getDeliveryChannels() const;
    void setDeliveryChannels(const QList<OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_deliveryChannels_inner> &delivery_channels);
    bool is_delivery_channels_Set() const;
    bool is_delivery_channels_Valid() const;

    qint32 getItemIndex() const;
    void setItemIndex(const qint32 &item_index);
    bool is_item_index_Set() const;
    bool is_item_index_Valid() const;

    OAICartSimulation_200_response_logisticsInfo_inner_itemMetadata getItemMetadata() const;
    void setItemMetadata(const OAICartSimulation_200_response_logisticsInfo_inner_itemMetadata &item_metadata);
    bool is_item_metadata_Set() const;
    bool is_item_metadata_Valid() const;

    QList<QJsonValue> getMessages() const;
    void setMessages(const QList<QJsonValue> &messages);
    bool is_messages_Set() const;
    bool is_messages_Valid() const;

    QList<QJsonValue> getPickupPoints() const;
    void setPickupPoints(const QList<QJsonValue> &pickup_points);
    bool is_pickup_points_Set() const;
    bool is_pickup_points_Valid() const;

    OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions getPurchaseConditions() const;
    void setPurchaseConditions(const OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions &purchase_conditions);
    bool is_purchase_conditions_Set() const;
    bool is_purchase_conditions_Valid() const;

    qint32 getQuantity() const;
    void setQuantity(const qint32 &quantity);
    bool is_quantity_Set() const;
    bool is_quantity_Valid() const;

    QString getSelectedDeliveryChannel() const;
    void setSelectedDeliveryChannel(const QString &selected_delivery_channel);
    bool is_selected_delivery_channel_Set() const;
    bool is_selected_delivery_channel_Valid() const;

    QString getSelectedSla() const;
    void setSelectedSla(const QString &selected_sla);
    bool is_selected_sla_Set() const;
    bool is_selected_sla_Valid() const;

    QList<QJsonValue> getShipsTo() const;
    void setShipsTo(const QList<QJsonValue> &ships_to);
    bool is_ships_to_Set() const;
    bool is_ships_to_Valid() const;

    QList<OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner> getSlas() const;
    void setSlas(const QList<OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner> &slas);
    bool is_slas_Set() const;
    bool is_slas_Valid() const;

    OAIObject getSubscriptionData() const;
    void setSubscriptionData(const OAIObject &subscription_data);
    bool is_subscription_data_Set() const;
    bool is_subscription_data_Valid() const;

    QList<OAICartSimulation_200_response_logisticsInfo_inner_totals_inner> getTotals() const;
    void setTotals(const QList<OAICartSimulation_200_response_logisticsInfo_inner_totals_inner> &totals);
    bool is_totals_Set() const;
    bool is_totals_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_address_id;
    bool m_address_id_isSet;
    bool m_address_id_isValid;

    QList<OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_deliveryChannels_inner> m_delivery_channels;
    bool m_delivery_channels_isSet;
    bool m_delivery_channels_isValid;

    qint32 m_item_index;
    bool m_item_index_isSet;
    bool m_item_index_isValid;

    OAICartSimulation_200_response_logisticsInfo_inner_itemMetadata m_item_metadata;
    bool m_item_metadata_isSet;
    bool m_item_metadata_isValid;

    QList<QJsonValue> m_messages;
    bool m_messages_isSet;
    bool m_messages_isValid;

    QList<QJsonValue> m_pickup_points;
    bool m_pickup_points_isSet;
    bool m_pickup_points_isValid;

    OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions m_purchase_conditions;
    bool m_purchase_conditions_isSet;
    bool m_purchase_conditions_isValid;

    qint32 m_quantity;
    bool m_quantity_isSet;
    bool m_quantity_isValid;

    QString m_selected_delivery_channel;
    bool m_selected_delivery_channel_isSet;
    bool m_selected_delivery_channel_isValid;

    QString m_selected_sla;
    bool m_selected_sla_isSet;
    bool m_selected_sla_isValid;

    QList<QJsonValue> m_ships_to;
    bool m_ships_to_isSet;
    bool m_ships_to_isValid;

    QList<OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner> m_slas;
    bool m_slas_isSet;
    bool m_slas_isValid;

    OAIObject m_subscription_data;
    bool m_subscription_data_isSet;
    bool m_subscription_data_isValid;

    QList<OAICartSimulation_200_response_logisticsInfo_inner_totals_inner> m_totals;
    bool m_totals_isSet;
    bool m_totals_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICartSimulation_200_response_logisticsInfo_inner)

#endif // OAICartSimulation_200_response_logisticsInfo_inner_H
