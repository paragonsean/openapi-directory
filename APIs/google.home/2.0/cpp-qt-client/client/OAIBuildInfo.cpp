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

#include "OAIBuildInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBuildInfo::OAIBuildInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBuildInfo::OAIBuildInfo() {
    this->initializeModel();
}

OAIBuildInfo::~OAIBuildInfo() {}

void OAIBuildInfo::initializeModel() {

    m_build_type_isSet = false;
    m_build_type_isValid = false;

    m_cast_build_revision_isSet = false;
    m_cast_build_revision_isValid = false;

    m_cast_control_version_isSet = false;
    m_cast_control_version_isValid = false;

    m_preview_channel_state_isSet = false;
    m_preview_channel_state_isValid = false;

    m_release_track_isSet = false;
    m_release_track_isValid = false;

    m_system_build_number_isSet = false;
    m_system_build_number_isValid = false;
}

void OAIBuildInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBuildInfo::fromJsonObject(QJsonObject json) {

    m_build_type_isValid = ::OpenAPI::fromJsonValue(m_build_type, json[QString("build_type")]);
    m_build_type_isSet = !json[QString("build_type")].isNull() && m_build_type_isValid;

    m_cast_build_revision_isValid = ::OpenAPI::fromJsonValue(m_cast_build_revision, json[QString("cast_build_revision")]);
    m_cast_build_revision_isSet = !json[QString("cast_build_revision")].isNull() && m_cast_build_revision_isValid;

    m_cast_control_version_isValid = ::OpenAPI::fromJsonValue(m_cast_control_version, json[QString("cast_control_version")]);
    m_cast_control_version_isSet = !json[QString("cast_control_version")].isNull() && m_cast_control_version_isValid;

    m_preview_channel_state_isValid = ::OpenAPI::fromJsonValue(m_preview_channel_state, json[QString("preview_channel_state")]);
    m_preview_channel_state_isSet = !json[QString("preview_channel_state")].isNull() && m_preview_channel_state_isValid;

    m_release_track_isValid = ::OpenAPI::fromJsonValue(m_release_track, json[QString("release_track")]);
    m_release_track_isSet = !json[QString("release_track")].isNull() && m_release_track_isValid;

    m_system_build_number_isValid = ::OpenAPI::fromJsonValue(m_system_build_number, json[QString("system_build_number")]);
    m_system_build_number_isSet = !json[QString("system_build_number")].isNull() && m_system_build_number_isValid;
}

QString OAIBuildInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBuildInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_build_type_isSet) {
        obj.insert(QString("build_type"), ::OpenAPI::toJsonValue(m_build_type));
    }
    if (m_cast_build_revision_isSet) {
        obj.insert(QString("cast_build_revision"), ::OpenAPI::toJsonValue(m_cast_build_revision));
    }
    if (m_cast_control_version_isSet) {
        obj.insert(QString("cast_control_version"), ::OpenAPI::toJsonValue(m_cast_control_version));
    }
    if (m_preview_channel_state_isSet) {
        obj.insert(QString("preview_channel_state"), ::OpenAPI::toJsonValue(m_preview_channel_state));
    }
    if (m_release_track_isSet) {
        obj.insert(QString("release_track"), ::OpenAPI::toJsonValue(m_release_track));
    }
    if (m_system_build_number_isSet) {
        obj.insert(QString("system_build_number"), ::OpenAPI::toJsonValue(m_system_build_number));
    }
    return obj;
}

qint32 OAIBuildInfo::getBuildType() const {
    return m_build_type;
}
void OAIBuildInfo::setBuildType(const qint32 &build_type) {
    m_build_type = build_type;
    m_build_type_isSet = true;
}

bool OAIBuildInfo::is_build_type_Set() const{
    return m_build_type_isSet;
}

bool OAIBuildInfo::is_build_type_Valid() const{
    return m_build_type_isValid;
}

QString OAIBuildInfo::getCastBuildRevision() const {
    return m_cast_build_revision;
}
void OAIBuildInfo::setCastBuildRevision(const QString &cast_build_revision) {
    m_cast_build_revision = cast_build_revision;
    m_cast_build_revision_isSet = true;
}

bool OAIBuildInfo::is_cast_build_revision_Set() const{
    return m_cast_build_revision_isSet;
}

bool OAIBuildInfo::is_cast_build_revision_Valid() const{
    return m_cast_build_revision_isValid;
}

qint32 OAIBuildInfo::getCastControlVersion() const {
    return m_cast_control_version;
}
void OAIBuildInfo::setCastControlVersion(const qint32 &cast_control_version) {
    m_cast_control_version = cast_control_version;
    m_cast_control_version_isSet = true;
}

bool OAIBuildInfo::is_cast_control_version_Set() const{
    return m_cast_control_version_isSet;
}

bool OAIBuildInfo::is_cast_control_version_Valid() const{
    return m_cast_control_version_isValid;
}

qint32 OAIBuildInfo::getPreviewChannelState() const {
    return m_preview_channel_state;
}
void OAIBuildInfo::setPreviewChannelState(const qint32 &preview_channel_state) {
    m_preview_channel_state = preview_channel_state;
    m_preview_channel_state_isSet = true;
}

bool OAIBuildInfo::is_preview_channel_state_Set() const{
    return m_preview_channel_state_isSet;
}

bool OAIBuildInfo::is_preview_channel_state_Valid() const{
    return m_preview_channel_state_isValid;
}

QString OAIBuildInfo::getReleaseTrack() const {
    return m_release_track;
}
void OAIBuildInfo::setReleaseTrack(const QString &release_track) {
    m_release_track = release_track;
    m_release_track_isSet = true;
}

bool OAIBuildInfo::is_release_track_Set() const{
    return m_release_track_isSet;
}

bool OAIBuildInfo::is_release_track_Valid() const{
    return m_release_track_isValid;
}

QString OAIBuildInfo::getSystemBuildNumber() const {
    return m_system_build_number;
}
void OAIBuildInfo::setSystemBuildNumber(const QString &system_build_number) {
    m_system_build_number = system_build_number;
    m_system_build_number_isSet = true;
}

bool OAIBuildInfo::is_system_build_number_Set() const{
    return m_system_build_number_isSet;
}

bool OAIBuildInfo::is_system_build_number_Valid() const{
    return m_system_build_number_isValid;
}

bool OAIBuildInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_build_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cast_build_revision_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cast_control_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_preview_channel_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_release_track_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_system_build_number_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBuildInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_build_type_isValid && m_cast_build_revision_isValid && m_cast_control_version_isValid && m_preview_channel_state_isValid && m_release_track_isValid && m_system_build_number_isValid && true;
}

} // namespace OpenAPI
