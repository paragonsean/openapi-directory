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

#include "OAIPromotionFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPromotionFields::OAIPromotionFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPromotionFields::OAIPromotionFields() {
    this->initializeModel();
}

OAIPromotionFields::~OAIPromotionFields() {}

void OAIPromotionFields::initializeModel() {

    m_begins_at_isSet = false;
    m_begins_at_isValid = false;

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

    m_id_isSet = false;
    m_id_isValid = false;

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

    m_status_isSet = false;
    m_status_isValid = false;

    m_times_used_isSet = false;
    m_times_used_isValid = false;
}

void OAIPromotionFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPromotionFields::fromJsonObject(QJsonObject json) {

    m_begins_at_isValid = ::OpenAPI::fromJsonValue(m_begins_at, json[QString("begins_at")]);
    m_begins_at_isSet = !json[QString("begins_at")].isNull() && m_begins_at_isValid;

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

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

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

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_times_used_isValid = ::OpenAPI::fromJsonValue(m_times_used, json[QString("times_used")]);
    m_times_used_isSet = !json[QString("times_used")].isNull() && m_times_used_isValid;
}

QString OAIPromotionFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPromotionFields::asJsonObject() const {
    QJsonObject obj;
    if (m_begins_at_isSet) {
        obj.insert(QString("begins_at"), ::OpenAPI::toJsonValue(m_begins_at));
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
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
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
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_times_used_isSet) {
        obj.insert(QString("times_used"), ::OpenAPI::toJsonValue(m_times_used));
    }
    return obj;
}

QString OAIPromotionFields::getBeginsAt() const {
    return m_begins_at;
}
void OAIPromotionFields::setBeginsAt(const QString &begins_at) {
    m_begins_at = begins_at;
    m_begins_at_isSet = true;
}

bool OAIPromotionFields::is_begins_at_Set() const{
    return m_begins_at_isSet;
}

bool OAIPromotionFields::is_begins_at_Valid() const{
    return m_begins_at_isValid;
}

QList<OAIId> OAIPromotionFields::getCategories() const {
    return m_categories;
}
void OAIPromotionFields::setCategories(const QList<OAIId> &categories) {
    m_categories = categories;
    m_categories_isSet = true;
}

bool OAIPromotionFields::is_categories_Set() const{
    return m_categories_isSet;
}

bool OAIPromotionFields::is_categories_Valid() const{
    return m_categories_isValid;
}

QString OAIPromotionFields::getCode() const {
    return m_code;
}
void OAIPromotionFields::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIPromotionFields::is_code_Set() const{
    return m_code_isSet;
}

bool OAIPromotionFields::is_code_Valid() const{
    return m_code_isValid;
}

float OAIPromotionFields::getConditionPrice() const {
    return m_condition_price;
}
void OAIPromotionFields::setConditionPrice(const float &condition_price) {
    m_condition_price = condition_price;
    m_condition_price_isSet = true;
}

bool OAIPromotionFields::is_condition_price_Set() const{
    return m_condition_price_isSet;
}

bool OAIPromotionFields::is_condition_price_Valid() const{
    return m_condition_price_isValid;
}

qint32 OAIPromotionFields::getConditionQty() const {
    return m_condition_qty;
}
void OAIPromotionFields::setConditionQty(const qint32 &condition_qty) {
    m_condition_qty = condition_qty;
    m_condition_qty_isSet = true;
}

bool OAIPromotionFields::is_condition_qty_Set() const{
    return m_condition_qty_isSet;
}

bool OAIPromotionFields::is_condition_qty_Valid() const{
    return m_condition_qty_isValid;
}

bool OAIPromotionFields::isCumulative() const {
    return m_cumulative;
}
void OAIPromotionFields::setCumulative(const bool &cumulative) {
    m_cumulative = cumulative;
    m_cumulative_isSet = true;
}

bool OAIPromotionFields::is_cumulative_Set() const{
    return m_cumulative_isSet;
}

bool OAIPromotionFields::is_cumulative_Valid() const{
    return m_cumulative_isValid;
}

QList<OAIId> OAIPromotionFields::getCustomerCategories() const {
    return m_customer_categories;
}
void OAIPromotionFields::setCustomerCategories(const QList<OAIId> &customer_categories) {
    m_customer_categories = customer_categories;
    m_customer_categories_isSet = true;
}

bool OAIPromotionFields::is_customer_categories_Set() const{
    return m_customer_categories_isSet;
}

bool OAIPromotionFields::is_customer_categories_Valid() const{
    return m_customer_categories_isValid;
}

float OAIPromotionFields::getDiscountAmountFix() const {
    return m_discount_amount_fix;
}
void OAIPromotionFields::setDiscountAmountFix(const float &discount_amount_fix) {
    m_discount_amount_fix = discount_amount_fix;
    m_discount_amount_fix_isSet = true;
}

bool OAIPromotionFields::is_discount_amount_fix_Set() const{
    return m_discount_amount_fix_isSet;
}

bool OAIPromotionFields::is_discount_amount_fix_Valid() const{
    return m_discount_amount_fix_isValid;
}

float OAIPromotionFields::getDiscountAmountPercent() const {
    return m_discount_amount_percent;
}
void OAIPromotionFields::setDiscountAmountPercent(const float &discount_amount_percent) {
    m_discount_amount_percent = discount_amount_percent;
    m_discount_amount_percent_isSet = true;
}

bool OAIPromotionFields::is_discount_amount_percent_Set() const{
    return m_discount_amount_percent_isSet;
}

bool OAIPromotionFields::is_discount_amount_percent_Valid() const{
    return m_discount_amount_percent_isValid;
}

QString OAIPromotionFields::getDiscountTarget() const {
    return m_discount_target;
}
void OAIPromotionFields::setDiscountTarget(const QString &discount_target) {
    m_discount_target = discount_target;
    m_discount_target_isSet = true;
}

bool OAIPromotionFields::is_discount_target_Set() const{
    return m_discount_target_isSet;
}

bool OAIPromotionFields::is_discount_target_Valid() const{
    return m_discount_target_isValid;
}

bool OAIPromotionFields::isEnabled() const {
    return m_enabled;
}
void OAIPromotionFields::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIPromotionFields::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIPromotionFields::is_enabled_Valid() const{
    return m_enabled_isValid;
}

QString OAIPromotionFields::getExpiresAt() const {
    return m_expires_at;
}
void OAIPromotionFields::setExpiresAt(const QString &expires_at) {
    m_expires_at = expires_at;
    m_expires_at_isSet = true;
}

bool OAIPromotionFields::is_expires_at_Set() const{
    return m_expires_at_isSet;
}

bool OAIPromotionFields::is_expires_at_Valid() const{
    return m_expires_at_isValid;
}

qint32 OAIPromotionFields::getId() const {
    return m_id;
}
void OAIPromotionFields::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPromotionFields::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPromotionFields::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPromotionFields::getLasts() const {
    return m_lasts;
}
void OAIPromotionFields::setLasts(const QString &lasts) {
    m_lasts = lasts;
    m_lasts_isSet = true;
}

bool OAIPromotionFields::is_lasts_Set() const{
    return m_lasts_isSet;
}

bool OAIPromotionFields::is_lasts_Valid() const{
    return m_lasts_isValid;
}

qint32 OAIPromotionFields::getMaxTimesUsed() const {
    return m_max_times_used;
}
void OAIPromotionFields::setMaxTimesUsed(const qint32 &max_times_used) {
    m_max_times_used = max_times_used;
    m_max_times_used_isSet = true;
}

bool OAIPromotionFields::is_max_times_used_Set() const{
    return m_max_times_used_isSet;
}

bool OAIPromotionFields::is_max_times_used_Valid() const{
    return m_max_times_used_isValid;
}

QString OAIPromotionFields::getName() const {
    return m_name;
}
void OAIPromotionFields::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPromotionFields::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPromotionFields::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIId> OAIPromotionFields::getProducts() const {
    return m_products;
}
void OAIPromotionFields::setProducts(const QList<OAIId> &products) {
    m_products = products;
    m_products_isSet = true;
}

bool OAIPromotionFields::is_products_Set() const{
    return m_products_isSet;
}

bool OAIPromotionFields::is_products_Valid() const{
    return m_products_isValid;
}

QList<OAIId> OAIPromotionFields::getProductsX() const {
    return m_products_x;
}
void OAIPromotionFields::setProductsX(const QList<OAIId> &products_x) {
    m_products_x = products_x;
    m_products_x_isSet = true;
}

bool OAIPromotionFields::is_products_x_Set() const{
    return m_products_x_isSet;
}

bool OAIPromotionFields::is_products_x_Valid() const{
    return m_products_x_isValid;
}

qint32 OAIPromotionFields::getQuantityX() const {
    return m_quantity_x;
}
void OAIPromotionFields::setQuantityX(const qint32 &quantity_x) {
    m_quantity_x = quantity_x;
    m_quantity_x_isSet = true;
}

bool OAIPromotionFields::is_quantity_x_Set() const{
    return m_quantity_x_isSet;
}

bool OAIPromotionFields::is_quantity_x_Valid() const{
    return m_quantity_x_isValid;
}

QString OAIPromotionFields::getStatus() const {
    return m_status;
}
void OAIPromotionFields::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIPromotionFields::is_status_Set() const{
    return m_status_isSet;
}

bool OAIPromotionFields::is_status_Valid() const{
    return m_status_isValid;
}

qint32 OAIPromotionFields::getTimesUsed() const {
    return m_times_used;
}
void OAIPromotionFields::setTimesUsed(const qint32 &times_used) {
    m_times_used = times_used;
    m_times_used_isSet = true;
}

bool OAIPromotionFields::is_times_used_Set() const{
    return m_times_used_isSet;
}

bool OAIPromotionFields::is_times_used_Valid() const{
    return m_times_used_isValid;
}

bool OAIPromotionFields::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_begins_at_isSet) {
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

        if (m_id_isSet) {
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

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_times_used_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPromotionFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
