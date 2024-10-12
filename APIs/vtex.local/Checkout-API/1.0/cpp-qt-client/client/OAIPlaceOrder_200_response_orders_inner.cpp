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

#include "OAIPlaceOrder_200_response_orders_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlaceOrder_200_response_orders_inner::OAIPlaceOrder_200_response_orders_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlaceOrder_200_response_orders_inner::OAIPlaceOrder_200_response_orders_inner() {
    this->initializeModel();
}

OAIPlaceOrder_200_response_orders_inner::~OAIPlaceOrder_200_response_orders_inner() {}

void OAIPlaceOrder_200_response_orders_inner::initializeModel() {

    m_allow_cancelation_isSet = false;
    m_allow_cancelation_isValid = false;

    m_allow_change_seller_isSet = false;
    m_allow_change_seller_isValid = false;

    m_allow_edition_isSet = false;
    m_allow_edition_isValid = false;

    m_checked_in_pickup_point_id_isSet = false;
    m_checked_in_pickup_point_id_isValid = false;

    m_client_profile_data_isSet = false;
    m_client_profile_data_isValid = false;

    m_creation_date_isSet = false;
    m_creation_date_isValid = false;

    m_follow_up_email_isSet = false;
    m_follow_up_email_isValid = false;

    m_host_name_isSet = false;
    m_host_name_isValid = false;

    m_is_checked_in_isSet = false;
    m_is_checked_in_isValid = false;

    m_is_completed_isSet = false;
    m_is_completed_isValid = false;

    m_is_user_data_visible_isSet = false;
    m_is_user_data_visible_isValid = false;

    m_item_metadata_isSet = false;
    m_item_metadata_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;

    m_last_change_isSet = false;
    m_last_change_isValid = false;

    m_merchant_name_isSet = false;
    m_merchant_name_isValid = false;

    m_order_form_creation_date_isSet = false;
    m_order_form_creation_date_isValid = false;

    m_order_group_isSet = false;
    m_order_group_isValid = false;

    m_order_id_isSet = false;
    m_order_id_isValid = false;

    m_payment_data_isSet = false;
    m_payment_data_isValid = false;

    m_rates_and_benefits_data_isSet = false;
    m_rates_and_benefits_data_isValid = false;

    m_rounding_error_isSet = false;
    m_rounding_error_isValid = false;

    m_sales_associate_id_isSet = false;
    m_sales_associate_id_isValid = false;

    m_sales_channel_isSet = false;
    m_sales_channel_isValid = false;

    m_seller_order_id_isSet = false;
    m_seller_order_id_isValid = false;

    m_sellers_isSet = false;
    m_sellers_isValid = false;

    m_shipping_data_isSet = false;
    m_shipping_data_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_store_id_isSet = false;
    m_store_id_isValid = false;

    m_time_zone_creation_date_isSet = false;
    m_time_zone_creation_date_isValid = false;

    m_time_zone_last_change_isSet = false;
    m_time_zone_last_change_isValid = false;

    m_totals_isSet = false;
    m_totals_isValid = false;

    m_user_type_isSet = false;
    m_user_type_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIPlaceOrder_200_response_orders_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlaceOrder_200_response_orders_inner::fromJsonObject(QJsonObject json) {

    m_allow_cancelation_isValid = ::OpenAPI::fromJsonValue(m_allow_cancelation, json[QString("allowCancelation")]);
    m_allow_cancelation_isSet = !json[QString("allowCancelation")].isNull() && m_allow_cancelation_isValid;

    m_allow_change_seller_isValid = ::OpenAPI::fromJsonValue(m_allow_change_seller, json[QString("allowChangeSeller")]);
    m_allow_change_seller_isSet = !json[QString("allowChangeSeller")].isNull() && m_allow_change_seller_isValid;

    m_allow_edition_isValid = ::OpenAPI::fromJsonValue(m_allow_edition, json[QString("allowEdition")]);
    m_allow_edition_isSet = !json[QString("allowEdition")].isNull() && m_allow_edition_isValid;

    m_checked_in_pickup_point_id_isValid = ::OpenAPI::fromJsonValue(m_checked_in_pickup_point_id, json[QString("checkedInPickupPointId")]);
    m_checked_in_pickup_point_id_isSet = !json[QString("checkedInPickupPointId")].isNull() && m_checked_in_pickup_point_id_isValid;

    m_client_profile_data_isValid = ::OpenAPI::fromJsonValue(m_client_profile_data, json[QString("clientProfileData")]);
    m_client_profile_data_isSet = !json[QString("clientProfileData")].isNull() && m_client_profile_data_isValid;

    m_creation_date_isValid = ::OpenAPI::fromJsonValue(m_creation_date, json[QString("creationDate")]);
    m_creation_date_isSet = !json[QString("creationDate")].isNull() && m_creation_date_isValid;

    m_follow_up_email_isValid = ::OpenAPI::fromJsonValue(m_follow_up_email, json[QString("followUpEmail")]);
    m_follow_up_email_isSet = !json[QString("followUpEmail")].isNull() && m_follow_up_email_isValid;

    m_host_name_isValid = ::OpenAPI::fromJsonValue(m_host_name, json[QString("hostName")]);
    m_host_name_isSet = !json[QString("hostName")].isNull() && m_host_name_isValid;

    m_is_checked_in_isValid = ::OpenAPI::fromJsonValue(m_is_checked_in, json[QString("isCheckedIn")]);
    m_is_checked_in_isSet = !json[QString("isCheckedIn")].isNull() && m_is_checked_in_isValid;

    m_is_completed_isValid = ::OpenAPI::fromJsonValue(m_is_completed, json[QString("isCompleted")]);
    m_is_completed_isSet = !json[QString("isCompleted")].isNull() && m_is_completed_isValid;

    m_is_user_data_visible_isValid = ::OpenAPI::fromJsonValue(m_is_user_data_visible, json[QString("isUserDataVisible")]);
    m_is_user_data_visible_isSet = !json[QString("isUserDataVisible")].isNull() && m_is_user_data_visible_isValid;

    m_item_metadata_isValid = ::OpenAPI::fromJsonValue(m_item_metadata, json[QString("itemMetadata")]);
    m_item_metadata_isSet = !json[QString("itemMetadata")].isNull() && m_item_metadata_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_last_change_isValid = ::OpenAPI::fromJsonValue(m_last_change, json[QString("lastChange")]);
    m_last_change_isSet = !json[QString("lastChange")].isNull() && m_last_change_isValid;

    m_merchant_name_isValid = ::OpenAPI::fromJsonValue(m_merchant_name, json[QString("merchantName")]);
    m_merchant_name_isSet = !json[QString("merchantName")].isNull() && m_merchant_name_isValid;

    m_order_form_creation_date_isValid = ::OpenAPI::fromJsonValue(m_order_form_creation_date, json[QString("orderFormCreationDate")]);
    m_order_form_creation_date_isSet = !json[QString("orderFormCreationDate")].isNull() && m_order_form_creation_date_isValid;

    m_order_group_isValid = ::OpenAPI::fromJsonValue(m_order_group, json[QString("orderGroup")]);
    m_order_group_isSet = !json[QString("orderGroup")].isNull() && m_order_group_isValid;

    m_order_id_isValid = ::OpenAPI::fromJsonValue(m_order_id, json[QString("orderId")]);
    m_order_id_isSet = !json[QString("orderId")].isNull() && m_order_id_isValid;

    m_payment_data_isValid = ::OpenAPI::fromJsonValue(m_payment_data, json[QString("paymentData")]);
    m_payment_data_isSet = !json[QString("paymentData")].isNull() && m_payment_data_isValid;

    m_rates_and_benefits_data_isValid = ::OpenAPI::fromJsonValue(m_rates_and_benefits_data, json[QString("ratesAndBenefitsData")]);
    m_rates_and_benefits_data_isSet = !json[QString("ratesAndBenefitsData")].isNull() && m_rates_and_benefits_data_isValid;

    m_rounding_error_isValid = ::OpenAPI::fromJsonValue(m_rounding_error, json[QString("roundingError")]);
    m_rounding_error_isSet = !json[QString("roundingError")].isNull() && m_rounding_error_isValid;

    m_sales_associate_id_isValid = ::OpenAPI::fromJsonValue(m_sales_associate_id, json[QString("salesAssociateId")]);
    m_sales_associate_id_isSet = !json[QString("salesAssociateId")].isNull() && m_sales_associate_id_isValid;

    m_sales_channel_isValid = ::OpenAPI::fromJsonValue(m_sales_channel, json[QString("salesChannel")]);
    m_sales_channel_isSet = !json[QString("salesChannel")].isNull() && m_sales_channel_isValid;

    m_seller_order_id_isValid = ::OpenAPI::fromJsonValue(m_seller_order_id, json[QString("sellerOrderId")]);
    m_seller_order_id_isSet = !json[QString("sellerOrderId")].isNull() && m_seller_order_id_isValid;

    m_sellers_isValid = ::OpenAPI::fromJsonValue(m_sellers, json[QString("sellers")]);
    m_sellers_isSet = !json[QString("sellers")].isNull() && m_sellers_isValid;

    m_shipping_data_isValid = ::OpenAPI::fromJsonValue(m_shipping_data, json[QString("shippingData")]);
    m_shipping_data_isSet = !json[QString("shippingData")].isNull() && m_shipping_data_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_store_id_isValid = ::OpenAPI::fromJsonValue(m_store_id, json[QString("storeId")]);
    m_store_id_isSet = !json[QString("storeId")].isNull() && m_store_id_isValid;

    m_time_zone_creation_date_isValid = ::OpenAPI::fromJsonValue(m_time_zone_creation_date, json[QString("timeZoneCreationDate")]);
    m_time_zone_creation_date_isSet = !json[QString("timeZoneCreationDate")].isNull() && m_time_zone_creation_date_isValid;

    m_time_zone_last_change_isValid = ::OpenAPI::fromJsonValue(m_time_zone_last_change, json[QString("timeZoneLastChange")]);
    m_time_zone_last_change_isSet = !json[QString("timeZoneLastChange")].isNull() && m_time_zone_last_change_isValid;

    m_totals_isValid = ::OpenAPI::fromJsonValue(m_totals, json[QString("totals")]);
    m_totals_isSet = !json[QString("totals")].isNull() && m_totals_isValid;

    m_user_type_isValid = ::OpenAPI::fromJsonValue(m_user_type, json[QString("userType")]);
    m_user_type_isSet = !json[QString("userType")].isNull() && m_user_type_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlaceOrder_200_response_orders_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_allow_cancelation_isSet) {
        obj.insert(QString("allowCancelation"), ::OpenAPI::toJsonValue(m_allow_cancelation));
    }
    if (m_allow_change_seller_isSet) {
        obj.insert(QString("allowChangeSeller"), ::OpenAPI::toJsonValue(m_allow_change_seller));
    }
    if (m_allow_edition_isSet) {
        obj.insert(QString("allowEdition"), ::OpenAPI::toJsonValue(m_allow_edition));
    }
    if (m_checked_in_pickup_point_id_isSet) {
        obj.insert(QString("checkedInPickupPointId"), ::OpenAPI::toJsonValue(m_checked_in_pickup_point_id));
    }
    if (m_client_profile_data.isSet()) {
        obj.insert(QString("clientProfileData"), ::OpenAPI::toJsonValue(m_client_profile_data));
    }
    if (m_creation_date_isSet) {
        obj.insert(QString("creationDate"), ::OpenAPI::toJsonValue(m_creation_date));
    }
    if (m_follow_up_email_isSet) {
        obj.insert(QString("followUpEmail"), ::OpenAPI::toJsonValue(m_follow_up_email));
    }
    if (m_host_name_isSet) {
        obj.insert(QString("hostName"), ::OpenAPI::toJsonValue(m_host_name));
    }
    if (m_is_checked_in_isSet) {
        obj.insert(QString("isCheckedIn"), ::OpenAPI::toJsonValue(m_is_checked_in));
    }
    if (m_is_completed_isSet) {
        obj.insert(QString("isCompleted"), ::OpenAPI::toJsonValue(m_is_completed));
    }
    if (m_is_user_data_visible_isSet) {
        obj.insert(QString("isUserDataVisible"), ::OpenAPI::toJsonValue(m_is_user_data_visible));
    }
    if (m_item_metadata.isSet()) {
        obj.insert(QString("itemMetadata"), ::OpenAPI::toJsonValue(m_item_metadata));
    }
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_last_change_isSet) {
        obj.insert(QString("lastChange"), ::OpenAPI::toJsonValue(m_last_change));
    }
    if (m_merchant_name_isSet) {
        obj.insert(QString("merchantName"), ::OpenAPI::toJsonValue(m_merchant_name));
    }
    if (m_order_form_creation_date_isSet) {
        obj.insert(QString("orderFormCreationDate"), ::OpenAPI::toJsonValue(m_order_form_creation_date));
    }
    if (m_order_group_isSet) {
        obj.insert(QString("orderGroup"), ::OpenAPI::toJsonValue(m_order_group));
    }
    if (m_order_id_isSet) {
        obj.insert(QString("orderId"), ::OpenAPI::toJsonValue(m_order_id));
    }
    if (m_payment_data.isSet()) {
        obj.insert(QString("paymentData"), ::OpenAPI::toJsonValue(m_payment_data));
    }
    if (m_rates_and_benefits_data.isSet()) {
        obj.insert(QString("ratesAndBenefitsData"), ::OpenAPI::toJsonValue(m_rates_and_benefits_data));
    }
    if (m_rounding_error_isSet) {
        obj.insert(QString("roundingError"), ::OpenAPI::toJsonValue(m_rounding_error));
    }
    if (m_sales_associate_id_isSet) {
        obj.insert(QString("salesAssociateId"), ::OpenAPI::toJsonValue(m_sales_associate_id));
    }
    if (m_sales_channel_isSet) {
        obj.insert(QString("salesChannel"), ::OpenAPI::toJsonValue(m_sales_channel));
    }
    if (m_seller_order_id_isSet) {
        obj.insert(QString("sellerOrderId"), ::OpenAPI::toJsonValue(m_seller_order_id));
    }
    if (m_sellers.size() > 0) {
        obj.insert(QString("sellers"), ::OpenAPI::toJsonValue(m_sellers));
    }
    if (m_shipping_data.isSet()) {
        obj.insert(QString("shippingData"), ::OpenAPI::toJsonValue(m_shipping_data));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_store_id_isSet) {
        obj.insert(QString("storeId"), ::OpenAPI::toJsonValue(m_store_id));
    }
    if (m_time_zone_creation_date_isSet) {
        obj.insert(QString("timeZoneCreationDate"), ::OpenAPI::toJsonValue(m_time_zone_creation_date));
    }
    if (m_time_zone_last_change_isSet) {
        obj.insert(QString("timeZoneLastChange"), ::OpenAPI::toJsonValue(m_time_zone_last_change));
    }
    if (m_totals.size() > 0) {
        obj.insert(QString("totals"), ::OpenAPI::toJsonValue(m_totals));
    }
    if (m_user_type_isSet) {
        obj.insert(QString("userType"), ::OpenAPI::toJsonValue(m_user_type));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

bool OAIPlaceOrder_200_response_orders_inner::isAllowCancelation() const {
    return m_allow_cancelation;
}
void OAIPlaceOrder_200_response_orders_inner::setAllowCancelation(const bool &allow_cancelation) {
    m_allow_cancelation = allow_cancelation;
    m_allow_cancelation_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_allow_cancelation_Set() const{
    return m_allow_cancelation_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_allow_cancelation_Valid() const{
    return m_allow_cancelation_isValid;
}

bool OAIPlaceOrder_200_response_orders_inner::isAllowChangeSeller() const {
    return m_allow_change_seller;
}
void OAIPlaceOrder_200_response_orders_inner::setAllowChangeSeller(const bool &allow_change_seller) {
    m_allow_change_seller = allow_change_seller;
    m_allow_change_seller_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_allow_change_seller_Set() const{
    return m_allow_change_seller_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_allow_change_seller_Valid() const{
    return m_allow_change_seller_isValid;
}

bool OAIPlaceOrder_200_response_orders_inner::isAllowEdition() const {
    return m_allow_edition;
}
void OAIPlaceOrder_200_response_orders_inner::setAllowEdition(const bool &allow_edition) {
    m_allow_edition = allow_edition;
    m_allow_edition_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_allow_edition_Set() const{
    return m_allow_edition_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_allow_edition_Valid() const{
    return m_allow_edition_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getCheckedInPickupPointId() const {
    return m_checked_in_pickup_point_id;
}
void OAIPlaceOrder_200_response_orders_inner::setCheckedInPickupPointId(const QString &checked_in_pickup_point_id) {
    m_checked_in_pickup_point_id = checked_in_pickup_point_id;
    m_checked_in_pickup_point_id_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_checked_in_pickup_point_id_Set() const{
    return m_checked_in_pickup_point_id_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_checked_in_pickup_point_id_Valid() const{
    return m_checked_in_pickup_point_id_isValid;
}

OAIAddCoupons_200_response_clientProfileData OAIPlaceOrder_200_response_orders_inner::getClientProfileData() const {
    return m_client_profile_data;
}
void OAIPlaceOrder_200_response_orders_inner::setClientProfileData(const OAIAddCoupons_200_response_clientProfileData &client_profile_data) {
    m_client_profile_data = client_profile_data;
    m_client_profile_data_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_client_profile_data_Set() const{
    return m_client_profile_data_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_client_profile_data_Valid() const{
    return m_client_profile_data_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getCreationDate() const {
    return m_creation_date;
}
void OAIPlaceOrder_200_response_orders_inner::setCreationDate(const QString &creation_date) {
    m_creation_date = creation_date;
    m_creation_date_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_creation_date_Set() const{
    return m_creation_date_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_creation_date_Valid() const{
    return m_creation_date_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getFollowUpEmail() const {
    return m_follow_up_email;
}
void OAIPlaceOrder_200_response_orders_inner::setFollowUpEmail(const QString &follow_up_email) {
    m_follow_up_email = follow_up_email;
    m_follow_up_email_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_follow_up_email_Set() const{
    return m_follow_up_email_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_follow_up_email_Valid() const{
    return m_follow_up_email_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getHostName() const {
    return m_host_name;
}
void OAIPlaceOrder_200_response_orders_inner::setHostName(const QString &host_name) {
    m_host_name = host_name;
    m_host_name_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_host_name_Set() const{
    return m_host_name_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_host_name_Valid() const{
    return m_host_name_isValid;
}

bool OAIPlaceOrder_200_response_orders_inner::isIsCheckedIn() const {
    return m_is_checked_in;
}
void OAIPlaceOrder_200_response_orders_inner::setIsCheckedIn(const bool &is_checked_in) {
    m_is_checked_in = is_checked_in;
    m_is_checked_in_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_is_checked_in_Set() const{
    return m_is_checked_in_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_is_checked_in_Valid() const{
    return m_is_checked_in_isValid;
}

bool OAIPlaceOrder_200_response_orders_inner::isIsCompleted() const {
    return m_is_completed;
}
void OAIPlaceOrder_200_response_orders_inner::setIsCompleted(const bool &is_completed) {
    m_is_completed = is_completed;
    m_is_completed_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_is_completed_Set() const{
    return m_is_completed_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_is_completed_Valid() const{
    return m_is_completed_isValid;
}

bool OAIPlaceOrder_200_response_orders_inner::isIsUserDataVisible() const {
    return m_is_user_data_visible;
}
void OAIPlaceOrder_200_response_orders_inner::setIsUserDataVisible(const bool &is_user_data_visible) {
    m_is_user_data_visible = is_user_data_visible;
    m_is_user_data_visible_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_is_user_data_visible_Set() const{
    return m_is_user_data_visible_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_is_user_data_visible_Valid() const{
    return m_is_user_data_visible_isValid;
}

OAIAddCoupons_200_response_itemMetadata OAIPlaceOrder_200_response_orders_inner::getItemMetadata() const {
    return m_item_metadata;
}
void OAIPlaceOrder_200_response_orders_inner::setItemMetadata(const OAIAddCoupons_200_response_itemMetadata &item_metadata) {
    m_item_metadata = item_metadata;
    m_item_metadata_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_item_metadata_Set() const{
    return m_item_metadata_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_item_metadata_Valid() const{
    return m_item_metadata_isValid;
}

QList<OAIPlaceOrder_200_response_orders_inner_items_inner> OAIPlaceOrder_200_response_orders_inner::getItems() const {
    return m_items;
}
void OAIPlaceOrder_200_response_orders_inner::setItems(const QList<OAIPlaceOrder_200_response_orders_inner_items_inner> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_items_Set() const{
    return m_items_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_items_Valid() const{
    return m_items_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getLastChange() const {
    return m_last_change;
}
void OAIPlaceOrder_200_response_orders_inner::setLastChange(const QString &last_change) {
    m_last_change = last_change;
    m_last_change_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_last_change_Set() const{
    return m_last_change_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_last_change_Valid() const{
    return m_last_change_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getMerchantName() const {
    return m_merchant_name;
}
void OAIPlaceOrder_200_response_orders_inner::setMerchantName(const QString &merchant_name) {
    m_merchant_name = merchant_name;
    m_merchant_name_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_merchant_name_Set() const{
    return m_merchant_name_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_merchant_name_Valid() const{
    return m_merchant_name_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getOrderFormCreationDate() const {
    return m_order_form_creation_date;
}
void OAIPlaceOrder_200_response_orders_inner::setOrderFormCreationDate(const QString &order_form_creation_date) {
    m_order_form_creation_date = order_form_creation_date;
    m_order_form_creation_date_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_order_form_creation_date_Set() const{
    return m_order_form_creation_date_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_order_form_creation_date_Valid() const{
    return m_order_form_creation_date_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getOrderGroup() const {
    return m_order_group;
}
void OAIPlaceOrder_200_response_orders_inner::setOrderGroup(const QString &order_group) {
    m_order_group = order_group;
    m_order_group_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_order_group_Set() const{
    return m_order_group_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_order_group_Valid() const{
    return m_order_group_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getOrderId() const {
    return m_order_id;
}
void OAIPlaceOrder_200_response_orders_inner::setOrderId(const QString &order_id) {
    m_order_id = order_id;
    m_order_id_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_order_id_Set() const{
    return m_order_id_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_order_id_Valid() const{
    return m_order_id_isValid;
}

OAIAddCoupons_200_response_paymentData OAIPlaceOrder_200_response_orders_inner::getPaymentData() const {
    return m_payment_data;
}
void OAIPlaceOrder_200_response_orders_inner::setPaymentData(const OAIAddCoupons_200_response_paymentData &payment_data) {
    m_payment_data = payment_data;
    m_payment_data_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_payment_data_Set() const{
    return m_payment_data_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_payment_data_Valid() const{
    return m_payment_data_isValid;
}

OAIAddCoupons_200_response_ratesAndBenefitsData OAIPlaceOrder_200_response_orders_inner::getRatesAndBenefitsData() const {
    return m_rates_and_benefits_data;
}
void OAIPlaceOrder_200_response_orders_inner::setRatesAndBenefitsData(const OAIAddCoupons_200_response_ratesAndBenefitsData &rates_and_benefits_data) {
    m_rates_and_benefits_data = rates_and_benefits_data;
    m_rates_and_benefits_data_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_rates_and_benefits_data_Set() const{
    return m_rates_and_benefits_data_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_rates_and_benefits_data_Valid() const{
    return m_rates_and_benefits_data_isValid;
}

qint32 OAIPlaceOrder_200_response_orders_inner::getRoundingError() const {
    return m_rounding_error;
}
void OAIPlaceOrder_200_response_orders_inner::setRoundingError(const qint32 &rounding_error) {
    m_rounding_error = rounding_error;
    m_rounding_error_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_rounding_error_Set() const{
    return m_rounding_error_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_rounding_error_Valid() const{
    return m_rounding_error_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getSalesAssociateId() const {
    return m_sales_associate_id;
}
void OAIPlaceOrder_200_response_orders_inner::setSalesAssociateId(const QString &sales_associate_id) {
    m_sales_associate_id = sales_associate_id;
    m_sales_associate_id_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_sales_associate_id_Set() const{
    return m_sales_associate_id_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_sales_associate_id_Valid() const{
    return m_sales_associate_id_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getSalesChannel() const {
    return m_sales_channel;
}
void OAIPlaceOrder_200_response_orders_inner::setSalesChannel(const QString &sales_channel) {
    m_sales_channel = sales_channel;
    m_sales_channel_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_sales_channel_Set() const{
    return m_sales_channel_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_sales_channel_Valid() const{
    return m_sales_channel_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getSellerOrderId() const {
    return m_seller_order_id;
}
void OAIPlaceOrder_200_response_orders_inner::setSellerOrderId(const QString &seller_order_id) {
    m_seller_order_id = seller_order_id;
    m_seller_order_id_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_seller_order_id_Set() const{
    return m_seller_order_id_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_seller_order_id_Valid() const{
    return m_seller_order_id_isValid;
}

QList<OAIAddCoupons_200_response_sellers_inner> OAIPlaceOrder_200_response_orders_inner::getSellers() const {
    return m_sellers;
}
void OAIPlaceOrder_200_response_orders_inner::setSellers(const QList<OAIAddCoupons_200_response_sellers_inner> &sellers) {
    m_sellers = sellers;
    m_sellers_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_sellers_Set() const{
    return m_sellers_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_sellers_Valid() const{
    return m_sellers_isValid;
}

OAIAddCoupons_200_response_shippingData OAIPlaceOrder_200_response_orders_inner::getShippingData() const {
    return m_shipping_data;
}
void OAIPlaceOrder_200_response_orders_inner::setShippingData(const OAIAddCoupons_200_response_shippingData &shipping_data) {
    m_shipping_data = shipping_data;
    m_shipping_data_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_shipping_data_Set() const{
    return m_shipping_data_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_shipping_data_Valid() const{
    return m_shipping_data_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getState() const {
    return m_state;
}
void OAIPlaceOrder_200_response_orders_inner::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_state_Set() const{
    return m_state_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getStoreId() const {
    return m_store_id;
}
void OAIPlaceOrder_200_response_orders_inner::setStoreId(const QString &store_id) {
    m_store_id = store_id;
    m_store_id_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_store_id_Set() const{
    return m_store_id_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_store_id_Valid() const{
    return m_store_id_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getTimeZoneCreationDate() const {
    return m_time_zone_creation_date;
}
void OAIPlaceOrder_200_response_orders_inner::setTimeZoneCreationDate(const QString &time_zone_creation_date) {
    m_time_zone_creation_date = time_zone_creation_date;
    m_time_zone_creation_date_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_time_zone_creation_date_Set() const{
    return m_time_zone_creation_date_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_time_zone_creation_date_Valid() const{
    return m_time_zone_creation_date_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getTimeZoneLastChange() const {
    return m_time_zone_last_change;
}
void OAIPlaceOrder_200_response_orders_inner::setTimeZoneLastChange(const QString &time_zone_last_change) {
    m_time_zone_last_change = time_zone_last_change;
    m_time_zone_last_change_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_time_zone_last_change_Set() const{
    return m_time_zone_last_change_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_time_zone_last_change_Valid() const{
    return m_time_zone_last_change_isValid;
}

QList<OAICartSimulation_200_response_logisticsInfo_inner_totals_inner> OAIPlaceOrder_200_response_orders_inner::getTotals() const {
    return m_totals;
}
void OAIPlaceOrder_200_response_orders_inner::setTotals(const QList<OAICartSimulation_200_response_logisticsInfo_inner_totals_inner> &totals) {
    m_totals = totals;
    m_totals_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_totals_Set() const{
    return m_totals_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_totals_Valid() const{
    return m_totals_isValid;
}

QString OAIPlaceOrder_200_response_orders_inner::getUserType() const {
    return m_user_type;
}
void OAIPlaceOrder_200_response_orders_inner::setUserType(const QString &user_type) {
    m_user_type = user_type;
    m_user_type_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_user_type_Set() const{
    return m_user_type_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_user_type_Valid() const{
    return m_user_type_isValid;
}

qint32 OAIPlaceOrder_200_response_orders_inner::getValue() const {
    return m_value;
}
void OAIPlaceOrder_200_response_orders_inner::setValue(const qint32 &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIPlaceOrder_200_response_orders_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIPlaceOrder_200_response_orders_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIPlaceOrder_200_response_orders_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_allow_cancelation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_allow_change_seller_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_allow_edition_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_checked_in_pickup_point_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_profile_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_creation_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_follow_up_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_host_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_checked_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_completed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_user_data_visible_isSet) {
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

        if (m_last_change_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merchant_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_form_creation_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_group_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_rates_and_benefits_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_rounding_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sales_associate_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sales_channel_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seller_order_id_isSet) {
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

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_store_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_zone_creation_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_zone_last_change_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_totals.size() > 0) {
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

bool OAIPlaceOrder_200_response_orders_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
