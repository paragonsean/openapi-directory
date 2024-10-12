/**
 * OpenFinTech.io
 * # Introduction [OpenFinTech.io](https://openfintech.io) is an open database that comprises of standardized primary data for FinTech industry.<br> It contains such information as geolocation data (countries, cities, regions), organizations, currencies (national, digital, virtual, crypto), banks, digital exchangers, payment providers (PSP), payment methods, etc.<br> It is created for communication of cross-integrated micro-services on \"one language\". This is achieved through standardization of entity identifiers that are used to exchange information among different services.<br>  ### UML UML Domain Model diagram you can find [here](https://api.openfintech.io/public_domain_model.png).<br>  ### Persistence Entities are updated not more than 1 time per day.<br>  ### Terms and Conditions This *OpenFinTech.io* is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/).<br> Any rights in individual contents of the database are licensed under the [Database Contents License](http://opendatacommons.org/licenses/dbcl/1.0/).<br>  ### Contacts For any questions, please email - info@openfintech.io<br> Or you can contact us at <a href=\"https://gitter.im/paymaxicom/openfintech.io\">Gitter</a><br>  Powered by [Paymaxi](https://www.paymaxi.com)  # Get Started  If you use [POSTMAN](https://www.getpostman.com) or similar program which can operate with swagger`s files - just [download](https://docs.openfintech.io) our spec and [import it](https://www.getpostman.com/docs/importing_swagger). Also you can try live [API demo](https://api.openfintech.io).  ## Overview  The OpenFinTech API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors.<br> API is based on [JSON API](http://jsonapi.org) standard. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.<br> JSON API requires use of the JSON API media type (`application/vnd.api+json`) for exchanging data.<br> ### Additional Request Headers #### ACCEPT HEADER Your requests should always include the header: ```curl Accept: application/vnd.api+json ```  ## Authentication  To use OpenFinTech API no needed authorization.  ## Versioning  When we make changes to the API, we release new, dated versions. The current version is **2017-08-24**. Read our [API upgrades guide]() to see our API changelog and to learn more about backwards compatibility.  ## Pagination  OpenFinTech APIs to retrieve lists of banks, currencies and other resources - paginated to **100** items by default. The pagination information will be included in the list API response under the node name `meta` - contains information about listed objects [`total` - contains information about total count of listed objects, `pages` - count of pages], `links` - contain links to navigate between pages [`first` - link to first page, `prev` - link to previous page, `next` - link to next page, `last` - link to last page].<br> By default first page will be listed. For navigating through pages, use the page parameter (e.g. `page[number]`, `page[size]`).<br> The `page[size]` parameter can be used to set the number of records that you want to receive in the response.<br> The `page[number]` parameter can be used to set needed page number.<br> Example of response: ```json {   \"meta\": {     \"total\": 419,     \"pages\": 42   },   \"links\": {     \"first\": \"/v1/{path}?page[number]=1&page[size]=10\",     \"prev\": \"/v1/{path}?page[number]=39&page[size]=10\",     \"next\": \"/v1/{path}?page[number]=41&page[size]=10\",     \"last\": \"/v1/{path}?page[number]=42&page[size]=10\"   } ```  ### Sorting  OpenFinTech\\`s API supported query parameter to sort result collection [e.g. `?sort=code`]. Information about available parameters may be found in the endpoint description. Positive parameter [e.g. `?sort=code`] points to ascending sorting, negative  [e.g. `?sort=-code`] - to descending sorting. Also, supported multiple sorting parameters [e.g. `?sort=code, -name, id`, etc.] ```curl https://api.openfintech.io/v1/countries?sort=name,-area ```  ### Filtering  Filtering provided by unique query key `filter[*filtering_condition*]`. Information about available parameters may be found in the endpoint description. ```curl https://api.openfintech.io/v1/countries?filter[region]=europe ```  ## Images  OpenFinTech provides two types of images: icons and logos. To get one of those types you should to use next url pattern: ``` curl https://api.openfintech.io/v1/{path}/{id}/{icon/logo} ``` Also, images can be resized by adding next parameters: `h={height}&w={width}`. For example, you want to get organization icon with width equals to 20 pixels: ``` curl https://api.openfintech.io/v1/organizations/{id}/icon?w=20&h=20 ``` If argument height or width is missing API returns original image with real sizes.  ## Errors  API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the `5xx` range indicate an error with OpenFinTech's servers (these are rare).  | Code | Description | |------|-------------| | 200 - OK | Everything worked as expected. | | 400 - Bad Request | The request was unacceptable, often due to missing a required parameter. | | 401 - Unauthorized | No valid API key provided. | | 402 - Request Failed | The parameters were valid but the request failed. | | 404 - Not Found | The requested resource doesn't exist. | | 409 - Conflict | The request conflicts with another request (perhaps due to using the same idempotent key). | | 429 - Too Many Requests | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. | | 500, 502, 503, 504 - Server Errors | Something went wrong on OpenFinTech's end. (These are rare.) | 
 *
 * The version of the OpenAPI document: 2017-08-24
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICurrencyAttributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICurrencyAttributes::OAICurrencyAttributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICurrencyAttributes::OAICurrencyAttributes() {
    this->initializeModel();
}

OAICurrencyAttributes::~OAICurrencyAttributes() {}

void OAICurrencyAttributes::initializeModel() {

    m_category_isSet = false;
    m_category_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_code_estandards_alpha_isSet = false;
    m_code_estandards_alpha_isValid = false;

    m_code_iso_alpha3_isSet = false;
    m_code_iso_alpha3_isValid = false;

    m_code_iso_numeric3_isSet = false;
    m_code_iso_numeric3_isValid = false;

    m_code_json_alpha_isSet = false;
    m_code_json_alpha_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_currency_type_isSet = false;
    m_currency_type_isValid = false;

    m_decimal_e_isSet = false;
    m_decimal_e_isValid = false;

    m_icon_isSet = false;
    m_icon_isValid = false;

    m_issuer_isSet = false;
    m_issuer_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_native_symbol_isSet = false;
    m_native_symbol_isValid = false;

    m_symbol_isSet = false;
    m_symbol_isValid = false;
}

void OAICurrencyAttributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICurrencyAttributes::fromJsonObject(QJsonObject json) {

    m_category_isValid = ::OpenAPI::fromJsonValue(m_category, json[QString("category")]);
    m_category_isSet = !json[QString("category")].isNull() && m_category_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_code_estandards_alpha_isValid = ::OpenAPI::fromJsonValue(m_code_estandards_alpha, json[QString("code_estandards_alpha")]);
    m_code_estandards_alpha_isSet = !json[QString("code_estandards_alpha")].isNull() && m_code_estandards_alpha_isValid;

    m_code_iso_alpha3_isValid = ::OpenAPI::fromJsonValue(m_code_iso_alpha3, json[QString("code_iso_alpha3")]);
    m_code_iso_alpha3_isSet = !json[QString("code_iso_alpha3")].isNull() && m_code_iso_alpha3_isValid;

    m_code_iso_numeric3_isValid = ::OpenAPI::fromJsonValue(m_code_iso_numeric3, json[QString("code_iso_numeric3")]);
    m_code_iso_numeric3_isSet = !json[QString("code_iso_numeric3")].isNull() && m_code_iso_numeric3_isValid;

    m_code_json_alpha_isValid = ::OpenAPI::fromJsonValue(m_code_json_alpha, json[QString("code_json_alpha")]);
    m_code_json_alpha_isSet = !json[QString("code_json_alpha")].isNull() && m_code_json_alpha_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_currency_type_isValid = ::OpenAPI::fromJsonValue(m_currency_type, json[QString("currency_type")]);
    m_currency_type_isSet = !json[QString("currency_type")].isNull() && m_currency_type_isValid;

    m_decimal_e_isValid = ::OpenAPI::fromJsonValue(m_decimal_e, json[QString("decimal_e")]);
    m_decimal_e_isSet = !json[QString("decimal_e")].isNull() && m_decimal_e_isValid;

    m_icon_isValid = ::OpenAPI::fromJsonValue(m_icon, json[QString("icon")]);
    m_icon_isSet = !json[QString("icon")].isNull() && m_icon_isValid;

    m_issuer_isValid = ::OpenAPI::fromJsonValue(m_issuer, json[QString("issuer")]);
    m_issuer_isSet = !json[QString("issuer")].isNull() && m_issuer_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_native_symbol_isValid = ::OpenAPI::fromJsonValue(m_native_symbol, json[QString("native_symbol")]);
    m_native_symbol_isSet = !json[QString("native_symbol")].isNull() && m_native_symbol_isValid;

    m_symbol_isValid = ::OpenAPI::fromJsonValue(m_symbol, json[QString("symbol")]);
    m_symbol_isSet = !json[QString("symbol")].isNull() && m_symbol_isValid;
}

QString OAICurrencyAttributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICurrencyAttributes::asJsonObject() const {
    QJsonObject obj;
    if (m_category_isSet) {
        obj.insert(QString("category"), ::OpenAPI::toJsonValue(m_category));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_code_estandards_alpha_isSet) {
        obj.insert(QString("code_estandards_alpha"), ::OpenAPI::toJsonValue(m_code_estandards_alpha));
    }
    if (m_code_iso_alpha3_isSet) {
        obj.insert(QString("code_iso_alpha3"), ::OpenAPI::toJsonValue(m_code_iso_alpha3));
    }
    if (m_code_iso_numeric3_isSet) {
        obj.insert(QString("code_iso_numeric3"), ::OpenAPI::toJsonValue(m_code_iso_numeric3));
    }
    if (m_code_json_alpha_isSet) {
        obj.insert(QString("code_json_alpha"), ::OpenAPI::toJsonValue(m_code_json_alpha));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_currency_type_isSet) {
        obj.insert(QString("currency_type"), ::OpenAPI::toJsonValue(m_currency_type));
    }
    if (m_decimal_e_isSet) {
        obj.insert(QString("decimal_e"), ::OpenAPI::toJsonValue(m_decimal_e));
    }
    if (m_icon.isSet()) {
        obj.insert(QString("icon"), ::OpenAPI::toJsonValue(m_icon));
    }
    if (m_issuer_isSet) {
        obj.insert(QString("issuer"), ::OpenAPI::toJsonValue(m_issuer));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_native_symbol_isSet) {
        obj.insert(QString("native_symbol"), ::OpenAPI::toJsonValue(m_native_symbol));
    }
    if (m_symbol_isSet) {
        obj.insert(QString("symbol"), ::OpenAPI::toJsonValue(m_symbol));
    }
    return obj;
}

QString OAICurrencyAttributes::getCategory() const {
    return m_category;
}
void OAICurrencyAttributes::setCategory(const QString &category) {
    m_category = category;
    m_category_isSet = true;
}

bool OAICurrencyAttributes::is_category_Set() const{
    return m_category_isSet;
}

bool OAICurrencyAttributes::is_category_Valid() const{
    return m_category_isValid;
}

QString OAICurrencyAttributes::getCode() const {
    return m_code;
}
void OAICurrencyAttributes::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAICurrencyAttributes::is_code_Set() const{
    return m_code_isSet;
}

bool OAICurrencyAttributes::is_code_Valid() const{
    return m_code_isValid;
}

QString OAICurrencyAttributes::getCodeEstandardsAlpha() const {
    return m_code_estandards_alpha;
}
void OAICurrencyAttributes::setCodeEstandardsAlpha(const QString &code_estandards_alpha) {
    m_code_estandards_alpha = code_estandards_alpha;
    m_code_estandards_alpha_isSet = true;
}

bool OAICurrencyAttributes::is_code_estandards_alpha_Set() const{
    return m_code_estandards_alpha_isSet;
}

bool OAICurrencyAttributes::is_code_estandards_alpha_Valid() const{
    return m_code_estandards_alpha_isValid;
}

QString OAICurrencyAttributes::getCodeIsoAlpha3() const {
    return m_code_iso_alpha3;
}
void OAICurrencyAttributes::setCodeIsoAlpha3(const QString &code_iso_alpha3) {
    m_code_iso_alpha3 = code_iso_alpha3;
    m_code_iso_alpha3_isSet = true;
}

bool OAICurrencyAttributes::is_code_iso_alpha3_Set() const{
    return m_code_iso_alpha3_isSet;
}

bool OAICurrencyAttributes::is_code_iso_alpha3_Valid() const{
    return m_code_iso_alpha3_isValid;
}

qint32 OAICurrencyAttributes::getCodeIsoNumeric3() const {
    return m_code_iso_numeric3;
}
void OAICurrencyAttributes::setCodeIsoNumeric3(const qint32 &code_iso_numeric3) {
    m_code_iso_numeric3 = code_iso_numeric3;
    m_code_iso_numeric3_isSet = true;
}

bool OAICurrencyAttributes::is_code_iso_numeric3_Set() const{
    return m_code_iso_numeric3_isSet;
}

bool OAICurrencyAttributes::is_code_iso_numeric3_Valid() const{
    return m_code_iso_numeric3_isValid;
}

QString OAICurrencyAttributes::getCodeJsonAlpha() const {
    return m_code_json_alpha;
}
void OAICurrencyAttributes::setCodeJsonAlpha(const QString &code_json_alpha) {
    m_code_json_alpha = code_json_alpha;
    m_code_json_alpha_isSet = true;
}

bool OAICurrencyAttributes::is_code_json_alpha_Set() const{
    return m_code_json_alpha_isSet;
}

bool OAICurrencyAttributes::is_code_json_alpha_Valid() const{
    return m_code_json_alpha_isValid;
}

QString OAICurrencyAttributes::getCreated() const {
    return m_created;
}
void OAICurrencyAttributes::setCreated(const QString &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAICurrencyAttributes::is_created_Set() const{
    return m_created_isSet;
}

bool OAICurrencyAttributes::is_created_Valid() const{
    return m_created_isValid;
}

QString OAICurrencyAttributes::getCurrencyType() const {
    return m_currency_type;
}
void OAICurrencyAttributes::setCurrencyType(const QString &currency_type) {
    m_currency_type = currency_type;
    m_currency_type_isSet = true;
}

bool OAICurrencyAttributes::is_currency_type_Set() const{
    return m_currency_type_isSet;
}

bool OAICurrencyAttributes::is_currency_type_Valid() const{
    return m_currency_type_isValid;
}

QString OAICurrencyAttributes::getDecimalE() const {
    return m_decimal_e;
}
void OAICurrencyAttributes::setDecimalE(const QString &decimal_e) {
    m_decimal_e = decimal_e;
    m_decimal_e_isSet = true;
}

bool OAICurrencyAttributes::is_decimal_e_Set() const{
    return m_decimal_e_isSet;
}

bool OAICurrencyAttributes::is_decimal_e_Valid() const{
    return m_decimal_e_isValid;
}

OAICurrencyAttributesIcon OAICurrencyAttributes::getIcon() const {
    return m_icon;
}
void OAICurrencyAttributes::setIcon(const OAICurrencyAttributesIcon &icon) {
    m_icon = icon;
    m_icon_isSet = true;
}

bool OAICurrencyAttributes::is_icon_Set() const{
    return m_icon_isSet;
}

bool OAICurrencyAttributes::is_icon_Valid() const{
    return m_icon_isValid;
}

QString OAICurrencyAttributes::getIssuer() const {
    return m_issuer;
}
void OAICurrencyAttributes::setIssuer(const QString &issuer) {
    m_issuer = issuer;
    m_issuer_isSet = true;
}

bool OAICurrencyAttributes::is_issuer_Set() const{
    return m_issuer_isSet;
}

bool OAICurrencyAttributes::is_issuer_Valid() const{
    return m_issuer_isValid;
}

QString OAICurrencyAttributes::getName() const {
    return m_name;
}
void OAICurrencyAttributes::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICurrencyAttributes::is_name_Set() const{
    return m_name_isSet;
}

bool OAICurrencyAttributes::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICurrencyAttributes::getNativeSymbol() const {
    return m_native_symbol;
}
void OAICurrencyAttributes::setNativeSymbol(const QString &native_symbol) {
    m_native_symbol = native_symbol;
    m_native_symbol_isSet = true;
}

bool OAICurrencyAttributes::is_native_symbol_Set() const{
    return m_native_symbol_isSet;
}

bool OAICurrencyAttributes::is_native_symbol_Valid() const{
    return m_native_symbol_isValid;
}

QString OAICurrencyAttributes::getSymbol() const {
    return m_symbol;
}
void OAICurrencyAttributes::setSymbol(const QString &symbol) {
    m_symbol = symbol;
    m_symbol_isSet = true;
}

bool OAICurrencyAttributes::is_symbol_Set() const{
    return m_symbol_isSet;
}

bool OAICurrencyAttributes::is_symbol_Valid() const{
    return m_symbol_isValid;
}

bool OAICurrencyAttributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_category_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_estandards_alpha_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_iso_alpha3_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_iso_numeric3_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_json_alpha_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_decimal_e_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_icon.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_issuer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_native_symbol_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_symbol_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICurrencyAttributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
