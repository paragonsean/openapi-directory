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

#include "OAIBankAttributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBankAttributes::OAIBankAttributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBankAttributes::OAIBankAttributes() {
    this->initializeModel();
}

OAIBankAttributes::~OAIBankAttributes() {}

void OAIBankAttributes::initializeModel() {

    m_account_number_isSet = false;
    m_account_number_isValid = false;

    m_bank_code_isSet = false;
    m_bank_code_isValid = false;

    m_bic_isSet = false;
    m_bic_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_iban_isSet = false;
    m_iban_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_sort_code_isSet = false;
    m_sort_code_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_vatin_isSet = false;
    m_vatin_isValid = false;
}

void OAIBankAttributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBankAttributes::fromJsonObject(QJsonObject json) {

    m_account_number_isValid = ::OpenAPI::fromJsonValue(m_account_number, json[QString("account_number")]);
    m_account_number_isSet = !json[QString("account_number")].isNull() && m_account_number_isValid;

    m_bank_code_isValid = ::OpenAPI::fromJsonValue(m_bank_code, json[QString("bank_code")]);
    m_bank_code_isSet = !json[QString("bank_code")].isNull() && m_bank_code_isValid;

    m_bic_isValid = ::OpenAPI::fromJsonValue(m_bic, json[QString("bic")]);
    m_bic_isSet = !json[QString("bic")].isNull() && m_bic_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_iban_isValid = ::OpenAPI::fromJsonValue(m_iban, json[QString("iban")]);
    m_iban_isSet = !json[QString("iban")].isNull() && m_iban_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_sort_code_isValid = ::OpenAPI::fromJsonValue(m_sort_code, json[QString("sort_code")]);
    m_sort_code_isSet = !json[QString("sort_code")].isNull() && m_sort_code_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_vatin_isValid = ::OpenAPI::fromJsonValue(m_vatin, json[QString("vatin")]);
    m_vatin_isSet = !json[QString("vatin")].isNull() && m_vatin_isValid;
}

QString OAIBankAttributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBankAttributes::asJsonObject() const {
    QJsonObject obj;
    if (m_account_number_isSet) {
        obj.insert(QString("account_number"), ::OpenAPI::toJsonValue(m_account_number));
    }
    if (m_bank_code_isSet) {
        obj.insert(QString("bank_code"), ::OpenAPI::toJsonValue(m_bank_code));
    }
    if (m_bic_isSet) {
        obj.insert(QString("bic"), ::OpenAPI::toJsonValue(m_bic));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_iban_isSet) {
        obj.insert(QString("iban"), ::OpenAPI::toJsonValue(m_iban));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_sort_code_isSet) {
        obj.insert(QString("sort_code"), ::OpenAPI::toJsonValue(m_sort_code));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_vatin_isSet) {
        obj.insert(QString("vatin"), ::OpenAPI::toJsonValue(m_vatin));
    }
    return obj;
}

QString OAIBankAttributes::getAccountNumber() const {
    return m_account_number;
}
void OAIBankAttributes::setAccountNumber(const QString &account_number) {
    m_account_number = account_number;
    m_account_number_isSet = true;
}

bool OAIBankAttributes::is_account_number_Set() const{
    return m_account_number_isSet;
}

bool OAIBankAttributes::is_account_number_Valid() const{
    return m_account_number_isValid;
}

QString OAIBankAttributes::getBankCode() const {
    return m_bank_code;
}
void OAIBankAttributes::setBankCode(const QString &bank_code) {
    m_bank_code = bank_code;
    m_bank_code_isSet = true;
}

bool OAIBankAttributes::is_bank_code_Set() const{
    return m_bank_code_isSet;
}

bool OAIBankAttributes::is_bank_code_Valid() const{
    return m_bank_code_isValid;
}

QString OAIBankAttributes::getBic() const {
    return m_bic;
}
void OAIBankAttributes::setBic(const QString &bic) {
    m_bic = bic;
    m_bic_isSet = true;
}

bool OAIBankAttributes::is_bic_Set() const{
    return m_bic_isSet;
}

bool OAIBankAttributes::is_bic_Valid() const{
    return m_bic_isValid;
}

QString OAIBankAttributes::getCode() const {
    return m_code;
}
void OAIBankAttributes::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIBankAttributes::is_code_Set() const{
    return m_code_isSet;
}

bool OAIBankAttributes::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIBankAttributes::getIban() const {
    return m_iban;
}
void OAIBankAttributes::setIban(const QString &iban) {
    m_iban = iban;
    m_iban_isSet = true;
}

bool OAIBankAttributes::is_iban_Set() const{
    return m_iban_isSet;
}

bool OAIBankAttributes::is_iban_Valid() const{
    return m_iban_isValid;
}

QString OAIBankAttributes::getName() const {
    return m_name;
}
void OAIBankAttributes::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBankAttributes::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBankAttributes::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIBankAttributes::getSortCode() const {
    return m_sort_code;
}
void OAIBankAttributes::setSortCode(const QString &sort_code) {
    m_sort_code = sort_code;
    m_sort_code_isSet = true;
}

bool OAIBankAttributes::is_sort_code_Set() const{
    return m_sort_code_isSet;
}

bool OAIBankAttributes::is_sort_code_Valid() const{
    return m_sort_code_isValid;
}

QString OAIBankAttributes::getStatus() const {
    return m_status;
}
void OAIBankAttributes::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIBankAttributes::is_status_Set() const{
    return m_status_isSet;
}

bool OAIBankAttributes::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIBankAttributes::getVatin() const {
    return m_vatin;
}
void OAIBankAttributes::setVatin(const QString &vatin) {
    m_vatin = vatin;
    m_vatin_isSet = true;
}

bool OAIBankAttributes::is_vatin_Set() const{
    return m_vatin_isSet;
}

bool OAIBankAttributes::is_vatin_Valid() const{
    return m_vatin_isValid;
}

bool OAIBankAttributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bank_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bic_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_iban_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sort_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vatin_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBankAttributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
