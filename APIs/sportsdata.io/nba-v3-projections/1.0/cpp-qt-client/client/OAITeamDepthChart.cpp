/**
 * NBA v3 Projections
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITeamDepthChart.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITeamDepthChart::OAITeamDepthChart(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITeamDepthChart::OAITeamDepthChart() {
    this->initializeModel();
}

OAITeamDepthChart::~OAITeamDepthChart() {}

void OAITeamDepthChart::initializeModel() {

    m_depth_charts_isSet = false;
    m_depth_charts_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;
}

void OAITeamDepthChart::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITeamDepthChart::fromJsonObject(QJsonObject json) {

    m_depth_charts_isValid = ::OpenAPI::fromJsonValue(m_depth_charts, json[QString("DepthCharts")]);
    m_depth_charts_isSet = !json[QString("DepthCharts")].isNull() && m_depth_charts_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("TeamID")]);
    m_team_id_isSet = !json[QString("TeamID")].isNull() && m_team_id_isValid;
}

QString OAITeamDepthChart::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITeamDepthChart::asJsonObject() const {
    QJsonObject obj;
    if (m_depth_charts.size() > 0) {
        obj.insert(QString("DepthCharts"), ::OpenAPI::toJsonValue(m_depth_charts));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("TeamID"), ::OpenAPI::toJsonValue(m_team_id));
    }
    return obj;
}

QList<OAIDepthChart> OAITeamDepthChart::getDepthCharts() const {
    return m_depth_charts;
}
void OAITeamDepthChart::setDepthCharts(const QList<OAIDepthChart> &depth_charts) {
    m_depth_charts = depth_charts;
    m_depth_charts_isSet = true;
}

bool OAITeamDepthChart::is_depth_charts_Set() const{
    return m_depth_charts_isSet;
}

bool OAITeamDepthChart::is_depth_charts_Valid() const{
    return m_depth_charts_isValid;
}

qint32 OAITeamDepthChart::getTeamId() const {
    return m_team_id;
}
void OAITeamDepthChart::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAITeamDepthChart::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAITeamDepthChart::is_team_id_Valid() const{
    return m_team_id_isValid;
}

bool OAITeamDepthChart::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_depth_charts.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITeamDepthChart::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
