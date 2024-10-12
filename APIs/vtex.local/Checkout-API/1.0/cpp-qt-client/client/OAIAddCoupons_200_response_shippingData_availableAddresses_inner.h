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
 * OAIAddCoupons_200_response_shippingData_availableAddresses_inner.h
 *
 * 
 */

#ifndef OAIAddCoupons_200_response_shippingData_availableAddresses_inner_H
#define OAIAddCoupons_200_response_shippingData_availableAddresses_inner_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAddCoupons_200_response_shippingData_availableAddresses_inner : public OAIObject {
public:
    OAIAddCoupons_200_response_shippingData_availableAddresses_inner();
    OAIAddCoupons_200_response_shippingData_availableAddresses_inner(QString json);
    ~OAIAddCoupons_200_response_shippingData_availableAddresses_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAddressId() const;
    void setAddressId(const QString &address_id);
    bool is_address_id_Set() const;
    bool is_address_id_Valid() const;

    QString getAddressType() const;
    void setAddressType(const QString &address_type);
    bool is_address_type_Set() const;
    bool is_address_type_Valid() const;

    QString getCity() const;
    void setCity(const QString &city);
    bool is_city_Set() const;
    bool is_city_Valid() const;

    QString getComplement() const;
    void setComplement(const QString &complement);
    bool is_complement_Set() const;
    bool is_complement_Valid() const;

    QString getCountry() const;
    void setCountry(const QString &country);
    bool is_country_Set() const;
    bool is_country_Valid() const;

    QList<double> getGeoCoordinates() const;
    void setGeoCoordinates(const QList<double> &geo_coordinates);
    bool is_geo_coordinates_Set() const;
    bool is_geo_coordinates_Valid() const;

    bool isIsDisposable() const;
    void setIsDisposable(const bool &is_disposable);
    bool is_is_disposable_Set() const;
    bool is_is_disposable_Valid() const;

    QString getNeighborhood() const;
    void setNeighborhood(const QString &neighborhood);
    bool is_neighborhood_Set() const;
    bool is_neighborhood_Valid() const;

    QString getNumber() const;
    void setNumber(const QString &number);
    bool is_number_Set() const;
    bool is_number_Valid() const;

    QString getPostalCode() const;
    void setPostalCode(const QString &postal_code);
    bool is_postal_code_Set() const;
    bool is_postal_code_Valid() const;

    QString getReceiverName() const;
    void setReceiverName(const QString &receiver_name);
    bool is_receiver_name_Set() const;
    bool is_receiver_name_Valid() const;

    QString getReference() const;
    void setReference(const QString &reference);
    bool is_reference_Set() const;
    bool is_reference_Valid() const;

    QString getState() const;
    void setState(const QString &state);
    bool is_state_Set() const;
    bool is_state_Valid() const;

    QString getStreet() const;
    void setStreet(const QString &street);
    bool is_street_Set() const;
    bool is_street_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_address_id;
    bool m_address_id_isSet;
    bool m_address_id_isValid;

    QString m_address_type;
    bool m_address_type_isSet;
    bool m_address_type_isValid;

    QString m_city;
    bool m_city_isSet;
    bool m_city_isValid;

    QString m_complement;
    bool m_complement_isSet;
    bool m_complement_isValid;

    QString m_country;
    bool m_country_isSet;
    bool m_country_isValid;

    QList<double> m_geo_coordinates;
    bool m_geo_coordinates_isSet;
    bool m_geo_coordinates_isValid;

    bool m_is_disposable;
    bool m_is_disposable_isSet;
    bool m_is_disposable_isValid;

    QString m_neighborhood;
    bool m_neighborhood_isSet;
    bool m_neighborhood_isValid;

    QString m_number;
    bool m_number_isSet;
    bool m_number_isValid;

    QString m_postal_code;
    bool m_postal_code_isSet;
    bool m_postal_code_isValid;

    QString m_receiver_name;
    bool m_receiver_name_isSet;
    bool m_receiver_name_isValid;

    QString m_reference;
    bool m_reference_isSet;
    bool m_reference_isValid;

    QString m_state;
    bool m_state_isSet;
    bool m_state_isValid;

    QString m_street;
    bool m_street_isSet;
    bool m_street_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAddCoupons_200_response_shippingData_availableAddresses_inner)

#endif // OAIAddCoupons_200_response_shippingData_availableAddresses_inner_H
