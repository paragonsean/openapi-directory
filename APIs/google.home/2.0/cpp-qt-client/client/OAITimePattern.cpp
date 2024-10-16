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

#include "OAITimePattern.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITimePattern::OAITimePattern(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITimePattern::OAITimePattern() {
    this->initializeModel();
}

OAITimePattern::~OAITimePattern() {}

void OAITimePattern::initializeModel() {

    m_hour_isSet = false;
    m_hour_isValid = false;

    m_minute_isSet = false;
    m_minute_isValid = false;

    m_second_isSet = false;
    m_second_isValid = false;
}

void OAITimePattern::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITimePattern::fromJsonObject(QJsonObject json) {

    m_hour_isValid = ::OpenAPI::fromJsonValue(m_hour, json[QString("hour")]);
    m_hour_isSet = !json[QString("hour")].isNull() && m_hour_isValid;

    m_minute_isValid = ::OpenAPI::fromJsonValue(m_minute, json[QString("minute")]);
    m_minute_isSet = !json[QString("minute")].isNull() && m_minute_isValid;

    m_second_isValid = ::OpenAPI::fromJsonValue(m_second, json[QString("second")]);
    m_second_isSet = !json[QString("second")].isNull() && m_second_isValid;
}

QString OAITimePattern::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITimePattern::asJsonObject() const {
    QJsonObject obj;
    if (m_hour_isSet) {
        obj.insert(QString("hour"), ::OpenAPI::toJsonValue(m_hour));
    }
    if (m_minute_isSet) {
        obj.insert(QString("minute"), ::OpenAPI::toJsonValue(m_minute));
    }
    if (m_second_isSet) {
        obj.insert(QString("second"), ::OpenAPI::toJsonValue(m_second));
    }
    return obj;
}

qint32 OAITimePattern::getHour() const {
    return m_hour;
}
void OAITimePattern::setHour(const qint32 &hour) {
    m_hour = hour;
    m_hour_isSet = true;
}

bool OAITimePattern::is_hour_Set() const{
    return m_hour_isSet;
}

bool OAITimePattern::is_hour_Valid() const{
    return m_hour_isValid;
}

qint32 OAITimePattern::getMinute() const {
    return m_minute;
}
void OAITimePattern::setMinute(const qint32 &minute) {
    m_minute = minute;
    m_minute_isSet = true;
}

bool OAITimePattern::is_minute_Set() const{
    return m_minute_isSet;
}

bool OAITimePattern::is_minute_Valid() const{
    return m_minute_isValid;
}

qint32 OAITimePattern::getSecond() const {
    return m_second;
}
void OAITimePattern::setSecond(const qint32 &second) {
    m_second = second;
    m_second_isSet = true;
}

bool OAITimePattern::is_second_Set() const{
    return m_second_isSet;
}

bool OAITimePattern::is_second_Valid() const{
    return m_second_isValid;
}

bool OAITimePattern::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_hour_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_minute_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_second_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITimePattern::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_hour_isValid && m_minute_isValid && m_second_isValid && true;
}

} // namespace OpenAPI
