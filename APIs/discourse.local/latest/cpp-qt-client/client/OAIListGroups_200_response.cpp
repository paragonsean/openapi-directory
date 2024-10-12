/**
 * Discourse API Documentation
 * This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 
 *
 * The version of the OpenAPI document: latest
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIListGroups_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListGroups_200_response::OAIListGroups_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListGroups_200_response::OAIListGroups_200_response() {
    this->initializeModel();
}

OAIListGroups_200_response::~OAIListGroups_200_response() {}

void OAIListGroups_200_response::initializeModel() {

    m_extras_isSet = false;
    m_extras_isValid = false;

    m_groups_isSet = false;
    m_groups_isValid = false;

    m_load_more_groups_isSet = false;
    m_load_more_groups_isValid = false;

    m_total_rows_groups_isSet = false;
    m_total_rows_groups_isValid = false;
}

void OAIListGroups_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListGroups_200_response::fromJsonObject(QJsonObject json) {

    m_extras_isValid = ::OpenAPI::fromJsonValue(m_extras, json[QString("extras")]);
    m_extras_isSet = !json[QString("extras")].isNull() && m_extras_isValid;

    m_groups_isValid = ::OpenAPI::fromJsonValue(m_groups, json[QString("groups")]);
    m_groups_isSet = !json[QString("groups")].isNull() && m_groups_isValid;

    m_load_more_groups_isValid = ::OpenAPI::fromJsonValue(m_load_more_groups, json[QString("load_more_groups")]);
    m_load_more_groups_isSet = !json[QString("load_more_groups")].isNull() && m_load_more_groups_isValid;

    m_total_rows_groups_isValid = ::OpenAPI::fromJsonValue(m_total_rows_groups, json[QString("total_rows_groups")]);
    m_total_rows_groups_isSet = !json[QString("total_rows_groups")].isNull() && m_total_rows_groups_isValid;
}

QString OAIListGroups_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListGroups_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_extras.isSet()) {
        obj.insert(QString("extras"), ::OpenAPI::toJsonValue(m_extras));
    }
    if (m_groups.size() > 0) {
        obj.insert(QString("groups"), ::OpenAPI::toJsonValue(m_groups));
    }
    if (m_load_more_groups_isSet) {
        obj.insert(QString("load_more_groups"), ::OpenAPI::toJsonValue(m_load_more_groups));
    }
    if (m_total_rows_groups_isSet) {
        obj.insert(QString("total_rows_groups"), ::OpenAPI::toJsonValue(m_total_rows_groups));
    }
    return obj;
}

OAIListGroups_200_response_extras OAIListGroups_200_response::getExtras() const {
    return m_extras;
}
void OAIListGroups_200_response::setExtras(const OAIListGroups_200_response_extras &extras) {
    m_extras = extras;
    m_extras_isSet = true;
}

bool OAIListGroups_200_response::is_extras_Set() const{
    return m_extras_isSet;
}

bool OAIListGroups_200_response::is_extras_Valid() const{
    return m_extras_isValid;
}

QList<OAIListGroups_200_response_groups_inner> OAIListGroups_200_response::getGroups() const {
    return m_groups;
}
void OAIListGroups_200_response::setGroups(const QList<OAIListGroups_200_response_groups_inner> &groups) {
    m_groups = groups;
    m_groups_isSet = true;
}

bool OAIListGroups_200_response::is_groups_Set() const{
    return m_groups_isSet;
}

bool OAIListGroups_200_response::is_groups_Valid() const{
    return m_groups_isValid;
}

QString OAIListGroups_200_response::getLoadMoreGroups() const {
    return m_load_more_groups;
}
void OAIListGroups_200_response::setLoadMoreGroups(const QString &load_more_groups) {
    m_load_more_groups = load_more_groups;
    m_load_more_groups_isSet = true;
}

bool OAIListGroups_200_response::is_load_more_groups_Set() const{
    return m_load_more_groups_isSet;
}

bool OAIListGroups_200_response::is_load_more_groups_Valid() const{
    return m_load_more_groups_isValid;
}

qint32 OAIListGroups_200_response::getTotalRowsGroups() const {
    return m_total_rows_groups;
}
void OAIListGroups_200_response::setTotalRowsGroups(const qint32 &total_rows_groups) {
    m_total_rows_groups = total_rows_groups;
    m_total_rows_groups_isSet = true;
}

bool OAIListGroups_200_response::is_total_rows_groups_Set() const{
    return m_total_rows_groups_isSet;
}

bool OAIListGroups_200_response::is_total_rows_groups_Valid() const{
    return m_total_rows_groups_isValid;
}

bool OAIListGroups_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_extras.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_groups.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_load_more_groups_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_rows_groups_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListGroups_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_extras_isValid && m_groups_isValid && m_load_more_groups_isValid && m_total_rows_groups_isValid && true;
}

} // namespace OpenAPI
