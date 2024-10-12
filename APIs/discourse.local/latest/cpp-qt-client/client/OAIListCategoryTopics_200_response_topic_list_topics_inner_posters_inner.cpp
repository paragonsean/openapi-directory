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

#include "OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner() {
    this->initializeModel();
}

OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::~OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner() {}

void OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_extras_isSet = false;
    m_extras_isValid = false;

    m_primary_group_id_isSet = false;
    m_primary_group_id_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_extras_isValid = ::OpenAPI::fromJsonValue(m_extras, json[QString("extras")]);
    m_extras_isSet = !json[QString("extras")].isNull() && m_extras_isValid;

    m_primary_group_id_isValid = ::OpenAPI::fromJsonValue(m_primary_group_id, json[QString("primary_group_id")]);
    m_primary_group_id_isSet = !json[QString("primary_group_id")].isNull() && m_primary_group_id_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;
}

QString OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_extras_isSet) {
        obj.insert(QString("extras"), ::OpenAPI::toJsonValue(m_extras));
    }
    if (m_primary_group_id_isSet) {
        obj.insert(QString("primary_group_id"), ::OpenAPI::toJsonValue(m_primary_group_id));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QString OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::getDescription() const {
    return m_description;
}
void OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::getExtras() const {
    return m_extras;
}
void OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::setExtras(const QString &extras) {
    m_extras = extras;
    m_extras_isSet = true;
}

bool OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::is_extras_Set() const{
    return m_extras_isSet;
}

bool OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::is_extras_Valid() const{
    return m_extras_isValid;
}

QString OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::getPrimaryGroupId() const {
    return m_primary_group_id;
}
void OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::setPrimaryGroupId(const QString &primary_group_id) {
    m_primary_group_id = primary_group_id;
    m_primary_group_id_isSet = true;
}

bool OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::is_primary_group_id_Set() const{
    return m_primary_group_id_isSet;
}

bool OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::is_primary_group_id_Valid() const{
    return m_primary_group_id_isValid;
}

qint32 OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::getUserId() const {
    return m_user_id;
}
void OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::setUserId(const qint32 &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extras_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_group_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIListCategoryTopics_200_response_topic_list_topics_inner_posters_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_description_isValid && m_extras_isValid && m_primary_group_id_isValid && m_user_id_isValid && true;
}

} // namespace OpenAPI
