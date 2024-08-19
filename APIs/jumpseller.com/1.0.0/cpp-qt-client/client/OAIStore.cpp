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

#include "OAIStore.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStore::OAIStore(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStore::OAIStore() {
    this->initializeModel();
}

OAIStore::~OAIStore() {}

void OAIStore::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_hooks_token_isSet = false;
    m_hooks_token_isValid = false;

    m_logo_isSet = false;
    m_logo_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_timezone_isSet = false;
    m_timezone_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_weight_unit_isSet = false;
    m_weight_unit_isValid = false;
}

void OAIStore::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStore::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_hooks_token_isValid = ::OpenAPI::fromJsonValue(m_hooks_token, json[QString("hooks_token")]);
    m_hooks_token_isSet = !json[QString("hooks_token")].isNull() && m_hooks_token_isValid;

    m_logo_isValid = ::OpenAPI::fromJsonValue(m_logo, json[QString("logo")]);
    m_logo_isSet = !json[QString("logo")].isNull() && m_logo_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_timezone_isValid = ::OpenAPI::fromJsonValue(m_timezone, json[QString("timezone")]);
    m_timezone_isSet = !json[QString("timezone")].isNull() && m_timezone_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_weight_unit_isValid = ::OpenAPI::fromJsonValue(m_weight_unit, json[QString("weight_unit")]);
    m_weight_unit_isSet = !json[QString("weight_unit")].isNull() && m_weight_unit_isValid;
}

QString OAIStore::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStore::asJsonObject() const {
    QJsonObject obj;
    if (m_address.isSet()) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_hooks_token_isSet) {
        obj.insert(QString("hooks_token"), ::OpenAPI::toJsonValue(m_hooks_token));
    }
    if (m_logo_isSet) {
        obj.insert(QString("logo"), ::OpenAPI::toJsonValue(m_logo));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_timezone_isSet) {
        obj.insert(QString("timezone"), ::OpenAPI::toJsonValue(m_timezone));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_weight_unit_isSet) {
        obj.insert(QString("weight_unit"), ::OpenAPI::toJsonValue(m_weight_unit));
    }
    return obj;
}

OAIStoreAddress OAIStore::getAddress() const {
    return m_address;
}
void OAIStore::setAddress(const OAIStoreAddress &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIStore::is_address_Set() const{
    return m_address_isSet;
}

bool OAIStore::is_address_Valid() const{
    return m_address_isValid;
}

QString OAIStore::getCode() const {
    return m_code;
}
void OAIStore::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIStore::is_code_Set() const{
    return m_code_isSet;
}

bool OAIStore::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIStore::getCountry() const {
    return m_country;
}
void OAIStore::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIStore::is_country_Set() const{
    return m_country_isSet;
}

bool OAIStore::is_country_Valid() const{
    return m_country_isValid;
}

QString OAIStore::getCurrency() const {
    return m_currency;
}
void OAIStore::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIStore::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIStore::is_currency_Valid() const{
    return m_currency_isValid;
}

QString OAIStore::getEmail() const {
    return m_email;
}
void OAIStore::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIStore::is_email_Set() const{
    return m_email_isSet;
}

bool OAIStore::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIStore::getHooksToken() const {
    return m_hooks_token;
}
void OAIStore::setHooksToken(const QString &hooks_token) {
    m_hooks_token = hooks_token;
    m_hooks_token_isSet = true;
}

bool OAIStore::is_hooks_token_Set() const{
    return m_hooks_token_isSet;
}

bool OAIStore::is_hooks_token_Valid() const{
    return m_hooks_token_isValid;
}

QString OAIStore::getLogo() const {
    return m_logo;
}
void OAIStore::setLogo(const QString &logo) {
    m_logo = logo;
    m_logo_isSet = true;
}

bool OAIStore::is_logo_Set() const{
    return m_logo_isSet;
}

bool OAIStore::is_logo_Valid() const{
    return m_logo_isValid;
}

QString OAIStore::getName() const {
    return m_name;
}
void OAIStore::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIStore::is_name_Set() const{
    return m_name_isSet;
}

bool OAIStore::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIStore::getTimezone() const {
    return m_timezone;
}
void OAIStore::setTimezone(const QString &timezone) {
    m_timezone = timezone;
    m_timezone_isSet = true;
}

bool OAIStore::is_timezone_Set() const{
    return m_timezone_isSet;
}

bool OAIStore::is_timezone_Valid() const{
    return m_timezone_isValid;
}

QString OAIStore::getUrl() const {
    return m_url;
}
void OAIStore::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIStore::is_url_Set() const{
    return m_url_isSet;
}

bool OAIStore::is_url_Valid() const{
    return m_url_isValid;
}

QString OAIStore::getWeightUnit() const {
    return m_weight_unit;
}
void OAIStore::setWeightUnit(const QString &weight_unit) {
    m_weight_unit = weight_unit;
    m_weight_unit_isSet = true;
}

bool OAIStore::is_weight_unit_Set() const{
    return m_weight_unit_isSet;
}

bool OAIStore::is_weight_unit_Valid() const{
    return m_weight_unit_isValid;
}

bool OAIStore::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hooks_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_logo_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weight_unit_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStore::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
