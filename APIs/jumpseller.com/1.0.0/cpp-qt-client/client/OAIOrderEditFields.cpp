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

#include "OAIOrderEditFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrderEditFields::OAIOrderEditFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrderEditFields::OAIOrderEditFields() {
    this->initializeModel();
}

OAIOrderEditFields::~OAIOrderEditFields() {}

void OAIOrderEditFields::initializeModel() {

    m_additional_fields_isSet = false;
    m_additional_fields_isValid = false;

    m_additional_information_isSet = false;
    m_additional_information_isValid = false;

    m_shipment_status_isSet = false;
    m_shipment_status_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_tracking_company_isSet = false;
    m_tracking_company_isValid = false;

    m_tracking_number_isSet = false;
    m_tracking_number_isValid = false;

    m_tracking_url_isSet = false;
    m_tracking_url_isValid = false;
}

void OAIOrderEditFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrderEditFields::fromJsonObject(QJsonObject json) {

    m_additional_fields_isValid = ::OpenAPI::fromJsonValue(m_additional_fields, json[QString("additional_fields")]);
    m_additional_fields_isSet = !json[QString("additional_fields")].isNull() && m_additional_fields_isValid;

    m_additional_information_isValid = ::OpenAPI::fromJsonValue(m_additional_information, json[QString("additional_information")]);
    m_additional_information_isSet = !json[QString("additional_information")].isNull() && m_additional_information_isValid;

    m_shipment_status_isValid = ::OpenAPI::fromJsonValue(m_shipment_status, json[QString("shipment_status")]);
    m_shipment_status_isSet = !json[QString("shipment_status")].isNull() && m_shipment_status_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_tracking_company_isValid = ::OpenAPI::fromJsonValue(m_tracking_company, json[QString("tracking_company")]);
    m_tracking_company_isSet = !json[QString("tracking_company")].isNull() && m_tracking_company_isValid;

    m_tracking_number_isValid = ::OpenAPI::fromJsonValue(m_tracking_number, json[QString("tracking_number")]);
    m_tracking_number_isSet = !json[QString("tracking_number")].isNull() && m_tracking_number_isValid;

    m_tracking_url_isValid = ::OpenAPI::fromJsonValue(m_tracking_url, json[QString("tracking_url")]);
    m_tracking_url_isSet = !json[QString("tracking_url")].isNull() && m_tracking_url_isValid;
}

QString OAIOrderEditFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrderEditFields::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_fields.size() > 0) {
        obj.insert(QString("additional_fields"), ::OpenAPI::toJsonValue(m_additional_fields));
    }
    if (m_additional_information_isSet) {
        obj.insert(QString("additional_information"), ::OpenAPI::toJsonValue(m_additional_information));
    }
    if (m_shipment_status_isSet) {
        obj.insert(QString("shipment_status"), ::OpenAPI::toJsonValue(m_shipment_status));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
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

QList<OAIOrderAdditionalFields> OAIOrderEditFields::getAdditionalFields() const {
    return m_additional_fields;
}
void OAIOrderEditFields::setAdditionalFields(const QList<OAIOrderAdditionalFields> &additional_fields) {
    m_additional_fields = additional_fields;
    m_additional_fields_isSet = true;
}

bool OAIOrderEditFields::is_additional_fields_Set() const{
    return m_additional_fields_isSet;
}

bool OAIOrderEditFields::is_additional_fields_Valid() const{
    return m_additional_fields_isValid;
}

QString OAIOrderEditFields::getAdditionalInformation() const {
    return m_additional_information;
}
void OAIOrderEditFields::setAdditionalInformation(const QString &additional_information) {
    m_additional_information = additional_information;
    m_additional_information_isSet = true;
}

bool OAIOrderEditFields::is_additional_information_Set() const{
    return m_additional_information_isSet;
}

bool OAIOrderEditFields::is_additional_information_Valid() const{
    return m_additional_information_isValid;
}

QString OAIOrderEditFields::getShipmentStatus() const {
    return m_shipment_status;
}
void OAIOrderEditFields::setShipmentStatus(const QString &shipment_status) {
    m_shipment_status = shipment_status;
    m_shipment_status_isSet = true;
}

bool OAIOrderEditFields::is_shipment_status_Set() const{
    return m_shipment_status_isSet;
}

bool OAIOrderEditFields::is_shipment_status_Valid() const{
    return m_shipment_status_isValid;
}

QString OAIOrderEditFields::getStatus() const {
    return m_status;
}
void OAIOrderEditFields::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIOrderEditFields::is_status_Set() const{
    return m_status_isSet;
}

bool OAIOrderEditFields::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIOrderEditFields::getTrackingCompany() const {
    return m_tracking_company;
}
void OAIOrderEditFields::setTrackingCompany(const QString &tracking_company) {
    m_tracking_company = tracking_company;
    m_tracking_company_isSet = true;
}

bool OAIOrderEditFields::is_tracking_company_Set() const{
    return m_tracking_company_isSet;
}

bool OAIOrderEditFields::is_tracking_company_Valid() const{
    return m_tracking_company_isValid;
}

QString OAIOrderEditFields::getTrackingNumber() const {
    return m_tracking_number;
}
void OAIOrderEditFields::setTrackingNumber(const QString &tracking_number) {
    m_tracking_number = tracking_number;
    m_tracking_number_isSet = true;
}

bool OAIOrderEditFields::is_tracking_number_Set() const{
    return m_tracking_number_isSet;
}

bool OAIOrderEditFields::is_tracking_number_Valid() const{
    return m_tracking_number_isValid;
}

QString OAIOrderEditFields::getTrackingUrl() const {
    return m_tracking_url;
}
void OAIOrderEditFields::setTrackingUrl(const QString &tracking_url) {
    m_tracking_url = tracking_url;
    m_tracking_url_isSet = true;
}

bool OAIOrderEditFields::is_tracking_url_Set() const{
    return m_tracking_url_isSet;
}

bool OAIOrderEditFields::is_tracking_url_Valid() const{
    return m_tracking_url_isValid;
}

bool OAIOrderEditFields::isSet() const {
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

        if (m_shipment_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
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

bool OAIOrderEditFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
