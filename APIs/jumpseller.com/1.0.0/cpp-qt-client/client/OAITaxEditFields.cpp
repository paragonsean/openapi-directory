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

#include "OAITaxEditFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITaxEditFields::OAITaxEditFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITaxEditFields::OAITaxEditFields() {
    this->initializeModel();
}

OAITaxEditFields::~OAITaxEditFields() {}

void OAITaxEditFields::initializeModel() {

    m_category_id_isSet = false;
    m_category_id_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_fixed_isSet = false;
    m_fixed_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_shipping_isSet = false;
    m_shipping_isValid = false;

    m_tax_isSet = false;
    m_tax_isValid = false;
}

void OAITaxEditFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITaxEditFields::fromJsonObject(QJsonObject json) {

    m_category_id_isValid = ::OpenAPI::fromJsonValue(m_category_id, json[QString("category_id")]);
    m_category_id_isSet = !json[QString("category_id")].isNull() && m_category_id_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_fixed_isValid = ::OpenAPI::fromJsonValue(m_fixed, json[QString("fixed")]);
    m_fixed_isSet = !json[QString("fixed")].isNull() && m_fixed_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_shipping_isValid = ::OpenAPI::fromJsonValue(m_shipping, json[QString("shipping")]);
    m_shipping_isSet = !json[QString("shipping")].isNull() && m_shipping_isValid;

    m_tax_isValid = ::OpenAPI::fromJsonValue(m_tax, json[QString("tax")]);
    m_tax_isSet = !json[QString("tax")].isNull() && m_tax_isValid;
}

QString OAITaxEditFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITaxEditFields::asJsonObject() const {
    QJsonObject obj;
    if (m_category_id_isSet) {
        obj.insert(QString("category_id"), ::OpenAPI::toJsonValue(m_category_id));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_fixed_isSet) {
        obj.insert(QString("fixed"), ::OpenAPI::toJsonValue(m_fixed));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_shipping_isSet) {
        obj.insert(QString("shipping"), ::OpenAPI::toJsonValue(m_shipping));
    }
    if (m_tax_isSet) {
        obj.insert(QString("tax"), ::OpenAPI::toJsonValue(m_tax));
    }
    return obj;
}

qint32 OAITaxEditFields::getCategoryId() const {
    return m_category_id;
}
void OAITaxEditFields::setCategoryId(const qint32 &category_id) {
    m_category_id = category_id;
    m_category_id_isSet = true;
}

bool OAITaxEditFields::is_category_id_Set() const{
    return m_category_id_isSet;
}

bool OAITaxEditFields::is_category_id_Valid() const{
    return m_category_id_isValid;
}

QString OAITaxEditFields::getCountry() const {
    return m_country;
}
void OAITaxEditFields::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAITaxEditFields::is_country_Set() const{
    return m_country_isSet;
}

bool OAITaxEditFields::is_country_Valid() const{
    return m_country_isValid;
}

bool OAITaxEditFields::isFixed() const {
    return m_fixed;
}
void OAITaxEditFields::setFixed(const bool &fixed) {
    m_fixed = fixed;
    m_fixed_isSet = true;
}

bool OAITaxEditFields::is_fixed_Set() const{
    return m_fixed_isSet;
}

bool OAITaxEditFields::is_fixed_Valid() const{
    return m_fixed_isValid;
}

QString OAITaxEditFields::getName() const {
    return m_name;
}
void OAITaxEditFields::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITaxEditFields::is_name_Set() const{
    return m_name_isSet;
}

bool OAITaxEditFields::is_name_Valid() const{
    return m_name_isValid;
}

QString OAITaxEditFields::getRegion() const {
    return m_region;
}
void OAITaxEditFields::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAITaxEditFields::is_region_Set() const{
    return m_region_isSet;
}

bool OAITaxEditFields::is_region_Valid() const{
    return m_region_isValid;
}

bool OAITaxEditFields::isShipping() const {
    return m_shipping;
}
void OAITaxEditFields::setShipping(const bool &shipping) {
    m_shipping = shipping;
    m_shipping_isSet = true;
}

bool OAITaxEditFields::is_shipping_Set() const{
    return m_shipping_isSet;
}

bool OAITaxEditFields::is_shipping_Valid() const{
    return m_shipping_isValid;
}

float OAITaxEditFields::getTax() const {
    return m_tax;
}
void OAITaxEditFields::setTax(const float &tax) {
    m_tax = tax;
    m_tax_isSet = true;
}

bool OAITaxEditFields::is_tax_Set() const{
    return m_tax_isSet;
}

bool OAITaxEditFields::is_tax_Valid() const{
    return m_tax_isValid;
}

bool OAITaxEditFields::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_category_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fixed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITaxEditFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
