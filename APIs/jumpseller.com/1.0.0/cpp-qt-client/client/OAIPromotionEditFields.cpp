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

#include "OAIPromotionEditFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPromotionEditFields::OAIPromotionEditFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPromotionEditFields::OAIPromotionEditFields() {
    this->initializeModel();
}

OAIPromotionEditFields::~OAIPromotionEditFields() {}

void OAIPromotionEditFields::initializeModel() {

    m_begins_at_isSet = false;
    m_begins_at_isValid = false;

    m_buys_at_least_isSet = false;
    m_buys_at_least_isValid = false;

    m_categories_isSet = false;
    m_categories_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_condition_price_isSet = false;
    m_condition_price_isValid = false;

    m_condition_qty_isSet = false;
    m_condition_qty_isValid = false;

    m_cumulative_isSet = false;
    m_cumulative_isValid = false;

    m_customer_categories_isSet = false;
    m_customer_categories_isValid = false;

    m_customers_isSet = false;
    m_customers_isValid = false;

    m_discount_amount_fix_isSet = false;
    m_discount_amount_fix_isValid = false;

    m_discount_amount_percent_isSet = false;
    m_discount_amount_percent_isValid = false;

    m_discount_target_isSet = false;
    m_discount_target_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_expires_at_isSet = false;
    m_expires_at_isValid = false;

    m_lasts_isSet = false;
    m_lasts_isValid = false;

    m_max_times_used_isSet = false;
    m_max_times_used_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_products_isSet = false;
    m_products_isValid = false;

    m_products_x_isSet = false;
    m_products_x_isValid = false;

    m_quantity_x_isSet = false;
    m_quantity_x_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIPromotionEditFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPromotionEditFields::fromJsonObject(QJsonObject json) {

    m_begins_at_isValid = ::OpenAPI::fromJsonValue(m_begins_at, json[QString("begins_at")]);
    m_begins_at_isSet = !json[QString("begins_at")].isNull() && m_begins_at_isValid;

    m_buys_at_least_isValid = ::OpenAPI::fromJsonValue(m_buys_at_least, json[QString("buys_at_least")]);
    m_buys_at_least_isSet = !json[QString("buys_at_least")].isNull() && m_buys_at_least_isValid;

    m_categories_isValid = ::OpenAPI::fromJsonValue(m_categories, json[QString("categories")]);
    m_categories_isSet = !json[QString("categories")].isNull() && m_categories_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_condition_price_isValid = ::OpenAPI::fromJsonValue(m_condition_price, json[QString("condition_price")]);
    m_condition_price_isSet = !json[QString("condition_price")].isNull() && m_condition_price_isValid;

    m_condition_qty_isValid = ::OpenAPI::fromJsonValue(m_condition_qty, json[QString("condition_qty")]);
    m_condition_qty_isSet = !json[QString("condition_qty")].isNull() && m_condition_qty_isValid;

    m_cumulative_isValid = ::OpenAPI::fromJsonValue(m_cumulative, json[QString("cumulative")]);
    m_cumulative_isSet = !json[QString("cumulative")].isNull() && m_cumulative_isValid;

    m_customer_categories_isValid = ::OpenAPI::fromJsonValue(m_customer_categories, json[QString("customer_categories")]);
    m_customer_categories_isSet = !json[QString("customer_categories")].isNull() && m_customer_categories_isValid;

    m_customers_isValid = ::OpenAPI::fromJsonValue(m_customers, json[QString("customers")]);
    m_customers_isSet = !json[QString("customers")].isNull() && m_customers_isValid;

    m_discount_amount_fix_isValid = ::OpenAPI::fromJsonValue(m_discount_amount_fix, json[QString("discount_amount_fix")]);
    m_discount_amount_fix_isSet = !json[QString("discount_amount_fix")].isNull() && m_discount_amount_fix_isValid;

    m_discount_amount_percent_isValid = ::OpenAPI::fromJsonValue(m_discount_amount_percent, json[QString("discount_amount_percent")]);
    m_discount_amount_percent_isSet = !json[QString("discount_amount_percent")].isNull() && m_discount_amount_percent_isValid;

    m_discount_target_isValid = ::OpenAPI::fromJsonValue(m_discount_target, json[QString("discount_target")]);
    m_discount_target_isSet = !json[QString("discount_target")].isNull() && m_discount_target_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_expires_at_isValid = ::OpenAPI::fromJsonValue(m_expires_at, json[QString("expires_at")]);
    m_expires_at_isSet = !json[QString("expires_at")].isNull() && m_expires_at_isValid;

    m_lasts_isValid = ::OpenAPI::fromJsonValue(m_lasts, json[QString("lasts")]);
    m_lasts_isSet = !json[QString("lasts")].isNull() && m_lasts_isValid;

    m_max_times_used_isValid = ::OpenAPI::fromJsonValue(m_max_times_used, json[QString("max_times_used")]);
    m_max_times_used_isSet = !json[QString("max_times_used")].isNull() && m_max_times_used_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_products_isValid = ::OpenAPI::fromJsonValue(m_products, json[QString("products")]);
    m_products_isSet = !json[QString("products")].isNull() && m_products_isValid;

    m_products_x_isValid = ::OpenAPI::fromJsonValue(m_products_x, json[QString("products_x")]);
    m_products_x_isSet = !json[QString("products_x")].isNull() && m_products_x_isValid;

    m_quantity_x_isValid = ::OpenAPI::fromJsonValue(m_quantity_x, json[QString("quantity_x")]);
    m_quantity_x_isSet = !json[QString("quantity_x")].isNull() && m_quantity_x_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIPromotionEditFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPromotionEditFields::asJsonObject() const {
    QJsonObject obj;
    if (m_begins_at_isSet) {
        obj.insert(QString("begins_at"), ::OpenAPI::toJsonValue(m_begins_at));
    }
    if (m_buys_at_least_isSet) {
        obj.insert(QString("buys_at_least"), ::OpenAPI::toJsonValue(m_buys_at_least));
    }
    if (m_categories.size() > 0) {
        obj.insert(QString("categories"), ::OpenAPI::toJsonValue(m_categories));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_condition_price_isSet) {
        obj.insert(QString("condition_price"), ::OpenAPI::toJsonValue(m_condition_price));
    }
    if (m_condition_qty_isSet) {
        obj.insert(QString("condition_qty"), ::OpenAPI::toJsonValue(m_condition_qty));
    }
    if (m_cumulative_isSet) {
        obj.insert(QString("cumulative"), ::OpenAPI::toJsonValue(m_cumulative));
    }
    if (m_customer_categories.size() > 0) {
        obj.insert(QString("customer_categories"), ::OpenAPI::toJsonValue(m_customer_categories));
    }
    if (m_customers_isSet) {
        obj.insert(QString("customers"), ::OpenAPI::toJsonValue(m_customers));
    }
    if (m_discount_amount_fix_isSet) {
        obj.insert(QString("discount_amount_fix"), ::OpenAPI::toJsonValue(m_discount_amount_fix));
    }
    if (m_discount_amount_percent_isSet) {
        obj.insert(QString("discount_amount_percent"), ::OpenAPI::toJsonValue(m_discount_amount_percent));
    }
    if (m_discount_target_isSet) {
        obj.insert(QString("discount_target"), ::OpenAPI::toJsonValue(m_discount_target));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_expires_at_isSet) {
        obj.insert(QString("expires_at"), ::OpenAPI::toJsonValue(m_expires_at));
    }
    if (m_lasts_isSet) {
        obj.insert(QString("lasts"), ::OpenAPI::toJsonValue(m_lasts));
    }
    if (m_max_times_used_isSet) {
        obj.insert(QString("max_times_used"), ::OpenAPI::toJsonValue(m_max_times_used));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_products.size() > 0) {
        obj.insert(QString("products"), ::OpenAPI::toJsonValue(m_products));
    }
    if (m_products_x.size() > 0) {
        obj.insert(QString("products_x"), ::OpenAPI::toJsonValue(m_products_x));
    }
    if (m_quantity_x_isSet) {
        obj.insert(QString("quantity_x"), ::OpenAPI::toJsonValue(m_quantity_x));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIPromotionEditFields::getBeginsAt() const {
    return m_begins_at;
}
void OAIPromotionEditFields::setBeginsAt(const QString &begins_at) {
    m_begins_at = begins_at;
    m_begins_at_isSet = true;
}

bool OAIPromotionEditFields::is_begins_at_Set() const{
    return m_begins_at_isSet;
}

bool OAIPromotionEditFields::is_begins_at_Valid() const{
    return m_begins_at_isValid;
}

QString OAIPromotionEditFields::getBuysAtLeast() const {
    return m_buys_at_least;
}
void OAIPromotionEditFields::setBuysAtLeast(const QString &buys_at_least) {
    m_buys_at_least = buys_at_least;
    m_buys_at_least_isSet = true;
}

bool OAIPromotionEditFields::is_buys_at_least_Set() const{
    return m_buys_at_least_isSet;
}

bool OAIPromotionEditFields::is_buys_at_least_Valid() const{
    return m_buys_at_least_isValid;
}

QList<OAIId> OAIPromotionEditFields::getCategories() const {
    return m_categories;
}
void OAIPromotionEditFields::setCategories(const QList<OAIId> &categories) {
    m_categories = categories;
    m_categories_isSet = true;
}

bool OAIPromotionEditFields::is_categories_Set() const{
    return m_categories_isSet;
}

bool OAIPromotionEditFields::is_categories_Valid() const{
    return m_categories_isValid;
}

QString OAIPromotionEditFields::getCode() const {
    return m_code;
}
void OAIPromotionEditFields::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIPromotionEditFields::is_code_Set() const{
    return m_code_isSet;
}

bool OAIPromotionEditFields::is_code_Valid() const{
    return m_code_isValid;
}

float OAIPromotionEditFields::getConditionPrice() const {
    return m_condition_price;
}
void OAIPromotionEditFields::setConditionPrice(const float &condition_price) {
    m_condition_price = condition_price;
    m_condition_price_isSet = true;
}

bool OAIPromotionEditFields::is_condition_price_Set() const{
    return m_condition_price_isSet;
}

bool OAIPromotionEditFields::is_condition_price_Valid() const{
    return m_condition_price_isValid;
}

qint32 OAIPromotionEditFields::getConditionQty() const {
    return m_condition_qty;
}
void OAIPromotionEditFields::setConditionQty(const qint32 &condition_qty) {
    m_condition_qty = condition_qty;
    m_condition_qty_isSet = true;
}

bool OAIPromotionEditFields::is_condition_qty_Set() const{
    return m_condition_qty_isSet;
}

bool OAIPromotionEditFields::is_condition_qty_Valid() const{
    return m_condition_qty_isValid;
}

bool OAIPromotionEditFields::isCumulative() const {
    return m_cumulative;
}
void OAIPromotionEditFields::setCumulative(const bool &cumulative) {
    m_cumulative = cumulative;
    m_cumulative_isSet = true;
}

bool OAIPromotionEditFields::is_cumulative_Set() const{
    return m_cumulative_isSet;
}

bool OAIPromotionEditFields::is_cumulative_Valid() const{
    return m_cumulative_isValid;
}

QList<OAIId> OAIPromotionEditFields::getCustomerCategories() const {
    return m_customer_categories;
}
void OAIPromotionEditFields::setCustomerCategories(const QList<OAIId> &customer_categories) {
    m_customer_categories = customer_categories;
    m_customer_categories_isSet = true;
}

bool OAIPromotionEditFields::is_customer_categories_Set() const{
    return m_customer_categories_isSet;
}

bool OAIPromotionEditFields::is_customer_categories_Valid() const{
    return m_customer_categories_isValid;
}

QString OAIPromotionEditFields::getCustomers() const {
    return m_customers;
}
void OAIPromotionEditFields::setCustomers(const QString &customers) {
    m_customers = customers;
    m_customers_isSet = true;
}

bool OAIPromotionEditFields::is_customers_Set() const{
    return m_customers_isSet;
}

bool OAIPromotionEditFields::is_customers_Valid() const{
    return m_customers_isValid;
}

float OAIPromotionEditFields::getDiscountAmountFix() const {
    return m_discount_amount_fix;
}
void OAIPromotionEditFields::setDiscountAmountFix(const float &discount_amount_fix) {
    m_discount_amount_fix = discount_amount_fix;
    m_discount_amount_fix_isSet = true;
}

bool OAIPromotionEditFields::is_discount_amount_fix_Set() const{
    return m_discount_amount_fix_isSet;
}

bool OAIPromotionEditFields::is_discount_amount_fix_Valid() const{
    return m_discount_amount_fix_isValid;
}

float OAIPromotionEditFields::getDiscountAmountPercent() const {
    return m_discount_amount_percent;
}
void OAIPromotionEditFields::setDiscountAmountPercent(const float &discount_amount_percent) {
    m_discount_amount_percent = discount_amount_percent;
    m_discount_amount_percent_isSet = true;
}

bool OAIPromotionEditFields::is_discount_amount_percent_Set() const{
    return m_discount_amount_percent_isSet;
}

bool OAIPromotionEditFields::is_discount_amount_percent_Valid() const{
    return m_discount_amount_percent_isValid;
}

QString OAIPromotionEditFields::getDiscountTarget() const {
    return m_discount_target;
}
void OAIPromotionEditFields::setDiscountTarget(const QString &discount_target) {
    m_discount_target = discount_target;
    m_discount_target_isSet = true;
}

bool OAIPromotionEditFields::is_discount_target_Set() const{
    return m_discount_target_isSet;
}

bool OAIPromotionEditFields::is_discount_target_Valid() const{
    return m_discount_target_isValid;
}

bool OAIPromotionEditFields::isEnabled() const {
    return m_enabled;
}
void OAIPromotionEditFields::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIPromotionEditFields::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIPromotionEditFields::is_enabled_Valid() const{
    return m_enabled_isValid;
}

QString OAIPromotionEditFields::getExpiresAt() const {
    return m_expires_at;
}
void OAIPromotionEditFields::setExpiresAt(const QString &expires_at) {
    m_expires_at = expires_at;
    m_expires_at_isSet = true;
}

bool OAIPromotionEditFields::is_expires_at_Set() const{
    return m_expires_at_isSet;
}

bool OAIPromotionEditFields::is_expires_at_Valid() const{
    return m_expires_at_isValid;
}

QString OAIPromotionEditFields::getLasts() const {
    return m_lasts;
}
void OAIPromotionEditFields::setLasts(const QString &lasts) {
    m_lasts = lasts;
    m_lasts_isSet = true;
}

bool OAIPromotionEditFields::is_lasts_Set() const{
    return m_lasts_isSet;
}

bool OAIPromotionEditFields::is_lasts_Valid() const{
    return m_lasts_isValid;
}

qint32 OAIPromotionEditFields::getMaxTimesUsed() const {
    return m_max_times_used;
}
void OAIPromotionEditFields::setMaxTimesUsed(const qint32 &max_times_used) {
    m_max_times_used = max_times_used;
    m_max_times_used_isSet = true;
}

bool OAIPromotionEditFields::is_max_times_used_Set() const{
    return m_max_times_used_isSet;
}

bool OAIPromotionEditFields::is_max_times_used_Valid() const{
    return m_max_times_used_isValid;
}

QString OAIPromotionEditFields::getName() const {
    return m_name;
}
void OAIPromotionEditFields::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPromotionEditFields::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPromotionEditFields::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIId> OAIPromotionEditFields::getProducts() const {
    return m_products;
}
void OAIPromotionEditFields::setProducts(const QList<OAIId> &products) {
    m_products = products;
    m_products_isSet = true;
}

bool OAIPromotionEditFields::is_products_Set() const{
    return m_products_isSet;
}

bool OAIPromotionEditFields::is_products_Valid() const{
    return m_products_isValid;
}

QList<OAIId> OAIPromotionEditFields::getProductsX() const {
    return m_products_x;
}
void OAIPromotionEditFields::setProductsX(const QList<OAIId> &products_x) {
    m_products_x = products_x;
    m_products_x_isSet = true;
}

bool OAIPromotionEditFields::is_products_x_Set() const{
    return m_products_x_isSet;
}

bool OAIPromotionEditFields::is_products_x_Valid() const{
    return m_products_x_isValid;
}

qint32 OAIPromotionEditFields::getQuantityX() const {
    return m_quantity_x;
}
void OAIPromotionEditFields::setQuantityX(const qint32 &quantity_x) {
    m_quantity_x = quantity_x;
    m_quantity_x_isSet = true;
}

bool OAIPromotionEditFields::is_quantity_x_Set() const{
    return m_quantity_x_isSet;
}

bool OAIPromotionEditFields::is_quantity_x_Valid() const{
    return m_quantity_x_isValid;
}

QString OAIPromotionEditFields::getType() const {
    return m_type;
}
void OAIPromotionEditFields::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIPromotionEditFields::is_type_Set() const{
    return m_type_isSet;
}

bool OAIPromotionEditFields::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIPromotionEditFields::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_begins_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_buys_at_least_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_condition_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_condition_qty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cumulative_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_customers_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_amount_fix_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_amount_percent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_discount_target_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_expires_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lasts_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_times_used_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_products.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_products_x.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_x_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPromotionEditFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
