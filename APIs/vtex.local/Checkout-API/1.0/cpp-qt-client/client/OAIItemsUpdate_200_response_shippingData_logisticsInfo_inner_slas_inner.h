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
 * OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner.h
 *
 * 
 */

#ifndef OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_H
#define OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_H

#include <QJsonObject>

#include "OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner.h"
#include "OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner;
class OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo;

class OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner : public OAIObject {
public:
    OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner();
    OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner(QString json);
    ~OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getDeliveryChannel() const;
    void setDeliveryChannel(const QString &delivery_channel);
    bool is_delivery_channel_Set() const;
    bool is_delivery_channel_Valid() const;

    QList<OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner> getDeliveryIds() const;
    void setDeliveryIds(const QList<OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner> &delivery_ids);
    bool is_delivery_ids_Set() const;
    bool is_delivery_ids_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    qint32 getListPrice() const;
    void setListPrice(const qint32 &list_price);
    bool is_list_price_Set() const;
    bool is_list_price_Valid() const;

    QString getLockTtl() const;
    void setLockTtl(const QString &lock_ttl);
    bool is_lock_ttl_Set() const;
    bool is_lock_ttl_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getPickupDistance() const;
    void setPickupDistance(const qint32 &pickup_distance);
    bool is_pickup_distance_Set() const;
    bool is_pickup_distance_Valid() const;

    QString getPickupPointId() const;
    void setPickupPointId(const QString &pickup_point_id);
    bool is_pickup_point_id_Set() const;
    bool is_pickup_point_id_Valid() const;

    OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo getPickupStoreInfo() const;
    void setPickupStoreInfo(const OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo &pickup_store_info);
    bool is_pickup_store_info_Set() const;
    bool is_pickup_store_info_Valid() const;

    QString getPolygonName() const;
    void setPolygonName(const QString &polygon_name);
    bool is_polygon_name_Set() const;
    bool is_polygon_name_Valid() const;

    qint32 getPrice() const;
    void setPrice(const qint32 &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QString getShippingEstimate() const;
    void setShippingEstimate(const QString &shipping_estimate);
    bool is_shipping_estimate_Set() const;
    bool is_shipping_estimate_Valid() const;

    QString getShippingEstimateDate() const;
    void setShippingEstimateDate(const QString &shipping_estimate_date);
    bool is_shipping_estimate_date_Set() const;
    bool is_shipping_estimate_date_Valid() const;

    qint32 getTax() const;
    void setTax(const qint32 &tax);
    bool is_tax_Set() const;
    bool is_tax_Valid() const;

    QString getTransitTime() const;
    void setTransitTime(const QString &transit_time);
    bool is_transit_time_Set() const;
    bool is_transit_time_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_delivery_channel;
    bool m_delivery_channel_isSet;
    bool m_delivery_channel_isValid;

    QList<OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner> m_delivery_ids;
    bool m_delivery_ids_isSet;
    bool m_delivery_ids_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    qint32 m_list_price;
    bool m_list_price_isSet;
    bool m_list_price_isValid;

    QString m_lock_ttl;
    bool m_lock_ttl_isSet;
    bool m_lock_ttl_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_pickup_distance;
    bool m_pickup_distance_isSet;
    bool m_pickup_distance_isValid;

    QString m_pickup_point_id;
    bool m_pickup_point_id_isSet;
    bool m_pickup_point_id_isValid;

    OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo m_pickup_store_info;
    bool m_pickup_store_info_isSet;
    bool m_pickup_store_info_isValid;

    QString m_polygon_name;
    bool m_polygon_name_isSet;
    bool m_polygon_name_isValid;

    qint32 m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QString m_shipping_estimate;
    bool m_shipping_estimate_isSet;
    bool m_shipping_estimate_isValid;

    QString m_shipping_estimate_date;
    bool m_shipping_estimate_date_isSet;
    bool m_shipping_estimate_date_isValid;

    qint32 m_tax;
    bool m_tax_isSet;
    bool m_tax_isValid;

    QString m_transit_time;
    bool m_transit_time_isSet;
    bool m_transit_time_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner)

#endif // OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_H
