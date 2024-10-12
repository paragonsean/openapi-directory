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

#include "OAIAddCoupons_200_response_items_inner_priceDefinition.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddCoupons_200_response_items_inner_priceDefinition::OAIAddCoupons_200_response_items_inner_priceDefinition(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddCoupons_200_response_items_inner_priceDefinition::OAIAddCoupons_200_response_items_inner_priceDefinition() {
    this->initializeModel();
}

OAIAddCoupons_200_response_items_inner_priceDefinition::~OAIAddCoupons_200_response_items_inner_priceDefinition() {}

void OAIAddCoupons_200_response_items_inner_priceDefinition::initializeModel() {

    m_calculated_selling_price_isSet = false;
    m_calculated_selling_price_isValid = false;

    m_selling_prices_isSet = false;
    m_selling_prices_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;
}

void OAIAddCoupons_200_response_items_inner_priceDefinition::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddCoupons_200_response_items_inner_priceDefinition::fromJsonObject(QJsonObject json) {

    m_calculated_selling_price_isValid = ::OpenAPI::fromJsonValue(m_calculated_selling_price, json[QString("calculatedSellingPrice")]);
    m_calculated_selling_price_isSet = !json[QString("calculatedSellingPrice")].isNull() && m_calculated_selling_price_isValid;

    m_selling_prices_isValid = ::OpenAPI::fromJsonValue(m_selling_prices, json[QString("sellingPrices")]);
    m_selling_prices_isSet = !json[QString("sellingPrices")].isNull() && m_selling_prices_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;
}

QString OAIAddCoupons_200_response_items_inner_priceDefinition::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddCoupons_200_response_items_inner_priceDefinition::asJsonObject() const {
    QJsonObject obj;
    if (m_calculated_selling_price_isSet) {
        obj.insert(QString("calculatedSellingPrice"), ::OpenAPI::toJsonValue(m_calculated_selling_price));
    }
    if (m_selling_prices.size() > 0) {
        obj.insert(QString("sellingPrices"), ::OpenAPI::toJsonValue(m_selling_prices));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    return obj;
}

qint32 OAIAddCoupons_200_response_items_inner_priceDefinition::getCalculatedSellingPrice() const {
    return m_calculated_selling_price;
}
void OAIAddCoupons_200_response_items_inner_priceDefinition::setCalculatedSellingPrice(const qint32 &calculated_selling_price) {
    m_calculated_selling_price = calculated_selling_price;
    m_calculated_selling_price_isSet = true;
}

bool OAIAddCoupons_200_response_items_inner_priceDefinition::is_calculated_selling_price_Set() const{
    return m_calculated_selling_price_isSet;
}

bool OAIAddCoupons_200_response_items_inner_priceDefinition::is_calculated_selling_price_Valid() const{
    return m_calculated_selling_price_isValid;
}

QList<OAIAddCoupons_200_response_items_inner_priceDefinition_sellingPrices_inner> OAIAddCoupons_200_response_items_inner_priceDefinition::getSellingPrices() const {
    return m_selling_prices;
}
void OAIAddCoupons_200_response_items_inner_priceDefinition::setSellingPrices(const QList<OAIAddCoupons_200_response_items_inner_priceDefinition_sellingPrices_inner> &selling_prices) {
    m_selling_prices = selling_prices;
    m_selling_prices_isSet = true;
}

bool OAIAddCoupons_200_response_items_inner_priceDefinition::is_selling_prices_Set() const{
    return m_selling_prices_isSet;
}

bool OAIAddCoupons_200_response_items_inner_priceDefinition::is_selling_prices_Valid() const{
    return m_selling_prices_isValid;
}

qint32 OAIAddCoupons_200_response_items_inner_priceDefinition::getTotal() const {
    return m_total;
}
void OAIAddCoupons_200_response_items_inner_priceDefinition::setTotal(const qint32 &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIAddCoupons_200_response_items_inner_priceDefinition::is_total_Set() const{
    return m_total_isSet;
}

bool OAIAddCoupons_200_response_items_inner_priceDefinition::is_total_Valid() const{
    return m_total_isValid;
}

bool OAIAddCoupons_200_response_items_inner_priceDefinition::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_calculated_selling_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_selling_prices.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddCoupons_200_response_items_inner_priceDefinition::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
