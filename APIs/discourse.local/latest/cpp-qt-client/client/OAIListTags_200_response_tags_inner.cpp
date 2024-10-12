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

#include "OAIListTags_200_response_tags_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListTags_200_response_tags_inner::OAIListTags_200_response_tags_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListTags_200_response_tags_inner::OAIListTags_200_response_tags_inner() {
    this->initializeModel();
}

OAIListTags_200_response_tags_inner::~OAIListTags_200_response_tags_inner() {}

void OAIListTags_200_response_tags_inner::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_pm_count_isSet = false;
    m_pm_count_isValid = false;

    m_target_tag_isSet = false;
    m_target_tag_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;
}

void OAIListTags_200_response_tags_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListTags_200_response_tags_inner::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_pm_count_isValid = ::OpenAPI::fromJsonValue(m_pm_count, json[QString("pm_count")]);
    m_pm_count_isSet = !json[QString("pm_count")].isNull() && m_pm_count_isValid;

    m_target_tag_isValid = ::OpenAPI::fromJsonValue(m_target_tag, json[QString("target_tag")]);
    m_target_tag_isSet = !json[QString("target_tag")].isNull() && m_target_tag_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;
}

QString OAIListTags_200_response_tags_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListTags_200_response_tags_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_pm_count_isSet) {
        obj.insert(QString("pm_count"), ::OpenAPI::toJsonValue(m_pm_count));
    }
    if (m_target_tag_isSet) {
        obj.insert(QString("target_tag"), ::OpenAPI::toJsonValue(m_target_tag));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    return obj;
}

qint32 OAIListTags_200_response_tags_inner::getCount() const {
    return m_count;
}
void OAIListTags_200_response_tags_inner::setCount(const qint32 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIListTags_200_response_tags_inner::is_count_Set() const{
    return m_count_isSet;
}

bool OAIListTags_200_response_tags_inner::is_count_Valid() const{
    return m_count_isValid;
}

QString OAIListTags_200_response_tags_inner::getId() const {
    return m_id;
}
void OAIListTags_200_response_tags_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIListTags_200_response_tags_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIListTags_200_response_tags_inner::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIListTags_200_response_tags_inner::getPmCount() const {
    return m_pm_count;
}
void OAIListTags_200_response_tags_inner::setPmCount(const qint32 &pm_count) {
    m_pm_count = pm_count;
    m_pm_count_isSet = true;
}

bool OAIListTags_200_response_tags_inner::is_pm_count_Set() const{
    return m_pm_count_isSet;
}

bool OAIListTags_200_response_tags_inner::is_pm_count_Valid() const{
    return m_pm_count_isValid;
}

QString OAIListTags_200_response_tags_inner::getTargetTag() const {
    return m_target_tag;
}
void OAIListTags_200_response_tags_inner::setTargetTag(const QString &target_tag) {
    m_target_tag = target_tag;
    m_target_tag_isSet = true;
}

bool OAIListTags_200_response_tags_inner::is_target_tag_Set() const{
    return m_target_tag_isSet;
}

bool OAIListTags_200_response_tags_inner::is_target_tag_Valid() const{
    return m_target_tag_isValid;
}

QString OAIListTags_200_response_tags_inner::getText() const {
    return m_text;
}
void OAIListTags_200_response_tags_inner::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIListTags_200_response_tags_inner::is_text_Set() const{
    return m_text_isSet;
}

bool OAIListTags_200_response_tags_inner::is_text_Valid() const{
    return m_text_isValid;
}

bool OAIListTags_200_response_tags_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pm_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_target_tag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListTags_200_response_tags_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
