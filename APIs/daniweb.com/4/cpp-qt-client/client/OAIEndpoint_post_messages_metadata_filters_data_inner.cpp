/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEndpoint_post_messages_metadata_filters_data_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEndpoint_post_messages_metadata_filters_data_inner::OAIEndpoint_post_messages_metadata_filters_data_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEndpoint_post_messages_metadata_filters_data_inner::OAIEndpoint_post_messages_metadata_filters_data_inner() {
    this->initializeModel();
}

OAIEndpoint_post_messages_metadata_filters_data_inner::~OAIEndpoint_post_messages_metadata_filters_data_inner() {}

void OAIEndpoint_post_messages_metadata_filters_data_inner::initializeModel() {

    m_matched_metadata_isSet = false;
    m_matched_metadata_isValid = false;

    m_message_isSet = false;
    m_message_isValid = false;
}

void OAIEndpoint_post_messages_metadata_filters_data_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEndpoint_post_messages_metadata_filters_data_inner::fromJsonObject(QJsonObject json) {

    if(json["matched_metadata"].isObject()){
        auto varmap = json["matched_metadata"].toObject().toVariantMap();
        m_matched_metadata_isValid = true;
        if(varmap.count() > 0){
            for(auto val : varmap.keys()){
                QList<QString> item;
                auto jval = QJsonValue::fromVariant(varmap.value(val));
                m_matched_metadata_isValid &= ::OpenAPI::fromJsonValue(item, jval);
                m_matched_metadata_isSet &= !jval.isNull() && m_matched_metadata_isValid;
                m_matched_metadata.insert(m_matched_metadata.end(), val, item);
            }
        }
    }

    m_message_isValid = ::OpenAPI::fromJsonValue(m_message, json[QString("message")]);
    m_message_isSet = !json[QString("message")].isNull() && m_message_isValid;
}

QString OAIEndpoint_post_messages_metadata_filters_data_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEndpoint_post_messages_metadata_filters_data_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_matched_metadata.size() > 0) {
        
        obj.insert(QString("matched_metadata"), toJsonValue(m_matched_metadata));
    }
    if (m_message.isSet()) {
        obj.insert(QString("message"), ::OpenAPI::toJsonValue(m_message));
    }
    return obj;
}

QMap<QString, QList<QString>> OAIEndpoint_post_messages_metadata_filters_data_inner::getMatchedMetadata() const {
    return m_matched_metadata;
}
void OAIEndpoint_post_messages_metadata_filters_data_inner::setMatchedMetadata(const QMap<QString, QList<QString>> &matched_metadata) {
    m_matched_metadata = matched_metadata;
    m_matched_metadata_isSet = true;
}

bool OAIEndpoint_post_messages_metadata_filters_data_inner::is_matched_metadata_Set() const{
    return m_matched_metadata_isSet;
}

bool OAIEndpoint_post_messages_metadata_filters_data_inner::is_matched_metadata_Valid() const{
    return m_matched_metadata_isValid;
}

OAIMessage OAIEndpoint_post_messages_metadata_filters_data_inner::getMessage() const {
    return m_message;
}
void OAIEndpoint_post_messages_metadata_filters_data_inner::setMessage(const OAIMessage &message) {
    m_message = message;
    m_message_isSet = true;
}

bool OAIEndpoint_post_messages_metadata_filters_data_inner::is_message_Set() const{
    return m_message_isSet;
}

bool OAIEndpoint_post_messages_metadata_filters_data_inner::is_message_Valid() const{
    return m_message_isValid;
}

bool OAIEndpoint_post_messages_metadata_filters_data_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_matched_metadata.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_message.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEndpoint_post_messages_metadata_filters_data_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
