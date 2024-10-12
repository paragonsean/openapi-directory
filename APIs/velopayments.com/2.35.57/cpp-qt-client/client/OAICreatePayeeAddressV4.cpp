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

#include "OAICreatePayeeAddressV4.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreatePayeeAddressV4::OAICreatePayeeAddressV4(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreatePayeeAddressV4::OAICreatePayeeAddressV4() {
    this->initializeModel();
}

OAICreatePayeeAddressV4::~OAICreatePayeeAddressV4() {}

void OAICreatePayeeAddressV4::initializeModel() {

    m_city_isSet = false;
    m_city_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_county_or_province_isSet = false;
    m_county_or_province_isValid = false;

    m_line1_isSet = false;
    m_line1_isValid = false;

    m_line2_isSet = false;
    m_line2_isValid = false;

    m_line3_isSet = false;
    m_line3_isValid = false;

    m_line4_isSet = false;
    m_line4_isValid = false;

    m_zip_or_postcode_isSet = false;
    m_zip_or_postcode_isValid = false;
}

void OAICreatePayeeAddressV4::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreatePayeeAddressV4::fromJsonObject(QJsonObject json) {

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_county_or_province_isValid = ::OpenAPI::fromJsonValue(m_county_or_province, json[QString("countyOrProvince")]);
    m_county_or_province_isSet = !json[QString("countyOrProvince")].isNull() && m_county_or_province_isValid;

    m_line1_isValid = ::OpenAPI::fromJsonValue(m_line1, json[QString("line1")]);
    m_line1_isSet = !json[QString("line1")].isNull() && m_line1_isValid;

    m_line2_isValid = ::OpenAPI::fromJsonValue(m_line2, json[QString("line2")]);
    m_line2_isSet = !json[QString("line2")].isNull() && m_line2_isValid;

    m_line3_isValid = ::OpenAPI::fromJsonValue(m_line3, json[QString("line3")]);
    m_line3_isSet = !json[QString("line3")].isNull() && m_line3_isValid;

    m_line4_isValid = ::OpenAPI::fromJsonValue(m_line4, json[QString("line4")]);
    m_line4_isSet = !json[QString("line4")].isNull() && m_line4_isValid;

    m_zip_or_postcode_isValid = ::OpenAPI::fromJsonValue(m_zip_or_postcode, json[QString("zipOrPostcode")]);
    m_zip_or_postcode_isSet = !json[QString("zipOrPostcode")].isNull() && m_zip_or_postcode_isValid;
}

QString OAICreatePayeeAddressV4::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreatePayeeAddressV4::asJsonObject() const {
    QJsonObject obj;
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_county_or_province_isSet) {
        obj.insert(QString("countyOrProvince"), ::OpenAPI::toJsonValue(m_county_or_province));
    }
    if (m_line1_isSet) {
        obj.insert(QString("line1"), ::OpenAPI::toJsonValue(m_line1));
    }
    if (m_line2_isSet) {
        obj.insert(QString("line2"), ::OpenAPI::toJsonValue(m_line2));
    }
    if (m_line3_isSet) {
        obj.insert(QString("line3"), ::OpenAPI::toJsonValue(m_line3));
    }
    if (m_line4_isSet) {
        obj.insert(QString("line4"), ::OpenAPI::toJsonValue(m_line4));
    }
    if (m_zip_or_postcode_isSet) {
        obj.insert(QString("zipOrPostcode"), ::OpenAPI::toJsonValue(m_zip_or_postcode));
    }
    return obj;
}

QString OAICreatePayeeAddressV4::getCity() const {
    return m_city;
}
void OAICreatePayeeAddressV4::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAICreatePayeeAddressV4::is_city_Set() const{
    return m_city_isSet;
}

bool OAICreatePayeeAddressV4::is_city_Valid() const{
    return m_city_isValid;
}

QString OAICreatePayeeAddressV4::getCountry() const {
    return m_country;
}
void OAICreatePayeeAddressV4::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAICreatePayeeAddressV4::is_country_Set() const{
    return m_country_isSet;
}

bool OAICreatePayeeAddressV4::is_country_Valid() const{
    return m_country_isValid;
}

QString OAICreatePayeeAddressV4::getCountyOrProvince() const {
    return m_county_or_province;
}
void OAICreatePayeeAddressV4::setCountyOrProvince(const QString &county_or_province) {
    m_county_or_province = county_or_province;
    m_county_or_province_isSet = true;
}

bool OAICreatePayeeAddressV4::is_county_or_province_Set() const{
    return m_county_or_province_isSet;
}

bool OAICreatePayeeAddressV4::is_county_or_province_Valid() const{
    return m_county_or_province_isValid;
}

QString OAICreatePayeeAddressV4::getLine1() const {
    return m_line1;
}
void OAICreatePayeeAddressV4::setLine1(const QString &line1) {
    m_line1 = line1;
    m_line1_isSet = true;
}

bool OAICreatePayeeAddressV4::is_line1_Set() const{
    return m_line1_isSet;
}

bool OAICreatePayeeAddressV4::is_line1_Valid() const{
    return m_line1_isValid;
}

QString OAICreatePayeeAddressV4::getLine2() const {
    return m_line2;
}
void OAICreatePayeeAddressV4::setLine2(const QString &line2) {
    m_line2 = line2;
    m_line2_isSet = true;
}

bool OAICreatePayeeAddressV4::is_line2_Set() const{
    return m_line2_isSet;
}

bool OAICreatePayeeAddressV4::is_line2_Valid() const{
    return m_line2_isValid;
}

QString OAICreatePayeeAddressV4::getLine3() const {
    return m_line3;
}
void OAICreatePayeeAddressV4::setLine3(const QString &line3) {
    m_line3 = line3;
    m_line3_isSet = true;
}

bool OAICreatePayeeAddressV4::is_line3_Set() const{
    return m_line3_isSet;
}

bool OAICreatePayeeAddressV4::is_line3_Valid() const{
    return m_line3_isValid;
}

QString OAICreatePayeeAddressV4::getLine4() const {
    return m_line4;
}
void OAICreatePayeeAddressV4::setLine4(const QString &line4) {
    m_line4 = line4;
    m_line4_isSet = true;
}

bool OAICreatePayeeAddressV4::is_line4_Set() const{
    return m_line4_isSet;
}

bool OAICreatePayeeAddressV4::is_line4_Valid() const{
    return m_line4_isValid;
}

QString OAICreatePayeeAddressV4::getZipOrPostcode() const {
    return m_zip_or_postcode;
}
void OAICreatePayeeAddressV4::setZipOrPostcode(const QString &zip_or_postcode) {
    m_zip_or_postcode = zip_or_postcode;
    m_zip_or_postcode_isSet = true;
}

bool OAICreatePayeeAddressV4::is_zip_or_postcode_Set() const{
    return m_zip_or_postcode_isSet;
}

bool OAICreatePayeeAddressV4::is_zip_or_postcode_Valid() const{
    return m_zip_or_postcode_isValid;
}

bool OAICreatePayeeAddressV4::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_county_or_province_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line3_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_line4_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_zip_or_postcode_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreatePayeeAddressV4::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_city_isValid && m_country_isValid && m_line1_isValid && true;
}

} // namespace OpenAPI
