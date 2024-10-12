/**
 * Public Api
 * # Introduction  This API allows resellers to manage their resources in a simple, programmatic way using HTTP requests.  # Conventions  ## Requests  The API supports different methods depending on the required action.  | Method | Description | ---  | --- | GET  | Retrieve resources in a collection or get a single resource.<br/>Getters will never have any effect on the queried resources. | POST  | Create a new resource in a collection. | PUT  | Update an existing resource with its new representation. | DELETE | Delete an existing resource.  ## HTTP status codes  The API will reply with different HTTP statuscodes:  | StatusCode    | Description | ---      | --- | 200 OK     | The requests was processed and you receive data as a result. | 201 CREATED    | The resource has been created. Either the Location header contains a link to the created resource, or links are being returned in the response body. The applied method will be indicated in the documentation. | 202 ACCEPTED    | The request has been validated and accepted. Because we need to do some background processing prior to returning the result, we cannot send back a useful representation. | 204 NOCONTENT    | The request has been processed, but no details can be returned. | 400 BADREQUEST   | Your request is malformed. | 401 UNAUTHORIZED   | You are not authorized. Follow the instructions in the Authorization documentation. | 403 FORBIDDEN    | Access to the resource or operation is not allowed. | 404 NOTFOUND    | The resource cannot be found. | 410 GONE                  | The resource is permanently no longer available. | 429 TOOMANYREQUESTS  | The ratelimit has been exceeded. Please refer to the documentation on rate limiting for more details. | 500 INTERNALSERVERERROR | An error occurred during the processing of the request. The error is unexpected and most likely due to a bug in the api.  In the event of a problem, the body of the response will usually contain an errorcode and errormessage. In rare cases additional details about the error are reported.  Errorcodes 400-499 are considered to be client errors and indicate that there was an issue with the request. We will not take any action besides monitoring.   Errorcodes 500-599 are considered to be server errors. The errors are monitored AND action will be taken to resolve the error.  ## Formatting  Snake casing is applied on resources and query parameters. The API is strictly returning JSON. No other formats are supported.  Datetimes are returned in ISO-8601 format.  ## Pagination  Pagination is on by default on collections and is controlled by specifying *skip* and *take* parameters.   **Skip** indicates the number of results to skip and where to start the new take.   **Take** indicates the number of records to return. The returned number of items can be smaller than the requested take.  Paged results will have headers with useful information regarding the paging.  | Header    | Description | ---     | --- | X-Paging-Skipped  | The number of results that have been skipped. | X-Paging-Take   | The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. | X-Paging-TotalResults | The total number of results regardless of paging.  ## Rate limiting  The number of requests per interval is limited. Detailed information on the rate limiting can be found in specific headers which will be sent on each request.  | Header    | Description | ---     | --- | X-RateLimit-Limit  | The number of requests that can be made in a specific time interval. | X-RateLimit-Usage  | The number of requests already made in the current time interval. | X-RateLimit-Remaining | The number of requests remaining until the reset. | X-RateLimit-Reset  | The number of seconds until the reset.<br />After the reset you are allowed to make as many requests as specified by the X-RateLimit-Limit header. | Retry-After   | The number of seconds you have to wait until you can make new requests.<br />This header is only present when the rate limit has been reached. It is identical to X-RateLimit-Reset.  When the ratelimit has been reached, all requests will return with a HTTP statuscode 429 and ReasonPhrase '*Too many requests, retry later.*'.  # Authentication  The Api uses HMAC authentication.   Hash-based message authentication code (HMAC) is a mechanism for calculating a message authentication code involving a hash function in combination with a secret key.   Both the integrity and the authenticity of the message are verified this way.  ## Steps to generate the HMAC  1. Get your api key and secret from your controlpanel.   It is absolutely vital that the secret is never exposed. Once the secret is out, anyone would be able to generate hmacs to impersonate you.   In case your secret is compromised, you can generate a new api key and secret on your controlpanel. 2. Construct the input value for generating the hmac.   Concatenate:apikey, request method, path and querystring information, unix timestamp, nonce and content.  |          | Description | ---         | --- | apikey        | The key that is linked to your user. | request method      | lowercased (eg: get, post, delete,...) | path and querystring information  | urlencoding of the lowercased relative path and querystring.<br />The path **MUST start with the api version (/v2)**.<br />The hexadecimal codes (percent encoding) MUST be uppercased. | unix timestamp      | the unix timestamp in **seconds**. | nonce         | a unique string for each request. It should be a random string, not related to the request. The nonce (in combination with the unix timestamp) protects you from replay attacks in case anyone was able to intercept a request. | content        | When the request body is not empty, this should be the Base64 encoded Md5 hash of the request body.<br />An empty body should not be encoded.  3. Hash the concatenated string using your api secret and the SHA-256 algorithm. 4. Base64 encode the result of the hash function. This is the hmac signature you will need to send an authorized request.  ## Sending an authorized request  An authorized request can be made by sending the generated HMAC in the authorization header.   A correct authorizationheader uses the hmac authorization scheme and a correctly formatted authorization parameter.  Create the authorization parameter by concatenating:   * apikey   * colon ':'   * generated HMAC signature (see above)   * colon ':'   * nonce (the one used to generate the signature)   * colon ':'   * unix timestamp (the one used to generate the signature)  A sample (illustrated):  * The first line is the string you create to feed to the hashing algorithm. * The second line is the authorization header that should be sent in the request.  ![hmac authorization header illustrated](/v2/images/authentication_illustration.jpg \"authorization header illustrated\")  ## IP whitelisting  Access is by default restricted for all IP addresses. You need to explicitly whitelist an IP or an IP range in your controlpanel.  # Versioning  Because of breaking contract changes compared to v1, we released v2 of the API.   V1 will still be available, but you are strongly encouraged to migrate to the latest version.   New features will only be available on v2.  # Policy  ### Fair use policy  Please respect the rate limits and do not use the api for any purposes of abuse.   All requests are being monitored and logged.   Intentional abuse might result in api key revocation.  # Errors  The API attempts to return appropriate HTTP status codes for every request.   When the status code indicates failure, the API will also provide an error message in most cases.  An error message contains a machine-parseable error code accompanied by a descriptive error text.   The text for an error message might change over time, but codes will stay the same.  [An overview of error codes can be found here](/v2/documentation/errorcodes).  # Change log  [An overview of new changes can be found here](/v2/documentation/changelog).  # Provisioning information  ## Terminology  | Term   | Definition                | | ---   | ---                  | | Servicepack | Defines a set of assets that belong together. An example is a hosting package which offers Linux hosting, a domain name, a couple of mailboxes and databases.<br/>It also limits the size of individual assets within the same account. | | Account  | Represents an instance of the servicepack. It contains one or more assets. The number and size of assets is defined by the servicepack. | | Asset   | A manageable service. For example: a mysql database, a linux hosting, a mailbox,...<br/>Some assets are created at the moment when the account is created. Other assets can be created afterwards.   ## Common provisioning scenario  **Provisioning of an account with Linux hosting with one MySql database**  *Without a pre-existing account:*  1. Create a new account.<br/>Perform a POST on the accounts route and provide the desired servicepack id and identifier (domain name). 2. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 3. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/> When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/> This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 4. The created resource will point to an account. You now know the account's Id and can continue with the provisioning of a MySql database on this account. 5. Perform a POST on the mysqldatabases route and provide the account id along with other requested information. 6. Read the Location header from the response and perform a GET of the provided resource (a provisioning job). 7. When the response returns 200(OK), you should repeat the GET operation after a certain interval (Repeat this step).<br/> When the response returns 201(Created), you should read the response body. This will contain links to the created resources.<br/> This will usually hold only one link, but to be futureproof, this has been designed to return a collection. 8. The created resource will point to a MySql database resource.  ## SSL certificate requests  **Requesting an SSL certificate causes the purchase of a paying product.**  1. A certificate is created by adding an ssl certificate request. 2. Upon statuscode 201 you should query for certificate completion on the resource provided in the location response header. 3. The resource request can respond with different statuscodes: <ul>     <li>200: the certificate request is ongoing.<br/> Check the validations collection for validation values that are not auto_validated. Those should be set by you system.<br/> Call verify domain validations once all validation values are in place. It might take some time for verification to take place. It is not necessary to call this method more than once.</li>     <li>303: the certificate request is complete; there is no more certificate request resource available. Check the location header value to retrieve the representation of the resulting ssl certificate.</li>     <li>410: the certificate request does not exist anymore, there is no certificate created as a result of the request.</li> </ul>
 *
 * The version of the OpenAPI document: v2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRegistrantInput.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRegistrantInput::OAIRegistrantInput(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRegistrantInput::OAIRegistrantInput() {
    this->initializeModel();
}

OAIRegistrantInput::~OAIRegistrantInput() {}

void OAIRegistrantInput::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_company_name_isSet = false;
    m_company_name_isValid = false;

    m_country_code_isSet = false;
    m_country_code_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_enterprise_number_isSet = false;
    m_enterprise_number_isValid = false;

    m_extra_fields_isSet = false;
    m_extra_fields_isValid = false;

    m_fax_isSet = false;
    m_fax_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_language_code_isSet = false;
    m_language_code_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_phone_isSet = false;
    m_phone_isValid = false;

    m_postal_code_isSet = false;
    m_postal_code_isValid = false;
}

void OAIRegistrantInput::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRegistrantInput::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_company_name_isValid = ::OpenAPI::fromJsonValue(m_company_name, json[QString("company_name")]);
    m_company_name_isSet = !json[QString("company_name")].isNull() && m_company_name_isValid;

    m_country_code_isValid = ::OpenAPI::fromJsonValue(m_country_code, json[QString("country_code")]);
    m_country_code_isSet = !json[QString("country_code")].isNull() && m_country_code_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_enterprise_number_isValid = ::OpenAPI::fromJsonValue(m_enterprise_number, json[QString("enterprise_number")]);
    m_enterprise_number_isSet = !json[QString("enterprise_number")].isNull() && m_enterprise_number_isValid;

    m_extra_fields_isValid = ::OpenAPI::fromJsonValue(m_extra_fields, json[QString("extra_fields")]);
    m_extra_fields_isSet = !json[QString("extra_fields")].isNull() && m_extra_fields_isValid;

    m_fax_isValid = ::OpenAPI::fromJsonValue(m_fax, json[QString("fax")]);
    m_fax_isSet = !json[QString("fax")].isNull() && m_fax_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_language_code_isValid = ::OpenAPI::fromJsonValue(m_language_code, json[QString("language_code")]);
    m_language_code_isSet = !json[QString("language_code")].isNull() && m_language_code_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_phone_isValid = ::OpenAPI::fromJsonValue(m_phone, json[QString("phone")]);
    m_phone_isSet = !json[QString("phone")].isNull() && m_phone_isValid;

    m_postal_code_isValid = ::OpenAPI::fromJsonValue(m_postal_code, json[QString("postal_code")]);
    m_postal_code_isSet = !json[QString("postal_code")].isNull() && m_postal_code_isValid;
}

QString OAIRegistrantInput::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRegistrantInput::asJsonObject() const {
    QJsonObject obj;
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_company_name_isSet) {
        obj.insert(QString("company_name"), ::OpenAPI::toJsonValue(m_company_name));
    }
    if (m_country_code_isSet) {
        obj.insert(QString("country_code"), ::OpenAPI::toJsonValue(m_country_code));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_enterprise_number_isSet) {
        obj.insert(QString("enterprise_number"), ::OpenAPI::toJsonValue(m_enterprise_number));
    }
    if (m_extra_fields.size() > 0) {
        obj.insert(QString("extra_fields"), ::OpenAPI::toJsonValue(m_extra_fields));
    }
    if (m_fax_isSet) {
        obj.insert(QString("fax"), ::OpenAPI::toJsonValue(m_fax));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_language_code_isSet) {
        obj.insert(QString("language_code"), ::OpenAPI::toJsonValue(m_language_code));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_phone_isSet) {
        obj.insert(QString("phone"), ::OpenAPI::toJsonValue(m_phone));
    }
    if (m_postal_code_isSet) {
        obj.insert(QString("postal_code"), ::OpenAPI::toJsonValue(m_postal_code));
    }
    return obj;
}

QString OAIRegistrantInput::getAddress() const {
    return m_address;
}
void OAIRegistrantInput::setAddress(const QString &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIRegistrantInput::is_address_Set() const{
    return m_address_isSet;
}

bool OAIRegistrantInput::is_address_Valid() const{
    return m_address_isValid;
}

QString OAIRegistrantInput::getCity() const {
    return m_city;
}
void OAIRegistrantInput::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIRegistrantInput::is_city_Set() const{
    return m_city_isSet;
}

bool OAIRegistrantInput::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIRegistrantInput::getCompanyName() const {
    return m_company_name;
}
void OAIRegistrantInput::setCompanyName(const QString &company_name) {
    m_company_name = company_name;
    m_company_name_isSet = true;
}

bool OAIRegistrantInput::is_company_name_Set() const{
    return m_company_name_isSet;
}

bool OAIRegistrantInput::is_company_name_Valid() const{
    return m_company_name_isValid;
}

QString OAIRegistrantInput::getCountryCode() const {
    return m_country_code;
}
void OAIRegistrantInput::setCountryCode(const QString &country_code) {
    m_country_code = country_code;
    m_country_code_isSet = true;
}

bool OAIRegistrantInput::is_country_code_Set() const{
    return m_country_code_isSet;
}

bool OAIRegistrantInput::is_country_code_Valid() const{
    return m_country_code_isValid;
}

QString OAIRegistrantInput::getEmail() const {
    return m_email;
}
void OAIRegistrantInput::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIRegistrantInput::is_email_Set() const{
    return m_email_isSet;
}

bool OAIRegistrantInput::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIRegistrantInput::getEnterpriseNumber() const {
    return m_enterprise_number;
}
void OAIRegistrantInput::setEnterpriseNumber(const QString &enterprise_number) {
    m_enterprise_number = enterprise_number;
    m_enterprise_number_isSet = true;
}

bool OAIRegistrantInput::is_enterprise_number_Set() const{
    return m_enterprise_number_isSet;
}

bool OAIRegistrantInput::is_enterprise_number_Valid() const{
    return m_enterprise_number_isValid;
}

QList<OAIExtraField> OAIRegistrantInput::getExtraFields() const {
    return m_extra_fields;
}
void OAIRegistrantInput::setExtraFields(const QList<OAIExtraField> &extra_fields) {
    m_extra_fields = extra_fields;
    m_extra_fields_isSet = true;
}

bool OAIRegistrantInput::is_extra_fields_Set() const{
    return m_extra_fields_isSet;
}

bool OAIRegistrantInput::is_extra_fields_Valid() const{
    return m_extra_fields_isValid;
}

QString OAIRegistrantInput::getFax() const {
    return m_fax;
}
void OAIRegistrantInput::setFax(const QString &fax) {
    m_fax = fax;
    m_fax_isSet = true;
}

bool OAIRegistrantInput::is_fax_Set() const{
    return m_fax_isSet;
}

bool OAIRegistrantInput::is_fax_Valid() const{
    return m_fax_isValid;
}

QString OAIRegistrantInput::getFirstName() const {
    return m_first_name;
}
void OAIRegistrantInput::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIRegistrantInput::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIRegistrantInput::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIRegistrantInput::getLanguageCode() const {
    return m_language_code;
}
void OAIRegistrantInput::setLanguageCode(const QString &language_code) {
    m_language_code = language_code;
    m_language_code_isSet = true;
}

bool OAIRegistrantInput::is_language_code_Set() const{
    return m_language_code_isSet;
}

bool OAIRegistrantInput::is_language_code_Valid() const{
    return m_language_code_isValid;
}

QString OAIRegistrantInput::getLastName() const {
    return m_last_name;
}
void OAIRegistrantInput::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIRegistrantInput::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIRegistrantInput::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIRegistrantInput::getPhone() const {
    return m_phone;
}
void OAIRegistrantInput::setPhone(const QString &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAIRegistrantInput::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAIRegistrantInput::is_phone_Valid() const{
    return m_phone_isValid;
}

QString OAIRegistrantInput::getPostalCode() const {
    return m_postal_code;
}
void OAIRegistrantInput::setPostalCode(const QString &postal_code) {
    m_postal_code = postal_code;
    m_postal_code_isSet = true;
}

bool OAIRegistrantInput::is_postal_code_Set() const{
    return m_postal_code_isSet;
}

bool OAIRegistrantInput::is_postal_code_Valid() const{
    return m_postal_code_isValid;
}

bool OAIRegistrantInput::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enterprise_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extra_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_fax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postal_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRegistrantInput::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
