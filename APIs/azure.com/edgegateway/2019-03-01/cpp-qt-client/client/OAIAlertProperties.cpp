/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAlertProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAlertProperties::OAIAlertProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAlertProperties::OAIAlertProperties() {
    this->initializeModel();
}

OAIAlertProperties::~OAIAlertProperties() {}

void OAIAlertProperties::initializeModel() {

    m_alert_type_isSet = false;
    m_alert_type_isValid = false;

    m_appeared_at_date_time_isSet = false;
    m_appeared_at_date_time_isValid = false;

    m_detailed_information_isSet = false;
    m_detailed_information_isValid = false;

    m_error_details_isSet = false;
    m_error_details_isValid = false;

    m_recommendation_isSet = false;
    m_recommendation_isValid = false;

    m_severity_isSet = false;
    m_severity_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;
}

void OAIAlertProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAlertProperties::fromJsonObject(QJsonObject json) {

    m_alert_type_isValid = ::OpenAPI::fromJsonValue(m_alert_type, json[QString("alertType")]);
    m_alert_type_isSet = !json[QString("alertType")].isNull() && m_alert_type_isValid;

    m_appeared_at_date_time_isValid = ::OpenAPI::fromJsonValue(m_appeared_at_date_time, json[QString("appearedAtDateTime")]);
    m_appeared_at_date_time_isSet = !json[QString("appearedAtDateTime")].isNull() && m_appeared_at_date_time_isValid;

    m_detailed_information_isValid = ::OpenAPI::fromJsonValue(m_detailed_information, json[QString("detailedInformation")]);
    m_detailed_information_isSet = !json[QString("detailedInformation")].isNull() && m_detailed_information_isValid;

    m_error_details_isValid = ::OpenAPI::fromJsonValue(m_error_details, json[QString("errorDetails")]);
    m_error_details_isSet = !json[QString("errorDetails")].isNull() && m_error_details_isValid;

    m_recommendation_isValid = ::OpenAPI::fromJsonValue(m_recommendation, json[QString("recommendation")]);
    m_recommendation_isSet = !json[QString("recommendation")].isNull() && m_recommendation_isValid;

    m_severity_isValid = ::OpenAPI::fromJsonValue(m_severity, json[QString("severity")]);
    m_severity_isSet = !json[QString("severity")].isNull() && m_severity_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;
}

QString OAIAlertProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAlertProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_alert_type_isSet) {
        obj.insert(QString("alertType"), ::OpenAPI::toJsonValue(m_alert_type));
    }
    if (m_appeared_at_date_time_isSet) {
        obj.insert(QString("appearedAtDateTime"), ::OpenAPI::toJsonValue(m_appeared_at_date_time));
    }
    if (m_detailed_information.size() > 0) {
        obj.insert(QString("detailedInformation"), ::OpenAPI::toJsonValue(m_detailed_information));
    }
    if (m_error_details.isSet()) {
        obj.insert(QString("errorDetails"), ::OpenAPI::toJsonValue(m_error_details));
    }
    if (m_recommendation_isSet) {
        obj.insert(QString("recommendation"), ::OpenAPI::toJsonValue(m_recommendation));
    }
    if (m_severity_isSet) {
        obj.insert(QString("severity"), ::OpenAPI::toJsonValue(m_severity));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    return obj;
}

QString OAIAlertProperties::getAlertType() const {
    return m_alert_type;
}
void OAIAlertProperties::setAlertType(const QString &alert_type) {
    m_alert_type = alert_type;
    m_alert_type_isSet = true;
}

bool OAIAlertProperties::is_alert_type_Set() const{
    return m_alert_type_isSet;
}

bool OAIAlertProperties::is_alert_type_Valid() const{
    return m_alert_type_isValid;
}

QDateTime OAIAlertProperties::getAppearedAtDateTime() const {
    return m_appeared_at_date_time;
}
void OAIAlertProperties::setAppearedAtDateTime(const QDateTime &appeared_at_date_time) {
    m_appeared_at_date_time = appeared_at_date_time;
    m_appeared_at_date_time_isSet = true;
}

bool OAIAlertProperties::is_appeared_at_date_time_Set() const{
    return m_appeared_at_date_time_isSet;
}

bool OAIAlertProperties::is_appeared_at_date_time_Valid() const{
    return m_appeared_at_date_time_isValid;
}

QMap<QString, QString> OAIAlertProperties::getDetailedInformation() const {
    return m_detailed_information;
}
void OAIAlertProperties::setDetailedInformation(const QMap<QString, QString> &detailed_information) {
    m_detailed_information = detailed_information;
    m_detailed_information_isSet = true;
}

bool OAIAlertProperties::is_detailed_information_Set() const{
    return m_detailed_information_isSet;
}

bool OAIAlertProperties::is_detailed_information_Valid() const{
    return m_detailed_information_isValid;
}

OAIAlertErrorDetails OAIAlertProperties::getErrorDetails() const {
    return m_error_details;
}
void OAIAlertProperties::setErrorDetails(const OAIAlertErrorDetails &error_details) {
    m_error_details = error_details;
    m_error_details_isSet = true;
}

bool OAIAlertProperties::is_error_details_Set() const{
    return m_error_details_isSet;
}

bool OAIAlertProperties::is_error_details_Valid() const{
    return m_error_details_isValid;
}

QString OAIAlertProperties::getRecommendation() const {
    return m_recommendation;
}
void OAIAlertProperties::setRecommendation(const QString &recommendation) {
    m_recommendation = recommendation;
    m_recommendation_isSet = true;
}

bool OAIAlertProperties::is_recommendation_Set() const{
    return m_recommendation_isSet;
}

bool OAIAlertProperties::is_recommendation_Valid() const{
    return m_recommendation_isValid;
}

QString OAIAlertProperties::getSeverity() const {
    return m_severity;
}
void OAIAlertProperties::setSeverity(const QString &severity) {
    m_severity = severity;
    m_severity_isSet = true;
}

bool OAIAlertProperties::is_severity_Set() const{
    return m_severity_isSet;
}

bool OAIAlertProperties::is_severity_Valid() const{
    return m_severity_isValid;
}

QString OAIAlertProperties::getTitle() const {
    return m_title;
}
void OAIAlertProperties::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIAlertProperties::is_title_Set() const{
    return m_title_isSet;
}

bool OAIAlertProperties::is_title_Valid() const{
    return m_title_isValid;
}

bool OAIAlertProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_alert_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_appeared_at_date_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_detailed_information.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_error_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_recommendation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_severity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAlertProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
