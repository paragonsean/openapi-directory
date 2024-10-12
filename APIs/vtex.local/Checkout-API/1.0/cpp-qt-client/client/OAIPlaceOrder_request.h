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
 * OAIPlaceOrder_request.h
 *
 * 
 */

#ifndef OAIPlaceOrder_request_H
#define OAIPlaceOrder_request_H

#include <QJsonObject>

#include "OAIAddMerchantContextData_request_salesAssociateData.h"
#include "OAIPlaceOrder_request_clientProfileData.h"
#include "OAIPlaceOrder_request_items_inner.h"
#include "OAIPlaceOrder_request_marketingData.h"
#include "OAIPlaceOrder_request_paymentData.h"
#include "OAIPlaceOrder_request_shippingData.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPlaceOrder_request_clientProfileData;
class OAIPlaceOrder_request_items_inner;
class OAIPlaceOrder_request_marketingData;
class OAIPlaceOrder_request_paymentData;
class OAIAddMerchantContextData_request_salesAssociateData;
class OAIPlaceOrder_request_shippingData;

class OAIPlaceOrder_request : public OAIObject {
public:
    OAIPlaceOrder_request();
    OAIPlaceOrder_request(QString json);
    ~OAIPlaceOrder_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPlaceOrder_request_clientProfileData getClientProfileData() const;
    void setClientProfileData(const OAIPlaceOrder_request_clientProfileData &client_profile_data);
    bool is_client_profile_data_Set() const;
    bool is_client_profile_data_Valid() const;

    QList<OAIPlaceOrder_request_items_inner> getItems() const;
    void setItems(const QList<OAIPlaceOrder_request_items_inner> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    OAIPlaceOrder_request_marketingData getMarketingData() const;
    void setMarketingData(const OAIPlaceOrder_request_marketingData &marketing_data);
    bool is_marketing_data_Set() const;
    bool is_marketing_data_Valid() const;

    QString getOpenTextField() const;
    void setOpenTextField(const QString &open_text_field);
    bool is_open_text_field_Set() const;
    bool is_open_text_field_Valid() const;

    OAIPlaceOrder_request_paymentData getPaymentData() const;
    void setPaymentData(const OAIPlaceOrder_request_paymentData &payment_data);
    bool is_payment_data_Set() const;
    bool is_payment_data_Valid() const;

    OAIAddMerchantContextData_request_salesAssociateData getSalesAssociateData() const;
    void setSalesAssociateData(const OAIAddMerchantContextData_request_salesAssociateData &sales_associate_data);
    bool is_sales_associate_data_Set() const;
    bool is_sales_associate_data_Valid() const;

    OAIPlaceOrder_request_shippingData getShippingData() const;
    void setShippingData(const OAIPlaceOrder_request_shippingData &shipping_data);
    bool is_shipping_data_Set() const;
    bool is_shipping_data_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPlaceOrder_request_clientProfileData m_client_profile_data;
    bool m_client_profile_data_isSet;
    bool m_client_profile_data_isValid;

    QList<OAIPlaceOrder_request_items_inner> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    OAIPlaceOrder_request_marketingData m_marketing_data;
    bool m_marketing_data_isSet;
    bool m_marketing_data_isValid;

    QString m_open_text_field;
    bool m_open_text_field_isSet;
    bool m_open_text_field_isValid;

    OAIPlaceOrder_request_paymentData m_payment_data;
    bool m_payment_data_isSet;
    bool m_payment_data_isValid;

    OAIAddMerchantContextData_request_salesAssociateData m_sales_associate_data;
    bool m_sales_associate_data_isSet;
    bool m_sales_associate_data_isValid;

    OAIPlaceOrder_request_shippingData m_shipping_data;
    bool m_shipping_data_isSet;
    bool m_shipping_data_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlaceOrder_request)

#endif // OAIPlaceOrder_request_H
