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

#include "OAIPaymentProviderAttributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPaymentProviderAttributes::OAIPaymentProviderAttributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPaymentProviderAttributes::OAIPaymentProviderAttributes() {
    this->initializeModel();
}

OAIPaymentProviderAttributes::~OAIPaymentProviderAttributes() {}

void OAIPaymentProviderAttributes::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_features_isSet = false;
    m_features_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_sales_channels_isSet = false;
    m_sales_channels_isValid = false;

    m_types_isSet = false;
    m_types_isValid = false;
}

void OAIPaymentProviderAttributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPaymentProviderAttributes::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_features_isValid = ::OpenAPI::fromJsonValue(m_features, json[QString("features")]);
    m_features_isSet = !json[QString("features")].isNull() && m_features_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_sales_channels_isValid = ::OpenAPI::fromJsonValue(m_sales_channels, json[QString("sales_channels")]);
    m_sales_channels_isSet = !json[QString("sales_channels")].isNull() && m_sales_channels_isValid;

    m_types_isValid = ::OpenAPI::fromJsonValue(m_types, json[QString("types")]);
    m_types_isSet = !json[QString("types")].isNull() && m_types_isValid;
}

QString OAIPaymentProviderAttributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPaymentProviderAttributes::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_features.size() > 0) {
        obj.insert(QString("features"), ::OpenAPI::toJsonValue(m_features));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_sales_channels.size() > 0) {
        obj.insert(QString("sales_channels"), ::OpenAPI::toJsonValue(m_sales_channels));
    }
    if (m_types.size() > 0) {
        obj.insert(QString("types"), ::OpenAPI::toJsonValue(m_types));
    }
    return obj;
}

QString OAIPaymentProviderAttributes::getCode() const {
    return m_code;
}
void OAIPaymentProviderAttributes::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIPaymentProviderAttributes::is_code_Set() const{
    return m_code_isSet;
}

bool OAIPaymentProviderAttributes::is_code_Valid() const{
    return m_code_isValid;
}

QList<QString> OAIPaymentProviderAttributes::getFeatures() const {
    return m_features;
}
void OAIPaymentProviderAttributes::setFeatures(const QList<QString> &features) {
    m_features = features;
    m_features_isSet = true;
}

bool OAIPaymentProviderAttributes::is_features_Set() const{
    return m_features_isSet;
}

bool OAIPaymentProviderAttributes::is_features_Valid() const{
    return m_features_isValid;
}

QString OAIPaymentProviderAttributes::getName() const {
    return m_name;
}
void OAIPaymentProviderAttributes::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPaymentProviderAttributes::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPaymentProviderAttributes::is_name_Valid() const{
    return m_name_isValid;
}

QList<QString> OAIPaymentProviderAttributes::getSalesChannels() const {
    return m_sales_channels;
}
void OAIPaymentProviderAttributes::setSalesChannels(const QList<QString> &sales_channels) {
    m_sales_channels = sales_channels;
    m_sales_channels_isSet = true;
}

bool OAIPaymentProviderAttributes::is_sales_channels_Set() const{
    return m_sales_channels_isSet;
}

bool OAIPaymentProviderAttributes::is_sales_channels_Valid() const{
    return m_sales_channels_isValid;
}

QList<QString> OAIPaymentProviderAttributes::getTypes() const {
    return m_types;
}
void OAIPaymentProviderAttributes::setTypes(const QList<QString> &types) {
    m_types = types;
    m_types_isSet = true;
}

bool OAIPaymentProviderAttributes::is_types_Set() const{
    return m_types_isSet;
}

bool OAIPaymentProviderAttributes::is_types_Valid() const{
    return m_types_isValid;
}

bool OAIPaymentProviderAttributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_features.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sales_channels.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_types.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPaymentProviderAttributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
