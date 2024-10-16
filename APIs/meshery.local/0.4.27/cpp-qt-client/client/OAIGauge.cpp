/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGauge.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGauge::OAIGauge(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGauge::OAIGauge() {
    this->initializeModel();
}

OAIGauge::~OAIGauge() {}

void OAIGauge::initializeModel() {

    m_max_value_isSet = false;
    m_max_value_isValid = false;

    m_min_value_isSet = false;
    m_min_value_isValid = false;

    m_show_isSet = false;
    m_show_isValid = false;

    m_threshold_labels_isSet = false;
    m_threshold_labels_isValid = false;

    m_threshold_markers_isSet = false;
    m_threshold_markers_isValid = false;
}

void OAIGauge::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGauge::fromJsonObject(QJsonObject json) {

    m_max_value_isValid = ::OpenAPI::fromJsonValue(m_max_value, json[QString("maxValue")]);
    m_max_value_isSet = !json[QString("maxValue")].isNull() && m_max_value_isValid;

    m_min_value_isValid = ::OpenAPI::fromJsonValue(m_min_value, json[QString("minValue")]);
    m_min_value_isSet = !json[QString("minValue")].isNull() && m_min_value_isValid;

    m_show_isValid = ::OpenAPI::fromJsonValue(m_show, json[QString("show")]);
    m_show_isSet = !json[QString("show")].isNull() && m_show_isValid;

    m_threshold_labels_isValid = ::OpenAPI::fromJsonValue(m_threshold_labels, json[QString("thresholdLabels")]);
    m_threshold_labels_isSet = !json[QString("thresholdLabels")].isNull() && m_threshold_labels_isValid;

    m_threshold_markers_isValid = ::OpenAPI::fromJsonValue(m_threshold_markers, json[QString("thresholdMarkers")]);
    m_threshold_markers_isSet = !json[QString("thresholdMarkers")].isNull() && m_threshold_markers_isValid;
}

QString OAIGauge::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGauge::asJsonObject() const {
    QJsonObject obj;
    if (m_max_value_isSet) {
        obj.insert(QString("maxValue"), ::OpenAPI::toJsonValue(m_max_value));
    }
    if (m_min_value_isSet) {
        obj.insert(QString("minValue"), ::OpenAPI::toJsonValue(m_min_value));
    }
    if (m_show_isSet) {
        obj.insert(QString("show"), ::OpenAPI::toJsonValue(m_show));
    }
    if (m_threshold_labels_isSet) {
        obj.insert(QString("thresholdLabels"), ::OpenAPI::toJsonValue(m_threshold_labels));
    }
    if (m_threshold_markers_isSet) {
        obj.insert(QString("thresholdMarkers"), ::OpenAPI::toJsonValue(m_threshold_markers));
    }
    return obj;
}

float OAIGauge::getMaxValue() const {
    return m_max_value;
}
void OAIGauge::setMaxValue(const float &max_value) {
    m_max_value = max_value;
    m_max_value_isSet = true;
}

bool OAIGauge::is_max_value_Set() const{
    return m_max_value_isSet;
}

bool OAIGauge::is_max_value_Valid() const{
    return m_max_value_isValid;
}

float OAIGauge::getMinValue() const {
    return m_min_value;
}
void OAIGauge::setMinValue(const float &min_value) {
    m_min_value = min_value;
    m_min_value_isSet = true;
}

bool OAIGauge::is_min_value_Set() const{
    return m_min_value_isSet;
}

bool OAIGauge::is_min_value_Valid() const{
    return m_min_value_isValid;
}

bool OAIGauge::isShow() const {
    return m_show;
}
void OAIGauge::setShow(const bool &show) {
    m_show = show;
    m_show_isSet = true;
}

bool OAIGauge::is_show_Set() const{
    return m_show_isSet;
}

bool OAIGauge::is_show_Valid() const{
    return m_show_isValid;
}

bool OAIGauge::isThresholdLabels() const {
    return m_threshold_labels;
}
void OAIGauge::setThresholdLabels(const bool &threshold_labels) {
    m_threshold_labels = threshold_labels;
    m_threshold_labels_isSet = true;
}

bool OAIGauge::is_threshold_labels_Set() const{
    return m_threshold_labels_isSet;
}

bool OAIGauge::is_threshold_labels_Valid() const{
    return m_threshold_labels_isValid;
}

bool OAIGauge::isThresholdMarkers() const {
    return m_threshold_markers;
}
void OAIGauge::setThresholdMarkers(const bool &threshold_markers) {
    m_threshold_markers = threshold_markers;
    m_threshold_markers_isSet = true;
}

bool OAIGauge::is_threshold_markers_Set() const{
    return m_threshold_markers_isSet;
}

bool OAIGauge::is_threshold_markers_Valid() const{
    return m_threshold_markers_isValid;
}

bool OAIGauge::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_max_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_show_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_threshold_labels_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_threshold_markers_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGauge::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
