/**
 * Google Home
 * # Google Home Local API This is an unofficial documentation of the local API used by the Home app to communicate with GH devices. [GitHub Repo](https://github.com/rithvikvibhu/GHLocalApi)  [![GitHub stars](https://img.shields.io/github/stars/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/stargazers) [![GitHub license](https://img.shields.io/github/license/rithvikvibhu/GHLocalApi)](https://github.com/rithvikvibhu/GHLocalApi/blob/master/LICENSE.md)  ## Getting Started  Requests must be made over HTTPS, port 8443, so the base URL for these endpoints is: `https://<google-home-ip>:8443/setup/`  Get the IP of Google Home from the Google Home app (Device Settings -> End of the list) or from your router.  GET requests are simple, in the browser kind.   POST requests need to set the header (when there's a body): `content-type: application/json`  ## Authentication  Since June 2019, most requests (with exceptions like `/setup/eureka_info`) need a local authorization token.  There are 3 kinds of tokens involved here:  ### Local Authorization Token This token must be sent in all requests in the header `cast-local-authorization-token`. It is short-lived (~1 day) and may change unexpectedly (with a sync, change in homegraph, etc.) ##### Get this token - With access to an android device, [get this token directly by either method](https://gist.github.com/rithvikvibhu/1a0f4937af957ef6a78453e3be482c1f). - Without a device, or to integrate it with a script, use an access token to get the homegraph and extract the token. To get an access token, read the next section. Check the example section for more info.  ### Access Token This is a standard google oauth2 access token. It is in the form `ya29.***`. This gives access to the Google Home Foyer API. These expire in an hour. Use this to get the homegraph (and then the local authorization token above). ##### Get this token To get this access token, either a Google account username/password or a Google Master Token is needed. More info in the gist. Use the script [from this gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d).  ### Master Token This is in the form `aas_et/_***` and can be used to request access tokens. ##### Get this token The same [script in the gist](https://gist.github.com/rithvikvibhu/952f83ea656c6782fbd0f1645059055d) that gets the access token can also get the master token. Needs Google account creds.  ## Example  Here's the whole flow from just a pair of username/password to using the local API.  Prerequisites: - [grpcurl](https://github.com/fullstorydev/grpcurl) - [Proto files](https://drive.google.com/drive/folders/1RvnN3y-G23pd2SWHmfV_7sef8QU5GNF4?usp=sharing) (preserve folder structure)  ### 1. Get an access token with the script - Download get_tokens.py - Fill in username and password ```sh python3 get_tokens.py # Note down the access token printed. ```  ### 2. Use the access token and get home graph - This prints the json and uses jq to parse and filter out the fields deviceName and localAuthToken - This will give a list of all devices and their local auth tokens ```sh ./grpcurl -H 'authorization: Bearer ya29.a0Af****' \\  -import-path /path/to/protos \\  -proto /path/to/protos/google/internal/home/foyer/v1.proto \\  googlehomefoyer-pa.googleapis.com:443 \\  google.internal.home.foyer.v1.StructuresService/GetHomeGraph | jq '.home.devices[] | {deviceName, localAuthToken}' # Note down the local auth token for the device you want. ```  ### 3. Make the call to the local device using the local auth token ```sh curl -H \"cast-local-authorization-token: LOCAL_AUTH_TOKEN\" --verbose --insecure https://192.168.0.18:8443/setup/bluetooth/status ```
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDeviceInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDeviceInfo::OAIDeviceInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDeviceInfo::OAIDeviceInfo() {
    this->initializeModel();
}

OAIDeviceInfo::~OAIDeviceInfo() {}

void OAIDeviceInfo::initializeModel() {

    m_r_4k_blocked_isSet = false;
    m_r_4k_blocked_isValid = false;

    m_capabilities_isSet = false;
    m_capabilities_isValid = false;

    m_cloud_device_id_isSet = false;
    m_cloud_device_id_isValid = false;

    m_factory_country_code_isSet = false;
    m_factory_country_code_isValid = false;

    m_hotspot_bssid_isSet = false;
    m_hotspot_bssid_isValid = false;

    m_local_authorization_token_hash_isSet = false;
    m_local_authorization_token_hash_isValid = false;

    m_mac_address_isSet = false;
    m_mac_address_isValid = false;

    m_manufacturer_isSet = false;
    m_manufacturer_isValid = false;

    m_model_name_isSet = false;
    m_model_name_isValid = false;

    m_product_name_isSet = false;
    m_product_name_isValid = false;

    m_public_key_isSet = false;
    m_public_key_isValid = false;

    m_ssdp_udn_isSet = false;
    m_ssdp_udn_isValid = false;

    m_uma_client_id_isSet = false;
    m_uma_client_id_isValid = false;

    m_uptime_isSet = false;
    m_uptime_isValid = false;

    m_weave_device_id_isSet = false;
    m_weave_device_id_isValid = false;
}

void OAIDeviceInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDeviceInfo::fromJsonObject(QJsonObject json) {

    m_r_4k_blocked_isValid = ::OpenAPI::fromJsonValue(m_r_4k_blocked, json[QString("4k_blocked")]);
    m_r_4k_blocked_isSet = !json[QString("4k_blocked")].isNull() && m_r_4k_blocked_isValid;

    m_capabilities_isValid = ::OpenAPI::fromJsonValue(m_capabilities, json[QString("capabilities")]);
    m_capabilities_isSet = !json[QString("capabilities")].isNull() && m_capabilities_isValid;

    m_cloud_device_id_isValid = ::OpenAPI::fromJsonValue(m_cloud_device_id, json[QString("cloud_device_id")]);
    m_cloud_device_id_isSet = !json[QString("cloud_device_id")].isNull() && m_cloud_device_id_isValid;

    m_factory_country_code_isValid = ::OpenAPI::fromJsonValue(m_factory_country_code, json[QString("factory_country_code")]);
    m_factory_country_code_isSet = !json[QString("factory_country_code")].isNull() && m_factory_country_code_isValid;

    m_hotspot_bssid_isValid = ::OpenAPI::fromJsonValue(m_hotspot_bssid, json[QString("hotspot_bssid")]);
    m_hotspot_bssid_isSet = !json[QString("hotspot_bssid")].isNull() && m_hotspot_bssid_isValid;

    m_local_authorization_token_hash_isValid = ::OpenAPI::fromJsonValue(m_local_authorization_token_hash, json[QString("local_authorization_token_hash")]);
    m_local_authorization_token_hash_isSet = !json[QString("local_authorization_token_hash")].isNull() && m_local_authorization_token_hash_isValid;

    m_mac_address_isValid = ::OpenAPI::fromJsonValue(m_mac_address, json[QString("mac_address")]);
    m_mac_address_isSet = !json[QString("mac_address")].isNull() && m_mac_address_isValid;

    m_manufacturer_isValid = ::OpenAPI::fromJsonValue(m_manufacturer, json[QString("manufacturer")]);
    m_manufacturer_isSet = !json[QString("manufacturer")].isNull() && m_manufacturer_isValid;

    m_model_name_isValid = ::OpenAPI::fromJsonValue(m_model_name, json[QString("model_name")]);
    m_model_name_isSet = !json[QString("model_name")].isNull() && m_model_name_isValid;

    m_product_name_isValid = ::OpenAPI::fromJsonValue(m_product_name, json[QString("product_name")]);
    m_product_name_isSet = !json[QString("product_name")].isNull() && m_product_name_isValid;

    m_public_key_isValid = ::OpenAPI::fromJsonValue(m_public_key, json[QString("public_key")]);
    m_public_key_isSet = !json[QString("public_key")].isNull() && m_public_key_isValid;

    m_ssdp_udn_isValid = ::OpenAPI::fromJsonValue(m_ssdp_udn, json[QString("ssdp_udn")]);
    m_ssdp_udn_isSet = !json[QString("ssdp_udn")].isNull() && m_ssdp_udn_isValid;

    m_uma_client_id_isValid = ::OpenAPI::fromJsonValue(m_uma_client_id, json[QString("uma_client_id")]);
    m_uma_client_id_isSet = !json[QString("uma_client_id")].isNull() && m_uma_client_id_isValid;

    m_uptime_isValid = ::OpenAPI::fromJsonValue(m_uptime, json[QString("uptime")]);
    m_uptime_isSet = !json[QString("uptime")].isNull() && m_uptime_isValid;

    m_weave_device_id_isValid = ::OpenAPI::fromJsonValue(m_weave_device_id, json[QString("weave_device_id")]);
    m_weave_device_id_isSet = !json[QString("weave_device_id")].isNull() && m_weave_device_id_isValid;
}

QString OAIDeviceInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDeviceInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_r_4k_blocked_isSet) {
        obj.insert(QString("4k_blocked"), ::OpenAPI::toJsonValue(m_r_4k_blocked));
    }
    if (m_capabilities.isSet()) {
        obj.insert(QString("capabilities"), ::OpenAPI::toJsonValue(m_capabilities));
    }
    if (m_cloud_device_id_isSet) {
        obj.insert(QString("cloud_device_id"), ::OpenAPI::toJsonValue(m_cloud_device_id));
    }
    if (m_factory_country_code_isSet) {
        obj.insert(QString("factory_country_code"), ::OpenAPI::toJsonValue(m_factory_country_code));
    }
    if (m_hotspot_bssid_isSet) {
        obj.insert(QString("hotspot_bssid"), ::OpenAPI::toJsonValue(m_hotspot_bssid));
    }
    if (m_local_authorization_token_hash_isSet) {
        obj.insert(QString("local_authorization_token_hash"), ::OpenAPI::toJsonValue(m_local_authorization_token_hash));
    }
    if (m_mac_address_isSet) {
        obj.insert(QString("mac_address"), ::OpenAPI::toJsonValue(m_mac_address));
    }
    if (m_manufacturer_isSet) {
        obj.insert(QString("manufacturer"), ::OpenAPI::toJsonValue(m_manufacturer));
    }
    if (m_model_name_isSet) {
        obj.insert(QString("model_name"), ::OpenAPI::toJsonValue(m_model_name));
    }
    if (m_product_name_isSet) {
        obj.insert(QString("product_name"), ::OpenAPI::toJsonValue(m_product_name));
    }
    if (m_public_key_isSet) {
        obj.insert(QString("public_key"), ::OpenAPI::toJsonValue(m_public_key));
    }
    if (m_ssdp_udn_isSet) {
        obj.insert(QString("ssdp_udn"), ::OpenAPI::toJsonValue(m_ssdp_udn));
    }
    if (m_uma_client_id_isSet) {
        obj.insert(QString("uma_client_id"), ::OpenAPI::toJsonValue(m_uma_client_id));
    }
    if (m_uptime_isSet) {
        obj.insert(QString("uptime"), ::OpenAPI::toJsonValue(m_uptime));
    }
    if (m_weave_device_id_isSet) {
        obj.insert(QString("weave_device_id"), ::OpenAPI::toJsonValue(m_weave_device_id));
    }
    return obj;
}

qint32 OAIDeviceInfo::getR4kBlocked() const {
    return m_r_4k_blocked;
}
void OAIDeviceInfo::setR4kBlocked(const qint32 &r_4k_blocked) {
    m_r_4k_blocked = r_4k_blocked;
    m_r_4k_blocked_isSet = true;
}

bool OAIDeviceInfo::is_r_4k_blocked_Set() const{
    return m_r_4k_blocked_isSet;
}

bool OAIDeviceInfo::is_r_4k_blocked_Valid() const{
    return m_r_4k_blocked_isValid;
}

OAICapabilities OAIDeviceInfo::getCapabilities() const {
    return m_capabilities;
}
void OAIDeviceInfo::setCapabilities(const OAICapabilities &capabilities) {
    m_capabilities = capabilities;
    m_capabilities_isSet = true;
}

bool OAIDeviceInfo::is_capabilities_Set() const{
    return m_capabilities_isSet;
}

bool OAIDeviceInfo::is_capabilities_Valid() const{
    return m_capabilities_isValid;
}

QString OAIDeviceInfo::getCloudDeviceId() const {
    return m_cloud_device_id;
}
void OAIDeviceInfo::setCloudDeviceId(const QString &cloud_device_id) {
    m_cloud_device_id = cloud_device_id;
    m_cloud_device_id_isSet = true;
}

bool OAIDeviceInfo::is_cloud_device_id_Set() const{
    return m_cloud_device_id_isSet;
}

bool OAIDeviceInfo::is_cloud_device_id_Valid() const{
    return m_cloud_device_id_isValid;
}

QString OAIDeviceInfo::getFactoryCountryCode() const {
    return m_factory_country_code;
}
void OAIDeviceInfo::setFactoryCountryCode(const QString &factory_country_code) {
    m_factory_country_code = factory_country_code;
    m_factory_country_code_isSet = true;
}

bool OAIDeviceInfo::is_factory_country_code_Set() const{
    return m_factory_country_code_isSet;
}

bool OAIDeviceInfo::is_factory_country_code_Valid() const{
    return m_factory_country_code_isValid;
}

QString OAIDeviceInfo::getHotspotBssid() const {
    return m_hotspot_bssid;
}
void OAIDeviceInfo::setHotspotBssid(const QString &hotspot_bssid) {
    m_hotspot_bssid = hotspot_bssid;
    m_hotspot_bssid_isSet = true;
}

bool OAIDeviceInfo::is_hotspot_bssid_Set() const{
    return m_hotspot_bssid_isSet;
}

bool OAIDeviceInfo::is_hotspot_bssid_Valid() const{
    return m_hotspot_bssid_isValid;
}

QString OAIDeviceInfo::getLocalAuthorizationTokenHash() const {
    return m_local_authorization_token_hash;
}
void OAIDeviceInfo::setLocalAuthorizationTokenHash(const QString &local_authorization_token_hash) {
    m_local_authorization_token_hash = local_authorization_token_hash;
    m_local_authorization_token_hash_isSet = true;
}

bool OAIDeviceInfo::is_local_authorization_token_hash_Set() const{
    return m_local_authorization_token_hash_isSet;
}

bool OAIDeviceInfo::is_local_authorization_token_hash_Valid() const{
    return m_local_authorization_token_hash_isValid;
}

QString OAIDeviceInfo::getMacAddress() const {
    return m_mac_address;
}
void OAIDeviceInfo::setMacAddress(const QString &mac_address) {
    m_mac_address = mac_address;
    m_mac_address_isSet = true;
}

bool OAIDeviceInfo::is_mac_address_Set() const{
    return m_mac_address_isSet;
}

bool OAIDeviceInfo::is_mac_address_Valid() const{
    return m_mac_address_isValid;
}

QString OAIDeviceInfo::getManufacturer() const {
    return m_manufacturer;
}
void OAIDeviceInfo::setManufacturer(const QString &manufacturer) {
    m_manufacturer = manufacturer;
    m_manufacturer_isSet = true;
}

bool OAIDeviceInfo::is_manufacturer_Set() const{
    return m_manufacturer_isSet;
}

bool OAIDeviceInfo::is_manufacturer_Valid() const{
    return m_manufacturer_isValid;
}

QString OAIDeviceInfo::getModelName() const {
    return m_model_name;
}
void OAIDeviceInfo::setModelName(const QString &model_name) {
    m_model_name = model_name;
    m_model_name_isSet = true;
}

bool OAIDeviceInfo::is_model_name_Set() const{
    return m_model_name_isSet;
}

bool OAIDeviceInfo::is_model_name_Valid() const{
    return m_model_name_isValid;
}

QString OAIDeviceInfo::getProductName() const {
    return m_product_name;
}
void OAIDeviceInfo::setProductName(const QString &product_name) {
    m_product_name = product_name;
    m_product_name_isSet = true;
}

bool OAIDeviceInfo::is_product_name_Set() const{
    return m_product_name_isSet;
}

bool OAIDeviceInfo::is_product_name_Valid() const{
    return m_product_name_isValid;
}

QString OAIDeviceInfo::getPublicKey() const {
    return m_public_key;
}
void OAIDeviceInfo::setPublicKey(const QString &public_key) {
    m_public_key = public_key;
    m_public_key_isSet = true;
}

bool OAIDeviceInfo::is_public_key_Set() const{
    return m_public_key_isSet;
}

bool OAIDeviceInfo::is_public_key_Valid() const{
    return m_public_key_isValid;
}

QString OAIDeviceInfo::getSsdpUdn() const {
    return m_ssdp_udn;
}
void OAIDeviceInfo::setSsdpUdn(const QString &ssdp_udn) {
    m_ssdp_udn = ssdp_udn;
    m_ssdp_udn_isSet = true;
}

bool OAIDeviceInfo::is_ssdp_udn_Set() const{
    return m_ssdp_udn_isSet;
}

bool OAIDeviceInfo::is_ssdp_udn_Valid() const{
    return m_ssdp_udn_isValid;
}

QString OAIDeviceInfo::getUmaClientId() const {
    return m_uma_client_id;
}
void OAIDeviceInfo::setUmaClientId(const QString &uma_client_id) {
    m_uma_client_id = uma_client_id;
    m_uma_client_id_isSet = true;
}

bool OAIDeviceInfo::is_uma_client_id_Set() const{
    return m_uma_client_id_isSet;
}

bool OAIDeviceInfo::is_uma_client_id_Valid() const{
    return m_uma_client_id_isValid;
}

double OAIDeviceInfo::getUptime() const {
    return m_uptime;
}
void OAIDeviceInfo::setUptime(const double &uptime) {
    m_uptime = uptime;
    m_uptime_isSet = true;
}

bool OAIDeviceInfo::is_uptime_Set() const{
    return m_uptime_isSet;
}

bool OAIDeviceInfo::is_uptime_Valid() const{
    return m_uptime_isValid;
}

QString OAIDeviceInfo::getWeaveDeviceId() const {
    return m_weave_device_id;
}
void OAIDeviceInfo::setWeaveDeviceId(const QString &weave_device_id) {
    m_weave_device_id = weave_device_id;
    m_weave_device_id_isSet = true;
}

bool OAIDeviceInfo::is_weave_device_id_Set() const{
    return m_weave_device_id_isSet;
}

bool OAIDeviceInfo::is_weave_device_id_Valid() const{
    return m_weave_device_id_isValid;
}

bool OAIDeviceInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_r_4k_blocked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_capabilities.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_cloud_device_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_factory_country_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hotspot_bssid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_local_authorization_token_hash_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mac_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_manufacturer_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_model_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_public_key_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ssdp_udn_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uma_client_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uptime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_weave_device_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDeviceInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_r_4k_blocked_isValid && m_capabilities_isValid && m_cloud_device_id_isValid && m_factory_country_code_isValid && m_hotspot_bssid_isValid && m_local_authorization_token_hash_isValid && m_mac_address_isValid && m_manufacturer_isValid && m_model_name_isValid && m_product_name_isValid && m_public_key_isValid && m_ssdp_udn_isValid && m_uma_client_id_isValid && m_uptime_isValid && m_weave_device_id_isValid && true;
}

} // namespace OpenAPI
