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

#include "OAIExample16.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExample16::OAIExample16(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExample16::OAIExample16() {
    this->initializeModel();
}

OAIExample16::~OAIExample16() {}

void OAIExample16::initializeModel() {

    m_bytes_received_isSet = false;
    m_bytes_received_isValid = false;

    m_response_code_isSet = false;
    m_response_code_isValid = false;

    m_time_for_data_fetch_isSet = false;
    m_time_for_data_fetch_isValid = false;

    m_time_for_http_response_isSet = false;
    m_time_for_http_response_isValid = false;
}

void OAIExample16::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExample16::fromJsonObject(QJsonObject json) {

    m_bytes_received_isValid = ::OpenAPI::fromJsonValue(m_bytes_received, json[QString("bytes_received")]);
    m_bytes_received_isSet = !json[QString("bytes_received")].isNull() && m_bytes_received_isValid;

    m_response_code_isValid = ::OpenAPI::fromJsonValue(m_response_code, json[QString("response_code")]);
    m_response_code_isSet = !json[QString("response_code")].isNull() && m_response_code_isValid;

    m_time_for_data_fetch_isValid = ::OpenAPI::fromJsonValue(m_time_for_data_fetch, json[QString("time_for_data_fetch")]);
    m_time_for_data_fetch_isSet = !json[QString("time_for_data_fetch")].isNull() && m_time_for_data_fetch_isValid;

    m_time_for_http_response_isValid = ::OpenAPI::fromJsonValue(m_time_for_http_response, json[QString("time_for_http_response")]);
    m_time_for_http_response_isSet = !json[QString("time_for_http_response")].isNull() && m_time_for_http_response_isValid;
}

QString OAIExample16::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExample16::asJsonObject() const {
    QJsonObject obj;
    if (m_bytes_received_isSet) {
        obj.insert(QString("bytes_received"), ::OpenAPI::toJsonValue(m_bytes_received));
    }
    if (m_response_code_isSet) {
        obj.insert(QString("response_code"), ::OpenAPI::toJsonValue(m_response_code));
    }
    if (m_time_for_data_fetch_isSet) {
        obj.insert(QString("time_for_data_fetch"), ::OpenAPI::toJsonValue(m_time_for_data_fetch));
    }
    if (m_time_for_http_response_isSet) {
        obj.insert(QString("time_for_http_response"), ::OpenAPI::toJsonValue(m_time_for_http_response));
    }
    return obj;
}

qint32 OAIExample16::getBytesReceived() const {
    return m_bytes_received;
}
void OAIExample16::setBytesReceived(const qint32 &bytes_received) {
    m_bytes_received = bytes_received;
    m_bytes_received_isSet = true;
}

bool OAIExample16::is_bytes_received_Set() const{
    return m_bytes_received_isSet;
}

bool OAIExample16::is_bytes_received_Valid() const{
    return m_bytes_received_isValid;
}

qint32 OAIExample16::getResponseCode() const {
    return m_response_code;
}
void OAIExample16::setResponseCode(const qint32 &response_code) {
    m_response_code = response_code;
    m_response_code_isSet = true;
}

bool OAIExample16::is_response_code_Set() const{
    return m_response_code_isSet;
}

bool OAIExample16::is_response_code_Valid() const{
    return m_response_code_isValid;
}

qint32 OAIExample16::getTimeForDataFetch() const {
    return m_time_for_data_fetch;
}
void OAIExample16::setTimeForDataFetch(const qint32 &time_for_data_fetch) {
    m_time_for_data_fetch = time_for_data_fetch;
    m_time_for_data_fetch_isSet = true;
}

bool OAIExample16::is_time_for_data_fetch_Set() const{
    return m_time_for_data_fetch_isSet;
}

bool OAIExample16::is_time_for_data_fetch_Valid() const{
    return m_time_for_data_fetch_isValid;
}

qint32 OAIExample16::getTimeForHttpResponse() const {
    return m_time_for_http_response;
}
void OAIExample16::setTimeForHttpResponse(const qint32 &time_for_http_response) {
    m_time_for_http_response = time_for_http_response;
    m_time_for_http_response_isSet = true;
}

bool OAIExample16::is_time_for_http_response_Set() const{
    return m_time_for_http_response_isSet;
}

bool OAIExample16::is_time_for_http_response_Valid() const{
    return m_time_for_http_response_isValid;
}

bool OAIExample16::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bytes_received_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_response_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_for_data_fetch_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_for_http_response_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExample16::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_bytes_received_isValid && m_response_code_isValid && m_time_for_data_fetch_isValid && m_time_for_http_response_isValid && true;
}

} // namespace OpenAPI
