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

#include "OAIClearorderFormMessages_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIClearorderFormMessages_200_response::OAIClearorderFormMessages_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIClearorderFormMessages_200_response::OAIClearorderFormMessages_200_response() {
    this->initializeModel();
}

OAIClearorderFormMessages_200_response::~OAIClearorderFormMessages_200_response() {}

void OAIClearorderFormMessages_200_response::initializeModel() {

    m_allow_manual_price_isSet = false;
    m_allow_manual_price_isValid = false;

    m_available_accounts_isSet = false;
    m_available_accounts_isValid = false;

    m_available_addresses_isSet = false;
    m_available_addresses_isValid = false;

    m_can_edit_data_isSet = false;
    m_can_edit_data_isValid = false;

    m_client_preferences_data_isSet = false;
    m_client_preferences_data_isValid = false;

    m_client_profile_data_isSet = false;
    m_client_profile_data_isValid = false;

    m_commercial_condition_data_isSet = false;
    m_commercial_condition_data_isValid = false;

    m_custom_data_isSet = false;
    m_custom_data_isValid = false;

    m_gift_registry_data_isSet = false;
    m_gift_registry_data_isValid = false;

    m_hooks_data_isSet = false;
    m_hooks_data_isValid = false;

    m_ignore_profile_data_isSet = false;
    m_ignore_profile_data_isValid = false;

    m_invoice_data_isSet = false;
    m_invoice_data_isValid = false;

    m_is_checked_in_isSet = false;
    m_is_checked_in_isValid = false;

    m_item_metadata_isSet = false;
    m_item_metadata_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;

    m_items_ordination_isSet = false;
    m_items_ordination_isValid = false;

    m_logged_in_isSet = false;
    m_logged_in_isValid = false;

    m_marketing_data_isSet = false;
    m_marketing_data_isValid = false;

    m_messages_isSet = false;
    m_messages_isValid = false;

    m_open_text_field_isSet = false;
    m_open_text_field_isValid = false;

    m_order_form_id_isSet = false;
    m_order_form_id_isValid = false;

    m_payment_data_isSet = false;
    m_payment_data_isValid = false;

    m_profile_provider_isSet = false;
    m_profile_provider_isValid = false;

    m_rates_and_benefits_data_isSet = false;
    m_rates_and_benefits_data_isValid = false;

    m_sales_channel_isSet = false;
    m_sales_channel_isValid = false;

    m_selectable_gifts_isSet = false;
    m_selectable_gifts_isValid = false;

    m_sellers_isSet = false;
    m_sellers_isValid = false;

    m_shipping_data_isSet = false;
    m_shipping_data_isValid = false;

    m_store_id_isSet = false;
    m_store_id_isValid = false;

    m_store_preferences_data_isSet = false;
    m_store_preferences_data_isValid = false;

    m_subscription_data_isSet = false;
    m_subscription_data_isValid = false;

    m_totalizers_isSet = false;
    m_totalizers_isValid = false;

    m_user_profile_id_isSet = false;
    m_user_profile_id_isValid = false;

    m_user_type_isSet = false;
    m_user_type_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIClearorderFormMessages_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIClearorderFormMessages_200_response::fromJsonObject(QJsonObject json) {

    m_allow_manual_price_isValid = ::OpenAPI::fromJsonValue(m_allow_manual_price, json[QString("allowManualPrice")]);
    m_allow_manual_price_isSet = !json[QString("allowManualPrice")].isNull() && m_allow_manual_price_isValid;

    m_available_accounts_isValid = ::OpenAPI::fromJsonValue(m_available_accounts, json[QString("availableAccounts")]);
    m_available_accounts_isSet = !json[QString("availableAccounts")].isNull() && m_available_accounts_isValid;

    m_available_addresses_isValid = ::OpenAPI::fromJsonValue(m_available_addresses, json[QString("availableAddresses")]);
    m_available_addresses_isSet = !json[QString("availableAddresses")].isNull() && m_available_addresses_isValid;

    m_can_edit_data_isValid = ::OpenAPI::fromJsonValue(m_can_edit_data, json[QString("canEditData")]);
    m_can_edit_data_isSet = !json[QString("canEditData")].isNull() && m_can_edit_data_isValid;

    m_client_preferences_data_isValid = ::OpenAPI::fromJsonValue(m_client_preferences_data, json[QString("clientPreferencesData")]);
    m_client_preferences_data_isSet = !json[QString("clientPreferencesData")].isNull() && m_client_preferences_data_isValid;

    m_client_profile_data_isValid = ::OpenAPI::fromJsonValue(m_client_profile_data, json[QString("clientProfileData")]);
    m_client_profile_data_isSet = !json[QString("clientProfileData")].isNull() && m_client_profile_data_isValid;

    m_commercial_condition_data_isValid = ::OpenAPI::fromJsonValue(m_commercial_condition_data, json[QString("commercialConditionData")]);
    m_commercial_condition_data_isSet = !json[QString("commercialConditionData")].isNull() && m_commercial_condition_data_isValid;

    m_custom_data_isValid = ::OpenAPI::fromJsonValue(m_custom_data, json[QString("customData")]);
    m_custom_data_isSet = !json[QString("customData")].isNull() && m_custom_data_isValid;

    m_gift_registry_data_isValid = ::OpenAPI::fromJsonValue(m_gift_registry_data, json[QString("giftRegistryData")]);
    m_gift_registry_data_isSet = !json[QString("giftRegistryData")].isNull() && m_gift_registry_data_isValid;

    m_hooks_data_isValid = ::OpenAPI::fromJsonValue(m_hooks_data, json[QString("hooksData")]);
    m_hooks_data_isSet = !json[QString("hooksData")].isNull() && m_hooks_data_isValid;

    m_ignore_profile_data_isValid = ::OpenAPI::fromJsonValue(m_ignore_profile_data, json[QString("ignoreProfileData")]);
    m_ignore_profile_data_isSet = !json[QString("ignoreProfileData")].isNull() && m_ignore_profile_data_isValid;

    m_invoice_data_isValid = ::OpenAPI::fromJsonValue(m_invoice_data, json[QString("invoiceData")]);
    m_invoice_data_isSet = !json[QString("invoiceData")].isNull() && m_invoice_data_isValid;

    m_is_checked_in_isValid = ::OpenAPI::fromJsonValue(m_is_checked_in, json[QString("isCheckedIn")]);
    m_is_checked_in_isSet = !json[QString("isCheckedIn")].isNull() && m_is_checked_in_isValid;

    m_item_metadata_isValid = ::OpenAPI::fromJsonValue(m_item_metadata, json[QString("itemMetadata")]);
    m_item_metadata_isSet = !json[QString("itemMetadata")].isNull() && m_item_metadata_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_items_ordination_isValid = ::OpenAPI::fromJsonValue(m_items_ordination, json[QString("itemsOrdination")]);
    m_items_ordination_isSet = !json[QString("itemsOrdination")].isNull() && m_items_ordination_isValid;

    m_logged_in_isValid = ::OpenAPI::fromJsonValue(m_logged_in, json[QString("loggedIn")]);
    m_logged_in_isSet = !json[QString("loggedIn")].isNull() && m_logged_in_isValid;

    m_marketing_data_isValid = ::OpenAPI::fromJsonValue(m_marketing_data, json[QString("marketingData")]);
    m_marketing_data_isSet = !json[QString("marketingData")].isNull() && m_marketing_data_isValid;

    m_messages_isValid = ::OpenAPI::fromJsonValue(m_messages, json[QString("messages")]);
    m_messages_isSet = !json[QString("messages")].isNull() && m_messages_isValid;

    m_open_text_field_isValid = ::OpenAPI::fromJsonValue(m_open_text_field, json[QString("openTextField")]);
    m_open_text_field_isSet = !json[QString("openTextField")].isNull() && m_open_text_field_isValid;

    m_order_form_id_isValid = ::OpenAPI::fromJsonValue(m_order_form_id, json[QString("orderFormId")]);
    m_order_form_id_isSet = !json[QString("orderFormId")].isNull() && m_order_form_id_isValid;

    m_payment_data_isValid = ::OpenAPI::fromJsonValue(m_payment_data, json[QString("paymentData")]);
    m_payment_data_isSet = !json[QString("paymentData")].isNull() && m_payment_data_isValid;

    m_profile_provider_isValid = ::OpenAPI::fromJsonValue(m_profile_provider, json[QString("profileProvider")]);
    m_profile_provider_isSet = !json[QString("profileProvider")].isNull() && m_profile_provider_isValid;

    m_rates_and_benefits_data_isValid = ::OpenAPI::fromJsonValue(m_rates_and_benefits_data, json[QString("ratesAndBenefitsData")]);
    m_rates_and_benefits_data_isSet = !json[QString("ratesAndBenefitsData")].isNull() && m_rates_and_benefits_data_isValid;

    m_sales_channel_isValid = ::OpenAPI::fromJsonValue(m_sales_channel, json[QString("salesChannel")]);
    m_sales_channel_isSet = !json[QString("salesChannel")].isNull() && m_sales_channel_isValid;

    m_selectable_gifts_isValid = ::OpenAPI::fromJsonValue(m_selectable_gifts, json[QString("selectableGifts")]);
    m_selectable_gifts_isSet = !json[QString("selectableGifts")].isNull() && m_selectable_gifts_isValid;

    m_sellers_isValid = ::OpenAPI::fromJsonValue(m_sellers, json[QString("sellers")]);
    m_sellers_isSet = !json[QString("sellers")].isNull() && m_sellers_isValid;

    m_shipping_data_isValid = ::OpenAPI::fromJsonValue(m_shipping_data, json[QString("shippingData")]);
    m_shipping_data_isSet = !json[QString("shippingData")].isNull() && m_shipping_data_isValid;

    m_store_id_isValid = ::OpenAPI::fromJsonValue(m_store_id, json[QString("storeId")]);
    m_store_id_isSet = !json[QString("storeId")].isNull() && m_store_id_isValid;

    m_store_preferences_data_isValid = ::OpenAPI::fromJsonValue(m_store_preferences_data, json[QString("storePreferencesData")]);
    m_store_preferences_data_isSet = !json[QString("storePreferencesData")].isNull() && m_store_preferences_data_isValid;

    m_subscription_data_isValid = ::OpenAPI::fromJsonValue(m_subscription_data, json[QString("subscriptionData")]);
    m_subscription_data_isSet = !json[QString("subscriptionData")].isNull() && m_subscription_data_isValid;

    m_totalizers_isValid = ::OpenAPI::fromJsonValue(m_totalizers, json[QString("totalizers")]);
    m_totalizers_isSet = !json[QString("totalizers")].isNull() && m_totalizers_isValid;

    m_user_profile_id_isValid = ::OpenAPI::fromJsonValue(m_user_profile_id, json[QString("userProfileId")]);
    m_user_profile_id_isSet = !json[QString("userProfileId")].isNull() && m_user_profile_id_isValid;

    m_user_type_isValid = ::OpenAPI::fromJsonValue(m_user_type, json[QString("userType")]);
    m_user_type_isSet = !json[QString("userType")].isNull() && m_user_type_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIClearorderFormMessages_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIClearorderFormMessages_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_allow_manual_price_isSet) {
        obj.insert(QString("allowManualPrice"), ::OpenAPI::toJsonValue(m_allow_manual_price));
    }
    if (m_available_accounts.size() > 0) {
        obj.insert(QString("availableAccounts"), ::OpenAPI::toJsonValue(m_available_accounts));
    }
    if (m_available_addresses.size() > 0) {
        obj.insert(QString("availableAddresses"), ::OpenAPI::toJsonValue(m_available_addresses));
    }
    if (m_can_edit_data_isSet) {
        obj.insert(QString("canEditData"), ::OpenAPI::toJsonValue(m_can_edit_data));
    }
    if (m_client_preferences_data.isSet()) {
        obj.insert(QString("clientPreferencesData"), ::OpenAPI::toJsonValue(m_client_preferences_data));
    }
    if (m_client_profile_data.isSet()) {
        obj.insert(QString("clientProfileData"), ::OpenAPI::toJsonValue(m_client_profile_data));
    }
    if (m_commercial_condition_data_isSet) {
        obj.insert(QString("commercialConditionData"), ::OpenAPI::toJsonValue(m_commercial_condition_data));
    }
    if (m_custom_data_isSet) {
        obj.insert(QString("customData"), ::OpenAPI::toJsonValue(m_custom_data));
    }
    if (m_gift_registry_data_isSet) {
        obj.insert(QString("giftRegistryData"), ::OpenAPI::toJsonValue(m_gift_registry_data));
    }
    if (m_hooks_data_isSet) {
        obj.insert(QString("hooksData"), ::OpenAPI::toJsonValue(m_hooks_data));
    }
    if (m_ignore_profile_data_isSet) {
        obj.insert(QString("ignoreProfileData"), ::OpenAPI::toJsonValue(m_ignore_profile_data));
    }
    if (m_invoice_data_isSet) {
        obj.insert(QString("invoiceData"), ::OpenAPI::toJsonValue(m_invoice_data));
    }
    if (m_is_checked_in_isSet) {
        obj.insert(QString("isCheckedIn"), ::OpenAPI::toJsonValue(m_is_checked_in));
    }
    if (m_item_metadata.isSet()) {
        obj.insert(QString("itemMetadata"), ::OpenAPI::toJsonValue(m_item_metadata));
    }
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_items_ordination.isSet()) {
        obj.insert(QString("itemsOrdination"), ::OpenAPI::toJsonValue(m_items_ordination));
    }
    if (m_logged_in_isSet) {
        obj.insert(QString("loggedIn"), ::OpenAPI::toJsonValue(m_logged_in));
    }
    if (m_marketing_data.isSet()) {
        obj.insert(QString("marketingData"), ::OpenAPI::toJsonValue(m_marketing_data));
    }
    if (m_messages.size() > 0) {
        obj.insert(QString("messages"), ::OpenAPI::toJsonValue(m_messages));
    }
    if (m_open_text_field_isSet) {
        obj.insert(QString("openTextField"), ::OpenAPI::toJsonValue(m_open_text_field));
    }
    if (m_order_form_id_isSet) {
        obj.insert(QString("orderFormId"), ::OpenAPI::toJsonValue(m_order_form_id));
    }
    if (m_payment_data.isSet()) {
        obj.insert(QString("paymentData"), ::OpenAPI::toJsonValue(m_payment_data));
    }
    if (m_profile_provider_isSet) {
        obj.insert(QString("profileProvider"), ::OpenAPI::toJsonValue(m_profile_provider));
    }
    if (m_rates_and_benefits_data.isSet()) {
        obj.insert(QString("ratesAndBenefitsData"), ::OpenAPI::toJsonValue(m_rates_and_benefits_data));
    }
    if (m_sales_channel_isSet) {
        obj.insert(QString("salesChannel"), ::OpenAPI::toJsonValue(m_sales_channel));
    }
    if (m_selectable_gifts.size() > 0) {
        obj.insert(QString("selectableGifts"), ::OpenAPI::toJsonValue(m_selectable_gifts));
    }
    if (m_sellers.size() > 0) {
        obj.insert(QString("sellers"), ::OpenAPI::toJsonValue(m_sellers));
    }
    if (m_shipping_data.isSet()) {
        obj.insert(QString("shippingData"), ::OpenAPI::toJsonValue(m_shipping_data));
    }
    if (m_store_id_isSet) {
        obj.insert(QString("storeId"), ::OpenAPI::toJsonValue(m_store_id));
    }
    if (m_store_preferences_data_isSet) {
        obj.insert(QString("storePreferencesData"), ::OpenAPI::toJsonValue(m_store_preferences_data));
    }
    if (m_subscription_data_isSet) {
        obj.insert(QString("subscriptionData"), ::OpenAPI::toJsonValue(m_subscription_data));
    }
    if (m_totalizers.size() > 0) {
        obj.insert(QString("totalizers"), ::OpenAPI::toJsonValue(m_totalizers));
    }
    if (m_user_profile_id_isSet) {
        obj.insert(QString("userProfileId"), ::OpenAPI::toJsonValue(m_user_profile_id));
    }
    if (m_user_type_isSet) {
        obj.insert(QString("userType"), ::OpenAPI::toJsonValue(m_user_type));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

bool OAIClearorderFormMessages_200_response::isAllowManualPrice() const {
    return m_allow_manual_price;
}
void OAIClearorderFormMessages_200_response::setAllowManualPrice(const bool &allow_manual_price) {
    m_allow_manual_price = allow_manual_price;
    m_allow_manual_price_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_allow_manual_price_Set() const{
    return m_allow_manual_price_isSet;
}

bool OAIClearorderFormMessages_200_response::is_allow_manual_price_Valid() const{
    return m_allow_manual_price_isValid;
}

QList<QString> OAIClearorderFormMessages_200_response::getAvailableAccounts() const {
    return m_available_accounts;
}
void OAIClearorderFormMessages_200_response::setAvailableAccounts(const QList<QString> &available_accounts) {
    m_available_accounts = available_accounts;
    m_available_accounts_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_available_accounts_Set() const{
    return m_available_accounts_isSet;
}

bool OAIClearorderFormMessages_200_response::is_available_accounts_Valid() const{
    return m_available_accounts_isValid;
}

QList<OAIAddCoupons_200_response_availableAddresses_inner> OAIClearorderFormMessages_200_response::getAvailableAddresses() const {
    return m_available_addresses;
}
void OAIClearorderFormMessages_200_response::setAvailableAddresses(const QList<OAIAddCoupons_200_response_availableAddresses_inner> &available_addresses) {
    m_available_addresses = available_addresses;
    m_available_addresses_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_available_addresses_Set() const{
    return m_available_addresses_isSet;
}

bool OAIClearorderFormMessages_200_response::is_available_addresses_Valid() const{
    return m_available_addresses_isValid;
}

bool OAIClearorderFormMessages_200_response::isCanEditData() const {
    return m_can_edit_data;
}
void OAIClearorderFormMessages_200_response::setCanEditData(const bool &can_edit_data) {
    m_can_edit_data = can_edit_data;
    m_can_edit_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_can_edit_data_Set() const{
    return m_can_edit_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_can_edit_data_Valid() const{
    return m_can_edit_data_isValid;
}

OAIItems_200_response_clientPreferencesData OAIClearorderFormMessages_200_response::getClientPreferencesData() const {
    return m_client_preferences_data;
}
void OAIClearorderFormMessages_200_response::setClientPreferencesData(const OAIItems_200_response_clientPreferencesData &client_preferences_data) {
    m_client_preferences_data = client_preferences_data;
    m_client_preferences_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_client_preferences_data_Set() const{
    return m_client_preferences_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_client_preferences_data_Valid() const{
    return m_client_preferences_data_isValid;
}

OAIAddCoupons_200_response_clientProfileData OAIClearorderFormMessages_200_response::getClientProfileData() const {
    return m_client_profile_data;
}
void OAIClearorderFormMessages_200_response::setClientProfileData(const OAIAddCoupons_200_response_clientProfileData &client_profile_data) {
    m_client_profile_data = client_profile_data;
    m_client_profile_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_client_profile_data_Set() const{
    return m_client_profile_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_client_profile_data_Valid() const{
    return m_client_profile_data_isValid;
}

OAIObject OAIClearorderFormMessages_200_response::getCommercialConditionData() const {
    return m_commercial_condition_data;
}
void OAIClearorderFormMessages_200_response::setCommercialConditionData(const OAIObject &commercial_condition_data) {
    m_commercial_condition_data = commercial_condition_data;
    m_commercial_condition_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_commercial_condition_data_Set() const{
    return m_commercial_condition_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_commercial_condition_data_Valid() const{
    return m_commercial_condition_data_isValid;
}

OAIObject OAIClearorderFormMessages_200_response::getCustomData() const {
    return m_custom_data;
}
void OAIClearorderFormMessages_200_response::setCustomData(const OAIObject &custom_data) {
    m_custom_data = custom_data;
    m_custom_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_custom_data_Set() const{
    return m_custom_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_custom_data_Valid() const{
    return m_custom_data_isValid;
}

OAIObject OAIClearorderFormMessages_200_response::getGiftRegistryData() const {
    return m_gift_registry_data;
}
void OAIClearorderFormMessages_200_response::setGiftRegistryData(const OAIObject &gift_registry_data) {
    m_gift_registry_data = gift_registry_data;
    m_gift_registry_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_gift_registry_data_Set() const{
    return m_gift_registry_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_gift_registry_data_Valid() const{
    return m_gift_registry_data_isValid;
}

OAIObject OAIClearorderFormMessages_200_response::getHooksData() const {
    return m_hooks_data;
}
void OAIClearorderFormMessages_200_response::setHooksData(const OAIObject &hooks_data) {
    m_hooks_data = hooks_data;
    m_hooks_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_hooks_data_Set() const{
    return m_hooks_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_hooks_data_Valid() const{
    return m_hooks_data_isValid;
}

bool OAIClearorderFormMessages_200_response::isIgnoreProfileData() const {
    return m_ignore_profile_data;
}
void OAIClearorderFormMessages_200_response::setIgnoreProfileData(const bool &ignore_profile_data) {
    m_ignore_profile_data = ignore_profile_data;
    m_ignore_profile_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_ignore_profile_data_Set() const{
    return m_ignore_profile_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_ignore_profile_data_Valid() const{
    return m_ignore_profile_data_isValid;
}

OAIObject OAIClearorderFormMessages_200_response::getInvoiceData() const {
    return m_invoice_data;
}
void OAIClearorderFormMessages_200_response::setInvoiceData(const OAIObject &invoice_data) {
    m_invoice_data = invoice_data;
    m_invoice_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_invoice_data_Set() const{
    return m_invoice_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_invoice_data_Valid() const{
    return m_invoice_data_isValid;
}

bool OAIClearorderFormMessages_200_response::isIsCheckedIn() const {
    return m_is_checked_in;
}
void OAIClearorderFormMessages_200_response::setIsCheckedIn(const bool &is_checked_in) {
    m_is_checked_in = is_checked_in;
    m_is_checked_in_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_is_checked_in_Set() const{
    return m_is_checked_in_isSet;
}

bool OAIClearorderFormMessages_200_response::is_is_checked_in_Valid() const{
    return m_is_checked_in_isValid;
}

OAIAddCoupons_200_response_itemMetadata OAIClearorderFormMessages_200_response::getItemMetadata() const {
    return m_item_metadata;
}
void OAIClearorderFormMessages_200_response::setItemMetadata(const OAIAddCoupons_200_response_itemMetadata &item_metadata) {
    m_item_metadata = item_metadata;
    m_item_metadata_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_item_metadata_Set() const{
    return m_item_metadata_isSet;
}

bool OAIClearorderFormMessages_200_response::is_item_metadata_Valid() const{
    return m_item_metadata_isValid;
}

QList<OAIItems_200_response_items_inner> OAIClearorderFormMessages_200_response::getItems() const {
    return m_items;
}
void OAIClearorderFormMessages_200_response::setItems(const QList<OAIItems_200_response_items_inner> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_items_Set() const{
    return m_items_isSet;
}

bool OAIClearorderFormMessages_200_response::is_items_Valid() const{
    return m_items_isValid;
}

OAIAddCoupons_200_response_itemsOrdination OAIClearorderFormMessages_200_response::getItemsOrdination() const {
    return m_items_ordination;
}
void OAIClearorderFormMessages_200_response::setItemsOrdination(const OAIAddCoupons_200_response_itemsOrdination &items_ordination) {
    m_items_ordination = items_ordination;
    m_items_ordination_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_items_ordination_Set() const{
    return m_items_ordination_isSet;
}

bool OAIClearorderFormMessages_200_response::is_items_ordination_Valid() const{
    return m_items_ordination_isValid;
}

bool OAIClearorderFormMessages_200_response::isLoggedIn() const {
    return m_logged_in;
}
void OAIClearorderFormMessages_200_response::setLoggedIn(const bool &logged_in) {
    m_logged_in = logged_in;
    m_logged_in_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_logged_in_Set() const{
    return m_logged_in_isSet;
}

bool OAIClearorderFormMessages_200_response::is_logged_in_Valid() const{
    return m_logged_in_isValid;
}

OAIClearorderFormMessages_200_response_marketingData OAIClearorderFormMessages_200_response::getMarketingData() const {
    return m_marketing_data;
}
void OAIClearorderFormMessages_200_response::setMarketingData(const OAIClearorderFormMessages_200_response_marketingData &marketing_data) {
    m_marketing_data = marketing_data;
    m_marketing_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_marketing_data_Set() const{
    return m_marketing_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_marketing_data_Valid() const{
    return m_marketing_data_isValid;
}

QList<QJsonValue> OAIClearorderFormMessages_200_response::getMessages() const {
    return m_messages;
}
void OAIClearorderFormMessages_200_response::setMessages(const QList<QJsonValue> &messages) {
    m_messages = messages;
    m_messages_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_messages_Set() const{
    return m_messages_isSet;
}

bool OAIClearorderFormMessages_200_response::is_messages_Valid() const{
    return m_messages_isValid;
}

QString OAIClearorderFormMessages_200_response::getOpenTextField() const {
    return m_open_text_field;
}
void OAIClearorderFormMessages_200_response::setOpenTextField(const QString &open_text_field) {
    m_open_text_field = open_text_field;
    m_open_text_field_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_open_text_field_Set() const{
    return m_open_text_field_isSet;
}

bool OAIClearorderFormMessages_200_response::is_open_text_field_Valid() const{
    return m_open_text_field_isValid;
}

QString OAIClearorderFormMessages_200_response::getOrderFormId() const {
    return m_order_form_id;
}
void OAIClearorderFormMessages_200_response::setOrderFormId(const QString &order_form_id) {
    m_order_form_id = order_form_id;
    m_order_form_id_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_order_form_id_Set() const{
    return m_order_form_id_isSet;
}

bool OAIClearorderFormMessages_200_response::is_order_form_id_Valid() const{
    return m_order_form_id_isValid;
}

OAIAddCoupons_200_response_paymentData OAIClearorderFormMessages_200_response::getPaymentData() const {
    return m_payment_data;
}
void OAIClearorderFormMessages_200_response::setPaymentData(const OAIAddCoupons_200_response_paymentData &payment_data) {
    m_payment_data = payment_data;
    m_payment_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_payment_data_Set() const{
    return m_payment_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_payment_data_Valid() const{
    return m_payment_data_isValid;
}

QString OAIClearorderFormMessages_200_response::getProfileProvider() const {
    return m_profile_provider;
}
void OAIClearorderFormMessages_200_response::setProfileProvider(const QString &profile_provider) {
    m_profile_provider = profile_provider;
    m_profile_provider_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_profile_provider_Set() const{
    return m_profile_provider_isSet;
}

bool OAIClearorderFormMessages_200_response::is_profile_provider_Valid() const{
    return m_profile_provider_isValid;
}

OAIAddCoupons_200_response_ratesAndBenefitsData OAIClearorderFormMessages_200_response::getRatesAndBenefitsData() const {
    return m_rates_and_benefits_data;
}
void OAIClearorderFormMessages_200_response::setRatesAndBenefitsData(const OAIAddCoupons_200_response_ratesAndBenefitsData &rates_and_benefits_data) {
    m_rates_and_benefits_data = rates_and_benefits_data;
    m_rates_and_benefits_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_rates_and_benefits_data_Set() const{
    return m_rates_and_benefits_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_rates_and_benefits_data_Valid() const{
    return m_rates_and_benefits_data_isValid;
}

QString OAIClearorderFormMessages_200_response::getSalesChannel() const {
    return m_sales_channel;
}
void OAIClearorderFormMessages_200_response::setSalesChannel(const QString &sales_channel) {
    m_sales_channel = sales_channel;
    m_sales_channel_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_sales_channel_Set() const{
    return m_sales_channel_isSet;
}

bool OAIClearorderFormMessages_200_response::is_sales_channel_Valid() const{
    return m_sales_channel_isValid;
}

QList<QJsonValue> OAIClearorderFormMessages_200_response::getSelectableGifts() const {
    return m_selectable_gifts;
}
void OAIClearorderFormMessages_200_response::setSelectableGifts(const QList<QJsonValue> &selectable_gifts) {
    m_selectable_gifts = selectable_gifts;
    m_selectable_gifts_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_selectable_gifts_Set() const{
    return m_selectable_gifts_isSet;
}

bool OAIClearorderFormMessages_200_response::is_selectable_gifts_Valid() const{
    return m_selectable_gifts_isValid;
}

QList<OAIAddCoupons_200_response_sellers_inner> OAIClearorderFormMessages_200_response::getSellers() const {
    return m_sellers;
}
void OAIClearorderFormMessages_200_response::setSellers(const QList<OAIAddCoupons_200_response_sellers_inner> &sellers) {
    m_sellers = sellers;
    m_sellers_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_sellers_Set() const{
    return m_sellers_isSet;
}

bool OAIClearorderFormMessages_200_response::is_sellers_Valid() const{
    return m_sellers_isValid;
}

OAIAddCoupons_200_response_shippingData OAIClearorderFormMessages_200_response::getShippingData() const {
    return m_shipping_data;
}
void OAIClearorderFormMessages_200_response::setShippingData(const OAIAddCoupons_200_response_shippingData &shipping_data) {
    m_shipping_data = shipping_data;
    m_shipping_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_shipping_data_Set() const{
    return m_shipping_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_shipping_data_Valid() const{
    return m_shipping_data_isValid;
}

QString OAIClearorderFormMessages_200_response::getStoreId() const {
    return m_store_id;
}
void OAIClearorderFormMessages_200_response::setStoreId(const QString &store_id) {
    m_store_id = store_id;
    m_store_id_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_store_id_Set() const{
    return m_store_id_isSet;
}

bool OAIClearorderFormMessages_200_response::is_store_id_Valid() const{
    return m_store_id_isValid;
}

OAIObject OAIClearorderFormMessages_200_response::getStorePreferencesData() const {
    return m_store_preferences_data;
}
void OAIClearorderFormMessages_200_response::setStorePreferencesData(const OAIObject &store_preferences_data) {
    m_store_preferences_data = store_preferences_data;
    m_store_preferences_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_store_preferences_data_Set() const{
    return m_store_preferences_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_store_preferences_data_Valid() const{
    return m_store_preferences_data_isValid;
}

OAIObject OAIClearorderFormMessages_200_response::getSubscriptionData() const {
    return m_subscription_data;
}
void OAIClearorderFormMessages_200_response::setSubscriptionData(const OAIObject &subscription_data) {
    m_subscription_data = subscription_data;
    m_subscription_data_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_subscription_data_Set() const{
    return m_subscription_data_isSet;
}

bool OAIClearorderFormMessages_200_response::is_subscription_data_Valid() const{
    return m_subscription_data_isValid;
}

QList<QJsonValue> OAIClearorderFormMessages_200_response::getTotalizers() const {
    return m_totalizers;
}
void OAIClearorderFormMessages_200_response::setTotalizers(const QList<QJsonValue> &totalizers) {
    m_totalizers = totalizers;
    m_totalizers_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_totalizers_Set() const{
    return m_totalizers_isSet;
}

bool OAIClearorderFormMessages_200_response::is_totalizers_Valid() const{
    return m_totalizers_isValid;
}

QString OAIClearorderFormMessages_200_response::getUserProfileId() const {
    return m_user_profile_id;
}
void OAIClearorderFormMessages_200_response::setUserProfileId(const QString &user_profile_id) {
    m_user_profile_id = user_profile_id;
    m_user_profile_id_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_user_profile_id_Set() const{
    return m_user_profile_id_isSet;
}

bool OAIClearorderFormMessages_200_response::is_user_profile_id_Valid() const{
    return m_user_profile_id_isValid;
}

QString OAIClearorderFormMessages_200_response::getUserType() const {
    return m_user_type;
}
void OAIClearorderFormMessages_200_response::setUserType(const QString &user_type) {
    m_user_type = user_type;
    m_user_type_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_user_type_Set() const{
    return m_user_type_isSet;
}

bool OAIClearorderFormMessages_200_response::is_user_type_Valid() const{
    return m_user_type_isValid;
}

qint32 OAIClearorderFormMessages_200_response::getValue() const {
    return m_value;
}
void OAIClearorderFormMessages_200_response::setValue(const qint32 &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIClearorderFormMessages_200_response::is_value_Set() const{
    return m_value_isSet;
}

bool OAIClearorderFormMessages_200_response::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIClearorderFormMessages_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_allow_manual_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_available_accounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_available_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_can_edit_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_preferences_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_profile_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_commercial_condition_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_registry_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hooks_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ignore_profile_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_invoice_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_checked_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_item_metadata.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_items_ordination.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_logged_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_marketing_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_messages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_open_text_field_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_form_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_profile_provider_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rates_and_benefits_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_sales_channel_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_selectable_gifts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_sellers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_store_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_store_preferences_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subscription_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_totalizers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_profile_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIClearorderFormMessages_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
