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

#include "OAICountryAttributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICountryAttributes::OAICountryAttributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICountryAttributes::OAICountryAttributes() {
    this->initializeModel();
}

OAICountryAttributes::~OAICountryAttributes() {}

void OAICountryAttributes::initializeModel() {

    m_area_isSet = false;
    m_area_isValid = false;

    m_calling_codes_isSet = false;
    m_calling_codes_isValid = false;

    m_capital_isSet = false;
    m_capital_isValid = false;

    m_code_alpha3_isSet = false;
    m_code_alpha3_isValid = false;

    m_languages_isSet = false;
    m_languages_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_native_name_isSet = false;
    m_native_name_isValid = false;

    m_population_isSet = false;
    m_population_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_sub_region_isSet = false;
    m_sub_region_isValid = false;

    m_timezones_isSet = false;
    m_timezones_isValid = false;

    m_top_level_domains_isSet = false;
    m_top_level_domains_isValid = false;
}

void OAICountryAttributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICountryAttributes::fromJsonObject(QJsonObject json) {

    m_area_isValid = ::OpenAPI::fromJsonValue(m_area, json[QString("area")]);
    m_area_isSet = !json[QString("area")].isNull() && m_area_isValid;

    m_calling_codes_isValid = ::OpenAPI::fromJsonValue(m_calling_codes, json[QString("calling_codes")]);
    m_calling_codes_isSet = !json[QString("calling_codes")].isNull() && m_calling_codes_isValid;

    m_capital_isValid = ::OpenAPI::fromJsonValue(m_capital, json[QString("capital")]);
    m_capital_isSet = !json[QString("capital")].isNull() && m_capital_isValid;

    m_code_alpha3_isValid = ::OpenAPI::fromJsonValue(m_code_alpha3, json[QString("code_alpha3")]);
    m_code_alpha3_isSet = !json[QString("code_alpha3")].isNull() && m_code_alpha3_isValid;

    m_languages_isValid = ::OpenAPI::fromJsonValue(m_languages, json[QString("languages")]);
    m_languages_isSet = !json[QString("languages")].isNull() && m_languages_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_native_name_isValid = ::OpenAPI::fromJsonValue(m_native_name, json[QString("native_name")]);
    m_native_name_isSet = !json[QString("native_name")].isNull() && m_native_name_isValid;

    m_population_isValid = ::OpenAPI::fromJsonValue(m_population, json[QString("population")]);
    m_population_isSet = !json[QString("population")].isNull() && m_population_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_sub_region_isValid = ::OpenAPI::fromJsonValue(m_sub_region, json[QString("sub_region")]);
    m_sub_region_isSet = !json[QString("sub_region")].isNull() && m_sub_region_isValid;

    m_timezones_isValid = ::OpenAPI::fromJsonValue(m_timezones, json[QString("timezones")]);
    m_timezones_isSet = !json[QString("timezones")].isNull() && m_timezones_isValid;

    m_top_level_domains_isValid = ::OpenAPI::fromJsonValue(m_top_level_domains, json[QString("top_level_domains")]);
    m_top_level_domains_isSet = !json[QString("top_level_domains")].isNull() && m_top_level_domains_isValid;
}

QString OAICountryAttributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICountryAttributes::asJsonObject() const {
    QJsonObject obj;
    if (m_area_isSet) {
        obj.insert(QString("area"), ::OpenAPI::toJsonValue(m_area));
    }
    if (m_calling_codes.size() > 0) {
        obj.insert(QString("calling_codes"), ::OpenAPI::toJsonValue(m_calling_codes));
    }
    if (m_capital_isSet) {
        obj.insert(QString("capital"), ::OpenAPI::toJsonValue(m_capital));
    }
    if (m_code_alpha3_isSet) {
        obj.insert(QString("code_alpha3"), ::OpenAPI::toJsonValue(m_code_alpha3));
    }
    if (m_languages.size() > 0) {
        obj.insert(QString("languages"), ::OpenAPI::toJsonValue(m_languages));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_native_name_isSet) {
        obj.insert(QString("native_name"), ::OpenAPI::toJsonValue(m_native_name));
    }
    if (m_population_isSet) {
        obj.insert(QString("population"), ::OpenAPI::toJsonValue(m_population));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_sub_region_isSet) {
        obj.insert(QString("sub_region"), ::OpenAPI::toJsonValue(m_sub_region));
    }
    if (m_timezones.size() > 0) {
        obj.insert(QString("timezones"), ::OpenAPI::toJsonValue(m_timezones));
    }
    if (m_top_level_domains.size() > 0) {
        obj.insert(QString("top_level_domains"), ::OpenAPI::toJsonValue(m_top_level_domains));
    }
    return obj;
}

QString OAICountryAttributes::getArea() const {
    return m_area;
}
void OAICountryAttributes::setArea(const QString &area) {
    m_area = area;
    m_area_isSet = true;
}

bool OAICountryAttributes::is_area_Set() const{
    return m_area_isSet;
}

bool OAICountryAttributes::is_area_Valid() const{
    return m_area_isValid;
}

QList<qint32> OAICountryAttributes::getCallingCodes() const {
    return m_calling_codes;
}
void OAICountryAttributes::setCallingCodes(const QList<qint32> &calling_codes) {
    m_calling_codes = calling_codes;
    m_calling_codes_isSet = true;
}

bool OAICountryAttributes::is_calling_codes_Set() const{
    return m_calling_codes_isSet;
}

bool OAICountryAttributes::is_calling_codes_Valid() const{
    return m_calling_codes_isValid;
}

QString OAICountryAttributes::getCapital() const {
    return m_capital;
}
void OAICountryAttributes::setCapital(const QString &capital) {
    m_capital = capital;
    m_capital_isSet = true;
}

bool OAICountryAttributes::is_capital_Set() const{
    return m_capital_isSet;
}

bool OAICountryAttributes::is_capital_Valid() const{
    return m_capital_isValid;
}

QString OAICountryAttributes::getCodeAlpha3() const {
    return m_code_alpha3;
}
void OAICountryAttributes::setCodeAlpha3(const QString &code_alpha3) {
    m_code_alpha3 = code_alpha3;
    m_code_alpha3_isSet = true;
}

bool OAICountryAttributes::is_code_alpha3_Set() const{
    return m_code_alpha3_isSet;
}

bool OAICountryAttributes::is_code_alpha3_Valid() const{
    return m_code_alpha3_isValid;
}

QList<QString> OAICountryAttributes::getLanguages() const {
    return m_languages;
}
void OAICountryAttributes::setLanguages(const QList<QString> &languages) {
    m_languages = languages;
    m_languages_isSet = true;
}

bool OAICountryAttributes::is_languages_Set() const{
    return m_languages_isSet;
}

bool OAICountryAttributes::is_languages_Valid() const{
    return m_languages_isValid;
}

QString OAICountryAttributes::getName() const {
    return m_name;
}
void OAICountryAttributes::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICountryAttributes::is_name_Set() const{
    return m_name_isSet;
}

bool OAICountryAttributes::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICountryAttributes::getNativeName() const {
    return m_native_name;
}
void OAICountryAttributes::setNativeName(const QString &native_name) {
    m_native_name = native_name;
    m_native_name_isSet = true;
}

bool OAICountryAttributes::is_native_name_Set() const{
    return m_native_name_isSet;
}

bool OAICountryAttributes::is_native_name_Valid() const{
    return m_native_name_isValid;
}

QString OAICountryAttributes::getPopulation() const {
    return m_population;
}
void OAICountryAttributes::setPopulation(const QString &population) {
    m_population = population;
    m_population_isSet = true;
}

bool OAICountryAttributes::is_population_Set() const{
    return m_population_isSet;
}

bool OAICountryAttributes::is_population_Valid() const{
    return m_population_isValid;
}

QString OAICountryAttributes::getRegion() const {
    return m_region;
}
void OAICountryAttributes::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAICountryAttributes::is_region_Set() const{
    return m_region_isSet;
}

bool OAICountryAttributes::is_region_Valid() const{
    return m_region_isValid;
}

QString OAICountryAttributes::getSubRegion() const {
    return m_sub_region;
}
void OAICountryAttributes::setSubRegion(const QString &sub_region) {
    m_sub_region = sub_region;
    m_sub_region_isSet = true;
}

bool OAICountryAttributes::is_sub_region_Set() const{
    return m_sub_region_isSet;
}

bool OAICountryAttributes::is_sub_region_Valid() const{
    return m_sub_region_isValid;
}

QList<QString> OAICountryAttributes::getTimezones() const {
    return m_timezones;
}
void OAICountryAttributes::setTimezones(const QList<QString> &timezones) {
    m_timezones = timezones;
    m_timezones_isSet = true;
}

bool OAICountryAttributes::is_timezones_Set() const{
    return m_timezones_isSet;
}

bool OAICountryAttributes::is_timezones_Valid() const{
    return m_timezones_isValid;
}

QList<QString> OAICountryAttributes::getTopLevelDomains() const {
    return m_top_level_domains;
}
void OAICountryAttributes::setTopLevelDomains(const QList<QString> &top_level_domains) {
    m_top_level_domains = top_level_domains;
    m_top_level_domains_isSet = true;
}

bool OAICountryAttributes::is_top_level_domains_Set() const{
    return m_top_level_domains_isSet;
}

bool OAICountryAttributes::is_top_level_domains_Valid() const{
    return m_top_level_domains_isValid;
}

bool OAICountryAttributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_area_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_calling_codes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_capital_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_alpha3_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_languages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_native_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_population_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sub_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timezones.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_top_level_domains.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICountryAttributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
