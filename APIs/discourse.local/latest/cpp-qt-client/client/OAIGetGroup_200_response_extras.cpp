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

#include "OAIGetGroup_200_response_extras.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetGroup_200_response_extras::OAIGetGroup_200_response_extras(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetGroup_200_response_extras::OAIGetGroup_200_response_extras() {
    this->initializeModel();
}

OAIGetGroup_200_response_extras::~OAIGetGroup_200_response_extras() {}

void OAIGetGroup_200_response_extras::initializeModel() {

    m_visible_group_names_isSet = false;
    m_visible_group_names_isValid = false;
}

void OAIGetGroup_200_response_extras::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetGroup_200_response_extras::fromJsonObject(QJsonObject json) {

    m_visible_group_names_isValid = ::OpenAPI::fromJsonValue(m_visible_group_names, json[QString("visible_group_names")]);
    m_visible_group_names_isSet = !json[QString("visible_group_names")].isNull() && m_visible_group_names_isValid;
}

QString OAIGetGroup_200_response_extras::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetGroup_200_response_extras::asJsonObject() const {
    QJsonObject obj;
    if (m_visible_group_names.size() > 0) {
        obj.insert(QString("visible_group_names"), ::OpenAPI::toJsonValue(m_visible_group_names));
    }
    return obj;
}

QList<QJsonValue> OAIGetGroup_200_response_extras::getVisibleGroupNames() const {
    return m_visible_group_names;
}
void OAIGetGroup_200_response_extras::setVisibleGroupNames(const QList<QJsonValue> &visible_group_names) {
    m_visible_group_names = visible_group_names;
    m_visible_group_names_isSet = true;
}

bool OAIGetGroup_200_response_extras::is_visible_group_names_Set() const{
    return m_visible_group_names_isSet;
}

bool OAIGetGroup_200_response_extras::is_visible_group_names_Valid() const{
    return m_visible_group_names_isValid;
}

bool OAIGetGroup_200_response_extras::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_visible_group_names.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetGroup_200_response_extras::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_visible_group_names_isValid && true;
}

} // namespace OpenAPI
