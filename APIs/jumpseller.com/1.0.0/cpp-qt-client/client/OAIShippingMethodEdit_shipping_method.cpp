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

#include "OAIShippingMethodEdit_shipping_method.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShippingMethodEdit_shipping_method::OAIShippingMethodEdit_shipping_method(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShippingMethodEdit_shipping_method::OAIShippingMethodEdit_shipping_method() {
    this->initializeModel();
}

OAIShippingMethodEdit_shipping_method::~OAIShippingMethodEdit_shipping_method() {}

void OAIShippingMethodEdit_shipping_method::initializeModel() {

    m_callback_url_isSet = false;
    m_callback_url_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_fetch_services_url_isSet = false;
    m_fetch_services_url_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_postal_isSet = false;
    m_postal_isValid = false;

    m_state_isSet = false;
    m_state_isValid = false;

    m_token_isSet = false;
    m_token_isValid = false;
}

void OAIShippingMethodEdit_shipping_method::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShippingMethodEdit_shipping_method::fromJsonObject(QJsonObject json) {

    m_callback_url_isValid = ::OpenAPI::fromJsonValue(m_callback_url, json[QString("callback_url")]);
    m_callback_url_isSet = !json[QString("callback_url")].isNull() && m_callback_url_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_fetch_services_url_isValid = ::OpenAPI::fromJsonValue(m_fetch_services_url, json[QString("fetch_services_url")]);
    m_fetch_services_url_isSet = !json[QString("fetch_services_url")].isNull() && m_fetch_services_url_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_postal_isValid = ::OpenAPI::fromJsonValue(m_postal, json[QString("postal")]);
    m_postal_isSet = !json[QString("postal")].isNull() && m_postal_isValid;

    m_state_isValid = ::OpenAPI::fromJsonValue(m_state, json[QString("state")]);
    m_state_isSet = !json[QString("state")].isNull() && m_state_isValid;

    m_token_isValid = ::OpenAPI::fromJsonValue(m_token, json[QString("token")]);
    m_token_isSet = !json[QString("token")].isNull() && m_token_isValid;
}

QString OAIShippingMethodEdit_shipping_method::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShippingMethodEdit_shipping_method::asJsonObject() const {
    QJsonObject obj;
    if (m_callback_url_isSet) {
        obj.insert(QString("callback_url"), ::OpenAPI::toJsonValue(m_callback_url));
    }
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_fetch_services_url_isSet) {
        obj.insert(QString("fetch_services_url"), ::OpenAPI::toJsonValue(m_fetch_services_url));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_postal_isSet) {
        obj.insert(QString("postal"), ::OpenAPI::toJsonValue(m_postal));
    }
    if (m_state_isSet) {
        obj.insert(QString("state"), ::OpenAPI::toJsonValue(m_state));
    }
    if (m_token_isSet) {
        obj.insert(QString("token"), ::OpenAPI::toJsonValue(m_token));
    }
    return obj;
}

QString OAIShippingMethodEdit_shipping_method::getCallbackUrl() const {
    return m_callback_url;
}
void OAIShippingMethodEdit_shipping_method::setCallbackUrl(const QString &callback_url) {
    m_callback_url = callback_url;
    m_callback_url_isSet = true;
}

bool OAIShippingMethodEdit_shipping_method::is_callback_url_Set() const{
    return m_callback_url_isSet;
}

bool OAIShippingMethodEdit_shipping_method::is_callback_url_Valid() const{
    return m_callback_url_isValid;
}

QString OAIShippingMethodEdit_shipping_method::getCity() const {
    return m_city;
}
void OAIShippingMethodEdit_shipping_method::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIShippingMethodEdit_shipping_method::is_city_Set() const{
    return m_city_isSet;
}

bool OAIShippingMethodEdit_shipping_method::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIShippingMethodEdit_shipping_method::getFetchServicesUrl() const {
    return m_fetch_services_url;
}
void OAIShippingMethodEdit_shipping_method::setFetchServicesUrl(const QString &fetch_services_url) {
    m_fetch_services_url = fetch_services_url;
    m_fetch_services_url_isSet = true;
}

bool OAIShippingMethodEdit_shipping_method::is_fetch_services_url_Set() const{
    return m_fetch_services_url_isSet;
}

bool OAIShippingMethodEdit_shipping_method::is_fetch_services_url_Valid() const{
    return m_fetch_services_url_isValid;
}

QString OAIShippingMethodEdit_shipping_method::getName() const {
    return m_name;
}
void OAIShippingMethodEdit_shipping_method::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIShippingMethodEdit_shipping_method::is_name_Set() const{
    return m_name_isSet;
}

bool OAIShippingMethodEdit_shipping_method::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIShippingMethodEdit_shipping_method::getPostal() const {
    return m_postal;
}
void OAIShippingMethodEdit_shipping_method::setPostal(const QString &postal) {
    m_postal = postal;
    m_postal_isSet = true;
}

bool OAIShippingMethodEdit_shipping_method::is_postal_Set() const{
    return m_postal_isSet;
}

bool OAIShippingMethodEdit_shipping_method::is_postal_Valid() const{
    return m_postal_isValid;
}

QString OAIShippingMethodEdit_shipping_method::getState() const {
    return m_state;
}
void OAIShippingMethodEdit_shipping_method::setState(const QString &state) {
    m_state = state;
    m_state_isSet = true;
}

bool OAIShippingMethodEdit_shipping_method::is_state_Set() const{
    return m_state_isSet;
}

bool OAIShippingMethodEdit_shipping_method::is_state_Valid() const{
    return m_state_isValid;
}

QString OAIShippingMethodEdit_shipping_method::getToken() const {
    return m_token;
}
void OAIShippingMethodEdit_shipping_method::setToken(const QString &token) {
    m_token = token;
    m_token_isSet = true;
}

bool OAIShippingMethodEdit_shipping_method::is_token_Set() const{
    return m_token_isSet;
}

bool OAIShippingMethodEdit_shipping_method::is_token_Valid() const{
    return m_token_isValid;
}

bool OAIShippingMethodEdit_shipping_method::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_callback_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fetch_services_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postal_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIShippingMethodEdit_shipping_method::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
