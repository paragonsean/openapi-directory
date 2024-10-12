/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICompanyDropdownList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICompanyDropdownList::OAICompanyDropdownList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICompanyDropdownList::OAICompanyDropdownList() {
    this->initializeModel();
}

OAICompanyDropdownList::~OAICompanyDropdownList() {}

void OAICompanyDropdownList::initializeModel() {

    m_companies_isSet = false;
    m_companies_isValid = false;

    m_page_number_isSet = false;
    m_page_number_isValid = false;

    m_page_size_isSet = false;
    m_page_size_isValid = false;

    m_total_count_isSet = false;
    m_total_count_isValid = false;
}

void OAICompanyDropdownList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICompanyDropdownList::fromJsonObject(QJsonObject json) {

    m_companies_isValid = ::OpenAPI::fromJsonValue(m_companies, json[QString("Companies")]);
    m_companies_isSet = !json[QString("Companies")].isNull() && m_companies_isValid;

    m_page_number_isValid = ::OpenAPI::fromJsonValue(m_page_number, json[QString("PageNumber")]);
    m_page_number_isSet = !json[QString("PageNumber")].isNull() && m_page_number_isValid;

    m_page_size_isValid = ::OpenAPI::fromJsonValue(m_page_size, json[QString("PageSize")]);
    m_page_size_isSet = !json[QString("PageSize")].isNull() && m_page_size_isValid;

    m_total_count_isValid = ::OpenAPI::fromJsonValue(m_total_count, json[QString("TotalCount")]);
    m_total_count_isSet = !json[QString("TotalCount")].isNull() && m_total_count_isValid;
}

QString OAICompanyDropdownList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICompanyDropdownList::asJsonObject() const {
    QJsonObject obj;
    if (m_companies.size() > 0) {
        obj.insert(QString("Companies"), ::OpenAPI::toJsonValue(m_companies));
    }
    if (m_page_number_isSet) {
        obj.insert(QString("PageNumber"), ::OpenAPI::toJsonValue(m_page_number));
    }
    if (m_page_size_isSet) {
        obj.insert(QString("PageSize"), ::OpenAPI::toJsonValue(m_page_size));
    }
    if (m_total_count_isSet) {
        obj.insert(QString("TotalCount"), ::OpenAPI::toJsonValue(m_total_count));
    }
    return obj;
}

QList<OAICompanyMinimal> OAICompanyDropdownList::getCompanies() const {
    return m_companies;
}
void OAICompanyDropdownList::setCompanies(const QList<OAICompanyMinimal> &companies) {
    m_companies = companies;
    m_companies_isSet = true;
}

bool OAICompanyDropdownList::is_companies_Set() const{
    return m_companies_isSet;
}

bool OAICompanyDropdownList::is_companies_Valid() const{
    return m_companies_isValid;
}

qint32 OAICompanyDropdownList::getPageNumber() const {
    return m_page_number;
}
void OAICompanyDropdownList::setPageNumber(const qint32 &page_number) {
    m_page_number = page_number;
    m_page_number_isSet = true;
}

bool OAICompanyDropdownList::is_page_number_Set() const{
    return m_page_number_isSet;
}

bool OAICompanyDropdownList::is_page_number_Valid() const{
    return m_page_number_isValid;
}

qint32 OAICompanyDropdownList::getPageSize() const {
    return m_page_size;
}
void OAICompanyDropdownList::setPageSize(const qint32 &page_size) {
    m_page_size = page_size;
    m_page_size_isSet = true;
}

bool OAICompanyDropdownList::is_page_size_Set() const{
    return m_page_size_isSet;
}

bool OAICompanyDropdownList::is_page_size_Valid() const{
    return m_page_size_isValid;
}

qint32 OAICompanyDropdownList::getTotalCount() const {
    return m_total_count;
}
void OAICompanyDropdownList::setTotalCount(const qint32 &total_count) {
    m_total_count = total_count;
    m_total_count_isSet = true;
}

bool OAICompanyDropdownList::is_total_count_Set() const{
    return m_total_count_isSet;
}

bool OAICompanyDropdownList::is_total_count_Valid() const{
    return m_total_count_isValid;
}

bool OAICompanyDropdownList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_companies.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_page_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICompanyDropdownList::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
