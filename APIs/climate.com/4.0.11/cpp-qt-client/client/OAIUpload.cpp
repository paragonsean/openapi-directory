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

#include "OAIUpload.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpload::OAIUpload(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpload::OAIUpload() {
    this->initializeModel();
}

OAIUpload::~OAIUpload() {}

void OAIUpload::initializeModel() {

    m_content_type_isSet = false;
    m_content_type_isValid = false;

    m_length_isSet = false;
    m_length_isValid = false;

    m_md5_isSet = false;
    m_md5_isValid = false;

    m_metadata_isSet = false;
    m_metadata_isValid = false;
}

void OAIUpload::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpload::fromJsonObject(QJsonObject json) {

    m_content_type_isValid = ::OpenAPI::fromJsonValue(m_content_type, json[QString("contentType")]);
    m_content_type_isSet = !json[QString("contentType")].isNull() && m_content_type_isValid;

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("length")]);
    m_length_isSet = !json[QString("length")].isNull() && m_length_isValid;

    m_md5_isValid = ::OpenAPI::fromJsonValue(m_md5, json[QString("md5")]);
    m_md5_isSet = !json[QString("md5")].isNull() && m_md5_isValid;

    m_metadata_isValid = ::OpenAPI::fromJsonValue(m_metadata, json[QString("metadata")]);
    m_metadata_isSet = !json[QString("metadata")].isNull() && m_metadata_isValid;
}

QString OAIUpload::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpload::asJsonObject() const {
    QJsonObject obj;
    if (m_content_type_isSet) {
        obj.insert(QString("contentType"), ::OpenAPI::toJsonValue(m_content_type));
    }
    if (m_length_isSet) {
        obj.insert(QString("length"), ::OpenAPI::toJsonValue(m_length));
    }
    if (m_md5_isSet) {
        obj.insert(QString("md5"), ::OpenAPI::toJsonValue(m_md5));
    }
    if (m_metadata.size() > 0) {
        obj.insert(QString("metadata"), ::OpenAPI::toJsonValue(m_metadata));
    }
    return obj;
}

QString OAIUpload::getContentType() const {
    return m_content_type;
}
void OAIUpload::setContentType(const QString &content_type) {
    m_content_type = content_type;
    m_content_type_isSet = true;
}

bool OAIUpload::is_content_type_Set() const{
    return m_content_type_isSet;
}

bool OAIUpload::is_content_type_Valid() const{
    return m_content_type_isValid;
}

qint64 OAIUpload::getLength() const {
    return m_length;
}
void OAIUpload::setLength(const qint64 &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAIUpload::is_length_Set() const{
    return m_length_isSet;
}

bool OAIUpload::is_length_Valid() const{
    return m_length_isValid;
}

QString OAIUpload::getMd5() const {
    return m_md5;
}
void OAIUpload::setMd5(const QString &md5) {
    m_md5 = md5;
    m_md5_isSet = true;
}

bool OAIUpload::is_md5_Set() const{
    return m_md5_isSet;
}

bool OAIUpload::is_md5_Valid() const{
    return m_md5_isValid;
}

QMap<QString, QJsonValue> OAIUpload::getMetadata() const {
    return m_metadata;
}
void OAIUpload::setMetadata(const QMap<QString, QJsonValue> &metadata) {
    m_metadata = metadata;
    m_metadata_isSet = true;
}

bool OAIUpload::is_metadata_Set() const{
    return m_metadata_isSet;
}

bool OAIUpload::is_metadata_Valid() const{
    return m_metadata_isValid;
}

bool OAIUpload::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_content_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_md5_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_metadata.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpload::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_content_type_isValid && m_length_isValid && m_md5_isValid && true;
}

} // namespace OpenAPI
