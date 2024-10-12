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
 * OAIPlaceOrder_200_response_orders_inner.h
 *
 * 
 */

#ifndef OAIPlaceOrder_200_response_orders_inner_H
#define OAIPlaceOrder_200_response_orders_inner_H

#include <QJsonObject>

#include "OAIAddCoupons_200_response_clientProfileData.h"
#include "OAIAddCoupons_200_response_itemMetadata.h"
#include "OAIAddCoupons_200_response_paymentData.h"
#include "OAIAddCoupons_200_response_ratesAndBenefitsData.h"
#include "OAIAddCoupons_200_response_sellers_inner.h"
#include "OAIAddCoupons_200_response_shippingData.h"
#include "OAICartSimulation_200_response_logisticsInfo_inner_totals_inner.h"
#include "OAIPlaceOrder_200_response_orders_inner_items_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAddCoupons_200_response_clientProfileData;
class OAIAddCoupons_200_response_itemMetadata;
class OAIPlaceOrder_200_response_orders_inner_items_inner;
class OAIAddCoupons_200_response_paymentData;
class OAIAddCoupons_200_response_ratesAndBenefitsData;
class OAIAddCoupons_200_response_sellers_inner;
class OAIAddCoupons_200_response_shippingData;
class OAICartSimulation_200_response_logisticsInfo_inner_totals_inner;

class OAIPlaceOrder_200_response_orders_inner : public OAIObject {
public:
    OAIPlaceOrder_200_response_orders_inner();
    OAIPlaceOrder_200_response_orders_inner(QString json);
    ~OAIPlaceOrder_200_response_orders_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllowCancelation() const;
    void setAllowCancelation(const bool &allow_cancelation);
    bool is_allow_cancelation_Set() const;
    bool is_allow_cancelation_Valid() const;

    bool isAllowChangeSeller() const;
    void setAllowChangeSeller(const bool &allow_change_seller);
    bool is_allow_change_seller_Set() const;
    bool is_allow_change_seller_Valid() const;

    bool isAllowEdition() const;
    void setAllowEdition(const bool &allow_edition);
    bool is_allow_edition_Set() const;
    bool is_allow_edition_Valid() const;

    QString getCheckedInPickupPointId() const;
    void setCheckedInPickupPointId(const QString &checked_in_pickup_point_id);
    bool is_checked_in_pickup_point_id_Set() const;
    bool is_checked_in_pickup_point_id_Valid() const;

    OAIAddCoupons_200_response_clientProfileData getClientProfileData() const;
    void setClientProfileData(const OAIAddCoupons_200_response_clientProfileData &client_profile_data);
    bool is_client_profile_data_Set() const;
    bool is_client_profile_data_Valid() const;

    QString getCreationDate() const;
    void setCreationDate(const QString &creation_date);
    bool is_creation_date_Set() const;
    bool is_creation_date_Valid() const;

    QString getFollowUpEmail() const;
    void setFollowUpEmail(const QString &follow_up_email);
    bool is_follow_up_email_Set() const;
    bool is_follow_up_email_Valid() const;

    QString getHostName() const;
    void setHostName(const QString &host_name);
    bool is_host_name_Set() const;
    bool is_host_name_Valid() const;

    bool isIsCheckedIn() const;
    void setIsCheckedIn(const bool &is_checked_in);
    bool is_is_checked_in_Set() const;
    bool is_is_checked_in_Valid() const;

    bool isIsCompleted() const;
    void setIsCompleted(const bool &is_completed);
    bool is_is_completed_Set() const;
    bool is_is_completed_Valid() const;

    bool isIsUserDataVisible() const;
    void setIsUserDataVisible(const bool &is_user_data_visible);
    bool is_is_user_data_visible_Set() const;
    bool is_is_user_data_visible_Valid() const;

    OAIAddCoupons_200_response_itemMetadata getItemMetadata() const;
    void setItemMetadata(const OAIAddCoupons_200_response_itemMetadata &item_metadata);
    bool is_item_metadata_Set() const;
    bool is_item_metadata_Valid() const;

    QList<OAIPlaceOrder_200_response_orders_inner_items_inner> getItems() const;
    void setItems(const QList<OAIPlaceOrder_200_response_orders_inner_items_inner> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    QString getLastChange() const;
    void setLastChange(const QString &last_change);
    bool is_last_change_Set() const;
    bool is_last_change_Valid() const;

    QString getMerchantName() const;
    void setMerchantName(const QString &merchant_name);
    bool is_merchant_name_Set() const;
    bool is_merchant_name_Valid() const;

    QString getOrderFormCreationDate() const;
    void setOrderFormCreationDate(const QString &order_form_creation_date);
    bool is_order_form_creation_date_Set() const;
    bool is_order_form_creation_date_Valid() const;

    QString getOrderGroup() const;
    void setOrderGroup(const QString &order_group);
    bool is_order_group_Set() const;
    bool is_order_group_Valid() const;

    QString getOrderId() const;
    void setOrderId(const QString &order_id);
    bool is_order_id_Set() const;
    bool is_order_id_Valid() const;

    OAIAddCoupons_200_response_paymentData getPaymentData() const;
    void setPaymentData(const OAIAddCoupons_200_response_paymentData &payment_data);
    bool is_payment_data_Set() const;
    bool is_payment_data_Valid() const;

    OAIAddCoupons_200_response_ratesAndBenefitsData getRatesAndBenefitsData() const;
    void setRatesAndBenefitsData(const OAIAddCoupons_200_response_ratesAndBenefitsData &rates_and_benefits_data);
    bool is_rates_and_benefits_data_Set() const;
    bool is_rates_and_benefits_data_Valid() const;

    qint32 getRoundingError() const;
    void setRoundingError(const qint32 &rounding_error);
    bool is_rounding_error_Set() const;
    bool is_rounding_error_Valid() const;

    QString getSalesAssociateId() const;
    void setSalesAssociateId(const QString &sales_associate_id);
    bool is_sales_associate_id_Set() const;
    bool is_sales_associate_id_Valid() const;

    QString getSalesChannel() const;
    void setSalesChannel(const QString &sales_channel);
    bool is_sales_channel_Set() const;
    bool is_sales_channel_Valid() const;

    QString getSellerOrderId() const;
    void setSellerOrderId(const QString &seller_order_id);
    bool is_seller_order_id_Set() const;
    bool is_seller_order_id_Valid() const;

    QList<OAIAddCoupons_200_response_sellers_inner> getSellers() const;
    void setSellers(const QList<OAIAddCoupons_200_response_sellers_inner> &sellers);
    bool is_sellers_Set() const;
    bool is_sellers_Valid() const;

    OAIAddCoupons_200_response_shippingData getShippingData() const;
    void setShippingData(const OAIAddCoupons_200_response_shippingData &shipping_data);
    bool is_shipping_data_Set() const;
    bool is_shipping_data_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getStoreId() const;
    void setStoreId(const QString &store_id);
    bool is_store_id_Set() const;
    bool is_store_id_Valid() const;

    QString getTimeZoneCreationDate() const;
    void setTimeZoneCreationDate(const QString &time_zone_creation_date);
    bool is_time_zone_creation_date_Set() const;
    bool is_time_zone_creation_date_Valid() const;

    QString getTimeZoneLastChange() const;
    void setTimeZoneLastChange(const QString &time_zone_last_change);
    bool is_time_zone_last_change_Set() const;
    bool is_time_zone_last_change_Valid() const;

    QList<OAICartSimulation_200_response_logisticsInfo_inner_totals_inner> getTotals() const;
    void setTotals(const QList<OAICartSimulation_200_response_logisticsInfo_inner_totals_inner> &totals);
    bool is_totals_Set() const;
    bool is_totals_Valid() const;

    QString getUserType() const;
    void setUserType(const QString &user_type);
    bool is_user_type_Set() const;
    bool is_user_type_Valid() const;

    qint32 getValue() const;
    void setValue(const qint32 &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_allow_cancelation;
    bool m_allow_cancelation_isSet;
    bool m_allow_cancelation_isValid;

    bool m_allow_change_seller;
    bool m_allow_change_seller_isSet;
    bool m_allow_change_seller_isValid;

    bool m_allow_edition;
    bool m_allow_edition_isSet;
    bool m_allow_edition_isValid;

    QString m_checked_in_pickup_point_id;
    bool m_checked_in_pickup_point_id_isSet;
    bool m_checked_in_pickup_point_id_isValid;

    OAIAddCoupons_200_response_clientProfileData m_client_profile_data;
    bool m_client_profile_data_isSet;
    bool m_client_profile_data_isValid;

    QString m_creation_date;
    bool m_creation_date_isSet;
    bool m_creation_date_isValid;

    QString m_follow_up_email;
    bool m_follow_up_email_isSet;
    bool m_follow_up_email_isValid;

    QString m_host_name;
    bool m_host_name_isSet;
    bool m_host_name_isValid;

    bool m_is_checked_in;
    bool m_is_checked_in_isSet;
    bool m_is_checked_in_isValid;

    bool m_is_completed;
    bool m_is_completed_isSet;
    bool m_is_completed_isValid;

    bool m_is_user_data_visible;
    bool m_is_user_data_visible_isSet;
    bool m_is_user_data_visible_isValid;

    OAIAddCoupons_200_response_itemMetadata m_item_metadata;
    bool m_item_metadata_isSet;
    bool m_item_metadata_isValid;

    QList<OAIPlaceOrder_200_response_orders_inner_items_inner> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    QString m_last_change;
    bool m_last_change_isSet;
    bool m_last_change_isValid;

    QString m_merchant_name;
    bool m_merchant_name_isSet;
    bool m_merchant_name_isValid;

    QString m_order_form_creation_date;
    bool m_order_form_creation_date_isSet;
    bool m_order_form_creation_date_isValid;

    QString m_order_group;
    bool m_order_group_isSet;
    bool m_order_group_isValid;

    QString m_order_id;
    bool m_order_id_isSet;
    bool m_order_id_isValid;

    OAIAddCoupons_200_response_paymentData m_payment_data;
    bool m_payment_data_isSet;
    bool m_payment_data_isValid;

    OAIAddCoupons_200_response_ratesAndBenefitsData m_rates_and_benefits_data;
    bool m_rates_and_benefits_data_isSet;
    bool m_rates_and_benefits_data_isValid;

    qint32 m_rounding_error;
    bool m_rounding_error_isSet;
    bool m_rounding_error_isValid;

    QString m_sales_associate_id;
    bool m_sales_associate_id_isSet;
    bool m_sales_associate_id_isValid;

    QString m_sales_channel;
    bool m_sales_channel_isSet;
    bool m_sales_channel_isValid;

    QString m_seller_order_id;
    bool m_seller_order_id_isSet;
    bool m_seller_order_id_isValid;

    QList<OAIAddCoupons_200_response_sellers_inner> m_sellers;
    bool m_sellers_isSet;
    bool m_sellers_isValid;

    OAIAddCoupons_200_response_shippingData m_shipping_data;
    bool m_shipping_data_isSet;
    bool m_shipping_data_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_store_id;
    bool m_store_id_isSet;
    bool m_store_id_isValid;

    QString m_time_zone_creation_date;
    bool m_time_zone_creation_date_isSet;
    bool m_time_zone_creation_date_isValid;

    QString m_time_zone_last_change;
    bool m_time_zone_last_change_isSet;
    bool m_time_zone_last_change_isValid;

    QList<OAICartSimulation_200_response_logisticsInfo_inner_totals_inner> m_totals;
    bool m_totals_isSet;
    bool m_totals_isValid;

    QString m_user_type;
    bool m_user_type_isSet;
    bool m_user_type_isValid;

    qint32 m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlaceOrder_200_response_orders_inner)

#endif // OAIPlaceOrder_200_response_orders_inner_H
