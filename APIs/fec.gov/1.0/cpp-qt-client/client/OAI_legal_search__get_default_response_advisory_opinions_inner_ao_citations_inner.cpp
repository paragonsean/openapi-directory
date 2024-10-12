/**
 * OpenFEC
 * This application programming interface (API) allows you to explore the way candidates and committees fund their campaigns.    The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There are a lot of data, and a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in the `/schedule_a/` endpoints.    <b class=\"body\" id=\"getting_started_head\">Getting started with the openFEC API</b><br>    If you would like to use the FEC's API programmatically, you can sign up for your own API key using our form. Alternatively, you can still try out our API without an API key by using the web interface and using DEMO_KEY. Note that when you use the openFEC API you are subject to the [Terms of Service](https://github.com/fecgov/FEC/blob/master/TERMS-OF-SERVICE.md) and [Acceptable Use policy](https://github.com/fecgov/FEC/blob/master/ACCEPTABLE-USE-POLICY.md).    Signing up for an API key will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 7,200 calls an hour (120 calls per minute) to <a href=\"mailto:APIinfo@fec.gov\">APIinfo@fec.gov</a>. You can also ask questions and discuss the data in a community led [group](https://groups.google.com/forum/#!forum/fec-data).    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [Inspect our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!    <p><br></p> <h2 class=\"title\" id=\"signup_head\">Sign up for an API key</h2> <div id=\"apidatagov_signup\">Loading signup form...</div>
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner() {
    this->initializeModel();
}

OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::~OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner() {}

void OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_r_false_isSet = false;
    m_r_false_isValid = false;
}

void OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_r_false_isValid = ::OpenAPI::fromJsonValue(m_r_false, json[QString("false")]);
    m_r_false_isSet = !json[QString("false")].isNull() && m_r_false_isValid;
}

QString OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_r_false_isSet) {
        obj.insert(QString("false"), ::OpenAPI::toJsonValue(m_r_false));
    }
    return obj;
}

QString OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::getName() const {
    return m_name;
}
void OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::getRFalse() const {
    return m_r_false;
}
void OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::setRFalse(const QString &r_false) {
    m_r_false = r_false;
    m_r_false_isSet = true;
}

bool OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::is_r_false_Set() const{
    return m_r_false_isSet;
}

bool OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::is_r_false_Valid() const{
    return m_r_false_isValid;
}

bool OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_false_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
