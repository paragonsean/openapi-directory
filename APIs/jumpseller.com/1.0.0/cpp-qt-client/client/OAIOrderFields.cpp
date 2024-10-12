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

#include "OAIOrderFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrderFields::OAIOrderFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrderFields::OAIOrderFields() {
    this->initializeModel();
}

OAIOrderFields::~OAIOrderFields() {}

void OAIOrderFields::initializeModel() {

    m_additional_fields_isSet = false;
    m_additional_fields_isValid = false;

    m_additional_information_isSet = false;
    m_additional_information_isValid = false;

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_checkout_url_isSet = false;
    m_checkout_url_isValid = false;

    m_coupons_isSet = false;
    m_coupons_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_customer_isSet = false;
    m_customer_isValid = false;

    m_discount_isSet = false;
    m_discount_isValid = false;

    m_duplicate_url_isSet = false;
    m_duplicate_url_isValid = false;

    m_external_shipping_rate_id_isSet = false;
    m_external_shipping_rate_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_payment_information_isSet = false;
    m_payment_information_isValid = false;

    m_payment_method_name_isSet = false;
    m_payment_method_name_isValid = false;

    m_payment_method_type_isSet = false;
    m_payment_method_type_isValid = false;

    m_products_isSet = false;
    m_products_isValid = false;

    m_recovery_url_isSet = false;
    m_recovery_url_isValid = false;

    m_shipment_status_isSet = false;
    m_shipment_status_isValid = false;

    m_shipping_isSet = false;
    m_shipping_isValid = false;

    m_shipping_address_isSet = false;
    m_shipping_address_isValid = false;

    m_shipping_discount_isSet = false;
    m_shipping_discount_isValid = false;

    m_shipping_method_id_isSet = false;
    m_shipping_method_id_isValid = false;

    m_shipping_method_name_isSet = false;
    m_shipping_method_name_isValid = false;

    m_shipping_option_isSet = false;
    m_shipping_option_isValid = false;

    m_shipping_required_isSet = false;
    m_shipping_required_isValid = false;

    m_shipping_tax_isSet = false;
    m_shipping_tax_isValid = false;

    m_shipping_taxes_isSet = false;
    m_shipping_taxes_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_subtotal_isSet = false;
    m_subtotal_isValid = false;

    m_tax_isSet = false;
    m_tax_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;

    m_tracking_company_isSet = false;
    m_tracking_company_isValid = false;

    m_tracking_number_isSet = false;
    m_tracking_number_isValid = false;

    m_tracking_url_isSet = false;
    m_tracking_url_isValid = false;
}

void OAIOrderFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrderFields::fromJsonObject(QJsonObject json) {

    m_additional_fields_isValid = ::OpenAPI::fromJsonValue(m_additional_fields, json[QString("additional_fields")]);
    m_additional_fields_isSet = !json[QString("additional_fields")].isNull() && m_additional_fields_isValid;

    m_additional_information_isValid = ::OpenAPI::fromJsonValue(m_additional_information, json[QString("additional_information")]);
    m_additional_information_isSet = !json[QString("additional_information")].isNull() && m_additional_information_isValid;

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billing_address")]);
    m_billing_address_isSet = !json[QString("billing_address")].isNull() && m_billing_address_isValid;

    m_checkout_url_isValid = ::OpenAPI::fromJsonValue(m_checkout_url, json[QString("checkout_url")]);
    m_checkout_url_isSet = !json[QString("checkout_url")].isNull() && m_checkout_url_isValid;

    m_coupons_isValid = ::OpenAPI::fromJsonValue(m_coupons, json[QString("coupons")]);
    m_coupons_isSet = !json[QString("coupons")].isNull() && m_coupons_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_customer_isValid = ::OpenAPI::fromJsonValue(m_customer, json[QString("customer")]);
    m_customer_isSet = !json[QString("customer")].isNull() && m_customer_isValid;

    m_discount_isValid = ::OpenAPI::fromJsonValue(m_discount, json[QString("discount")]);
    m_discount_isSet = !json[QString("discount")].isNull() && m_discount_isValid;

    m_duplicate_url_isValid = ::OpenAPI::fromJsonValue(m_duplicate_url, json[QString("duplicate_url")]);
    m_duplicate_url_isSet = !json[QString("duplicate_url")].isNull() && m_duplicate_url_isValid;

    m_external_shipping_rate_id_isValid = ::OpenAPI::fromJsonValue(m_external_shipping_rate_id, json[QString("external_shipping_rate_id")]);
    m_external_shipping_rate_id_isSet = !json[QString("external_shipping_rate_id")].isNull() && m_external_shipping_rate_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_payment_information_isValid = ::OpenAPI::fromJsonValue(m_payment_information, json[QString("payment_information")]);
    m_payment_information_isSet = !json[QString("payment_information")].isNull() && m_payment_information_isValid;

    m_payment_method_name_isValid = ::OpenAPI::fromJsonValue(m_payment_method_name, json[QString("payment_method_name")]);
    m_payment_method_name_isSet = !json[QString("payment_method_name")].isNull() && m_payment_method_name_isValid;

    m_payment_method_type_isValid = ::OpenAPI::fromJsonValue(m_payment_method_type, json[QString("payment_method_type")]);
    m_payment_method_type_isSet = !json[QString("payment_method_type")].isNull() && m_payment_method_type_isValid;

    m_products_isValid = ::OpenAPI::fromJsonValue(m_products, json[QString("products")]);
    m_products_isSet = !json[QString("products")].isNull() && m_products_isValid;

    m_recovery_url_isValid = ::OpenAPI::fromJsonValue(m_recovery_url, json[QString("recovery_url")]);
    m_recovery_url_isSet = !json[QString("recovery_url")].isNull() && m_recovery_url_isValid;

    m_shipment_status_isValid = ::OpenAPI::fromJsonValue(m_shipment_status, json[QString("shipment_status")]);
    m_shipment_status_isSet = !json[QString("shipment_status")].isNull() && m_shipment_status_isValid;

    m_shipping_isValid = ::OpenAPI::fromJsonValue(m_shipping, json[QString("shipping")]);
    m_shipping_isSet = !json[QString("shipping")].isNull() && m_shipping_isValid;

    m_shipping_address_isValid = ::OpenAPI::fromJsonValue(m_shipping_address, json[QString("shipping_address")]);
    m_shipping_address_isSet = !json[QString("shipping_address")].isNull() && m_shipping_address_isValid;

    m_shipping_discount_isValid = ::OpenAPI::fromJsonValue(m_shipping_discount, json[QString("shipping_discount")]);
    m_shipping_discount_isSet = !json[QString("shipping_discount")].isNull() && m_shipping_discount_isValid;

    m_shipping_method_id_isValid = ::OpenAPI::fromJsonValue(m_shipping_method_id, json[QString("shipping_method_id")]);
    m_shipping_method_id_isSet = !json[QString("shipping_method_id")].isNull() && m_shipping_method_id_isValid;

    m_shipping_method_name_isValid = ::OpenAPI::fromJsonValue(m_shipping_method_name, json[QString("shipping_method_name")]);
    m_shipping_method_name_isSet = !json[QString("shipping_method_name")].isNull() && m_shipping_method_name_isValid;

    m_shipping_option_isValid = ::OpenAPI::fromJsonValue(m_shipping_option, json[QString("shipping_option")]);
    m_shipping_option_isSet = !json[QString("shipping_option")].isNull() && m_shipping_option_isValid;

    m_shipping_required_isValid = ::OpenAPI::fromJsonValue(m_shipping_required, json[QString("shipping_required")]);
    m_shipping_required_isSet = !json[QString("shipping_required")].isNull() && m_shipping_required_isValid;

    m_shipping_tax_isValid = ::OpenAPI::fromJsonValue(m_shipping_tax, json[QString("shipping_tax")]);
    m_shipping_tax_isSet = !json[QString("shipping_tax")].isNull() && m_shipping_tax_isValid;

    m_shipping_taxes_isValid = ::OpenAPI::fromJsonValue(m_shipping_taxes, json[QString("shipping_taxes")]);
    m_shipping_taxes_isSet = !json[QString("shipping_taxes")].isNull() && m_shipping_taxes_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_subtotal_isValid = ::OpenAPI::fromJsonValue(m_subtotal, json[QString("subtotal")]);
    m_subtotal_isSet = !json[QString("subtotal")].isNull() && m_subtotal_isValid;

    m_tax_isValid = ::OpenAPI::fromJsonValue(m_tax, json[QString("tax")]);
    m_tax_isSet = !json[QString("tax")].isNull() && m_tax_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;

    m_tracking_company_isValid = ::OpenAPI::fromJsonValue(m_tracking_company, json[QString("tracking_company")]);
    m_tracking_company_isSet = !json[QString("tracking_company")].isNull() && m_tracking_company_isValid;

    m_tracking_number_isValid = ::OpenAPI::fromJsonValue(m_tracking_number, json[QString("tracking_number")]);
    m_tracking_number_isSet = !json[QString("tracking_number")].isNull() && m_tracking_number_isValid;

    m_tracking_url_isValid = ::OpenAPI::fromJsonValue(m_tracking_url, json[QString("tracking_url")]);
    m_tracking_url_isSet = !json[QString("tracking_url")].isNull() && m_tracking_url_isValid;
}

QString OAIOrderFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrderFields::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_fields.size() > 0) {
        obj.insert(QString("additional_fields"), ::OpenAPI::toJsonValue(m_additional_fields));
    }
    if (m_additional_information_isSet) {
        obj.insert(QString("additional_information"), ::OpenAPI::toJsonValue(m_additional_information));
    }
    if (m_billing_address.isSet()) {
        obj.insert(QString("billing_address"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_checkout_url_isSet) {
        obj.insert(QString("checkout_url"), ::OpenAPI::toJsonValue(m_checkout_url));
    }
    if (m_coupons_isSet) {
        obj.insert(QString("coupons"), ::OpenAPI::toJsonValue(m_coupons));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_customer.isSet()) {
        obj.insert(QString("customer"), ::OpenAPI::toJsonValue(m_customer));
    }
    if (m_discount_isSet) {
        obj.insert(QString("discount"), ::OpenAPI::toJsonValue(m_discount));
    }
    if (m_duplicate_url_isSet) {
        obj.insert(QString("duplicate_url"), ::OpenAPI::toJsonValue(m_duplicate_url));
    }
    if (m_external_shipping_rate_id_isSet) {
        obj.insert(QString("external_shipping_rate_id"), ::OpenAPI::toJsonValue(m_external_shipping_rate_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_payment_information_isSet) {
        obj.insert(QString("payment_information"), ::OpenAPI::toJsonValue(m_payment_information));
    }
    if (m_payment_method_name_isSet) {
        obj.insert(QString("payment_method_name"), ::OpenAPI::toJsonValue(m_payment_method_name));
    }
    if (m_payment_method_type_isSet) {
        obj.insert(QString("payment_method_type"), ::OpenAPI::toJsonValue(m_payment_method_type));
    }
    if (m_products.size() > 0) {
        obj.insert(QString("products"), ::OpenAPI::toJsonValue(m_products));
    }
    if (m_recovery_url_isSet) {
        obj.insert(QString("recovery_url"), ::OpenAPI::toJsonValue(m_recovery_url));
    }
    if (m_shipment_status_isSet) {
        obj.insert(QString("shipment_status"), ::OpenAPI::toJsonValue(m_shipment_status));
    }
    if (m_shipping_isSet) {
        obj.insert(QString("shipping"), ::OpenAPI::toJsonValue(m_shipping));
    }
    if (m_shipping_address.isSet()) {
        obj.insert(QString("shipping_address"), ::OpenAPI::toJsonValue(m_shipping_address));
    }
    if (m_shipping_discount_isSet) {
        obj.insert(QString("shipping_discount"), ::OpenAPI::toJsonValue(m_shipping_discount));
    }
    if (m_shipping_method_id_isSet) {
        obj.insert(QString("shipping_method_id"), ::OpenAPI::toJsonValue(m_shipping_method_id));
    }
    if (m_shipping_method_name_isSet) {
        obj.insert(QString("shipping_method_name"), ::OpenAPI::toJsonValue(m_shipping_method_name));
    }
    if (m_shipping_option_isSet) {
        obj.insert(QString("shipping_option"), ::OpenAPI::toJsonValue(m_shipping_option));
    }
    if (m_shipping_required_isSet) {
        obj.insert(QString("shipping_required"), ::OpenAPI::toJsonValue(m_shipping_required));
    }
    if (m_shipping_tax_isSet) {
        obj.insert(QString("shipping_tax"), ::OpenAPI::toJsonValue(m_shipping_tax));
    }
    if (m_shipping_taxes.size() > 0) {
        obj.insert(QString("shipping_taxes"), ::OpenAPI::toJsonValue(m_shipping_taxes));
    }
    if (m_source.isSet()) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_subtotal_isSet) {
        obj.insert(QString("subtotal"), ::OpenAPI::toJsonValue(m_subtotal));
    }
    if (m_tax_isSet) {
        obj.insert(QString("tax"), ::OpenAPI::toJsonValue(m_tax));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    if (m_tracking_company_isSet) {
        obj.insert(QString("tracking_company"), ::OpenAPI::toJsonValue(m_tracking_company));
    }
    if (m_tracking_number_isSet) {
        obj.insert(QString("tracking_number"), ::OpenAPI::toJsonValue(m_tracking_number));
    }
    if (m_tracking_url_isSet) {
        obj.insert(QString("tracking_url"), ::OpenAPI::toJsonValue(m_tracking_url));
    }
    return obj;
}

QList<OAIOrderAdditionalFields> OAIOrderFields::getAdditionalFields() const {
    return m_additional_fields;
}
void OAIOrderFields::setAdditionalFields(const QList<OAIOrderAdditionalFields> &additional_fields) {
    m_additional_fields = additional_fields;
    m_additional_fields_isSet = true;
}

bool OAIOrderFields::is_additional_fields_Set() const{
    return m_additional_fields_isSet;
}

bool OAIOrderFields::is_additional_fields_Valid() const{
    return m_additional_fields_isValid;
}

QString OAIOrderFields::getAdditionalInformation() const {
    return m_additional_information;
}
void OAIOrderFields::setAdditionalInformation(const QString &additional_information) {
    m_additional_information = additional_information;
    m_additional_information_isSet = true;
}

bool OAIOrderFields::is_additional_information_Set() const{
    return m_additional_information_isSet;
}

bool OAIOrderFields::is_additional_information_Valid() const{
    return m_additional_information_isValid;
}

OAIOrderBillingAddress OAIOrderFields::getBillingAddress() const {
    return m_billing_address;
}
void OAIOrderFields::setBillingAddress(const OAIOrderBillingAddress &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAIOrderFields::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAIOrderFields::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QString OAIOrderFields::getCheckoutUrl() const {
    return m_checkout_url;
}
void OAIOrderFields::setCheckoutUrl(const QString &checkout_url) {
    m_checkout_url = checkout_url;
    m_checkout_url_isSet = true;
}

bool OAIOrderFields::is_checkout_url_Set() const{
    return m_checkout_url_isSet;
}

bool OAIOrderFields::is_checkout_url_Valid() const{
    return m_checkout_url_isValid;
}

QString OAIOrderFields::getCoupons() const {
    return m_coupons;
}
void OAIOrderFields::setCoupons(const QString &coupons) {
    m_coupons = coupons;
    m_coupons_isSet = true;
}

bool OAIOrderFields::is_coupons_Set() const{
    return m_coupons_isSet;
}

bool OAIOrderFields::is_coupons_Valid() const{
    return m_coupons_isValid;
}

QString OAIOrderFields::getCreatedAt() const {
    return m_created_at;
}
void OAIOrderFields::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIOrderFields::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIOrderFields::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIOrderFields::getCurrency() const {
    return m_currency;
}
void OAIOrderFields::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIOrderFields::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIOrderFields::is_currency_Valid() const{
    return m_currency_isValid;
}

OAICustomer OAIOrderFields::getCustomer() const {
    return m_customer;
}
void OAIOrderFields::setCustomer(const OAICustomer &customer) {
    m_customer = customer;
    m_customer_isSet = true;
}

bool OAIOrderFields::is_customer_Set() const{
    return m_customer_isSet;
}

bool OAIOrderFields::is_customer_Valid() const{
    return m_customer_isValid;
}

float OAIOrderFields::getDiscount() const {
    return m_discount;
}
void OAIOrderFields::setDiscount(const float &discount) {
    m_discount = discount;
    m_discount_isSet = true;
}

bool OAIOrderFields::is_discount_Set() const{
    return m_discount_isSet;
}

bool OAIOrderFields::is_discount_Valid() const{
    return m_discount_isValid;
}

QString OAIOrderFields::getDuplicateUrl() const {
    return m_duplicate_url;
}
void OAIOrderFields::setDuplicateUrl(const QString &duplicate_url) {
    m_duplicate_url = duplicate_url;
    m_duplicate_url_isSet = true;
}

bool OAIOrderFields::is_duplicate_url_Set() const{
    return m_duplicate_url_isSet;
}

bool OAIOrderFields::is_duplicate_url_Valid() const{
    return m_duplicate_url_isValid;
}

QString OAIOrderFields::getExternalShippingRateId() const {
    return m_external_shipping_rate_id;
}
void OAIOrderFields::setExternalShippingRateId(const QString &external_shipping_rate_id) {
    m_external_shipping_rate_id = external_shipping_rate_id;
    m_external_shipping_rate_id_isSet = true;
}

bool OAIOrderFields::is_external_shipping_rate_id_Set() const{
    return m_external_shipping_rate_id_isSet;
}

bool OAIOrderFields::is_external_shipping_rate_id_Valid() const{
    return m_external_shipping_rate_id_isValid;
}

qint32 OAIOrderFields::getId() const {
    return m_id;
}
void OAIOrderFields::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOrderFields::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOrderFields::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIOrderFields::getPaymentInformation() const {
    return m_payment_information;
}
void OAIOrderFields::setPaymentInformation(const QString &payment_information) {
    m_payment_information = payment_information;
    m_payment_information_isSet = true;
}

bool OAIOrderFields::is_payment_information_Set() const{
    return m_payment_information_isSet;
}

bool OAIOrderFields::is_payment_information_Valid() const{
    return m_payment_information_isValid;
}

QString OAIOrderFields::getPaymentMethodName() const {
    return m_payment_method_name;
}
void OAIOrderFields::setPaymentMethodName(const QString &payment_method_name) {
    m_payment_method_name = payment_method_name;
    m_payment_method_name_isSet = true;
}

bool OAIOrderFields::is_payment_method_name_Set() const{
    return m_payment_method_name_isSet;
}

bool OAIOrderFields::is_payment_method_name_Valid() const{
    return m_payment_method_name_isValid;
}

QString OAIOrderFields::getPaymentMethodType() const {
    return m_payment_method_type;
}
void OAIOrderFields::setPaymentMethodType(const QString &payment_method_type) {
    m_payment_method_type = payment_method_type;
    m_payment_method_type_isSet = true;
}

bool OAIOrderFields::is_payment_method_type_Set() const{
    return m_payment_method_type_isSet;
}

bool OAIOrderFields::is_payment_method_type_Valid() const{
    return m_payment_method_type_isValid;
}

QList<OAIOrderProduct> OAIOrderFields::getProducts() const {
    return m_products;
}
void OAIOrderFields::setProducts(const QList<OAIOrderProduct> &products) {
    m_products = products;
    m_products_isSet = true;
}

bool OAIOrderFields::is_products_Set() const{
    return m_products_isSet;
}

bool OAIOrderFields::is_products_Valid() const{
    return m_products_isValid;
}

QString OAIOrderFields::getRecoveryUrl() const {
    return m_recovery_url;
}
void OAIOrderFields::setRecoveryUrl(const QString &recovery_url) {
    m_recovery_url = recovery_url;
    m_recovery_url_isSet = true;
}

bool OAIOrderFields::is_recovery_url_Set() const{
    return m_recovery_url_isSet;
}

bool OAIOrderFields::is_recovery_url_Valid() const{
    return m_recovery_url_isValid;
}

QString OAIOrderFields::getShipmentStatus() const {
    return m_shipment_status;
}
void OAIOrderFields::setShipmentStatus(const QString &shipment_status) {
    m_shipment_status = shipment_status;
    m_shipment_status_isSet = true;
}

bool OAIOrderFields::is_shipment_status_Set() const{
    return m_shipment_status_isSet;
}

bool OAIOrderFields::is_shipment_status_Valid() const{
    return m_shipment_status_isValid;
}

float OAIOrderFields::getShipping() const {
    return m_shipping;
}
void OAIOrderFields::setShipping(const float &shipping) {
    m_shipping = shipping;
    m_shipping_isSet = true;
}

bool OAIOrderFields::is_shipping_Set() const{
    return m_shipping_isSet;
}

bool OAIOrderFields::is_shipping_Valid() const{
    return m_shipping_isValid;
}

OAIOrderShippingAddress OAIOrderFields::getShippingAddress() const {
    return m_shipping_address;
}
void OAIOrderFields::setShippingAddress(const OAIOrderShippingAddress &shipping_address) {
    m_shipping_address = shipping_address;
    m_shipping_address_isSet = true;
}

bool OAIOrderFields::is_shipping_address_Set() const{
    return m_shipping_address_isSet;
}

bool OAIOrderFields::is_shipping_address_Valid() const{
    return m_shipping_address_isValid;
}

float OAIOrderFields::getShippingDiscount() const {
    return m_shipping_discount;
}
void OAIOrderFields::setShippingDiscount(const float &shipping_discount) {
    m_shipping_discount = shipping_discount;
    m_shipping_discount_isSet = true;
}

bool OAIOrderFields::is_shipping_discount_Set() const{
    return m_shipping_discount_isSet;
}

bool OAIOrderFields::is_shipping_discount_Valid() const{
    return m_shipping_discount_isValid;
}

qint32 OAIOrderFields::getShippingMethodId() const {
    return m_shipping_method_id;
}
void OAIOrderFields::setShippingMethodId(const qint32 &shipping_method_id) {
    m_shipping_method_id = shipping_method_id;
    m_shipping_method_id_isSet = true;
}

bool OAIOrderFields::is_shipping_method_id_Set() const{
    return m_shipping_method_id_isSet;
}

bool OAIOrderFields::is_shipping_method_id_Valid() const{
    return m_shipping_method_id_isValid;
}

QString OAIOrderFields::getShippingMethodName() const {
    return m_shipping_method_name;
}
void OAIOrderFields::setShippingMethodName(const QString &shipping_method_name) {
    m_shipping_method_name = shipping_method_name;
    m_shipping_method_name_isSet = true;
}

bool OAIOrderFields::is_shipping_method_name_Set() const{
    return m_shipping_method_name_isSet;
}

bool OAIOrderFields::is_shipping_method_name_Valid() const{
    return m_shipping_method_name_isValid;
}

QString OAIOrderFields::getShippingOption() const {
    return m_shipping_option;
}
void OAIOrderFields::setShippingOption(const QString &shipping_option) {
    m_shipping_option = shipping_option;
    m_shipping_option_isSet = true;
}

bool OAIOrderFields::is_shipping_option_Set() const{
    return m_shipping_option_isSet;
}

bool OAIOrderFields::is_shipping_option_Valid() const{
    return m_shipping_option_isValid;
}

bool OAIOrderFields::isShippingRequired() const {
    return m_shipping_required;
}
void OAIOrderFields::setShippingRequired(const bool &shipping_required) {
    m_shipping_required = shipping_required;
    m_shipping_required_isSet = true;
}

bool OAIOrderFields::is_shipping_required_Set() const{
    return m_shipping_required_isSet;
}

bool OAIOrderFields::is_shipping_required_Valid() const{
    return m_shipping_required_isValid;
}

float OAIOrderFields::getShippingTax() const {
    return m_shipping_tax;
}
void OAIOrderFields::setShippingTax(const float &shipping_tax) {
    m_shipping_tax = shipping_tax;
    m_shipping_tax_isSet = true;
}

bool OAIOrderFields::is_shipping_tax_Set() const{
    return m_shipping_tax_isSet;
}

bool OAIOrderFields::is_shipping_tax_Valid() const{
    return m_shipping_tax_isValid;
}

QList<OAIOrderShippingTax> OAIOrderFields::getShippingTaxes() const {
    return m_shipping_taxes;
}
void OAIOrderFields::setShippingTaxes(const QList<OAIOrderShippingTax> &shipping_taxes) {
    m_shipping_taxes = shipping_taxes;
    m_shipping_taxes_isSet = true;
}

bool OAIOrderFields::is_shipping_taxes_Set() const{
    return m_shipping_taxes_isSet;
}

bool OAIOrderFields::is_shipping_taxes_Valid() const{
    return m_shipping_taxes_isValid;
}

OAITrafficSource OAIOrderFields::getSource() const {
    return m_source;
}
void OAIOrderFields::setSource(const OAITrafficSource &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIOrderFields::is_source_Set() const{
    return m_source_isSet;
}

bool OAIOrderFields::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIOrderFields::getStatus() const {
    return m_status;
}
void OAIOrderFields::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIOrderFields::is_status_Set() const{
    return m_status_isSet;
}

bool OAIOrderFields::is_status_Valid() const{
    return m_status_isValid;
}

float OAIOrderFields::getSubtotal() const {
    return m_subtotal;
}
void OAIOrderFields::setSubtotal(const float &subtotal) {
    m_subtotal = subtotal;
    m_subtotal_isSet = true;
}

bool OAIOrderFields::is_subtotal_Set() const{
    return m_subtotal_isSet;
}

bool OAIOrderFields::is_subtotal_Valid() const{
    return m_subtotal_isValid;
}

float OAIOrderFields::getTax() const {
    return m_tax;
}
void OAIOrderFields::setTax(const float &tax) {
    m_tax = tax;
    m_tax_isSet = true;
}

bool OAIOrderFields::is_tax_Set() const{
    return m_tax_isSet;
}

bool OAIOrderFields::is_tax_Valid() const{
    return m_tax_isValid;
}

float OAIOrderFields::getTotal() const {
    return m_total;
}
void OAIOrderFields::setTotal(const float &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIOrderFields::is_total_Set() const{
    return m_total_isSet;
}

bool OAIOrderFields::is_total_Valid() const{
    return m_total_isValid;
}

QString OAIOrderFields::getTrackingCompany() const {
    return m_tracking_company;
}
void OAIOrderFields::setTrackingCompany(const QString &tracking_company) {
    m_tracking_company = tracking_company;
    m_tracking_company_isSet = true;
}

bool OAIOrderFields::is_tracking_company_Set() const{
    return m_tracking_company_isSet;
}

bool OAIOrderFields::is_tracking_company_Valid() const{
    return m_tracking_company_isValid;
}

QString OAIOrderFields::getTrackingNumber() const {
    return m_tracking_number;
}
void OAIOrderFields::setTrackingNumber(const QString &tracking_number) {
    m_tracking_number = tracking_number;
    m_tracking_number_isSet = true;
}

bool OAIOrderFields::is_tracking_number_Set() const{
    return m_tracking_number_isSet;
}

bool OAIOrderFields::is_tracking_number_Valid() const{
    return m_tracking_number_isValid;
}

QString OAIOrderFields::getTrackingUrl() const {
    return m_tracking_url;
}
void OAIOrderFields::setTrackingUrl(const QString &tracking_url) {
    m_tracking_url = tracking_url;
    m_tracking_url_isSet = true;
}

bool OAIOrderFields::is_tracking_url_Set() const{
    return m_tracking_url_isSet;
}

bool OAIOrderFields::is_tracking_url_Valid() const{
    return m_tracking_url_isValid;
}

bool OAIOrderFields::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_additional_information_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_checkout_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coupons_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duplicate_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_external_shipping_rate_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_information_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_method_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_method_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_products.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_recovery_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipment_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_discount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_method_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_method_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_option_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_required_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_taxes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_source.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subtotal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tracking_company_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tracking_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tracking_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrderFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
