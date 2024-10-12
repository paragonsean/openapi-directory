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

#include "OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address() {
    this->initializeModel();
}

OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::~OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address() {}

void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::initializeModel() {

    m_address_type_isSet = false;
    m_address_type_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_complement_isSet = false;
    m_complement_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_geo_coordinates_isSet = false;
    m_geo_coordinates_isValid = false;

    m_neighborhood_isSet = false;
    m_neighborhood_isValid = false;

    m_number_isSet = false;
    m_number_isValid = false;

    m_postal_code_isSet = false;
    m_postal_code_isValid = false;

    m_reference_isSet = false;
    m_reference_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_street_isSet = false;
    m_street_isValid = false;
}

void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::fromJsonObject(QJsonObject json) {

    m_address_type_isValid = ::OpenAPI::fromJsonValue(m_address_type, json[QString("addressType")]);
    m_address_type_isSet = !json[QString("addressType")].isNull() && m_address_type_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_complement_isValid = ::OpenAPI::fromJsonValue(m_complement, json[QString("complement")]);
    m_complement_isSet = !json[QString("complement")].isNull() && m_complement_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_geo_coordinates_isValid = ::OpenAPI::fromJsonValue(m_geo_coordinates, json[QString("geoCoordinates")]);
    m_geo_coordinates_isSet = !json[QString("geoCoordinates")].isNull() && m_geo_coordinates_isValid;

    m_neighborhood_isValid = ::OpenAPI::fromJsonValue(m_neighborhood, json[QString("neighborhood")]);
    m_neighborhood_isSet = !json[QString("neighborhood")].isNull() && m_neighborhood_isValid;

    m_number_isValid = ::OpenAPI::fromJsonValue(m_number, json[QString("number")]);
    m_number_isSet = !json[QString("number")].isNull() && m_number_isValid;

    m_postal_code_isValid = ::OpenAPI::fromJsonValue(m_postal_code, json[QString("postalCode")]);
    m_postal_code_isSet = !json[QString("postalCode")].isNull() && m_postal_code_isValid;

    m_reference_isValid = ::OpenAPI::fromJsonValue(m_reference, json[QString("reference")]);
    m_reference_isSet = !json[QString("reference")].isNull() && m_reference_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_street_isValid = ::OpenAPI::fromJsonValue(m_street, json[QString("street")]);
    m_street_isSet = !json[QString("street")].isNull() && m_street_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::asJsonObject() const {
    QJsonObject obj;
    if (m_address_type_isSet) {
        obj.insert(QString("addressType"), ::OpenAPI::toJsonValue(m_address_type));
    }
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_complement_isSet) {
        obj.insert(QString("complement"), ::OpenAPI::toJsonValue(m_complement));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_geo_coordinates.size() > 0) {
        obj.insert(QString("geoCoordinates"), ::OpenAPI::toJsonValue(m_geo_coordinates));
    }
    if (m_neighborhood_isSet) {
        obj.insert(QString("neighborhood"), ::OpenAPI::toJsonValue(m_neighborhood));
    }
    if (m_number_isSet) {
        obj.insert(QString("number"), ::OpenAPI::toJsonValue(m_number));
    }
    if (m_postal_code_isSet) {
        obj.insert(QString("postalCode"), ::OpenAPI::toJsonValue(m_postal_code));
    }
    if (m_reference_isSet) {
        obj.insert(QString("reference"), ::OpenAPI::toJsonValue(m_reference));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_street_isSet) {
        obj.insert(QString("street"), ::OpenAPI::toJsonValue(m_street));
    }
    return obj;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::getAddressType() const {
    return m_address_type;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::setAddressType(const QString &address_type) {
    m_address_type = address_type;
    m_address_type_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_address_type_Set() const{
    return m_address_type_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_address_type_Valid() const{
    return m_address_type_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::getCity() const {
    return m_city;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_city_Set() const{
    return m_city_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::getComplement() const {
    return m_complement;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::setComplement(const QString &complement) {
    m_complement = complement;
    m_complement_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_complement_Set() const{
    return m_complement_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_complement_Valid() const{
    return m_complement_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::getCountry() const {
    return m_country;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_country_Set() const{
    return m_country_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_country_Valid() const{
    return m_country_isValid;
}

QList<QString> OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::getGeoCoordinates() const {
    return m_geo_coordinates;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::setGeoCoordinates(const QList<QString> &geo_coordinates) {
    m_geo_coordinates = geo_coordinates;
    m_geo_coordinates_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_geo_coordinates_Set() const{
    return m_geo_coordinates_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_geo_coordinates_Valid() const{
    return m_geo_coordinates_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::getNeighborhood() const {
    return m_neighborhood;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::setNeighborhood(const QString &neighborhood) {
    m_neighborhood = neighborhood;
    m_neighborhood_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_neighborhood_Set() const{
    return m_neighborhood_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_neighborhood_Valid() const{
    return m_neighborhood_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::getNumber() const {
    return m_number;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::setNumber(const QString &number) {
    m_number = number;
    m_number_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_number_Set() const{
    return m_number_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_number_Valid() const{
    return m_number_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::getPostalCode() const {
    return m_postal_code;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::setPostalCode(const QString &postal_code) {
    m_postal_code = postal_code;
    m_postal_code_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_postal_code_Set() const{
    return m_postal_code_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_postal_code_Valid() const{
    return m_postal_code_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::getReference() const {
    return m_reference;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::setReference(const QString &reference) {
    m_reference = reference;
    m_reference_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_reference_Set() const{
    return m_reference_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_reference_Valid() const{
    return m_reference_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::getState() const {
    return m_state;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_state_Set() const{
    return m_state_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::getStreet() const {
    return m_street;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::setStreet(const QString &street) {
    m_street = street;
    m_street_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_street_Set() const{
    return m_street_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::is_street_Valid() const{
    return m_street_isValid;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_complement_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_geo_coordinates.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_neighborhood_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postal_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo_address::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
