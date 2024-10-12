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

/*
 * OAIRiskMetadata.h
 *
 * Risk metadata used for 3DS and risk scoring.
 */

#ifndef OAIRiskMetadata_H
#define OAIRiskMetadata_H

#include <QJsonObject>

#include "OAIBrowserData.h"
#include <QMap>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBrowserData;

class OAIRiskMetadata : public OAIObject {
public:
    OAIRiskMetadata();
    OAIRiskMetadata(QString json);
    ~OAIRiskMetadata() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getAccuracyRadius() const;
    void setAccuracyRadius(const qint32 &accuracy_radius);
    bool is_accuracy_radius_Set() const;
    bool is_accuracy_radius_Valid() const;

    OAIBrowserData getBrowserData() const;
    void setBrowserData(const OAIBrowserData &browser_data);
    bool is_browser_data_Set() const;
    bool is_browser_data_Valid() const;

    QString getCity() const;
    void setCity(const QString &city);
    bool is_city_Set() const;
    bool is_city_Valid() const;

    QString getCountry() const;
    void setCountry(const QString &country);
    bool is_country_Set() const;
    bool is_country_Valid() const;

    qint32 getDeviceVelocity() const;
    void setDeviceVelocity(const qint32 &device_velocity);
    bool is_device_velocity_Set() const;
    bool is_device_velocity_Valid() const;

    qint32 getDistance() const;
    void setDistance(const qint32 &distance);
    bool is_distance_Set() const;
    bool is_distance_Valid() const;

    QString getFingerprint() const;
    void setFingerprint(const QString &fingerprint);
    bool is_fingerprint_Set() const;
    bool is_fingerprint_Valid() const;

    bool isHasMismatchedBankCountry() const;
    void setHasMismatchedBankCountry(const bool &has_mismatched_bank_country);
    bool is_has_mismatched_bank_country_Set() const;
    bool is_has_mismatched_bank_country_Valid() const;

    bool isHasMismatchedBillingAddressCountry() const;
    void setHasMismatchedBillingAddressCountry(const bool &has_mismatched_billing_address_country);
    bool is_has_mismatched_billing_address_country_Set() const;
    bool is_has_mismatched_billing_address_country_Valid() const;

    bool isHasMismatchedHolderName() const;
    void setHasMismatchedHolderName(const bool &has_mismatched_holder_name);
    bool is_has_mismatched_holder_name_Set() const;
    bool is_has_mismatched_holder_name_Valid() const;

    bool isHasMismatchedTimeZone() const;
    void setHasMismatchedTimeZone(const bool &has_mismatched_time_zone);
    bool is_has_mismatched_time_zone_Set() const;
    bool is_has_mismatched_time_zone_Valid() const;

    QMap<QString, QString> getHttpHeaders() const;
    void setHttpHeaders(const QMap<QString, QString> &http_headers);
    bool is_http_headers_Set() const;
    bool is_http_headers_Valid() const;

    QString getIpAddress() const;
    void setIpAddress(const QString &ip_address);
    bool is_ip_address_Set() const;
    bool is_ip_address_Valid() const;

    bool isIsHosting() const;
    void setIsHosting(const bool &is_hosting);
    bool is_is_hosting_Set() const;
    bool is_is_hosting_Valid() const;

    bool isIsProxy() const;
    void setIsProxy(const bool &is_proxy);
    bool is_is_proxy_Set() const;
    bool is_is_proxy_Valid() const;

    bool isIsTor() const;
    void setIsTor(const bool &is_tor);
    bool is_is_tor_Set() const;
    bool is_is_tor_Valid() const;

    bool isIsVpn() const;
    void setIsVpn(const bool &is_vpn);
    bool is_is_vpn_Set() const;
    bool is_is_vpn_Valid() const;

    QString getIsp() const;
    void setIsp(const QString &isp);
    bool is_isp_Set() const;
    bool is_isp_Valid() const;

    double getLatitude() const;
    void setLatitude(const double &latitude);
    bool is_latitude_Set() const;
    bool is_latitude_Valid() const;

    double getLongitude() const;
    void setLongitude(const double &longitude);
    bool is_longitude_Set() const;
    bool is_longitude_Valid() const;

    qint32 getPaymentInstrumentVelocity() const;
    void setPaymentInstrumentVelocity(const qint32 &payment_instrument_velocity);
    bool is_payment_instrument_velocity_Set() const;
    bool is_payment_instrument_velocity_Valid() const;

    QString getPostalCode() const;
    void setPostalCode(const QString &postal_code);
    bool is_postal_code_Set() const;
    bool is_postal_code_Valid() const;

    QString getRegion() const;
    void setRegion(const QString &region);
    bool is_region_Set() const;
    bool is_region_Valid() const;

    qint32 getScore() const;
    void setScore(const qint32 &score);
    bool is_score_Set() const;
    bool is_score_Valid() const;

    QString getTimeZone() const;
    void setTimeZone(const QString &time_zone);
    bool is_time_zone_Set() const;
    bool is_time_zone_Valid() const;

    QString getVpnServiceName() const;
    void setVpnServiceName(const QString &vpn_service_name);
    bool is_vpn_service_name_Set() const;
    bool is_vpn_service_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_accuracy_radius;
    bool m_accuracy_radius_isSet;
    bool m_accuracy_radius_isValid;

    OAIBrowserData m_browser_data;
    bool m_browser_data_isSet;
    bool m_browser_data_isValid;

    QString m_city;
    bool m_city_isSet;
    bool m_city_isValid;

    QString m_country;
    bool m_country_isSet;
    bool m_country_isValid;

    qint32 m_device_velocity;
    bool m_device_velocity_isSet;
    bool m_device_velocity_isValid;

    qint32 m_distance;
    bool m_distance_isSet;
    bool m_distance_isValid;

    QString m_fingerprint;
    bool m_fingerprint_isSet;
    bool m_fingerprint_isValid;

    bool m_has_mismatched_bank_country;
    bool m_has_mismatched_bank_country_isSet;
    bool m_has_mismatched_bank_country_isValid;

    bool m_has_mismatched_billing_address_country;
    bool m_has_mismatched_billing_address_country_isSet;
    bool m_has_mismatched_billing_address_country_isValid;

    bool m_has_mismatched_holder_name;
    bool m_has_mismatched_holder_name_isSet;
    bool m_has_mismatched_holder_name_isValid;

    bool m_has_mismatched_time_zone;
    bool m_has_mismatched_time_zone_isSet;
    bool m_has_mismatched_time_zone_isValid;

    QMap<QString, QString> m_http_headers;
    bool m_http_headers_isSet;
    bool m_http_headers_isValid;

    QString m_ip_address;
    bool m_ip_address_isSet;
    bool m_ip_address_isValid;

    bool m_is_hosting;
    bool m_is_hosting_isSet;
    bool m_is_hosting_isValid;

    bool m_is_proxy;
    bool m_is_proxy_isSet;
    bool m_is_proxy_isValid;

    bool m_is_tor;
    bool m_is_tor_isSet;
    bool m_is_tor_isValid;

    bool m_is_vpn;
    bool m_is_vpn_isSet;
    bool m_is_vpn_isValid;

    QString m_isp;
    bool m_isp_isSet;
    bool m_isp_isValid;

    double m_latitude;
    bool m_latitude_isSet;
    bool m_latitude_isValid;

    double m_longitude;
    bool m_longitude_isSet;
    bool m_longitude_isValid;

    qint32 m_payment_instrument_velocity;
    bool m_payment_instrument_velocity_isSet;
    bool m_payment_instrument_velocity_isValid;

    QString m_postal_code;
    bool m_postal_code_isSet;
    bool m_postal_code_isValid;

    QString m_region;
    bool m_region_isSet;
    bool m_region_isValid;

    qint32 m_score;
    bool m_score_isSet;
    bool m_score_isValid;

    QString m_time_zone;
    bool m_time_zone_isSet;
    bool m_time_zone_isValid;

    QString m_vpn_service_name;
    bool m_vpn_service_name_isSet;
    bool m_vpn_service_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIRiskMetadata)

#endif // OAIRiskMetadata_H
