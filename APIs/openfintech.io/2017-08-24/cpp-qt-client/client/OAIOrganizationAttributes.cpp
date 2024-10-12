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

#include "OAIOrganizationAttributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrganizationAttributes::OAIOrganizationAttributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrganizationAttributes::OAIOrganizationAttributes() {
    this->initializeModel();
}

OAIOrganizationAttributes::~OAIOrganizationAttributes() {}

void OAIOrganizationAttributes::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_blog_isSet = false;
    m_blog_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_contacts_isSet = false;
    m_contacts_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_icon_isSet = false;
    m_icon_isValid = false;

    m_industries_isSet = false;
    m_industries_isValid = false;

    m_logo_isSet = false;
    m_logo_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_site_isSet = false;
    m_site_isValid = false;

    m_social_profiles_isSet = false;
    m_social_profiles_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_wiki_isSet = false;
    m_wiki_isValid = false;
}

void OAIOrganizationAttributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrganizationAttributes::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_blog_isValid = ::OpenAPI::fromJsonValue(m_blog, json[QString("blog")]);
    m_blog_isSet = !json[QString("blog")].isNull() && m_blog_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_contacts_isValid = ::OpenAPI::fromJsonValue(m_contacts, json[QString("contacts")]);
    m_contacts_isSet = !json[QString("contacts")].isNull() && m_contacts_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_icon_isValid = ::OpenAPI::fromJsonValue(m_icon, json[QString("icon")]);
    m_icon_isSet = !json[QString("icon")].isNull() && m_icon_isValid;

    m_industries_isValid = ::OpenAPI::fromJsonValue(m_industries, json[QString("industries")]);
    m_industries_isSet = !json[QString("industries")].isNull() && m_industries_isValid;

    m_logo_isValid = ::OpenAPI::fromJsonValue(m_logo, json[QString("logo")]);
    m_logo_isSet = !json[QString("logo")].isNull() && m_logo_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_site_isValid = ::OpenAPI::fromJsonValue(m_site, json[QString("site")]);
    m_site_isSet = !json[QString("site")].isNull() && m_site_isValid;

    m_social_profiles_isValid = ::OpenAPI::fromJsonValue(m_social_profiles, json[QString("social_profiles")]);
    m_social_profiles_isSet = !json[QString("social_profiles")].isNull() && m_social_profiles_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_wiki_isValid = ::OpenAPI::fromJsonValue(m_wiki, json[QString("wiki")]);
    m_wiki_isSet = !json[QString("wiki")].isNull() && m_wiki_isValid;
}

QString OAIOrganizationAttributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrganizationAttributes::asJsonObject() const {
    QJsonObject obj;
    if (m_address.isSet()) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_blog_isSet) {
        obj.insert(QString("blog"), ::OpenAPI::toJsonValue(m_blog));
    }
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_contacts.isSet()) {
        obj.insert(QString("contacts"), ::OpenAPI::toJsonValue(m_contacts));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_icon.isSet()) {
        obj.insert(QString("icon"), ::OpenAPI::toJsonValue(m_icon));
    }
    if (m_industries.size() > 0) {
        obj.insert(QString("industries"), ::OpenAPI::toJsonValue(m_industries));
    }
    if (m_logo.isSet()) {
        obj.insert(QString("logo"), ::OpenAPI::toJsonValue(m_logo));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_site_isSet) {
        obj.insert(QString("site"), ::OpenAPI::toJsonValue(m_site));
    }
    if (m_social_profiles.isSet()) {
        obj.insert(QString("social_profiles"), ::OpenAPI::toJsonValue(m_social_profiles));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_wiki_isSet) {
        obj.insert(QString("wiki"), ::OpenAPI::toJsonValue(m_wiki));
    }
    return obj;
}

OAIOrganizationAddress OAIOrganizationAttributes::getAddress() const {
    return m_address;
}
void OAIOrganizationAttributes::setAddress(const OAIOrganizationAddress &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIOrganizationAttributes::is_address_Set() const{
    return m_address_isSet;
}

bool OAIOrganizationAttributes::is_address_Valid() const{
    return m_address_isValid;
}

QString OAIOrganizationAttributes::getBlog() const {
    return m_blog;
}
void OAIOrganizationAttributes::setBlog(const QString &blog) {
    m_blog = blog;
    m_blog_isSet = true;
}

bool OAIOrganizationAttributes::is_blog_Set() const{
    return m_blog_isSet;
}

bool OAIOrganizationAttributes::is_blog_Valid() const{
    return m_blog_isValid;
}

QString OAIOrganizationAttributes::getCode() const {
    return m_code;
}
void OAIOrganizationAttributes::setCode(const QString &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIOrganizationAttributes::is_code_Set() const{
    return m_code_isSet;
}

bool OAIOrganizationAttributes::is_code_Valid() const{
    return m_code_isValid;
}

OAIOrganizationContacts OAIOrganizationAttributes::getContacts() const {
    return m_contacts;
}
void OAIOrganizationAttributes::setContacts(const OAIOrganizationContacts &contacts) {
    m_contacts = contacts;
    m_contacts_isSet = true;
}

bool OAIOrganizationAttributes::is_contacts_Set() const{
    return m_contacts_isSet;
}

bool OAIOrganizationAttributes::is_contacts_Valid() const{
    return m_contacts_isValid;
}

QString OAIOrganizationAttributes::getDescription() const {
    return m_description;
}
void OAIOrganizationAttributes::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIOrganizationAttributes::is_description_Set() const{
    return m_description_isSet;
}

bool OAIOrganizationAttributes::is_description_Valid() const{
    return m_description_isValid;
}

OAIOrganizationAttributesIcon OAIOrganizationAttributes::getIcon() const {
    return m_icon;
}
void OAIOrganizationAttributes::setIcon(const OAIOrganizationAttributesIcon &icon) {
    m_icon = icon;
    m_icon_isSet = true;
}

bool OAIOrganizationAttributes::is_icon_Set() const{
    return m_icon_isSet;
}

bool OAIOrganizationAttributes::is_icon_Valid() const{
    return m_icon_isValid;
}

QList<QString> OAIOrganizationAttributes::getIndustries() const {
    return m_industries;
}
void OAIOrganizationAttributes::setIndustries(const QList<QString> &industries) {
    m_industries = industries;
    m_industries_isSet = true;
}

bool OAIOrganizationAttributes::is_industries_Set() const{
    return m_industries_isSet;
}

bool OAIOrganizationAttributes::is_industries_Valid() const{
    return m_industries_isValid;
}

OAIOrganizationAttributesLogo OAIOrganizationAttributes::getLogo() const {
    return m_logo;
}
void OAIOrganizationAttributes::setLogo(const OAIOrganizationAttributesLogo &logo) {
    m_logo = logo;
    m_logo_isSet = true;
}

bool OAIOrganizationAttributes::is_logo_Set() const{
    return m_logo_isSet;
}

bool OAIOrganizationAttributes::is_logo_Valid() const{
    return m_logo_isValid;
}

QString OAIOrganizationAttributes::getName() const {
    return m_name;
}
void OAIOrganizationAttributes::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIOrganizationAttributes::is_name_Set() const{
    return m_name_isSet;
}

bool OAIOrganizationAttributes::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIOrganizationAttributes::getSite() const {
    return m_site;
}
void OAIOrganizationAttributes::setSite(const QString &site) {
    m_site = site;
    m_site_isSet = true;
}

bool OAIOrganizationAttributes::is_site_Set() const{
    return m_site_isSet;
}

bool OAIOrganizationAttributes::is_site_Valid() const{
    return m_site_isValid;
}

OAIOrganizationSocial OAIOrganizationAttributes::getSocialProfiles() const {
    return m_social_profiles;
}
void OAIOrganizationAttributes::setSocialProfiles(const OAIOrganizationSocial &social_profiles) {
    m_social_profiles = social_profiles;
    m_social_profiles_isSet = true;
}

bool OAIOrganizationAttributes::is_social_profiles_Set() const{
    return m_social_profiles_isSet;
}

bool OAIOrganizationAttributes::is_social_profiles_Valid() const{
    return m_social_profiles_isValid;
}

QString OAIOrganizationAttributes::getStatus() const {
    return m_status;
}
void OAIOrganizationAttributes::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIOrganizationAttributes::is_status_Set() const{
    return m_status_isSet;
}

bool OAIOrganizationAttributes::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIOrganizationAttributes::getWiki() const {
    return m_wiki;
}
void OAIOrganizationAttributes::setWiki(const QString &wiki) {
    m_wiki = wiki;
    m_wiki_isSet = true;
}

bool OAIOrganizationAttributes::is_wiki_Set() const{
    return m_wiki_isSet;
}

bool OAIOrganizationAttributes::is_wiki_Valid() const{
    return m_wiki_isValid;
}

bool OAIOrganizationAttributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_blog_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_contacts.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_icon.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_industries.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_logo.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_site_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_social_profiles.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wiki_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrganizationAttributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
