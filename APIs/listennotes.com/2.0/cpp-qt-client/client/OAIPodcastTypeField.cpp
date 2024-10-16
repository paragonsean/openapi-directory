/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPodcastTypeField.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPodcastTypeField::OAIPodcastTypeField(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPodcastTypeField::OAIPodcastTypeField() {
    this->initializeModel();
}

OAIPodcastTypeField::~OAIPodcastTypeField() {}

void OAIPodcastTypeField::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIPodcastTypeField::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIPodcastTypeField::fromJson(QString jsonString) {
    
    if ( jsonString.compare("episodic", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPodcastTypeField::EPISODIC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("serial", Qt::CaseInsensitive) == 0) {
        m_value = eOAIPodcastTypeField::SERIAL;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIPodcastTypeField::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIPodcastTypeField::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIPodcastTypeField::EPISODIC:
            val = "episodic";
            break;
        case eOAIPodcastTypeField::SERIAL:
            val = "serial";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIPodcastTypeField::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIPodcastTypeField::eOAIPodcastTypeField OAIPodcastTypeField::getValue() const {
    return m_value;
}

void OAIPodcastTypeField::setValue(const OAIPodcastTypeField::eOAIPodcastTypeField& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIPodcastTypeField::isSet() const {
    
    return m_value_isSet;
}

bool OAIPodcastTypeField::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
