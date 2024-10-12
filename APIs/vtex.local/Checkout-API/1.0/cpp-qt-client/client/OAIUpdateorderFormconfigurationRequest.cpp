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

#include "OAIUpdateorderFormconfigurationRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateorderFormconfigurationRequest::OAIUpdateorderFormconfigurationRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateorderFormconfigurationRequest::OAIUpdateorderFormconfigurationRequest() {
    this->initializeModel();
}

OAIUpdateorderFormconfigurationRequest::~OAIUpdateorderFormconfigurationRequest() {}

void OAIUpdateorderFormconfigurationRequest::initializeModel() {

    m_allow_manual_price_isSet = false;
    m_allow_manual_price_isValid = false;

    m_allow_multiple_deliveries_isSet = false;
    m_allow_multiple_deliveries_isValid = false;

    m_apps_isSet = false;
    m_apps_isValid = false;

    m_decimal_digits_precision_isSet = false;
    m_decimal_digits_precision_isValid = false;

    m_mask_first_purchase_data_isSet = false;
    m_mask_first_purchase_data_isValid = false;

    m_max_number_of_white_label_sellers_isSet = false;
    m_max_number_of_white_label_sellers_isValid = false;

    m_minimum_quantity_accumulated_for_items_isSet = false;
    m_minimum_quantity_accumulated_for_items_isValid = false;

    m_minimum_value_accumulated_isSet = false;
    m_minimum_value_accumulated_isValid = false;

    m_payment_configuration_isSet = false;
    m_payment_configuration_isValid = false;

    m_payment_system_to_check_first_installment_isSet = false;
    m_payment_system_to_check_first_installment_isValid = false;

    m_recaptcha_validation_isSet = false;
    m_recaptcha_validation_isValid = false;

    m_tax_configuration_isSet = false;
    m_tax_configuration_isValid = false;
}

void OAIUpdateorderFormconfigurationRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateorderFormconfigurationRequest::fromJsonObject(QJsonObject json) {

    m_allow_manual_price_isValid = ::OpenAPI::fromJsonValue(m_allow_manual_price, json[QString("allowManualPrice")]);
    m_allow_manual_price_isSet = !json[QString("allowManualPrice")].isNull() && m_allow_manual_price_isValid;

    m_allow_multiple_deliveries_isValid = ::OpenAPI::fromJsonValue(m_allow_multiple_deliveries, json[QString("allowMultipleDeliveries")]);
    m_allow_multiple_deliveries_isSet = !json[QString("allowMultipleDeliveries")].isNull() && m_allow_multiple_deliveries_isValid;

    m_apps_isValid = ::OpenAPI::fromJsonValue(m_apps, json[QString("apps")]);
    m_apps_isSet = !json[QString("apps")].isNull() && m_apps_isValid;

    m_decimal_digits_precision_isValid = ::OpenAPI::fromJsonValue(m_decimal_digits_precision, json[QString("decimalDigitsPrecision")]);
    m_decimal_digits_precision_isSet = !json[QString("decimalDigitsPrecision")].isNull() && m_decimal_digits_precision_isValid;

    m_mask_first_purchase_data_isValid = ::OpenAPI::fromJsonValue(m_mask_first_purchase_data, json[QString("maskFirstPurchaseData")]);
    m_mask_first_purchase_data_isSet = !json[QString("maskFirstPurchaseData")].isNull() && m_mask_first_purchase_data_isValid;

    m_max_number_of_white_label_sellers_isValid = ::OpenAPI::fromJsonValue(m_max_number_of_white_label_sellers, json[QString("maxNumberOfWhiteLabelSellers")]);
    m_max_number_of_white_label_sellers_isSet = !json[QString("maxNumberOfWhiteLabelSellers")].isNull() && m_max_number_of_white_label_sellers_isValid;

    m_minimum_quantity_accumulated_for_items_isValid = ::OpenAPI::fromJsonValue(m_minimum_quantity_accumulated_for_items, json[QString("minimumQuantityAccumulatedForItems")]);
    m_minimum_quantity_accumulated_for_items_isSet = !json[QString("minimumQuantityAccumulatedForItems")].isNull() && m_minimum_quantity_accumulated_for_items_isValid;

    m_minimum_value_accumulated_isValid = ::OpenAPI::fromJsonValue(m_minimum_value_accumulated, json[QString("minimumValueAccumulated")]);
    m_minimum_value_accumulated_isSet = !json[QString("minimumValueAccumulated")].isNull() && m_minimum_value_accumulated_isValid;

    m_payment_configuration_isValid = ::OpenAPI::fromJsonValue(m_payment_configuration, json[QString("paymentConfiguration")]);
    m_payment_configuration_isSet = !json[QString("paymentConfiguration")].isNull() && m_payment_configuration_isValid;

    m_payment_system_to_check_first_installment_isValid = ::OpenAPI::fromJsonValue(m_payment_system_to_check_first_installment, json[QString("paymentSystemToCheckFirstInstallment")]);
    m_payment_system_to_check_first_installment_isSet = !json[QString("paymentSystemToCheckFirstInstallment")].isNull() && m_payment_system_to_check_first_installment_isValid;

    m_recaptcha_validation_isValid = ::OpenAPI::fromJsonValue(m_recaptcha_validation, json[QString("recaptchaValidation")]);
    m_recaptcha_validation_isSet = !json[QString("recaptchaValidation")].isNull() && m_recaptcha_validation_isValid;

    m_tax_configuration_isValid = ::OpenAPI::fromJsonValue(m_tax_configuration, json[QString("taxConfiguration")]);
    m_tax_configuration_isSet = !json[QString("taxConfiguration")].isNull() && m_tax_configuration_isValid;
}

QString OAIUpdateorderFormconfigurationRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateorderFormconfigurationRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_allow_manual_price_isSet) {
        obj.insert(QString("allowManualPrice"), ::OpenAPI::toJsonValue(m_allow_manual_price));
    }
    if (m_allow_multiple_deliveries_isSet) {
        obj.insert(QString("allowMultipleDeliveries"), ::OpenAPI::toJsonValue(m_allow_multiple_deliveries));
    }
    if (m_apps.size() > 0) {
        obj.insert(QString("apps"), ::OpenAPI::toJsonValue(m_apps));
    }
    if (m_decimal_digits_precision_isSet) {
        obj.insert(QString("decimalDigitsPrecision"), ::OpenAPI::toJsonValue(m_decimal_digits_precision));
    }
    if (m_mask_first_purchase_data_isSet) {
        obj.insert(QString("maskFirstPurchaseData"), ::OpenAPI::toJsonValue(m_mask_first_purchase_data));
    }
    if (m_max_number_of_white_label_sellers_isSet) {
        obj.insert(QString("maxNumberOfWhiteLabelSellers"), ::OpenAPI::toJsonValue(m_max_number_of_white_label_sellers));
    }
    if (m_minimum_quantity_accumulated_for_items_isSet) {
        obj.insert(QString("minimumQuantityAccumulatedForItems"), ::OpenAPI::toJsonValue(m_minimum_quantity_accumulated_for_items));
    }
    if (m_minimum_value_accumulated_isSet) {
        obj.insert(QString("minimumValueAccumulated"), ::OpenAPI::toJsonValue(m_minimum_value_accumulated));
    }
    if (m_payment_configuration.isSet()) {
        obj.insert(QString("paymentConfiguration"), ::OpenAPI::toJsonValue(m_payment_configuration));
    }
    if (m_payment_system_to_check_first_installment_isSet) {
        obj.insert(QString("paymentSystemToCheckFirstInstallment"), ::OpenAPI::toJsonValue(m_payment_system_to_check_first_installment));
    }
    if (m_recaptcha_validation_isSet) {
        obj.insert(QString("recaptchaValidation"), ::OpenAPI::toJsonValue(m_recaptcha_validation));
    }
    if (m_tax_configuration.isSet()) {
        obj.insert(QString("taxConfiguration"), ::OpenAPI::toJsonValue(m_tax_configuration));
    }
    return obj;
}

bool OAIUpdateorderFormconfigurationRequest::isAllowManualPrice() const {
    return m_allow_manual_price;
}
void OAIUpdateorderFormconfigurationRequest::setAllowManualPrice(const bool &allow_manual_price) {
    m_allow_manual_price = allow_manual_price;
    m_allow_manual_price_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_allow_manual_price_Set() const{
    return m_allow_manual_price_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_allow_manual_price_Valid() const{
    return m_allow_manual_price_isValid;
}

bool OAIUpdateorderFormconfigurationRequest::isAllowMultipleDeliveries() const {
    return m_allow_multiple_deliveries;
}
void OAIUpdateorderFormconfigurationRequest::setAllowMultipleDeliveries(const bool &allow_multiple_deliveries) {
    m_allow_multiple_deliveries = allow_multiple_deliveries;
    m_allow_multiple_deliveries_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_allow_multiple_deliveries_Set() const{
    return m_allow_multiple_deliveries_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_allow_multiple_deliveries_Valid() const{
    return m_allow_multiple_deliveries_isValid;
}

QList<OAIUpdateorderFormconfigurationRequest_apps_inner> OAIUpdateorderFormconfigurationRequest::getApps() const {
    return m_apps;
}
void OAIUpdateorderFormconfigurationRequest::setApps(const QList<OAIUpdateorderFormconfigurationRequest_apps_inner> &apps) {
    m_apps = apps;
    m_apps_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_apps_Set() const{
    return m_apps_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_apps_Valid() const{
    return m_apps_isValid;
}

qint32 OAIUpdateorderFormconfigurationRequest::getDecimalDigitsPrecision() const {
    return m_decimal_digits_precision;
}
void OAIUpdateorderFormconfigurationRequest::setDecimalDigitsPrecision(const qint32 &decimal_digits_precision) {
    m_decimal_digits_precision = decimal_digits_precision;
    m_decimal_digits_precision_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_decimal_digits_precision_Set() const{
    return m_decimal_digits_precision_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_decimal_digits_precision_Valid() const{
    return m_decimal_digits_precision_isValid;
}

bool OAIUpdateorderFormconfigurationRequest::isMaskFirstPurchaseData() const {
    return m_mask_first_purchase_data;
}
void OAIUpdateorderFormconfigurationRequest::setMaskFirstPurchaseData(const bool &mask_first_purchase_data) {
    m_mask_first_purchase_data = mask_first_purchase_data;
    m_mask_first_purchase_data_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_mask_first_purchase_data_Set() const{
    return m_mask_first_purchase_data_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_mask_first_purchase_data_Valid() const{
    return m_mask_first_purchase_data_isValid;
}

qint32 OAIUpdateorderFormconfigurationRequest::getMaxNumberOfWhiteLabelSellers() const {
    return m_max_number_of_white_label_sellers;
}
void OAIUpdateorderFormconfigurationRequest::setMaxNumberOfWhiteLabelSellers(const qint32 &max_number_of_white_label_sellers) {
    m_max_number_of_white_label_sellers = max_number_of_white_label_sellers;
    m_max_number_of_white_label_sellers_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_max_number_of_white_label_sellers_Set() const{
    return m_max_number_of_white_label_sellers_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_max_number_of_white_label_sellers_Valid() const{
    return m_max_number_of_white_label_sellers_isValid;
}

qint32 OAIUpdateorderFormconfigurationRequest::getMinimumQuantityAccumulatedForItems() const {
    return m_minimum_quantity_accumulated_for_items;
}
void OAIUpdateorderFormconfigurationRequest::setMinimumQuantityAccumulatedForItems(const qint32 &minimum_quantity_accumulated_for_items) {
    m_minimum_quantity_accumulated_for_items = minimum_quantity_accumulated_for_items;
    m_minimum_quantity_accumulated_for_items_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_minimum_quantity_accumulated_for_items_Set() const{
    return m_minimum_quantity_accumulated_for_items_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_minimum_quantity_accumulated_for_items_Valid() const{
    return m_minimum_quantity_accumulated_for_items_isValid;
}

qint32 OAIUpdateorderFormconfigurationRequest::getMinimumValueAccumulated() const {
    return m_minimum_value_accumulated;
}
void OAIUpdateorderFormconfigurationRequest::setMinimumValueAccumulated(const qint32 &minimum_value_accumulated) {
    m_minimum_value_accumulated = minimum_value_accumulated;
    m_minimum_value_accumulated_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_minimum_value_accumulated_Set() const{
    return m_minimum_value_accumulated_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_minimum_value_accumulated_Valid() const{
    return m_minimum_value_accumulated_isValid;
}

OAIPaymentConfiguration OAIUpdateorderFormconfigurationRequest::getPaymentConfiguration() const {
    return m_payment_configuration;
}
void OAIUpdateorderFormconfigurationRequest::setPaymentConfiguration(const OAIPaymentConfiguration &payment_configuration) {
    m_payment_configuration = payment_configuration;
    m_payment_configuration_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_payment_configuration_Set() const{
    return m_payment_configuration_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_payment_configuration_Valid() const{
    return m_payment_configuration_isValid;
}

QString OAIUpdateorderFormconfigurationRequest::getPaymentSystemToCheckFirstInstallment() const {
    return m_payment_system_to_check_first_installment;
}
void OAIUpdateorderFormconfigurationRequest::setPaymentSystemToCheckFirstInstallment(const QString &payment_system_to_check_first_installment) {
    m_payment_system_to_check_first_installment = payment_system_to_check_first_installment;
    m_payment_system_to_check_first_installment_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_payment_system_to_check_first_installment_Set() const{
    return m_payment_system_to_check_first_installment_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_payment_system_to_check_first_installment_Valid() const{
    return m_payment_system_to_check_first_installment_isValid;
}

QString OAIUpdateorderFormconfigurationRequest::getRecaptchaValidation() const {
    return m_recaptcha_validation;
}
void OAIUpdateorderFormconfigurationRequest::setRecaptchaValidation(const QString &recaptcha_validation) {
    m_recaptcha_validation = recaptcha_validation;
    m_recaptcha_validation_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_recaptcha_validation_Set() const{
    return m_recaptcha_validation_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_recaptcha_validation_Valid() const{
    return m_recaptcha_validation_isValid;
}

OAIUpdateorderFormconfigurationRequest_taxConfiguration OAIUpdateorderFormconfigurationRequest::getTaxConfiguration() const {
    return m_tax_configuration;
}
void OAIUpdateorderFormconfigurationRequest::setTaxConfiguration(const OAIUpdateorderFormconfigurationRequest_taxConfiguration &tax_configuration) {
    m_tax_configuration = tax_configuration;
    m_tax_configuration_isSet = true;
}

bool OAIUpdateorderFormconfigurationRequest::is_tax_configuration_Set() const{
    return m_tax_configuration_isSet;
}

bool OAIUpdateorderFormconfigurationRequest::is_tax_configuration_Valid() const{
    return m_tax_configuration_isValid;
}

bool OAIUpdateorderFormconfigurationRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_allow_manual_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_allow_multiple_deliveries_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_apps.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_decimal_digits_precision_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mask_first_purchase_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_number_of_white_label_sellers_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_minimum_quantity_accumulated_for_items_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_minimum_value_accumulated_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_configuration.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_system_to_check_first_installment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recaptcha_validation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_configuration.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateorderFormconfigurationRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_allow_manual_price_isValid && m_allow_multiple_deliveries_isValid && m_apps_isValid && m_decimal_digits_precision_isValid && m_minimum_quantity_accumulated_for_items_isValid && m_minimum_value_accumulated_isValid && m_payment_configuration_isValid && m_tax_configuration_isValid && true;
}

} // namespace OpenAPI
