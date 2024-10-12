/**
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIOrderFields.h
 *
 * 
 */

#ifndef OAIOrderFields_H
#define OAIOrderFields_H

#include <QJsonObject>

#include "OAICustomer.h"
#include "OAIOrderAdditionalFields.h"
#include "OAIOrderBillingAddress.h"
#include "OAIOrderProduct.h"
#include "OAIOrderShippingAddress.h"
#include "OAIOrderShippingTax.h"
#include "OAITrafficSource.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIOrderAdditionalFields;
class OAIOrderBillingAddress;
class OAICustomer;
class OAIOrderProduct;
class OAIOrderShippingAddress;
class OAIOrderShippingTax;
class OAITrafficSource;

class OAIOrderFields : public OAIObject {
public:
    OAIOrderFields();
    OAIOrderFields(QString json);
    ~OAIOrderFields() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIOrderAdditionalFields> getAdditionalFields() const;
    void setAdditionalFields(const QList<OAIOrderAdditionalFields> &additional_fields);
    bool is_additional_fields_Set() const;
    bool is_additional_fields_Valid() const;

    QString getAdditionalInformation() const;
    void setAdditionalInformation(const QString &additional_information);
    bool is_additional_information_Set() const;
    bool is_additional_information_Valid() const;

    OAIOrderBillingAddress getBillingAddress() const;
    void setBillingAddress(const OAIOrderBillingAddress &billing_address);
    bool is_billing_address_Set() const;
    bool is_billing_address_Valid() const;

    QString getCheckoutUrl() const;
    void setCheckoutUrl(const QString &checkout_url);
    bool is_checkout_url_Set() const;
    bool is_checkout_url_Valid() const;

    QString getCoupons() const;
    void setCoupons(const QString &coupons);
    bool is_coupons_Set() const;
    bool is_coupons_Valid() const;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getCurrency() const;
    void setCurrency(const QString &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    OAICustomer getCustomer() const;
    void setCustomer(const OAICustomer &customer);
    bool is_customer_Set() const;
    bool is_customer_Valid() const;

    float getDiscount() const;
    void setDiscount(const float &discount);
    bool is_discount_Set() const;
    bool is_discount_Valid() const;

    QString getDuplicateUrl() const;
    void setDuplicateUrl(const QString &duplicate_url);
    bool is_duplicate_url_Set() const;
    bool is_duplicate_url_Valid() const;

    QString getExternalShippingRateId() const;
    void setExternalShippingRateId(const QString &external_shipping_rate_id);
    bool is_external_shipping_rate_id_Set() const;
    bool is_external_shipping_rate_id_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QString getPaymentInformation() const;
    void setPaymentInformation(const QString &payment_information);
    bool is_payment_information_Set() const;
    bool is_payment_information_Valid() const;

    QString getPaymentMethodName() const;
    void setPaymentMethodName(const QString &payment_method_name);
    bool is_payment_method_name_Set() const;
    bool is_payment_method_name_Valid() const;

    QString getPaymentMethodType() const;
    void setPaymentMethodType(const QString &payment_method_type);
    bool is_payment_method_type_Set() const;
    bool is_payment_method_type_Valid() const;

    QList<OAIOrderProduct> getProducts() const;
    void setProducts(const QList<OAIOrderProduct> &products);
    bool is_products_Set() const;
    bool is_products_Valid() const;

    QString getRecoveryUrl() const;
    void setRecoveryUrl(const QString &recovery_url);
    bool is_recovery_url_Set() const;
    bool is_recovery_url_Valid() const;

    QString getShipmentStatus() const;
    void setShipmentStatus(const QString &shipment_status);
    bool is_shipment_status_Set() const;
    bool is_shipment_status_Valid() const;

    float getShipping() const;
    void setShipping(const float &shipping);
    bool is_shipping_Set() const;
    bool is_shipping_Valid() const;

    OAIOrderShippingAddress getShippingAddress() const;
    void setShippingAddress(const OAIOrderShippingAddress &shipping_address);
    bool is_shipping_address_Set() const;
    bool is_shipping_address_Valid() const;

    float getShippingDiscount() const;
    void setShippingDiscount(const float &shipping_discount);
    bool is_shipping_discount_Set() const;
    bool is_shipping_discount_Valid() const;

    qint32 getShippingMethodId() const;
    void setShippingMethodId(const qint32 &shipping_method_id);
    bool is_shipping_method_id_Set() const;
    bool is_shipping_method_id_Valid() const;

    QString getShippingMethodName() const;
    void setShippingMethodName(const QString &shipping_method_name);
    bool is_shipping_method_name_Set() const;
    bool is_shipping_method_name_Valid() const;

    QString getShippingOption() const;
    void setShippingOption(const QString &shipping_option);
    bool is_shipping_option_Set() const;
    bool is_shipping_option_Valid() const;

    bool isShippingRequired() const;
    void setShippingRequired(const bool &shipping_required);
    bool is_shipping_required_Set() const;
    bool is_shipping_required_Valid() const;

    float getShippingTax() const;
    void setShippingTax(const float &shipping_tax);
    bool is_shipping_tax_Set() const;
    bool is_shipping_tax_Valid() const;

    QList<OAIOrderShippingTax> getShippingTaxes() const;
    void setShippingTaxes(const QList<OAIOrderShippingTax> &shipping_taxes);
    bool is_shipping_taxes_Set() const;
    bool is_shipping_taxes_Valid() const;

    OAITrafficSource getSource() const;
    void setSource(const OAITrafficSource &source);
    bool is_source_Set() const;
    bool is_source_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    float getSubtotal() const;
    void setSubtotal(const float &subtotal);
    bool is_subtotal_Set() const;
    bool is_subtotal_Valid() const;

    float getTax() const;
    void setTax(const float &tax);
    bool is_tax_Set() const;
    bool is_tax_Valid() const;

    float getTotal() const;
    void setTotal(const float &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    QString getTrackingCompany() const;
    void setTrackingCompany(const QString &tracking_company);
    bool is_tracking_company_Set() const;
    bool is_tracking_company_Valid() const;

    QString getTrackingNumber() const;
    void setTrackingNumber(const QString &tracking_number);
    bool is_tracking_number_Set() const;
    bool is_tracking_number_Valid() const;

    QString getTrackingUrl() const;
    void setTrackingUrl(const QString &tracking_url);
    bool is_tracking_url_Set() const;
    bool is_tracking_url_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIOrderAdditionalFields> m_additional_fields;
    bool m_additional_fields_isSet;
    bool m_additional_fields_isValid;

    QString m_additional_information;
    bool m_additional_information_isSet;
    bool m_additional_information_isValid;

    OAIOrderBillingAddress m_billing_address;
    bool m_billing_address_isSet;
    bool m_billing_address_isValid;

    QString m_checkout_url;
    bool m_checkout_url_isSet;
    bool m_checkout_url_isValid;

    QString m_coupons;
    bool m_coupons_isSet;
    bool m_coupons_isValid;

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    OAICustomer m_customer;
    bool m_customer_isSet;
    bool m_customer_isValid;

    float m_discount;
    bool m_discount_isSet;
    bool m_discount_isValid;

    QString m_duplicate_url;
    bool m_duplicate_url_isSet;
    bool m_duplicate_url_isValid;

    QString m_external_shipping_rate_id;
    bool m_external_shipping_rate_id_isSet;
    bool m_external_shipping_rate_id_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QString m_payment_information;
    bool m_payment_information_isSet;
    bool m_payment_information_isValid;

    QString m_payment_method_name;
    bool m_payment_method_name_isSet;
    bool m_payment_method_name_isValid;

    QString m_payment_method_type;
    bool m_payment_method_type_isSet;
    bool m_payment_method_type_isValid;

    QList<OAIOrderProduct> m_products;
    bool m_products_isSet;
    bool m_products_isValid;

    QString m_recovery_url;
    bool m_recovery_url_isSet;
    bool m_recovery_url_isValid;

    QString m_shipment_status;
    bool m_shipment_status_isSet;
    bool m_shipment_status_isValid;

    float m_shipping;
    bool m_shipping_isSet;
    bool m_shipping_isValid;

    OAIOrderShippingAddress m_shipping_address;
    bool m_shipping_address_isSet;
    bool m_shipping_address_isValid;

    float m_shipping_discount;
    bool m_shipping_discount_isSet;
    bool m_shipping_discount_isValid;

    qint32 m_shipping_method_id;
    bool m_shipping_method_id_isSet;
    bool m_shipping_method_id_isValid;

    QString m_shipping_method_name;
    bool m_shipping_method_name_isSet;
    bool m_shipping_method_name_isValid;

    QString m_shipping_option;
    bool m_shipping_option_isSet;
    bool m_shipping_option_isValid;

    bool m_shipping_required;
    bool m_shipping_required_isSet;
    bool m_shipping_required_isValid;

    float m_shipping_tax;
    bool m_shipping_tax_isSet;
    bool m_shipping_tax_isValid;

    QList<OAIOrderShippingTax> m_shipping_taxes;
    bool m_shipping_taxes_isSet;
    bool m_shipping_taxes_isValid;

    OAITrafficSource m_source;
    bool m_source_isSet;
    bool m_source_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    float m_subtotal;
    bool m_subtotal_isSet;
    bool m_subtotal_isValid;

    float m_tax;
    bool m_tax_isSet;
    bool m_tax_isValid;

    float m_total;
    bool m_total_isSet;
    bool m_total_isValid;

    QString m_tracking_company;
    bool m_tracking_company_isSet;
    bool m_tracking_company_isValid;

    QString m_tracking_number;
    bool m_tracking_number_isSet;
    bool m_tracking_number_isValid;

    QString m_tracking_url;
    bool m_tracking_url_isSet;
    bool m_tracking_url_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIOrderFields)

#endif // OAIOrderFields_H
