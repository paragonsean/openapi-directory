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
 * OAIItemsUpdate_200_response_shippingData.h
 *
 * Shipping information pertinent to the order.
 */

#ifndef OAIItemsUpdate_200_response_shippingData_H
#define OAIItemsUpdate_200_response_shippingData_H

#include <QJsonObject>

#include "OAIItemsUpdate_200_response_shippingData_address.h"
#include "OAIItemsUpdate_200_response_shippingData_availableAddresses_inner.h"
#include "OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIItemsUpdate_200_response_shippingData_address;
class OAIItemsUpdate_200_response_shippingData_availableAddresses_inner;
class OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner;

class OAIItemsUpdate_200_response_shippingData : public OAIObject {
public:
    OAIItemsUpdate_200_response_shippingData();
    OAIItemsUpdate_200_response_shippingData(QString json);
    ~OAIItemsUpdate_200_response_shippingData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIItemsUpdate_200_response_shippingData_address getAddress() const;
    void setAddress(const OAIItemsUpdate_200_response_shippingData_address &address);
    bool is_address_Set() const;
    bool is_address_Valid() const;

    QList<OAIItemsUpdate_200_response_shippingData_availableAddresses_inner> getAvailableAddresses() const;
    void setAvailableAddresses(const QList<OAIItemsUpdate_200_response_shippingData_availableAddresses_inner> &available_addresses);
    bool is_available_addresses_Set() const;
    bool is_available_addresses_Valid() const;

    QList<OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner> getLogisticsInfo() const;
    void setLogisticsInfo(const QList<OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner> &logistics_info);
    bool is_logistics_info_Set() const;
    bool is_logistics_info_Valid() const;

    QList<OAIItemsUpdate_200_response_shippingData_availableAddresses_inner> getSelectedAddresses() const;
    void setSelectedAddresses(const QList<OAIItemsUpdate_200_response_shippingData_availableAddresses_inner> &selected_addresses);
    bool is_selected_addresses_Set() const;
    bool is_selected_addresses_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIItemsUpdate_200_response_shippingData_address m_address;
    bool m_address_isSet;
    bool m_address_isValid;

    QList<OAIItemsUpdate_200_response_shippingData_availableAddresses_inner> m_available_addresses;
    bool m_available_addresses_isSet;
    bool m_available_addresses_isValid;

    QList<OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner> m_logistics_info;
    bool m_logistics_info_isSet;
    bool m_logistics_info_isValid;

    QList<OAIItemsUpdate_200_response_shippingData_availableAddresses_inner> m_selected_addresses;
    bool m_selected_addresses_isSet;
    bool m_selected_addresses_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIItemsUpdate_200_response_shippingData)

#endif // OAIItemsUpdate_200_response_shippingData_H
