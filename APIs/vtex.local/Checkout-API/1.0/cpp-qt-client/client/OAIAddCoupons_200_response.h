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
 * OAIAddCoupons_200_response.h
 *
 * 
 */

#ifndef OAIAddCoupons_200_response_H
#define OAIAddCoupons_200_response_H

#include <QJsonObject>

#include "OAIAddCoupons_200_response_availableAddresses_inner.h"
#include "OAIAddCoupons_200_response_clientPreferencesData.h"
#include "OAIAddCoupons_200_response_clientProfileData.h"
#include "OAIAddCoupons_200_response_itemMetadata.h"
#include "OAIAddCoupons_200_response_itemsOrdination.h"
#include "OAIAddCoupons_200_response_items_inner.h"
#include "OAIAddCoupons_200_response_marketingData.h"
#include "OAIAddCoupons_200_response_paymentData.h"
#include "OAIAddCoupons_200_response_ratesAndBenefitsData.h"
#include "OAIAddCoupons_200_response_sellers_inner.h"
#include "OAIAddCoupons_200_response_shippingData.h"
#include "OAIObject.h"
#include <QJsonValue>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAddCoupons_200_response_availableAddresses_inner;
class OAIAddCoupons_200_response_clientPreferencesData;
class OAIAddCoupons_200_response_clientProfileData;
class OAIAddCoupons_200_response_itemMetadata;
class OAIAddCoupons_200_response_items_inner;
class OAIAddCoupons_200_response_itemsOrdination;
class OAIAddCoupons_200_response_marketingData;
class OAIAddCoupons_200_response_paymentData;
class OAIAddCoupons_200_response_ratesAndBenefitsData;
class OAIAddCoupons_200_response_sellers_inner;
class OAIAddCoupons_200_response_shippingData;

class OAIAddCoupons_200_response : public OAIObject {
public:
    OAIAddCoupons_200_response();
    OAIAddCoupons_200_response(QString json);
    ~OAIAddCoupons_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAllowManualPrice() const;
    void setAllowManualPrice(const bool &allow_manual_price);
    bool is_allow_manual_price_Set() const;
    bool is_allow_manual_price_Valid() const;

    QList<QString> getAvailableAccounts() const;
    void setAvailableAccounts(const QList<QString> &available_accounts);
    bool is_available_accounts_Set() const;
    bool is_available_accounts_Valid() const;

    QList<OAIAddCoupons_200_response_availableAddresses_inner> getAvailableAddresses() const;
    void setAvailableAddresses(const QList<OAIAddCoupons_200_response_availableAddresses_inner> &available_addresses);
    bool is_available_addresses_Set() const;
    bool is_available_addresses_Valid() const;

    bool isCanEditData() const;
    void setCanEditData(const bool &can_edit_data);
    bool is_can_edit_data_Set() const;
    bool is_can_edit_data_Valid() const;

    OAIAddCoupons_200_response_clientPreferencesData getClientPreferencesData() const;
    void setClientPreferencesData(const OAIAddCoupons_200_response_clientPreferencesData &client_preferences_data);
    bool is_client_preferences_data_Set() const;
    bool is_client_preferences_data_Valid() const;

    OAIAddCoupons_200_response_clientProfileData getClientProfileData() const;
    void setClientProfileData(const OAIAddCoupons_200_response_clientProfileData &client_profile_data);
    bool is_client_profile_data_Set() const;
    bool is_client_profile_data_Valid() const;

    OAIObject getCommercialConditionData() const;
    void setCommercialConditionData(const OAIObject &commercial_condition_data);
    bool is_commercial_condition_data_Set() const;
    bool is_commercial_condition_data_Valid() const;

    OAIObject getCustomData() const;
    void setCustomData(const OAIObject &custom_data);
    bool is_custom_data_Set() const;
    bool is_custom_data_Valid() const;

    OAIObject getGiftRegistryData() const;
    void setGiftRegistryData(const OAIObject &gift_registry_data);
    bool is_gift_registry_data_Set() const;
    bool is_gift_registry_data_Valid() const;

    OAIObject getHooksData() const;
    void setHooksData(const OAIObject &hooks_data);
    bool is_hooks_data_Set() const;
    bool is_hooks_data_Valid() const;

    bool isIgnoreProfileData() const;
    void setIgnoreProfileData(const bool &ignore_profile_data);
    bool is_ignore_profile_data_Set() const;
    bool is_ignore_profile_data_Valid() const;

    OAIObject getInvoiceData() const;
    void setInvoiceData(const OAIObject &invoice_data);
    bool is_invoice_data_Set() const;
    bool is_invoice_data_Valid() const;

    bool isIsCheckedIn() const;
    void setIsCheckedIn(const bool &is_checked_in);
    bool is_is_checked_in_Set() const;
    bool is_is_checked_in_Valid() const;

    OAIAddCoupons_200_response_itemMetadata getItemMetadata() const;
    void setItemMetadata(const OAIAddCoupons_200_response_itemMetadata &item_metadata);
    bool is_item_metadata_Set() const;
    bool is_item_metadata_Valid() const;

    QList<OAIAddCoupons_200_response_items_inner> getItems() const;
    void setItems(const QList<OAIAddCoupons_200_response_items_inner> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    OAIAddCoupons_200_response_itemsOrdination getItemsOrdination() const;
    void setItemsOrdination(const OAIAddCoupons_200_response_itemsOrdination &items_ordination);
    bool is_items_ordination_Set() const;
    bool is_items_ordination_Valid() const;

    bool isLoggedIn() const;
    void setLoggedIn(const bool &logged_in);
    bool is_logged_in_Set() const;
    bool is_logged_in_Valid() const;

    OAIAddCoupons_200_response_marketingData getMarketingData() const;
    void setMarketingData(const OAIAddCoupons_200_response_marketingData &marketing_data);
    bool is_marketing_data_Set() const;
    bool is_marketing_data_Valid() const;

    QList<QJsonValue> getMessages() const;
    void setMessages(const QList<QJsonValue> &messages);
    bool is_messages_Set() const;
    bool is_messages_Valid() const;

    QString getOpenTextField() const;
    void setOpenTextField(const QString &open_text_field);
    bool is_open_text_field_Set() const;
    bool is_open_text_field_Valid() const;

    QString getOrderFormId() const;
    void setOrderFormId(const QString &order_form_id);
    bool is_order_form_id_Set() const;
    bool is_order_form_id_Valid() const;

    OAIAddCoupons_200_response_paymentData getPaymentData() const;
    void setPaymentData(const OAIAddCoupons_200_response_paymentData &payment_data);
    bool is_payment_data_Set() const;
    bool is_payment_data_Valid() const;

    QString getProfileProvider() const;
    void setProfileProvider(const QString &profile_provider);
    bool is_profile_provider_Set() const;
    bool is_profile_provider_Valid() const;

    OAIAddCoupons_200_response_ratesAndBenefitsData getRatesAndBenefitsData() const;
    void setRatesAndBenefitsData(const OAIAddCoupons_200_response_ratesAndBenefitsData &rates_and_benefits_data);
    bool is_rates_and_benefits_data_Set() const;
    bool is_rates_and_benefits_data_Valid() const;

    QString getSalesChannel() const;
    void setSalesChannel(const QString &sales_channel);
    bool is_sales_channel_Set() const;
    bool is_sales_channel_Valid() const;

    QList<QJsonValue> getSelectableGifts() const;
    void setSelectableGifts(const QList<QJsonValue> &selectable_gifts);
    bool is_selectable_gifts_Set() const;
    bool is_selectable_gifts_Valid() const;

    QList<OAIAddCoupons_200_response_sellers_inner> getSellers() const;
    void setSellers(const QList<OAIAddCoupons_200_response_sellers_inner> &sellers);
    bool is_sellers_Set() const;
    bool is_sellers_Valid() const;

    OAIAddCoupons_200_response_shippingData getShippingData() const;
    void setShippingData(const OAIAddCoupons_200_response_shippingData &shipping_data);
    bool is_shipping_data_Set() const;
    bool is_shipping_data_Valid() const;

    QString getStoreId() const;
    void setStoreId(const QString &store_id);
    bool is_store_id_Set() const;
    bool is_store_id_Valid() const;

    OAIObject getStorePreferencesData() const;
    void setStorePreferencesData(const OAIObject &store_preferences_data);
    bool is_store_preferences_data_Set() const;
    bool is_store_preferences_data_Valid() const;

    OAIObject getSubscriptionData() const;
    void setSubscriptionData(const OAIObject &subscription_data);
    bool is_subscription_data_Set() const;
    bool is_subscription_data_Valid() const;

    QList<QJsonValue> getTotalizers() const;
    void setTotalizers(const QList<QJsonValue> &totalizers);
    bool is_totalizers_Set() const;
    bool is_totalizers_Valid() const;

    QString getUserProfileId() const;
    void setUserProfileId(const QString &user_profile_id);
    bool is_user_profile_id_Set() const;
    bool is_user_profile_id_Valid() const;

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

    bool m_allow_manual_price;
    bool m_allow_manual_price_isSet;
    bool m_allow_manual_price_isValid;

    QList<QString> m_available_accounts;
    bool m_available_accounts_isSet;
    bool m_available_accounts_isValid;

    QList<OAIAddCoupons_200_response_availableAddresses_inner> m_available_addresses;
    bool m_available_addresses_isSet;
    bool m_available_addresses_isValid;

    bool m_can_edit_data;
    bool m_can_edit_data_isSet;
    bool m_can_edit_data_isValid;

    OAIAddCoupons_200_response_clientPreferencesData m_client_preferences_data;
    bool m_client_preferences_data_isSet;
    bool m_client_preferences_data_isValid;

    OAIAddCoupons_200_response_clientProfileData m_client_profile_data;
    bool m_client_profile_data_isSet;
    bool m_client_profile_data_isValid;

    OAIObject m_commercial_condition_data;
    bool m_commercial_condition_data_isSet;
    bool m_commercial_condition_data_isValid;

    OAIObject m_custom_data;
    bool m_custom_data_isSet;
    bool m_custom_data_isValid;

    OAIObject m_gift_registry_data;
    bool m_gift_registry_data_isSet;
    bool m_gift_registry_data_isValid;

    OAIObject m_hooks_data;
    bool m_hooks_data_isSet;
    bool m_hooks_data_isValid;

    bool m_ignore_profile_data;
    bool m_ignore_profile_data_isSet;
    bool m_ignore_profile_data_isValid;

    OAIObject m_invoice_data;
    bool m_invoice_data_isSet;
    bool m_invoice_data_isValid;

    bool m_is_checked_in;
    bool m_is_checked_in_isSet;
    bool m_is_checked_in_isValid;

    OAIAddCoupons_200_response_itemMetadata m_item_metadata;
    bool m_item_metadata_isSet;
    bool m_item_metadata_isValid;

    QList<OAIAddCoupons_200_response_items_inner> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    OAIAddCoupons_200_response_itemsOrdination m_items_ordination;
    bool m_items_ordination_isSet;
    bool m_items_ordination_isValid;

    bool m_logged_in;
    bool m_logged_in_isSet;
    bool m_logged_in_isValid;

    OAIAddCoupons_200_response_marketingData m_marketing_data;
    bool m_marketing_data_isSet;
    bool m_marketing_data_isValid;

    QList<QJsonValue> m_messages;
    bool m_messages_isSet;
    bool m_messages_isValid;

    QString m_open_text_field;
    bool m_open_text_field_isSet;
    bool m_open_text_field_isValid;

    QString m_order_form_id;
    bool m_order_form_id_isSet;
    bool m_order_form_id_isValid;

    OAIAddCoupons_200_response_paymentData m_payment_data;
    bool m_payment_data_isSet;
    bool m_payment_data_isValid;

    QString m_profile_provider;
    bool m_profile_provider_isSet;
    bool m_profile_provider_isValid;

    OAIAddCoupons_200_response_ratesAndBenefitsData m_rates_and_benefits_data;
    bool m_rates_and_benefits_data_isSet;
    bool m_rates_and_benefits_data_isValid;

    QString m_sales_channel;
    bool m_sales_channel_isSet;
    bool m_sales_channel_isValid;

    QList<QJsonValue> m_selectable_gifts;
    bool m_selectable_gifts_isSet;
    bool m_selectable_gifts_isValid;

    QList<OAIAddCoupons_200_response_sellers_inner> m_sellers;
    bool m_sellers_isSet;
    bool m_sellers_isValid;

    OAIAddCoupons_200_response_shippingData m_shipping_data;
    bool m_shipping_data_isSet;
    bool m_shipping_data_isValid;

    QString m_store_id;
    bool m_store_id_isSet;
    bool m_store_id_isValid;

    OAIObject m_store_preferences_data;
    bool m_store_preferences_data_isSet;
    bool m_store_preferences_data_isValid;

    OAIObject m_subscription_data;
    bool m_subscription_data_isSet;
    bool m_subscription_data_isValid;

    QList<QJsonValue> m_totalizers;
    bool m_totalizers_isSet;
    bool m_totalizers_isValid;

    QString m_user_profile_id;
    bool m_user_profile_id_isSet;
    bool m_user_profile_id_isValid;

    QString m_user_type;
    bool m_user_type_isSet;
    bool m_user_type_isValid;

    qint32 m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAddCoupons_200_response)

#endif // OAIAddCoupons_200_response_H
