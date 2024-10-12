/**
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEMS_allOf_credentials.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEMS_allOf_credentials::OAIEMS_allOf_credentials(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEMS_allOf_credentials::OAIEMS_allOf_credentials() {
    this->initializeModel();
}

OAIEMS_allOf_credentials::~OAIEMS_allOf_credentials() {}

void OAIEMS_allOf_credentials::initializeModel() {

    m_client_certificate_isSet = false;
    m_client_certificate_isValid = false;

    m_client_certificate_password_isSet = false;
    m_client_certificate_password_isValid = false;

    m_merchant_name_isSet = false;
    m_merchant_name_isValid = false;

    m_password_isSet = false;
    m_password_isValid = false;

    m_private_key_isSet = false;
    m_private_key_isValid = false;

    m_private_key_password_isSet = false;
    m_private_key_password_isValid = false;

    m_server_certificate_isSet = false;
    m_server_certificate_isValid = false;

    m_sftp_private_key_isSet = false;
    m_sftp_private_key_isValid = false;

    m_store_id_isSet = false;
    m_store_id_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIEMS_allOf_credentials::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEMS_allOf_credentials::fromJsonObject(QJsonObject json) {

    m_client_certificate_isValid = ::OpenAPI::fromJsonValue(m_client_certificate, json[QString("clientCertificate")]);
    m_client_certificate_isSet = !json[QString("clientCertificate")].isNull() && m_client_certificate_isValid;

    m_client_certificate_password_isValid = ::OpenAPI::fromJsonValue(m_client_certificate_password, json[QString("clientCertificatePassword")]);
    m_client_certificate_password_isSet = !json[QString("clientCertificatePassword")].isNull() && m_client_certificate_password_isValid;

    m_merchant_name_isValid = ::OpenAPI::fromJsonValue(m_merchant_name, json[QString("merchantName")]);
    m_merchant_name_isSet = !json[QString("merchantName")].isNull() && m_merchant_name_isValid;

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_private_key_isValid = ::OpenAPI::fromJsonValue(m_private_key, json[QString("privateKey")]);
    m_private_key_isSet = !json[QString("privateKey")].isNull() && m_private_key_isValid;

    m_private_key_password_isValid = ::OpenAPI::fromJsonValue(m_private_key_password, json[QString("privateKeyPassword")]);
    m_private_key_password_isSet = !json[QString("privateKeyPassword")].isNull() && m_private_key_password_isValid;

    m_server_certificate_isValid = ::OpenAPI::fromJsonValue(m_server_certificate, json[QString("serverCertificate")]);
    m_server_certificate_isSet = !json[QString("serverCertificate")].isNull() && m_server_certificate_isValid;

    m_sftp_private_key_isValid = ::OpenAPI::fromJsonValue(m_sftp_private_key, json[QString("sftpPrivateKey")]);
    m_sftp_private_key_isSet = !json[QString("sftpPrivateKey")].isNull() && m_sftp_private_key_isValid;

    m_store_id_isValid = ::OpenAPI::fromJsonValue(m_store_id, json[QString("storeId")]);
    m_store_id_isSet = !json[QString("storeId")].isNull() && m_store_id_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("userId")]);
    m_user_id_isSet = !json[QString("userId")].isNull() && m_user_id_isValid;
}

QString OAIEMS_allOf_credentials::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEMS_allOf_credentials::asJsonObject() const {
    QJsonObject obj;
    if (m_client_certificate_isSet) {
        obj.insert(QString("clientCertificate"), ::OpenAPI::toJsonValue(m_client_certificate));
    }
    if (m_client_certificate_password_isSet) {
        obj.insert(QString("clientCertificatePassword"), ::OpenAPI::toJsonValue(m_client_certificate_password));
    }
    if (m_merchant_name_isSet) {
        obj.insert(QString("merchantName"), ::OpenAPI::toJsonValue(m_merchant_name));
    }
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_private_key_isSet) {
        obj.insert(QString("privateKey"), ::OpenAPI::toJsonValue(m_private_key));
    }
    if (m_private_key_password_isSet) {
        obj.insert(QString("privateKeyPassword"), ::OpenAPI::toJsonValue(m_private_key_password));
    }
    if (m_server_certificate_isSet) {
        obj.insert(QString("serverCertificate"), ::OpenAPI::toJsonValue(m_server_certificate));
    }
    if (m_sftp_private_key_isSet) {
        obj.insert(QString("sftpPrivateKey"), ::OpenAPI::toJsonValue(m_sftp_private_key));
    }
    if (m_store_id_isSet) {
        obj.insert(QString("storeId"), ::OpenAPI::toJsonValue(m_store_id));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("userId"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QString OAIEMS_allOf_credentials::getClientCertificate() const {
    return m_client_certificate;
}
void OAIEMS_allOf_credentials::setClientCertificate(const QString &client_certificate) {
    m_client_certificate = client_certificate;
    m_client_certificate_isSet = true;
}

bool OAIEMS_allOf_credentials::is_client_certificate_Set() const{
    return m_client_certificate_isSet;
}

bool OAIEMS_allOf_credentials::is_client_certificate_Valid() const{
    return m_client_certificate_isValid;
}

QString OAIEMS_allOf_credentials::getClientCertificatePassword() const {
    return m_client_certificate_password;
}
void OAIEMS_allOf_credentials::setClientCertificatePassword(const QString &client_certificate_password) {
    m_client_certificate_password = client_certificate_password;
    m_client_certificate_password_isSet = true;
}

bool OAIEMS_allOf_credentials::is_client_certificate_password_Set() const{
    return m_client_certificate_password_isSet;
}

bool OAIEMS_allOf_credentials::is_client_certificate_password_Valid() const{
    return m_client_certificate_password_isValid;
}

QString OAIEMS_allOf_credentials::getMerchantName() const {
    return m_merchant_name;
}
void OAIEMS_allOf_credentials::setMerchantName(const QString &merchant_name) {
    m_merchant_name = merchant_name;
    m_merchant_name_isSet = true;
}

bool OAIEMS_allOf_credentials::is_merchant_name_Set() const{
    return m_merchant_name_isSet;
}

bool OAIEMS_allOf_credentials::is_merchant_name_Valid() const{
    return m_merchant_name_isValid;
}

QString OAIEMS_allOf_credentials::getPassword() const {
    return m_password;
}
void OAIEMS_allOf_credentials::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIEMS_allOf_credentials::is_password_Set() const{
    return m_password_isSet;
}

bool OAIEMS_allOf_credentials::is_password_Valid() const{
    return m_password_isValid;
}

QString OAIEMS_allOf_credentials::getPrivateKey() const {
    return m_private_key;
}
void OAIEMS_allOf_credentials::setPrivateKey(const QString &private_key) {
    m_private_key = private_key;
    m_private_key_isSet = true;
}

bool OAIEMS_allOf_credentials::is_private_key_Set() const{
    return m_private_key_isSet;
}

bool OAIEMS_allOf_credentials::is_private_key_Valid() const{
    return m_private_key_isValid;
}

QString OAIEMS_allOf_credentials::getPrivateKeyPassword() const {
    return m_private_key_password;
}
void OAIEMS_allOf_credentials::setPrivateKeyPassword(const QString &private_key_password) {
    m_private_key_password = private_key_password;
    m_private_key_password_isSet = true;
}

bool OAIEMS_allOf_credentials::is_private_key_password_Set() const{
    return m_private_key_password_isSet;
}

bool OAIEMS_allOf_credentials::is_private_key_password_Valid() const{
    return m_private_key_password_isValid;
}

QString OAIEMS_allOf_credentials::getServerCertificate() const {
    return m_server_certificate;
}
void OAIEMS_allOf_credentials::setServerCertificate(const QString &server_certificate) {
    m_server_certificate = server_certificate;
    m_server_certificate_isSet = true;
}

bool OAIEMS_allOf_credentials::is_server_certificate_Set() const{
    return m_server_certificate_isSet;
}

bool OAIEMS_allOf_credentials::is_server_certificate_Valid() const{
    return m_server_certificate_isValid;
}

QString OAIEMS_allOf_credentials::getSftpPrivateKey() const {
    return m_sftp_private_key;
}
void OAIEMS_allOf_credentials::setSftpPrivateKey(const QString &sftp_private_key) {
    m_sftp_private_key = sftp_private_key;
    m_sftp_private_key_isSet = true;
}

bool OAIEMS_allOf_credentials::is_sftp_private_key_Set() const{
    return m_sftp_private_key_isSet;
}

bool OAIEMS_allOf_credentials::is_sftp_private_key_Valid() const{
    return m_sftp_private_key_isValid;
}

QString OAIEMS_allOf_credentials::getStoreId() const {
    return m_store_id;
}
void OAIEMS_allOf_credentials::setStoreId(const QString &store_id) {
    m_store_id = store_id;
    m_store_id_isSet = true;
}

bool OAIEMS_allOf_credentials::is_store_id_Set() const{
    return m_store_id_isSet;
}

bool OAIEMS_allOf_credentials::is_store_id_Valid() const{
    return m_store_id_isValid;
}

QString OAIEMS_allOf_credentials::getUserId() const {
    return m_user_id;
}
void OAIEMS_allOf_credentials::setUserId(const QString &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIEMS_allOf_credentials::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIEMS_allOf_credentials::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIEMS_allOf_credentials::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_certificate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_certificate_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merchant_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_private_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_private_key_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_server_certificate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sftp_private_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_store_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEMS_allOf_credentials::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_client_certificate_isValid && m_client_certificate_password_isValid && m_password_isValid && m_private_key_isValid && m_private_key_password_isValid && m_server_certificate_isValid && m_store_id_isValid && m_user_id_isValid && true;
}

} // namespace OpenAPI
