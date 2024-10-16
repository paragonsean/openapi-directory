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

#include "OAIScanfordevicesRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIScanfordevicesRequest::OAIScanfordevicesRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIScanfordevicesRequest::OAIScanfordevicesRequest() {
    this->initializeModel();
}

OAIScanfordevicesRequest::~OAIScanfordevicesRequest() {}

void OAIScanfordevicesRequest::initializeModel() {

    m_clear_results_isSet = false;
    m_clear_results_isValid = false;

    m_enable_isSet = false;
    m_enable_isValid = false;

    m_timeout_isSet = false;
    m_timeout_isValid = false;
}

void OAIScanfordevicesRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIScanfordevicesRequest::fromJsonObject(QJsonObject json) {

    m_clear_results_isValid = ::OpenAPI::fromJsonValue(m_clear_results, json[QString("clear_results")]);
    m_clear_results_isSet = !json[QString("clear_results")].isNull() && m_clear_results_isValid;

    m_enable_isValid = ::OpenAPI::fromJsonValue(m_enable, json[QString("enable")]);
    m_enable_isSet = !json[QString("enable")].isNull() && m_enable_isValid;

    m_timeout_isValid = ::OpenAPI::fromJsonValue(m_timeout, json[QString("timeout")]);
    m_timeout_isSet = !json[QString("timeout")].isNull() && m_timeout_isValid;
}

QString OAIScanfordevicesRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIScanfordevicesRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_clear_results_isSet) {
        obj.insert(QString("clear_results"), ::OpenAPI::toJsonValue(m_clear_results));
    }
    if (m_enable_isSet) {
        obj.insert(QString("enable"), ::OpenAPI::toJsonValue(m_enable));
    }
    if (m_timeout_isSet) {
        obj.insert(QString("timeout"), ::OpenAPI::toJsonValue(m_timeout));
    }
    return obj;
}

bool OAIScanfordevicesRequest::isClearResults() const {
    return m_clear_results;
}
void OAIScanfordevicesRequest::setClearResults(const bool &clear_results) {
    m_clear_results = clear_results;
    m_clear_results_isSet = true;
}

bool OAIScanfordevicesRequest::is_clear_results_Set() const{
    return m_clear_results_isSet;
}

bool OAIScanfordevicesRequest::is_clear_results_Valid() const{
    return m_clear_results_isValid;
}

bool OAIScanfordevicesRequest::isEnable() const {
    return m_enable;
}
void OAIScanfordevicesRequest::setEnable(const bool &enable) {
    m_enable = enable;
    m_enable_isSet = true;
}

bool OAIScanfordevicesRequest::is_enable_Set() const{
    return m_enable_isSet;
}

bool OAIScanfordevicesRequest::is_enable_Valid() const{
    return m_enable_isValid;
}

qint32 OAIScanfordevicesRequest::getTimeout() const {
    return m_timeout;
}
void OAIScanfordevicesRequest::setTimeout(const qint32 &timeout) {
    m_timeout = timeout;
    m_timeout_isSet = true;
}

bool OAIScanfordevicesRequest::is_timeout_Set() const{
    return m_timeout_isSet;
}

bool OAIScanfordevicesRequest::is_timeout_Valid() const{
    return m_timeout_isValid;
}

bool OAIScanfordevicesRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_clear_results_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timeout_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIScanfordevicesRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_clear_results_isValid && m_enable_isValid && m_timeout_isValid && true;
}

} // namespace OpenAPI
