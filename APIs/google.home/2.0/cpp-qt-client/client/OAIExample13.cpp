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

#include "OAIExample13.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExample13::OAIExample13(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExample13::OAIExample13() {
    this->initializeModel();
}

OAIExample13::~OAIExample13() {}

void OAIExample13::initializeModel() {

    m_can_enroll_isSet = false;
    m_can_enroll_isValid = false;

    m_enrollment_state_isSet = false;
    m_enrollment_state_isValid = false;

    m_error_code_isSet = false;
    m_error_code_isValid = false;

    m_ready_isSet = false;
    m_ready_isValid = false;

    m_retryable_isSet = false;
    m_retryable_isValid = false;
}

void OAIExample13::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExample13::fromJsonObject(QJsonObject json) {

    m_can_enroll_isValid = ::OpenAPI::fromJsonValue(m_can_enroll, json[QString("can_enroll")]);
    m_can_enroll_isSet = !json[QString("can_enroll")].isNull() && m_can_enroll_isValid;

    m_enrollment_state_isValid = ::OpenAPI::fromJsonValue(m_enrollment_state, json[QString("enrollment_state")]);
    m_enrollment_state_isSet = !json[QString("enrollment_state")].isNull() && m_enrollment_state_isValid;

    m_error_code_isValid = ::OpenAPI::fromJsonValue(m_error_code, json[QString("error_code")]);
    m_error_code_isSet = !json[QString("error_code")].isNull() && m_error_code_isValid;

    m_ready_isValid = ::OpenAPI::fromJsonValue(m_ready, json[QString("ready")]);
    m_ready_isSet = !json[QString("ready")].isNull() && m_ready_isValid;

    m_retryable_isValid = ::OpenAPI::fromJsonValue(m_retryable, json[QString("retryable")]);
    m_retryable_isSet = !json[QString("retryable")].isNull() && m_retryable_isValid;
}

QString OAIExample13::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExample13::asJsonObject() const {
    QJsonObject obj;
    if (m_can_enroll_isSet) {
        obj.insert(QString("can_enroll"), ::OpenAPI::toJsonValue(m_can_enroll));
    }
    if (m_enrollment_state_isSet) {
        obj.insert(QString("enrollment_state"), ::OpenAPI::toJsonValue(m_enrollment_state));
    }
    if (m_error_code_isSet) {
        obj.insert(QString("error_code"), ::OpenAPI::toJsonValue(m_error_code));
    }
    if (m_ready_isSet) {
        obj.insert(QString("ready"), ::OpenAPI::toJsonValue(m_ready));
    }
    if (m_retryable_isSet) {
        obj.insert(QString("retryable"), ::OpenAPI::toJsonValue(m_retryable));
    }
    return obj;
}

bool OAIExample13::isCanEnroll() const {
    return m_can_enroll;
}
void OAIExample13::setCanEnroll(const bool &can_enroll) {
    m_can_enroll = can_enroll;
    m_can_enroll_isSet = true;
}

bool OAIExample13::is_can_enroll_Set() const{
    return m_can_enroll_isSet;
}

bool OAIExample13::is_can_enroll_Valid() const{
    return m_can_enroll_isValid;
}

qint32 OAIExample13::getEnrollmentState() const {
    return m_enrollment_state;
}
void OAIExample13::setEnrollmentState(const qint32 &enrollment_state) {
    m_enrollment_state = enrollment_state;
    m_enrollment_state_isSet = true;
}

bool OAIExample13::is_enrollment_state_Set() const{
    return m_enrollment_state_isSet;
}

bool OAIExample13::is_enrollment_state_Valid() const{
    return m_enrollment_state_isValid;
}

qint32 OAIExample13::getErrorCode() const {
    return m_error_code;
}
void OAIExample13::setErrorCode(const qint32 &error_code) {
    m_error_code = error_code;
    m_error_code_isSet = true;
}

bool OAIExample13::is_error_code_Set() const{
    return m_error_code_isSet;
}

bool OAIExample13::is_error_code_Valid() const{
    return m_error_code_isValid;
}

bool OAIExample13::isReady() const {
    return m_ready;
}
void OAIExample13::setReady(const bool &ready) {
    m_ready = ready;
    m_ready_isSet = true;
}

bool OAIExample13::is_ready_Set() const{
    return m_ready_isSet;
}

bool OAIExample13::is_ready_Valid() const{
    return m_ready_isValid;
}

bool OAIExample13::isRetryable() const {
    return m_retryable;
}
void OAIExample13::setRetryable(const bool &retryable) {
    m_retryable = retryable;
    m_retryable_isSet = true;
}

bool OAIExample13::is_retryable_Set() const{
    return m_retryable_isSet;
}

bool OAIExample13::is_retryable_Valid() const{
    return m_retryable_isValid;
}

bool OAIExample13::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_can_enroll_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enrollment_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ready_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_retryable_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExample13::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_can_enroll_isValid && m_enrollment_state_isValid && m_error_code_isValid && m_ready_isValid && m_retryable_isValid && true;
}

} // namespace OpenAPI
