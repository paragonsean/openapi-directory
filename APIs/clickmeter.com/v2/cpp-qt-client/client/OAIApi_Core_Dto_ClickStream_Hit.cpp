/**
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApi_Core_Dto_ClickStream_Hit.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApi_Core_Dto_ClickStream_Hit::OAIApi_Core_Dto_ClickStream_Hit(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApi_Core_Dto_ClickStream_Hit::OAIApi_Core_Dto_ClickStream_Hit() {
    this->initializeModel();
}

OAIApi_Core_Dto_ClickStream_Hit::~OAIApi_Core_Dto_ClickStream_Hit() {}

void OAIApi_Core_Dto_ClickStream_Hit::initializeModel() {

    m_access_time_isSet = false;
    m_access_time_isValid = false;

    m_browser_isSet = false;
    m_browser_isValid = false;

    m_client_language_isSet = false;
    m_client_language_isValid = false;

    m_conversion1_isSet = false;
    m_conversion1_isValid = false;

    m_conversion2_isSet = false;
    m_conversion2_isValid = false;

    m_conversion3_isSet = false;
    m_conversion3_isValid = false;

    m_conversion4_isSet = false;
    m_conversion4_isValid = false;

    m_conversion5_isSet = false;
    m_conversion5_isValid = false;

    m_conversions_isSet = false;
    m_conversions_isValid = false;

    m_entity_isSet = false;
    m_entity_isValid = false;

    m_ip_isSet = false;
    m_ip_isValid = false;

    m_is_proxy_isSet = false;
    m_is_proxy_isValid = false;

    m_is_spider_isSet = false;
    m_is_spider_isValid = false;

    m_is_unique_isSet = false;
    m_is_unique_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_org_isSet = false;
    m_org_isValid = false;

    m_os_isSet = false;
    m_os_isValid = false;

    m_query_params_isSet = false;
    m_query_params_isValid = false;

    m_real_destination_url_isSet = false;
    m_real_destination_url_isValid = false;

    m_referer_isSet = false;
    m_referer_isValid = false;

    m_source_isSet = false;
    m_source_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIApi_Core_Dto_ClickStream_Hit::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApi_Core_Dto_ClickStream_Hit::fromJsonObject(QJsonObject json) {

    m_access_time_isValid = ::OpenAPI::fromJsonValue(m_access_time, json[QString("accessTime")]);
    m_access_time_isSet = !json[QString("accessTime")].isNull() && m_access_time_isValid;

    m_browser_isValid = ::OpenAPI::fromJsonValue(m_browser, json[QString("browser")]);
    m_browser_isSet = !json[QString("browser")].isNull() && m_browser_isValid;

    m_client_language_isValid = ::OpenAPI::fromJsonValue(m_client_language, json[QString("clientLanguage")]);
    m_client_language_isSet = !json[QString("clientLanguage")].isNull() && m_client_language_isValid;

    m_conversion1_isValid = ::OpenAPI::fromJsonValue(m_conversion1, json[QString("conversion1")]);
    m_conversion1_isSet = !json[QString("conversion1")].isNull() && m_conversion1_isValid;

    m_conversion2_isValid = ::OpenAPI::fromJsonValue(m_conversion2, json[QString("conversion2")]);
    m_conversion2_isSet = !json[QString("conversion2")].isNull() && m_conversion2_isValid;

    m_conversion3_isValid = ::OpenAPI::fromJsonValue(m_conversion3, json[QString("conversion3")]);
    m_conversion3_isSet = !json[QString("conversion3")].isNull() && m_conversion3_isValid;

    m_conversion4_isValid = ::OpenAPI::fromJsonValue(m_conversion4, json[QString("conversion4")]);
    m_conversion4_isSet = !json[QString("conversion4")].isNull() && m_conversion4_isValid;

    m_conversion5_isValid = ::OpenAPI::fromJsonValue(m_conversion5, json[QString("conversion5")]);
    m_conversion5_isSet = !json[QString("conversion5")].isNull() && m_conversion5_isValid;

    m_conversions_isValid = ::OpenAPI::fromJsonValue(m_conversions, json[QString("conversions")]);
    m_conversions_isSet = !json[QString("conversions")].isNull() && m_conversions_isValid;

    m_entity_isValid = ::OpenAPI::fromJsonValue(m_entity, json[QString("entity")]);
    m_entity_isSet = !json[QString("entity")].isNull() && m_entity_isValid;

    m_ip_isValid = ::OpenAPI::fromJsonValue(m_ip, json[QString("ip")]);
    m_ip_isSet = !json[QString("ip")].isNull() && m_ip_isValid;

    m_is_proxy_isValid = ::OpenAPI::fromJsonValue(m_is_proxy, json[QString("isProxy")]);
    m_is_proxy_isSet = !json[QString("isProxy")].isNull() && m_is_proxy_isValid;

    m_is_spider_isValid = ::OpenAPI::fromJsonValue(m_is_spider, json[QString("isSpider")]);
    m_is_spider_isSet = !json[QString("isSpider")].isNull() && m_is_spider_isValid;

    m_is_unique_isValid = ::OpenAPI::fromJsonValue(m_is_unique, json[QString("isUnique")]);
    m_is_unique_isSet = !json[QString("isUnique")].isNull() && m_is_unique_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_org_isValid = ::OpenAPI::fromJsonValue(m_org, json[QString("org")]);
    m_org_isSet = !json[QString("org")].isNull() && m_org_isValid;

    m_os_isValid = ::OpenAPI::fromJsonValue(m_os, json[QString("os")]);
    m_os_isSet = !json[QString("os")].isNull() && m_os_isValid;

    m_query_params_isValid = ::OpenAPI::fromJsonValue(m_query_params, json[QString("queryParams")]);
    m_query_params_isSet = !json[QString("queryParams")].isNull() && m_query_params_isValid;

    m_real_destination_url_isValid = ::OpenAPI::fromJsonValue(m_real_destination_url, json[QString("realDestinationUrl")]);
    m_real_destination_url_isSet = !json[QString("realDestinationUrl")].isNull() && m_real_destination_url_isValid;

    m_referer_isValid = ::OpenAPI::fromJsonValue(m_referer, json[QString("referer")]);
    m_referer_isSet = !json[QString("referer")].isNull() && m_referer_isValid;

    m_source_isValid = ::OpenAPI::fromJsonValue(m_source, json[QString("source")]);
    m_source_isSet = !json[QString("source")].isNull() && m_source_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIApi_Core_Dto_ClickStream_Hit::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApi_Core_Dto_ClickStream_Hit::asJsonObject() const {
    QJsonObject obj;
    if (m_access_time_isSet) {
        obj.insert(QString("accessTime"), ::OpenAPI::toJsonValue(m_access_time));
    }
    if (m_browser.isSet()) {
        obj.insert(QString("browser"), ::OpenAPI::toJsonValue(m_browser));
    }
    if (m_client_language_isSet) {
        obj.insert(QString("clientLanguage"), ::OpenAPI::toJsonValue(m_client_language));
    }
    if (m_conversion1.isSet()) {
        obj.insert(QString("conversion1"), ::OpenAPI::toJsonValue(m_conversion1));
    }
    if (m_conversion2.isSet()) {
        obj.insert(QString("conversion2"), ::OpenAPI::toJsonValue(m_conversion2));
    }
    if (m_conversion3.isSet()) {
        obj.insert(QString("conversion3"), ::OpenAPI::toJsonValue(m_conversion3));
    }
    if (m_conversion4.isSet()) {
        obj.insert(QString("conversion4"), ::OpenAPI::toJsonValue(m_conversion4));
    }
    if (m_conversion5.isSet()) {
        obj.insert(QString("conversion5"), ::OpenAPI::toJsonValue(m_conversion5));
    }
    if (m_conversions.size() > 0) {
        obj.insert(QString("conversions"), ::OpenAPI::toJsonValue(m_conversions));
    }
    if (m_entity.isSet()) {
        obj.insert(QString("entity"), ::OpenAPI::toJsonValue(m_entity));
    }
    if (m_ip_isSet) {
        obj.insert(QString("ip"), ::OpenAPI::toJsonValue(m_ip));
    }
    if (m_is_proxy_isSet) {
        obj.insert(QString("isProxy"), ::OpenAPI::toJsonValue(m_is_proxy));
    }
    if (m_is_spider_isSet) {
        obj.insert(QString("isSpider"), ::OpenAPI::toJsonValue(m_is_spider));
    }
    if (m_is_unique_isSet) {
        obj.insert(QString("isUnique"), ::OpenAPI::toJsonValue(m_is_unique));
    }
    if (m_location.isSet()) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_org_isSet) {
        obj.insert(QString("org"), ::OpenAPI::toJsonValue(m_org));
    }
    if (m_os.isSet()) {
        obj.insert(QString("os"), ::OpenAPI::toJsonValue(m_os));
    }
    if (m_query_params_isSet) {
        obj.insert(QString("queryParams"), ::OpenAPI::toJsonValue(m_query_params));
    }
    if (m_real_destination_url_isSet) {
        obj.insert(QString("realDestinationUrl"), ::OpenAPI::toJsonValue(m_real_destination_url));
    }
    if (m_referer_isSet) {
        obj.insert(QString("referer"), ::OpenAPI::toJsonValue(m_referer));
    }
    if (m_source.isSet()) {
        obj.insert(QString("source"), ::OpenAPI::toJsonValue(m_source));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIApi_Core_Dto_ClickStream_Hit::getAccessTime() const {
    return m_access_time;
}
void OAIApi_Core_Dto_ClickStream_Hit::setAccessTime(const QString &access_time) {
    m_access_time = access_time;
    m_access_time_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_access_time_Set() const{
    return m_access_time_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_access_time_Valid() const{
    return m_access_time_isValid;
}

OAIApi_Core_Dto_ClickStream_HitBrowserInfo OAIApi_Core_Dto_ClickStream_Hit::getBrowser() const {
    return m_browser;
}
void OAIApi_Core_Dto_ClickStream_Hit::setBrowser(const OAIApi_Core_Dto_ClickStream_HitBrowserInfo &browser) {
    m_browser = browser;
    m_browser_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_browser_Set() const{
    return m_browser_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_browser_Valid() const{
    return m_browser_isValid;
}

QString OAIApi_Core_Dto_ClickStream_Hit::getClientLanguage() const {
    return m_client_language;
}
void OAIApi_Core_Dto_ClickStream_Hit::setClientLanguage(const QString &client_language) {
    m_client_language = client_language;
    m_client_language_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_client_language_Set() const{
    return m_client_language_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_client_language_Valid() const{
    return m_client_language_isValid;
}

OAIApi_Core_Dto_ClickStream_HitConversionInfo OAIApi_Core_Dto_ClickStream_Hit::getConversion1() const {
    return m_conversion1;
}
void OAIApi_Core_Dto_ClickStream_Hit::setConversion1(const OAIApi_Core_Dto_ClickStream_HitConversionInfo &conversion1) {
    m_conversion1 = conversion1;
    m_conversion1_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversion1_Set() const{
    return m_conversion1_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversion1_Valid() const{
    return m_conversion1_isValid;
}

OAIApi_Core_Dto_ClickStream_HitConversionInfo OAIApi_Core_Dto_ClickStream_Hit::getConversion2() const {
    return m_conversion2;
}
void OAIApi_Core_Dto_ClickStream_Hit::setConversion2(const OAIApi_Core_Dto_ClickStream_HitConversionInfo &conversion2) {
    m_conversion2 = conversion2;
    m_conversion2_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversion2_Set() const{
    return m_conversion2_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversion2_Valid() const{
    return m_conversion2_isValid;
}

OAIApi_Core_Dto_ClickStream_HitConversionInfo OAIApi_Core_Dto_ClickStream_Hit::getConversion3() const {
    return m_conversion3;
}
void OAIApi_Core_Dto_ClickStream_Hit::setConversion3(const OAIApi_Core_Dto_ClickStream_HitConversionInfo &conversion3) {
    m_conversion3 = conversion3;
    m_conversion3_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversion3_Set() const{
    return m_conversion3_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversion3_Valid() const{
    return m_conversion3_isValid;
}

OAIApi_Core_Dto_ClickStream_HitConversionInfo OAIApi_Core_Dto_ClickStream_Hit::getConversion4() const {
    return m_conversion4;
}
void OAIApi_Core_Dto_ClickStream_Hit::setConversion4(const OAIApi_Core_Dto_ClickStream_HitConversionInfo &conversion4) {
    m_conversion4 = conversion4;
    m_conversion4_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversion4_Set() const{
    return m_conversion4_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversion4_Valid() const{
    return m_conversion4_isValid;
}

OAIApi_Core_Dto_ClickStream_HitConversionInfo OAIApi_Core_Dto_ClickStream_Hit::getConversion5() const {
    return m_conversion5;
}
void OAIApi_Core_Dto_ClickStream_Hit::setConversion5(const OAIApi_Core_Dto_ClickStream_HitConversionInfo &conversion5) {
    m_conversion5 = conversion5;
    m_conversion5_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversion5_Set() const{
    return m_conversion5_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversion5_Valid() const{
    return m_conversion5_isValid;
}

QList<OAIApi_Core_Dto_ClickStream_HitConversionInfo> OAIApi_Core_Dto_ClickStream_Hit::getConversions() const {
    return m_conversions;
}
void OAIApi_Core_Dto_ClickStream_Hit::setConversions(const QList<OAIApi_Core_Dto_ClickStream_HitConversionInfo> &conversions) {
    m_conversions = conversions;
    m_conversions_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversions_Set() const{
    return m_conversions_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_conversions_Valid() const{
    return m_conversions_isValid;
}

OAIApi_Core_Dto_ClickStream_HitDatapointInfo OAIApi_Core_Dto_ClickStream_Hit::getEntity() const {
    return m_entity;
}
void OAIApi_Core_Dto_ClickStream_Hit::setEntity(const OAIApi_Core_Dto_ClickStream_HitDatapointInfo &entity) {
    m_entity = entity;
    m_entity_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_entity_Set() const{
    return m_entity_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_entity_Valid() const{
    return m_entity_isValid;
}

QString OAIApi_Core_Dto_ClickStream_Hit::getIp() const {
    return m_ip;
}
void OAIApi_Core_Dto_ClickStream_Hit::setIp(const QString &ip) {
    m_ip = ip;
    m_ip_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_ip_Set() const{
    return m_ip_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_ip_Valid() const{
    return m_ip_isValid;
}

QString OAIApi_Core_Dto_ClickStream_Hit::getIsProxy() const {
    return m_is_proxy;
}
void OAIApi_Core_Dto_ClickStream_Hit::setIsProxy(const QString &is_proxy) {
    m_is_proxy = is_proxy;
    m_is_proxy_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_is_proxy_Set() const{
    return m_is_proxy_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_is_proxy_Valid() const{
    return m_is_proxy_isValid;
}

QString OAIApi_Core_Dto_ClickStream_Hit::getIsSpider() const {
    return m_is_spider;
}
void OAIApi_Core_Dto_ClickStream_Hit::setIsSpider(const QString &is_spider) {
    m_is_spider = is_spider;
    m_is_spider_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_is_spider_Set() const{
    return m_is_spider_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_is_spider_Valid() const{
    return m_is_spider_isValid;
}

QString OAIApi_Core_Dto_ClickStream_Hit::getIsUnique() const {
    return m_is_unique;
}
void OAIApi_Core_Dto_ClickStream_Hit::setIsUnique(const QString &is_unique) {
    m_is_unique = is_unique;
    m_is_unique_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_is_unique_Set() const{
    return m_is_unique_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_is_unique_Valid() const{
    return m_is_unique_isValid;
}

OAIApi_Core_Dto_ClickStream_HitLocationInfo OAIApi_Core_Dto_ClickStream_Hit::getLocation() const {
    return m_location;
}
void OAIApi_Core_Dto_ClickStream_Hit::setLocation(const OAIApi_Core_Dto_ClickStream_HitLocationInfo &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_location_Set() const{
    return m_location_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_location_Valid() const{
    return m_location_isValid;
}

QString OAIApi_Core_Dto_ClickStream_Hit::getOrg() const {
    return m_org;
}
void OAIApi_Core_Dto_ClickStream_Hit::setOrg(const QString &org) {
    m_org = org;
    m_org_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_org_Set() const{
    return m_org_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_org_Valid() const{
    return m_org_isValid;
}

OAIApi_Core_Dto_ClickStream_HitOsInfo OAIApi_Core_Dto_ClickStream_Hit::getOs() const {
    return m_os;
}
void OAIApi_Core_Dto_ClickStream_Hit::setOs(const OAIApi_Core_Dto_ClickStream_HitOsInfo &os) {
    m_os = os;
    m_os_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_os_Set() const{
    return m_os_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_os_Valid() const{
    return m_os_isValid;
}

QString OAIApi_Core_Dto_ClickStream_Hit::getQueryParams() const {
    return m_query_params;
}
void OAIApi_Core_Dto_ClickStream_Hit::setQueryParams(const QString &query_params) {
    m_query_params = query_params;
    m_query_params_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_query_params_Set() const{
    return m_query_params_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_query_params_Valid() const{
    return m_query_params_isValid;
}

QString OAIApi_Core_Dto_ClickStream_Hit::getRealDestinationUrl() const {
    return m_real_destination_url;
}
void OAIApi_Core_Dto_ClickStream_Hit::setRealDestinationUrl(const QString &real_destination_url) {
    m_real_destination_url = real_destination_url;
    m_real_destination_url_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_real_destination_url_Set() const{
    return m_real_destination_url_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_real_destination_url_Valid() const{
    return m_real_destination_url_isValid;
}

QString OAIApi_Core_Dto_ClickStream_Hit::getReferer() const {
    return m_referer;
}
void OAIApi_Core_Dto_ClickStream_Hit::setReferer(const QString &referer) {
    m_referer = referer;
    m_referer_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_referer_Set() const{
    return m_referer_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_referer_Valid() const{
    return m_referer_isValid;
}

OAIApi_Core_Dto_ClickStream_HitSource OAIApi_Core_Dto_ClickStream_Hit::getSource() const {
    return m_source;
}
void OAIApi_Core_Dto_ClickStream_Hit::setSource(const OAIApi_Core_Dto_ClickStream_HitSource &source) {
    m_source = source;
    m_source_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_source_Set() const{
    return m_source_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_source_Valid() const{
    return m_source_isValid;
}

QString OAIApi_Core_Dto_ClickStream_Hit::getType() const {
    return m_type;
}
void OAIApi_Core_Dto_ClickStream_Hit::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_type_Set() const{
    return m_type_isSet;
}

bool OAIApi_Core_Dto_ClickStream_Hit::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIApi_Core_Dto_ClickStream_Hit::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_access_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_browser.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_client_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_conversion1.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_conversion2.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_conversion3.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_conversion4.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_conversion5.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_conversions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_entity.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_ip_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_proxy_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_spider_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_unique_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_org_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_os.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_query_params_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_real_destination_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_referer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApi_Core_Dto_ClickStream_Hit::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
