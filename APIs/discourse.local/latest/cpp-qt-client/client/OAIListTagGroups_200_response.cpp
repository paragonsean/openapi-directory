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

#include "OAIListTagGroups_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListTagGroups_200_response::OAIListTagGroups_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListTagGroups_200_response::OAIListTagGroups_200_response() {
    this->initializeModel();
}

OAIListTagGroups_200_response::~OAIListTagGroups_200_response() {}

void OAIListTagGroups_200_response::initializeModel() {

    m_tag_groups_isSet = false;
    m_tag_groups_isValid = false;
}

void OAIListTagGroups_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListTagGroups_200_response::fromJsonObject(QJsonObject json) {

    m_tag_groups_isValid = ::OpenAPI::fromJsonValue(m_tag_groups, json[QString("tag_groups")]);
    m_tag_groups_isSet = !json[QString("tag_groups")].isNull() && m_tag_groups_isValid;
}

QString OAIListTagGroups_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListTagGroups_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_tag_groups.size() > 0) {
        obj.insert(QString("tag_groups"), ::OpenAPI::toJsonValue(m_tag_groups));
    }
    return obj;
}

QList<OAIListTagGroups_200_response_tag_groups_inner> OAIListTagGroups_200_response::getTagGroups() const {
    return m_tag_groups;
}
void OAIListTagGroups_200_response::setTagGroups(const QList<OAIListTagGroups_200_response_tag_groups_inner> &tag_groups) {
    m_tag_groups = tag_groups;
    m_tag_groups_isSet = true;
}

bool OAIListTagGroups_200_response::is_tag_groups_Set() const{
    return m_tag_groups_isSet;
}

bool OAIListTagGroups_200_response::is_tag_groups_Valid() const{
    return m_tag_groups_isValid;
}

bool OAIListTagGroups_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_tag_groups.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListTagGroups_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
