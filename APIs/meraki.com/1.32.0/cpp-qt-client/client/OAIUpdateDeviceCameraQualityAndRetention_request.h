/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIUpdateDeviceCameraQualityAndRetention_request.h
 *
 * 
 */

#ifndef OAIUpdateDeviceCameraQualityAndRetention_request_H
#define OAIUpdateDeviceCameraQualityAndRetention_request_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIUpdateDeviceCameraQualityAndRetention_request : public OAIObject {
public:
    OAIUpdateDeviceCameraQualityAndRetention_request();
    OAIUpdateDeviceCameraQualityAndRetention_request(QString json);
    ~OAIUpdateDeviceCameraQualityAndRetention_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isAudioRecordingEnabled() const;
    void setAudioRecordingEnabled(const bool &audio_recording_enabled);
    bool is_audio_recording_enabled_Set() const;
    bool is_audio_recording_enabled_Valid() const;

    bool isMotionBasedRetentionEnabled() const;
    void setMotionBasedRetentionEnabled(const bool &motion_based_retention_enabled);
    bool is_motion_based_retention_enabled_Set() const;
    bool is_motion_based_retention_enabled_Valid() const;

    qint32 getMotionDetectorVersion() const;
    void setMotionDetectorVersion(const qint32 &motion_detector_version);
    bool is_motion_detector_version_Set() const;
    bool is_motion_detector_version_Valid() const;

    QString getProfileId() const;
    void setProfileId(const QString &profile_id);
    bool is_profile_id_Set() const;
    bool is_profile_id_Valid() const;

    QString getQuality() const;
    void setQuality(const QString &quality);
    bool is_quality_Set() const;
    bool is_quality_Valid() const;

    QString getResolution() const;
    void setResolution(const QString &resolution);
    bool is_resolution_Set() const;
    bool is_resolution_Valid() const;

    bool isRestrictedBandwidthModeEnabled() const;
    void setRestrictedBandwidthModeEnabled(const bool &restricted_bandwidth_mode_enabled);
    bool is_restricted_bandwidth_mode_enabled_Set() const;
    bool is_restricted_bandwidth_mode_enabled_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_audio_recording_enabled;
    bool m_audio_recording_enabled_isSet;
    bool m_audio_recording_enabled_isValid;

    bool m_motion_based_retention_enabled;
    bool m_motion_based_retention_enabled_isSet;
    bool m_motion_based_retention_enabled_isValid;

    qint32 m_motion_detector_version;
    bool m_motion_detector_version_isSet;
    bool m_motion_detector_version_isValid;

    QString m_profile_id;
    bool m_profile_id_isSet;
    bool m_profile_id_isValid;

    QString m_quality;
    bool m_quality_isSet;
    bool m_quality_isValid;

    QString m_resolution;
    bool m_resolution_isSet;
    bool m_resolution_isValid;

    bool m_restricted_bandwidth_mode_enabled;
    bool m_restricted_bandwidth_mode_enabled_isSet;
    bool m_restricted_bandwidth_mode_enabled_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdateDeviceCameraQualityAndRetention_request)

#endif // OAIUpdateDeviceCameraQualityAndRetention_request_H
