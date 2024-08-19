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

#include "OAICustomerFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomerFields::OAICustomerFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomerFields::OAICustomerFields() {
    this->initializeModel();
}

OAICustomerFields::~OAICustomerFields() {}

void OAICustomerFields::initializeModel() {

    m_billing_address_isSet = false;
    m_billing_address_isValid = false;

    m_customer_additional_fields_isSet = false;
    m_customer_additional_fields_isValid = false;

    m_customer_categories_isSet = false;
    m_customer_categories_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_phone_isSet = false;
    m_phone_isValid = false;

    m_shipping_address_isSet = false;
    m_shipping_address_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_surname_isSet = false;
    m_surname_isValid = false;
}

void OAICustomerFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomerFields::fromJsonObject(QJsonObject json) {

    m_billing_address_isValid = ::OpenAPI::fromJsonValue(m_billing_address, json[QString("billing_address")]);
    m_billing_address_isSet = !json[QString("billing_address")].isNull() && m_billing_address_isValid;

    m_customer_additional_fields_isValid = ::OpenAPI::fromJsonValue(m_customer_additional_fields, json[QString("customer_additional_fields")]);
    m_customer_additional_fields_isSet = !json[QString("customer_additional_fields")].isNull() && m_customer_additional_fields_isValid;

    m_customer_categories_isValid = ::OpenAPI::fromJsonValue(m_customer_categories, json[QString("customer_categories")]);
    m_customer_categories_isSet = !json[QString("customer_categories")].isNull() && m_customer_categories_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_phone_isValid = ::OpenAPI::fromJsonValue(m_phone, json[QString("phone")]);
    m_phone_isSet = !json[QString("phone")].isNull() && m_phone_isValid;

    m_shipping_address_isValid = ::OpenAPI::fromJsonValue(m_shipping_address, json[QString("shipping_address")]);
    m_shipping_address_isSet = !json[QString("shipping_address")].isNull() && m_shipping_address_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_surname_isValid = ::OpenAPI::fromJsonValue(m_surname, json[QString("surname")]);
    m_surname_isSet = !json[QString("surname")].isNull() && m_surname_isValid;
}

QString OAICustomerFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomerFields::asJsonObject() const {
    QJsonObject obj;
    if (m_billing_address.isSet()) {
        obj.insert(QString("billing_address"), ::OpenAPI::toJsonValue(m_billing_address));
    }
    if (m_customer_additional_fields.size() > 0) {
        obj.insert(QString("customer_additional_fields"), ::OpenAPI::toJsonValue(m_customer_additional_fields));
    }
    if (m_customer_categories.size() > 0) {
        obj.insert(QString("customer_categories"), ::OpenAPI::toJsonValue(m_customer_categories));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_phone_isSet) {
        obj.insert(QString("phone"), ::OpenAPI::toJsonValue(m_phone));
    }
    if (m_shipping_address.isSet()) {
        obj.insert(QString("shipping_address"), ::OpenAPI::toJsonValue(m_shipping_address));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_surname_isSet) {
        obj.insert(QString("surname"), ::OpenAPI::toJsonValue(m_surname));
    }
    return obj;
}

OAIBillingAddress OAICustomerFields::getBillingAddress() const {
    return m_billing_address;
}
void OAICustomerFields::setBillingAddress(const OAIBillingAddress &billing_address) {
    m_billing_address = billing_address;
    m_billing_address_isSet = true;
}

bool OAICustomerFields::is_billing_address_Set() const{
    return m_billing_address_isSet;
}

bool OAICustomerFields::is_billing_address_Valid() const{
    return m_billing_address_isValid;
}

QList<OAICustomerAdditionalField> OAICustomerFields::getCustomerAdditionalFields() const {
    return m_customer_additional_fields;
}
void OAICustomerFields::setCustomerAdditionalFields(const QList<OAICustomerAdditionalField> &customer_additional_fields) {
    m_customer_additional_fields = customer_additional_fields;
    m_customer_additional_fields_isSet = true;
}

bool OAICustomerFields::is_customer_additional_fields_Set() const{
    return m_customer_additional_fields_isSet;
}

bool OAICustomerFields::is_customer_additional_fields_Valid() const{
    return m_customer_additional_fields_isValid;
}

QList<OAICustomerCategory> OAICustomerFields::getCustomerCategories() const {
    return m_customer_categories;
}
void OAICustomerFields::setCustomerCategories(const QList<OAICustomerCategory> &customer_categories) {
    m_customer_categories = customer_categories;
    m_customer_categories_isSet = true;
}

bool OAICustomerFields::is_customer_categories_Set() const{
    return m_customer_categories_isSet;
}

bool OAICustomerFields::is_customer_categories_Valid() const{
    return m_customer_categories_isValid;
}

QString OAICustomerFields::getEmail() const {
    return m_email;
}
void OAICustomerFields::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAICustomerFields::is_email_Set() const{
    return m_email_isSet;
}

bool OAICustomerFields::is_email_Valid() const{
    return m_email_isValid;
}

qint32 OAICustomerFields::getId() const {
    return m_id;
}
void OAICustomerFields::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICustomerFields::is_id_Set() const{
    return m_id_isSet;
}

bool OAICustomerFields::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICustomerFields::getName() const {
    return m_name;
}
void OAICustomerFields::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICustomerFields::is_name_Set() const{
    return m_name_isSet;
}

bool OAICustomerFields::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICustomerFields::getPhone() const {
    return m_phone;
}
void OAICustomerFields::setPhone(const QString &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAICustomerFields::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAICustomerFields::is_phone_Valid() const{
    return m_phone_isValid;
}

OAIShippingAddress OAICustomerFields::getShippingAddress() const {
    return m_shipping_address;
}
void OAICustomerFields::setShippingAddress(const OAIShippingAddress &shipping_address) {
    m_shipping_address = shipping_address;
    m_shipping_address_isSet = true;
}

bool OAICustomerFields::is_shipping_address_Set() const{
    return m_shipping_address_isSet;
}

bool OAICustomerFields::is_shipping_address_Valid() const{
    return m_shipping_address_isValid;
}

QString OAICustomerFields::getStatus() const {
    return m_status;
}
void OAICustomerFields::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAICustomerFields::is_status_Set() const{
    return m_status_isSet;
}

bool OAICustomerFields::is_status_Valid() const{
    return m_status_isValid;
}

QString OAICustomerFields::getSurname() const {
    return m_surname;
}
void OAICustomerFields::setSurname(const QString &surname) {
    m_surname = surname;
    m_surname_isSet = true;
}

bool OAICustomerFields::is_surname_Set() const{
    return m_surname_isSet;
}

bool OAICustomerFields::is_surname_Valid() const{
    return m_surname_isValid;
}

bool OAICustomerFields::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_billing_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_additional_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_surname_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomerFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
