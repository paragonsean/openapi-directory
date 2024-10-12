/**
 * Climate FieldView Platform APIs
 * **Last Modified**: Wed Jan  4 12:47:29 UTC 2023   All endpoints are only accessible via HTTPS.  * All API endpoints are located at `https://platform.climate.com` (e.g. `https://platform.climate.com/v4/fields`).  * The authorization token endpoint is located at `https://api.climate.com/api/oauth/token`.  ## Troubleshooting  `X-Http-Request-Id` response header will be returned on every call, successful or not. If you experience an issue with our api and need to contact technical support, please supply the value of the `X-Http-Request-Id` header along with an approximate time of when the request was made.  ## Request Limits  When you’re onboarded to Climate’s API platform, your `x-api-key` is assigned a custom usage plan. Usage plans are unique to each partner and have the following key attributes:   1. Throttling information     * burstLimit: Maximum rate limit over a period ranging from 1 second to a few seconds     * rateLimit: A steady-state rate limit  2. Quota information     * Limit: The maximum number of requests that can be made in a given month  When the request rate threshold is exceeded, a `429` response code is returned. Optionally, the [`Retry-After`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37) header may be returned:   Following are examples of rate limit errors:  1. Rate limit exceeded:  <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 32     {\"message\":\"Too Many Requests\"}  2. Quota exhausted: <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 29      {\"message\":\"Limit Exceeded\"}  ## Pagination  Pagination is performed via headers. Any request which returns a `\"results\"` array may be paginated. The following figure shows how query results are laid out with X-Limit=4 and no filter applied.  <img style=\"width:70%;height:auto;\" src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/paging.png\">  * If there are no results, a response code of `304` will be returned.  * If the response is the last set of results, a response code of `200` or `206` will be returned.  * If there are more results, a response code of `206` will be returned.  * If `X-Next-Token` is provided in the request headers but the token has expired, a response code of `409` will be returned. This is only applicable for some endpoints; see specific endpoint documentation below.  #### X-Limit  The page size can be controlled with the `X-Limit` header. Valid values are `1-100` and defaults to `100`.  #### X-Next-Token  If the results are paginated, a response header of `X-Next-Token` will be returned. Use the associated value in the subsequent request (via the `X-Next-Token` request header) to retrieve the next page. The following sequence diagram shows how to use `X-Next-Token` to fetch all the records.  <img src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/x-next-token.svg\">   ## Chunked Uploads  Uploads larger than `5MiB` (`5242880 bytes`) must be done in `5MiB` chunks (with the exception of the final chunk). Each chunk request MUST contain a `Content-Range` header specifying the portion of the upload, and a `Content-Type` header specifying binary content type (`application/octet-stream`). Range uploads must be contiguous. The maximum upload size is capped at `500MiB` (`524288000 bytes`).  ## Chunked Downloads  Downloads larger than `5MiB` (`5242880 bytes`) must be done in `1-5MiB` chunks (with the exception of the final chunk, which may be less than `1MiB`). Each chunk request MUST contain a `Range` header specifying the requested portion of the download, and an `Accept` header specifying binary and json content types  (`application/octet-stream,application/json`) or all content types (`*_/_*`).  ## Drivers  If you need drivers to process agronomic data, download the ADAPT plugin below. We only support the plugin in the Windows environment, minimum is Windows 7 SP1.  For asPlanted, asHarvested and asApplied data: * [ADAPT Plugin](https://dev.fieldview.com/drivers/ClimateADAPTPlugin_latest.exe) <br>Release notes can be found [here](https://dev.fieldview.com/drivers/adapt-release-notes.txt). <br>Download and use of the ADAPT plugin means that you agree to the EULA for use of the ADAPT plugin.  <br>Please review the [EULA](https://dev.fieldview.com/EULA/ADAPT%20Plugin%20EULA-06-19.pdf) (last updated on June 6th, 2019) before download and use of the ADAPT plugin. <br>For more information, please refer to:   * [ADAPT Resources](https://adaptframework.org/)   * [ADAPT Overview](https://aggateway.atlassian.net/wiki/spaces/ADM/overview)   * [ADAPT FAQ](https://aggateway.atlassian.net/wiki/spaces/ADM/pages/165942474/ADAPT+Frequently-Asked+Questions+FAQ)   * [ADAPT Videos](https://adaptframework.org/adapt-videos/)  ## Sample Test Data  Sample agronomic data: * [asPlanted and asHarvested data](https://dev.fieldview.com/sample-agronomic-data/Planting_Harvesting_data_04_18_2018_21_46_18.zip) * [asApplied data set 1](https://dev.fieldview.com/sample-agronomic-data/as-applied-data1.zip) * [asApplied data set 2](https://dev.fieldview.com/sample-agronomic-data/as-applied-data2.zip) <br>To upload the sample data to your account, please follow the instructions in this [link](https://support.climate.com/kt#/kA02A000000AaxzSAC/en_US).  Sample soil data: * [Sample soil data](https://dev.fieldview.com/sample-soil-data/soil-sample.xml) --- 
 *
 * The version of the OpenAPI document: 4.0.11
 * Contact: developer@climate.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIExportStatus.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIExportStatus::OAIExportStatus(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIExportStatus::OAIExportStatus() {
    this->initializeModel();
}

OAIExportStatus::~OAIExportStatus() {}

void OAIExportStatus::initializeModel() {

    m_checksum_isSet = false;
    m_checksum_isValid = false;

    m_error_isSet = false;
    m_error_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_x_next_token_isSet = false;
    m_x_next_token_isValid = false;
}

void OAIExportStatus::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIExportStatus::fromJsonObject(QJsonObject json) {

    m_checksum_isValid = ::OpenAPI::fromJsonValue(m_checksum, json[QString("checksum")]);
    m_checksum_isSet = !json[QString("checksum")].isNull() && m_checksum_isValid;

    m_error_isValid = ::OpenAPI::fromJsonValue(m_error, json[QString("error")]);
    m_error_isSet = !json[QString("error")].isNull() && m_error_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_x_next_token_isValid = ::OpenAPI::fromJsonValue(m_x_next_token, json[QString("xNextToken")]);
    m_x_next_token_isSet = !json[QString("xNextToken")].isNull() && m_x_next_token_isValid;
}

QString OAIExportStatus::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIExportStatus::asJsonObject() const {
    QJsonObject obj;
    if (m_checksum_isSet) {
        obj.insert(QString("checksum"), ::OpenAPI::toJsonValue(m_checksum));
    }
    if (m_error_isSet) {
        obj.insert(QString("error"), ::OpenAPI::toJsonValue(m_error));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_x_next_token_isSet) {
        obj.insert(QString("xNextToken"), ::OpenAPI::toJsonValue(m_x_next_token));
    }
    return obj;
}

QString OAIExportStatus::getChecksum() const {
    return m_checksum;
}
void OAIExportStatus::setChecksum(const QString &checksum) {
    m_checksum = checksum;
    m_checksum_isSet = true;
}

bool OAIExportStatus::is_checksum_Set() const{
    return m_checksum_isSet;
}

bool OAIExportStatus::is_checksum_Valid() const{
    return m_checksum_isValid;
}

QString OAIExportStatus::getError() const {
    return m_error;
}
void OAIExportStatus::setError(const QString &error) {
    m_error = error;
    m_error_isSet = true;
}

bool OAIExportStatus::is_error_Set() const{
    return m_error_isSet;
}

bool OAIExportStatus::is_error_Valid() const{
    return m_error_isValid;
}

qint64 OAIExportStatus::getSize() const {
    return m_size;
}
void OAIExportStatus::setSize(const qint64 &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIExportStatus::is_size_Set() const{
    return m_size_isSet;
}

bool OAIExportStatus::is_size_Valid() const{
    return m_size_isValid;
}

QString OAIExportStatus::getStatus() const {
    return m_status;
}
void OAIExportStatus::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIExportStatus::is_status_Set() const{
    return m_status_isSet;
}

bool OAIExportStatus::is_status_Valid() const{
    return m_status_isValid;
}

QString OAIExportStatus::getXNextToken() const {
    return m_x_next_token;
}
void OAIExportStatus::setXNextToken(const QString &x_next_token) {
    m_x_next_token = x_next_token;
    m_x_next_token_isSet = true;
}

bool OAIExportStatus::is_x_next_token_Set() const{
    return m_x_next_token_isSet;
}

bool OAIExportStatus::is_x_next_token_Valid() const{
    return m_x_next_token_isValid;
}

bool OAIExportStatus::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_checksum_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_x_next_token_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIExportStatus::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_status_isValid && true;
}

} // namespace OpenAPI
