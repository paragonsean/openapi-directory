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

#include "OAIScoutingObservation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIScoutingObservation::OAIScoutingObservation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIScoutingObservation::OAIScoutingObservation() {
    this->initializeModel();
}

OAIScoutingObservation::~OAIScoutingObservation() {}

void OAIScoutingObservation::initializeModel() {

    m_end_time_isSet = false;
    m_end_time_isValid = false;

    m_field_ids_isSet = false;
    m_field_ids_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_location_display_color_isSet = false;
    m_location_display_color_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_start_time_isSet = false;
    m_start_time_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_timespan_isSet = false;
    m_timespan_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAIScoutingObservation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIScoutingObservation::fromJsonObject(QJsonObject json) {

    m_end_time_isValid = ::OpenAPI::fromJsonValue(m_end_time, json[QString("endTime")]);
    m_end_time_isSet = !json[QString("endTime")].isNull() && m_end_time_isValid;

    m_field_ids_isValid = ::OpenAPI::fromJsonValue(m_field_ids, json[QString("fieldIds")]);
    m_field_ids_isSet = !json[QString("fieldIds")].isNull() && m_field_ids_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_location_display_color_isValid = ::OpenAPI::fromJsonValue(m_location_display_color, json[QString("locationDisplayColor")]);
    m_location_display_color_isSet = !json[QString("locationDisplayColor")].isNull() && m_location_display_color_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_start_time_isValid = ::OpenAPI::fromJsonValue(m_start_time, json[QString("startTime")]);
    m_start_time_isSet = !json[QString("startTime")].isNull() && m_start_time_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_timespan_isValid = ::OpenAPI::fromJsonValue(m_timespan, json[QString("timespan")]);
    m_timespan_isSet = !json[QString("timespan")].isNull() && m_timespan_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updatedAt")]);
    m_updated_at_isSet = !json[QString("updatedAt")].isNull() && m_updated_at_isValid;
}

QString OAIScoutingObservation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIScoutingObservation::asJsonObject() const {
    QJsonObject obj;
    if (m_end_time_isSet) {
        obj.insert(QString("endTime"), ::OpenAPI::toJsonValue(m_end_time));
    }
    if (m_field_ids.size() > 0) {
        obj.insert(QString("fieldIds"), ::OpenAPI::toJsonValue(m_field_ids));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_location.isSet()) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_location_display_color_isSet) {
        obj.insert(QString("locationDisplayColor"), ::OpenAPI::toJsonValue(m_location_display_color));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_start_time_isSet) {
        obj.insert(QString("startTime"), ::OpenAPI::toJsonValue(m_start_time));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_timespan_isSet) {
        obj.insert(QString("timespan"), ::OpenAPI::toJsonValue(m_timespan));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updatedAt"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

QDateTime OAIScoutingObservation::getEndTime() const {
    return m_end_time;
}
void OAIScoutingObservation::setEndTime(const QDateTime &end_time) {
    m_end_time = end_time;
    m_end_time_isSet = true;
}

bool OAIScoutingObservation::is_end_time_Set() const{
    return m_end_time_isSet;
}

bool OAIScoutingObservation::is_end_time_Valid() const{
    return m_end_time_isValid;
}

QList<QString> OAIScoutingObservation::getFieldIds() const {
    return m_field_ids;
}
void OAIScoutingObservation::setFieldIds(const QList<QString> &field_ids) {
    m_field_ids = field_ids;
    m_field_ids_isSet = true;
}

bool OAIScoutingObservation::is_field_ids_Set() const{
    return m_field_ids_isSet;
}

bool OAIScoutingObservation::is_field_ids_Valid() const{
    return m_field_ids_isValid;
}

QString OAIScoutingObservation::getId() const {
    return m_id;
}
void OAIScoutingObservation::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIScoutingObservation::is_id_Set() const{
    return m_id_isSet;
}

bool OAIScoutingObservation::is_id_Valid() const{
    return m_id_isValid;
}

OAIGeometry OAIScoutingObservation::getLocation() const {
    return m_location;
}
void OAIScoutingObservation::setLocation(const OAIGeometry &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAIScoutingObservation::is_location_Set() const{
    return m_location_isSet;
}

bool OAIScoutingObservation::is_location_Valid() const{
    return m_location_isValid;
}

QString OAIScoutingObservation::getLocationDisplayColor() const {
    return m_location_display_color;
}
void OAIScoutingObservation::setLocationDisplayColor(const QString &location_display_color) {
    m_location_display_color = location_display_color;
    m_location_display_color_isSet = true;
}

bool OAIScoutingObservation::is_location_display_color_Set() const{
    return m_location_display_color_isSet;
}

bool OAIScoutingObservation::is_location_display_color_Valid() const{
    return m_location_display_color_isValid;
}

QString OAIScoutingObservation::getNote() const {
    return m_note;
}
void OAIScoutingObservation::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAIScoutingObservation::is_note_Set() const{
    return m_note_isSet;
}

bool OAIScoutingObservation::is_note_Valid() const{
    return m_note_isValid;
}

QDateTime OAIScoutingObservation::getStartTime() const {
    return m_start_time;
}
void OAIScoutingObservation::setStartTime(const QDateTime &start_time) {
    m_start_time = start_time;
    m_start_time_isSet = true;
}

bool OAIScoutingObservation::is_start_time_Set() const{
    return m_start_time_isSet;
}

bool OAIScoutingObservation::is_start_time_Valid() const{
    return m_start_time_isValid;
}

QString OAIScoutingObservation::getStatus() const {
    return m_status;
}
void OAIScoutingObservation::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIScoutingObservation::is_status_Set() const{
    return m_status_isSet;
}

bool OAIScoutingObservation::is_status_Valid() const{
    return m_status_isValid;
}

QList<OAIScoutingTag> OAIScoutingObservation::getTags() const {
    return m_tags;
}
void OAIScoutingObservation::setTags(const QList<OAIScoutingTag> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIScoutingObservation::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIScoutingObservation::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIScoutingObservation::getTimespan() const {
    return m_timespan;
}
void OAIScoutingObservation::setTimespan(const QString &timespan) {
    m_timespan = timespan;
    m_timespan_isSet = true;
}

bool OAIScoutingObservation::is_timespan_Set() const{
    return m_timespan_isSet;
}

bool OAIScoutingObservation::is_timespan_Valid() const{
    return m_timespan_isValid;
}

QString OAIScoutingObservation::getTitle() const {
    return m_title;
}
void OAIScoutingObservation::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIScoutingObservation::is_title_Set() const{
    return m_title_isSet;
}

bool OAIScoutingObservation::is_title_Valid() const{
    return m_title_isValid;
}

QDateTime OAIScoutingObservation::getUpdatedAt() const {
    return m_updated_at;
}
void OAIScoutingObservation::setUpdatedAt(const QDateTime &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIScoutingObservation::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIScoutingObservation::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIScoutingObservation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_end_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_field_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_display_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_timespan_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIScoutingObservation::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_end_time_isValid && m_field_ids_isValid && m_id_isValid && m_location_isValid && m_location_display_color_isValid && m_note_isValid && m_start_time_isValid && m_status_isValid && m_tags_isValid && m_timespan_isValid && m_title_isValid && m_updated_at_isValid && true;
}

} // namespace OpenAPI
