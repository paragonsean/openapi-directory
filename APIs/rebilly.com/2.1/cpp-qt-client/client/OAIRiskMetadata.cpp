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

#include "OAIRiskMetadata.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRiskMetadata::OAIRiskMetadata(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRiskMetadata::OAIRiskMetadata() {
    this->initializeModel();
}

OAIRiskMetadata::~OAIRiskMetadata() {}

void OAIRiskMetadata::initializeModel() {

    m_accuracy_radius_isSet = false;
    m_accuracy_radius_isValid = false;

    m_browser_data_isSet = false;
    m_browser_data_isValid = false;

    m_city_isSet = false;
    m_city_isValid = false;

    m_country_isSet = false;
    m_country_isValid = false;

    m_device_velocity_isSet = false;
    m_device_velocity_isValid = false;

    m_distance_isSet = false;
    m_distance_isValid = false;

    m_fingerprint_isSet = false;
    m_fingerprint_isValid = false;

    m_has_mismatched_bank_country_isSet = false;
    m_has_mismatched_bank_country_isValid = false;

    m_has_mismatched_billing_address_country_isSet = false;
    m_has_mismatched_billing_address_country_isValid = false;

    m_has_mismatched_holder_name_isSet = false;
    m_has_mismatched_holder_name_isValid = false;

    m_has_mismatched_time_zone_isSet = false;
    m_has_mismatched_time_zone_isValid = false;

    m_http_headers_isSet = false;
    m_http_headers_isValid = false;

    m_ip_address_isSet = false;
    m_ip_address_isValid = false;

    m_is_hosting_isSet = false;
    m_is_hosting_isValid = false;

    m_is_proxy_isSet = false;
    m_is_proxy_isValid = false;

    m_is_tor_isSet = false;
    m_is_tor_isValid = false;

    m_is_vpn_isSet = false;
    m_is_vpn_isValid = false;

    m_isp_isSet = false;
    m_isp_isValid = false;

    m_latitude_isSet = false;
    m_latitude_isValid = false;

    m_longitude_isSet = false;
    m_longitude_isValid = false;

    m_payment_instrument_velocity_isSet = false;
    m_payment_instrument_velocity_isValid = false;

    m_postal_code_isSet = false;
    m_postal_code_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_score_isSet = false;
    m_score_isValid = false;

    m_time_zone_isSet = false;
    m_time_zone_isValid = false;

    m_vpn_service_name_isSet = false;
    m_vpn_service_name_isValid = false;
}

void OAIRiskMetadata::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRiskMetadata::fromJsonObject(QJsonObject json) {

    m_accuracy_radius_isValid = ::OpenAPI::fromJsonValue(m_accuracy_radius, json[QString("accuracyRadius")]);
    m_accuracy_radius_isSet = !json[QString("accuracyRadius")].isNull() && m_accuracy_radius_isValid;

    m_browser_data_isValid = ::OpenAPI::fromJsonValue(m_browser_data, json[QString("browserData")]);
    m_browser_data_isSet = !json[QString("browserData")].isNull() && m_browser_data_isValid;

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_device_velocity_isValid = ::OpenAPI::fromJsonValue(m_device_velocity, json[QString("deviceVelocity")]);
    m_device_velocity_isSet = !json[QString("deviceVelocity")].isNull() && m_device_velocity_isValid;

    m_distance_isValid = ::OpenAPI::fromJsonValue(m_distance, json[QString("distance")]);
    m_distance_isSet = !json[QString("distance")].isNull() && m_distance_isValid;

    m_fingerprint_isValid = ::OpenAPI::fromJsonValue(m_fingerprint, json[QString("fingerprint")]);
    m_fingerprint_isSet = !json[QString("fingerprint")].isNull() && m_fingerprint_isValid;

    m_has_mismatched_bank_country_isValid = ::OpenAPI::fromJsonValue(m_has_mismatched_bank_country, json[QString("hasMismatchedBankCountry")]);
    m_has_mismatched_bank_country_isSet = !json[QString("hasMismatchedBankCountry")].isNull() && m_has_mismatched_bank_country_isValid;

    m_has_mismatched_billing_address_country_isValid = ::OpenAPI::fromJsonValue(m_has_mismatched_billing_address_country, json[QString("hasMismatchedBillingAddressCountry")]);
    m_has_mismatched_billing_address_country_isSet = !json[QString("hasMismatchedBillingAddressCountry")].isNull() && m_has_mismatched_billing_address_country_isValid;

    m_has_mismatched_holder_name_isValid = ::OpenAPI::fromJsonValue(m_has_mismatched_holder_name, json[QString("hasMismatchedHolderName")]);
    m_has_mismatched_holder_name_isSet = !json[QString("hasMismatchedHolderName")].isNull() && m_has_mismatched_holder_name_isValid;

    m_has_mismatched_time_zone_isValid = ::OpenAPI::fromJsonValue(m_has_mismatched_time_zone, json[QString("hasMismatchedTimeZone")]);
    m_has_mismatched_time_zone_isSet = !json[QString("hasMismatchedTimeZone")].isNull() && m_has_mismatched_time_zone_isValid;

    m_http_headers_isValid = ::OpenAPI::fromJsonValue(m_http_headers, json[QString("httpHeaders")]);
    m_http_headers_isSet = !json[QString("httpHeaders")].isNull() && m_http_headers_isValid;

    m_ip_address_isValid = ::OpenAPI::fromJsonValue(m_ip_address, json[QString("ipAddress")]);
    m_ip_address_isSet = !json[QString("ipAddress")].isNull() && m_ip_address_isValid;

    m_is_hosting_isValid = ::OpenAPI::fromJsonValue(m_is_hosting, json[QString("isHosting")]);
    m_is_hosting_isSet = !json[QString("isHosting")].isNull() && m_is_hosting_isValid;

    m_is_proxy_isValid = ::OpenAPI::fromJsonValue(m_is_proxy, json[QString("isProxy")]);
    m_is_proxy_isSet = !json[QString("isProxy")].isNull() && m_is_proxy_isValid;

    m_is_tor_isValid = ::OpenAPI::fromJsonValue(m_is_tor, json[QString("isTor")]);
    m_is_tor_isSet = !json[QString("isTor")].isNull() && m_is_tor_isValid;

    m_is_vpn_isValid = ::OpenAPI::fromJsonValue(m_is_vpn, json[QString("isVpn")]);
    m_is_vpn_isSet = !json[QString("isVpn")].isNull() && m_is_vpn_isValid;

    m_isp_isValid = ::OpenAPI::fromJsonValue(m_isp, json[QString("isp")]);
    m_isp_isSet = !json[QString("isp")].isNull() && m_isp_isValid;

    m_latitude_isValid = ::OpenAPI::fromJsonValue(m_latitude, json[QString("latitude")]);
    m_latitude_isSet = !json[QString("latitude")].isNull() && m_latitude_isValid;

    m_longitude_isValid = ::OpenAPI::fromJsonValue(m_longitude, json[QString("longitude")]);
    m_longitude_isSet = !json[QString("longitude")].isNull() && m_longitude_isValid;

    m_payment_instrument_velocity_isValid = ::OpenAPI::fromJsonValue(m_payment_instrument_velocity, json[QString("paymentInstrumentVelocity")]);
    m_payment_instrument_velocity_isSet = !json[QString("paymentInstrumentVelocity")].isNull() && m_payment_instrument_velocity_isValid;

    m_postal_code_isValid = ::OpenAPI::fromJsonValue(m_postal_code, json[QString("postalCode")]);
    m_postal_code_isSet = !json[QString("postalCode")].isNull() && m_postal_code_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_score_isValid = ::OpenAPI::fromJsonValue(m_score, json[QString("score")]);
    m_score_isSet = !json[QString("score")].isNull() && m_score_isValid;

    m_time_zone_isValid = ::OpenAPI::fromJsonValue(m_time_zone, json[QString("timeZone")]);
    m_time_zone_isSet = !json[QString("timeZone")].isNull() && m_time_zone_isValid;

    m_vpn_service_name_isValid = ::OpenAPI::fromJsonValue(m_vpn_service_name, json[QString("vpnServiceName")]);
    m_vpn_service_name_isSet = !json[QString("vpnServiceName")].isNull() && m_vpn_service_name_isValid;
}

QString OAIRiskMetadata::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRiskMetadata::asJsonObject() const {
    QJsonObject obj;
    if (m_accuracy_radius_isSet) {
        obj.insert(QString("accuracyRadius"), ::OpenAPI::toJsonValue(m_accuracy_radius));
    }
    if (m_browser_data.isSet()) {
        obj.insert(QString("browserData"), ::OpenAPI::toJsonValue(m_browser_data));
    }
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_device_velocity_isSet) {
        obj.insert(QString("deviceVelocity"), ::OpenAPI::toJsonValue(m_device_velocity));
    }
    if (m_distance_isSet) {
        obj.insert(QString("distance"), ::OpenAPI::toJsonValue(m_distance));
    }
    if (m_fingerprint_isSet) {
        obj.insert(QString("fingerprint"), ::OpenAPI::toJsonValue(m_fingerprint));
    }
    if (m_has_mismatched_bank_country_isSet) {
        obj.insert(QString("hasMismatchedBankCountry"), ::OpenAPI::toJsonValue(m_has_mismatched_bank_country));
    }
    if (m_has_mismatched_billing_address_country_isSet) {
        obj.insert(QString("hasMismatchedBillingAddressCountry"), ::OpenAPI::toJsonValue(m_has_mismatched_billing_address_country));
    }
    if (m_has_mismatched_holder_name_isSet) {
        obj.insert(QString("hasMismatchedHolderName"), ::OpenAPI::toJsonValue(m_has_mismatched_holder_name));
    }
    if (m_has_mismatched_time_zone_isSet) {
        obj.insert(QString("hasMismatchedTimeZone"), ::OpenAPI::toJsonValue(m_has_mismatched_time_zone));
    }
    if (m_http_headers.size() > 0) {
        obj.insert(QString("httpHeaders"), ::OpenAPI::toJsonValue(m_http_headers));
    }
    if (m_ip_address_isSet) {
        obj.insert(QString("ipAddress"), ::OpenAPI::toJsonValue(m_ip_address));
    }
    if (m_is_hosting_isSet) {
        obj.insert(QString("isHosting"), ::OpenAPI::toJsonValue(m_is_hosting));
    }
    if (m_is_proxy_isSet) {
        obj.insert(QString("isProxy"), ::OpenAPI::toJsonValue(m_is_proxy));
    }
    if (m_is_tor_isSet) {
        obj.insert(QString("isTor"), ::OpenAPI::toJsonValue(m_is_tor));
    }
    if (m_is_vpn_isSet) {
        obj.insert(QString("isVpn"), ::OpenAPI::toJsonValue(m_is_vpn));
    }
    if (m_isp_isSet) {
        obj.insert(QString("isp"), ::OpenAPI::toJsonValue(m_isp));
    }
    if (m_latitude_isSet) {
        obj.insert(QString("latitude"), ::OpenAPI::toJsonValue(m_latitude));
    }
    if (m_longitude_isSet) {
        obj.insert(QString("longitude"), ::OpenAPI::toJsonValue(m_longitude));
    }
    if (m_payment_instrument_velocity_isSet) {
        obj.insert(QString("paymentInstrumentVelocity"), ::OpenAPI::toJsonValue(m_payment_instrument_velocity));
    }
    if (m_postal_code_isSet) {
        obj.insert(QString("postalCode"), ::OpenAPI::toJsonValue(m_postal_code));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_score_isSet) {
        obj.insert(QString("score"), ::OpenAPI::toJsonValue(m_score));
    }
    if (m_time_zone_isSet) {
        obj.insert(QString("timeZone"), ::OpenAPI::toJsonValue(m_time_zone));
    }
    if (m_vpn_service_name_isSet) {
        obj.insert(QString("vpnServiceName"), ::OpenAPI::toJsonValue(m_vpn_service_name));
    }
    return obj;
}

qint32 OAIRiskMetadata::getAccuracyRadius() const {
    return m_accuracy_radius;
}
void OAIRiskMetadata::setAccuracyRadius(const qint32 &accuracy_radius) {
    m_accuracy_radius = accuracy_radius;
    m_accuracy_radius_isSet = true;
}

bool OAIRiskMetadata::is_accuracy_radius_Set() const{
    return m_accuracy_radius_isSet;
}

bool OAIRiskMetadata::is_accuracy_radius_Valid() const{
    return m_accuracy_radius_isValid;
}

OAIBrowserData OAIRiskMetadata::getBrowserData() const {
    return m_browser_data;
}
void OAIRiskMetadata::setBrowserData(const OAIBrowserData &browser_data) {
    m_browser_data = browser_data;
    m_browser_data_isSet = true;
}

bool OAIRiskMetadata::is_browser_data_Set() const{
    return m_browser_data_isSet;
}

bool OAIRiskMetadata::is_browser_data_Valid() const{
    return m_browser_data_isValid;
}

QString OAIRiskMetadata::getCity() const {
    return m_city;
}
void OAIRiskMetadata::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAIRiskMetadata::is_city_Set() const{
    return m_city_isSet;
}

bool OAIRiskMetadata::is_city_Valid() const{
    return m_city_isValid;
}

QString OAIRiskMetadata::getCountry() const {
    return m_country;
}
void OAIRiskMetadata::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAIRiskMetadata::is_country_Set() const{
    return m_country_isSet;
}

bool OAIRiskMetadata::is_country_Valid() const{
    return m_country_isValid;
}

qint32 OAIRiskMetadata::getDeviceVelocity() const {
    return m_device_velocity;
}
void OAIRiskMetadata::setDeviceVelocity(const qint32 &device_velocity) {
    m_device_velocity = device_velocity;
    m_device_velocity_isSet = true;
}

bool OAIRiskMetadata::is_device_velocity_Set() const{
    return m_device_velocity_isSet;
}

bool OAIRiskMetadata::is_device_velocity_Valid() const{
    return m_device_velocity_isValid;
}

qint32 OAIRiskMetadata::getDistance() const {
    return m_distance;
}
void OAIRiskMetadata::setDistance(const qint32 &distance) {
    m_distance = distance;
    m_distance_isSet = true;
}

bool OAIRiskMetadata::is_distance_Set() const{
    return m_distance_isSet;
}

bool OAIRiskMetadata::is_distance_Valid() const{
    return m_distance_isValid;
}

QString OAIRiskMetadata::getFingerprint() const {
    return m_fingerprint;
}
void OAIRiskMetadata::setFingerprint(const QString &fingerprint) {
    m_fingerprint = fingerprint;
    m_fingerprint_isSet = true;
}

bool OAIRiskMetadata::is_fingerprint_Set() const{
    return m_fingerprint_isSet;
}

bool OAIRiskMetadata::is_fingerprint_Valid() const{
    return m_fingerprint_isValid;
}

bool OAIRiskMetadata::isHasMismatchedBankCountry() const {
    return m_has_mismatched_bank_country;
}
void OAIRiskMetadata::setHasMismatchedBankCountry(const bool &has_mismatched_bank_country) {
    m_has_mismatched_bank_country = has_mismatched_bank_country;
    m_has_mismatched_bank_country_isSet = true;
}

bool OAIRiskMetadata::is_has_mismatched_bank_country_Set() const{
    return m_has_mismatched_bank_country_isSet;
}

bool OAIRiskMetadata::is_has_mismatched_bank_country_Valid() const{
    return m_has_mismatched_bank_country_isValid;
}

bool OAIRiskMetadata::isHasMismatchedBillingAddressCountry() const {
    return m_has_mismatched_billing_address_country;
}
void OAIRiskMetadata::setHasMismatchedBillingAddressCountry(const bool &has_mismatched_billing_address_country) {
    m_has_mismatched_billing_address_country = has_mismatched_billing_address_country;
    m_has_mismatched_billing_address_country_isSet = true;
}

bool OAIRiskMetadata::is_has_mismatched_billing_address_country_Set() const{
    return m_has_mismatched_billing_address_country_isSet;
}

bool OAIRiskMetadata::is_has_mismatched_billing_address_country_Valid() const{
    return m_has_mismatched_billing_address_country_isValid;
}

bool OAIRiskMetadata::isHasMismatchedHolderName() const {
    return m_has_mismatched_holder_name;
}
void OAIRiskMetadata::setHasMismatchedHolderName(const bool &has_mismatched_holder_name) {
    m_has_mismatched_holder_name = has_mismatched_holder_name;
    m_has_mismatched_holder_name_isSet = true;
}

bool OAIRiskMetadata::is_has_mismatched_holder_name_Set() const{
    return m_has_mismatched_holder_name_isSet;
}

bool OAIRiskMetadata::is_has_mismatched_holder_name_Valid() const{
    return m_has_mismatched_holder_name_isValid;
}

bool OAIRiskMetadata::isHasMismatchedTimeZone() const {
    return m_has_mismatched_time_zone;
}
void OAIRiskMetadata::setHasMismatchedTimeZone(const bool &has_mismatched_time_zone) {
    m_has_mismatched_time_zone = has_mismatched_time_zone;
    m_has_mismatched_time_zone_isSet = true;
}

bool OAIRiskMetadata::is_has_mismatched_time_zone_Set() const{
    return m_has_mismatched_time_zone_isSet;
}

bool OAIRiskMetadata::is_has_mismatched_time_zone_Valid() const{
    return m_has_mismatched_time_zone_isValid;
}

QMap<QString, QString> OAIRiskMetadata::getHttpHeaders() const {
    return m_http_headers;
}
void OAIRiskMetadata::setHttpHeaders(const QMap<QString, QString> &http_headers) {
    m_http_headers = http_headers;
    m_http_headers_isSet = true;
}

bool OAIRiskMetadata::is_http_headers_Set() const{
    return m_http_headers_isSet;
}

bool OAIRiskMetadata::is_http_headers_Valid() const{
    return m_http_headers_isValid;
}

QString OAIRiskMetadata::getIpAddress() const {
    return m_ip_address;
}
void OAIRiskMetadata::setIpAddress(const QString &ip_address) {
    m_ip_address = ip_address;
    m_ip_address_isSet = true;
}

bool OAIRiskMetadata::is_ip_address_Set() const{
    return m_ip_address_isSet;
}

bool OAIRiskMetadata::is_ip_address_Valid() const{
    return m_ip_address_isValid;
}

bool OAIRiskMetadata::isIsHosting() const {
    return m_is_hosting;
}
void OAIRiskMetadata::setIsHosting(const bool &is_hosting) {
    m_is_hosting = is_hosting;
    m_is_hosting_isSet = true;
}

bool OAIRiskMetadata::is_is_hosting_Set() const{
    return m_is_hosting_isSet;
}

bool OAIRiskMetadata::is_is_hosting_Valid() const{
    return m_is_hosting_isValid;
}

bool OAIRiskMetadata::isIsProxy() const {
    return m_is_proxy;
}
void OAIRiskMetadata::setIsProxy(const bool &is_proxy) {
    m_is_proxy = is_proxy;
    m_is_proxy_isSet = true;
}

bool OAIRiskMetadata::is_is_proxy_Set() const{
    return m_is_proxy_isSet;
}

bool OAIRiskMetadata::is_is_proxy_Valid() const{
    return m_is_proxy_isValid;
}

bool OAIRiskMetadata::isIsTor() const {
    return m_is_tor;
}
void OAIRiskMetadata::setIsTor(const bool &is_tor) {
    m_is_tor = is_tor;
    m_is_tor_isSet = true;
}

bool OAIRiskMetadata::is_is_tor_Set() const{
    return m_is_tor_isSet;
}

bool OAIRiskMetadata::is_is_tor_Valid() const{
    return m_is_tor_isValid;
}

bool OAIRiskMetadata::isIsVpn() const {
    return m_is_vpn;
}
void OAIRiskMetadata::setIsVpn(const bool &is_vpn) {
    m_is_vpn = is_vpn;
    m_is_vpn_isSet = true;
}

bool OAIRiskMetadata::is_is_vpn_Set() const{
    return m_is_vpn_isSet;
}

bool OAIRiskMetadata::is_is_vpn_Valid() const{
    return m_is_vpn_isValid;
}

QString OAIRiskMetadata::getIsp() const {
    return m_isp;
}
void OAIRiskMetadata::setIsp(const QString &isp) {
    m_isp = isp;
    m_isp_isSet = true;
}

bool OAIRiskMetadata::is_isp_Set() const{
    return m_isp_isSet;
}

bool OAIRiskMetadata::is_isp_Valid() const{
    return m_isp_isValid;
}

double OAIRiskMetadata::getLatitude() const {
    return m_latitude;
}
void OAIRiskMetadata::setLatitude(const double &latitude) {
    m_latitude = latitude;
    m_latitude_isSet = true;
}

bool OAIRiskMetadata::is_latitude_Set() const{
    return m_latitude_isSet;
}

bool OAIRiskMetadata::is_latitude_Valid() const{
    return m_latitude_isValid;
}

double OAIRiskMetadata::getLongitude() const {
    return m_longitude;
}
void OAIRiskMetadata::setLongitude(const double &longitude) {
    m_longitude = longitude;
    m_longitude_isSet = true;
}

bool OAIRiskMetadata::is_longitude_Set() const{
    return m_longitude_isSet;
}

bool OAIRiskMetadata::is_longitude_Valid() const{
    return m_longitude_isValid;
}

qint32 OAIRiskMetadata::getPaymentInstrumentVelocity() const {
    return m_payment_instrument_velocity;
}
void OAIRiskMetadata::setPaymentInstrumentVelocity(const qint32 &payment_instrument_velocity) {
    m_payment_instrument_velocity = payment_instrument_velocity;
    m_payment_instrument_velocity_isSet = true;
}

bool OAIRiskMetadata::is_payment_instrument_velocity_Set() const{
    return m_payment_instrument_velocity_isSet;
}

bool OAIRiskMetadata::is_payment_instrument_velocity_Valid() const{
    return m_payment_instrument_velocity_isValid;
}

QString OAIRiskMetadata::getPostalCode() const {
    return m_postal_code;
}
void OAIRiskMetadata::setPostalCode(const QString &postal_code) {
    m_postal_code = postal_code;
    m_postal_code_isSet = true;
}

bool OAIRiskMetadata::is_postal_code_Set() const{
    return m_postal_code_isSet;
}

bool OAIRiskMetadata::is_postal_code_Valid() const{
    return m_postal_code_isValid;
}

QString OAIRiskMetadata::getRegion() const {
    return m_region;
}
void OAIRiskMetadata::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAIRiskMetadata::is_region_Set() const{
    return m_region_isSet;
}

bool OAIRiskMetadata::is_region_Valid() const{
    return m_region_isValid;
}

qint32 OAIRiskMetadata::getScore() const {
    return m_score;
}
void OAIRiskMetadata::setScore(const qint32 &score) {
    m_score = score;
    m_score_isSet = true;
}

bool OAIRiskMetadata::is_score_Set() const{
    return m_score_isSet;
}

bool OAIRiskMetadata::is_score_Valid() const{
    return m_score_isValid;
}

QString OAIRiskMetadata::getTimeZone() const {
    return m_time_zone;
}
void OAIRiskMetadata::setTimeZone(const QString &time_zone) {
    m_time_zone = time_zone;
    m_time_zone_isSet = true;
}

bool OAIRiskMetadata::is_time_zone_Set() const{
    return m_time_zone_isSet;
}

bool OAIRiskMetadata::is_time_zone_Valid() const{
    return m_time_zone_isValid;
}

QString OAIRiskMetadata::getVpnServiceName() const {
    return m_vpn_service_name;
}
void OAIRiskMetadata::setVpnServiceName(const QString &vpn_service_name) {
    m_vpn_service_name = vpn_service_name;
    m_vpn_service_name_isSet = true;
}

bool OAIRiskMetadata::is_vpn_service_name_Set() const{
    return m_vpn_service_name_isSet;
}

bool OAIRiskMetadata::is_vpn_service_name_Valid() const{
    return m_vpn_service_name_isValid;
}

bool OAIRiskMetadata::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_accuracy_radius_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_browser_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_device_velocity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_distance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fingerprint_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_mismatched_bank_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_mismatched_billing_address_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_mismatched_holder_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_mismatched_time_zone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_http_headers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_ip_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_hosting_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_proxy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_tor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_vpn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_isp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_latitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_longitude_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_instrument_velocity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postal_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_zone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vpn_service_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRiskMetadata::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
