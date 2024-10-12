/**
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIListFundingAccountsResponseV2.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListFundingAccountsResponseV2::OAIListFundingAccountsResponseV2(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListFundingAccountsResponseV2::OAIListFundingAccountsResponseV2() {
    this->initializeModel();
}

OAIListFundingAccountsResponseV2::~OAIListFundingAccountsResponseV2() {}

void OAIListFundingAccountsResponseV2::initializeModel() {

    m_content_isSet = false;
    m_content_isValid = false;

    m_links_isSet = false;
    m_links_isValid = false;

    m_page_isSet = false;
    m_page_isValid = false;
}

void OAIListFundingAccountsResponseV2::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListFundingAccountsResponseV2::fromJsonObject(QJsonObject json) {

    m_content_isValid = ::OpenAPI::fromJsonValue(m_content, json[QString("content")]);
    m_content_isSet = !json[QString("content")].isNull() && m_content_isValid;

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;

    m_page_isValid = ::OpenAPI::fromJsonValue(m_page, json[QString("page")]);
    m_page_isSet = !json[QString("page")].isNull() && m_page_isValid;
}

QString OAIListFundingAccountsResponseV2::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListFundingAccountsResponseV2::asJsonObject() const {
    QJsonObject obj;
    if (m_content.size() > 0) {
        obj.insert(QString("content"), ::OpenAPI::toJsonValue(m_content));
    }
    if (m_links.size() > 0) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    if (m_page.isSet()) {
        obj.insert(QString("page"), ::OpenAPI::toJsonValue(m_page));
    }
    return obj;
}

QList<OAIFundingAccountResponseV2> OAIListFundingAccountsResponseV2::getContent() const {
    return m_content;
}
void OAIListFundingAccountsResponseV2::setContent(const QList<OAIFundingAccountResponseV2> &content) {
    m_content = content;
    m_content_isSet = true;
}

bool OAIListFundingAccountsResponseV2::is_content_Set() const{
    return m_content_isSet;
}

bool OAIListFundingAccountsResponseV2::is_content_Valid() const{
    return m_content_isValid;
}

QList<OAIListFundingAccountsResponseV2_links> OAIListFundingAccountsResponseV2::getLinks() const {
    return m_links;
}
void OAIListFundingAccountsResponseV2::setLinks(const QList<OAIListFundingAccountsResponseV2_links> &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAIListFundingAccountsResponseV2::is_links_Set() const{
    return m_links_isSet;
}

bool OAIListFundingAccountsResponseV2::is_links_Valid() const{
    return m_links_isValid;
}

OAIListFundingAccountsResponseV2_page OAIListFundingAccountsResponseV2::getPage() const {
    return m_page;
}
void OAIListFundingAccountsResponseV2::setPage(const OAIListFundingAccountsResponseV2_page &page) {
    m_page = page;
    m_page_isSet = true;
}

bool OAIListFundingAccountsResponseV2::is_page_Set() const{
    return m_page_isSet;
}

bool OAIListFundingAccountsResponseV2::is_page_Valid() const{
    return m_page_isValid;
}

bool OAIListFundingAccountsResponseV2::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_content.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_page.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListFundingAccountsResponseV2::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
