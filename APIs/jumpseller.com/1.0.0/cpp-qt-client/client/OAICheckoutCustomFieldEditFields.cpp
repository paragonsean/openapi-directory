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

#include "OAICheckoutCustomFieldEditFields.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICheckoutCustomFieldEditFields::OAICheckoutCustomFieldEditFields(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICheckoutCustomFieldEditFields::OAICheckoutCustomFieldEditFields() {
    this->initializeModel();
}

OAICheckoutCustomFieldEditFields::~OAICheckoutCustomFieldEditFields() {}

void OAICheckoutCustomFieldEditFields::initializeModel() {

    m_area_isSet = false;
    m_area_isValid = false;

    m_custom_field_select_options_isSet = false;
    m_custom_field_select_options_isValid = false;

    m_deletable_isSet = false;
    m_deletable_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_required_isSet = false;
    m_required_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAICheckoutCustomFieldEditFields::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICheckoutCustomFieldEditFields::fromJsonObject(QJsonObject json) {

    m_area_isValid = ::OpenAPI::fromJsonValue(m_area, json[QString("area")]);
    m_area_isSet = !json[QString("area")].isNull() && m_area_isValid;

    m_custom_field_select_options_isValid = ::OpenAPI::fromJsonValue(m_custom_field_select_options, json[QString("custom_field_select_options")]);
    m_custom_field_select_options_isSet = !json[QString("custom_field_select_options")].isNull() && m_custom_field_select_options_isValid;

    m_deletable_isValid = ::OpenAPI::fromJsonValue(m_deletable, json[QString("deletable")]);
    m_deletable_isSet = !json[QString("deletable")].isNull() && m_deletable_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("position")]);
    m_position_isSet = !json[QString("position")].isNull() && m_position_isValid;

    m_required_isValid = ::OpenAPI::fromJsonValue(m_required, json[QString("required")]);
    m_required_isSet = !json[QString("required")].isNull() && m_required_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAICheckoutCustomFieldEditFields::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICheckoutCustomFieldEditFields::asJsonObject() const {
    QJsonObject obj;
    if (m_area_isSet) {
        obj.insert(QString("area"), ::OpenAPI::toJsonValue(m_area));
    }
    if (m_custom_field_select_options.size() > 0) {
        obj.insert(QString("custom_field_select_options"), ::OpenAPI::toJsonValue(m_custom_field_select_options));
    }
    if (m_deletable_isSet) {
        obj.insert(QString("deletable"), ::OpenAPI::toJsonValue(m_deletable));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_position_isSet) {
        obj.insert(QString("position"), ::OpenAPI::toJsonValue(m_position));
    }
    if (m_required_isSet) {
        obj.insert(QString("required"), ::OpenAPI::toJsonValue(m_required));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAICheckoutCustomFieldEditFields::getArea() const {
    return m_area;
}
void OAICheckoutCustomFieldEditFields::setArea(const QString &area) {
    m_area = area;
    m_area_isSet = true;
}

bool OAICheckoutCustomFieldEditFields::is_area_Set() const{
    return m_area_isSet;
}

bool OAICheckoutCustomFieldEditFields::is_area_Valid() const{
    return m_area_isValid;
}

QList<QString> OAICheckoutCustomFieldEditFields::getCustomFieldSelectOptions() const {
    return m_custom_field_select_options;
}
void OAICheckoutCustomFieldEditFields::setCustomFieldSelectOptions(const QList<QString> &custom_field_select_options) {
    m_custom_field_select_options = custom_field_select_options;
    m_custom_field_select_options_isSet = true;
}

bool OAICheckoutCustomFieldEditFields::is_custom_field_select_options_Set() const{
    return m_custom_field_select_options_isSet;
}

bool OAICheckoutCustomFieldEditFields::is_custom_field_select_options_Valid() const{
    return m_custom_field_select_options_isValid;
}

bool OAICheckoutCustomFieldEditFields::isDeletable() const {
    return m_deletable;
}
void OAICheckoutCustomFieldEditFields::setDeletable(const bool &deletable) {
    m_deletable = deletable;
    m_deletable_isSet = true;
}

bool OAICheckoutCustomFieldEditFields::is_deletable_Set() const{
    return m_deletable_isSet;
}

bool OAICheckoutCustomFieldEditFields::is_deletable_Valid() const{
    return m_deletable_isValid;
}

QString OAICheckoutCustomFieldEditFields::getLabel() const {
    return m_label;
}
void OAICheckoutCustomFieldEditFields::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAICheckoutCustomFieldEditFields::is_label_Set() const{
    return m_label_isSet;
}

bool OAICheckoutCustomFieldEditFields::is_label_Valid() const{
    return m_label_isValid;
}

qint32 OAICheckoutCustomFieldEditFields::getPosition() const {
    return m_position;
}
void OAICheckoutCustomFieldEditFields::setPosition(const qint32 &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAICheckoutCustomFieldEditFields::is_position_Set() const{
    return m_position_isSet;
}

bool OAICheckoutCustomFieldEditFields::is_position_Valid() const{
    return m_position_isValid;
}

bool OAICheckoutCustomFieldEditFields::isRequired() const {
    return m_required;
}
void OAICheckoutCustomFieldEditFields::setRequired(const bool &required) {
    m_required = required;
    m_required_isSet = true;
}

bool OAICheckoutCustomFieldEditFields::is_required_Set() const{
    return m_required_isSet;
}

bool OAICheckoutCustomFieldEditFields::is_required_Valid() const{
    return m_required_isValid;
}

QString OAICheckoutCustomFieldEditFields::getType() const {
    return m_type;
}
void OAICheckoutCustomFieldEditFields::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICheckoutCustomFieldEditFields::is_type_Set() const{
    return m_type_isSet;
}

bool OAICheckoutCustomFieldEditFields::is_type_Valid() const{
    return m_type_isValid;
}

bool OAICheckoutCustomFieldEditFields::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_area_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_field_select_options.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_deletable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_required_isSet) {
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

bool OAICheckoutCustomFieldEditFields::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
