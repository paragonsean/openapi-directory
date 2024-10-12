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
 * OAIPlaceOrder_request_items_inner.h
 *
 * 
 */

#ifndef OAIPlaceOrder_request_items_inner_H
#define OAIPlaceOrder_request_items_inner_H

#include <QJsonObject>

#include "OAIPlaceOrder_request_items_inner_bundleItems_inner.h"
#include "OAIPlaceOrder_request_items_inner_itemAttachment.h"
#include "OAIPlaceOrder_request_items_inner_priceTags_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPlaceOrder_request_items_inner_bundleItems_inner;
class OAIPlaceOrder_request_items_inner_itemAttachment;
class OAIPlaceOrder_request_items_inner_priceTags_inner;

class OAIPlaceOrder_request_items_inner : public OAIObject {
public:
    OAIPlaceOrder_request_items_inner();
    OAIPlaceOrder_request_items_inner(QString json);
    ~OAIPlaceOrder_request_items_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QString> getAttachments() const;
    void setAttachments(const QList<QString> &attachments);
    bool is_attachments_Set() const;
    bool is_attachments_Valid() const;

    QList<OAIPlaceOrder_request_items_inner_bundleItems_inner> getBundleItems() const;
    void setBundleItems(const QList<OAIPlaceOrder_request_items_inner_bundleItems_inner> &bundle_items);
    bool is_bundle_items_Set() const;
    bool is_bundle_items_Valid() const;

    qint32 getCommission() const;
    void setCommission(const qint32 &commission);
    bool is_commission_Set() const;
    bool is_commission_Valid() const;

    qint32 getFreightCommission() const;
    void setFreightCommission(const qint32 &freight_commission);
    bool is_freight_commission_Set() const;
    bool is_freight_commission_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsGift() const;
    void setIsGift(const bool &is_gift);
    bool is_is_gift_Set() const;
    bool is_is_gift_Valid() const;

    OAIPlaceOrder_request_items_inner_itemAttachment getItemAttachment() const;
    void setItemAttachment(const OAIPlaceOrder_request_items_inner_itemAttachment &item_attachment);
    bool is_item_attachment_Set() const;
    bool is_item_attachment_Valid() const;

    QString getMeasurementUnit() const;
    void setMeasurementUnit(const QString &measurement_unit);
    bool is_measurement_unit_Set() const;
    bool is_measurement_unit_Valid() const;

    qint32 getPrice() const;
    void setPrice(const qint32 &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QList<OAIPlaceOrder_request_items_inner_priceTags_inner> getPriceTags() const;
    void setPriceTags(const QList<OAIPlaceOrder_request_items_inner_priceTags_inner> &price_tags);
    bool is_price_tags_Set() const;
    bool is_price_tags_Valid() const;

    qint32 getQuantity() const;
    void setQuantity(const qint32 &quantity);
    bool is_quantity_Set() const;
    bool is_quantity_Valid() const;

    QString getSeller() const;
    void setSeller(const QString &seller);
    bool is_seller_Set() const;
    bool is_seller_Valid() const;

    qint32 getUnitMultiplier() const;
    void setUnitMultiplier(const qint32 &unit_multiplier);
    bool is_unit_multiplier_Set() const;
    bool is_unit_multiplier_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QString> m_attachments;
    bool m_attachments_isSet;
    bool m_attachments_isValid;

    QList<OAIPlaceOrder_request_items_inner_bundleItems_inner> m_bundle_items;
    bool m_bundle_items_isSet;
    bool m_bundle_items_isValid;

    qint32 m_commission;
    bool m_commission_isSet;
    bool m_commission_isValid;

    qint32 m_freight_commission;
    bool m_freight_commission_isSet;
    bool m_freight_commission_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_gift;
    bool m_is_gift_isSet;
    bool m_is_gift_isValid;

    OAIPlaceOrder_request_items_inner_itemAttachment m_item_attachment;
    bool m_item_attachment_isSet;
    bool m_item_attachment_isValid;

    QString m_measurement_unit;
    bool m_measurement_unit_isSet;
    bool m_measurement_unit_isValid;

    qint32 m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QList<OAIPlaceOrder_request_items_inner_priceTags_inner> m_price_tags;
    bool m_price_tags_isSet;
    bool m_price_tags_isValid;

    qint32 m_quantity;
    bool m_quantity_isSet;
    bool m_quantity_isValid;

    QString m_seller;
    bool m_seller_isSet;
    bool m_seller_isValid;

    qint32 m_unit_multiplier;
    bool m_unit_multiplier_isSet;
    bool m_unit_multiplier_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlaceOrder_request_items_inner)

#endif // OAIPlaceOrder_request_items_inner_H
