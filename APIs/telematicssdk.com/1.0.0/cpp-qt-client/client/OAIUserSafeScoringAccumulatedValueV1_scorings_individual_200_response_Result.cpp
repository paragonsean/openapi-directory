/**
 * Quick start - Telematics SDK
 * # Introduction We have prepared a set of APIs for quick start to integrate telematics SDK that powers mobile telematics inside 3rd party mobile applications.  * [CONTACT US](https://telematicssdk.com) * [SANDBOX](https://userdatahub.com) * [DEV.PORTAL](https://docs.telematicssdk.com) * [DEMO APP](https://raxeltelematics.com/telematics-app)   # Overview Datamotion provides telematics infrastructure for mobile applications.   Telematics SDK turns any smartphone into telematics data gathering device to collect Location, driving and behavior data. API services unlocks power of your mobile application  There are 3 groups of methods: * 1 - user management * 2 - statistics for mobile app * 3 - statistics for back-end(s)  in certain cases you will need SNS or any other notification services. read more [here](https://docs.telematicssdk.com/platform-features/sns) # Possible architecture  There are three common schemes that are used by our clients. These schemes can be combined * Collect, Process, Store (required: 1&2) * Collect, Process (required: 1& sns) * Collect (required 1&sns)   ## Collect, Process, Store ![Collect, Process, Store](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection%2C+processing%2C+storage)  ## Collect, Process ![Collect, Process](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+and+processing)  ## Collect ![Collect](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+only)  *** ![Telematic sdk](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Github/transportation_small.png)  # Common use-cases: * Safe and efficient driving * Usage-based insurance * Safe driving assessment * Driver assessment * Trip log * Geo-analysis * Accident monitoring * Driving engagements * Location based services * Realtime Tracking and beyond  # How to start * Register a [SANDBOX ACCOUNT](https://userdatahub.com) * Get [CREDENTIALS](https://docs.userdatahub.com/sandbox/credentials)  * Follow the guide from [DEVELOPER POERTAL](https://docs.telematicssdk.com)  # Authentication To create a user on datamotion platform, you require to use InstanceID and InstanceKEY. You can get it in Datahub -> management -> user-service credentials  Once you create a user, you will get Device token, JWT token and refresh token. then, you will use it for APIs
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result() {
    this->initializeModel();
}

OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::~OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result() {}

void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::initializeModel() {

    m_acceleration_score_isSet = false;
    m_acceleration_score_isValid = false;

    m_app_id_isSet = false;
    m_app_id_isValid = false;

    m_braking_score_isSet = false;
    m_braking_score_isValid = false;

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_cornering_score_isSet = false;
    m_cornering_score_isValid = false;

    m_device_token_isSet = false;
    m_device_token_isValid = false;

    m_distracted_score_isSet = false;
    m_distracted_score_isValid = false;

    m_instance_id_isSet = false;
    m_instance_id_isValid = false;

    m_overall_score_isSet = false;
    m_overall_score_isValid = false;

    m_speeding_score_isSet = false;
    m_speeding_score_isValid = false;
}

void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::fromJsonObject(QJsonObject json) {

    m_acceleration_score_isValid = ::OpenAPI::fromJsonValue(m_acceleration_score, json[QString("AccelerationScore")]);
    m_acceleration_score_isSet = !json[QString("AccelerationScore")].isNull() && m_acceleration_score_isValid;

    m_app_id_isValid = ::OpenAPI::fromJsonValue(m_app_id, json[QString("AppId")]);
    m_app_id_isSet = !json[QString("AppId")].isNull() && m_app_id_isValid;

    m_braking_score_isValid = ::OpenAPI::fromJsonValue(m_braking_score, json[QString("BrakingScore")]);
    m_braking_score_isSet = !json[QString("BrakingScore")].isNull() && m_braking_score_isValid;

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("CompanyId")]);
    m_company_id_isSet = !json[QString("CompanyId")].isNull() && m_company_id_isValid;

    m_cornering_score_isValid = ::OpenAPI::fromJsonValue(m_cornering_score, json[QString("CorneringScore")]);
    m_cornering_score_isSet = !json[QString("CorneringScore")].isNull() && m_cornering_score_isValid;

    m_device_token_isValid = ::OpenAPI::fromJsonValue(m_device_token, json[QString("DeviceToken")]);
    m_device_token_isSet = !json[QString("DeviceToken")].isNull() && m_device_token_isValid;

    m_distracted_score_isValid = ::OpenAPI::fromJsonValue(m_distracted_score, json[QString("DistractedScore")]);
    m_distracted_score_isSet = !json[QString("DistractedScore")].isNull() && m_distracted_score_isValid;

    m_instance_id_isValid = ::OpenAPI::fromJsonValue(m_instance_id, json[QString("InstanceId")]);
    m_instance_id_isSet = !json[QString("InstanceId")].isNull() && m_instance_id_isValid;

    m_overall_score_isValid = ::OpenAPI::fromJsonValue(m_overall_score, json[QString("OverallScore")]);
    m_overall_score_isSet = !json[QString("OverallScore")].isNull() && m_overall_score_isValid;

    m_speeding_score_isValid = ::OpenAPI::fromJsonValue(m_speeding_score, json[QString("SpeedingScore")]);
    m_speeding_score_isSet = !json[QString("SpeedingScore")].isNull() && m_speeding_score_isValid;
}

QString OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::asJsonObject() const {
    QJsonObject obj;
    if (m_acceleration_score_isSet) {
        obj.insert(QString("AccelerationScore"), ::OpenAPI::toJsonValue(m_acceleration_score));
    }
    if (m_app_id_isSet) {
        obj.insert(QString("AppId"), ::OpenAPI::toJsonValue(m_app_id));
    }
    if (m_braking_score_isSet) {
        obj.insert(QString("BrakingScore"), ::OpenAPI::toJsonValue(m_braking_score));
    }
    if (m_company_id_isSet) {
        obj.insert(QString("CompanyId"), ::OpenAPI::toJsonValue(m_company_id));
    }
    if (m_cornering_score_isSet) {
        obj.insert(QString("CorneringScore"), ::OpenAPI::toJsonValue(m_cornering_score));
    }
    if (m_device_token_isSet) {
        obj.insert(QString("DeviceToken"), ::OpenAPI::toJsonValue(m_device_token));
    }
    if (m_distracted_score_isSet) {
        obj.insert(QString("DistractedScore"), ::OpenAPI::toJsonValue(m_distracted_score));
    }
    if (m_instance_id_isSet) {
        obj.insert(QString("InstanceId"), ::OpenAPI::toJsonValue(m_instance_id));
    }
    if (m_overall_score_isSet) {
        obj.insert(QString("OverallScore"), ::OpenAPI::toJsonValue(m_overall_score));
    }
    if (m_speeding_score_isSet) {
        obj.insert(QString("SpeedingScore"), ::OpenAPI::toJsonValue(m_speeding_score));
    }
    return obj;
}

double OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::getAccelerationScore() const {
    return m_acceleration_score;
}
void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::setAccelerationScore(const double &acceleration_score) {
    m_acceleration_score = acceleration_score;
    m_acceleration_score_isSet = true;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_acceleration_score_Set() const{
    return m_acceleration_score_isSet;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_acceleration_score_Valid() const{
    return m_acceleration_score_isValid;
}

QString OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::getAppId() const {
    return m_app_id;
}
void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::setAppId(const QString &app_id) {
    m_app_id = app_id;
    m_app_id_isSet = true;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_app_id_Set() const{
    return m_app_id_isSet;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_app_id_Valid() const{
    return m_app_id_isValid;
}

double OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::getBrakingScore() const {
    return m_braking_score;
}
void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::setBrakingScore(const double &braking_score) {
    m_braking_score = braking_score;
    m_braking_score_isSet = true;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_braking_score_Set() const{
    return m_braking_score_isSet;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_braking_score_Valid() const{
    return m_braking_score_isValid;
}

QString OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::getCompanyId() const {
    return m_company_id;
}
void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::setCompanyId(const QString &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_company_id_Valid() const{
    return m_company_id_isValid;
}

double OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::getCorneringScore() const {
    return m_cornering_score;
}
void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::setCorneringScore(const double &cornering_score) {
    m_cornering_score = cornering_score;
    m_cornering_score_isSet = true;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_cornering_score_Set() const{
    return m_cornering_score_isSet;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_cornering_score_Valid() const{
    return m_cornering_score_isValid;
}

QString OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::getDeviceToken() const {
    return m_device_token;
}
void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::setDeviceToken(const QString &device_token) {
    m_device_token = device_token;
    m_device_token_isSet = true;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_device_token_Set() const{
    return m_device_token_isSet;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_device_token_Valid() const{
    return m_device_token_isValid;
}

double OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::getDistractedScore() const {
    return m_distracted_score;
}
void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::setDistractedScore(const double &distracted_score) {
    m_distracted_score = distracted_score;
    m_distracted_score_isSet = true;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_distracted_score_Set() const{
    return m_distracted_score_isSet;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_distracted_score_Valid() const{
    return m_distracted_score_isValid;
}

QString OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::getInstanceId() const {
    return m_instance_id;
}
void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::setInstanceId(const QString &instance_id) {
    m_instance_id = instance_id;
    m_instance_id_isSet = true;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_instance_id_Set() const{
    return m_instance_id_isSet;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_instance_id_Valid() const{
    return m_instance_id_isValid;
}

double OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::getOverallScore() const {
    return m_overall_score;
}
void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::setOverallScore(const double &overall_score) {
    m_overall_score = overall_score;
    m_overall_score_isSet = true;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_overall_score_Set() const{
    return m_overall_score_isSet;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_overall_score_Valid() const{
    return m_overall_score_isValid;
}

double OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::getSpeedingScore() const {
    return m_speeding_score;
}
void OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::setSpeedingScore(const double &speeding_score) {
    m_speeding_score = speeding_score;
    m_speeding_score_isSet = true;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_speeding_score_Set() const{
    return m_speeding_score_isSet;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::is_speeding_score_Valid() const{
    return m_speeding_score_isValid;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_acceleration_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_app_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_braking_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cornering_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_device_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_distracted_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_instance_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_overall_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_speeding_score_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUserSafeScoringAccumulatedValueV1_scorings_individual_200_response_Result::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
