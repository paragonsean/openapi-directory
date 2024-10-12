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

#include "OAIGetSite_200_response_archetypes_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetSite_200_response_archetypes_inner::OAIGetSite_200_response_archetypes_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetSite_200_response_archetypes_inner::OAIGetSite_200_response_archetypes_inner() {
    this->initializeModel();
}

OAIGetSite_200_response_archetypes_inner::~OAIGetSite_200_response_archetypes_inner() {}

void OAIGetSite_200_response_archetypes_inner::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_options_isSet = false;
    m_options_isValid = false;
}

void OAIGetSite_200_response_archetypes_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetSite_200_response_archetypes_inner::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_options_isValid = ::OpenAPI::fromJsonValue(m_options, json[QString("options")]);
    m_options_isSet = !json[QString("options")].isNull() && m_options_isValid;
}

QString OAIGetSite_200_response_archetypes_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetSite_200_response_archetypes_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_options.size() > 0) {
        obj.insert(QString("options"), ::OpenAPI::toJsonValue(m_options));
    }
    return obj;
}

QString OAIGetSite_200_response_archetypes_inner::getId() const {
    return m_id;
}
void OAIGetSite_200_response_archetypes_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIGetSite_200_response_archetypes_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIGetSite_200_response_archetypes_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIGetSite_200_response_archetypes_inner::getName() const {
    return m_name;
}
void OAIGetSite_200_response_archetypes_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIGetSite_200_response_archetypes_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIGetSite_200_response_archetypes_inner::is_name_Valid() const{
    return m_name_isValid;
}

QList<QJsonValue> OAIGetSite_200_response_archetypes_inner::getOptions() const {
    return m_options;
}
void OAIGetSite_200_response_archetypes_inner::setOptions(const QList<QJsonValue> &options) {
    m_options = options;
    m_options_isSet = true;
}

bool OAIGetSite_200_response_archetypes_inner::is_options_Set() const{
    return m_options_isSet;
}

bool OAIGetSite_200_response_archetypes_inner::is_options_Valid() const{
    return m_options_isValid;
}

bool OAIGetSite_200_response_archetypes_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_options.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetSite_200_response_archetypes_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_name_isValid && m_options_isValid && true;
}

} // namespace OpenAPI
